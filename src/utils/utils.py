from numpy import linspace

class Utils:

    def Evaluate(input_values, preconditions):
        result, term, operation, negate = {}, [], None, False
        preconditions = preconditions.split()

        for precondition in preconditions:
            if precondition == 'not':
                negate = True
                continue
            if precondition == 'and' or precondition == 'or':
                operation = precondition
                continue
            if precondition == 'is':
                continue
            
            term.append(precondition)
            if len(term) == 2:
                e = input_values[term[0]]['function_value'][term[1]]
                variable, term = term[0], []

                if negate:
                    e = 1 - e
                    negate = False
                if operation is None or variable not in result:
                    result[variable] = e
                else:
                    if operation == 'and':
                        result[variable] = min(result[variable], e)
                    else:
                        result[variable] = max(result[variable], e)

        return result

    def Area(function, interval):
        area = 0
        for i in linspace(interval[0], interval[1], 100):
            area += function(i)
        return area

    def GetMaximun(function, interval):
        minimum, maximum, value = 10 ** 9, -10 ** 9, -10 ** 9

        for i in linspace(interval[0], interval[1], 10 ** 4):
            if function(i) > value:
                minimum = maximum = i 
                value = function(i)
            if abs(function(i) - value) < 10 ** -9:
                minimum = min(minimum, i)
                maximum = max(maximum, i)
                
        return minimum, maximum

