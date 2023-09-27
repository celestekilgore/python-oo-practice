from random import choice

class WordFinder:
    """Word Finder: finds random words from a file."""

    def __init__(self,file_path):
        """Makes a new instance of WordFinder given a file path"""

        print("inside parent __init__")
        self.file_path = file_path
        self.words = self.get_file_data()
        print(f"{len(self.words)} words read")

    def __repr__(self):
        return f"<WordFinder file path = {self.file_path}"

    def get_file_data(self):
        """Reads the instance's file, returns a list of each line in the file"""

        print("inside parent get_file_data")
        with open(self.file_path,"r") as file:
            words_list = [line.strip() for line in file]
        return words_list

    def random(self):
        """returns a random element from instance's words list"""

        return choice(self.words)

class RandomWordFinder(WordFinder):
    """Finds random words from a file. Adds clean_file method"""

    def get_file_data(self): #make method name the same as parent for polymorphism
        """Iterates over instances word list and removes extra whitespace and #s"""

        print("inside child get_file_data")
        lst = [word for word in super().get_file_data() if word != "" and not word.startswith("#")]
        return lst

