from parser import load_logs, extract_commands, detect_failed_logins
from collections import defaultdict
from parser import load_logs, extract_commands
from analyzer import predict_attack, risk_level

logs = load_logs("logs/cowrie.json")
failed_logins = detect_failed_logins(logs)
commands = extract_commands(logs)

print("\n=== AI Attack Analysis ===\n")

ip_attacks = defaultdict(list)
for entry in commands:
    attack = predict_attack(entry["command"])
    ip_attacks[entry["ip"]].append(attack)
    risk = risk_level(attack)

    print(f"IP: {entry['ip']}")
    print(f"Command: {entry['command']}")
    print(f"AI Prediction: {attack}")
    print(f"Risk Level: {risk}")
    print("-" * 40)
    print("\n=== Attacker Profiling ===\n")

for ip, attacks in ip_attacks.items():
    print(f"IP: {ip}")
    print(f"Total Attacks: {len(attacks)}")
    print(f"Attack Types: {set(attacks)}")

    if len(attacks) > 2:
        print("Threat Level: HIGH")
    else:
        print("Threat Level: LOW")

    print("-" * 40)
from collections import Counter

print("\n=== Brute Force Detection ===\n")

login_counts = Counter(failed_logins)

for ip, count in login_counts.items():
    if count > 3:
        print(f"{ip} → Possible Brute Force Attack ({count} failed attempts)")
