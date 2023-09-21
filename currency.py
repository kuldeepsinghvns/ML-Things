class Currency:
    def pad(self, n):
        if n < 10:
            return "0" + str(n)
        else:
            return str(n)
    
    def __add__(self,other):
        # print("add",self,other)
        c=Currency(0,self.paisa+ other.paisa)
        return c

    def __init__(self, rupees, paisa) -> None:
        self.paisa = rupees*100 + paisa

    def __str__(self) -> str:
        r = self.paisa//100
        p = self.paisa % 100
        return "₹ {0}.{1}".format(self.pad(r), self.pad(p))
    def __lt__(self,other):
        return self.paisa<other.paisa

    def __le__(self,other):
        return self.paisa<=other.paisa


c1 = Currency(1, 5)
c2=Currency(1,5)
print(c1,c2)
sum=c2+c1+c1
print(sum)
print(c2<c1)
print(c2<=c1)
