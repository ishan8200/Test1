class Student():
    def __init__(self,name,maths,science,english):
        self.name=name
        self.maths=maths
        self.science=science
        self.english=english
    def get_lname(self):
        lname =self.name.split() 
        return lname[-1]
    def get_average(self):
        total= self.maths+self.science+self.english
        return total/3

s1 = Student("Harry Potter", 80, 80, 80)
print(s1.get_lname()) # prints Potter
print(s1.get_average()) # prints 80
