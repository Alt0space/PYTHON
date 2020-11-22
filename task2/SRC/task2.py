import re
import math
import sys


line1 = "\{([\d\,\.\[\]\-\s]+)\}"
line2 = "[\,\]\[\}\{]"
draft_radius = r'radius:([\s\d\.]+)'
draft_center = r'center:([\[\,\s\d\.]+)'

#draft = '{sphere: {center: [0, 0, 0], radius: 10.67}, line: {[1, 0.5, 15], [43, -14.6, 0.04]}}'

with open(f'{sys.argv[1]}', 'r') as f:
    draft = f.read()

# ПАРСИНГ СТРОКИ С ПОМОЩЬЮ РЕГУЛЯРНЫХ ВЫРАЖЕНИЙ

line = re.search(f'{line1}', draft)
line = line.group(0)
line = re.sub(f'{line2}', '', line)
line = line.split()
radius = re.search(f'{draft_radius}', draft)
radius = radius.group(1)
radius = re.sub('[\s]+', '', radius)
center = re.search(f'{draft_center}', draft)
center = center.group(1)
center = re.sub('[\,\[]+', '', center)
center = center.split()

# КООРДИНАТЫ ТОЧЕК
xc = float(center[0])
yc = float(center[1])
zc = float(center[2])
radius = float(radius)
x1 = float(line[0])
y1 = float(line[1])
z1 = float(line[2])
x2 = float(line[3])
y2 = float(line[4])
z2 = float(line[5])

# РЕШЕНИЕ
a = (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2
b = -2 * ((x2 - x1) * (xc - x1) + (y2 - y1) * (yc - y1) + (zc - z1) * (z2 - z1))
c = (xc - x1)**2 + (yc - y1)**2 + (zc - z1)**2 - radius**2

d = b**2-4*a*c   # дискриминант

points_of_collision = []
n = 0

if d < 0:
    n = 0
elif d == 0:
    t = (-b+math.sqrt(b**2-4*a*c))/2*a
    n = 1
else:
    t1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
    t2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
    n = 2

if n == 1:
    x_0 = round((x1 + (x2 - x1) * t), 2)
    y_0 = round((1 + (y2 - y1) * t), 2)
    z_0 = round((z1 + (z2 - z1) * t), 2)
    print(x_0, y_0, z_0)
elif n == 2:
    x_1 = round((x1 + (x2 - x1) * t1), 2)
    y_1 = round((1 + (y2 - y1) * t1), 2)
    z_1 = round((z1 + (z2 - z1) * t1), 2)
    x_2 = round((x1 + (x2 - x1) * t2), 2)
    y_2 = round((1 + (y2 - y1) * t2), 2)
    z_2 = round((z1 + (z2 - z1) * t2), 2)
    print(x_1, y_1, z_1, '\n')
    print(x_2, y_2, z_2, '\n')
else:
    print('Коллизий не найдено')
