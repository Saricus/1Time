#Generatyory

def generator(end):
    n = 1
    #nums = []
    while n < end:
        yield n # zwracanie
        #nums.append(n)  
        n += 1
    #return nums

values = generator(100)

#print(values)

print(next(values))
print(next(values))
print(next(values))
print(next(values))

for v in values: #odwołanie do generatora
    print(v)

