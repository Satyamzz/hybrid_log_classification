import re
def classify_text(text):
    patterns = {
        "system_complexity-backup":"^Backup (started|ended) at \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.|^Backup completed successfully\.$"
    }

    for label, pattern in patterns.items():
        if re.match(pattern, text):
            return label

    return "Unknown"


# Test examples
samples = [
    "test@example.com",
    "+1-800-555-1234",
    "https://www.google.com",
    "Hello world"
]

for sample in samples:
    print(f"{sample} → {classify_text(sample)}")