#Ab projectEuler #263

def factornot35(num): #8 loops
    #factor module
    x=int(num**.5)+1
    faclist=[1]
    faclist.append(num)
    for i in range(2,x,15): #loop 1
        if num%i==0.0:
            faclist.append(i)
            faclist.append(num/i)
    for i in range(4,x,15): #loop 2
        if num%i==0.0:
            faclist.append(i)
            faclist.append(num/i)
    for i in range(7,x,15): #loop 3
        if num%i==0.0:
            faclist.append(i)
            faclist.append(num/i)
    for i in range(8,x,15): #loop 4
        if num%i==0.0:
            faclist.append(i)
            faclist.append(num/i)
    for i in range(11,x,15): #loop 5
        if num%i==0.0:
            faclist.append(i)
            faclist.append(num/i)
    for i in range(13,x,15): #loop 6
        if num%i==0.0:
            faclist.append(i)
            faclist.append(num/i)
    for i in range(14,x,15): #loop 7
        if num%i==0.0:
            faclist.append(i)
            faclist.append(num/i)
    for i in range(16,x,15): #loop 8
        if num%i==0.0:
            faclist.append(i)
            faclist.append(num/i)
    return faclist #return a list of factors

def factorall(num): #one loop
    x=int(num**.5)+1
    faclist=[1]
    faclist.append(num)
    for i in range(2,x): #loop 1
        if num%i==0.0:
            faclist.append(i)
            faclist.append(num/i)
    return faclist

def factornot3(num): #two loops
    x=int(num**.5)+1
    faclist=[1]
    faclist.append(num)
    for i in range(2,x,3): #loop 1
        if num%i==0.0:
            faclist.append(i)
            faclist.append(num/i)
    for i in range(4,x,3): #loop 2
        if num%i==0.0:
            faclist.append(i)
            faclist.append(num/i)
    return faclist

def factornot5(num): #four loops
    x=int(num**.5)+1
    faclist=[1]
    faclist.append(num)
    for i in range(2,x,5): #loop 1
        if num%i==0.0:
            faclist.append(i)
            faclist.append(num/i)
    for i in range(3,x,5): #loop 2
        if num%i==0.0:
            faclist.append(i)
            faclist.append(num/i)
    for i in range(4,x,5): #loop 3
        if num%i==0.0:
            faclist.append(i)
            faclist.append(num/i)
    for i in range(6,x,5): #loop 4
        if num%i==0.0:
            faclist.append(i)
            faclist.append(num/i)
    return faclist
    

def prime(num):
    #primecheck module
    x=int(num**.5)+1
    prime=True
    if num%2==0.0:
        prime=False
    if num%3==0.0:
        prime=False
    if num%5==0.0:
        prime=False
    if prime==True:
        for i in range(7,x,30): #loop 1
            if num%i==0:
                prime=False
                lowfac=i
                break
        if prime==True:
            for i in range(11,x,30): #loop 2
                if num%i==0:
                    prime=False
                    lowfac=i
                    break
            if prime==True:
                for i in range(13,x,30): #loop 3
                    if num%i==0:
                        prime=False
                        lowfac=i
                        break
                if prime==True:
                    for i in range(17,x,30): #loop 4
                        if num%i==0:
                            prime=False
                            lowfac=i
                            break
                    if prime==True:
                        for i in range(19,x,30): #loop 5
                            if num%i==0:
                                prime=False
                                lowfac=i
                                break
                        if prime==True:
                            for i in range(23,x,30): #loop 6
                                if num%i==0:
                                    prime=False
                                    lowfac=i
                                    break
                            if prime==True:
                                for i in range(29,x,30): #loop 7
                                    if num%i==0:
                                        prime=False
                                        lowfac=i
                                        break
                                if prime==True:
                                    for i in range(31,x,30): #loop 8
                                        if num%i==0:
                                            prime=False
                                            lowfac=i
                                            break
    return prime

def triplepair(n):
    w=n-9
    x=n-3
    y=n+3
    z=n+9
    triple=False
    if prime(w):
        if prime(x):
            if prime(y):
                if prime(z):
                    triple=True
    return triple

def factor(num):
    if num%3==0.0:
        if num%5==0.0:
            faclist=factorall(num)
        else:
            faclist=factornot5(num)
    elif num%5==0.0:
        faclist=factornot3(num)
    else:
        faclist=factornot35(num)
    return faclist

def practicalfast(i):
    factors=factor(i)
    factors.sort()
    result=True
    limit=1
    for i in factors:
        if i>limit:
            result=False
        limit=limit+i
    return result


def practicalset(num):
    a=num-8
    b=num-4
    c=num+4
    d=num+8
    result=False
    if practicalfast(a):
        if practicalfast(b):
            if practicalfast(num):
                if practicalfast(c):
                    if practicalfast(d):
                        
                        result=True
    return result

def triplecheck(n):
    result=True
    if prime(n-7):
        result=False
    elif prime(n-5):
        result=False
    elif prime(n-1):
        result=False
    elif prime(n+1):
        result=False
    elif prime(n+5):
        result=False
    elif prime(n+7):
        result=False
    return result

def main():
    go=raw_input("Go?")
    ans=[]
    for i in range (600000020,2000000000,24): #+2 sequence
        if triplepair(i):
            if triplecheck(i):
                if practicalset(i):
                    print i
                    ans.append(i)
        if i==700000028:
            print "we have passed 700000000"
                
#219869980 is the 1st engineer's paradise
#312501820 is the 2nd engineer's paradise
#360613700 is the 3rd engineer's paradise

main()
