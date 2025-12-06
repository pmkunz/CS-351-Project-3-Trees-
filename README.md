Paige Kunz
The Trie (Prefix Tree)

    I implemented a Trie (prefix tree), which is a tree-based data structure meant for fast prefix lookups. My application laods a list of words, stores them in a Trie, and provides an interactive autocomplete system. Users may input any prefix and instantly receive matching word sucggestiosn, ranked by frequency of insertion. 

    Anyone building search bars, code editors, or mobile keybaord suggestions would benefit from using the Trie, since it offers very fast prefix queries. 
    

Installation & Setup

    Prerequisites (Python version, libraries, etc.)
        - No external libraries are required

    Step-by-step setup instructions
        1. Clone or download this repositroy
        2. Run the application 
        3. Ensure the folder setup looks correct:

            /data
                words.txt
            /screenshots

            /src
                application.py
                tree.py
            /tests
                test_trie.py
        
Usage Guide

    How to run and use your application
        1. Use the run button in application.py
        2. You'll see something like this:

                ---Autocomplete System (Trie)---
                Loaded 20 words into the Trie.
                Type a prefix to get autocomplete suggestions.
                Type 'exit' to quit.

                Enter prefix: 
        3. This is a prompt for user input. As an example, you may enter "app"
        4. Then you will see this:

                Enter prefix: app

                Suggestions:
                    app
                    apple
                    application
                    apply

        5. You will be prompted to enter another prefix, OR you can type "exit" to quit the program. 

    - There is also a test_trie.py file in which you can run a few tests.

        INSTRUCTIONS: 
        
        0. Run "pip install pytest" in the terminal, if you don't already have pytest installed.

        1. Then run "pytest -v" in the terminal. You will see an output showing which tests passed and which failed.


Screenshots/Demos
    Screenshots showing my application in action can be seen inside /screenshots. 

Tree Implementation Details

    Brief explanation of how your tree works
        Each node stores a single character, child pointers, an is_end boolean to mark full words, and a counter to track duplicate insertions. 

    Time/space complexity of key operations
        m = word length
        p = prefix length
        k = average word length
        
        insert(word)
            Time Complexity: O(m)
            Space Complexity: O(m)
        
        search(word)
            Time Complexity: O(m)
            Space Complexity: O(1)

        starts_with(prefix)
            Time Complexity: O(p)
            Space Complexity: O(1)

        get_words_with_prefix(prefix)
            Time Complexity: O(p + n*k _ n log n),
                where p = prefix length,
                    n = number of results,
                    k = average word length
                    n log n =  sorting by counter
            Space Complexity: O(n*k) for storing results

        delete(word)
            Time Complexity: O(m)
            Space Complexity: O(m) 
        
        _find_nodeprefix()
            Time Complexity: O(p)
            Space Complexity: O(1)

    Any interesting implementation choices
        The _find_node method served as a helper fucntion to avoid repeating the same traversal for search, starts_with, and get_words_with_prefix.

Evolution of the Interface

    What changed from your initial design and why?
        - Added _find_node to reduce duplicated traversal code
        - Added sorting to prefix queries, giving a better autocomplete experience
        - Added return types and full docstrings under every method for clarity

    What did you learn from this iterative process?
        - Tries can be simply understood conceptually, but they require careful handling of small details such as prefix tracking, returning words, and logic for deletion
        - A good interface makes the job a lot easier
        - Tree-based structures force you to think abotu parent/child relationships and the layout for memory

Challenges & Solutions
    
    What was hard? How did you solve tough problems?
        - Removing nodes without accidentally breaking other words required careful attention.
        - Needed to avoid repeating the same traversal for search, starts_with, and get_words_with_prefix. The _find_node method served as a helper fucntion for this.
    
Future Enhancements
    What would you add with more time?
        - I only tried my application with word,  but code tokens and city names would also work!
        - The ability to update the dictionary, adding new words based on user input
        - A visualizer to show the tree 