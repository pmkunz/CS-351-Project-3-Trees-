from typing import Dict, List, Tuple, Optional

class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a counter indicating how many times a word is inserted
        # (if this node's is_end is True)
        self.counter = 0

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}


class Trie(object):
    """The trie object"""

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.root = TrieNode("")
    
    def insert(self, word: str) -> None:
        """Insert a word into the trie
        Time Complexity: O(m), where m = length of the word
        Space Complexity: O(m) in the worst case (new nodes created for each character)
        """
        node = self.root
        
        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        
        # Mark the end of a word
        node.is_end = True

        # Increment the counter to indicate that we see this word once more
        node.counter += 1

    def search(self, word: str) -> bool:
        """Check if word exists in trie
        Time Complexity: O(m), where m is word length
        Space Complexity: O(1)
        """
        node = self._find_node(word)
        return bool(node and node.is_end)

    def starts_with(self, prefix: str) -> bool:
        """Check if any word has this prefix
        Time: O(p), where p is the length of the prefix
        Space: O(1)
        """
        return self._find_node(prefix) is not None

    def get_words_with_prefix(self, prefix: str) -> List[str]:
        """Return all words starting with prefix
        Time Complexity: O(p + n*k _ n log n),
            where p = prefix length,
                  n = number of results,
                  k = average word length
                  n log n =  sorting by counter
        Space Complexity: O(n*k) for storing results
        """
        if prefix == "":
            # traverse entire trie
            node = self.root
            start_pref = ""
        else:
            node = self._find_node(prefix)
            if node is None:
                return []
            # to form words correctly we pass prefix up to char before node.char
            # but since _find_node returned node for last char in prefix,
            # pass prefix[:-1] and dfs will append node.char
            start_pref = prefix[:-1]

        out: List[Tuple[str, int]] = []
        self.dfs(node, start_pref, out)

        # sort by counter desc then lexicographically for stable output
        out.sort(key=lambda x: (-x[1], x[0]))
        return out

    def delete(self, word: str) -> bool:
        """Remove word from trie
        Time Complexity: O(m), where m = word length
        Space Complexity: O(m) 
        """
        # stack to hold (parent, char, node) so we can traverse back to prune
        node = self.root
        stack: List[Tuple[TrieNode, str, TrieNode]] = []

        for char in word:
            if char in node.children:
                parent = node
                node = node.children[char]
                stack.append((parent, char, node))
            else:
                return False  # word not present

        if not node.is_end:
            return False  # prefix existed but not a word

        # if multiple insertions were done, just decrement counter
        if node.counter > 1:
            node.counter -= 1
            return True

        # else counter == 1, remove word mark and prune nodes if needed
        node.is_end = False
        node.counter = 0

        # prune nodes from leaf upwards while they have no children and are not ends
        while stack:
            parent, char, child = stack.pop()
            if child.children or child.is_end:
                break  # cannot prune this child
            # else safe to remove child node
            del parent.children[char]
        return True
        
    def dfs(self, node, prefix: str, out) -> None:
        """Depth-first traversal of the trie
        
        Args:
            - node: the node to start with for traversal
            - prefix: the current prefix, for tracing a word while traversing the trie
            - out: output list to append results

        Time Complexity: O(size of subtrie)
        Space Complexity: O(h), where h = height of subtrie
        """
        if node.is_end:
            out.append((prefix + node.char, node.counter))
        
        for child in node.children.values():
            self.dfs(child, prefix + node.char, out)
        
    def query(self, x: str):
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of 
        times they have been inserted

        Time Complexity: O(p + n*k + n log n),
            where p = prefix length
                  n = number of words with prefix
                  k = average word length
        Space Complexity: O(n*k)
        """
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        out = []
        node = self.root
        
        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []
        
        # Traverse the trie to get all candidates
        self.dfs(node, x[:-1], out)

        # Sort the results in reverse order and return
        return sorted(out, key=lambda x: x[1], reverse=True)


    def _find_node(self, prefix: str) -> Optional[TrieNode]:
        """Return the node corresponding to the end of the prefix, or None if it doesn't exist.
        Time Complexity: O(p), where p = length of prefix
        Space Complexity: O(1)
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
