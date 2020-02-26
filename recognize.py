from Neural_Network import NeuralNetwork as NN
import scipy.misc as smc
import numpy as np


def recognize(sett):
    '''Обучение и тестирование нейронной сети'''

    # Инициализация экземпляра нейроннйо сети
    nn = NN(sett.input_nodes, 
            sett.hidden_nodes, 
            sett.output_nodes, 
            sett.rate)

    # Загрузка тренировочных данных
    training_data = open("dataset/mnist_train_100.csv", 'r')
    training_list = training_data.readlines()
    training_data.close()

    # Обучение
    for _ in range(5):
        for record in training_list:
            all_values = record.split(',')
            inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
            targets = np.zeros(sett.output_nodes) + 0.01
            targets[int(all_values[0])] = 0.99
            nn.train(inputs, targets)

    # Загрзука тестовых данных
    test_data = open("dataset/mnist_test_10.csv", 'r')
    test_list = test_data.readlines()
    test_data.close()

    score_card = []

    # Тестирование сети
    for record in test_list:
        all_values = record.split(',')
        correct_val = int(all_values[0])
        inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        outputs = nn.query(inputs)
        network_val = np.argmax(outputs)
        score_card.append( 1 if correct_val == network_val else 0 )

    # Загрузка входного изображения и преобразование его в массив
    img_array = smc.imread("numbs/new.png", flatten=True)
    img_data = 255.0 - img_array.reshape(784)
    img_data = (img_data / 255.0 * 0.99) + 0.01

    # Выходные сигналы
    outputs_new = nn.query(img_data)

    # Значение цифры, которое имеет наибольший процент сходства с изображением
    network_val = np.argmax(outputs_new)
    return network_val