'''
Created on Feb 23, 2018

@author: Sagar Bayar
'''
import timeit

def fib(n):
    a,b=0,1
    while a<n:
        print(a,end='')
        a,b=b,a+b
        print()
start=timeit.default_timer()
fib(9135431354684231638546513216859468635216548967465163216854651321356476513216546546541654654165465465465465465465463646541246846516354968621685496846541687961635416846516354684652168765135241684684999999999999999999999999999999999999999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000019846849685496846484684646846448684864468484646464646464646464846464846846846546846546846546846568464684646546984654684685465468461684654165496846894)
stop=timeit.default_timer()
print()
print("Start:",start," Stop:",stop," Total Time:",stop-start)

