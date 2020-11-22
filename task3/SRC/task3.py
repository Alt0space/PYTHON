from datetime import datetime
import sys
import re
#^(.+)\.




log = []

with open(f'{sys.argv[1]}', 'r') as f:
    for line in f:
        log.append(line)


def s_liters(string):
    linedraft = "(\d+)l"
    value = re.match(f'{linedraft}', string)
    return value.group(0)

#date1 = datetime.fromisoformat(f'{sys.argv[2]}')
#date2 = datetime.fromisoformat(f'{sys.argv[3]}')
volume = log[1]
liters = log[2]
top_ups = 0
mistakes = 0
top_up_volume = 0
missed_top_up = 0
scoop_volume = 0
missed_scoop = 0
volume_0 = 0
volume_l = 0

#for i in range(3, len(log)):
