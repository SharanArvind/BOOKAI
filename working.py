import google.generativeai as genai

# API key
genai.configure(api_key="AIzaSyADHeHvTj-UQmPfnKMpWXlgPUTQSsfxmy8")

# generation and safety settings
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(model_name="gemini-pro",
                             generation_config=generation_config,
                             safety_settings=safety_settings)

# Initialize conversation history
convo = model.start_chat()

# Welcome message
print("Welcome to your Book Chatbot! Ask me anything about books.")

# Loop for continuous conversation
while True:
    # user input
    user_query = input("You: ")

    # Check for quit command
    if user_query.lower() == "quit":
        break

    # Send user query to the model
    convo.send_message(user_query)

    # Retrieve and print model response
    model_response = convo.last.text
    print(f"Bot: {model_response}")

# Final message
print("Thank you for chatting with me! See you next time.")