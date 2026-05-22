import ember
import numpy as np


def extract_features(file_path: str) -> np.ndarray:
    """
    Extract 2381-dimensional EMBER v2 feature vector from a PE file.
    Returns None if the file cannot be parsed.
    """
    try:
        with open(file_path, "rb") as f:
            bytez = f.read()
        extractor = ember.PEFeatureExtractor(feature_version=2)
        features = extractor.feature_vector(bytez)
        return np.array(features, dtype=np.float32)
    except Exception as e:
        print(f"[ERROR] Feature extraction failed for {file_path}: {e}")
        return None # type: ignore