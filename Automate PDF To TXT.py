import os
import time
import win32com.client
import win32gui
import win32process

def get_path():
    """ Return the current working directory. """
    return os.path.dirname(os.path.abspath(__file__))+'/'

shell = win32com.client.Dispatch("WScript.Shell")
shell.AppActivate('Console2')

# Load all .pdf files from the /PDF directory
classes = []
for pdf_file in os.listdir(get_path() + "PDF"):
    if pdf_file.endswith(".pdf"):
        classes.append(pdf_file)
        file = open("Output/" + pdf_file + ".txt", 'w')
        file.close()

# Open each .pdf, and copy its text. Then past that
# into a new txt file
time_to_sleep = 5
for pdf_file in classes:
    # Open the .pdf file
    os.startfile(get_path() + 'PDF/' + pdf_file)
    time.sleep(time_to_sleep)
    # Take control of the pdf reader window 
    adobe = win32gui.GetForegroundWindow()
    # Select all text and copy
    shell.SendKeys('^{a}')
    shell.SendKeys('^{c}')
    shell.SendKeys('^{w}')
    time.sleep(time_to_sleep)
    shell.SendKeys('^{w}')
    time.sleep(time_to_sleep)

    # Open the .txt file
    os.startfile(get_path() + "Output/" + pdf_file + '.txt')
    time.sleep(time_to_sleep)
    # Take control of the txt editor window
    notepad = win32gui.GetForegroundWindow()
    # Paste the text
    shell.SendKeys('^{v}')
    shell.SendKeys('^{s}')
    shell.SendKeys('^{w}')