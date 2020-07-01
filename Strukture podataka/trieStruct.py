# Preuzeta implementacija sa : https://www.geeksforgeeks.org/trie-insert-and-search/
class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = {}
        self.isEndOfWord = (False,0)
        self.links = {}

    def IntoSet(self):
        s = Set()
        for item in self.links:
            s.dodaj(item)
        return s

class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        return TrieNode()

    def _charToIndex(self, ch):

        return ord(ch) - ord('a')

    def insert(self, key,link):
        key = key.lower()
        node = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if index not in node.children:
                node.children[index] = self.getNode()
            node = node.children[index]
        m = node.isEndOfWord[1] + 1
        node.isEndOfWord = (True, m)

        if link not in node.links:
            node.links[link] = 1
        else:
            node.links[link] += 1

    def search(self, key):
        key = key.lower()
        node = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if index not in node.children:
                return False
            node =  node.children[index]
        return  node.isEndOfWord,node.links,node



    def zaVrednost(self,rijecZaPretragu):
        rijec = rijecZaPretragu.lower()

        if rijec == '':
            return False
        if rijec is None:
            print("Error")

        cvor = self.root
        exists = False
        if self.search(rijec):
            novicvor = self.search(rijec)[2] # ovde nam se nalazi cvor za prvi rec
            exists = True
        else:
            novicvor = self.root


        return exists,novicvor

