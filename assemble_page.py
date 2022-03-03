# coding=utf-8

# ----------------
# 组装页面
# author：sbin
# date：2022-03-03
# ----------------

import util
import os
import json


# 组装js文件
def assemble_js_file(config):
    data_str = ""
    func_str = ""
    # 组装json配置
    for item in config:
        if item == 'data':  # 拼接data对象
            data_config = config[item].values()
            for i in data_config:
                if i:
                    data_str += ": ".join(i.values()) + ",\n    "
        elif item == "life_circle" or item == "method":  # 拼接生命周期函数和方法
            if item == "life_circle" and len(config[item]) > 0:
                func_str += "pageLifetimes: {\n"
            circle_config = config[item].values()
            for c_item in circle_config:
                for k in c_item:
                    if k['name'] != "":
                        if k['note'] != "":
                            func_str += "// " + k['note'] + "\n"
                        func_str += k['name'] + "("
                        if k['params']:
                            func_str += ", ".join(k['params'])
                        func_str += "){\n  "
                        func_str += "\n  ".join(k['body']) + "\n"
                        func_str += "},\n\n"
            if item == "life_circle" and len(config[item]) > 0:
                func_str += "},\n"
    # 拼接文件
    content = "const app = getApp()\n\nPage({\n  data:{\n    "
    content += data_str.rstrip(",\n    ")
    content += "\n  },\n\n"
    content += func_str
    content += "})\n"

    return content


# 组装json文件
def assemble_json_file(config):
    json_str = ""
    # 组装json配置
    for item in config:
        json_config = config[item].values()
        json_str += ": ".join(json_config) + ",\n    "
    # 拼接文件
    content = "{\n  \"usingComponents\": {\n    "
    if json_str != "":
        content += json_str.rstrip(",\n    ")
    content += "\n  }"
    content += "\n}"

    return content


# 组装wxml文件
def assemble_wxml_file(config):
    wxml_str = ""
    # 组装json配置
    for item in config:
        for tag in config[item]:
            wxml_str += tag + "\n  "
    # 拼接文件
    content = "<view>\n  "
    content += wxml_str.rstrip()
    content += "\n</view>"

    return content


# 组装wxss文件
def assemble_wxss_file(config):
    wxss_str = ""
    for item in config:
        wxss_str += item + "{\n  "
        wxss_str += ";\n  ".join(config[item])
        wxss_str += "\n}".rstrip()
    return wxss_str


# 创建页面
def create_page(page_config):
    # 拼接文件
    js_content = ""
    json_content = ""
    wxml_content = ""
    wxss_content = ""
    for item in page_config:
        if item == "js":  # index.js
            js_content = assemble_js_file(page_config[item])
        elif item == "json":  # index.json
            json_content = assemble_json_file(page_config[item])
        elif item == "wxml":  # index.wxml
            wxml_content = assemble_wxml_file(page_config[item])
        elif item == "wxss":  # index.wxss
            wxss_content = assemble_wxss_file(page_config[item])

    return {
        "js": js_content,
        "json": json_content,
        "wxml": wxml_content,
        "wxss": wxss_content
    }


# 添加小程序页面
def add_page(project_path, name, contents):
    # 创建文件夹
    path = project_path + "pages/"
    os.makedirs(path + name)
    # 创建文件
    with open(path + name + '/index.js', 'w', encoding='utf8') as fp:
        fp.write(contents["js"])
    with open(path + name + '/index.json', 'w', encoding='utf8') as fp:
        fp.write(contents["json"])
    with open(path + name + '/index.wxml', 'w', encoding='utf8') as fp:
        fp.write(contents["wxml"])
    with open(path + name + '/index.wxss', 'w', encoding='utf8') as fp:
        fp.write(contents["wxss"])
    # app.json写入新增的页面
    with open(project_path + 'app.json', 'r', encoding='utf8') as fp:
        app_json_string = json.load(fp)
    app_json_string['pages'].append("pages/" + name + '/index')
    with open(project_path + 'app.json', 'w', encoding='utf8') as fp:
        json.dump(app_json_string, fp, ensure_ascii=False, indent=2)
