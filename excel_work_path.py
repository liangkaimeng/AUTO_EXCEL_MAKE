# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: LiangKaimeng
# Date  : 2021/1/9

import os
import warnings
import datetime

warnings.filterwarnings('ignore')

def extract_file_name(path, keyword):
    """
    :param path: 备份表所在路径， 例如：root_path + "备份表\\"
    :param keyword: 关键词，即需要处理汇总的工作表中的关键词, 例如：test
    :return: 工作表的路径
    """
    # 初始化一个日期 -- 昨天
    up_day = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y%m%d")
    # 返回路径下所有的文件名称，以列表形式存储
    all_file_name = os.listdir(path)
    ### 提取包含“.xls”与".xlsx"文件扩展名的文件，并且包含关键词，以列表形式存储
    # 初始化excel文件名
    excel_file_name = ''
    for file_name in all_file_name: # 遍历文件名列表
        # 如果文件名包含"test"，并且文件扩展名为".xls"或".xlsx"，则赋值给
        if keyword in file_name and file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            excel_file_name = file_name
        else:
            pass

    # 备份表路径
    work_path = os.getcwd() + "\工作表\\"
    # 待处理的excel文件名进行命名重构
    work_file_name = os.path.splitext(excel_file_name)[0] + '-' + up_day + '.xlsx'
    # 构造路径+文件名
    front_path_file = path + excel_file_name
    later_path_file = work_path + work_file_name
    if len(excel_file_name) > 0:
        os.system(r"copy {} {}".format(front_path_file, later_path_file))
    else:
        pass

    return later_path_file