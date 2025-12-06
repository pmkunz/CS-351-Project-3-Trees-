from tree import Trie

DATA_FILE = "../data/words.txt"

def load_words(filepath: str) -> list[str]:
    """
    Load a list of words from a file
    Returns a list of strings (words)
    """
    words = []
    try:
        with open(filepath, "r") as f:
            for line in f:
                word = line.strip()     # remove new lines and spaces
                if word:                # ignore empty lines
                    words.append(word)
    except FileNotFoundError:
        print(f"Error: Could not find {filepath}. Make sure the file exists.")
    return words


def main():
    """ 
    Runs an interactive autocomplete program, using a Trie.

    -Loads a list of words from the file
    -Inserts the words into the Trie
    -Prompts the user to enter prefixes
    -Prints up to 10 autocomplete suggestions for each prefix
    -Runs continuously, until the user exits the program

    """

    print("---Autocomplete System (Trie)---")

    trie = Trie()                   # Create an empty Trie
    words = load_words(DATA_FILE)   # Load words from the text file 

    # Insert words into Trie:
    for w in words:
        trie.insert(w)

    print(f"Loaded {len(words)} words into the Trie.")
    print("Type a prefix to get autocomplete suggestions.")
    print("Type 'exit' to quit.\n")

    # Input loop for the autocomplete system:
    while True:
        prefix = input("Enter prefix: ").strip()

        # To exit the program:
        if prefix.lower() == "exit":
            print("Goodbye!")
            break

        # user must type at least one character
        if not prefix:
            print("Please enter at least one character.\n")
            continue

        # Retrieve autocomplete suggestions (using the get_words_with_prefix method)
        results = trie.get_words_with_prefix(prefix)

        if not results:
            print("No suggestions found.\n")
        else:
            print("\nSuggestions:")
            for word, count in results[:10]:   # show top 10 suggestions
                print(f"  {word}")
            print()                            # blank line for spacing


if __name__ == "__main__":
    main()
