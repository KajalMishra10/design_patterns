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
        
# Example usage:
if __name__ == "__main__":
    # Simple GET request
    get = HTTPRequest.Builder("https://api.example.com/users") \
        .build()

    # POST with body and custom timeout
    post = HTTPRequest.Builder("https://api.example.com/users") \
        .set_method("POST") \
        .set_headers({"Content-Type": "application/json"}) \
        .set_body('{"name":"Alice","email":"alice@example.com"}') \
        .build()

    # Authenticated PUT with query parameters
    put = HTTPRequest.Builder("https://api.example.com/config") \
        .set_method("PUT") \
        .set_headers({"Authorization": "Bearer token123"}) \
        .set_body('{"feature_flag":true}') \
        .build()

    print(get)
    print(post)
    print(put)