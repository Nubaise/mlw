import os
import pickle
import numpy as np
from src.features import extract_features

MODEL_PATH = "models/lgbm_ember2018.pkl"


def predict(file_path: str) -> None:
    if not os.path.exists(file_path):
        print(f"[ERROR] File not found: {file_path}")
        return

    if not os.path.exists(MODEL_PATH):
        print(f"[ERROR] Model not found at {MODEL_PATH}. Run train.py first.")
        return

    print(f"[*] Scanning: {file_path}")
    features = extract_features(file_path)

    if features is None:
        print("[ERROR] Could not extract features from file.")
        return

    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    prob = model.predict_proba([features])[0][1]
    verdict = "MALWARE" if prob >= 0.5 else "BENIGN"
    confidence = prob if verdict == "MALWARE" else 1 - prob

    print(f"[*] Verdict    : {verdict}")
    print(f"[*] Confidence : {confidence * 100:.1f}%")
    print(f"[*] Raw Score  : {prob:.4f}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m src.predict <path_to_exe>")
    else:
        predict(sys.argv[1])