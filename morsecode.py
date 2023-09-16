import RPi.GPIO as GPIO  # Import the GPIO library for Raspberry Pi
import time  # Import the time module for controlling timing
from tkinter import *  # Import the tkinter library for creating the GUI
from gpiozero import LED  # Import the LED module from gpiozero for controlling the LED

GPIO.setmode(GPIO.BOARD)  # Set the GPIO mode to BOARD, which refers to pin numbering

led = LED(17)  # Create an LED object connected to GPIO pin 17
blink_duration = 0.25  # Define the duration for a Morse code dot

def mdot():
    led.on()  # Turn on the LED
    time.sleep(blink_duration)  # Pause for the dot duration
    led.off()  # Turn off the LED
    time.sleep(blink_duration)  # Pause again for the dot duration

def mdash():
    led.on()  # Turn on the LED
    time.sleep(4 * blink_duration)  # Pause for the dash duration (4 times dot duration)
    led.off()  # Turn off the LED
    time.sleep(blink_duration)  # Pause again for the dot duration

MORSE_CODE = {
     'A': '. _',
    'B': '_ . . .',
    'C': '_ . _ .',
    'D': '_ . .',
    'E': '.',  # Morse code for 'E' is just a dot
    'F': '. . _ .',
    'G': '_ _ .',
    'H': '. . . .',
    'I': '. .',
    'J': '. _ _ _',
    'K': '_ . _',
    'L': '. _ . .',
    'M': '_ _',
    'N': '_ .',
    'O': '_ _ _',
    'P': '. _ _ .',
    'Q': '_ _ . _',
    'R': '. _ .',
    'S': '. . .',
    'T': '_',  # Morse code for 'T' is a dash
    'U': '. . _',
    'V': '. . . _',
    'W': '. _ _',
    'X': '_ . . _',
    'Y': '_ . _ _',
    'Z': '_ _ . .',
    ' ': ' ',  # Space character in Morse code
}

def Convert_to_morsecode(name):
    name = name.upper()  # Convert the input text to uppercase
    ename = ""  # Initialize the variable to store the Morse code
    for char in name:
        if char == ' ':
            ename += ' '  # If the character is a space, add a space to separate words
            time.sleep(7 * blink_duration)  # Pause for the word space duration
        else:
            code = MORSE_CODE.get(char, '')  # Get the Morse code for the character
            ename += code + ' '  # Append the Morse code and add a space to separate symbols
            for symbol in code:
                if symbol == '.':
                    mdot()  # Blink the LED for a dot
                elif symbol == '_':
                    mdash()  # Blink the LED for a dash
                time.sleep(blink_duration)  # Pause between Morse code symbols
    return ename  # Return the Morse code as a string

def Write():
    name = inputtxt.get("1.0", "end-1c")  # Get the text from the input Text widget
    ename = Convert_to_morsecode(name)  # Convert the text to Morse code
    morse_label.config(text="Morse Code: " + ename)  # Update the label to display the Morse code

win = Tk()  # Create a Tkinter window
win.title("Morse Code GUI")  # Set the window title
win.geometry('400x300')  # Set the window size

# Black and mint theme
win.configure(bg="black")  # Set the window background color to black
label = Label(win, text="Convert alphabets to Morse Code", font=("Helvetica", 14), fg="mint cream", bg="black")
inputtxt = Text(win, height=6, width=20, bg="mint cream", font=("Helvetica", 12))  # Create a Text widget
MorseButton = Button(win, height=2, width=20, text="Convert", command=Write, font=("Helvetica", 12), bg="mint cream")
morse_label = Label(win, text="Morse Code: ", font=("Helvetica", 12), fg="mint cream", bg="black")
spacing_label = Label(win, text="", font=("Helvetica", 12), bg="black")  # Create a spacing label

label.pack()  # Pack the label into the window
inputtxt.pack()  # Pack the input Text widget into the window
MorseButton.pack()  # Pack the Convert button into the window
spacing_label.pack()  # Pack the spacing label into the window
morse_label.pack()  # Pack the Morse code label into the window

win.mainloop()  # Start the Tkinter main loop
