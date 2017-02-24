# -*- coding: UTF-8 -*-
# 需要指定文件的打开编码，否则会使用系统默认的GBK编码，产生错误
with open('more', 'r', encoding='utf-8') as f:
    with open('after', 'w') as output:
        for line in f.readlines():
            line = line.strip()
            # 如果是.py文件，就只去除空行，不去除tab和空格
            # line = line.strip('\n\r')
            if len(line) > 0:
                print(line)
                output.write(line+'\n')
