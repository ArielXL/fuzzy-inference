from math import fabs
from utils.utils import Utils
from numpy import exp, linspace, fabs
from utils.type_check import type_check

class FuzzyModel:

    def __init__(self, aggregation='TSK', defuzzy='lom'):
        self.aggregation_methods = {
            'TSK'        : self.takagi_sugeno_kang,
            'Tsukamoto'  : self.tsukamoto
        }
        self.defuzzy_methods = {
            'centroid'   : self.centroid,
            'bisection'  : self.bisection,
            'lom'        : self.largest_of_max,
            'som'        : self.smallest_of_max,
            'mom'        : self.mean_of_max
        }

        self.rules = []
        self.variables = {}
        self.input_values = {}

        if aggregation not in self.aggregation_methods:
            raise Exception(f'Método de agregación no definido: {aggregation}.')
        elif defuzzy and defuzzy not in self.defuzzy_methods:
            raise Exception(f'Método de desdifusificación no definido: {defuzzy}.')
        
        self.aggregation = self.aggregation_methods[aggregation]
        self.defuzzy = self.defuzzy_methods[defuzzy]

    @type_check
    def add_input(self, name : str, var_type : str, value : int) -> None:
        '''
        Agrega una entrada al Modelo de Inferencia. Recibe el nombre 
        de la variable lingüística (string), su tipo (string) y su 
        valor (int). No devuelve nada.
        '''
        self.input_values[name] = {
            'variable_type'  : var_type,
            'function_value' : {
                i : self.variables[var_type][i](value) for i in self.variables[var_type]
            }
        }

    @type_check
    def add_variable(self, var_type : str, states : list, 
                                membership_function : list) -> None:
        '''
        Agrega una variable al Modelo de Inferencia. Recibe el nombre 
        de la variable lingüística (string), los valores lingüísticos 
        (List<string>) y las funciones de pertenencia de cada valor 
        (List<MembershipFunction>). No devuelve nada.
        '''
        self.variables[var_type] = {
            states[i] : membership_function[i] for i in range(len(states))
        }

    @type_check
    def add_rule(self, precondition : str, postcondition) -> None:
        '''
        Agrega una regla al Modelo de Inferencia. Recibe la 
        precondición (string) y la postcondición dependiendo del 
        método de agregación, si es TSK es una función 
        y si es Tsukamoto es un string.
        '''
        self.rules.append([precondition, postcondition])

    @type_check
    def solve(self) -> float:
        '''
        Resuelve el problema definido. No recibe nada. Devuelve la 
        solución (float).
        '''
        return self.aggregation()

    # region METODOS DE AGREGACION

    def takagi_sugeno_kang(self):
        numerator, denominator = 0, 0

        for rule in self.rules:
            tupla = tuple(Utils.Evaluate(self.input_values, rule[0]).values())
            numerator += rule[1](*tupla)
            denominator += min(tupla)

        if numerator == 0:
            return 0
        else:
            return numerator / denominator

    def tsukamoto(self):
        numerator, denominator = 0, 0

        for rule in self.rules:
            words = rule[1].split(' is ')
            function = self.variables[words[0]][words[1]]
            self.get_interval = function.get_interval()
            value = min(tuple(Utils.Evaluate(self.input_values, rule[0]).values()))
            numerator += value * self.defuzzy(lambda x: min(value, function(x)))
            denominator += value

        if numerator == 0:
            return 0
        else:
            return numerator / denominator

    # endregion

    # region METODOS DE DESDIFUSIFICACION

    def centroid(self, function):
        interval = self.get_interval
        numerator, denominator = 0, 0

        for i in linspace(interval[0], interval[1], 10 ** 4):
            numerator += i * function(i)
            denominator += function(i)

        if numerator == 0:
            return 0
        else:
            return numerator / denominator

    def bisection(self, function):
        interval = self.get_interval
        left, right, center = interval[0], interval[1], 0

        for _ in range(100):
            center = (left + right) / 2
            a = Utils.Area(function, [interval[0], center])
            b = Utils.Area(function, [center, interval[1]])

            if fabs(a - b) < 10 ** -6:
                return center
            elif a > b:
                r = center
            else:
                l = center

        return center

    def largest_of_max(self, function):
        interval = Utils.GetMaximun(function, self.get_interval)
        return interval[1]
    
    def smallest_of_max(self, function):
        interval = Utils.GetMaximun(function, self.get_interval)
        return interval[0]

    def mean_of_max(self, function):
        interval = Utils.GetMaximun(function, self.get_interval)
        return (interval[1] + interval[0]) / 2

    # endregion
