import speech_recognition as sr
import tkinter as tk

def start_listening():
    # Initialize the recognizer
    r = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Speak now!")
        # Listen for speech and convert it to text
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: ", text)
            # Insert the recognized text into the text box
            text_box.insert(tk.END, text + "\n")
        except:
            print("Sorry, could not recognize your speech.")

# Create the GUI
root = tk.Tk()
root.title("Voice to Text")

# Create the text box
text_box = tk.Text(root, height=10, width=50)
text_box.pack(pady=10)

# Create the "Start" button
start_button = tk.Button(root, text="Start", command=start_listening)
start_button.pack()

root.mainloop()

