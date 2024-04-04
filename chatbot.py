import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import random

# Download NLTK resources (word tokenizer, stopwords list, lemmatizer)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Define responses for the chatbot
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thank you!", "I'm doing well, thanks for asking!", "All good here, thanks!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm not sure what you mean."],
}

# Function to preprocess user input
def preprocess_input(user_input):
    # Tokenize the input
    tokens = word_tokenize(user_input.lower())
    # Remove stopwords and lemmatize tokens
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    return tokens

# Function to generate response based on user input
def generate_response(user_input):
    tokens = preprocess_input(user_input)
    # Loop through each response category
    for key in responses:
        # Check if any of the keywords in the user input match the keywords for this response category
        if any(keyword in tokens for keyword in preprocess_input(key)):
            # If there is a match, randomly select and return a response from this category
            return random.choice(responses[key])
    # If no matching response category is found, return a default response
    return random.choice(responses["default"])

# Main loop for interacting with the chatbot
print("Welcome! How can I help you today?")
while True:
    user_input = input("> ")
    # Check if the user wants to quit the chatbot
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    else:
        # Generate and print a response based on the user's input
        response = generate_response(user_input)
        print(response)
