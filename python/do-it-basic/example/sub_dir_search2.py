# sub_dir_search2.py
import os

for (path, dir, files) in os.walk("/Users/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == ".py":
            print(f"{path}/{filename}")