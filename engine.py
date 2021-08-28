class huffman:


    class Node:
        def __init__(self , freq = 0 , ch = None , left = None, right = None) -> None:
            self.freq = freq
            self.ch = ch
            self.left = left
            self.right = right
        def __repr__(self) -> str:
            if not self.left and not self.right:
                return self.ch
            return "{ch : %s freq: %s  left: %s right: %s}" % (self.ch, self.freq , self.left , self.right) 



    def __init__(self , input) -> None:
        fp = open(input , "r")
        self.text = fp.read()
        fp.close()
        self.encode()








    #sorts nodes for making the tree
    def sort_nodes(self,nodes):
        for i in range(len(nodes)):
            for j in range(i + 1  , len(nodes)):
                if nodes[i].freq > nodes[j].freq:
                    nodes[i] , nodes[j] = nodes[j],nodes[i]
        return nodes

    #makes trees
    def make_tree(self,freq):
        nodes = []
        for x in freq:
            nodes.append(self.Node(freq[x], x,))
        nodes = self.sort_nodes(nodes)
        for x in nodes:
            print(x.ch , x.freq)
        while len(nodes) >= 2:
            x = nodes.pop(0)
            y = nodes.pop(0) 
            nodes.append(self.Node(x.freq+y.freq , None,x,y))
            nodes = self.sort_nodes(nodes)
        return nodes[0]

    #gets Frequency for each node
    def get_freq(self,text):
        freq = {}
        for x in text:
            freq[x] = freq.get(x,0) + 1
        return freq

    def encode(self):
        freq = self.get_freq(self.text)
        self.make_tree(freq)
        



if __name__ == "__main__":
    huffman("text.txt")