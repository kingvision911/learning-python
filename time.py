import time 
import datetime

class Entity(object):
    def __init__(self, me):
        self.name = me
        self.time = time.time()

        self.date = datetime.date.fromtimestamp(self.time)
    def __str__(self):
        string1 = 'person %s started at %10.2fs,\n'\ % (self.name, self.time)

        string2 = 'which correspond to year %d , month %d , and day %d.')\ % (self.date.year,self.self.month,self.date.day)
        return string1 + string2
    def __repr__(self):
        return str(self)
    
    def set_name(self, new_name):
        self.name = new_name

    def service_time(self):
        return time.time() - self.time

