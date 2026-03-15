import re
def classify_text(text):
    patterns = {
        "system_complexity": r"^(Backup (started|ended) at \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.|Backup completed successfully\.|File .* uploaded successfully by user\d+|System reboot initiated by user User\d+|System updated to version \d+\.\d+\.\d+|Disk cleanup completed successfully)\.?$",
        "user_action": r"^(Account with ID \d+ created by User\d+|User User\d+ logged (in|out))"

    }

    for label, pattern in patterns.items():
        if re.match(pattern, text):
            return label

    return "Unknown"


# Test examples
samples = [
    "test@example.com",
    "File data_9318.csv uploaded successfully by user234",
    "Disk cleanup completed successfully.",
    "Backup started at 2025-05-14 07:06:55.",
    "User User429 logged out"
]

for sample in samples:
    print(f"{sample} → {classify_text(sample)}")