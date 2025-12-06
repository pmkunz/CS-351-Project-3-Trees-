import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.tree import Trie

""" 
INSTRUCTIONS:
0. Run "pip install pytest" in the terminal, if you don't already have pytest installed.
1. Then run "pytest -v" in the terminal. You will see an output showing which tests passed and which failed.

"""

def test_insert_search():
    """ 
    -Inseritng a word makes it searchable in the Trie
    -Searching for a prefix that is not a full word returns False
    """

    t = Trie()                          # create an empty Trie
    t.insert("apple")                   # Insert word
    assert t.search("apple") == True    # Word has fully been inserted. So True
    assert t.search("app") == False     # "app" is only a prefix, not a word. So False


def test_prefix_and_get():
    """
    -Tests that starts_with() correclty identifies valid prefixes
    -Tests that get_words_with_prefix() returns all the matching words
    """
    t = Trie()                          # create an empty Trie
    for w in ["app", "apple", "application", "apt"]: 
        t.insert(w)                     # Inserting several words that share prefixes
    assert t.starts_with("ap") is True
    results = t.get_words_with_prefix("app") # get all words that begin with "app"
    words = [w for w, c in results]         # List with the extracted words
    assert "app" in words and "apple" in words and "application" in words # They should appear in autocomplete results


def test_delete_and_counter():
    """
    -Inserting the same word twice increases its count
    -Deleting the word once still leaves one remaining instance
    - Deleting the word twice fully removes it
    """

    t = Trie()                          # create an empty Trie
    t.insert("test")                    # Insert the same word twice
    t.insert("test")                    # ^
    assert t.search("test") is True     # Check that the word exists
    t.delete("test")                    # Delete one
    assert t.search("test") is True     # But one should still exist
    t.delete("test")                    # Delete the other one
    assert t.search("test") is False    # Now there should be none that exist
