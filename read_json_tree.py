# -*- encoding=utf-8 -*-

import os
import json


class test_tree:
    
    def __init__(self):
        pass
    
    # get loctation path
    def setting_location_path(self):
        self.root_path = os.getcwd() + "/"
    
    # set all paths 
    def route_paths(self):
        self.tree_files = self.root_path + "tree.json"
    
    # read json file
    def read_tree(self, get_json_name):
        with open(get_json_name, "r") as f:
            get_json_dict = json.load(f)
        return get_json_dict
    
    # cell tree
    def start_tree(self):
        self.setting_location_path()
        self.route_paths()
        self.tree_data = self.read_tree(self.tree_files)
        print(self.tree_data["project_id"])
        self.loop_file(self.tree_data["file_version"])
    
    # show tree
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

# test_tree end

if __name__ == "__main__":
    my_tree = test_tree()
    my_tree.start_tree()