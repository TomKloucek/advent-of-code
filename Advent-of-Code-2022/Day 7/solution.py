import os
file1 = open('input.txt', 'r')

directory = []

accum = 0

class Folder:
    def __init__(self,name, parent):
        self.folders = []
        self.name = name
        self.parent = parent

    def __repr__(self) -> str:
            return f'Folder - {self.name} - {self.folders}'

    def get_size(self):
        size = 0
        for folder in self.folders:
            size += folder.get_size()
        return size

class File:
    def __init__(self,name,size):
        self.name = name
        self.size = size

    def __repr__(self) -> str:
        return f'File - {self.name} - {self.size}'

    def get_size(self):
        return int(self.size)

current_folder = Folder('/', None)
root = current_folder

while True:
    changed = False
    line = file1.readline().strip().split()
    if not line:
        break 
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '..':
                current_folder = current_folder.parent
            else:
                for folder in current_folder.folders:
                    if folder.name == line[2]:
                        current_folder = folder
                        changed = True
                if current_folder.name != line[2]: 
                    if not changed:
                        current_folder.folders.append(Folder(line[2], current_folder))
        if line[1] == 'ls':
            loaded = file1.readline().strip().split()
            if loaded == '$ cd ..':
                current_folder = current_folder.parent
            if loaded[0] == '$':
                for folder in current_folder.folders:
                    if folder.name == loaded[2]:
                        current_folder = folder 
                break
            if loaded[0] == 'dir':
                current_folder.folders.append(Folder(loaded[1], current_folder))
            else:
                current_folder.folders.append(File(loaded[1],int(loaded[0])))
            while loaded[0] != '$':
                loaded = file1.readline().strip().split()
                if not loaded:
                    break
                if loaded == '$ cd ..':
                    current_folder = current_folder.parent
                if loaded[0] == '$':
                    for folder in current_folder.folders:
                        if folder.name == loaded[2]:
                            current_folder = folder 
                    break
                if loaded[0] == 'dir':
                    current_folder.folders.append(Folder(loaded[1], current_folder))
                else:
                    current_folder.folders.append(File(loaded[1],int(loaded[0])))
            if loaded == []:
                break
            if loaded[0] == '$':
                    if loaded[2] == '..':
                        current_folder = current_folder.parent
                    else:
                        for folder in current_folder.folders:
                            if folder.name == loaded[2]:
                                current_folder = folder


def count_size(folder):
    for file in folder.folders:
        if isinstance(file, Folder):
            count_size(file)
    directory.append([folder.name, folder.get_size()])

count_size(root)

to_delete = root.get_size()
free_space = 70000000 - root.get_size()

for folder in directory:
    if folder[1] <= 100000:
        accum += folder[1]
    if (folder[1]+free_space) >= 30000000:
        if folder[1] < to_delete:
            to_delete = folder[1] 

print(accum, to_delete)