from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
  file = open(ROOT_PATH / "new-directory" / "new.txt", "r")
except FileNotFoundError as exc:
  print("File not found !")
  print(exc)
except IsADirectoryError as exc:
  print(f"It was not possible to open the file: {exc}")
except IOError as exc:
  print(f"There was an error while opening the file: {exc}")
except Exception as exc:
  print(f"There was a problem while opening the file: {exc}")


#try:
#  file = open(ROOT_PATH / "new-directory")
#except IsADirectoryError as exc:
#  print(f"It was not possible to open the file: {exc}")