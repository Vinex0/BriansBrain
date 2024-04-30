class Cell:
    def __init__(self, current_state=0, previous_state=0, neighbours_alive=0, neighbours) -> None:
        self.current_state = current_state #0 = off, 1 = dying, 2 = alive
        self.previous_state = previous_state
        self.neighbours_alive = neighbours_alive
        pass

    def update_neighbours(direction):
        if direction == -1:
            for neighbour in neighbours:
                neighbour.neighbours_alive -= 1

        elif direction == 1:
            for neighbour in neighbours:
                neighbour.neighbours_alive += 1

    def update_state():
        if self.neighbours_alive == 2 and current_state == 0:
            self.current_state = 2
            update_neighbours(1)

        elif self.current_state == 1:
            self.current_state  = 0

        elif self.current_state == 2:
            self.current_state = 1
            update_neighbours(-1)
