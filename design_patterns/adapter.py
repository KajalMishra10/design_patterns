class Adapter:
    def convert(self,pdf):
        pass

class convertPDF(Adapter):
    def __init__(self):
        self.remoteMethod=XMLProvider()

    def convert(self,pdf):
        s=self.remoteMethod.execute(pdf)
        return s+'converted to json'

class XMLProvider:
    def execute(self,pdf):
        return 'your pdf convert to xml'

class client:
    def __init__(self,adapter):
        self.adapter=adapter

    def execute(self,pdf):
        s=self.adapter.convert(pdf)
        print(s)


adp=convertPDF()
client1=client(adp)

client1.execute('here is my pdf convert it ok!')
