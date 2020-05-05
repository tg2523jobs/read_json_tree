# -*- encoding=utf-8 -*-

import json

tree_files = "tree.json"

with open(tree_files, "r") as f:
    tree_data = json.load(f)
