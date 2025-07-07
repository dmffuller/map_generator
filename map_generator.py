from tkinter import*
from random import*

root = Tk()
root.title("Map Generator")

canvas = Canvas(root, width=1000, height=1000, bg="white")
canvas.pack()

grid = {} # Populate with dictionary of posx, posy
clicks = 1
infection_queue = []

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

def get_mouse_pos(event):
    """gets mouse position as pixels and cell"""
    x = event.x
    gx = x // 10 + 1
    y = event.y
    gy = y // 10 + 1
    print(f"Mouse clicked at x:{x}, y:{y}")
    print(f"Cell ({gx}, {gy})")
    set_infection(gx, gy)

def set_infection(gx, gy):
    """Sets clicked point as infection"""
    global clicks
    if (gx, gy) in grid and grid[(gx, gy)]["status"] == "grass" and clicks > 0:
        grid[(gx, gy)]["status"] = "infection"
        canvas.create_rectangle(
            (gx - 1) * 10,
            (gy - 1) * 10,
            gx * 10,
            gy * 10,
            fill="red",
            outline="black"
        )
        clicks -= 1
        infection_queue.append((gx, gy))
        spread_infection()
    else:
        print("No clicks remain")           

def spread_infection():
    """Spreads the infection to nearby blocks"""
    if not infection_queue:
        return  # done!

    gx, gy = infection_queue.pop(0)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    for dx, dy in directions:
        nx, ny = gx + dx, gy + dy
        if (nx, ny) in grid and grid[(nx, ny)]["status"] == "grass":
            grid[(nx, ny)]["status"] = "infection"
            canvas.create_rectangle(
                (nx - 1) * 10, (ny - 1) * 10, nx * 10, ny * 10,
                fill="red", outline="black"
            )
            infection_queue.append((nx, ny))

    root.after(2, spread_infection)  # wait 0.1 sec

def create_grass(generations):
    """Creates Random Grass and fills adjacent empty tiles."""
    max_attempts = generations * 10
    attempts = 0

    while generations > 0 and attempts < max_attempts:
        gx = randint(1, 100)
        gy = randint(1, 100)
        attempts += 1
        status = check_status(gx, gy)

        if status == "empty":
            add_grass_and_adjacent(gx, gy)
            generations -= 1

def add_grass_and_adjacent(x, y):
    """Sets grass at (x, y) and fills empty adjacent tiles with grass."""
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # left, right, up, down

    def set_grass(gx, gy):
        if (gx, gy) in grid and grid[(gx, gy)]["status"] == "empty":
            grid[(gx, gy)]["status"] = "grass"
            canvas.create_rectangle(
                (gx - 1) * 10,
                (gy - 1) * 10,
                gx * 10,
                gy * 10,
                fill="green",
                outline="black"
            )

    set_grass(x, y)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        set_grass(nx, ny)

def fill_empty_with_water():
    """Fills every remaining empty cell with water"""
    for (x, y), data in grid.items():
        if data["status"] == "empty":
            grid[(x, y)]["status"] = "water"
            canvas.create_rectangle(
                (x - 1) * 10,
                (y - 1) * 10,
                x * 10,
                y * 10,
                fill="blue",
                outline="black"
            )

def check_status(gx, gy): # may not be needed
    """Converts position to grid to check list of dictionary"""
    return grid.get((gx, gy), {}).get("status")

generate_grid() # Create the grid
create_grass(2000) # Populate with grass
fill_empty_with_water()  # Fill remaining empty cells with water


root.bind("<Button-1>", get_mouse_pos)

# Start the window
root.mainloop()