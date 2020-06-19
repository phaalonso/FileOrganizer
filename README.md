# File Organizer

This sricpt can be utilised to organize files by the file extensio.

## How to use

You can simply call `python3 src/organizer.py <path_to_dir>` passing the path to the dir that you want to organize! :D (this works on all operating systems)

In linux:
 - you can give the file permission to execute with `chmod +x src/organizer.py` and run the program with `.src/organizer.py <path_to_dir>`.
 - or add a symbolic link using `sudo ln -s FileOrganizer/src/organizer.py /usr/local/bin/organizer` and call the program with `organizer <path_to_dir>`

## Configs
The default config file is in `src/defaults.json`

If you want to make some modifications will have to follow this format: 
```json
{
    "extension": {
    	"ignore": [
            "iso"
        ],
        "customDirs": {
            "zip": "Compactados",
            "extension": "Dir name"
    	}
    },
    "name": {
        "ignore": [],
        "customDirs": {
            "BD1C3": "Banco de Dados 1",
            "name that the file have in the start or in the end": "dirName"
        }
    }
}


```

## TO DO
- [X] Sort files in a given path

- [X] Receives the dir path as a arg

- [X] Ignore files types of a determined list

- [X] Ignore files with size above 1 GB

- [X] Process args 
  - [X] Create a arg parser

  - [X] Receive the `-v` or `--verbose` to activate the log in command line

  - [X] Receive the `-m <size>` or `--minSize <size>` arg to especify the minimun size of the file that will be moved

  - [X] Receive the `-M <size>` or `--maxSize <size>` arg to especify the max size of the file that will be moved 

  - [X] Receive the `-i <type>` or `--ignore <type>` to ignore a determined file type

  - [X] Receive the `-I` or `--ignoreDefault` to ignore the default ignored files

  - [X] Receive the `-c <type> <dir_name>` or `--custom <type> <dir_name>` to temporaly sorty the determined file type in a custom dir

- [X] Sort by file name
  - [X] Change the structure of the `src/defaults.json` file to separate extension and name sorting
  - [X] Permite select the sorting of a file by it's name
  - [X] Permite to ignore a file by it's name

- [ ] REGEX
  - [ ] Receive the `-f <regex>` or `--file <regex>` to process only the files that respect the regex 
  
  - [ ] Store regex as a default custom, so the files that correspond to it will be moved to a custom file
    *So file like 'HomeWork.txt' can be parsed to the custom dir '~/Documents/University/HomeWork/'

## BUG FIX
- [X] Fixing a bug, that ocurs when calling `src/organizer.py` in others dirs because it can't find the `src/defaults.json` file
