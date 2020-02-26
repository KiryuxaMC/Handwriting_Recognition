class Settings:
    '''Класс настроек приложения'''
    def __init__(self):
        # Натсройки игрового окна
        self.W = 500
        self.H = 400

        # Нстройки входного излбражения
        self.path = 'numbs/new.png'
        self.img_size = 28

        # Настройки поля рисования
        self.field_size = 200
        self.field_x = (self.W - self.field_size) // 2
        self.field_y = 80

        # FPS
        self.FPS = 210

        # Пременная для запуска процесса распознавания
        self.active_recognize = False

        # Настройки нейронной сети
        self.input_nodes = self.img_size**2
        self.hidden_nodes = 200
        self.output_nodes = 10
        self.rate = 0.1

        # Цвета
        self.white = 255, 255, 255
        self.red = 218, 0, 0
        self.blue = 12, 12, 255
        self.orange = 255, 111, 0
        self.black = 0, 0, 0