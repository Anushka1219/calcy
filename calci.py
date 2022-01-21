class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print(self.num1+self.num2)

    def mul(self):
        print(self.num1*self.num2)

    def div(self):
        print(self.num1/self.num2)

    def sub(self):
        print(self.num1-self.num2)


obj1=calculator(12,6)
obj1.add()
obj1.sub()
obj1.mul()
obj1.div()

obj2=calculator(20,5)
obj2.add()
obj2.mul()
obj2.sub()
obj2.div()

            
