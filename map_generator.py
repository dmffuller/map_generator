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
grid = {} # Populate with dictionary of posx, posy




def generate_grid():
    """Generates the grid"""
    for y in range(1, 101):
        for x in range(1, 101):
            grid[(x, y)] = {"status": "empty"}
            canvas.create_rectangle(
                (x - 1) * 10,
                (y - 1) * 10,
                x * 10,
                y * 10,
                fill="white",
                outline="black"
            )


def create_grass(generations):
    """Creates Random Grass"""
    global x1, x2, y1, y2

    while generations > 0: # Loop through set generations
        gx = randint(1, 100)
        gy = randint(1,100)
        status = check_status(gx, gy)

        if status == "empty": # Only set status on empty cells
            # Change the status
            if (gx, gy) in grid:
                grid[(gx, gy)]["status"] = "grass"

                # Draw the grass cell:
                canvas.create_rectangle(
                    (gx - 1) * 10,
                    (gy - 1) * 10,
                    gx * 10,
                    gy * 10,
                    fill="green",
                    outline="black"
                )

                generations -= 1



def check_status(gx, gy): # may not be needed
    """Converts position to grid to check list of dictionary"""
    return grid.get((gx, gy), {}).get("status")

generate_grid() # Create the grid
create_grass(5000) # Popu;ate with grass






# Start the window
root.mainloop()