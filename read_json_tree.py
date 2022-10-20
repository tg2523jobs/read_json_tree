# -*- encoding=utf-8 -*-

import os
import json


class test_tree:
    
    def __init__(self):
        pass
        
    def setting_location_path(self):
        self.root_path = os.getcwd() + "/"
    
    def route_paths(self):
        self.tree_files = self.root_path + "tree.json"
        
    def read_tree(self):
        with open(self.tree_files, "r") as f:
            self.tree_data = json.load(f)
    
    def start_tree(self):
        self.setting_location_path()
        self.route_paths()
        self.read_tree()
        print(self.tree_data["project_id"])
        self.loop_file(self.tree_data["file_version"])

    def loop_file(self, NODE_DATA, LEVEL_INDEX = 0):
        level_index = LEVEL_INDEX
        node_data = NODE_DATA

        for node in node_data:
            # print(node)
            for node_inside in node:
                add_head = ""
                if level_index > 0:
                    add_head = "|   "
                print("%s|-->%s" % (add_head * level_index, node_inside))
                if node[node_inside]["filetype"] == "file":
                    if node[node_inside]["project_version"].upper() == "YES":
                        if "now_version" in node[node_inside]:
                            print("|   %s|-->now version:%s" % (add_head * level_index, node[node_inside]["now_version"]))
                        if "now_version" in node[node_inside]:
                            print("|   %s|-->new version:%s" % (add_head * level_index, node[node_inside]["now_version"]))
                elif node[node_inside]["filetype"] == "dir":
                    level_index += 1
                    loop_file(node[node_inside]["children"], level_index)
                    level_index -= 1

# end