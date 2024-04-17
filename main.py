import openai

# Set up your OpenAI API key
openai.api_key = 'sk-proj-ehPPP9ydLbLMF6IK6zINT3BlbkFJdQknPUqKftokKAac7CA1'

def ask_gpt(prompt):
    # Call the completion endpoint of the API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to the GPT Chatbot!")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = ask_gpt(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
