class Content:
    def render(self):
        pass


class TextContent(Content):
    def __init__(self,text):
        self.text=text


    def render(self):        
        return self.text
    
class ImageContent(Content):
    def __init__(self,image_url):
        self.image_url=image_url


    def render(self):        
        return f'<img src="{self.image_url}" alt="Image">'
    

class BoldTextContent(Content):
    def __init__(self,content):
        self.content=content
    def render(self):        
        return f'<b>{self.content.render()}</b>'


class ItalicTextContent(Content):  
    def __init__(self,content):
        self.content=content

    def render(self):        
        return f'<i>{self.content.render()}</i>'