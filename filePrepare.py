
class PrepareBuilder:

    def select_file(self, arg):
        pass


    def open_file(self, file_name):
        pass


class ConcreatePrepareBuilder:
    def select_file(self, arg):

        print('Enter the file path and file name of the file that ' +
              'requires analyzing')
        # call file opener
        if (arg.endswith(".js")):
            file_name = arg
            print('You selected ', file_name, "\n")
            self.open_file(file_name)
        else:
            print("The file is not a JavaScript file")

    def open_file(self, file_name):
        if file_name != '':
            try:
                file = open(file_name)
            except FileNotFoundError:
                print("The file does not exist at that location\n"
                      "Please check your file and try again")
            else:
                self.js_file_content = file.read()
                print("\n Hi", file_name, "\n")
                print(self.js_file_content)
