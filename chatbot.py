def response(user_word):
    phrases = ["hello","bye"]
    if phrases[0] in user_word:
        return "Hi there! How can I help you today?"
    elif phrases[1] in user_word:
        return "Goodbye! Have a nice day."
    else:
        return "I’m not sure how to respond to that."
    
def main():
    user_input=input("You: ")
    output=" "
    while user_input != "exit":
        output=response(user_input)
        print("Chatbot: "+output)
        if output == "Goodbye! Have a nice day.":
            #print(output)
            return
        user_input=input("You: ")
    return

main()