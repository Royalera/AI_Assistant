# from hugchat import hugchat

# def ai_process(command):
#     user_input = command.lower()
#     chatbot = hugchat.ChatBot(cookie_path="C:\\python\\pythonproject\\ai assistant\\cookies.json")
#     id = chatbot.new_conversation()
#     chatbot.change_conversation(id)
#     response =  chatbot.chat(user_input)
#     print(response)
#     # speak(response)
#     return response

# print(ai_process("Hello"))

from hugchat import hugchat
import time

def ai_process(command):
    """
    Process user input using the HugChat chatbot.
    """
    # Validate the input
    if not isinstance(command, str) or not command.strip():
        raise ValueError("Input must be a non-empty string.")

    user_input = command.lower()

    # Initialize the chatbot
    try:
        chatbot = hugchat.ChatBot(cookie_path="C:\\python\\pythonproject\\ai assistant\\cookies.json")
    except hugchat.exceptions.ChatBotInitError as e:
        print(f"Error: {e}")
        return "Failed to initialize chatbot. Check the cookies.json file."

    # Create a new conversation and switch to it
    try:
        conversation_id = chatbot.new_conversation()
        chatbot.change_conversation(conversation_id)

        # Retry mechanism for API overload
        for attempt in range(3):  # Retry up to 3 times
            try:
                response = chatbot.chat(user_input)
                if response:  # Ensure the response is valid
                    print(response)
                    # speak(response)  # Uncomment if text-to-speech is implemented
                    return response
                else:
                    print("Empty response received, retrying...")
            except Exception as e:
                print(f"Attempt {attempt + 1}: Error during chat: {e}")
                time.sleep(2)  # Wait 2 seconds before retrying

        # If retries fail
        return "The chatbot failed to respond. Please try again later."

    except Exception as e:
        print(f"Error during chatbot conversation: {e}")
        return "An error occurred during processing."

# Example usage
if __name__ == "__main__":
    try:
        response = ai_process("Hello")
        print(f"Chatbot Response: {response}")
    except Exception as e:
        print(f"Unhandled Error: {e}")
