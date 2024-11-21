class Color:
    def __init__(
        self,
        r: int,
        g: int,
        b: int,
    ):
        self.red=r
        self.green=g
        self.blue=b

    def get_html_rgb_value(self):
        return f'rgb({self.red},{self.green},{self.blue})'

data=[[199,183,163],[140,97,49],[70,135,170]]
for c in data:
    r,g,b=c
    color=Color(r,g,b)
    print(color.get_html_rgb_value())

'''
rgb(199,183,163)
rgb(140,97,49)
rgb(70,135,170)
'''