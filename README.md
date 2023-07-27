
---

# WWF Quiz Game

This is a Python-based WWF Quiz game designed to raise awareness about endangered species. 

## Prerequisites

The game requires Python 3.x to run. If you haven't installed Python on your system, follow the instructions below:

### Installing Python

1. Visit the official [Python downloads page](https://www.python.org/downloads/).
2. Download the version suitable for your operating system.
3. Run the installer and ensure that you check the box that says "Add Python to PATH" during installation. This will make Python executable from your command line interface.

### Locating Python in System Directory

1. By default, Python is typically installed in a location like: `C:\Users\<your-username>\AppData\Local\Programs\Python\Python39\`.
2. Please replace `<your-username>` with your actual username.

### Adding Python to System PATH

If you didn't add Python to your PATH during the installation, follow these steps:

1. Right-click on the 'Computer' icon on your desktop or in the Start Menu.
2. Choose 'Properties'.
3. Click on 'Advanced system settings'.
4. Click on 'Environment Variables...'.
5. Under 'System variables', scroll until you find the 'Path' variable, then click on 'Edit...'.
6. In the 'Variable value:' box, scroll to the end of the string and add the path to your Python directory. Be sure to separate this new entry from the previous one with a semicolon (;).
7. Click 'OK' to close each of the windows.

## Running the Game

You can run the WWF Quiz Game from the command line interface in your operating system.

### Windows Command Prompt or PowerShell

1. Navigate to the directory containing the game using the `cd` command. For example: `cd C:\Users\<your-username>\Desktop\PythonGame`.
2. Run the game with the command: `python wwfquiz.py`.

### Git Bash

If you are using Git Bash and you face an issue with Python not being recognized, you can create an alias for the Python command in your current Git Bash session:

1. Run this command (replace the path with the actual path to your Python installation):
    ```
    alias python='winpty C:\\Users\\<your-username>\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
    ```

2. Navigate to the directory containing the game using the `cd` command. For example: `cd ~/Desktop/PythonGame`.
3. Run the game with the command: `python wwfquiz.py`.

*Please note: This alias is only valid for the current session of Git Bash. If you close and reopen Git Bash, you would have to set the alias again.*

## Contributions

Contributions, issues, and feature requests are welcome!

Enjoy the game!

---