class Icommand:
    def action(self):
        pass

    def split_command(self, commands):
        new_command = []
        for word in commands:
            if word != "":
                new_command.append(word)
        return new_command
