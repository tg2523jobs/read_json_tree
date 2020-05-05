# -*- encoding=utf-8 -*-

import os
import json

root_path = os.getcwd() + "/"
tree_files = root_path + "tree.json"

with open(tree_files, "r") as f:
    tree_data = json.load(f)


print(tree_files["project_id"])
