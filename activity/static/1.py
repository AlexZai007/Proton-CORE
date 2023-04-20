import time

import matplotlib.pyplot as plt
import numpy as np

import math
import os
import requests



def get_info():
    x = requests.get('http://localhost:4000/chain')
    res = x.json()
    res = res.get('chain')
    return len(res)



async def show():
    plt.show()


a = 1
list1, list2 = [], []
while True:


    transaction1 = int(get_info())
    time.sleep(1)
    transaction2 = int(get_info())
    tran_per_sec = transaction2 - transaction1



    list1.append(a)
    list2.append(tran_per_sec)

    plt.ion()
    for n in range(1):
        # Данные для очередного кадра
        ylist = [math.sin(x + n / 2.0) for x in list1]

        # Выведем новые данные
        plt.plot(list1, list2)

        # !!! Нарисуем их
        # !!! Обратите внимание, что здесь используется функция draw(), а не show()
        plt.draw()  # Должно быть это, а в итоге не это, приходится каждый раз открывать картинку
        plt.pause(0.1)

    plt.ioff()
    show()

    a = a + 1


