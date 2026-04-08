class Publication:
    def _init_(self, name):
        self.name = name

class Book(Publication):
    def _init_(self, name, author, pages):
        super()._init_(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print(self.name, "-", self.author + ",", self.pages, "pages")

class Magazine(Publication):
    def _init_(self, name, chief_editor):
        super()._init_(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(self.name, "- Chief editor:", self.chief_editor)


# main program
donald = Magazine("Donald Duck", "Aki Hyyppä")
compartment = Book("Compartment No. 6", "Rosa Liksom", 192)

donald.print_information()
compartment.print_information()
