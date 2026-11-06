with open('./email.txt', 'r') as f:
    data = f.read().lower()

    if (
        '4u' in data or
        'for u' in data or
        'urgent' in data or
        'immediate action required' in data or
        'critical alert' in data or
        'final warning' in data or
        'account suspended' in data or
        'action required' in data or
        'security breach' in data or
        'unauthorized access' in data
    ):
        print("⚠️ Suspicious / Potential Phishing Email")

    else:
        print("Email appears legitimate")
