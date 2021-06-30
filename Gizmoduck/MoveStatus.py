
class MoveStatus:
    
    def __init__(self):
        self.left = False
        self.right = False
        self.firstAxis = False
        self.secondAxis = False
        
    def setLeft(self, move):
        self.left = move
        
    def setRight(move):
        self.right = move
        
    def setFirstAxis(move):
        self.firstAxis = move
        
    def setSecondAxis(move):
        self.secondAxis = move
        
    def getLeft(self):
        return self.left
        
    def getRight(move):
        self.right = move
        
    def getFirstAxis(move):
        self.firstAxis = move
        
    def getSecondAxis(move):
        self.secondAxis = move