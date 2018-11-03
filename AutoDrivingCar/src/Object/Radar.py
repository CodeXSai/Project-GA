class Radar:
    _radius = None
    _aicanvas = None
    _posX = None
    _posY = None

    def __init__(self, radius, aicanvas, posX, posY):
        self._radius = radius
        self._aicanvas = aicanvas
        self._posX = posX
        self._posY = posY

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, set_radius):
        self._radius = set_radius

    @radius.deleter
    def radius(self):
        del self._radius

    @property
    def posX(self):
        return self._posX

    @posX.setter
    def posX(self, set_pos):
        self._posX = set_pos

    @posX.deleter
    def posX(self):
        del self._posX

    @property
    def posY(self):
        return self._posY

    @posY.setter
    def posY(self, set_pos):
        self._posY = set_pos

    @posY.deleter
    def posY(self):
        del self._posY

    def create_circle(self, **kwargs):
        return self._aicanvas.create_oval(self._posX - self._radius, self._posY - self._radius,
                                          self._posX + self._radius, self._posY + self._radius, **kwargs)

    def create_arc(self, **kwargs):
        if "start" in kwargs and "end" in kwargs:
            kwargs["extent"] = kwargs["end"] - kwargs["start"]
            del kwargs["end"]
        return self._aicanvas.create_arc(self._posX - self._radius, self._posY - self._radius,
                                         self._posX + self._radius, self._posY + self._radius, **kwargs)

# How to create circle
    #Radar.create_circle(100, 120, 50, fill="blue", outline="#DDD", width=4)
    #Radar.create_circle_arc(100, 120, 48, fill="green", outline="", start=45, end=140)
    #Radar.create_circle_arc(100, 120, 48, fill="green", outline="", start=275, end=305)
    #Radar.create_circle_arc(100, 120, 45, style="arc", outline="white", width=6, start=270-25, end=270+25)
    #Radar.create_circle(150, 40, 20, fill="#BBB", outline="")
