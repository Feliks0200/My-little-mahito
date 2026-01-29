import datetime
from datetime import *


#Сохранение статистики

def save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money):
     with open('mlm/user_data.txt', 'w') as f:
         f.write(f'golod = {golod} '
                 f'\nsleep = {sleep} '
                 f'\nigrat = {igrat} '
                 f'\ntoilet = {toilet} '
                 f'\npopitka = {popitka}'
                 f'\nkol_eat = {kol_eat}'
                 f'\nkol_money = {kol_money}')


#Загрузка статистики

def info():
    with open('mlm/user_data.txt') as file:
        line1 = file.readline()  # Первая строка
        golod = int(line1.split()[2])

        line2 = file.readline()  # Вторая строка
        sleep = int(line2.split()[2])

        line3 = file.readline()
        igrat = int(line3.split()[2])

        line4 = file.readline()
        toilet = int(line4.split()[2])

        line5 = file.readline()
        popitka = int(line5.split()[2])

        line6 = file.readline()
        kol_eat = int(line6.split()[2])

        line7 = file.readline()
        kol_money = int(line7.split()[2])
    return golod, sleep, igrat, toilet, popitka, kol_eat, kol_money


#Сохранение времени
def side_vremya(last_log, last_eat, last_toilet, last_sleep, last_lose, last_game):
    with open('mlm/sidetime_log.txt', 'w') as fa:
        fa.write(f'last_log= {last_log}'
                f'\nlast_eat= {last_eat}'
                f'\nlast_toilet= {last_toilet}'
                f'\nlast_sleep= {last_sleep}'
                f'\nlast_lose= {last_lose}'
                f'\nlast_game= {last_game}')

def vremya(last_log, last_eat, last_toilet, last_sleep, last_lose, last_game):
    with open('mlm/time_log.txt', 'w') as f:
        f.write(f'last_log= {last_log}'
                 f'\nlast_eat= {last_eat}'
                 f'\nlast_toilet= {last_toilet}'
                 f'\nlast_sleep= {last_sleep}'
                 f'\nlast_lose= {last_lose}'
                 f'\nlast_game= {last_game}')
    side_vremya(last_log, last_eat, last_toilet, last_sleep, last_lose, last_game)


#Загрузка времени

def vremya_read():
    with open('mlm/time_log.txt') as file:
        line8 = file.readline()
        last_log = line8.split()[1]

        line9 = file.readline()
        last_eat = line9.split()[1]

        line10 = file.readline()
        last_toilet = line10.split()[1]

        line11 = file.readline()
        last_sleep = line11.split()[1]

        line12 = file.readline()
        last_lose = line12.split()[1]

        line13 = file.readline()
        last_game = line13.split()[1]
    return last_log, last_eat, last_toilet, last_sleep, last_lose, last_game

def side_vremya_read():
    with open('mlm/sidetime_log.txt') as file:
        line8 = file.readline()
        last_log = line8.split()[1]

        line9 = file.readline()
        last_eat = line9.split()[1]

        line10 = file.readline()
        last_toilet = line10.split()[1]

        line11 = file.readline()
        last_sleep = line11.split()[1]

        line12 = file.readline()
        last_lose = line12.split()[1]

        line13 = file.readline()
        last_game = line13.split()[1]
    return last_log, last_eat, last_toilet, last_sleep, last_lose, last_game

#Перевод времени для сравнения
def sravn(time_str):
    while time_str[0]=='"':
        time_str = time_str[1:]
    while time_str[-1]=='"':
        time_str = time_str[:-1]
    Y,m,d,H,M,S = map(int, time_str.split('-'))
    return datetime(Y,m,d,H,M,S)

def kak_davno(log_date):
    a = f'"{log_date}"'
    return sravn(today())-sravn(a)


#Сохранение предметов

def plushki(krovat, toilet_zoloto):
    with open('mlm/plushki.txt', 'w') as f:
        f.write(f'{krovat}\n{toilet_zoloto}')


#Загрузка предметов

def plushki_read():
    with open('mlm/plushki.txt') as file:
        line1 = file.readline()  # Первая строка
        krovat = int(line1.split()[0])

        line2 = file.readline()  # Вторая строка
        toilet_zoloto = int(line2.split()[0])
    return krovat, toilet_zoloto


#Узнавание времени


def today():
     now = datetime.now()
     time = now.strftime('"%Y-%m-%d-%H-%M-%S"')
     return time


# plushki(0,0)
# save(101, 102, 103, 104, 10, 20, 20)
#side_vremya(today(),today(),today(),today(),today(),today())
# last_log, last_eat, last_toilet, last_sleep, last_lose = vremya_read()
# vremya(last_log, last_eat, last_toilet, last_sleep, last_lose)
# a = last_log[1:-1].split('-')
