from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        line = Line(Point(x1, y1), Point(x1, y2))
        left_color = "black" if self.has_left_wall else "white"
        self._win.draw_line(line, fill_color=left_color)

        line = Line(Point(x1, y1), Point(x2, y1))
        top_color = "black" if self.has_top_wall else "white"
        self._win.draw_line(line, fill_color=top_color)

        line = Line(Point(x2, y1), Point(x2, y2))
        right_color = "black" if self.has_right_wall else "white"
        self._win.draw_line(line, fill_color=right_color)

        line = Line(Point(x1, y2), Point(x2, y2))
        bottom_color = "black" if self.has_bottom_wall else "white"
        self._win.draw_line(line, fill_color=bottom_color)
    
    def draw_move(self, to_cell, undo=False):
        center_x1 = (self._x1 + self._x2) / 2
        center_y1 = (self._y1 + self._y2) / 2

        center_x2 = (to_cell._x1 + to_cell._x2) / 2
        center_y2 = (to_cell._y1 + to_cell._y2) / 2
        
        fill_color = "red" if not undo else "gray"
        line = Line(Point(center_x1, center_y1), Point(center_x2, center_y2))
        self._win.draw_line(line, fill_color)