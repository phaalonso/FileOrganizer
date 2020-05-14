# File Organizer

This sricpt can be utilised to organize files by the file extensio.

## How to use
There is two ways to use it.

You can simply call `python3 src/organizer.py <path_to_dir>` passing the path to the dir that you want to organize! :D

In linux you also can give the file permission to execute with `chmod +x src/organizer.py` and run the program with `.src/organizer.py <path_to_dir>`.

### TO DO
[X] Sort files in a given path

[X] Receives the dir path as a arg

[X] Ignore files types of a determined list

[X] Ignore files with size above 1 GB

[ ] Process args 
    [ ] Create a arg parser

    [ ] Receive the `-v` or `--verbose` to activate the log in command line

    [ ] Receive the `-m <size>` or `--minSize <size>` arg to especify the minimun size of the file that will be moved

    [ ] Receive the `-M <size>` or `--maxSize <size>` arg to especify the max size of the file that will be moved 

    [ ] Receive the `-i <type>` or `--ignore <type>` to ignore a determined file type

    [ ] Receive the `-I` or `--ignoreDefault` to ignore the default ignored files

    [ ] Receive the `-c <type> <dir_name>` or `--custom <type> <dir_name>` to temporaly sorty the determined file type in a custom dir