import re

rules=[
    (r'hi|hello|hey',['Hello! How can I help you today?','Hi there!']),
    (r'my name is (.*)',['Nice to meet you, {0}!']),
    (r'how are you',["I'm doing well, thank you! How about you?"]),
    (r'what is your name',['I am a simple rule based chatbot.']),
    (r'(.*) help (.*)',['Sure, tell me more about your problem.']),
    (r'bye|quit|exit',['Goodbye! Have a nice day.']),
]

def get_response(user_input):
    user_input=user_input.lower().strip()
    for pattern,responses in rules:
        match=re.search(pattern,user_input)
        if match:
            response=responses[0]
            if match.groups():
                response=response.format(*match.groups())
            return response
    return "I'm sorry, I did not understand that. Can you rephrase?"

if __name__=="__main__":
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input=input("You: ")
        reply=get_response(user_input)
        print("Chatbot:",reply)
        if re.search(r'bye|quit|exit',user_input.lower()):
            break