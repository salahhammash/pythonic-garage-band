#  Band,
#     Musician,
#     Guitarist,
#     Bassist,
    # Drummer,
from abc import abstractclassmethod


class Musician:
    def __init__(self,name):
        self.name = name

    @abstractclassmethod
    def __str__(self):
        pass

    @abstractclassmethod
    def __repr__ (self):
        pass    
    
    @abstractclassmethod
    def get_instrument(self):
        pass

    @abstractclassmethod
    def play_solo(self):
        pass



class Guitarist(Musician):
    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f'My name is {self.name} and I play guitar'
    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'
    def get_instrument(self):
        return f'guitar'
    
    def play_solo(self):
        return 'face melting guitar solo'
    

class Drummer(Musician):
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
    # inheretens : c
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

    @classmethod   
    def to_list(cls):
         return cls.instances 