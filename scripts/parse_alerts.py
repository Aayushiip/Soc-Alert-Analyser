import csv

failed_logins = 0

with open("alerts/sample_log1.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['event_type'] == 'failed_login':
            failed_logins += 1

print(f"Total failed login attempts: {failed_logins}")
