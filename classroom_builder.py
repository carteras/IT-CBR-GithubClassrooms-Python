"""
Classroom builder creates a basic framework for github classrooms. 
"""
from os import read
from pathlib import Path
import shutil
import argparse

def build_classrooms(class_file):
    p = Path.cwd()
    new_year = p / "github" /class_file
    new_year.mkdir(parents=True, exist_ok=False)

    classroom_builder_name = class_file

    classrooms = []
    template_path = p  / "0.0.0.Template"
    with open(classroom_builder_name, 'r') as classrooms_to_make:
        for line in classrooms_to_make:
            classrooms.append(line.strip())

    for classroom in classrooms:
        classroom_path = new_year / classroom
        classroom_path.mkdir(parents=True, exist_ok=False)
        print(classroom_path)
        for f in template_path.glob("**/*"):
            if not f.is_file(): 
                continue
            print(f.name, classroom_path/f.name)
            src = template_path / f.name
            dest = classroom_path / f.name
            dest.write_text(src.read_text())

parser = argparse.ArgumentParser("Build Github Classrooms")
parser.add_argument("-b", '--build', help="-b filename to force a build of classrooms given in the filename (danger, this will reset stuff)")
parser.add_argument('-r', '--reset', help='-r filename to force delete all folders other than the template given in the filename')
args = parser.parse_args()
print(args)

if args.build:
    build_classrooms(args.build)

if args.reset:
    p = Path.cwd()
    del_path = p / "github" /args.reset
    shutil.rmtree(template_path)


