from time import perf_counter

#initialize global variables
cache = {}
cacheHit = 0
counter = 0
counter2 = 0

#initial recursive function
def weightOn(r,c):
    global counter
    counter += 1
    if c > r:
        return 0
    if r == 0:
        return 0
    if c == 0:
        return 100 + (weightOn(r-1,c))/2
    if c == r:
        return 100 + (weightOn(r-1,c-1))/2
    else:
        return 200 + (weightOn(r-1,c)+ weightOn(r-1,c-1))/2

#recursive function using cache
def weightOnCache(r,c):
    global counter2
    global cache
    global cacheHit
    counter2 += 1
    if (r,c) in cache:
        cacheHit += 1
        return cache[(r,c)]
    else:
        cache[(r,c)] = weightOn(r,c)
        if c > r:
            return 0
        if r == 0:
            return 0
        if c == 0:
            return 100 + (weightOnCache(r-1,c))/2
        if c == r:
            return 100 + (weightOnCache(r-1,c-1))/2
        else:
            return 200 + (weightOnCache(r-1,c)+ weightOnCache(r-1,c-1))/2

#Create part2.txt to turn in 
def part2(num):
    f = open('part2.txt','w')
    start = perf_counter()
    
    for i in range(int(num)):
        line = ''
        for x in range(i+1):
            line += str("{:.2f}".format(weightOn(i, x)))
            line += " "
        f.write(f'\n{line}')
    end = perf_counter()
    f.write(f"\n\nElapsed time: {end - start} seconds")
    f.write(f'\nNumber of function calls: {counter}')
    f.close()


#Create cache manualy outisde of function
'''for i in range(20):
    for x in range(i+1):
        if weightOn(i,x) in cache:
            pass
        else:
            cache[(i,x)] = weightOn(i,x)'''
            
#Create part3.txt to turn in
def part3(num):
    t = open('part3.txt','w')
    start = perf_counter()
    for i in range(int(num)):
        line = ''
        for x in range(i+1):
            line += str("{:.2f}".format(weightOnCache(i, x)))
            line += " "
        t.write(f'\n{line}')
    end = perf_counter()
    t.write(f"\n\nElapsed time: {end - start} seconds")
    t.write(f'\nNumber of function calls: {counter2}')
    t.write(f'\nNumber of cache hits: {cacheHit}')
    t.close()