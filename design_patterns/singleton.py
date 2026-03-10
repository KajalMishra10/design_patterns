
import threading


class Restaurant:
    _instance = None
    lock = threading.Lock()
    def __new__(cls, name):
        if cls._instance is None:
            with cls.lock:
               if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.name = name
        return cls._instance
    

res1=Restaurant('McDonalds')
print(Restaurant._instance.name)  # Output: McDonalds
res2=Restaurant('Burger King')
print(Restaurant._instance.name)  # Output: McDonalds   
print(res1==res2)