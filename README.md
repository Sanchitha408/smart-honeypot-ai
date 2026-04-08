# 🔥 Smart Honeypot Analyzer with AI

## 🚀 Overview

Smart Honeypot Analyzer is an AI-powered cybersecurity tool that analyzes honeypot logs (Cowrie) to detect, classify, and profile attacker behavior.

## 🎯 Features

* 🤖 AI-based attack classification (Malware, Backdoor, etc.)
* ⚠️ Risk scoring (High / Medium / Low)
* 🧠 Attacker profiling (IP-based analysis)
* 🔐 Brute force detection
* 📊 Log parsing and analysis

## 🛠️ Technologies Used

* Python
* scikit-learn
* Joblib

## 📂 Project Structure

```
smart-honeypot-ai/
├── logs/
├── model/
├── parser.py
├── analyzer.py
├── main.py
├── features.py
```

## ▶️ How to Run

### 1. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train model

```bash
python model/train.py
```

### 4. Run analyzer

```bash
python main.py
```

## 📊 Sample Output

```
AI Prediction: Malware
Risk Level: HIGH
```

## 🎯 Future Improvements

* Real-time attack detection
* Web dashboard (Flask)
* Threat intelligence integration

## 👩‍💻 Author

Sanchitha S
Cybersecurity Enthusiast | GSoC Aspirant
