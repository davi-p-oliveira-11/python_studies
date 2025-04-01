from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
  with open(ROOT_PATH / "lorem.txt", "r") as file:
    print(file.read())
except IOError as exc:
  print(f"Error opening the file {exc}")

#try:
#  with open(ROOT_PATH / "file-utf-8.txt", "w", encoding="utf-8") as file:
#    file.write("Learning to manipulate files using Python.")
#except IOError as exc:
#  print(f"Error on opening file.")

try:
  with open(ROOT_PATH / "arquivo-utf-8", "r", encoding="utf-8") as file:
    print(file.read())
except IOError as exc:
  print(f"Error on opening the file {exc}")
except UnicodeDecodeError as exc:
  print(exc)