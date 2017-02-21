# -*- coding: UTF-8 -*-
with open('more', 'r') as f:
    with open('after', 'w') as output:
        for line in f.readlines():
            line = line.strip()
            if len(line) > 0:
                print(line)
                output.write(line+'\n')