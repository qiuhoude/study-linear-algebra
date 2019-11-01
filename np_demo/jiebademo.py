#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 结巴安装 conda install -c conda-forge jieba
import jieba

test_Str = "上海大学城书店"

seg_list = jieba.cut(test_Str, cut_all=True)
print("Full Mode: ", "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut(test_Str, cut_all=False)
print("Default Mode: ", "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut(test_Str)  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search(test_Str)  # 搜索引擎模式
print("Search Mode", "/ ".join(seg_list))
