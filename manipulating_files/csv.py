import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

COLUMN_ID = 0
COLUMN_NAME = 1


try:
    with open(ROOT_PATH / "users.csv", "w", newline="", encoding="utf-8") as file:
        write = csv.writer(file)
        write.writerow(["id", "name"])
        write.writerow(["1", "Mary"])
        write.writerow(["2", "John"])
except IOError as exc:
    print(f"Error creating the file. {exc}")


try:
    with open(ROOT_PATH / "users.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            print(f"ID: {row[COLUMN_ID]}")
            print(f"Name: {row[COLUMN_NAME]}")
except IOError as exc:
    print(f"Error creating the file. {exc}")


try:
    with open(ROOT_PATH / "users.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"ID: {row['id']}")
            print(f"Name: {row['nome']}")
except IOError as exc:
    print(f"Error creating the file. {exc}")