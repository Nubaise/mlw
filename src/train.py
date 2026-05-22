import os
import pickle
import ember
import lightgbm as lgb
import numpy as np
from sklearn.model_selection import train_test_split # type: ignore


DATA_DIR = "data/ember2018"
MODEL_PATH = "models/lgbm_ember2018.pkl"


def train():
    print("[*] Loading EMBER dataset...")
    X_train, y_train, X_test, y_test = ember.read_vectorized_features(DATA_DIR) # type: ignore

    # Remove unlabeled samples (label == -1)
    train_mask = y_train != -1
    X_train, y_train = X_train[train_mask], y_train[train_mask] # type: ignore

    test_mask = y_test != -1
    X_test, y_test = X_test[test_mask], y_test[test_mask] # type: ignore

    print(f"[*] Training samples: {len(X_train)}")
    print(f"[*] Testing samples: {len(X_test)}")

    print("[*] Training LightGBM model...")
    model = lgb.LGBMClassifier(n_estimators=300, n_jobs=-1, verbose=-1)
    model.fit(X_train, y_train)

    os.makedirs("models", exist_ok=True)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    print(f"[*] Model saved to {MODEL_PATH}")
    return model, X_test, y_test


if __name__ == "__main__":
    train()