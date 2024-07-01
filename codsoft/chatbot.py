import re

def chatbot_response(user_input):
    # Converting the input to lowercase to make the chatbot case-insensitive
    user_input = user_input.lower()

    # Pattern matching for predefined responses
    if re.match(r"\b(hello|hi|hey|helo)\b", user_input):
        return "Hello! How can I assist you today?"
    elif re.match(r"\b(bye|goodbye|by|tata)\b", user_input):
        return "Goodbye! Have a great day!"
    elif re.match(r"\b(how are you\?|how are you|how are u)\b", user_input):
        return "I'm a chatbot, so I'm always functioning at full capacity!"
    elif re.match(r"\b(what is your name\?|what is your name|what's your name)\b", user_input):
        return "I am a simple rule-based chatbot."
    elif re.match(r"\b(what can you do\?|what can you do)\b", user_input):
        return "I can respond to basic greetings and questions. Try asking me something!"
    elif re.match(r"\b(tell me a joke|joke)\b", user_input):
        return "Why don't skeletons fight each other? They don't have the guts!!"
    elif re.match(r"\b(what's the weather|weather)\b", user_input):
        return "I can't check the weather, but it’s always sunny in the virtual world!"
    elif re.match(r"\b(thank you|thanks|thx)\b", user_input):
        return "You're welcome! Happy to help."
    elif re.match(r"\b(what's your favorite color|favorite color)\b", user_input):
        return "I like red, the color of the rose and the tika !"
    elif re.match(r"\b(who created you\?|who is your creator|who made you)\b", user_input):
        return "I was created by Bhaskar to assist and chat with you!"
    elif re.match(r"\b(what's your favorite food|favorite food)\b", user_input):
        return "I don't eat, but if I did, I'd probably enjoy byte-sized treats!"
    elif re.match(r"\b(tell me a fact|interesting fact)\b", user_input):
        return "Did you know? Polar beer can smell their prey in the range of 35km!"
    else:
        return "I'm sorry, I don't understand that. Can you try rephrasing?"

# User and chatbot interaction

def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if re.match(r"\b(bye|goodbye|by|tata)\b", user_input.lower()):
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

chat()
