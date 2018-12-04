
import time
import random

def some_func():
    ques_what = raw_input('type Y or N :\n')

    answer = random.choice('YN')
    while ques_what != answer:
        print 'You\'re not guessed'
        ques_what = raw_input('type Y or N :\n')
        answer =random.choice('YN')
    else:
        return 'Cogratulation you\'re pass'


def stapwatch (func):
    start = time.time()
    func()
    end = time.time()
    return  int(end - start)

rows_list = [1,2,3,4,5,6,7,8]

def navigate(navig_list = ['some spesific code','OK']):
    num = int(input('Some number of row:\n'))
    for x in range(0, num-1):
        navig_list.insert(-1,'Down')
    return navig_list