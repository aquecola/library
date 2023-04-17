import os

# получаем текущую рабочую директорию
cwd = os.getcwd()
print(cwd)

# создаем новую директорию
new_dir_path = os.path.join(cwd, 'new_dir')
os.mkdir(new_dir_path)

# создаем новый файл
new_file_path = os.path.join(new_dir_path, 'new_file.txt')
with open(new_file_path, 'w') as f:
    f.write('Hello, world!')

# удаляем файл и директорию
os.remove(new_file_path)
os.rmdir(new_dir_path)

