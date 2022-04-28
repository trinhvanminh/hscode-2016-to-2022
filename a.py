import os

path = '.'

directory_contents = os.listdir(path)
for item in directory_contents:
    if os.path.isdir(item):
        print(item)
