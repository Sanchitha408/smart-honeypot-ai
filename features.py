def extract_features(command):
    return {
        "has_wget": int("wget" in command),
        "has_curl": int("curl" in command),
        "has_chmod": int("chmod" in command),
        "has_nc": int("nc" in command or "netcat" in command),
        "length": len(command)
    }
