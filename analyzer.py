import joblib
from features import extract_features

model = joblib.load("model/model.pkl")

def predict_attack(command):
    f = extract_features(command)
    feature_list = list(f.values())
    return model.predict([feature_list])[0]
def risk_level(attack):
    if attack in ["Malware", "Backdoor"]:
        return "HIGH"
    elif attack == "Download":
        return "MEDIUM"
    else:
        return "LOW"
