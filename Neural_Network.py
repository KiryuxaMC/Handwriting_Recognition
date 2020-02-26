import numpy as np
import scipy.special as sc

class NeuralNetwork:
    '''Класс нейронной сети'''
    def __init__(self, input_n, hidden_n, output_n, rate):
        '''Инициалзация слоёв и весов'''
        # Слои
        self.i_nodes = input_n
        self.h_nodes = hidden_n
        self.o_nodes = output_n
        self.l_rate = rate

        # Веса сети
        self.weight_h_i = np.random.normal(0.0, pow(self.h_nodes, -0.5), (self.h_nodes, self.i_nodes))
        self.weight_o_h = np.random.normal(0.0, pow(self.o_nodes, -0.5), (self.o_nodes, self.h_nodes))

        # Функция актвации
        self.activation = lambda x: sc.expit(x)
        
    def train(self, inputs_list, targets_list):
        '''Тренировка сети'''

        # Настройка входных данных во входной слой 
        inputs = np.array(inputs_list, ndmin = 2).T
        targets = np.array(targets_list, ndmin = 2).T

        # Расчёт входных и выходных сигналов для скрытого слоя
        hidden_inputs = np.dot(self.weight_h_i, inputs)
        hidden_outputs = self.activation(hidden_inputs)

        # Расчёт входных и выходных сигналов для выходного слоя
        final_inputs = np.dot(self.weight_o_h, hidden_outputs)
        final_outputs = self.activation(final_inputs)

        # Расчёт ошибок
        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.weight_o_h.T, output_errors)

        # Перерaчёт весов при наличии ошибок
        self.weight_o_h += self.l_rate*np.dot(output_errors*final_outputs*(1.0 - final_outputs), np.transpose(hidden_outputs))
        self.weight_h_i += self.l_rate*np.dot(hidden_errors*hidden_outputs*(1.0 - hidden_outputs), np.transpose(inputs))

    def query(self, input_list):
        '''Расчёт сигналов на слоях'''

        # Настройка входных данных во входной слой 
        inputs = np.array(input_list, ndmin = 2).T

        # Расчёт входных и выходных сигналов для скрытого слоя
        hidden_inputs = np.dot(self.weight_h_i, inputs)
        hidden_outputs = self.activation(hidden_inputs)

        # Расчёт входных и выходных сигналов для выходного слоя
        final_inputs = np.dot(self.weight_o_h, hidden_outputs)
        final_outputs = self.activation(final_inputs)

        # Вывод сигналов выходного слоя
        return final_outputs
