#  Band,
#     Musician,
#     Guitarist,
#     Bassist,
    # Drummer,
from abc import abstractclassmethod

'''
Defines the abstract base class Musician, which represents a musician who plays a musical instrument
'''
class Musician:
    def __init__(self,name):
        self.name = name

    @abstractclassmethod
    def __str__(self):
        pass
    '''
    __str__(): Returns a string representation of the musician

    '''

    @abstractclassmethod
    def __repr__ (self):
        pass   
    '''
    Returns a string representation of the musician that can be used to recreate the object
    ''' 
    
    @abstractclassmethod
    def get_instrument(self):
        pass
    '''
    Returns the name of the instrument played by the musician
    '''

    @abstractclassmethod
    def play_solo(self):
        pass


class Guitarist(Musician):
    '''
    Defines a concrete subclass of Musician called Guitarist, which represents a musician who plays guitar
    '''
    def __init__(self,name):
        super().__init__(name)
    '''
    Initializes a new Guitarist instance with the given name
    '''

    def __str__(self):
        return f'My name is {self.name} and I play guitar'
    '''
    Returns a string representation of the guitarist.
    '''

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'
    '''
    Returns a string representation of the guitarist that can be used to recreate the object
        '''
    
    def get_instrument(self):
        return f'guitar'
    '''
    Returns the name of the instrument played by the guitarist
    '''
    
    def play_solo(self):
        return 'face melting guitar solo'
    
    '''
    play_solo(): Plays a face-melting guitar solo
    '''




class Drummer(Musician):
    '''
    Defines a concrete subclass of Musician called Drummer, which represents a musician who plays drums
    '''
    def __init__(self,name):
        super().__init__(name)

  
    def __str__(self):
        return f'My name is {self.name} and I play drums'
    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'
    
    def get_instrument(self):
        return f'drums'    
    def play_solo(self):
        return "rattle boom crash"  




class Bassist(Musician): 
    # this is inheretens (Bassist(Musician))
    '''
    Defines a concrete subclass of Musician called Drummer, which represents a musician who plays Bassist
    '''
    def __init__(self, name):
        super().__init__(name)   
    
    def __str__(self):
        return f'My name is {self.name} and I play bass' 
    def __repr__(self) :
        return f'Bassist instance. Name = {self.name}'
    
    def get_instrument(self):
        return f'bass'
    
    def play_solo(self):
        return "bom bom buh bom"    
    
class Band :
    '''
    Defines a class called Band, which represents a musical band consisting of multiple musicians
    '''
    # 
    # inheretens : c The list of all instances of the Band class
    instances = []

    def __init__(self,name,members):
        self.name = name
        self.members = members
        Band.instances.append(self)
        
        
    
    def play_solos (self):
         solos = []
         for member in self.members:
             solos.append(member.play_solo())
         return solos     
         
    def __str__(self):
         return f'The {self.name} is the best band ever' 
           
    def __repr__(self):
         return f'{self.name}'    



    '''
     - This class does not inherit from any other class.
    - The `__init__` method takes a `name` argument, which is used to initialize the `name` attribute of the band, and a `members` argument, which is a list of Musician objects representing the members of the band. The `members` list can be empty.
    - The `play_solos` method invokes the `play_solo` method on each member of the band and returns a list of the resulting solos.
    - The `__str__` method returns a string that includes the name of the band.
    - The `__repr__` method returns a string that can be used to recreate the object.
    - The `instances` attribute is a class-level variable that keeps track of all instances of the Band class. It is initially an empty list, and is updated whenever a new Band instance is created.
"""
    '''
    @classmethod   
    def to_list(cls):
         return cls.instances 
    '''
    Returns a list of all instances of the Band class , it is called on the class itself, rather than on an instance of the class
    ( cls method referans to the class it self )
    '''