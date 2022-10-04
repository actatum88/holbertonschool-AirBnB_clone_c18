#!/usr/bin/python3
""" Console Module """
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Creates class for console commands. """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exits the command line at the end of file."""
        return True

    def emptyline(self):
        """Empty line + Enter doesn't execute anything."""
        pass

    def do_create(self, args):
        """Creates a new object and prints the object ID."""
        arg = args.split()
        if len(arg) < 1:
            print("** Class name missing **")
            return False
        if len(arg) > 1:
            print("** Too many Arguments **")
            return False
        if arg[0] !=  "BaseModel":
            print("** Class name missing **")
            return False
        new_object = eval(str(args) + '()')
        new_object.save()
        print(new_object.id)
