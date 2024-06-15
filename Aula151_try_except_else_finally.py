try:
    print('Tente abrir o arquivo')
    8/1

except ZeroDivisionError:
    print('Dividiu por zero ta errado')

else:
    print('ta certo')

finally:
    print('Fechar')