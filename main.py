#coding=utf-8

import os
import shutil
from jinja2 import Template
import util
import assemble_tabbar
import assemble_page


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
# def create_project(project_name):
#     project_path = service_path + project_name
#     if not os.path.exists(project_path):
#         os.makedirs(project_path)
#     shutil.copytree(os.path.abspath(base_template_path), project_path)
#     return project_path

# 添加组件
# def add_component(component_name, project_path):
#     source_custom_tabbar_path = os.path.abspath(base_components_path + '/' + component_name)
#     target_project_path = os.path.abspath(project_path + '/' + component_name)
#     component_path = base_components_path + '/' + component_name
#     # if not os.path.exists(component_path):
#     #     print(component_name + '组件不存在')
#     shutil.copytree(source_custom_tabbar_path, target_project_path)
#     print('添加' + component_name + '组件成功')

def add_custom_tabbar():
    # 指定页面（app.json、custom-tab-bar/index.js）
    # 指定图标
    # 添加全局变量
    # 配置app.json 测试时去掉 "lazyCodeLoading": "requiredComponents"
    print('自定义tabBar成功')


def assemble_pages(project_path, project_config):
    pages = project_config["pages"].keys()
    for page in pages:
        page_contents = assemble_page.create_page(project_config["pages"][page])
        assemble_page.add_page(project_path, page, page_contents)


if __name__ == "__main__":
    # project_path = create_project('test_template')
    # project_path = service_path + '/test_template'
    # shutil.copytree(os.path.abspath(base_template_path), os.path.abspath(project_path))
    # add_component('custom-tab-bar', service_path + '/test_template')

    project_name = "202203020925"
    # 创建项目文件夹
    project_path = util.init_project(project_name)
    # 读取配置
    project_config = util.load_config()
    # 复制组件文件
    util.add_components(project_config["components"], project_path)
    # tabBar,更新配置文件
    tabbar_config = project_config['tabBar']
    tabbar_custom_config = tabbar_config['customConfig']
    # 填充app.js
    assemble_tabbar.app_js_template(project_name, "{\n        userInfo: null, \n        selectedIndex: 0\n  }")
    # 填充custom-tab-bar/index.js
    assemble_tabbar.tabbar_index_template(project_name, tabbar_custom_config)
    # 填充app_json
    assemble_tabbar.app_json_template(project_name, tabbar_config)
    # 组装页面文件
    assemble_pages(project_path, project_config)
    # 压缩文件夹
    # 输出压缩包