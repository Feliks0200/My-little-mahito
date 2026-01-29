import pygame
import sys
import random
from tkinter.messagebox import showerror, showinfo, showwarning
from mlm.savemahito import *
from mlm.savemahito import sravn, today


def quit():
    pygame.quit()
    sys.exit()
pygame.init()
screen=pygame.display.set_mode((600,800))
pygame.display.set_caption("My little mahito")
icon = pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/mlm.ico')
pygame.display.set_icon(icon)
bgmenu=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/mega_zaglotus.png')
surface=pygame.Surface(screen.get_size(),pygame.SRCALPHA)
clock = pygame.time.Clock()

#шрифты

shrift=pygame.font.Font('шрифт/asimovprobd.otf', 40)

shrift_log1=pygame.font.Font('шрифт/asimovprobd.otf', 25)

shrift_log2=pygame.font.Font('шрифт/asimovprobd.otf', 25)

#звуки

lose=pygame.mixer.Sound("звуки/vine-boom-hq-longer.mp3")

# ПЕРЕМЕННЫЕ интерфейса

interface_alph=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/интерфасе/interface_alpha.png')
interface_button_under=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/интерфасе/bot_buttons01.png')
interface_button_up=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/интерфасе/top_buttons01.png')

# Переменные фона

fone_good=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/bg/ok.png')
fone_sad=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/bg/sad.png')
fone_sleep=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/bg/sleep.png')
fone_sleepy=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/bg/sleepy.png')
fone_toilet=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/bg/toilet.png')
fone_ultra_sad=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/bg/ultrasad.png')
fone_hungry=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/bg/hungry.png')
fone_gameover=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/bg/end.png')
fone_gameover1=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/bg/bomjara.png')

# Переменные махито

maxito_ok=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/махито иконки/mlm_ok.png')
maxito_sad=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/махито иконки/mlm_sad.png')
maxito_sleep=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/махито иконки/mlm_sleep.png')
maxito_sleepy=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/махито иконки/mlm_sleepy.png')
maxito_toilet=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/махито иконки/mlm_toilet01.png')
maxito_ulta_sad=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/махито иконки/mlm_ultrasad.png')
maxito_hungry=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/махито иконки/mlm_hungry.png')
maxito_nothing=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/махито иконки/nothing.png')
maxito_bad_ending=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/махито иконки/true_form_mahito.png')
maxito_bad_ending1=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/махито иконки/Без имени-1.jpg')

# Переменные фонов кнопок сверху
fone_inv=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/интерфасе/маню/inv.png')
fone_info=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/интерфасе/маню/info.png')
fone_shop=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/интерфасе/маню/shop.png')
fone_minigames=pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/интерфасе/маню/minigames.png')
fone_son=pygame.image.load("My litle mahito/фоточки мб чето придумаю лучше/махито иконки/кнопки нижнего меню/eb139ce7-ff8b-45eb-a37c-d2dc299df365.png")
fone_krepkiy_son=pygame.image.load("My litle mahito/фоточки мб чето придумаю лучше/махито иконки/кнопки нижнего меню/de1e98cc-4572-416b-9366-74e0fbbc51e5.png")

# Переменные фонов кнопок снизу

# Ошибка природы
def bomj():
    showerror(title='Бичара))))', message="недостаточно средств")
def nezkrovat():
    showerror(title='Кровать', message="кровать уже куплена")
def netolkan():
    showerror(title="Туалет", message='золотой классный красивый крутой унитаз уже куплен')
def popitnol():
    showerror(title='Попытки', message='У вас закончились попытки. возвращайтесь через час')
def golodyes():
    showinfo(title='успешно покормлен', message='вы покормили махито')
def golodno1():
    showwarning(title='голодно(', message='У вас нету еды')
def zapret30min():
    showwarning(title='30 секунд', message='махито в туалете, дождитесь')
def truform():
    showerror(title='True ending', message='Вы слишком откормили махито')

# Игровые переменные

speed_x = -2
speed_y = 0
ball_x = 300
ball_y = 300
pl_y = 300 - 50
bt_y = 300 - 50
pl_collide = 300
bt_collide = bt_y
pl_count = 0
bt_count = 0
y_s = 4
cikl1 = 0
score1 = -1
shas1=0
lives = 3

bg_pong = pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/махито иконки/мини игры/pong_bg.png')
player_png = pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/махито иконки/мини игры/player.png')
bot_png = pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/махито иконки/мини игры/suguro.png')
ball_png = pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/махито иконки/мини игры/jogo.png')
lives_png = pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/махито иконки/мини игры/live.png')
pongigra = pygame.image.load('My litle mahito/фоточки мб чето придумаю лучше/махито иконки/мини игры/pongigra.png')

background_img = pygame.image.load("My litle mahito/фоточки мб чето придумаю лучше/махито иконки/мини игры/snakeigr.png").convert()  # Фон (размер 600x800, желательно)
apple_img = pygame.image.load("My litle mahito/фоточки мб чето придумаю лучше/махито иконки/мини игры/apple.png").convert_alpha()  # Яблочко (примерно 20x20px)
#Проверка на потребности

def golodno():
    if golod<=40:
        return True
    else:
        return False
def sleepym():
    if sleep<=40:
        return True
    else:
        return False
def igratixoc():
    if igrat<=40:
        return True
    else:
        return False
def popitkanol():
    if popitka==0:
        return True
    else:
        return False
def kakati():
    if toilet<=40:
        return True
    else:
        return False


#логи
last_log1, last_eat1, last_toilet1, last_sleep1, last_lose1, last_game1 = side_vremya_read()
golod, sleep, igrat, toilet, popitka, kol_eat, kol_money = info()

if kak_davno(last_eat1) > timedelta(0,1800):
    ubirau = kak_davno(last_eat1)
    while ubirau > timedelta(0,1800):
        ubirau -= timedelta(0,1800)
        golod -=5
        if golod <= 0:
            golod = 0
        # print(3)
    last_eat1=today()
if kak_davno(last_toilet1) > timedelta(0,1800):
    ubirau = kak_davno(last_toilet1)
    while ubirau > timedelta(0,1800):
        ubirau -= timedelta(0,1800)
        toilet -=5
        if toilet <= 0:
            toilet = 0
        # print(2)
    last_toilet1=today()
if kak_davno(last_game1) > timedelta(0,1800):
    ubirau = kak_davno(last_game1)
    while ubirau > timedelta(0,1800):
        ubirau -= timedelta(0,1800)
        igrat -=5
        if igrat <= 0:
            igrat = 0
        popitka +=1
        # print(1)
    last_game1=today()
if kak_davno(last_sleep1) > timedelta(0,1800):
    ubirau = kak_davno(last_sleep1)
    while ubirau > timedelta(0,1800):
        ubirau -= timedelta(0,1800)
        sleep -=5
        if sleep <= 0:
            sleep = 0
        # print(0)
    last_sleep1=today()
save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money)
last_log, last_eat, last_toilet, last_sleep, last_lose, last_game = vremya_read()
vremya(today(), last_eat, last_toilet, last_sleep, last_lose, last_game)
side_vremya(last_log1, last_eat1, last_toilet1, last_sleep1, last_lose1, last_game1)
secundi = 60
minute = sravn(today())+timedelta(0,secundi)


# остальной сброд

aleg=0
boba=0
timer=0
son_time=120
son_time_bobr=2
stroka="menu"
while True:

    # логи2
    if sravn(today()) > minute:
        last_log1, last_eat1, last_toilet1, last_sleep1, last_lose1, last_game1 = side_vremya_read()
        golod, sleep, igrat, toilet, popitka, kol_eat, kol_money = info()

        if kak_davno(last_eat1) > timedelta(0, 1800):
            ubirau = kak_davno(last_eat1)
            while ubirau > timedelta(0, 1800):
                ubirau -= timedelta(0, 1800)
                golod -= 5
                if golod <= 0:
                    golod = 0
                # print(3)
            last_eat1 = today()
        if kak_davno(last_toilet1) > timedelta(0, 1800):
            ubirau = kak_davno(last_toilet1)
            while ubirau > timedelta(0, 1800):
                ubirau -= timedelta(0, 1800)
                toilet -= 5
                if toilet <= 0:
                    toilet = 0
                # print(2)
            last_toilet1 = today()
        if kak_davno(last_game1) > timedelta(0, 1800):
            ubirau = kak_davno(last_game1)
            while ubirau > timedelta(0, 1800):
                ubirau -= timedelta(0, 1800)
                igrat -= 5
                if igrat <= 0:
                    igrat = 0
                popitka += 1
                # print(1)
            last_game1 = today()
        if kak_davno(last_sleep1) > timedelta(0, 1800):
            ubirau = kak_davno(last_sleep1)
            while ubirau > timedelta(0, 1800):
                ubirau -= timedelta(0, 1800)
                sleep -= 5
                if sleep <= 0:
                    sleep = 0
                # print(0)
            last_sleep1 = today()
        save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money)
        last_log, last_eat, last_toilet, last_sleep, last_lose, last_game = vremya_read()
        vremya(today(), last_eat, last_toilet, last_sleep, last_lose, last_game)
        side_vremya(last_log1, last_eat1, last_toilet1, last_sleep1, last_lose1, last_game1)
        minute = sravn(today()) + timedelta(0, secundi)
        # print(1)

    if sleep > 100:
        sleep = 100
        save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money)
    if toilet > 100:
        toilet = 100
        save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money)
    if popitka > 7:
        popitka=7
        save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money)


    golod, sleep, igrat, toilet, popitka, kol_eat, kol_money = info()
    # текст
    text_money = shrift.render(f":{kol_money} ₽", True, (255, 255, 255))
    text_try = shrift.render(F":{popitka} попыток", True, (255, 255, 255))
    text_eat = shrift.render(f":{kol_eat} Еды", True, (255, 255, 255))
    text_krovat_yes = shrift.render(f":Есть", True, (255, 255, 255))
    text_krovat_no = shrift.render(f":Нету", True, (255, 255, 255))
    text_toilet_yes = shrift.render(f":Есть", True, (255, 255, 255))
    text_toilet_no = shrift.render(f":Нету", True, (255, 255, 255))
    # текст времени
    last_log, last_eat, last_toilet, last_sleep, last_lose, last_game = vremya_read()
    last_log_text = shrift_log1.render(f'Время последнего захода: {last_log}', True, (255, 255, 255))
    last_eat_text = shrift_log1.render(f'Время последнего кормления: {last_eat}', True, (255, 255, 255))
    last_toilet_text = shrift_log1.render(f'Время последнего похода в туалет: {last_toilet}', True, (255, 255, 255))
    last_sleep_text = shrift_log1.render(f'Время последнего сна: {last_sleep}', True, (255, 255, 255))
    last_lose_text = shrift_log1.render(f'Время последнего проигрыша: {last_lose}', True, (255, 255, 255))

    last_log_text2 = shrift_log1.render(f'Время последнего захода: {last_log}', True, (0, 0, 0))
    last_eat_text2 = shrift_log1.render(f'Время последнего кормления: {last_eat}', True, (0, 0, 0))
    last_toilet_text2 = shrift_log1.render(f'Время последнего похода в туалет: {last_toilet}', True, (0, 0, 0))
    last_sleep_text2 = shrift_log1.render(f'Время последнего сна: {last_sleep}', True, (0, 0, 0))
    last_lose_text2 = shrift_log1.render(f'Время последнего проигрыша: {last_lose}', True, (0, 0, 0))
    #текст сна
    son_text = shrift_log1.render(f'Осталось спать: {(str(timedelta(0, son_time) - kak_davno(last_sleep)))[son_time_bobr:]}', True, (255, 255, 255))
    son_text2 = shrift_log1.render(f'Осталось спать: {(str(timedelta(0, son_time) - kak_davno(last_sleep)))[son_time_bobr:]}', True, (0, 0, 0))
    # текст туалета
    toilet_text = shrift_log1.render(f'Махито в туалете:\n {(str(timedelta(0, 30) - kak_davno(last_toilet)))[5:]}', True,(236, 195, 83))
    toilet_text2 = shrift_log1.render(f'Махито в туалете:\n {(str(timedelta(0, 30) - kak_davno(last_toilet)))[5:]}', True, (0, 0, 0))
    #текст скоров
    score1_text1 = shrift_log1.render(f'Счёт: {score1}', True, (255, 255, 255))
    score1_text2 = shrift_log1.render(f'Счёт: {score1}', True, (134, 107, 188))

    if popitka==0 and kol_money==0:
        now = pygame.time.get_ticks()
        if aleg==0:
            aleg=1
            timer=now
        screen.blit(fone_gameover, (0,0))
        if now-timer>=2000 and aleg==1:
            lose.play()
            screen.blit(fone_gameover1, (0,0))
            aleg=2

        if now-timer>=4000 and aleg==2:
            save(100, 100, 100, 100, 7, 20, 20)
            plushki(0, 0)
            vremya(today(), today(), today(), today(), today(),today())
            aleg = 0
            pygame.quit()
            sys.exit()
        pygame.display.flip()
        clock.tick(5)
    elif golod>140:
        now = pygame.time.get_ticks()
        if aleg == 0:
            screen.blit(fone_hungry, (0, 0))
            aleg = 1
            timer = now
            screen.blit(maxito_bad_ending, (0, 0))
        if now - timer >= 2000 and aleg == 1:
            lose.play()
            screen.blit(maxito_bad_ending1, (0, 0))
            aleg = 2


        if now - timer >= 4000 and aleg == 2:
            truform()
            save(100, 100, 100, 100, 7, 20, 20)
            plushki(0, 0)
            vremya(today(), today(), today(), today(), today(), today())
            aleg=0
            pygame.quit()
            sys.exit()
        pygame.display.flip()
        clock.tick(5)
    elif stroka=="menu":
        screen.blit(bgmenu, (0, 0))
        button = pygame.Rect(200, 200, 200, 180)
        pygame.draw.rect(surface, (255, 255, 255, 0), button)
        screen.blit(surface, (0, 0))

        if button.collidepoint(pygame.mouse.get_pos()):  # курсор
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    stroka="game"
        pygame.display.flip()
    elif stroka=="game":
        krovat,toilet_zoloto=plushki_read()
        #проверка на потребности(не получилось в def)

        if popitkanol() == True:
            fone_maxito = fone_ultra_sad
            maxito = maxito_ulta_sad
        elif golodno() == True:
            fone_maxito = fone_hungry
            maxito = maxito_hungry
        elif sleepym() == True:
            fone_maxito = fone_sleepy
            maxito = maxito_sleepy
        elif igratixoc() == True:
            fone_maxito = fone_sad
            maxito = maxito_sad
        elif kakati() == True:
            fone_maxito = fone_toilet
            maxito = maxito_toilet
        else:
            fone_maxito = fone_good
            maxito = maxito_ok

        #фон и всякая нужная штука(например невидимость для кнопок)

        bgmenu=fone_maxito
        screen.blit(bgmenu, (0,0))
        screen.blit(interface_button_up,(0,0))
        screen.blit(interface_alph, (0, 0))
        screen.blit(interface_button_under,(0,0))
        screen.blit(surface, (0, 0))

        #чубрик
        screen.blit(maxito, (0,0))

        #Кнопки нижнего меню

        button_eat=pygame.Rect(50,660,130,120)
        pygame.draw.rect(surface, (255, 255, 255,0), button_eat)

        button_toilet=pygame.Rect(230,660,130,120)
        pygame.draw.rect(surface, (255, 255, 255,0), button_toilet)

        button_sleep=pygame.Rect(420,660,130,120)
        pygame.draw.rect(surface, (255, 255, 255,0), button_sleep)

        #Кнопки верхнего меню

        button_info=pygame.Rect(0,2,100,100)
        pygame.draw.rect(surface, (255, 255, 255,0), button_info)

        button_game=pygame.Rect(313,2,100,100)
        pygame.draw.rect(surface, (255, 255, 255,0), button_game)

        button_inv = pygame.Rect(413, 2, 100, 100)
        pygame.draw.rect(surface, (255, 255, 255,0), button_inv)

        button_shop = pygame.Rect(513, 2, 100, 100)
        pygame.draw.rect(surface, (255, 255, 255,0), button_shop)

        #

        if button_info.collidepoint(pygame.mouse.get_pos()) or button_inv.collidepoint(pygame.mouse.get_pos()) or button_game.collidepoint(pygame.mouse.get_pos()) or button_shop.collidepoint(pygame.mouse.get_pos()) or button_eat.collidepoint(pygame.mouse.get_pos()) or button_sleep.collidepoint(pygame.mouse.get_pos()) or button_toilet.collidepoint(pygame.mouse.get_pos()): #курсор
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            # Кнопки сверху
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_info.collidepoint(event.pos):
                    stroka="FAQ(not FAQ)"
                if button_inv.collidepoint(event.pos):
                    stroka="inven"
                if button_game.collidepoint(event.pos):
                    stroka="minigame"
                if button_shop.collidepoint(event.pos):
                    stroka="shop"
            #кнопки снизу
                if button_eat.collidepoint(event.pos):
                    if kol_eat>0:
                        kol_eat-= 20
                        golod+=20
                        golodyes()
                        save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money)
                    else:
                        golodno1()
                if button_sleep.collidepoint(event.pos):
                    if krovat==1:
                        stroka="pisyatispat"
                        sleep+=40
                        toilet-=20
                        save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money)
                    else:
                        stroka="pisyatispat"
                        sleep+=20
                        toilet-=20
                        save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money)

                if button_toilet.collidepoint(event.pos):
                    if toilet_zoloto==1:
                        toilet+=40
                        vremya(last_log, last_eat, today(), last_sleep, last_lose, last_game)
                        save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money)
                        stroka = "toiletmonsterwow"
                    else:
                        toilet+=20
                        vremya(last_log, last_eat, today(), last_sleep, last_lose, last_game)
                        save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money)
                        stroka = "toiletmonsterwow"
        pygame.display.flip()
    elif stroka=="inven":
        screen.blit(fone_inv, (0, 0))
        screen.blit(surface, (0, 0))
        button_return=pygame.Rect(35,655,520,130)
        pygame.draw.rect(surface, (255, 255, 255, 0), button_return)

        screen.blit(text_try, (160,172))
        screen.blit(text_money, (160,274))
        screen.blit(text_eat, (160,372))

        krovat,toilet_zoloto=plushki_read()
        if krovat==1:
            screen.blit(text_krovat_yes, (160,460))
        else:
            screen.blit(text_krovat_no, (160,460))
        if toilet_zoloto==1:
            screen.blit(text_toilet_yes, (160,540))
        else:
            screen.blit(text_toilet_no, (160,540))


        if button_return.collidepoint(pygame.mouse.get_pos()):  # курсор
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_return.collidepoint(event.pos):
                    stroka="game"

        pygame.display.flip()
    elif stroka == "shop":
        screen.blit(fone_shop, (0, 0))
        screen.blit(surface, (0, 0))
        button_return = pygame.Rect(35, 655, 520, 130)
        pygame.draw.rect(surface, (255, 255, 255, 0), button_return)
        screen.blit(text_money, (20,20))
        krovat, toilet_zoloto = plushki_read()

        #кнопки покупки
        button_buy1=pygame.Rect(480,234,80,80)
        button_buy2=pygame.Rect(480,376,80,80)
        button_buy3=pygame.Rect(480,529,80,80)

        #отоброжение кнопок
        pygame.draw.rect(surface, (255, 255, 255,0), button_buy1)
        pygame.draw.rect(surface, (255, 255, 255,0), button_buy2)
        pygame.draw.rect(surface, (255, 255, 255,0), button_buy3)

        krovat, toilet_zoloto = plushki_read()

        if button_return.collidepoint(pygame.mouse.get_pos()) or button_buy1.collidepoint(pygame.mouse.get_pos()) or button_buy2.collidepoint(pygame.mouse.get_pos()) or button_buy3.collidepoint(pygame.mouse.get_pos()):  # курсор
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_return.collidepoint(event.pos):
                    stroka = "game"
                if button_buy1.collidepoint(event.pos):
                    if kol_money>=10:
                        kol_money-=10
                        kol_eat+=10
                        save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money)
                if button_buy2.collidepoint(event.pos):
                    if kol_money>=60:
                        if krovat==0:
                            kol_money-=60
                            krovat=1
                            plushki(krovat,toilet_zoloto)
                            save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money)
                        else:
                            nezkrovat()
                    else:
                        bomj()
                if button_buy3.collidepoint(event.pos):
                    if kol_money>=60:
                        if toilet_zoloto==0:
                            kol_money-=60
                            toilet_zoloto=1
                            plushki(krovat,toilet_zoloto)
                            save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money)
                        else:
                            netolkan()
                    else:
                        bomj()
        pygame.display.flip()
    elif stroka == "FAQ(not FAQ)":
        screen.blit(fone_info, (0, 0))
        screen.blit(surface, (0, 0))
        button_return = pygame.Rect(50, 650, 310, 130)
        pygame.draw.rect(surface, (255, 255, 255,0), button_return)
        button_sbros=pygame.Rect(420,650,124,130)
        pygame.draw.rect(surface, (255, 255, 255,0), button_sbros)

        #текст
        y = 3
        screen.blit(last_log_text2, (30 - 1, 200 + y))
        screen.blit(last_sleep_text2, (30 - 1, 275 + y))
        screen.blit(last_eat_text2, (30 - 1, 350 + y))
        screen.blit(last_lose_text2, (30 - 1, 425 + y))
        screen.blit(last_toilet_text2, (30 - 1, 500 + y))

        screen.blit(last_log_text, (30, 200))
        screen.blit(last_sleep_text, (30, 275))
        screen.blit(last_eat_text, (30, 350))
        screen.blit(last_lose_text, (30, 425))
        screen.blit(last_toilet_text, (30, 500))

        if button_sbros.collidepoint(pygame.mouse.get_pos()) or button_return.collidepoint(pygame.mouse.get_pos()):  # курсор
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_return.collidepoint(event.pos):
                    stroka = "game"
                if button_sbros.collidepoint(event.pos):
                    save(100, 100, 100, 100, 7, 20, 20)
                    plushki(0, 0)
                    vremya(today(), today(), today(), today(), today(),today())

        pygame.display.flip()
    elif stroka=="minigame":
        screen.blit(fone_minigames, (0, 0))
        screen.blit(surface, (0, 0))
        button_return = pygame.Rect(35, 655, 520, 130)
        pygame.draw.rect(surface, (255, 255, 255, 0), button_return)
        button_pong=pygame.Rect(35,200,230,300)
        pygame.draw.rect(surface, (255, 255, 255,0), button_pong)
        button_snake=pygame.Rect(330,200,230,300)
        pygame.draw.rect(surface, (255, 255, 255,0), button_snake)
        screen.blit(text_try,(200,120))



        if button_return.collidepoint(pygame.mouse.get_pos()) or button_snake.collidepoint(pygame.mouse.get_pos()) or button_pong.collidepoint(pygame.mouse.get_pos()):  # курсор
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_return.collidepoint(event.pos):
                    stroka="game"
                if button_snake.collidepoint(event.pos):
                    if popitka>0:
                        popitka-=1
                        stroka="snakeigr"
                        save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money)
                    else:
                        popitnol()
                if button_pong.collidepoint(event.pos):
                    if popitka>0:
                        popitka-=1
                        stroka="pongigr"
                        save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money)
                    else:
                        popitnol()
        pygame.display.flip()
    elif stroka=="snakeigr":
        button_ydi_Pojalysta=pygame.Rect(35, 655, 520, 130)
        pygame.draw.rect(surface, (255, 255, 255, 0), button_ydi_Pojalysta)

        CELL_SIZE = 20
        WIDTH=600
        HEIGHT=600

        # --- Функция рисования змейки ---
        def draw_snake(snake_body):
            for segment in snake_body:
                rect = pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, (181, 135, 237), rect)  # не Зеленый цвет змейки


        # --- Функция для генерации позиции яблока ---
        def random_apple_pos():
            x = random.randint(0, (600 - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            y = random.randint(0, (600 - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            return (x, y)


        # --- Основной цикл игры ---
        def main():
            clock = pygame.time.Clock()

            snake_pos = [600 // 2, 600 // 2]  # Начальная точка змейки (голова)
            snake_body = [snake_pos[:]]  # Тело змейки — список сегментов

            direction = "RIGHT"  # Начальное направление
            change_to = direction

            apple_pos = random_apple_pos()  # Позиция яблока
            score = 0

            while True:
                # Обработка событий (нажатия клавиш и выход)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        # Переключаем направление, но нельзя развернуться на 180°
                        if event.key == pygame.K_UP and direction != "DOWN":
                            change_to = "UP"
                        elif event.key == pygame.K_DOWN and direction != "UP":
                            change_to = "DOWN"
                        elif event.key == pygame.K_LEFT and direction != "RIGHT":
                            change_to = "LEFT"
                        elif event.key == pygame.K_RIGHT and direction != "LEFT":
                            change_to = "RIGHT"

                direction = change_to

                # Двигаем голову змейки
                if direction == "UP":
                    snake_pos[1] -= CELL_SIZE
                elif direction == "DOWN":
                    snake_pos[1] += CELL_SIZE
                elif direction == "LEFT":
                    snake_pos[0] -= CELL_SIZE
                elif direction == "RIGHT":
                    snake_pos[0] += CELL_SIZE

                # Добавляем новую голову в тело
                snake_body.insert(0, list(snake_pos))

                # Если съели яблоко
                if snake_pos == list(apple_pos):
                    score += 1
                    apple_pos = random_apple_pos()
                else:
                    # Иначе убираем хвост (змейка не растет)
                    snake_body.pop()
                kostil=0
                # Проверка выхода за границы (конец игры — выход из программы)
                if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
                        snake_pos[1] < 0 or snake_pos[1]
                        >= HEIGHT):
                    kostil=1

                    # Проверка съедения себя
                if snake_pos in snake_body[1:]:
                    kostil=1

                    # Отрисовка:
                screen.blit(background_img, (0, 0))  # Рисуем кастомный фон
                screen.blit(apple_img, apple_pos)  # Рисуем яблоко
                draw_snake(snake_body)  # Рисуем змейку

                # Отображение счета в левом верхнем углу
                font = pygame.font.SysFont(None, 30)
                score_text = font.render(f"Счет: {score}", True, (255, 255, 255))
                # Черный фон под счетом для читаемости
                score_bg = pygame.Surface(score_text.get_size())
                score_bg.fill((0, 0, 0))
                screen.blit(score_bg, (10, 10))
                screen.blit(score_text, (10, 10))

                button_return = pygame.Rect(50, 660, 500, 125)
                pygame.draw.rect(surface, (255, 255, 255, 0), button_return)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if button_return.collidepoint(event.pos):
                            kostil = 1

                clock.tick(10)  # Скорость обновления (FPS)
                if kostil==1:
                    return kostil, score
                pygame.display.update()
        kostil, score = main()

        if kostil==1:
            score = score // 10 * 10
            save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money+score)
            stroka="minigame"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
    elif stroka == "pongigr":
        now = pygame.time.get_ticks()
        if lives == 0:
            speed_x = -2
            speed_y = 0
            ball_x = 300
            ball_y = 300
            pl_y = 300 - 50
            bt_y = 300 - 50
            pl_collide = 300
            bt_collide = bt_y
            pl_count = 0
            bt_count = 0
            y_s = 4
            cikl1 = 0
            shas1 = 0
            lives = 3
            score1 = score1 // 10 * 10
            save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money + score1)
            score1 = -1
            stroka = "minigame"
        if score1 == -1:
            score1 = 0
            lives = 3
        if cikl1 == 0:
            cikl1 = 1
            shas1 = now
        screen.blit(pongigra, (0, 0))
        screen.blit(surface, (0, 0))

        button_return = pygame.Rect(50, 660, 500, 125)
        pygame.draw.rect(surface, (255, 255, 255, 0), button_return)

        ####################################
        back = pygame.Rect(0, 0, 600, 600)
        pygame.draw.rect(surface, (0, 0, 0, 0), back)
        screen.blit(bg_pong, (0, 0))

        borderbot = pygame.Rect(0, 600, 600, 10)
        pygame.draw.rect(surface, (0, 0, 0, 0), borderbot)

        bordertop = pygame.Rect(0, 0, 600, 1)
        pygame.draw.rect(surface, (0, 0, 0, 0), bordertop)

        borderleft = pygame.Rect(0, 0, 6, 600)
        pygame.draw.rect(surface, (0, 0, 0, 0), borderleft)

        borderright = pygame.Rect(594, 0, 6, 600)
        pygame.draw.rect(surface, (0, 0, 0, 0), borderright)

        for n in range(lives):
            screen.blit(lives_png, (20 + n * 40, 20))

        screen.blit(score1_text2, (26, 73))
        screen.blit(score1_text1, (26, 70))
        ####################################
        mid = pygame.Rect(295, 6, 5, 594)
        pygame.draw.rect(surface, (255, 255, 255, 0), mid)

        player = pygame.Rect(0, pl_y, 10, 100)
        pygame.draw.rect(surface, (255, 255, 255, 0), player)
        screen.blit(player_png, (0, pl_y))

        bot = pygame.Rect(590, bt_y, 10, 100)
        pygame.draw.rect(surface, (255, 255, 255, 0), bot)
        screen.blit(bot_png, (590, bt_y))

        ball = pygame.Rect(ball_x - 9, ball_y - 9, 12, 12)
        pygame.draw.rect(surface, (255, 255, 255, 0), ball)
        screen.blit(ball_png, (ball_x - 59, ball_y - 59))

        ####################################
        if ball.colliderect(player):
            speed_x *= -1
            score1 += 1
            if ball_y > pl_collide:
                speed_y = (ball_y - pl_collide) / 10
            elif ball_y < pl_collide:
                speed_y = (pl_collide - ball_y) / 10 * -1
            else:
                speed_y = 0

        elif ball.colliderect(bot):
            speed_x *= -1
            speed_y += random.randrange(-3, 3)
            if speed_y > 8:
                speed_y = 8

        elif ball.colliderect(borderbot) or ball.colliderect(bordertop):
            speed_y *= -1
        elif ball.colliderect(borderleft):
            bt_count += 1
            ball_x = 298
            ball_y = 291
            speed_x *= -1
            speed_y = 0
            pl_y = 250
            bt_y = 300 - 50
            pl_collide = 300
            bt_collide = 300
            cikl1 = 0
            lives -= 1
        elif ball.colliderect(borderright):
            bt_count += 1
            ball_x = 298
            ball_y = 291
            speed_x *= -1
            speed_y = 0
            pl_y = 250
            bt_y = 300 - 50
            pl_collide = 300
            bt_collide = 300
            cikl1 = 0

        knopka = pygame.key.get_pressed()
        if knopka[pygame.K_UP] or knopka[pygame.K_w]:
            pl_y -= y_s
            pl_collide = pl_y + 50
            if pl_y < 0:
                pl_y = 0
        elif knopka[pygame.K_DOWN] or knopka[pygame.K_s]:
            pl_y += y_s
            pl_collide = pl_y + 50
            if pl_y > 500:
                pl_y = 500

        ################### BOT ###################
        bt_y = ball_y - 50
        if ball_y > 650 or ball_y < -50 or ball_x > 650 or ball_x < -50:
            bt_count += 1
            ball_x = 291
            ball_y = 291
            speed_x *= -1
            speed_y = 0
            pl_y = 300 - 50
            bt_y = 300 - 50
            pl_collide = 300
            bt_collide = 300
            cikl1 = 0

        if bt_y < 0:
            bt_y = 0
        if bt_y > 500:
            bt_y = 500
        ###########################################
        if now - shas1 >= 1000:
            ball_x += speed_x
            ball_y += speed_y
        if button_return.collidepoint(pygame.mouse.get_pos()):  # курсор
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                score1 = score1 // 10 * 10
                save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money + score1)
                score1 = -1
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_return.collidepoint(event.pos):
                    speed_x = -2
                    speed_y = 0
                    ball_x = 300
                    ball_y = 300
                    pl_y = 300 - 50
                    bt_y = 300 - 50
                    pl_collide = 300
                    bt_collide = bt_y
                    pl_count = 0
                    bt_count = 0
                    y_s = 4
                    cikl1 = 0
                    shas1 = 0
                    lives = 3
                    score1 = score1 // 10 * 10
                    save(golod, sleep, igrat, toilet, popitka, kol_eat, kol_money + score1)
                    score1 = -1
                    stroka = "minigame"

        clock.tick(100)

        pygame.display.flip()
    elif stroka=="pisyatispat":
        krovat,toilet_zoloto=plushki_read()
        if boba == 0:
            boba = 1
            last_sleep = today()
            vremya(last_log, last_eat, last_toilet, last_sleep, last_lose, last_game)
        if krovat==1:
            screen.blit(fone_krepkiy_son,(0,0))
            son_time = 59
            if kak_davno(last_sleep) > timedelta(0, 59):
                stroka = "game"
        else:
            screen.blit(fone_son,(0,0))
            son_time = 120
            if kak_davno(last_sleep) > timedelta(0, 119):
                stroka = "game"
        if timedelta(0,son_time)-kak_davno(last_sleep) > timedelta(0,59):
            son_time_bobr = 2
        else:
            son_time_bobr = 5
        screen.blit(son_text2, (200,653))
        screen.blit(son_text, (200, 650))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.flip()
    elif stroka=="toiletmonsterwow":
        now = pygame.time.get_ticks()
        if aleg == 0:
            aleg = 1
            timer = sravn(today()) + timedelta(0,30)


        if popitkanol() == True:
            fone_maxito = fone_ultra_sad

        elif golodno() == True:
            fone_maxito = fone_hungry

        elif sleepym() == True:
            fone_maxito = fone_sleepy

        elif igratixoc() == True:
            fone_maxito = fone_sad

        elif kakati() == True:
            fone_maxito = fone_toilet

        else:
            fone_maxito = fone_good

        bgmenu = fone_maxito
        screen.blit(bgmenu, (0, 0))
        screen.blit(interface_button_up, (0, 0))
        screen.blit(interface_alph, (0, 0))
        screen.blit(interface_button_under, (0, 0))
        screen.blit(surface, (0, 0))



        # Кнопки нижнего меню

        button_eat = pygame.Rect(50, 660, 130, 120)
        pygame.draw.rect(surface, (255, 255, 255, 0), button_eat)

        button_toilet = pygame.Rect(230, 660, 130, 120)
        pygame.draw.rect(surface, (255, 255, 255, 0), button_toilet)

        button_sleep = pygame.Rect(420, 660, 130, 120)
        pygame.draw.rect(surface, (255, 255, 255, 0), button_sleep)

        # Кнопки верхнего меню

        button_info = pygame.Rect(0, 2, 100, 100)
        pygame.draw.rect(surface, (255, 255, 255, 0), button_info)

        button_game = pygame.Rect(313, 2, 100, 100)
        pygame.draw.rect(surface, (255, 255, 255, 0), button_game)

        button_inv = pygame.Rect(413, 2, 100, 100)
        pygame.draw.rect(surface, (255, 255, 255, 0), button_inv)

        button_shop = pygame.Rect(513, 2, 100, 100)
        pygame.draw.rect(surface, (255, 255, 255, 0), button_shop)

        screen.blit(toilet_text2, (190, 453))
        screen.blit(toilet_text, (190, 450))

        if sravn(today()) > timer:
            aleg = 0
            stroka = "game"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_info.collidepoint(pygame.mouse.get_pos()) or button_inv.collidepoint(
                    pygame.mouse.get_pos()) or button_game.collidepoint(
                    pygame.mouse.get_pos()) or button_shop.collidepoint(
                    pygame.mouse.get_pos()) or button_eat.collidepoint(
                    pygame.mouse.get_pos()) or button_sleep.collidepoint(
                    pygame.mouse.get_pos()) or button_toilet.collidepoint(pygame.mouse.get_pos()):
                    zapret30min()
        pygame.display.flip()