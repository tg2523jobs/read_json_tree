# -*- encoding=utf-8 -*-

import os
import json

root_path = os.getcwd() + "/"
tree_files = root_path + "tree.json"

with open(tree_files, "r") as f:
    tree_data = json.load(f)


def loop_file(NODE_DATA, LEVEL_INDEX = 0):
    level_index = LEVEL_INDEX
    node_data = NODE_DATA

    for node in node_data:
        print(node)

print(tree_data["project_id"])

loop_file(tree_data["file_version"])
