# coding=utf-8

# ----------------
# 组装index页面
# author：sbin
# date：2022-02-17
# ----------------

import util


# 创建页面
def create_page(name):
    # util.create_page(util.test_template_pages_path, 'index1')
    # print(util.create_page(name="index2"))
    return util.create_page(name="index2")


if __name__ == "__main__":
    create_page(name="index2")
