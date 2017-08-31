# argv represents the arguments to our program on the command line
from sys import argv, exit

# os has functions for working with files, paths, and directories
import os

import string

zoo_dir = ''

if len(argv) > 1:
    dont_care, first_arg = argv
    zoo_dir = os.path.abspath(first_arg)
else:
    zoo_dir = os.path.abspath(".")

os.chdir(zoo_dir)

if not os.path.exists("zoo"):
    print "Zoo directory not found in %s" % os.getcwd()
    exit(1)

if not os.path.isdir("zoo"):
    print "Zoo is not a directory"
    exit(1)

print "Zoo directory found"

animal_kind_dirs = os.listdir("zoo")

if not animal_kind_dirs:
    print "Nothing in zoo, maybe you should put some animals in there."
    exit(1)
    
animal_count = 0

for dir_name in os.listdir("zoo"):

    animal_kind_directory = os.path.join("zoo", dir_name)

    if not os.path.isdir(animal_kind_directory):
        print "Found %s in zoo, maybe it should be in a pen (folder) with other animals of its kind" % animal_kind_directory
        exit(1)

    print "Checking animals in %s" % dir_name

    for file_name in os.listdir(animal_kind_directory):

        animal_name_file = os.path.join(animal_kind_directory,file_name)

        if not os.path.isfile(animal_name_file):
            print "Found %s in %s but it was not a file" % (animal_name_file, dir_name)
            exit(1)

        print "Checking animal %s" % file_name
        animal_file = open(animal_name_file)
        file_contents = string.join(animal_file.readlines()).rstrip()

        if file_contents != dir_name:
            print "%s should be in the %s folder" % (file_name, file_contents)
            exit(1)

        animal_count = animal_count + 1
            
if animal_count != 13:
    print "Looks like you're missing some animals. There should be 13 but I found %d" % animal_count
    
print "Everything A-Ok!"

