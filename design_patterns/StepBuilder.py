class HTTPRequest:
    def __init__(self, url, method, headers, body):
        self.url = url
        self.method = method
        self.headers = headers
        self.body = body

    def __str__(self):
        return f"{self.method} {self.url} | Headers: {self.headers} | Body: {self.body}"



class URLStep:
    def set_url(self, url):
        pass

class MethodStep:
    def set_method(self, method):
        pass

class HeaderStep:
    def set_headers(self, headers):
        pass

class BodyStep:
    def set_body(self, body):
        pass

class BuildStep:
    def build(self):
        pass

class HTTPRequestBuilder(URLStep, MethodStep, HeaderStep, BodyStep, BuildStep):
    def __init__(self):
        self.url = None
        self.method = None
        self.headers = {}
        self.body = None

    # Step 1
    def set_url(self, url):
        self.url = url
        return self  # now MethodStep allowed

    # Step 2
    def set_method(self, method):
        self.method = method
        return self  # now HeaderStep allowed
    
    def set_headers(self, headers):
        self.headers = headers
        return self  # now BodyStep allowed

    # Step 4
    def set_body(self, body):
        self.body = body
        return self  # now BuildStep allowed
    # Final Step
    def build(self):
        return HTTPRequest(self.url, self.method, self.headers, self.body)
    
# Example usage:
if __name__ == "__main__":
    req = HTTPRequestBuilder() \
    .set_url("https://api.com") \
    .set_method("POST") \
    .set_headers({"Content-Type": "application/json"}) \
    .set_body("{}") \
    .build()

print(req)
