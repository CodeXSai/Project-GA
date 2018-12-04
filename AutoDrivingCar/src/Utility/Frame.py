from tkinter import *
from .AICanvas import AICanvas
from Object.Enum import CONST


class Frame:

    def __init__(self, set_root=None, set_canvas=None):
        if set_root is None:
            self._root = Tk()
        else:
            self._root = set_root

        if set_canvas is None:
            self._canvas = AICanvas(self._root)
        else:
            self._canvas = set_root

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, set_root):
        self._root = set_root

    def init_frame(self, frame_size, title):

        if frame_size == CONST.FRAME_SIZE:
            self._root.attributes(CONST.FULL_SCREEN, True)
            self._root.title(title)
            self._canvas.init_canvas(CONST.INITIALIZE_ZERO, CONST.INITIALIZE_ZERO, CONST.INITIALIZE_ZERO,
                                     CONST.INITIALIZE_ZERO)
        else:
            self._root.attributes(frame_size)
            self._root.title(title)
            self._canvas.init_canvas(CONST.INITIALIZE_ZERO, CONST.INITIALIZE_ZERO, CONST.INITIALIZE_ZERO,
                                     CONST.INITIALIZE_ZERO)

    @root.deleter
    def root(self):
        self._root.quit()
        del self._root

    @property
    def canvas(self):
        return self._canvas.canvas

    def frame_loop(self):
        self._root.mainloop()
