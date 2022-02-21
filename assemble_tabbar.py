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
def app_js_template(pages_data):
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

    util.append_content('/Users/shaobin/WeChatProjects/test_template/app_test.js', content)


def tabbar_index_template(data):
    template_string = "// custom-tab-bar/index.js\n" \
                      "const app = getApp()\n\n" \
                      "Component({\n\n  " \
                      "data: {\n    " \
                      "selected: {{data.selected_number}},\n    " \
                      "color: '{{data.color}}',\n    " \
                      "selectedColor: '{{data.selected_color}}',\n    " \
                      "list: ["
    for item in data['list']:
        template_string += "{\n      pagePath: '" + item['page_path'] + "',\n      "
        template_string += "iconPath: '" + item['icon_path'] + "',\n      "
        template_string += "selectedIconPath: '" + item['selected_icon_path'] + "',\n      "
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
    util.append_content('/Users/shaobin/WeChatProjects/test_template/custom-tab-bar/index_test.js', content)


# 修改app.json文件
def app_json_template(create_flag=True, custom_flag=True, custom_tabbar_data={}):
    if create_flag:
        with open('/Users/shaobin/WeChatProjects/test_template/app.json', 'r', encoding='utf8') as fp:
            app_json_string = json.load(fp)
        app_json_string['tabBar'] = {
            "custom": custom_flag,
            "color": custom_tabbar_data['color'],
            "selectedColor": custom_tabbar_data['selectedColor'],
            "borderStyle": custom_tabbar_data['borderStyle'],
            "backgroundColor": custom_tabbar_data['backgroundColor'],
            "list": custom_tabbar_data['list']
        }
        with open('/Users/shaobin/WeChatProjects/test_template/app_test.json', 'w', encoding='utf8') as fp:
            json.dump(app_json_string, fp, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # 填充app.js
    # app_js_template("{\n        userInfo: null, \n        selectedIndex: 0\n  }")
    # 填充custom-tab-bar/index.js
    tabbar_data = {
        'selected_number': 0,
        'color': "#7A7E83",
        'selected_color': "#e2a140",
        'list': [
            {
                'page_path': "/pages/index/index",
                'icon_path': "/assets/tabbar/home.png",
                'selected_icon_path': "/assets/tabbar/home_active.png",
                'text': "首页"
            },
            {
                'page_path': "/pages/logs/logs",
                'icon_path': "/assets/tabbar/profile.png",
                'selected_icon_path': "/assets/tabbar/profile_active.png",
                'text': "我的"
            }
        ]
    }
    # tabbar_index_template(tabbar_data)
    tabbar_json_data = {
        "custom": True,
        "color": "#7A7E83",
        "selectedColor": "#3cc51f",
        "borderStyle": "white",
        "backgroundColor": "#ffffff",
        "list": [
            {
                "text": "首页",
                "pagePath": "pages/index/index",
                "iconPath": "assets/tabbar/home.png",
                "selectedIconPath": "assets/tabbar/home_active.png"
            },
            {
                "text": "我的",
                "pagePath": "pages/logs/logs",
                "iconPath": "assets/tabbar/profile.png",
                "selectedIconPath": "assets/tabbar/profile_active.png"
            }
        ]
    }
    app_json_template(True, True, tabbar_json_data)
