class FileSystemComponent:
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        raise NotImplementedError("Subclasses must implement this method")
    
class File(FileSystemComponent):
    def display(self, indent=0):
        print(" " * indent + self.name)

class Directory(FileSystemComponent):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def display(self, indent=0):
        print(" " * indent + self.name + "/")
        for child in self.children:
            child.display(indent + 2)



# Example usage
root = Directory("root")    
home = Directory("home")
root.add(home)
home.add(File("file1.txt"))

home.add(File("file2.txt"))
documents = Directory("documents")
home.add(documents)
documents.add(File("resume.docx"))  
root.display()
