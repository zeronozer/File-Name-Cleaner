# FileNameCleaner

FileNameCleaner is a Python program that removes a specified string or symbol from file names in the current directory.

The "FileNameCleaner" repository contains a Python program that removes a specified string or symbol from file names in the current directory. The program is easy to use and requires only Python 3.6 or higher and the keyboard module. The program is useful for cleaning up file names and making them more consistent and readable. The repository also includes a README.md file with instructions for usage, notes, license information, and contribution guidelines.

## Requirements

- Python 3.6 or higher
- keyboard module: `pip install keyboard`

## Usage

1. Download the `filenamecleaner.py` file to your computer.
2. Open a terminal window and navigate to the directory that contains the `filenamecleaner.py` file.
3. Run the program by typing `python filenamecleaner.py` in the terminal.
4. When prompted, enter the string or symbol that you want to remove from file names in the current directory.
5. The program will remove the specified string or symbol from file names in the current directory and print a message for each file that has been renamed.
6. To exit the program, press the "Esc" key or close the terminal window.

## Notes

- The program only removes the specified string or symbol from file names in the current directory and does not modify the contents of the files.
- The program uses the `keyboard` module to detect when the "Esc" key is pressed and exit the program. If you encounter any issues with the "Esc" key detection, try running the program in a different terminal or shell.
- The program does not support recursive directory search. It only removes the specified string or symbol from file names in the current directory.
- The program will raise a `FileNotFoundError` if the specified directory does not exist.

## License

This program is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions to this program are welcome. If you encounter any issues or have suggestions for improvements, please create an issue or a pull request on the Codeberg repository.