class Vector:
    def __init__(self, n):
        """Creating a zero vector of n dimension"""
        self.vctr = [0]*n

    def __len__(self):
        """Returns the dimension of the vector"""
        return len(self.vctr)
    
    def __getitem__(self, j):
        """Returns the jth element of the vector"""
        return self.vctr[j]
    def __setitem__(self, j, value):
        self.vctr[j] = value
        
    def __add__(self,other):
        """Returns the sum of two vector"""
        if len(self) != len(other):
            raise ValueError("Dimension must agree")
        result = Vector(len(self))    
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result    
            
    def __mul__(self, other):
        """Scalar multiplication of two vectors"""
        if len(self) != len(other):
            raise ValueError("Vector must have same length")
        product = Vector(len(self))
        for i in range(len(self)):
            product[i] = self[i]*other[i]
        return product

u = Vector(10)
for i in range(len(u)):
    u.__setitem__(i, 2*i)    

v = Vector(10)
for i in range(len(v)):
    v.__setitem__(i, 3*i)
    
w = u*v
for i in range(len(w)):
    print(w.__getitem__(i))      
         
