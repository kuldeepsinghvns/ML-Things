class Subject:

    def __init__(self, name=None, maxmarks=None, minmarks=None, obtainedmarks=None) -> None:
        if name is None:
            self.name = input("Name= ")
        else:
            self. name = name
        if maxmarks is None:
            self.maxmarks=int(input("Max Marks= "))
        else:
            self.maxmarks = maxmarks

        if minmarks is None:
            self.minmarks=int(input("Min Marks= "))
        else:
            self. minmarks = minmarks
        if obtainedmarks is None:
            self.obtainedmarks=int(input("Obtained Marks= "))
        else:
            self.obtainedmarks = obtainedmarks

    def __str__(self) -> str:

        return "Name={0},Max Marks={1},Min Marks={2},Obitan Marks{3}".format(self.name, self.maxmarks, self.minmarks, self.obtainedmarks)
