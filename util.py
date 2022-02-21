# coding=utf-8

# ----------------
# 基础工具方法
# author：sbin
# date：2022-02-01
# ----------------

import os
import json

# 模版配置文件
component_config_path = '/Users/shaobin/WeChatProjects/base_components/template_config.json'
# 基础模板组件路径
base_components_path = '/Users/shaobin/WeChatProjects/base_components/'
# 基础模板路径
base_template_path = '/Users/shaobin/WeChatProjects/base_template/'
# 测试模板路径
test_template_path = '/Users/shaobin/WeChatProjects/test_template/'
# 测试模板组件路径
test_template_pages_path = '/Users/shaobin/WeChatProjects/test_template/pages/'

# 写入指定文件
def append_content(file_path, content):
    handle = open(file_path, 'w')
    handle.write(content)
    handle.close()

# 创建指定页面
def create_page(path, name):
    # 创建文件夹
    os.mkdir(path + name)
    # 创建文件
    open(path+name+'/index.js', 'a').close()
    open(path+name+'/index.wxml', 'a').close()
    open(path+name+'/index.wxss', 'a').close()
    # json文件写入配置，不能为空
    with open(path+name+'/index.json', 'w', encoding='utf8') as fp:
        fp.write("{\n  \"usingComponents\": {}\n}")
    # app.json写入新增的页面
    with open(test_template_path+'app.json', 'r', encoding='utf8') as fp:
        app_json_string = json.load(fp)
    app_json_string['pages'].append("pages/"+name+'/index')
    with open(test_template_path+'app_test.json', 'w', encoding='utf8') as fp:
        json.dump(app_json_string, fp, ensure_ascii=False, indent=2)
