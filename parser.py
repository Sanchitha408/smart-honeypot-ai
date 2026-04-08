import json

def load_logs(file_path):
    logs = []
    with open(file_path, "r") as f:
        for line in f:
            try:
                logs.append(json.loads(line))
            except:
                continue
    return logs


def extract_commands(logs):
    data = []
    for log in logs:
        if log.get("eventid") == "cowrie.command.input":
            data.append({
                "ip": log.get("src_ip"),
                "command": log.get("input")
            })
    return data
def detect_failed_logins(logs):
    failed = []

    for log in logs:
        if log.get("eventid") == "cowrie.login.failed":
            failed.append(log.get("src_ip"))

    return failed
