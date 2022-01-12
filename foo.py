from pathlib import Path
p = Path.cwd()
with open("classrooms2022", 'w') as file_writer:
    [file_writer.write(f"{x.name}\n") for x in p.glob("**/*") if x.is_dir()]