class rectangle :
    def __init__(self,width,height):
        self._width = width
        self._height = height
    @property
    def width(self):
        return f"{self._width}"
    @property
    def height (self):
        return f"{self._height}"

rect = rectangle(3,4)
print (rect.width)
print (rect.height)