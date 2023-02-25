import pygame


pygame.init()

width = 1000                                #ширина игрового окна
height = 650                             #высота игрового окна
fps = 10                        #частота кадров в секунду
game_name = 'Музыка'          #название нашей игры

speedx = 1                             #Скорость движения по горизонтали
speedy = 1                             #Скорость движения по вертикали


BLACK = "#000000"       #Черный
WHITE = "#FFFFFF"       #Белый
RED = "#FF0000"         #Красный
GREEN = "#008000"       #Зеленый
BLUE = "#0000FF"        #Синий
CYAN = "#00FFFF"        #Голубой


screen = pygame.display.set_mode((width, height))  #делаем игровое окно игре
pygame.display.set_caption(game_name)  #делаем надпись названия игры

icon = pygame.image.load('unnamed.png')         #Загружаем файл с иконкой
pygame.display.set_icon(icon)                #Устанавливаем иконку в окно


pic = pygame.image.load('dvd.png')     #Загружаем спрайт
pic_rect = pic.get_rect()                #Получаем рамку спрайта

def drawText(screen, text, size, x, y, color):  #переменная
    fontname = './Bradley Hand Bold.ttf'  #шрифт текста  #переменная
    font = pygame.font.Font(fontname, size)  #шрифт текста и размер
    textsprite = font.render(text, True, color)  #цвет текста  #переменная
    textrect = textsprite.get_rect()  #переменная
    screen.blit(textsprite, textrect)  #прорисовали текст

def drawText1(screen, text, size, x, y, color):  #переменная
    fontname = './Bradley Hand Bold.ttf'  #шрифт текста  #переменная
    font = pygame.font.Font(fontname, size)  #шрифт текста и размер
    textsprite = font.render(text, True, color)  #цвет текста  #переменная
    textrect = textsprite.get_rect()  #переменная
    screen.blit(textsprite, textrect)  #прорисовали текст

egor = (input('Введите название музыки: Hello Neighbour/Заяц/Лес/Луна/Джулия '))
if egor == 'Hello Neighbour':
    pygame.mixer.music.load('Hello Neighbor г.з — копия.wav')
    pygame.mixer.music.play()
    pygame.mixer.music.play(-1)
elif egor == 'Заяц':
    pygame.mixer.music.load('Заяц--3.wav')
    pygame.mixer.music.play()
    pygame.mixer.music.play(-1)
elif egor == 'Лес':
    pygame.mixer.music.load('Музыка-лес.wav')
    pygame.mixer.music.play()
    pygame.mixer.music.play(-1)
elif egor == 'Луна':
    pygame.mixer.music.load('Музыка-Луна-_1.wav')
    pygame.mixer.music.play()
    pygame.mixer.music.play(-1)
elif egor == 'Джулия':
    pygame.mixer.music.load('Никольская-улица.wav')
    pygame.mixer.music.play()
    pygame.mixer.music.play(-1)
else:
    print('Такой мелодии не существует')
    quit()


run = True                            #переменная для управления циклом
while run:                            #начинаем бесконечный цикл
    clock = pygame.time.Clock()  #Создаем таймер pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #закрытие окна
            run = False

    pic_rect.x += speedx  #Увеличиваем координату Х спрайта
    pic_rect.y += speedy  #Увеличиваем координату Y спрайта
    if pic_rect.bottom > height:  #Если достигли нижней границы экрана
        speedy = -speedy
    if pic_rect.top < 0:  #Если достигли верхней границы экрана
        speedy = -speedy
    if pic_rect.left < 0:  #Если достигли левой границы экрана
        speedx = -speedx
    if pic_rect.right > width:  #Если достигли правой границы экрана
        speedx = -speedx

    key = pygame.key.get_pressed()  # Считываем нажатия на клавиши
    if key[pygame.K_SPACE]:
        pygame.mixer.music.pause()
    key = pygame.key.get_pressed()  # Считываем нажатия на клавиши
    if key[pygame.K_w]:
        pygame.mixer.music.unpause()
    if key[pygame.K_ESCAPE]:
        run = False
    key = pygame.key.get_pressed()  # Считываем нажатия на клавиши
    screen.fill(GREEN)  #Заливка заднего фона
    screen.blit(pic, pic_rect)  #Отрисовываем спрайт с рамкой
    drawText(screen, str('Для того чтобы поставить на паузу нажмите пробел, а чтобы снять с паузы нажмите w'), 20, 86, 87, CYAN)
    pygame.display.update()  #Обновляем экран
