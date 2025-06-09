import nltk
nltk.download('brown')
nltk.download('punkt')
import tkinter as tk
from textblob import TextBlob

class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sentiment Chatbot")

        self.chat_log = tk.Text(master, state='disabled', width=60, height=20, wrap='word', bg="#f0f0f0")
        self.chat_log.pack(padx=10, pady=10)

        self.entry = tk.Entry(master, width=50)
        self.entry.pack(padx=10, pady=(0,10), side=tk.LEFT)
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(padx=(0,10), pady=(0,10), side=tk.LEFT)

        self.insert_message("Chatbot: Hello! I am a simple chatbot. Type 'exit' to end the conversation.")

    def insert_message(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, message + "\n")
        self.chat_log.config(state='disabled')
        self.chat_log.yview(tk.END)

    def send_message(self, event=None):
        user_input = self.entry.get().strip()
        if not user_input:
            return

        self.insert_message(f"You: {user_input}")
        self.entry.delete(0, tk.END)

        if user_input.lower() == "exit":
            self.insert_message("Chatbot: Goodbye!")
            self.entry.config(state='disabled')
            self.send_button.config(state='disabled')
            return

        sentiment = TextBlob(user_input).sentiment.polarity
        if sentiment > 0:
            response = "I'm glad to hear that!"
        elif sentiment < 0:
            response = "I'm sorry to hear that."
        else:
            response = "That's interesting!"

        self.insert_message(f"Chatbot: {response}")


if __name__ == "__main__":
    root = tk.Tk()
    chatbot_gui = ChatbotGUI(root)
    root.mainloop()

