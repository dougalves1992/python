

try:
    a = 18
    b = 0
    c = a/b
except ZeroDivisionError:
    print('ERRO - Não é possivel dividir por zero')

except NameError:
    print(' nome "b" não definido' )

except TypeError:
    print('tipo de "B" não é suportado')

except SyntaxError:
    print('você esqueceu de atribuir valor a variavel b')

except Exception:
    print('Erro desconhecido!')
    


print(' funcionou')