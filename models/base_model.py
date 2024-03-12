#!/usr/bin/python3
'''
This is my base model class where other classes will inherit from
'''
import uuid
from datetime import datetime

class BaseModel:
    '''The base model class'''
    def __init__(self, *args, **kwargs):
        '''Used to initialize the object, can take no arguments or key word arguments'''
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self,key,value)
        else:
            self.id = str(uuid.uuid4())
 
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        '''A string representation of an object'''
        return f"(<{self.__class__.__name__}>) ({self.id}) <{self.__dict__}>"
    
    def save(self):
        '''Called when a modification is done to an object'''
        self.updated_at = datetime.utcnow()
    
    def to_dict(self):
        '''Converts the Oject into a dictionary for it to be Serialized'''
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__ #Creating a new key __clas__ and asinging it the value of the objects class name
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()

        return my_dict

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print("--")
    print(type(my_model.created_at))
    
    