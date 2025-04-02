# random.py
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import choice

import time
#import BME1_name_list
name_lists=[
    "白天",
    "邱创辰",
    "罗杨林",
    "蔡慕天",
    "杨爽",
    "陈章武",
    "陈卓",
    "邓贵锋",
    "黄河翔",
    "黄俊泓",
    "蒋佳辰",
    "蓝荣熙",
    "林天予",
    "刘庆彬",
    "刘岩",
    "卢冠霖",
    "魏坚锐",
    "温钦正",
    "巫烨力",
    "伍浩然",
    "周胤宏",
    "庄承一",
    "艾熠恒",
    "胡文智",
    "花正荣", 
    "金家臣",
    "李煦徽",
    "潘昊宇",
    "王云彪",
    "谭晓鹏",
    "汪远洋",
    "游若飞",
    "余辉阳",
    "张彬彬",
    "张鹏程",
    "蔡致宁",
    "陈丽盈",
    "陈敏",
    "陈燕华",
    "纪嘉蒞",
    "邓静雯",
    "陈亿彤",
    "韩楚欣",
    "庞昕",
    "阮柔",
    "申信",
    "石颖",
    "袁雨柔",
    "张碧昀",
    "张嘉轩",
    "张靖宜",
    "程金玉",
    "龚晨曦",
    "张怡馨",
    "孟楠欣",
    "欧阳嫣然",
    "林梦露",
    "彭佳瑾",
    "杨思思",
    "李加林",
    "姚佳妹",
    "姚怡然"
    ]
print("\n\n\t\t\t\tBME1班\n")
time.sleep(3)
print("\n\t\t\t本次摇号公平、公正、公开\n")
time.sleep(3)
print("\t\t\t参与本次摇号人数62人")
time.sleep(1)
lucky_dogs_needed = int(input("\t需摇出人数："))
print('\n')
lucky_dogs=[]

lucky_dogs_num = 1
while lucky_dogs_num <= lucky_dogs_needed:
    lucky_dog = choice(name_lists)
    if lucky_dog not in lucky_dogs:
        lucky_dogs.append(lucky_dog)
        print(f"\t\t\t{lucky_dogs_num}.{lucky_dog}")
        lucky_dogs_num +=1
        time.sleep(2)

input("\n\t\t\t抽签结束！")

