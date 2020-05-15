#!/usr/bin/python3
import os
import sys
import argparse

ignore = [
    'iso'
]

custom_name = {
    'zip': 'Compactados',
    'rar': 'Compactados',
    'xz': 'Compactados',
    'pdf': 'Documentos',
    'odt': 'Documentos',
    'exe': 'Executaveis'
}

def move_files(file):
    # File path
    path = os.path.realpath(sys.argv[1])
    
    file_path = os.path.join(path, file)
    
    # If its a dir
    if os.path.isdir(file_path):
        return
    
    file_size = os.stat(file_path).st_size
    # Get kb
    file_size /= 1000 
    # Get mb
    file_size /= 1000


    file_type = file.split('.')[-1]

    # Get custom name, otherwise dir_name will have file_type
    dir_name = custom_name.get(file_type, file_type)

    if file_size > 1000:
        return

    if file_type in ignore:
        return


    # Path were the file will be moved
    dir_path = os.path.join(path, dir_name)

    if args.verbose:
        print('------------------------------')
        print(f'File name: {file}')
        print(f'File path: {file_path}')
        print(f'File size: {file_size}')
        print(f'Type of the file: {file_type}')
        print(f'Where file will be moved: {dir_path}')

    # If the dir doesn't exist it will create one with file_type as a name
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

    os.rename(file_path, os.path.join(dir_path, file))

if __name__ == '__main__':
    parser = argparse.ArgumentParser('File Organizer', 'Organize your files')
    parser.add_argument('path', help='The path that will be organized', type=str)
    parser.add_argument('-v','--verbose', help='Activate the cli log', action='store_true')

    args = parser.parse_args()
    print(args)

    files_list: list = os.listdir(args.path)
    if files_list.__len__() == 0:
        print(f'The path {args.path} is empty!')
    else:
        if args.verbose:
            print(files_list)

        for file in files_list:
            move_files(file)
