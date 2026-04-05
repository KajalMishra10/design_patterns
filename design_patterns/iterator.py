class Iterator:
    def hasNext(self):
        raise NotImplementedError
    
    def next(self):
        raise NotImplementedError


#  Playlist Iterator
class PlayListIterator(Iterator):
    def __init__(self, parent):
        self.parent = parent
        self.index = 0

    def hasNext(self):
        return self.index < len(self.parent.arr)

    def next(self):
        if not self.hasNext():
            return None
        value = self.parent.arr[self.index]
        self.index += 1
        return value


#  Binary Tree Iterator (Inorder)
class BinaryTreeIterator(Iterator):
    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        if not self.hasNext():
            return None
        
        node = self.stack.pop()
        if node.right:
            self._push_left(node.right)
        
        return node.value


#  Playlist
class PlayList:
    def __init__(self, arr):
        self.arr = arr

    def addSong(self, song):
        self.arr.append(song)

    def play(self, a):
        print(f'Playing song {a}')

    def createIterator(self):
        return PlayListIterator(self)


#  Tree Node
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#  Binary Tree (Aggregate)
class BinaryTree:
    def __init__(self, root):
        self.root = root

    def createIterator(self):
        return BinaryTreeIterator(self.root)




print("Playlist Iteration:")
playlist = PlayList(["song1", "song2", "song3"])
playlist.addSong("song4")

it = playlist.createIterator()
while it.hasNext():
    song = it.next()
    playlist.play(song)


print("\nBinary Tree Iteration (Inorder):")



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

tree = BinaryTree(root)
tree_it = tree.createIterator()

while tree_it.hasNext():
    print(tree_it.next())