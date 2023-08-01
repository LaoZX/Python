import random
def PI(n):
    inCircle = 0
    for i in range(n):
        x=random.uniform(0, 1)
        y=random.uniform(0, 1)
        d= (x-0.5)**2 + (y-0.5)**2
        if d<0.25:
            inCircle+=1
    return 4 * ( inCircle / n )

for i in range(10):
    for exp in range(6):
        print('N= %d: %f'%(10**exp, PI(10**exp)))