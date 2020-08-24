import time
from functools import wraps
def timer(func):
    @wraps(func)
    def inner(*args,**kwargs):
        start = time.time()
        re = func(*args,**kwargs)
        print(time.time() - start)
        return re
    return inner
 
@timer   #==> func1 = timer(func1)
def func1(a,b):
    print('in func1')
 
@timer   #==> func2 = timer(func2)
def func2(a):
    print('in func2 and get a:%s'%(a))
    return 'fun2 over'
 
func1('aaaaaa','bbbbbb')
print(func2('aaaaaa'))
print(func1.__name__)
print(func2.__name__)