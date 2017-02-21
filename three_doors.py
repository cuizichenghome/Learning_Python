
# -*- coding: UTF-8 -*-

import random

lose_count = 0
win_count = 0


def make_a_choice(switch=False):
    # 初始化箱子
    boxes = ['goat'] * 3
    index_car = random.randint(0, 2)
    for i in range(3):
        if i == index_car:
            boxes[i] = 'car'
            break

    # print('箱子里面是: %s' % boxes)

    # 选手选择
    start_choice = random.randint(0, 2)
    # print('选手的最初选择是： %d' % start_choice)

    # 主持人打开一个箱子
    a = []
    for index, item in enumerate(boxes):
        if index != start_choice:
            a.append(index)
    # print('除选手选择外，还剩下：%s' % a)
    # 判断情况
    #  一只羊，一辆车

    if boxes[a[0]] == 'car' or boxes[a[1]] == 'car':
        show, left = (a[0], a[1]) if boxes[a[0]] == 'goat' else (a[1], a[0])

    # 两只羊
    else:
        show = random.choice(a)
        for index, item in enumerate(a):
            if item != show:
                left = item
                break
            else:
                continue

    # print('主持人打开了%s号箱子，里面是一只羊' % show)
    # print('场上还剩下%s和%s号箱子' % (left,start_choice))
    if switch:
        # 选手更换选择
        finally_choice = left
    else:
        # 选手坚持最初选择
        finally_choice = start_choice

    if boxes[finally_choice] == 'car':
        # print('选手胜利！车子就在%s号箱内。' % start_choice)
        global win_count
        win_count = win_count + 1
    else:
        # print('选手失败！车子其实在%s号箱内。' % left)
        global lose_count
        lose_count = lose_count + 1


def stay100():
    for _ in range(1000):
        make_a_choice()
    print('*' * 50)
    print('选手坚持自己的选择:\n共执行1000次')
    print('胜利%s次，失败%s次' % (win_count, lose_count))
    print('胜率为：%s' % str((win_count/1000)*100)+'%')
    print('*' * 50)


def switch100():
    for _ in range(1000):
        make_a_choice(switch=True)
    print('*' * 50)
    print('选手改变自己的选择:\n共执行1000次')
    print('胜利%s次，失败%s次' % (win_count,lose_count))
    print('胜率为：%s' % str((win_count/1000)*100)+'%')
    print('*' * 50)
    
# 对闭包等概念还不太熟悉，不太会使用global变量
stay100()
# global win_count
win_count = 0
# global lose_count
lose_count = 0
switch100()

