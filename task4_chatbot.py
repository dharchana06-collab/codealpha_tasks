import datetime

def get_reply(msg, name):
    msg = msg.lower().strip()

    if msg == "hello" or msg == "hi" or msg == "hey":
        return "Hi " + name + "!"
    elif "how are you" in msg:
        return "I'm fine, thanks! How are you?"
    elif "i am fine" in msg or "i am good" in msg:
        return "Great to hear that!"
    elif "your name" in msg:
        return "I am CodeBot, a simple Python chatbot."
    elif "time" in msg:
        return "The time now is " + datetime.datetime.now().strftime("%H:%M")
    elif "date" in msg or "today" in msg:
        return "Today's date is " + datetime.datetime.now().strftime("%d-%m-%Y")
    elif "help" in msg:
        return "You can say: hello, how are you, your name, time, date, joke, bye"
    elif "joke" in msg:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"
    elif "thank" in msg:
        return "You're welcome!"
    elif msg == "bye" or msg == "exit":
        return "Goodbye, " + name + "! Have a nice day."
    else:
        return "Sorry, I did not understand. Type help to see what I can do."


print("=== CodeBot ===")
name = input("What is your name? ")
print("Nice to meet you,", name, "! Type help to see options, bye to exit.")

while True:
    user = input(name + ": ")
    if user.strip() == "":
        print("Bot: Please type something.")
        continue
    answer = get_reply(user, name)
    print("Bot:", answer)
    if user.lower().strip() == "bye" or user.lower().strip() == "exit":
        break
