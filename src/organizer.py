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

def parse_size(size):
    if size.lower().endswith('g'):
        parsed = int(size.lower().split('g')[0]) * 1000
    elif size.lower().endswith('m'):
        parsed = int(size.lower().split('m')[0])
    else:
        parsed = int(size)
    return parsed

def process_size(minSize, maxSize):
    # The args parser receives a str, or use the default value that is a number
    if isinstance(minSize, str):
        min_size = parse_size(minSize)
    else:
        min_size = minSize

    # The args parser receives a str, or use the default value that is a number
    if isinstance(maxSize, str):
        max_size = parse_size(maxSize)
    else:
        max_size = maxSize

    # My eyes '-'
    return min_size, max_size

def move_files(file, min_size, max_size):
    ''' 
        This function will move the file if its size is above the minimun and below the maximun size
    '''

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

    if max_size > file_size < min_size:
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
    parser.add_argument('-m', '--minSize', help='The minimun size of the file that will be organized', action='store', default=0)
    parser.add_argument('-M', '--maxSize', help='The max size of the file that will be organized', action='store', default=1000)

    args = parser.parse_args()
    print(args)

    # Process the sizes of the files

    min_size, max_size = process_size(args.minSize, args.maxSize)

    # Get the files list
    files_list: list = os.listdir(args.path)
    if files_list.__len__() == 0:
        print(f'The path {args.path} is empty!')
    else:
        if args.verbose:
            print(files_list)

        for file in files_list:
            move_files(file, min_size, max_size)
