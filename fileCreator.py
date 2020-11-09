class CreateFileBuilder:

    def create_file(self):
        pass


class ConcreteCreateFileBuilder:

    def create_file(self):
        self.dot_file1 = open("classfile.dot", "w")
        self.dot_file1.write(f'digraph G {{fontname = "Bitstream Vera Sans"\
    fontsize = 8 node [fontname = "Bitstream Vera Sans"\
    fontsize = 8 shape = "record"]\
    edge [fontname = "Bitstream Vera Sans"fontsize = 8] {self.class_name}\
    [ label = " {{{self.class_name}|{self.property_name}|{self.function_name}\
    }}"]}}')
        self.dot_file1.close()
        self.dot_file1 = open("classfile.dot", "r")
        print(self.dot_file1.read())
        self.dot_file1.close()
