class Cell:
    def __init__(self, zustand, lebendeNachbarn):
        self.zustand = zustand
        self.lebendeNachbarn1 = lebendeNachbarn
        self.lebendeNachbarn2 = lebendeNachbarn

    def __repr__(self):
        return f"Cell(zustand={self.zustand}, lebendeNachbarn1={self.lebendeNachbarn1})"
