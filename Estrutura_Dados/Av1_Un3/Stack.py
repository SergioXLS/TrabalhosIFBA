class Stack:
    def __init__(self):
        self.itens = []

    def is_Empty(self):
        return self.itens == []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.is_Empty():
            return self.itens.pop()

    def peek(self):
        if not self.is_Empty():
            return self.itens[-1]
        else:
            return []
    
    def size(self):
        return len(self.itens)
    
    def __str__(self):
        return str(self.itens)
