# argv represents the arguments to our program on the command line
from sys import argv

# os has functions for working with files, paths, and directories
import os

# has functions so we can get random animal kinds
import random

animals = [
    "Dog",
    "Cat",
    "Snake"
]

names = [
    "Sassy",
    "Peaches",
    "Mittens",
    "Santas Little Helper",
    "Snowball",
    "Buttercup",
    "Rex",
    "Fido",
    "Bullseye",
    "Harvey",
    "Excelsior",
    "Maximus",
    "Roger",
]

def write_animal_file(name,kind,in_dir):
    file_path = os.path.join(in_dir, name)
    animal_file = open(file_path, "w")
    animal_file.write(kind)
    animal_file.close()

def pick_where_files_will_be_written():
    if len(argv) > 1:
        dont_care, first_arg = argv
        return os.path.abspath(first_arg)
    else:
        return os.path.abspath(".")

out_dir = pick_where_files_will_be_written()

if out_dir and not os.path.exists(out_dir):
    print "Output goes to %s" % out_dir
    os.makedirs(out_dir)

for n in names:
    kind = random.choice(animals)
    print "Animal %s is a %s" % (n,kind)
    write_animal_file(n, kind, out_dir)

print "Done!"
