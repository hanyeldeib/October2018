import math

def f(x):
    return math.pow(x,4)-3*math.pow(x,3)+2*math.pow(x,2)-1
 
def df(x):
    return 4*math.pow(x,3)-9*math.pow(x,2)+4*x
                  
def dx(f,x):    
    return abs(0-f(x))
 
def newtons_method(f, df, x0, e):
    delta = dx(f, x0)
    while delta > e:
        if abs(df(x0))>0:
            x0 = x0 - f(x0)/df(x0)
            print('current solution is: ', x0)
            delta = dx(f, x0)
        else:
            print('Derivative equals zero')
            x0=x0+0.1
    print ('Root is at: ', x0, 'f(X) = ', f(x0))
    

x0s = [1,2,3,4,5]
for x0 in x0s:
    print('x0 is: ',x0)
    newtons_method(f, df, x0, 1e-5)
 
