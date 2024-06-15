string =  "asdasdas"
metodo = 'upper'

if hasattr(string, 'upper'):
    print('existe upper')
    print(getattr(string, metodo)())
    print(string)
else:
    print ('Checagem falhou')
