# Model Training & Evaluation

## 🤖 Models Used

- Logistic Regression (standard & balanced)
- Random Forest (standard & balanced)
- K-Nearest Neighbors
- LinearSVC (standard & balanced)
- Support Vector Machine (RBF kernel)
- XGBoost
- Naive Bayes

---

## ⚙️ Training Pipeline

- All models trained on standardized numerical + binary features
- Evaluated on stratified test split (20%)
- Key metrics:
  - Accuracy
  - F1 Score (weighted)
  - G-Mean
  - Macro Recall
  - Macro Specificity

---

## 🏆 Performance Summary

| Model                     | Accuracy | F1 Score | G-Mean | Recall | Specificity |
|--------------------------|----------|----------|--------|--------|-------------|
| Random Forest (Balanced) | 0.96     | 0.96     | 0.95   | 0.95   | 0.95        |
| Random Forest            | 0.96     | 0.96     | 0.95   | 0.94   | 0.95        |
| K-Nearest Neighbors      | 0.93     | 0.93     | 0.92   | 0.92   | 0.91        |
| XGBoost                  | 0.87     | 0.87     | 0.90   | 0.87   | 0.89        |
| Logistic Regression      | 0.73     | 0.72     | 0.69   | 0.70   | 0.68        |
| LinearSVC                | 0.71     | 0.70     | 0.65   | 0.69   | 0.63        |

> 📌 For full confusion matrices, training code, and evaluation plots, see `notebooks/covertype.ipynb`.

---

## ✅ Conclusion

Tree-based models (especially Random Forest) offer the best trade-off between accuracy and class balance, making them ideal for this task.