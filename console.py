#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
from models import storage


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

    def do_create(self, arg):
        """creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        class_name = storage.class_name()
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg in class_name.keys():
            class_name[arg]().save()
            print(class_name[arg]().id)
        else:
            print("** class doesn't exist **")

    def do_show(self, *args):
        """prints the string representation of an instance based on the class name and id"""
        class_name = storage.class_name()
        arg = args[0].split(' ')
        storage_all = storage.all()
        also_arg = arg[0] + "." + arg[1]
        if args[0] == "" or args[0] is None:
            print("** class name missing **")
            return
        if arg[0] not in class_name.keys():
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        if also_arg in storage_all.keys():
            print(storage_all[also_arg])
            return
        print("** no instance found **")

    def do_destroy(self, *args):
        """deletes an instance based on the class name and id"""
        class_name = storage.class_name()
        arg = args[0].split(' ')
        storage_all = storage.all()
        also_arg = arg[0] + "." + arg[1]
        if args[0] == "" or args[0] is None:
            print("** class name missing **")
            return
        if arg[0] not in class_name.keys():
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        if also_arg in storage_all.keys():
            del storage_all[also_arg]
            storage.save()
            return
        print("** no instance found **")

    def all(self, *args):
        """prints all string representation of all instances based or not on the class name"""
        class_name = storage.class_name()
        storage_all = storage.all()
        string_list = []
        if args[0] == "":
            for k, v in storage_all.items():
                string_list.append(str(v))
            print(string_list)
            return
        if args[0] not in class_name.keys():
            print("** class doesn't exist **")
            return
        for k, v in storage_all.items():
            if args[0] == type(v).__name__:
                string_list.append(str(v))
        print(string_list)

    def update(self, *args):
        """updates an instance based on the class name and id by adding or updating attribute"""
        class_name = storage.class_name()
        arg = args[0].split(' ')
        storage_all = storage.all()
        also_arg = arg[0] + "." + arg[1]
        if args[0] == "" or args[0] is None:
            print("** class name missing **")
            return
        if arg[0] not in class_name.keys():
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        if also_arg not in storage_all.keys():
            print("** no instance found **")
            return
        if len(arg) == 2:
            print("** attribute name missing **")
            return
        if len(arg) == 3:
            print("** value missing **")
            return
        try:
            x = float(arg[3])
            if x.is_integer():
                x = int(x)
        except (TypeError, ValueError):
            if "\"" in arg[3]:
                arg[3] = arg[3].replace("\"", "")
            setattr(storage_all[also_arg], arg[2], str(arg[3]))
            storage.save()
            return
        setattr(storage_all[also_arg], arg[2], x)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
