
def type_check(func):
    def wrapper(*args, **kargs):

        info = func.__annotations__
        for inf in info:
            if inf in kargs.keys() and not isinstance(kargs[inf], info[inf]):
                raise Exception('Error!')
        
        var = func.__code__.co_varnames
        i = 0

        for v in var:
            if i < len(var) and v in info.keys() and not isinstance(args[i], info[v]):
                raise Exception(f'Error! Los parámetros de la función {func.__name__} están mal especificados.')
            i += 1
        
        f = func(*args, **kargs)
        
        if 'return' in info.keys() and info['return'] != None and not isinstance(f, info['return']):
            raise Exception(f'Error! La función {func.__name__} no devuelve el tipo especificado.')
        
        return f
    return wrapper

@type_check
def f1(x : int, y : str) -> str:
    return y * x

@type_check
def f2(name : str) -> None:
    print(f'hello {name}')

# print(f1(3, '1'))
# f2('ariel')