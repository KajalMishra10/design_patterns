class decorator:
    def update(self):
        pass

class text(decorator):
    def __init__(self,content):
        self.content=content
    def update(self):
        return self.content


class decor(decorator):
    def __init__(self,decor):
        self.decor1=decor

class bold(decor):
    def __init__(self, decor):
        super().__init__(decor)
    def update(self):
        return self.decor1.update()+'bolded'
        
class Italic(decor):
    def __init__(self, decor):
        super().__init__(decor)
    def update(self):
        return self.decor1.update()+'italiced'
    
styled = bold(Italic(text('kajal')))
print(styled.update())
