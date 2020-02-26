import pygame
from matplotlib import pyplot as plt
from PIL import Image

def check_events(sett, rec_butt, screen, feat):
    '''События приложения'''
    for event in pygame.event.get():
        # Выход из игры
        if event.type == pygame.QUIT:
            exit()

        # Событие клавиатуры
        elif event.type == pygame.KEYDOWN:
            # Выход из игры
            if event.key == pygame.K_ESCAPE:
                game_over(screen, sett, stats)
        
        # Событие мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                feat.visible = True
                check_recognize(sett, mouse_x, mouse_y, rec_butt)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                feat.visible = False

def check_recognize(sett, mouse_x, mouse_y, rec_butt):
    '''Запуск процедуры распознавания'''
    if rec_butt.rect.collidepoint(mouse_x, mouse_y):
        sett.active_recognize = True

def check_drawing(sett, mouse_x, mouse_y):
    '''Функция для проверки зоны рисования'''
    if mouse_x in list(range(sett.field_x,
                            sett.field_x + sett.field_size)) and \
       mouse_y in list(range(sett.field_y,
                            sett.field_y + sett.field_size)):
        return True

    return False
    
def draw_numb(mouse_x, mouse_y, sett, mass, feat, screen):
    '''Отрисовка цифры'''

    # Проверка курсора в пределах области
    if check_drawing(sett, mouse_x, mouse_y) and feat.visible:
        pygame.mouse.set_visible(False)
        feat.blit_me(mouse_x, mouse_y)
        mass.append((mouse_x, mouse_y))
    else:
        pygame.mouse.set_visible(True)

    # Отрисовка массива точек в области
    for c in mass:
        pygame.draw.rect(screen, 
                        sett.black, 
                        (c[0], c[1], 7, 7))

def update_screen(sett, screen, rec_butt, feat, mass):
    '''Функция обновления экрана'''

    # Координаты мыши
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Заливка экрана
    screen.fill(sett.white)

    # Отрисовка кнопки
    rec_butt.draw()

    # Отрисовка цифры
    draw_numb(mouse_x, mouse_y, sett, mass, feat, screen)


    # Надпись над полем рисования
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Draw your number:', 1, sett.black)
    screen.blit(label, 
                (sett.field_x + sett.field_size // 2 - (label.get_width() // 2),
                30))
    
    # Отрисовка поля рисования
    pygame.draw.rect(screen, 
                    sett.blue, 
                    (sett.field_x, sett.field_y, 
                    sett.field_size, sett.field_size), 6)

    pygame.display.update()
    pygame.time.Clock().tick(sett.FPS)

def screen_recognize_update(sett, screen):
    screen.fill(sett.black)
    font = pygame.font.SysFont('comicsans', 60)
    message = font.render('RECOGNITION', 1, sett.white)
    screen.blit(message, 
                (sett.W // 2 - message.get_width() // 2,
                sett.H // 2))

    pygame.display.update()
    pygame.time.Clock().tick(sett.FPS)

def load_image(sett, coords):
    '''Загрузка изображения '''

    # Значения координат по х и у
    x_values = [c[0] for c in coords]
    y_values = [c[1] for c in coords]

    # Делаем диаграмму изображения 
    plt.scatter(x_values, y_values, c='black', s=180)
    plt.axis('off')
    plt.savefig(sett.path)

    # Изменяем изображение для входных данных
    im = Image.open(sett.path)
    im = im.transpose(Image.ROTATE_180)
    im = im.transpose(Image.FLIP_LEFT_RIGHT)
    resized = im.resize((sett.img_size, sett.img_size), 
                        Image.ANTIALIAS)
    resized.save(sett.path)

def output_numb(sett, screen, value):
    '''Вывод знаения'''
    screen.fill(sett.black)
    font = pygame.font.SysFont('comicsans', 60)
    message = font.render('Your number:', 1, sett.white)
    screen.blit(message, 
                (sett.W // 2 - message.get_width() // 2,
                sett.H // 2 - 50))
    font = pygame.font.SysFont('comicsans', 80)
    numb = font.render(f'{value}', 1, sett.white)
    screen.blit(numb, 
                (sett.W // 2 - numb.get_width() // 2,
                sett.H // 2))
    pygame.display.update()
    pygame.time.delay(3000)