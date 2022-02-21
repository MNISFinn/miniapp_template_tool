# coding=utf-8

# ----------------
# 组装index页面
# author：sbin
# date：2022-02-17
# ----------------

import util
import json
import os

# 加载配置文件
def load_config():
    with open(util.component_config_path, 'r', encoding='utf8') as fp:
        app_json_string = json.load(fp)
    return app_json_string

# 创建页面
def create_page():
    util.create_page(util.test_template_pages_path, 'index1')

def add_search_bar():
    print('添加searchBar组件成功')

if __name__ == "__main__":
    # create_page()
    print('创建成功！')