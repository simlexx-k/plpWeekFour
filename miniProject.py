import json
import difflib


# Load data from JSON file into a Python dictionary
def load_dictionary():
    with open('data.json') as file:
        data = json.load(file)
    return data


# Function to get definition of a word
def get_definition(word, data):
    word = word.lower()  # Convert word to lowercase
    if word in data:
        return data[word]
    else:
        similar_words = difflib.get_close_matches(word, data.keys())
        if similar_words:
            suggestion = similar_words[0]  # Take the first suggestion
            return f"Word not found. Did you mean '{suggestion}'?"
        else:
            return "Word not found in dictionary."


# Main function
def main():
    dictionary = load_dictionary()
    word = input("Enter a word: ")
    definition = get_definition(word, dictionary)
    print(definition)


if __name__ == "__main__":
    main()
