from Content import BoldTextContent, TextContent, ImageContent, ItalicTextContent

class Command:
    def execute(self):
        pass

    def undo(self):
        pass

class AddTextCommand(Command):
    def __init__(self, document, content):
        self.document = document
        self.content = content

    def execute(self):
        self.document.addContent(self.content)

    def undo(self):
        # Logic to remove the added text from the document
        self.document.contents=[content for content in self.document.contents if content != self.content                                    ]

class AddImageCommand(Command):
    def __init__(self, document, content):
        self.document = document
        self.content = content                  

    def execute(self):
        self.document.addContent(self.content)

    def undo(self):
        # Logic to remove the added image from the document
        self.document.contents=[content for content in self.document.contents if content != self.content]

class BoldTextCommand(Command):
    def __init__(self, document, content):
        self.document = document
        self.content = content

    def execute(self):
        bold_content=BoldTextContent(self.content)
        self.document.addContent(bold_content)

    def undo(self):
        # Logic to remove the bold text from the document
        self.document.contents=[content for content in self.document.contents if content.render() != f'<b>{self.content}</b>']  