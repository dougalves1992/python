try:
    a = 18
    b = 'a'
    c = a/b
except ZeroDivisionError:
    print('ERRO - Não é possivel dividir por zero')

except NameError:
    print(' nome "b" não definido' )

except (TypeError, IndexError) as error :
    print('TypeError, IndexError')
    print('Msg:', error)
    print('Nome', error.__class__.__name__ )

except SyntaxError:
    print('você esqueceu de atribuir valor a variavel b')

except Exception:
    print('Erro desconhecido!')
    


print(' funcionou')