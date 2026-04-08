from sklearn.ensemble import RandomForestClassifier

# Sample training data (you can improve later)
X = [
    [1,0,1,0,20],  # wget + chmod
    [0,1,0,0,15],  # curl
    [0,0,0,1,10],  # nc
    [0,0,0,0,5]    # normal
]

y = [
    "Malware",
    "Download",
    "Backdoor",
    "Unknown"
]

model = RandomForestClassifier()
model.fit(X, y)

import joblib
joblib.dump(model, "model/model.pkl")
