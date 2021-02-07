#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
import os

# decoration
print(stylize("\n---- | Get file size | ----\n", fg("red")))

# class
class FileSize:
    def __init__(self, path, file):
        self.path = path
        self.file = file

    # output magic method
    def __repr__(self):
        size = self.get_file_size(self.path, self.file)
        if size[1] == 2:
            size = stylize(self.get_file_size(self.path, self.file)[0], fg("red"))
            return f"\n{self.file} is {size} GB in size.\n"
        elif size[1] == 1:
            size = stylize(self.get_file_size(self.path, self.file)[0], fg("red"))
            return f"\n{self.file} is {size} MB in size.\n"
        else:
            size = stylize(self.get_file_size(self.path, self.file)[0], fg("red"))
            return f"\n{self.file} is {size} KB in size.\n"

    # methods
    def get_file_size(self, path, file):
        file_size = os.path.getsize(f"{path}/{file}")
        if file_size > 1000000000:
            file_size_gb = round(file_size / (1 * 10**9), 4)
            return file_size_gb, 2
        elif file_size > 1000000:
            file_size_mb = round(file_size / (1 * 10**6), 4)
            return file_size_mb, 1
        else:
            file_size_kb = round(file_size / (1 * 10**3), 4)
            return file_size_kb, 0

# main execution
if __name__ == "__main__":
    # user interaction
    filename = input("Filename: ")
    path = input("Path of file: ")

    print(FileSize(path, filename))
