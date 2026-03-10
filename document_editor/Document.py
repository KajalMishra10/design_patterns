from Content import TextContent, ImageContent, BoldTextContent, ItalicTextContent
class Document:
    def __init__(self):
        self.contents = []

    def addText(self, text):
        self.contents.append(TextContent(text))

    def addImage(self, image_url):
        self.contents.append(ImageContent(image_url))
    def addContent(self, content):
        self.contents.append(content)
    def render(self):
        return "\n".join([content.render() for content in self.contents])