import openai
import os

def gpt_in_terminal(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    try:    
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                  {"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt},
    ]
    )
    
        return response.choices[0].message['content'].strip()
    except openai.error.RateLimitError as e:
        return "Rate limit exceeded. Please try again later."
    except openai.error.AuthenticationError as e:
        return "Authentication error. Please check your API key."
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"

def main():
    print("Welcome to gpt!")
    print("Type your queries below. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        response = gpt_in_terminal(user_input)
        print(f"GPT: {response}")

if __name__ == "__main__":
    main()
