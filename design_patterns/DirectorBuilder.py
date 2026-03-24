class HTTPRequest:
    def __init__(self, Builder):
        self.method = Builder.method
        self.url = Builder.url
        self.headers = Builder.headers
        self.body = Builder.body
        
    def __str__(self):
        return f"Method: {self.method}, URL: {self.url}, Headers: {self.headers}, Body: {self.body}"
    
    class Builder:
        def __init__(self,url): 
            self.url = url
            self.method = 'GET'
            self.headers = {}
            self.body = None
        
        def set_method(self, method):
            self.method = method
            return self
        def set_headers(self, headers):
            self.headers.update(headers)
            return self
        def set_body(self, body):
            self.body = body
            return self
        def build(self):
            return HTTPRequest(self)
        

class HTTPRequestDirector:
   
    def build_authenticated_post(self, url, token, body):
        return HTTPRequest.Builder(url) \
            .set_method("POST") \
            .set_headers({"Authorization": f"Bearer {token}", "Content-Type": "application/json"}) \
            .set_body(body) \
            .build()

    def build_simple_get(self, url):
        return HTTPRequest.Builder(url) \
            .set_method("GET") \
            .build()
    
   
# Example usage:
if __name__ == "__main__":
    # Simple GET request
    get = HTTPRequestDirector().build_simple_get("https://api.example.com/users")

    # POST with body and custom timeout
    post = HTTPRequestDirector().build_authenticated_post(
        "https://api.example.com/users",
        "token123",
        '{"name":"Alice","email":"alice@example.com"}'
    )


    print(get)
    print(post)
