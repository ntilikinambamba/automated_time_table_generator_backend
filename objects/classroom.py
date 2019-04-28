#  Copyright (c) 2019.  Hex Inc.
#  Author: Akola Denis
#  Date: 13/04/2019
#  Time: 01:27

class Classroom(object):
    """classroom allocation class specifies the capacity of a class,the location
                
                Attributes
                ----------
                
                name : str
                ' the name of the classroom
                capacity : int
                   the capacity of the class room/the number of students the classroom can occupy a particular lecture room
                location : int
                    the location of the class room
                 
                    """

<<<<<<< HEAD
    def __init__(self, name, capacity, location=''):
        'the constructor for this class specifies the classroom name,the capacity,the location of the class'
        self._name = name
        self._capacity = capacity
        self._location = location

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.name == other.name and self.capacity == other.capacity and \
                   self.location == self.location
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(self, other.__class__):
            return self.name != other.name or self.capacity != other.capacity or \
                   self.location != self.location
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.name, self.capacity, self.location))

    def __str__(self):
        return "Room:" + self._name + '\t' + "Capacity :" \
               + str(self._capacity)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    def can_accomodate(self, size, allowance=0):
        return (self._capacity + allowance) >= size
=======
                def __init__(self,name,capacity):
                    self.name=name
                    self.capacity=capacity
                    #self._location=location

                def __eq__(self,other):
                    if isinstance(self,other.__class__):
                        return self.name == other.name and self.capacity == other.capacity# and\
                            #self.location == self.location
                    else:
                        return NotImplemented

                def __ne__(self, other):
                    if isinstance(self,other.__class__):
                        return self.name != other.name or self.capacity != other.capacity #or\
                            #self.location != self.location
                    else:
                        return NotImplemented

                def __hash__(self):
                        return hash((self.name,self.capacity))

                def __str__(self):
                    return "Room:"+ self._name+'\t'+"Capacity :"\
                        +str(self._capacity)  
                
                @property
                def name(self):
                    return self._name

                @name.setter      
                def name(self,new_name):
                    #TODO
                    #validate, new_name cannot be empty
                    self._name=new_name
                
                @property 
                def capacity(self):
                    return self._capacity

                @capacity.setter
                def capacity(self,capacity):
                    #TODO
                    #capacity should not be negative
                    self._capacity=capacity

                #@property
                #def location(self):
                 #   return self._location

                #@location.setter
                #def location(self,location):
                 #   self._location=location

                def can_accomodate(self,size,allowance=0):
                    return (self._capacity + allowance) >= size

                
               
                 
                    
                



                

>>>>>>> 606e1e09f411f3099ad835c32cbdc11365b7a368
