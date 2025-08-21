from pathlib import Path

filepath = Path("D:\\tatata.txt")
print(filepath)
print(__file__)
filepath = Path(__file__)
print(filepath)
file_dir = filepath.parent
print(file_dir)
file_dir_2 = filepath.parent.parent
print(file_dir_2)
all_objects = [i for i in file_dir_2.iterdir()]
print(all_objects)

directories = [d for d in file_dir_2.iterdir() if d.is_dir()]

# Виведення списку директорій
print("Список директорій:")
for directory in directories:
    print(directory)

files = [f for f in file_dir_2.iterdir() if f.is_file()]
print("Список всіх файлів:")
for file in files:
    print(file)

files = [f for f in file_dir.iterdir() if f.suffix == ".txt"]
# files = [f for f in file_dir.iterdir()]
print(files)
print(f"Is file '{files[0].name}'  exist? {files[0].exists()}")

path = "D:\\bababa.txt"
file_ne_path = Path(path)
print(f"Is file '{path}'  exist? {file_ne_path.exists()}")

print("it is dir?", files[0].is_dir())
print("it is file?", files[0].is_file())
print("current dir", file_dir)
readme_file = file_dir / "test" / "readme.txt"
print("it readme_file exists?", readme_file.exists())
print("it readme_file is dir?", readme_file.is_dir())
print("it readme_file is file?", readme_file.is_file())
print("it readme_file.parent is dir?", readme_file.parent.is_dir())
current_directory = Path.cwd() # звідки запущено скрипт
print("Поточна робоча директорія:", current_directory)
home_directory = Path.home()
print("Домашня директорія користувача:", home_directory)
new_dir = file_dir / "text" / "my_fanfic"
new_dir.mkdir(parents=True, exist_ok=True)

example_file = files[0]
print(example_file)
with example_file.open(encoding="utf8") as f:
    content = f.read()
    print(content)

with example_file.open("w", encoding="utf8") as f:
    f.write("Hello, World!")


with example_file.open("+a", encoding="utf-8") as f:
    f.write("""
Hi sttudents!
Але є один ньюанс
""")