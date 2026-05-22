import pickle
import numpy as np
from sklearn.metrics import ( # type: ignore
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
)

MODEL_PATH = "models/lgbm_ember2018.pkl"


def evaluate(X_test: np.ndarray, y_test: np.ndarray) -> None:
    print("[*] Loading model...")
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    print("[*] Running predictions...")
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    print("\n[*] Results:")
    print(f"Accuracy  : {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision : {precision_score(y_test, y_pred):.4f}")
    print(f"Recall    : {recall_score(y_test, y_pred):.4f}")
    print(f"F1 Score  : {f1_score(y_test, y_pred):.4f}")
    print(f"AUC-ROC   : {roc_auc_score(y_test, y_prob):.4f}")
    print("\n[*] Classification Report:")
    print(classification_report(y_test, y_pred, target_names=["Benign", "Malware"]))


if __name__ == "__main__":
    import ember
    DATA_DIR = "data/ember2018"
    _, _, X_test, y_test = ember.read_vectorized_features(DATA_DIR) # type: ignore
    test_mask = y_test != -1
    X_test, y_test = X_test[test_mask], y_test[test_mask] # type: ignore
    evaluate(X_test, y_test)