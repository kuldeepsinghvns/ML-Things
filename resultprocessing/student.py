class student:
    def __init__(self, rollno=None, name=None) -> None:
        if rollno is None:
            self.rollno = int(input("RollNo= "))
        else:
            self.rollno = rollno

        if name is None:
            self.name = input("Name= ")
        else:
            self.name = name

    def __str__(self) -> str:
        return "Name={0},Roll No={1}".format(self.name, self.rollno)
