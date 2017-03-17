import logging

logger  =  logging.getLogger()
handler  = logging.FileHandler("log.txt")
logger.addHandler(handler)
logger.setLevel(logging.NOTSET)
# def use_logging(func):
#     logging.warn("%s is running" % func.__name__)
#     func()
# def bar():
#     print('i am foo')
#     
   
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')
        

@Foo
def bar():
    print ('bar')

bar()



# def use_logging(func):

#     def wrapper(*args, **kwargs):
#         logging.warn("%s is running" % func.__name__)
#         return func(*args, **kwargs)
#     return wrapper

# def bar():
#     print('i am bar')



# # use_logging(bar)
# bar = use_logging(bar)
# bar()