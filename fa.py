import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

# FAQ dictionary -- Mobile Store
faqs = {
    "What types of mobile phones do you sell?": "We offer a wide range of mobile phones, including the latest models from brands like Apple, Samsung, Google, and more.",
    "Do you offer phone repairs?": "Yes, we provide repair services for most mobile devices, including screen replacements, battery changes, and software troubleshooting.",
    "What warranty do you provide on mobile phones?": "All new phones come with a manufacturer warranty, typically lasting one year. Extended warranty options are also available.",
    "Can I trade in my old phone?": "Yes, we offer trade-in programs where you can receive credit towards your new phone when you bring in your old device.",
    "Do you have financing options available?":"Yes, we provide various financing options, including installment plans and credit options to help you purchase your new phone.",
    "What accessories do you sell?":"We carry a variety of accessories, including cases, screen protectors, chargers, and headphones for all major phone models.",
    "How long does it take to receive my order?":"Shipping typically takes 3-5 business days, depending on your location and the availability of the product.",
    "Do you offer customer support for technical issues?":"Absolutely! Our customer support team is available to assist you with any technical questions or issues you may have.",
    "What payment methods do you accept?":"We accept major credit cards, debit cards, PayPal, and cash for in-store purchases.",
    "Are there any promotions or discounts available?":"Yes, we regularly have promotions and discounts on select models and accessories. Be sure to check our website or visit the store for current offers.",
}
def preprocess_input(user_input):
    """Tokenize and lower the user input."""
    tokens = word_tokenize(user_input.lower())
    return tokens

def find_best_answer(user_input):
    """Find the best matching answer based on keywords."""
    input_tokens = preprocess_input(user_input)
    
    best_match = None
    best_score = 0
    
    for question, answer in faqs.items():
        question_tokens = preprocess_input(question)
        
        #  the score based on matching tokens
        score = len(set(input_tokens) & set(question_tokens))
        
        
        if any(token in question_tokens for token in input_tokens):
            score += 1  # Boost the score for keyword presence

        if score > best_score:
            best_score = score
            best_match = answer
    
    return best_match if best_match else "I'm sorry, I don't have an answer for that."


def chat():
    print("Welcome to the Mobile Store Chatbot! (Type 'exit' to quit)")
    print()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = find_best_answer(user_input)
        print(f"Chatbot: {response}")

# Starting the chatbot
if __name__ == "__main__":
    chat()


