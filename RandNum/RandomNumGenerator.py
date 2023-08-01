def Rand1(n):
    x = 53402397  # Seed
    rand_seq = []
    
    for i in range(n):
        x = 65539 * x + 125654
        if x < 0:  # Check for overflow
            x += 2147483647  # +(M-1)
            x += 1
        rand_seq.append(x)
    return rand_seq

def Rand2(n):
    x=1
    A=48271
    M=21474836447
    Q = M // A #floor division
    R = M % A
    rand_seq=[]
    for i in range(n):
        x = A * (x % Q) - R * (x // Q)
        if x<0:
            x+=M
        rand_seq.append(x)
    return rand_seq

def Rand3(n):
    x=1
    next=0
    A=Rand2(55)
    rand_seq=[]
    for i in range(n):
        j=(next+31)%55
        x=A[j]-A[next]
        if x<0:
            x+= 2147483647
            x+=1
        A[next]=x
        next = (next + 1) % 55
        rand_seq.append (x)
    return rand_seq
                

num_of_int = 5
sequence1 = Rand1(num_of_int)
sequence2 = Rand2(num_of_int)
sequence3 = Rand3(num_of_int)

print('Rand1 sequence is ',sequence1)
print('Rand2 sequence is ',sequence2)
print('Rand3 sequence is ',sequence3)
