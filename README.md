old school homework

# Name to Binary convertor.

This application is an educational graphical application that converts the text entered by the user into the binary system and returns the resulting binary code to the user. Its purpose is to show how characters are written in binary format on a computer and to simplify the understanding of the basic principles of coding.

## The main functionality

- accepts the name entered by the user and the language selected.
- checks the input text based on the selected language.
- converts the entered text into the binary system (8-bit Unicode values).
- displays the result.

## Bonus Functionality & Limitation

- Current time display in binary system.
- Allow only Georgian (Mkhedruli) or Latin (English) characters depending on the selected language (additionally allows spaces to accommodate names that contain more than one word).

## Technology Used

- [**Python3**](https://www.python.org)
- **ReGex**
- [**PyQt5**](https://pypi.org/project/PyQt5/)
- [**Qt Designer**](https://www.pythonguis.com/installation/install-qt-designer-standalone/)

### Requirements:

1. Have **Python3** installed
\
If you don't have it installed, go to the official website and install the version of Python 3 using the installer appropriate for your operating system.

2. Have **PyQt5** installed
\
If you don't have it installed, open a terminal and type the following command:
\
Linux/Mac - `sudo pip3 install PyQt5`
\
Windows - `pip install PyQt5`

### Running the program

- Download the ZIP file and extract it, open a terminal and go to the same extracted folder and type the following command to run the program: `python3 main.py`

or

- Open a terminal on your computer, go to the folder where you want to download the project. In the same place, type the Git command: `git clone https://github.com/borderlineping/BTN.git`, then enter the project folder: `cd BTN` and run the program: `python3 main.py`

### Testing

After running the program, you will instantly see the current time in binary. Select your preferred language and enter your name in the text field. After clicking the button, you will see the result in binary code :))
