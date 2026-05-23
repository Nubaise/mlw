# mlw

Static malware detection for Windows PE files using machine learning.
No execution, no sandbox. Just the file.

## What it does

Parses a PE file, extracts a 2381-dimensional feature vector using EMBER v2,
and runs it through a LightGBM classifier to predict whether the file is malware or benign.

## Feature breakdown

| Category          | Dimensions |
| ----------------- | ---------- |
| Byte Histogram    | 256        |
| Byte Entropy      | 256        |
| String Features   | 104        |
| General File Info | 10         |
| Header Features   | 62         |
| Section Features  | 255        |
| Import Features   | 1280       |
| Export Features   | 128        |
| Data Directories  | 30         |
| Total             | 2381       |

## Model performance on EMBER 2018 test set

Tested on 200,000 samples (100k benign, 100k malware).

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 0.9596 |
| Precision | 0.9540 |
| Recall    | 0.9659 |
| F1 Score  | 0.9599 |
| AUC-ROC   | 0.9920 |

## Setup

```bash
git clone https://github.com/Nubaise/mlw.git
cd mlw
py -3.10 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Dataset

Download EMBER 2018 from https://github.com/elastic/ember and extract into data/ember2018/.

Vectorize the raw features before training:

```bash
python -c "import ember; ember.create_vectorized_features('data/ember2018')"
```

## Usage

Train:

```bash
python -m src.train
```

Evaluate:

```bash
python -m src.evaluate
```

Scan a file:

```bash
python -m src.predict path/to/file.exe
```

## Stack

Python 3.10, LightGBM, EMBER v2, LIEF, scikit-learn, NumPy
