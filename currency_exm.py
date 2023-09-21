class currency:

    def pad(self, n):
        if n < 10:
            return "0"+str(n)
        else:
            return str(n)

    def __init__(self, rupees, paisa) -> None:
        self.paisa = rupees*100+paisa

    def __str__(self) -> str:
        r = self.paisa//100
        p = self.paisa % 100
        return "₹ {0},{1}".format(self.pad(r), self.pad(p))

    # add Oprator
    # rater

    def __add__(self, other):
        sum = currency(0, self.paisa+other.paisa)
        return sum

    # sub Oprator


    def __sub__(self, other):
        sum = currency(0, self.paisa-other.paisa)
        return sum

    # Mul Oprator


    def __mul__(self, other):
        sum = currency(0, self.paisa*other.paisa)
        return sum

    # True Div Oprator
    # rater

    def __truediv__(self, other):
        sum = currency(0, self.paisa/other.paisa)
        return sum

    # floor div Oprator


    def __floordiv__(self, other):
        sum = currency(0, self.paisa//other.paisa)
        return sum

    # Mod Oprator


    def __mod__(self, other):
        sum = currency(0, self.paisa % other.paisa)

        return sum

    # Pow Oprator


    def __pow__(self, other):
        sum = currency(0, self.paisa**other.paisa)
        return sum

    # rshift Oprator


    def __rshift__(self, other):
        sum = currency(0, self.paisa >> other.paisa)
        return sum

    # lshift Oprator


    def __lshift__(self, other):
        sum = currency(0, self.paisa << other.paisa)
        return sum

    # And Oprator


    def __and__(self, other):
        sum = currency(0, self.paisa & other.paisa)
        return sum

    # or Oprator


    def __or__(self, other):
        sum = currency(0, self.paisa | other.paisa)
        return sum

     # xor Oprator


    def __xor__(self, other):
        sum = currency(0, self.paisa ^ other.paisa)
        return sum
    
# Comparison Oprator

# lt Oprator

    def __lt__(self,other):
        return self.paisa<other.paisa
    
    # gt Oprator

    def __gt__(self,other):
        return self.paisa>other.paisa
    
    # le oprator
    def __le__(self,other):
        return self.paisa<=other.paisa
    
    #  ge Oprator
    def __ge__(self,other):
        return self.paisa>=other.paisa
    
    # eq Oprator

    def __eq__(self,other):

        return self.paisa==other.paisa
    
    # ne Oprator

    def __ne__(self,other):

        return self.paisa!=other.paisa

    



c1 = currency(1, 5)
c2 = currency(1, 5)


print("c1", c1)
print("c2", c2)
print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1/c2)
print(c1//c2)
print(c1 % c2)
print(c1**c2)
print(c1 >> c2)
print(c1 << c2)
print(c1 & c2)
print(c1 | c2)
print(c1^c2)


# Comparison Oprators

print(c2<c1)
print(c2>c1)
print(c2<=c1)
print(c2>=c1)
print(c2==c1)
print(c2!=c1)

# Assignment Optators