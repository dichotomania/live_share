import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
print(os.path.join(BASE_DIR, 'html'))
print("test")

a, b, c = "1", "2", "3"

print(a + b + c)

print(eval(a+b+c))