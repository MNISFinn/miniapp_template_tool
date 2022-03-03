# coding=utf-8

# ----------------
# 组装tabBar
# author：sbin
# date：2022-02-01
# ----------------
import os
import shutil
from jinja2 import Template
import util
import json


# 编辑app.js文件
def app_js_template(project_name, pages_data):
    template_string = "// app.js\n" \
                      "App({\n  " \
                      "onLaunch() { \n    " \
                      "// 展示本地存储能力\n    " \
                      "const logs = wx.getStorageSync('logs') || []\n    " \
                      "logs.unshift(Date.now())\n    " \
                      "wx.setStorageSync('logs', logs)\n\n    " \
                      "// 登录\n    " \
                      "wx.login({\n      " \
                      "success: res => {\n        " \
                      "// 发送 res.code 到后台换取 openId, sessionKey, unionId\n      " \
                      "}\n    })\n  },\n  " \
                      "globalData: " \
                      "{{pages_data}}\n" \
                      "})"
    app_json_temp = Template(template_string)
    content = Template.render(app_json_temp, pages_data=pages_data)

    util.append_content(util.service_path+project_name+'/app.js', content)


def tabbar_index_template(project_name, custom_config):
    # 组装数据，路径加上斜杠
    pages_list = []
    for page in custom_config['pages']:
        temp_page = {
            'pagePath': '/' + page['pagePath'],
            'iconPath': '/' + page['iconPath'],
            'selectedIconPath': '/' + page['selectedIconPath'],
            'text': page['text'],
        }
        pages_list.append(temp_page)
    data = {
        'selectedNumber': custom_config['selectedNumber'],
        'color': custom_config['color'],
        'selectedColor': custom_config['selectedColor'],
        'list': pages_list
    }
    # 定义并填充模板
    template_string = "// custom-tab-bar/index.js\n" \
                      "const app = getApp()\n\n" \
                      "Component({\n\n  " \
                      "data: {\n    " \
                      "selected: {{data.selectedNumber}},\n    " \
                      "color: '{{data.color}}',\n    " \
                      "selectedColor: '{{data.selectedColor}}',\n    " \
                      "list: ["
    for item in data['list']:
        template_string += "{\n      pagePath: '" + item['pagePath'] + "',\n      "
        template_string += "iconPath: '" + item['iconPath'] + "',\n      "
        template_string += "selectedIconPath: '" + item['selectedIconPath'] + "',\n      "
        template_string += "text: '" + item['text'] + "'\n    },"
    template_string = template_string.rstrip(',')
    template_string += "]\n  " \
                       "},\n  " \
                       "ready:function(){\n    " \
                       "this.setData({\n    " \
                       "selected: app.globalData.selectedIndex\n    " \
                       "})\n  },\n\n  " \
                       "methods:{\n    " \
                       "switchTab(e) {\n      " \
                       "const data = e.currentTarget.dataset\n      " \
                       "app.globalData.selectedIndex = data.index;\n      " \
                       "const url = data.path\n      " \
                       "wx.switchTab({url})\n    " \
                       "}\n  }\n})"
    tabbar_index_temp = Template(template_string)
    content = Template.render(tabbar_index_temp, data=data)
    util.append_content(util.service_path+project_name+'/custom-tab-bar/index.js', content)


# 修改app.json文件
def app_json_template(project_name, tabbar_config):
    custom_config = tabbar_config['customConfig']
    custom_tabbar_data = {
        "show": tabbar_config['isShow'],
        "custom": tabbar_config['isCustom'],
        'color': custom_config['color'],
        'selectedColor': custom_config['selectedColor'],
        "borderStyle": custom_config['borderStyle'],
        "backgroundColor": custom_config['backgroundColor'],
        'list': custom_config['pages']
    }
    if custom_tabbar_data['show']:
        with open(util.service_path+project_name+'/app.json', 'r', encoding='utf8') as fp:
            app_json_string = json.load(fp)
        app_json_string['tabBar'] = {
            "custom": custom_tabbar_data['custom'],
            "color": custom_tabbar_data['color'],
            "selectedColor": custom_tabbar_data['selectedColor'],
            "borderStyle": custom_tabbar_data['borderStyle'],
            "backgroundColor": custom_tabbar_data['backgroundColor'],
            "list": custom_tabbar_data['list']
        }
        with open(util.service_path+project_name+'/app.json', 'w', encoding='utf8') as fp:
            json.dump(app_json_string, fp, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    project_config = util.load_config()
    tabbar_config = project_config['tabBar']
    tabbar_custom_config = tabbar_config['customConfig']
    project_name = "202203020925"

    # 填充app.js
    app_js_template(project_name, "{\n        userInfo: null, \n        selectedIndex: 0\n  }")
    # 填充custom-tab-bar/index.js
    tabbar_index_template(project_name, tabbar_custom_config)
    # 填充app_json
    app_json_template(project_name, tabbar_config)
