from tkinter import*
from random import*

root = Tk()
root.title("Map Generator")

canvas = Canvas(root, width=1000, height=1000, bg="white")
canvas.pack()

# Variable Init
x1 = 0
y1 = 0
x2 = 10
y2 = 10
length = 10
grid = [] # Populate with dictionary of posx, posy




def generate_grid():
    """Generates the grid"""
    global x1, x2, y1, y2
    gridx = 1
    gridy = 1
    while True:
        canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black") # Adds a blank square in grid
        grid.append({"gridx": gridx, "gridy": gridy, "status": "empty"})
        x1 += length
        x2 += length
        gridx += 1

        if x2 == 1010:
            x1 = 0
            x2 = 10
            y1 += length
            y2 += length
            gridx = 1
            gridy += 1

        if y2 == 1010:
            break


def create_grass(generations):
    """Creates Random Grass"""
    global x1, x2, y1, y2

    while generations != 0:  
        posx = randint(1, 100)
        posy = randint(1, 100)
        x1 = posx * 10
        y1 = posy * 10
        x2 = x1 + length
        y2 = y1 + length
        canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="black")
        generations -= 1

        for cell in grid:
            if cell["gridx"] == posx and cell["gridy"] == posy:
                cell["status"] = "grass"

        if generations == 0:
            break


def check_grid(posx, posy): # may not be needed
    """Converts position to grid to check list of dictionary"""
    gridx = posx // 10
    gridy = posy // 10
    return gridx, gridy


generate_grid()
create_grass(100)
print(grid)





# Start the window
root.mainloop()