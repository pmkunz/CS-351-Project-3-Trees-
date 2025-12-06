Tree Selection: Which tree did you choose and why?
    - I chose the Trie (prefix tree) because a this type is naturally suited for prefix-based queries and autocompletion, which piqued my interest. 

Use Cases: What problems does this tree solve well?
    - Autocomplete for search boxes
        - I did this with words
        - (But code tokens and city names would also work!)

Properties: What makes this tree unique? What are its performance characteristics?
    - In this tree's unqiue structure, each node stores a character, child pointers, an is_end flag, and a counter.
    - The maximum depth of the tree is dependent on the max word length.
    - Memory may become large if the words in the text file don't share many of the same prefixes. If more words have common prefixes, there are more shared nodes and memory is reduced. 
    - Input length determines the lookup complexity 
    

Interface Design: Method signatures with descriptions
    What operations does your tree support?
    What are the parameters and return types?
    What is the Big-O time complexity of each operation? (Required for every method)
    What is the space complexity? (if relevant)

        - All of these are listed in the docstrings of my methods. Here they are summarized and simplified, but you can see more detail in trees.py.

            def __init__(self):
            """
            Time Complexity: O(1)
            Space Complexity: O(1)
            """

            def insert(self, word: str) -> None:
            """
            Time Complexity: O(m), where m = length of the word
            Space Complexity: O(m) in the worst case (new nodes created for each character)
            """

            def search(self, word: str) -> bool:
            """
            Time Complexity: O(m), where m is word length
            Space Complexity: O(1)
            """

            def starts_with(self, prefix: str) -> bool:
            """
            Time: O(p), where p is the length of the prefix
            Space: O(1)
            """

            def get_words_with_prefix(self, prefix: str) -> List[str]:
            """
            Time Complexity: O(p + n*k _ n log n),
                where p = prefix length,
                    n = number of results,
                    k = average word length
                    n log n =  sorting by counter
            Space Complexity: O(n*k) for storing results
            """

            delete(self, word: str) -> bool:
            """
            Time Complexity: O(m), where m = word length
            Space Complexity: O(m) 
            """

            def dfs(self, node, prefix: str, out) -> None:
            """
            Time Complexity: O(size of subtrie)
            Space Complexity: O(h), where h = height of subtrie
            """

            def query(self, x: str):
            """
            Time Complexity: O(p + n*k + n log n),
                where p = prefix length
                    n = number of words with prefix
                    k = average word length
            Space Complexity: O(n*k)
            """

             def _find_node(self, prefix: str) -> Optional[TrieNode]:
            """
            Time Complexity: O(p), where p = length of prefix
            Space Complexity: O(1)
            """
            
    Important: Your initial interface is a starting point. You will likely need to add methods or modify signatures as you build your application. Document these changes in your final submission!

        I started by referencing both the example interface in the assignment description as well as the provided source:
        https://ayeung.dev/2020/06/15/python-trie.html

        I still needed to actually implement these methods:
            search
            starts_with
            get_words_with_prefix
            delete

        I also added the method _find_node, which served as a helper fucntion to avoid repeating the same traversal for search, starts_with, and get_words_with_prefix

        
Implementation Notes: Key algorithms or techniques you'll use
    - Trie nodes: store a character, a dictionary of children, a boolean is_end, and a counter in the case of duplicate words
    - Insertions: new nodes are created if a character is missing
    - Search and prefix operations to check for existence
    - Deletion uses a stack
    - Depth-first search (dfs) was used to efficinetly collect words starting from a given node
    - Sorting by using get_words_with_prefix and query, which ensures the mot freuqnelty inserted words appear first