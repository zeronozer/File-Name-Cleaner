import os
import sys
import shutil
import keyboard


def remove_target_str(directory, target_str) -> None:
    """
    **Remove underscores from filenames in the specified directory.**

    Args:
        directory (str): The directory to search.

    Returns:
        None.

    Raises:
        `FileNotFoundError` if the directory does not exist.

    **Description:**

    This function recursively searches the specified directory for filenames that contain the string "target_str". If a filename is found, the string "target_str" is removed from the filename and the filename is renamed.

        **Example:**

        ```python
        remove_target_str("/home/user/Downloads", "_")

        >>> # The following filenames will be renamed:
        >>> # - (target_str)Book1.pdf
        >>> # - (target_str)Book2.pdf
        >>> # - (target_str)Book3.pdf

        **Additional notes:**

        * The `os.path.isdir()` function returns `True` if the specified path is a directory and `False` otherwise.
        * The `os.listdir()` function returns a list of the files and subdirectories in the specified directory.
        * The `shutil.move()` function moves a file or directory from one location to another.
    
    """

    # Check if the specified directory exists
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a directory.")
        return

    # Loop through all files and subdirectories in the specified directory
    for filename in os.listdir(directory):
        # Check if the filename contains the string "target_str"
        if target_str in filename:
            # Replace the string "target_str" with an empty string to remove it from the filename
            new_filename = filename.replace(target_str, "")
            # Get the full path of the source file
            src = os.path.join(directory, filename)
            # Get the full path of the destination file
            dst = os.path.join(directory, new_filename)
            # Move the file from the source path to the destination path
            shutil.move(src, dst)
            # Print a message to indicate that the file has been renamed
            print(f"Renamed {filename} to {new_filename}")


def get_executable_dir() -> str:
    """
    **Get the directory of the executable file.**

    Args:
        None.

    Returns:
        The directory of the executable file.

    Raises:
        None.

    **Description:**

    This function returns the directory of the executable file. 
    If the file is a PyInstaller executable, the directory of the PyInstaller bundle will be returned.
    Otherwise, the directory of the source code file will be returned.

        **Example:**

        ```python
        >>> get_executable_dir()
        '/home/user/project/directory'
        
        **Additional notes:**

        * The `sys.frozen` attribute is a boolean value that indicates whether the current Python process is running a PyInstaller executable.
        * The `os.path.dirname()` function returns the directory of the specified file or path.
        * The `os.path.abspath()` function returns the absolute path of the specified file or path.
    """

    # Check if the current Python process is running a PyInstaller executable
    if getattr(sys, 'frozen', False):
        # If so, return the directory of the PyInstaller bundle
        return os.path.dirname(sys.executable)
    else:
        # Otherwise, return the directory of the source code file
        return os.path.abspath(os.path.dirname(__file__))
    

def on_key_press(event) -> None:
    """
    **Function to detect if the "Esc" key is pressed.**

    Args:
        event (keyboard.KeyEvent): The keyboard event object.

    Returns:
        None.

    Raises:
        None.

    **Description:**

    This function is used to detect if the "Esc" key is pressed. If it is, the program will exit.

    **Example:**

    ```python
    import keyboard


    def on_key_press(event) -> None:
        if event.name == 'esc':
            print("Process terminated by the user.")
            keyboard.unhook_all()
            exit()


    if __name__ == '__main__':
        keyboard.hook_key_press(on_key_press)
        keyboard.wait()
    ```
    """

    # Check if the "Esc" key is pressed
    if event.name == 'esc':
        # Print a message indicating that the user terminated the program
        print("Process terminated by the user.")
        # Unhook all keyboard hooks (i.e., remove all registered hotkeys)
        keyboard.unhook_all()  
        # Exit the program 
        exit() 


def main() -> None:
    """
    **Main function that removes underscores from file names in the current directory.**

    Args:
        None.

    Returns:
        None.

    Raises:
        None.

    **Description:**

    This function removes underscores from file names in the current directory. It first gets the absolute path of the current directory using the `get_executable_dir()` function. Then it removes underscores from files in the directory using the `remove_underscores()` function. Finally, it registers the event handling function for the "Esc" key using the `keyboard.on_press()` function and keeps the program running for key detection using the `keyboard.wait()` function.

    **Example:**

    ```python
    if __name__ == '__main__':
        main()
    ```

    """
    # Print a message indicating that the program is getting the absolute path of the current directory
    print("Getting the absolute path of the current directory")
    
    # Get the absolute path of the current directory
    directory_path = get_executable_dir()
    # Print a message indicating that the path has been obtained
    print("Path obtained!")

    target_str = input("Enter the word or symbol you want to remove from file names in the current directory: ")
    # Remove underscores from files in the directory
    remove_target_str(directory_path, target_str)
    # Print a message indicating that the program is removing underscores from files in the directory
    print(f"Removing '{target_str}' from files in the directory")

    # Print a message indicating that the process has been completed and provides instructions for exiting the program
    print("Process completed. Press the Esc key or close the window to exit.")

    # Register the event handling function for the "Esc" key
    keyboard.on_press(on_key_press)

    # Keep the program running for key detection
    keyboard.wait('esc')

if __name__ == "__main__":
    main()