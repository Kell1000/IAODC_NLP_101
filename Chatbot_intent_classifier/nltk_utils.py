# Import necessary libraries
import numpy as np
import nltk
# Uncomment the line below if 'punkt' is not already downloaded
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

# Initialize the PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    """
    Split sentence into array of words/tokens.
    A token can be a word, punctuation character, or number.
    
    Parameters:
    sentence (str): The sentence to tokenize.
    
    Returns:
    list: A list of tokens.
    """
    # Use NLTK's word_tokenize to split the sentence into words/tokens
    return nltk.word_tokenize(sentence)

def stem(word):
    """
    Stemming: Find the root form of the word.
    Examples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    
    Parameters:
    word (str): The word to stem.
    
    Returns:
    str: The stemmed word.
    """
    # Convert the word to lowercase and then stem it
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    """
    Return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise.
    
    Example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bag   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    
    Parameters:
    tokenized_sentence (list): The sentence that has been tokenized into a list of words.
    words (list): The list of known words.
    
    Returns:
    np.array: A bag of words array.
    """
    # Stem each word in the tokenized sentence
    sentence_words = [stem(word) for word in tokenized_sentence]
    # Initialize the bag with 0 for each known word
    bag = np.zeros(len(words), dtype=np.float32)
    # Mark the presence of known words in the sentence
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag