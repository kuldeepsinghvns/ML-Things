class menu:

    def __init__(self,search,exit,add) -> None:
        
        self.search=search
        self.exit=exit
        self.add=add

    def __str__(self) -> str:
        return "Search={0},Exit={1},Add={2}".format(self.search,self.exit,self.add)
    
        