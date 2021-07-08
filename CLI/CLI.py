class CLI:

    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return f"> {self.__name} >>> "

    def run(self):
        pass
