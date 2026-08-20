# ==========================================
# Project 1: Rule-Based AI Chatbot
# Artificial Intelligence - DecodeLabs
# ==========================================

print("=" * 50)
print("        🤖 RULE-BASED AI CHATBOT")
print("=" * 50)
print("Hello! I am your AI chatbot.")
print("You can ask me simple questions.")
print("Type 'bye', 'exit', or 'quit' to end the chat.")
print("=" * 50)


# Continuous conversation loop
while True:

    # Take input from the user
    user_input = input("\nYou: ").strip().lower()

    # -------------------------------
    # Greeting rules
    # -------------------------------
    if user_input in ["hello", "hi", "hey", "hii", "hola"]:
        print("Bot: Hello! 👋 How can I help you?")

    elif user_input in ["good morning", "morning"]:
        print("Bot: Good morning! ☀️ I hope you are having a great day.")

    elif user_input in ["good evening", "evening"]:
        print("Bot: Good evening! 🌙 How can I help you?")

    # -------------------------------
    # Basic conversation
    # -------------------------------
    elif user_input in ["how are you", "how are you doing"]:
        print("Bot: I'm doing great! Thanks for asking. 😊")

    elif user_input in ["what is your name", "your name"]:
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user_input in ["who are you", "what are you"]:
        print("Bot: I am a simple AI chatbot created using Python.")

    # -------------------------------
    # AI-related questions
    # -------------------------------
    elif user_input in ["what is ai", "what is artificial intelligence"]:
        print("Bot: Artificial Intelligence is the simulation of human")
        print("     intelligence by computer systems.")

    elif user_input in ["what is a chatbot", "define chatbot"]:
        print("Bot: A chatbot is a computer program that communicates")
        print("     with users through text or voice.")

    elif user_input in ["what is rule based ai", "what is rule based chatbot"]:
        print("Bot: Rule-based AI uses predefined rules to decide")
        print("     what response should be given to the user.")

    # -------------------------------
    # Help
    # -------------------------------
    elif user_input in ["help", "what can you do"]:
        print("Bot: I can:")
        print("     • Respond to greetings")
        print("     • Answer basic AI questions")
        print("     • Tell you about myself")
        print("     • Continue a conversation")
        print("     • Exit when you say bye")

    # -------------------------------
    # Thank-you responses
    # -------------------------------
    elif user_input in ["thanks", "thank you", "thankyou"]:
        print("Bot: You're welcome! 😊")

    # -------------------------------
    # Positive responses
    # -------------------------------
    elif user_input in ["good", "great", "awesome", "nice"]:
        print("Bot: That's great to hear! 👍")

    # -------------------------------
    # Exit commands
    # -------------------------------
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        print("Bot: Goodbye! 👋")
        print("Bot: Thanks for chatting with me.")
        break

    # -------------------------------
    # Unknown input
    # -------------------------------
    else:
        print("Bot: I'm sorry, I don't understand that.")
        print("Bot: Try asking me something else or type 'help'.")


print("\nChatbot session ended.")