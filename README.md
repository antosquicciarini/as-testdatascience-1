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
├── LICENSE
├── Makefile                <- Common project commands (e.g. `make data`, `make train`)
├── README.md               <- This file
├── data/                   <- Project data
│   ├── raw/                <- Original immutable data
│   ├── processed/          <- Cleaned data ready for modeling
│   ├── interim/            <- Intermediate data
│   └── external/           <- Third-party data
├── docs/                   <- Sphinx documentation
├── models/                 <- Trained models and outputs
├── notebooks/              <- Jupyter notebooks (EDA, modeling, etc.)
├── references/             <- External documentation or manuals
├── reports/                <- Generated analysis (e.g. HTML, PDF)
│   └── figures/            <- Visual assets for reports
├── requirements.txt        <- Dependencies list
├── setup.py                <- Package configuration for pip install
├── test_environment.py     <- Python version check
├── tox.ini                 <- Linting configuration
└── src/                    <- Source code
    ├── data/               <- Data processing scripts
    ├── features/           <- Feature engineering
    ├── models/             <- Training and evaluation logic
    └── visualization/      <- Visualization scripts
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/as-testdatascience-1.git
cd as-testdatascience-1
```

### 2. Set up the environment

Install in editable mode to enable direct use of the `src/` module:

```bash
pip install -e .
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Validate environment

```bash
python test_environment.py
```

---

## 🛠 Usage

### Download and prepare the data

The covertype.ipynb does not need a separate data download 

### Train models

```bash
python notebooks/covertype.ipynb
```

### Lint your code

```bash
make lint
```

---

## 📚 Documentation

Auto-generated using [Sphinx](https://www.sphinx-doc.org/).

Build docs:

```bash
cd docs
make html
```

Then open `docs/_build/html/index.html` in your browser.

---

## 🧪 Tests

While this repo doesn't include formal unit tests yet, the `test_environment.py` ensures your Python version matches project requirements. Future updates may include `pytest`-based tests for individual modules.

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Antonio Squicciarini**  
2025