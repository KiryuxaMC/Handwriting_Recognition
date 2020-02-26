import pygame
from settings import Settings
from button import Button
from feather import Feather
import application_functions as af
import recognize as r

def main():

    # Подключение класса настроек
    sett = Settings()

    # Инициализация pygame, настройка экрана
    pygame.init()
    screen = pygame.display.set_mode((sett.W, sett.H))
    pygame.display.set_caption('Handwriting Recognition')

    # Создание кнопки Play
    rec_butt = Button(sett, screen, 'Recognize!')

    # Создание курсора в виде пера
    feat = Feather(screen, sett)

    # Список для координат точек при рисовании
    coords = []

    while not sett.active_recognize:

        # Обработка событий
        af.check_events(sett, rec_butt, screen, feat)
    
        # Обновление экрана
        af.update_screen(sett, screen, rec_butt, feat, coords)
    
    # Загрузка входного изображения
    af.load_image(sett, coords)

    # Отрисовка экрана на время распознавания 
    af.screen_recognize_update(sett, screen)
    
    # Процесс распознавания
    your_numb = r.recognize(sett)
    
    # Вывод на экран значения
    af.output_numb(sett, screen, your_numb)



if __name__ == '__main__':
    main()