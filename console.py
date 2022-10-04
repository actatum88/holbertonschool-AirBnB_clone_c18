#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand Rules:
        -you can assume arguments are always in the right order
        -each arguments are separated by a space
        -a string argument with a space must be between double quote
        -the error management starts from the first argument to the last one
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """exits the command line at the end of file"""
        print("")
        return True

    def emptyline(self):
        """an empty line and ENTER shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
