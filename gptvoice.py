# BY CHATGPT 

import pyttsx3
import tkinter as tk
import openai

# Set your API key here
openai.api_key = "your_openai_key"

def get_gpt3_response(question):
  # Send the question to GPT-3
  response = openai.Completion.create(engine="text-davinci-003", prompt=question, max_tokens=1024)
  # Print the GPT-3 response in the console
  print(response.choices[0].text)
  # Return the GPT-3 response
  return response.choices[0].text

def speak_response(response):
  engine = pyttsx3.init()
  engine.say(response)
  engine.runAndWait()

# Create the main window
window = tk.Tk()
window.title("GPT-3 Chatbot")

# Create the text field
text_field = tk.Entry(window)
text_field.pack()

# Set the background color of the window to gray
window.configure(bg="gray")

# Set the width and height of the window
window.geometry("620x45")

# Make the "Send" button clicked by pressing Enter in the text field
def send_question():
  question = text_field.get()
  response = get_gpt3_response(question)
  speak_response(response)
text_field.bind(send_question)

# Make the text field bar increase while the user is typing
text_field.configure(width=100)

# Create the button
def send_question():
  question = text_field.get()
  response = get_gpt3_response(question)
  speak_response(response)

button = tk.Button(window, text="Send", command=send_question)
button.pack()

# Start the GUI event loop
window.mainloop()
