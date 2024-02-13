from sklearn.ensemble import RandomForestClassifier
def build_model():
        """Builds and returns the tuned RandomForestClassifier."""
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    return model
