import os
import pickle
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from Career_Navigator import TRAINING_DATA, ALL_SKILLS

X = pd.DataFrame([
    {s: int(s in skills) for s in ALL_SKILLS}
    for skills, career in TRAINING_DATA
])

y = [career for skills, career in TRAINING_DATA]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

print("Model Accuracy:", round(accuracy_score(
    y_test, model.predict(X_test)
) * 100, 2), "%")

os.makedirs("models", exist_ok=True)

with open("models/career_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/features.pkl", "wb") as f:
    pickle.dump(ALL_SKILLS, f)

print("Model saved successfully!")
