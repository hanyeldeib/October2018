import math

def f(x):
    return (math.tan(x))*(math.log(x))
 
def df(x):
    return (math.tan(x))/x + (math.log(x))*(1/(math.pow(math.cos(x),2)))
                  
def dx(f,x):    
    return abs(0-f(x))
 
def newtons_method(f, df, x0, e):
    delta = dx(f, x0)
    while delta > e:
        x0 = x0 - f(x0)/df(x0)
        print('current solution is: ', x0)
        delta = dx(f, x0)
    print ('Root is at: ', x0)
    print ('f(x) at root is: ', f(x0))

x0s = [1,2,3,4,5]
for x0 in x0s:
    print('x0 is: ',x0)
    newtons_method(f, df, x0, 1e-5)
 
