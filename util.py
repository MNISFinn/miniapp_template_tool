# coding=utf-8

# ----------------
# 基础工具方法
# author：sbin
# date：2022-02-01
# ----------------


import os
import json
import shutil

# 服务器中项目的公共路径
service_path = '/Users/shaobin/WeChatProjects/'
# 模版配置文件
component_config_path = '/Users/shaobin/WeChatProjects/base_components/template_config.json'
# 基础模板路径
base_template_path = service_path + 'test_base_template/'
# 基础模板组件路径
base_components_path = service_path + 'base_components/'
# 测试模板路径
test_template_path = '/Users/shaobin/WeChatProjects/test_template/'
# 测试模板组件路径
test_template_pages_path = '/Users/shaobin/WeChatProjects/test_template/pages/'


# 写入指定文件
def append_content(file_path, content):
    handle = open(file_path, 'w')
    handle.write(content)
    handle.close()


# 加载配置文件
def load_config():
    with open(component_config_path, 'r', encoding='utf8') as fp:
        app_json_string = json.load(fp)
    return app_json_string


def init_project(name):
    project_path = service_path + name
    if not os.path.exists(project_path):
        shutil.copytree(os.path.abspath(base_template_path), project_path)
    return project_path + "/"


# 添加组件
def add_components(components, project_path):
    if len(components) > 0:
        for component in components:
            source_path = os.path.abspath(base_components_path + component)
            # 自定义的tabBar是直接放在项目根目录的，其余自定义组件统一放到components目录
            if component == "custom-tab-bar":
                target_project_path = os.path.abspath(project_path + component)
            else:
                target_project_path = os.path.abspath(project_path + "components/" + component)
            shutil.copytree(source_path, target_project_path)
            print('添加' + component + '组件成功')
