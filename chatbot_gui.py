
import tkinter as tk
import random

# Responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! 👋"],
    "how_are_you": ["I'm doing great!", "All systems running smoothly ⚙️"],
    "study": ["Stay consistent. Small steps = big results."],
    "bye": ["Goodbye!", "See you soon!", "Take care!"]
}

def get_response(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return random.choice(responses["greeting"])
    elif "how are you" in user_input:
        return random.choice(responses["how_are_you"])
    elif "study" in user_input:
        return random.choice(responses["study"])
    elif "bye" in user_input:
        return random.choice(responses["bye"])
    else:
        return "I'm still learning 🤖"

def send_message():
    user_text = entry.get()
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_text + "\n")

    bot_reply = get_response(user_text)
    chat_log.insert(tk.END, "Bot: " + bot_reply + "\n\n")

    chat_log.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

# Window
root = tk.Tk()
root.title("Chatbot")
root.geometry("400x500")
root.config(bg="#1e1e2f")  # Dark background

# Face (simple emoji or label)
face = tk.Label(root, text="🤖", font=("Arial", 40), bg="#1e1e2f", fg="white")
face.pack(pady=10)

# Chat area
chat_log = tk.Text(root, height=15, width=45, bg="#2b2b3c", fg="white")
chat_log.pack(pady=10)
chat_log.config(state=tk.DISABLED)

# Entry box
entry = tk.Entry(root, width=30, bg="#3a3a4f", fg="white")
entry.pack(pady=5)

# Send button
send_btn = tk.Button(root, text="Send", command=send_message,
                     bg="#6c63ff", fg="white")
send_btn.pack(pady=5)

root.mainloop()