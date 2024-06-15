# def generator(n=0):
#     yield 1 #parou
#     print('Continuando')
#     yield 2
#     print('Continuando')
#     yield 10
#     print('ok')
#     return 'stop'

# gen =generator()
# for i in gen:
#     print(i)

def generator (n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return
        
gen = generator(maximum=10000)
for n in gen:
    print(n)