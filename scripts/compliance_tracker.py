import csv

with open("alerts/compliance_checklist.csv") as f:
    reader = csv.DictReader(f)
    print("Compliance Checklist Status:")
    for row in reader:
        print(f"{row['task']} - {row['status']}")
