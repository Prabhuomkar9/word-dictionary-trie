from pandas import read_csv
from time import time


class TrieNode:
    """
    Node of Trie data structure
    """

    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.isEndOfWord: bool = False
        self.meaningAt: int = -1


class TrieDictionary:
    """
    Word Dictionary using Trie data sturcture
    """

    def __init__(self):
        self.trie: TrieNode = TrieNode()
        self.dictionary: list[str] = []
        self.wordCount: int = 0

    def insert(self, word: str, meaning: str) -> None:
        """
        Inserts a word along with its meaning into the trie dictionary.

        Params:
            word (str): The word to be inserted into the trie dictionary.
            meaning (str): The meaning corresponding to the inserted word.

        Return:
            None

        Time Complexity: O(m)
        Space Complexity: O(m)
            where m is the length of the word being inserted.
        """
        word = word.lower()
        curr = self.trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEndOfWord = True
        self.dictionary.append(meaning)
        curr.meaningAt = self.wordCount
        self.wordCount += 1

    def search(self, word: str) -> bool:
        """
        Searches for a word in the trie dictionary.

        Params:
            word (str): The word to search for in the trie dictionary.

        Return:
            (bool) -> True if the word exists in the trie dictionary, False otherwise.

        Time Complexity: O(m)
        Space Complexity: O(1)
            where m is the length of the word being searched.
        """
        word = word.lower()
        curr = self.trie
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isEndOfWord

    def getMeaningOf(self, word: str) -> str:
        """
        Retrieves the meaning of a word from the trie dictionary.

        Params:
            word (str): The word whose meaning is to be retrieved from the trie dictionary.

        Return:
            (str) -> The meaning of the specified word.

        Rasies:
            KeyError: If the specified word does not exist in the trie dictionary.

        Time Complexity: O(m)
        Space Complexity: O(1)
            where m is the length of the word whose meaning is being retrieved.
        """
        word = word.lower()
        curr = self.trie
        for c in word:
            if c not in curr.children:
                raise KeyError("Word not found")
            curr = curr.children[c]
        if not curr.isEndOfWord:
            raise KeyError("Word not found")
        return self.dictionary[curr.meaningAt]

    def printTrie(self) -> None:
        """
        Prints the structure of the trie.

        Param: None

        Return: None

        Time Complexity: O(n)
        Space Complexity: O(n)
            where n is the total number of nodes in the trie.
        """

        def dfs(node: TrieNode, level: int) -> None:
            for c in node.children:
                print("  " * level + c)
                dfs(node.children[c], level + 1)

        dfs(self.trie, 0)

    def printDictionary(self) -> None:
        """
        Prints the dictionary of words along with their meanings.

        Param: None

        Return: None

        Time Complexity: O(w)
        Space Complexity: O(w)
            where w is the number of words in the dictionary.
        """
        for i, meaning in enumerate(self.dictionary):
            print(f"Idx {i} : {meaning}")


if __name__ == "__main__":
    # Driver Code
    timestamp: float = time()
    print("Trie Dictionary")
    td = TrieDictionary()

    if input("Do you want to preload some words? (y/n): ").lower() == "y":
        df = read_csv("data.csv")
        for i in range(len(df)):
            word = df.iloc[i, 0]
            meaning = df.iloc[i, 1]
            td.insert(word, meaning)

    while True:
        print("Choices: ")
        print("1. Insert new word")
        print("2. Search for a word")
        print("3. Get meaning of a word")
        print("4. Print Trie")
        print("5. Print Dictionary")
        print("6. Quit")

        choice = int(input("Enter choice: "))
        if choice == 1:
            word = input("Enter word to insert: ")
            meaning = input(f"Enter meaning of {word}: ")
            td.insert(word, meaning)
        elif choice == 2:
            word = input("Enter word to search: ")
            wordExists = td.search(word)
            print(f"Word '{word}' exists: {wordExists}")
        elif choice == 3:
            word = input("Enter word to get meaning: ")
            try:
                meaning = td.getMeaningOf(word)
                print(f"Meaning of '{word}': {meaning}")
            except KeyError:
                print(f"Word '{word}' not found")
        elif choice == 4:
            td.printTrie()
        elif choice == 5:
            td.printDictionary()
        elif choice == 6:
            timestamp = time() - timestamp
            print(f"Execution time: {timestamp}s")
            break
        else:
            print("Invalid choice! Try again.")
