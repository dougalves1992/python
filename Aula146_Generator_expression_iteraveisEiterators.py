import sys

iterable = ['EU', 'sou','_iter_']

iterator = iterable.__iter__() #tem que ter dois underline antes e depois

generator = (n for n in range(1000000))
print(sys.getsizeof(generator))
for i in generator:
    if i < 3069:
    
        print(i)
    
#se chamar mais um trava pq ele so vai até o ultimo