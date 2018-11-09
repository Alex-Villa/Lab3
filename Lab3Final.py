import AVL
import RedBlack


def main():
    count = [1]
    count[0] = 0

    userWord = input("Enter a word to find anagrams for: ")
    userWord = userWord.lower()
    print("The word", userWord.upper(), "uses two different trees to populate the dictionary.\nWhich of the two trees would you like to use?")

    while True:
        userTreeOption = int(input("1: AVL Tree\n2: Red-black Tree\nOption selected: "))
        if (userTreeOption == 1 or userTreeOption == 2):
            break
        else:
            print("I'm sorry that is not a valid answer please choose between 1 and 2\n")

    while True:
        fileName = input("Enter the name of your file you wish to use to populate the dictionary: ")
        try:
            if (userTreeOption == 1):
                tree = AVL.AVLTree()  # creates AVL tree
            else:
                tree = RedBlack.RedBlackTree()  # creates Red-Black tree
            create_tree(tree, fileName, userTreeOption) # opens file for tree option given
            break  # set to true to exit loop
        except FileNotFoundError:
            print("I'm sorry that file is not found. Please try again.")
    print("\n---------------------------------\nThe anagrams for", userWord.upper(), "are:")
    print_anagrams(userWord, "", tree)
    count_anagrams(userWord, "", tree, count)
    print("\n---------------------------------\n", userWord.upper(), "has a total of", count[0], "anagrams from the dictionary created\n---------------------------------")

    while True:
        fileName2 = input("Enter the name of your next file: ")
        try:
            max_anagrams(tree, count, fileName2) #reads second file and find the word with the most anagrams
            break  # set to true to exit loop
        except FileNotFoundError:
            print("I'm sorry that file is not found. Please try again.")

def create_tree(tree, fileName, userTreeOption):
    with open(fileName, "r") as file:
        for i in file:
            line = i.split()
            line[0] = line[0].lower()
            if (userTreeOption == 1):
                tree.insert(AVL.Node(line[0]))  # inserts to AVL tree
            else:
                tree.insert(line[0])  # inserts to Red-Black tree

# prints all anagrams of a given word
def print_anagrams(word, prefix, tree):

    if len(word) <= 1:
        str = prefix + word

        if (tree.search(str) == True):  # looks for str in the tree
            print(str)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur

            if cur not in before:  # Check if permutations of cur have not been generated.
                print_anagrams(before + after, prefix + cur, tree)

# counts how many anagrams a given word has
def count_anagrams(word, prefix, tree, count):
    if len(word) <= 1:
        str = prefix + word

        if (tree.search(str) == True):  # looks for str in the tree
            count[0] += 1
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur

            if cur not in before:  # Check if permutations of cur have not been generated.
                count_anagrams(before + after, prefix + cur, tree, count)

# finds the word with the maximum amount of anagrams
def max_anagrams(tree, count, fileName2):
    maxAnagrams = 0  # holds the max number of anagrams
    maxWord = ""  # holds the word with max num of anagrams

    with open(fileName2, "r") as file:
        for i in file:
            count[0] = 0
            line = i.split()
            count_anagrams(line[0], "", tree, count)

            if (count[0] > maxAnagrams):
                maxAnagrams = count[0]
                maxWord = line[0]
    print("The word with the most anagrams in", fileName2, "is the word", maxWord.upper(), "with", maxAnagrams, "anagrams.\nThe anagrams for", maxWord.upper(), "are:")
    print_anagrams(maxWord, "", tree)

main()