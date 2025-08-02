# Rule-Based Chatbot by Hitheesh Babu M

def get_bot_reply(user_input):
    message = user_input.strip().lower()

    if any(greet in message for greet in ["hi", "hello", "hey"]):
        return "Hi there! How can I help you today?"
    elif "how are you" in message:
        return "I'm just code, but I'm functioning well! 😊"
    elif "name" in message:
        return "I'm your friendly chatbot, created by Hitheesh."
    elif "help" in message:
        return "Sure! You can ask me about general questions."
    elif "bye" in message or "exit" in message:
        return "Goodbye! Hope to talk to you again soon."
    else:
        return "Hmm... I’m not sure I understand that. Could you rephrase?"

# Chat loop
print("🤖 Chatbot Activated! Type 'bye' to end the chat.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit"]:
        print("Bot: Goodbye! 👋")
        break
    bot_reply = get_bot_reply(user_input)
    print("Bot:", bot_reply)
