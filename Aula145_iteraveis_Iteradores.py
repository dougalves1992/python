iterable = ['EU', 'sou','_iter_']
iterator = iterable.__iter__() #tem que ter dois underline antes e depois

print(next(iterator))
print(next(iterator))
print(next(iterator))

#se chamar mais um trava pq ele so vai até o ultimo