#coding=utf-8

import os
import shutil
from jinja2 import Template
import assemble_tabbar


# 服务器中项目的公共路径
service_path = '/Users/shaobin/WeChatProjects/'
# 基础组件路径
base_components_path = service_path + 'base_components'
base_template_path = service_path + 'base_template'
# 生成的项目文件夹路径
target_project = service_path + 'test_template'
target_path = os.path.abspath(service_path + 'test_template')
# target_components_path = os.path.abspath(service_path + 'test_template/components')

if not os.path.exists(base_components_path):
    print('基础模版不存在')

# 新增文件夹
def create_project(project_name):
    print(1)
    project_path = service_path + '/' + project_name
    if not os.path.exists(project_path):
        os.makedirs(project_path)
    shutil.copytree(os.path.abspath(base_template_path), project_path)
    return project_path

# 添加组件
def add_component(component_name, project_path):
    source_custom_tabbar_path = os.path.abspath(base_components_path + '/' + component_name)
    target_project_path = os.path.abspath(project_path + '/' + component_name)
    component_path = base_components_path + '/' + component_name
    # if not os.path.exists(component_path):
    #     print(component_name + '组件不存在')
    shutil.copytree(source_custom_tabbar_path, target_project_path)
    print('添加' + component_name + '组件成功')

def add_custom_tabbar():
    # 指定页面（app.json、custom-tab-bar/index.js）
    # 指定图标
    # 添加全局变量
    # 配置app.json 测试时去掉 "lazyCodeLoading": "requiredComponents"
    print('自定义tabBar成功')

if __name__ == "__main__":
    # project_path = create_project('test_template')
    project_path = service_path + '/test_template'
    shutil.copytree(os.path.abspath(base_template_path), os.path.abspath(project_path))
    add_component('custom-tab-bar', service_path + '/test_template')