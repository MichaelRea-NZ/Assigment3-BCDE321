from PIL import Image


class DisplayBuilder:
    def display(self, arg):
        pass

class ConcreteDisplayBuilder:
    def display(self, arg):
        diagram = Image.open('classfile.dot.png')
        diagram.show()
