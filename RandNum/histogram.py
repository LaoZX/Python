#lcg
def Rand1(n,seed,A,C,M):
    x = seed
    rand_seq = []
    
    for i in range(n):
        x = (A * x + C ) % M
        if x < 0:  # Check for overflow
            x += (M+1)
            x += 1
        rand_seq.append(x/M)
    return rand_seq

def Rand2(n,seed,A,M):
    x=seed
    Q = M // A #floor division
    R = M % A
    rand_seq=[]
    for i in range(n):
        x = A * (x % Q) - R * (x // Q)
        if x<0:
            x+=M
        rand_seq.append(x/M)
    return rand_seq

#subtractive
def Rand3(n,seed,A,C,M):
    L=[0]*55
    L[0]=seed
    for i in range(1,55):
        L[i]=(A*L[i-1]+C)%M
    rand_seq=[]
    for j in range(n):
        x = (L[-24] - L[-55]) % (M+1)
        L.append(x)
        rand_seq.append(x / M)
    return rand_seq

def calculate_histogram(random_numbers):
    intervals = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    histogram = [0] * (len(intervals) - 1)
    for num in random_numbers:
        for i in range(len(histogram)):
            if intervals[i] <= num < intervals[i + 1]:
                histogram[i] += 1
                break

    total_numbers = len(random_numbers)
    #print(histogram)
    histogram_percentage = [count / total_numbers for count in histogram]

    return histogram_percentage

N = [10, 1000, 1000000]

results = {}
seed=53402397
A=65539
C=125654
M=2147483647



for n in N:
    print ('N=',n)
    rand1_seq =Rand1(n,seed,A,C,M)
    #print(rand1_seq)
    print('Rand1 histogram',calculate_histogram(rand1_seq))

    rand2_seq=Rand2(n,seed,A,M)
    #print(rand2_seq)
    print('Rand2 histogram',calculate_histogram(rand2_seq))

    rand3_seq=Rand3(n,seed,A,C,M)
    #print(rand3_seq)
    print('Rand3 histogram',calculate_histogram(rand3_seq))

