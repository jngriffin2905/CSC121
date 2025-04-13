from pathlib import Path

path = Path('Chapter_10\Practice\pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)

# Accessing a files lines

from pathlib import Path

path = Path('Chapter_10\Practice\pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)