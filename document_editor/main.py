from Content import (
    TextContent,
    ImageContent,
    BoldTextContent,
    ItalicTextContent
)
from Command import (
    Command,AddImageCommand,AddTextCommand,BoldTextCommand
)
from Document import Document
from Persistent import FilePersistent, DatabasePersistent
from DocumentEditor import DocumentEditor

def main():
    doc=Document()
    editor=DocumentEditor(doc)
    
    ADD_TEXT_COMMAND=AddTextCommand(doc, TextContent("Hello, World!"))
    #coomand
    ADD_IMAGE_COMMAND=AddImageCommand(doc, ImageContent("https://example.com/image.png"))
    BOLD_TEXT_COMMAND=BoldTextCommand(doc, TextContent("This is bold text."))
    editor.addText(ADD_TEXT_COMMAND)
    editor.addImage(ADD_IMAGE_COMMAND)                       
    editor.addText(BOLD_TEXT_COMMAND)               
    print("Document Content:")
    print(doc.render())
    # Save to file
    editor.save("file")
    editor.save("database")
    # Save to database      
   
if __name__ == "__main__":
    main()  
