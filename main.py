import tkinter as tk
from tkinter.scrolledtext import ScrolledText

from openai import OpenAI

#from dotenv import load_dotenv, find_dotenv
#_ = load_dotenv(find_dotenv())


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_openai_response(a_instructions, a_input):

    res = "Testing"
    '''
    response = client.responses.create(
        model="gpt-4o",
        instructions=a_instructions,
        input = a_input
    )
    res = response.output_text
    '''
    #instructions="You are a coding assistant that talks like a pirate.",
    #input="How do I check if a Python object is an instance of a class?",

    print(res)
    return res

def on_button_click():

    user_text = text_input.get("1.0", tk.END)
    mood = radio_var.get()

    instructions = f"""
    You are a coding assistant that has a {mood} mood or personality."
    """
    text_box.configure(state ='normal')
    text_box.insert(tk.END, "Mood: " + mood + "\n")
    text_box.insert(tk.END, user_text)
    text_box.configure(state ='disabled')

    response = get_openai_response(instructions, user_text)

    text_box.configure(state ='normal')
    text_box.insert(tk.END, response + "\n\n")
    text_box.configure(state ='disabled')

#----------------------------------
# MAIN
#----------------------------------

client = OpenAI()

# Create the main window
root = tk.Tk(screenName="Chatbot")
root.iconbitmap('img/hwdchiva.ico')
root.title("Chatbot")

# Create a ScrolledText widget
text_box = ScrolledText(root, state='disabled', wrap=tk.WORD, height=10, width=40)
text_box.pack(padx=10, pady=5)

# Create a Text widget for input
text_input_label = tk.Label(root, text="Enter text here:")
text_input_label.pack(pady=0)
text_input = tk.Text(root, wrap=tk.WORD, height=2, width=40)
text_input.pack(pady=5)

# Create a frame with a border to group the radio label and radio buttons
radio_group_frame = tk.Frame(root, relief=tk.SOLID, borderwidth=2)
radio_group_frame.pack(pady=10, padx=10, fill=tk.X)

# Add a label for the radio button frame
radio_label = tk.Label(radio_group_frame, text="Chatbot Mood")
radio_label.pack(pady=1)

# Add a variable to track the selected radio button
radio_var = tk.StringVar(value="Nice")

# Create a frame for the radio buttons
radio_frame = tk.Frame(radio_group_frame)
radio_frame.pack(pady=5)

# Add three mutually exclusive radio buttons
nice = tk.Radiobutton(radio_frame, text="Nice", variable=radio_var, value="Nice")
nice.pack(side=tk.LEFT, padx=5)

shake = tk.Radiobutton(radio_frame, text="Shakespeare", variable=radio_var, value="Shakespeare")
shake.pack(side=tk.LEFT, padx=5)

angry = tk.Radiobutton(radio_frame, text="Angry", variable=radio_var, value="Angry")
angry.pack(side=tk.LEFT, padx=5)

# Create a Button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=5)

# Example usage: Print the active radio button value when the button is clicked
#button = tk.Button(root, text="Get Active Radio", command=lambda: print(get_active_radio()))
#button.pack(pady=5)

# Run the application
root.mainloop()

