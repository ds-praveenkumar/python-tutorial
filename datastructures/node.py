# implements single node to store data

class Node:

    def __init__(self, data):
        self.node = None
        self.data = data

    def __repr__( self ):
        return self.data


if __name__ == '__main__':
    n1 = Node(4)
    print(n1)