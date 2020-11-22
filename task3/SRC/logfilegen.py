import datetime
import random


def random_date():
    earliest = datetime.datetime(2010, 1, 1, 13, 34, 9)
    latest = datetime.datetime(2030, 1, 1, 12, 54, 2)
    delta = latest - earliest
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return str(earliest + datetime.timedelta(seconds=random_second)).replace(' ', 'T')


scoop = ['scoop', 'top up']
litres = ['10', '20', '30', '40']
log_list = ['META DATA:', '200', '32']
success = ['(успех)', '(фейл)']


for i in range(18000):
    to_add = f'{random_date()}.{random.randint(100,999)}Z-[username{random.randint(1,200)}] - {random.choice(scoop)} {random.choice(litres)}l'
    log_list.append(to_add)


with open("log.log", 'w') as f:
   for log in log_list:
    f.write(log + '\n')



