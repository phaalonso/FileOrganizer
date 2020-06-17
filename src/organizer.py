#!/usr/bin/python3
import os
import sys
import argparse
import json

def parse_size(size) -> int:
    if size.lower().endswith('g'):
        parsed = int(size.lower().split('g')[0]) * 1000
    elif size.lower().endswith('m'):
        parsed = int(size.lower().split('m')[0])
    else:
        parsed = int(size)
    return parsed

def move_files(path, file, min_size, max_size):
    ''' 
        This function will move the file if its size is above the minimun and below the maximun size
    '''

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

    # If the file_size don't respect the constraints or it's in the ignore list then return
    if max_size > file_size < min_size or file_type in ignore:
        return

    # Get custom name, otherwise dir_name will have file_type
    dir_name = custom_dir.get(file_type, file_type)

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
    parser.add_argument('path', help='The path to the dir that will be organized', type=str)
    parser.add_argument('-v','--verbose', help='Activate the cli log', action='store_true')
    parser.add_argument('-m', '--minSize', help='The minimun size of the file that will be organized', action='store', default=0)
    parser.add_argument('-M', '--maxSize', help='The max size of the file that will be organized', action='store', default=1000)
    parser.add_argument('-i', '--ignore', help='Ignore some file type', action='store', type=str)
    parser.add_argument('-I', '--ignoreDefaults', help='Ignore the defaults determined by a file in the project', action='store_true')
    parser.add_argument('-c', '--custom', help='Custom name to store a file type', action='store', nargs=2)

    args = parser.parse_args()
    
    if args.verbose:
        print(args)

    ignore = []
    custom_dir = {}

    # print(os.path.dirname(__file__))

    if not args.ignoreDefaults:
        with open(os.path.join(os.path.dirname(__file__), 'defaults.json'), 'r') as file:
            data = json.load(file)
            ignore = data["ignore"]
            custom_dir = data["customDirs"]

    if isinstance(args.custom, list):
        file_type = args.custom[0]
        custom_name = args.custom[1]
        # print(f'File type: {file_type}, custom name: {custom_name}')
        custom_dir[file_type] = custom_name 

    if args.verbose:
        print(f'Custom dir: ${custom_dir}')
    
    # Process the sizes of the files
    if args.ignore:
        ignore.append(args.ignore)
    # print(ignore)

    min_size = parse_size(args.minSize) if isinstance(args.minSize, str) else args.minSize
    max_size = parse_size(args.maxSize) if isinstance(args.maxSize, str) else args.maxSize

    if args.verbose:
        print(f'Minimun size: ${min_size}\nMaximun size: ${max_size}')

    try: 
        # Get the files list
        pathToDir = os.path.realpath(args.path)
        files_list: list = os.listdir(pathToDir)
    except FileNotFoundError:
        print('Diretório não encontrado!')
        exit()

    if files_list.__len__() == 0:
        print(f'The path {args.path} is empty!')
    else:
        if args.verbose:
            print(files_list)

        for file in files_list:
            move_files(pathToDir, file, min_size, max_size)
