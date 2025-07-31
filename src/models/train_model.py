def train_models(models, X_train, y_train):
    trained_models = {}
    for name, model in models.items():
        print(f"\n📌 Training {name}")
        model.fit(X_train, y_train)
        trained_models[name] = model
    return trained_models
