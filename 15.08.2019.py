"""def exceptionexted():

    try :
        s=['a','b','c','d']
        p=s[10]
    except ZeroDivisionError:
        print('zer0 division error')
    except ValueError:
        print('value error')
    except RuntimeError:
        print('other')
    except NameError:
        print("name error")
    except IndexError:
        print("index error")
exceptionexted()
"""
"""
def raise_example():
    try:
        z=[]
        a=z[10]
    except IndexError:
        raise RuntimeError( "index out of bound")

raise_example()
"""

class time:
    def hours(self):
        print("hours")
    def mints(self):
        print("mints")
    def secs(self):
        print("seconds")

if __name__=='__main__':
    ob=time()
    ob.hours()
    ob.mints()
       ob.secs()
    print(ob.secs)



