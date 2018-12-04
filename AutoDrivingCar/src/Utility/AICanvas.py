from tkinter import *


class AICanvas:

    def __init__(self, root=None, canvas=None):
        if root is not None:
            self._root = root

        if canvas is not None:
            self._canvas = canvas

    def init_canvas(self, x, y, a, b):
        self._canvas = Canvas(self._root, width=self._root.winfo_width() - x, height=self._root.winfo_height() - y,
                              borderwidth=a, highlightthickness=b, bg="black")
        self._canvas.pack(fill=BOTH, expand=YES)

    @property
    def canvas(self):
        return self._canvas

    @canvas.setter
    def canvas(self, set_canvas):
        self._canvas = set_canvas

    @canvas.deleter
    def canvas(self):
        del self._canvas

    def canvas_loop(self):
        self._canvas.mainloop()
