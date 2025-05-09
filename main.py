from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.__running = False

        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack(fill = BOTH, expand = True)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )
        

def main():
    win = Window(800, 600)

    # Create some points
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(100, 200)

    # Create lines using those points
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)

    # Draw the lines with different colors
    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")

    win.wait_for_close()

main()
