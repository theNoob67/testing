from socket import timeout as Timeout
from urllib.request import urlopen as requests, URLError as UniformError

class Requests():
    def __init__(self, urls):
        self.urls = urls

    def requests(self):
        try:
            with requests(self.urls, timeout=10) as response:
                print(self.urls, response.getcode())
        except Exception as Error:
            print(Error)
        except UniformError:
            print(UniformError)
        except Timeout:
            print(Timeout)
