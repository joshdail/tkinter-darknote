# Darknote
## v.1.1.0

Darknote is a text editor for .txt files built with Tkinter, featuring light text on a dark background.

### Features:

- Customize your color settings! Set your background color and font color. Your settings will be saved when you close the program.
- Extract text from PDF files into the main window (Note: Darknote cannot create or edit PDF files)

### Dependencies:

- Python 3.9
- Tkinter
- pdfminer.six


### Notes:

Your color settings are saved in a file named config.txt, which MUST be in the same directory as the main application file. If no config file is found, for example if the config file is deleted, Darknote will automatically generate a config file. However, the config file is not meant to be edited directly by the user.
