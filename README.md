# AS-TestDataScience-1

**Multiclass classification of forest cover types** using the [Forest CoverType dataset (UCI)](https://archive.ics.uci.edu/dataset/31/covertype).  
This project includes:

- 📊 Exploratory Data Analysis (EDA)
- ⚙️ Feature engineering and preprocessing
- 🧠 Model training and evaluation across multiple classifiers
- 🔍 Dimensionality reduction for visualization
- 📈 Performance comparison based on Accuracy, F1 Score, G-Mean, Recall, and Specificity

The project is fully structured, reproducible, and built for experimentation and documentation via Sphinx.

---

## 📁 Project Structure

```
├── LICENSE             <- MIT License.
├── Makefile            <- Reproducible commands: make data, make train, etc.
├── README.md           <- Project overview and instructions.
├── models/             <- Trained models (.pth) and their training curves.
├── notebooks/          <- Jupyter notebooks for analysis and training.
├── reports/            <- Final reports and figures.
├── requirements.txt    <- Python dependencies.
├── setup.py            <- Installation script (`pip install -e .`)
├── src/                <- All source code (data prep, features, models, viz).
└── tox.ini             <- Linting rules.
```
---

## 📊 Dataset

**Forest CoverType** ([UCI Repository](https://archive.ics.uci.edu/dataset/31/covertype)):

- **Samples:** 581,012 forest observations
- **Features:** 54 attributes (10 quantitative, 44 binary)
- **Target:** Forest cover type (7 classes)
- **Notes:** Clean dataset, but highly imbalanced classes

---

## 🧹 Pipeline Overview

1. **Exploratory Data Analysis**
   - Target distribution plots
   - Correlation heatmaps
   - PCA and t-SNE visualization

2. **Preprocessing**
   - Feature scaling (StandardScaler)
   - Train-test split with stratification
   - Class imbalance analysis

3. **Model Training**
   - Random Forest
   - Logistic Regression
   - Gradient Boosting
   - Optional: Neural Network classifiers

4. **Evaluation**
   - Metrics: Accuracy, F1 Score, G-Mean, Recall, Specificity
   - Confusion matrices
   - Visual performance comparisons

---

## 🔧 Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/antosquicciarini/as-testdatascience-1.git
    cd as-testdatascience-1
    ```

2. **Create and activate environment** (automated via `make`):
   ```bash
   make create_environment
   ```

   If conda is available, then 
   ```bash
   conda activate as-testdatascience-1
   ```
   otherwise use virtual envirorment

3. **Install dependencies**:
   ```bash
   make requirements
   ```

4. **Validate environment setup**:
   ```bash
   make test_environment
   ```

5. **Run training**:
   run notebooks/energy_prediction.ipynb via Jupyter

---

## 🧪 Testing Your Environment

Run:

```bash
python test_environment.py
```

to confirm your Python version is compatible.

---

## 🧪 Testing & Code Quality

To ensure the code follows Python PEP8 style guidelines, you can run:

```bash
make lint
```
---

## ⚙️ DevOps Readiness

- Project structured with automation via Makefile
- Environment reproducibility via requirements.txt and setup.py
- Linting, testing, and documentation support (tox, flake8, Sphinx)
- Models saved and ready for deployment in production systems

---

## 📜 License

This project is licensed under the **MIT License**. See `LICENSE` for full details.

---

<p><small>Project scaffolded with <a href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science</a>.</small></p>