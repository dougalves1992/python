import importlib

import Aula133_lambda_anon

print(Aula133_lambda_anon.variavel)

for i in range(10):
    importlib.reload(Aula133_lambda_anon)
    print(i)

print('Fim')