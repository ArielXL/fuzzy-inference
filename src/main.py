from utils.type_check import type_check
from fuzzy.fuzzy_model import FuzzyModel
from fuzzy.membership_function import MembershipFunction

def adding_inputs(fuzzy_model):
    fuzzy_model.add_input('cola', 'tamaño', 19)
    fuzzy_model.add_input('tenderos', 'velocidad', 2)

def adding_variables(fuzzy_model):
    fuzzy_model.add_variable(
        'tamaño',
        [ 'larga', 'normal', 'corta' ],
        [
            MembershipFunction.Trapesoid(10, 15, 30, 30, 0, 30),
            MembershipFunction.Trapesoid(8, 9, 11, 12, 0, 30),
            MembershipFunction.Trapesoid(0, 0, 7, 10, 0, 30)
        ]
    )
    fuzzy_model.add_variable(
        'velocidad',
        [ 'lenta', 'normal', 'rapida' ],
        [
            MembershipFunction.Trapesoid(0, 0, 3, 5, 0, 5),
            MembershipFunction.Triangle(1, 2, 3, 0, 5),
            MembershipFunction.Trapesoid(2, 3, 5, 5, 0, 5)
        ]
    )
    fuzzy_model.add_variable(
        'bronca',
        [ 'alta', 'normal', 'baja' ],
        [
            MembershipFunction.Trapesoid(50, 60, 100, 100, 0, 100),
            MembershipFunction.Triangle(40, 50, 60, 0, 100),
            MembershipFunction.Trapesoid(0, 0, 50, 40, 0, 100)
        ]
    )

def adding_rules(fuzzy_model):
    # fuzzy_model.add_rule('tenderos is lenta', lambda x: 100)
    # fuzzy_model.add_rule('cola is larga', lambda x: 100)
    # fuzzy_model.add_rule('cola is normal and tenderos is normal', lambda x, y: x*y)

    fuzzy_model.add_rule('cola is larga or tenderos is lenta', 'bronca is alta')
    fuzzy_model.add_rule('cola is normal and tenderos is normal or cola is corta', 'bronca is normal')
    fuzzy_model.add_rule('cola is corta and tenderos is rapida', 'bronca is baja')

def main():

    # fuzzy_model = FuzzyModel(aggregation='TSK', defuzzy='lom')
    fuzzy_model = FuzzyModel(aggregation='Tsukamoto', defuzzy='lom')

    adding_variables(fuzzy_model)
    adding_inputs(fuzzy_model)
    adding_rules(fuzzy_model)
    solution = '%0.3f' % fuzzy_model.solve()

    print(f'La probabilidad de pelea es de {solution} %.')

if __name__ == "__main__":
    main()
