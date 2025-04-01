import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

os.mkdir(ROOT_PATH / "new-directory")

file = open(ROOT_PATH / "new.txt", "w")
file.close()

os.rename(ROOT_PATH / "new.txt", ROOT_PATH / "changed.txt")

os.remove(ROOT_PATH / "changed.txt")

shutil.move(ROOT_PATH / "new.txt", ROOT_PATH / "new-directory" / "new.txt")

