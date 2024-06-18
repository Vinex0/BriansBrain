from cell import Cell
import numpy as np

class Grid:
    def __init__(self, n, m):
        self.grid = np.array([[Cell(0, 0) for _ in range(m)] for _ in range(n)])
    


    # Rules: 
    #   dead: nach dying    --> nur diese Uberprufen
    #   dying: nach alive
    #   alive: falls davor dead und genau 2 Zellen alive

    # Grid: nxn Matrix mit 0 = dead, 1 = dying, 2 = alive
    #   Option 1: nur Zustand 0, 1, 2 speichern, fur alle 0er Nachbarn betrachten
    #   Option 2: Zustand & Anzahl der lebenden Nachbarn in letztem (lebendeNachbarn1) und diesem (lebendeNachbarn2) Zyklus speichern, bei Wechsel von 0 -> 2 und 2 -> 1 alle Nachbarn aktuallisieren
    
    def update(self):
        for n in range(self.grid.shape[0]):
            for m in range (self.grid.shape[1]):
                print('UPDATE')
                print(n, m, self.grid[n, m].zustand, self.grid[n, m].lebendeNachbarn1, self.grid[n, m].lebendeNachbarn2)
                if(self.grid[n, m].zustand == 0 and self.grid[n, m].lebendeNachbarn1 == 2):
                    self.grid[n, m].zustand = 2
                    updateNachbarn(self.grid, 1, n, m)
                    print('ist erwacht')
                    print(n, m)
                elif self.grid[n, m].zustand == 1:
                    self.grid[n, m].zustand = 0
                elif self.grid[n, m].zustand == 2:
                    self.grid[n, m].zustand = 1
                    updateNachbarn(self.grid, -1, n, m)
        for n in range(self.grid.shape[0]):
            for m in range(self.grid.shape[1]):
                self.grid[n, m].lebendeNachbarn1 = self.grid[n, m].lebendeNachbarn2
    def erwacken(self, n, m): 
        self.grid[n, m].zustand = 2
        
        for nCount in range(-1, 2):
            for mCount in range(-1, 2):
                if not (nCount == 0 and mCount == 0):
                    nNeu = nCount + n
                    mNeu = mCount + m
                    if(nNeu < 0):
                        nNeu = self.grid.shape[0]-1
                    elif(nNeu >= self.grid.shape[0]):
                        nNeu = 0
                    if(mNeu < 0):
                        mNeu = self.grid.shape[1]-1
                    elif(mNeu >= self.grid.shape[1]):
                        mNeu = 0
                    
                    self.grid[nNeu, mNeu].lebendeNachbarn2 += 1
                    self.grid[nNeu, mNeu].lebendeNachbarn2 += 1

def updateNachbarn(grid, a, n, m): # a = 1 fur Nachbar lebendig, a = -1 fur Nachbar stirbt
    nNeu = 0
    mNeu = 0
    for nCount in range(-1, 2):
        for mCount in range(-1, 2):
            if not (nCount == 0 and mCount == 0):
                nNeu = nCount + n
                mNeu = mCount + m
                if(nNeu < 0):
                    nNeu = grid.shape[0]-1
                elif(nNeu >= grid.shape[0]):
                    nNeu = 0
                if(mNeu < 0):
                    mNeu = grid.shape[1]-1
                elif(mNeu >= grid.shape[1]):
                    mNeu = 0
                
                grid[nNeu, mNeu].lebendeNachbarn2 += a
                print('nachbar update 2')
                print(grid[nNeu, mNeu].lebendeNachbarn1)
                print(n, m)
                print(nNeu, mNeu)
                