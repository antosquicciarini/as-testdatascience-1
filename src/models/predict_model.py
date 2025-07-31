from sklearn.metrics import (
    accuracy_score,
    f1_score,
    recall_score,
    confusion_matrix,
    classification_report
)
from imblearn.metrics import geometric_mean_score
import numpy as np


def evaluate_models(trained_models, X_test, y_test):
    results = []

    for name, model in trained_models.items():
        print(f"\n📌 Evaluating {name}")
        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average="weighted")
        recall = recall_score(y_test, y_pred, average=None, zero_division=0)

        cm = confusion_matrix(y_test, y_pred)
        specificity = []
        for i in range(len(cm)):
            tn = cm.sum() - (cm[i, :].sum() + cm[:, i].sum() - cm[i, i])
            fp = cm[:, i].sum() - cm[i, i]
            specificity.append(tn / (tn + fp) if (tn + fp) > 0 else 0)

        gmean = geometric_mean_score(y_test, y_pred, average='macro')

        print(classification_report(y_test, y_pred, zero_division=0))

        results.append({
            "Model": name,
            "Accuracy": acc,
            "F1 Score": f1,
            "G-Mean": gmean,
            "Recall (macro avg)": recall.mean(),
            "Specificity (macro avg)": np.mean(specificity)
        })

    return results
