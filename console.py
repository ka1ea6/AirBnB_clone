#!/usr/bin/env python3
'''Modlue for implementing a python command line interpreter'''
import cmd
import re

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = ['Amenity', 'BaseModel', 'City',
                 'Place', 'Review', 'State', 'User']

    def emptyline(self):
        pass

    def do_quit(self, arg):
        '''Quit command to exit the program \n'''
        return True

    def do_EOF(self, arg):
        '''Quit command upon passing of EOF\n'''
        return True

    def do_create(self, arg):
        '''Creates a new instance of BaseModel and saves it to the
JSON file storage and prints the id of the created Model'''
        arg_arr = arg.split(' ')
        if not arg_arr[0]:
            print('** class name missing **')
            return
        elif arg_arr[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        else:
            new_model = eval(arg_arr[0])()
            new_model.save()
            print(new_model.id)

    def do_all(self, arg):
        '''Prints the string represntation of all instances'''
        arg_arr = arg.split(' ')
        if not arg_arr[0]:
            print('** class name missing **')
            items = storage.all()
            [print(items[f'{item}']) for item in items]
            return
        elif arg_arr[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        items = storage.all()
        # print(items)
        [print(items[f'{item}']) if arg_arr[0]
         in item else '' for item in items]

    def do_show(self, arg):
        '''Prints the string representation of an instance based
on the class name and id'''
        try:
            arg_arr = arg.split(' ')
            if not arg_arr[0]:
                print('** class name missing **')
                return
            elif arg_arr[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            elif len(arg_arr) < 2:
                print("** instance id missing **")
                return

            items = storage.all()
            currItem = items[f'{arg_arr[0]}.{arg_arr[1]}']
            print(currItem)
        except KeyError:
            print("** no instance found **")
            return

    def do_update(self, arg):
        '''Prints the string representation of an instance based
on the class name and id'''
        try:
            arg_arr = arg.split(' ')
            if not arg_arr[0]:
                print('** class name missing **')
                return
            elif arg_arr[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            elif len(arg_arr) < 2:
                print("** instance id missing **")
                return
            elif len(arg_arr) < 3:
                print("** attribute name missing **")
                return
            elif len(arg_arr) < 4:
                print("** value missing **")
                return

            update_status = storage.update(
                f'{arg_arr[0]}.{arg_arr[1]}', arg_arr[2], arg_arr[3])
            if not update_status:
                print('** no instance found **')
        except KeyError:
            print("** no instance found **")
            return

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and'''
        arg_arr = arg.split(' ')
        if not arg_arr[0]:
            print('** class name missing **')
            return
        elif arg_arr[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(arg_arr) < 2:
            print("** instance id missing **")
            return

        del_status = storage.remove(f'{arg_arr[0]}.{arg_arr[1]}')
        if not del_status:
            print('** no instance found **')

    def do_count(self, arg):
        '''Retrieves the number of instances of a class'''
        arg_arr = arg.split(' ')
        if not arg_arr[0]:
            print('** class name missing **')
            return
        elif arg_arr[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        items = storage.all()
        # print(items)
        count = 0
        for item in items:
            if arg_arr[0] in item:
                count += 1
        print(count)

    def precmd(self, line: str) -> str:
        func = False
        if '(' in line:
            func = True

        line = re.sub(r'\(', ' ', line)
        line = re.sub(r'\)', '', line)
        if len(line.split(" ")) > 1 and func:
            line_arr = line.split(" ")
            inner_arr = line_arr[0].split(".")
            line_arr[0] = ' '.join(inner_arr[::-1])
            line_arr = [self.__clean_comma(str) for str in line_arr]
            line = ' '.join(line_arr)
        else:
            line_arr = line.split('.')
            line = ' '.join(line_arr[::-1])
        return super().precmd(line)

    def __clean_comma(self, str):
        return re.sub(r',', '', str)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
