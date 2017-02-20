with open('three_doors.py', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        if len(line) > 0:
            print(line)
