#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import sys
import cmd
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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
        exit()

    def do_EOF(self, arg):
        """exits the command line at the end of file"""
        exit()

    def emptyline(self):
        """an empty line and ENTER shouldn’t execute anything"""
        pass

    def can_exit(self):
        """support for do_quit and do_EOF"""
        return True

    def do_create(self, model_type="None"):
        """creates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id"""
        if model_type == "" or None:
            print("** class name missing **")
        elif model_type not in [
            "BaseModel",
            "City",
            "State",
            "User",
            "Review",
            "Place",
            "Amenity"
        ]:
            print("** class doesn't exist **")
        else:
            if model_type == "BaseModel":
                new_model = BaseModel()
            elif model_type == "State":
                new_model = State()
            elif model_type == "City":
                new_model = City()
            elif model_type == "User":
                new_model = User()
            elif model_type == "Place":
                new_model = Place()
            elif model_type == "Amenity":
                new_model = Amenity()
            elif model_type == "Review":
                new_model = Review()
            print(new_model.id)
            storage.new(new_model)
            storage.save()

    def do_show(self, model_key=None):
        """prints the string representation of an instance based on
            the class name and id"""
        class_name = None
        model_id = None
        if model_key != "":
            try:
                class_name = model_key.split(" ")[0]
                model_id = model_key.split(" ")[1]
            except IndexError:
                pass
        if class_name is None:
            print("** class name missing **")
        elif class_name not in ["BaseModel", "City", "State",
                                "User", "Review", "Place", "Amenity"]:
            print("** class doesn't exist **")
        elif model_id is None:
            print("** instance id missing **")
        else:
            model_key = class_name + "." + model_id
            key_exists = False
            for key in storage.all().keys():
                if key == model_key:
                    print(storage.all().get(key))
                    key_exists = True
                    break
            if key_exists is not True:
                print("** no instance found **")

    def do_destroy(self, model_key=None):
        """deletes an instance based on the class name and id"""
        class_name = None
        model_id = None
        if model_key != "":
            try:
                class_name = model_key.split(" ")[0]
                model_id = model_key.split(" ")[1]
            except IndexError:
                pass
        if class_name is None:
            print("** class name missing **")
        elif class_name not in ["BaseModel", "City", "State",
                                "User", "Review", "Place", "Amenity"]:
            print("** class doesn't exist **")
        elif model_id is None:
            print("** instance id missing **")
        else:
            model_key = class_name + "." + model_id
            delkey = None
            for key in storage.all().keys():
                if key == model_key:
                    delkey = key
                    break
            if delkey is not None:
                storage.all().pop(key)
                storage.save()
                try:
                    storage.reload()
                except FileNotFoundError:
                    pass
            else:
                print("** no instance found **")

    def do_all(self, model_type):
        """prints all string representation of all instances based or not on the class name"""
        obj_list = []
        if model_type == "":
            for obj in storage.all().values():
                obj_list.append(obj.__str__())
            print(obj_list)
        elif model_type not in ["BaseModel", "City", "State",
                                "User", "Review", "Place", "Amenity"]:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if obj.__class__.__name__ == model_type:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, model_info):
        """updates an instance based on the class name and id by adding or updating attribute"""
        model_type = None
        model_id = None
        model_attr = None
        model_val = None
        if model_info != "":
            try:
                model_type = model_info.split(" ")[0]
                model_id = model_info.split(" ")[1]
                model_attr = model_info.split(" ")[2]
                model_val = model_info.split(" ")[3]
                if model_val.startswith('"'):
                    model_val = model_info.split(" ")[3].strip('"')
                    model_val += " " + model_info.split(" ")[4].strip('"')
            except IndexError:
                pass
        if model_type is None:
            print("** class name missing **")
        elif model_id is None:
            print("** instance id missing **")
        elif model_attr is None:
            print("** attribute name missing **")
        elif model_val is None:
            print("** value missing **")
        else:
            model_key = model_type + "." + model_id
            key_exists = False
            for key in storage.all().keys():
                if key == model_key:
                    obj = storage.all().get(key)
                    setattr(obj, model_attr, model_val)
                    key_exists = True
                    break
            if key_exists is not True:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
