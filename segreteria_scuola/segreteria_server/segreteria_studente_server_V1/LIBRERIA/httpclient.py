
import http.client

class MyHttpClient():
    
    def __init__(self, nomeHost, porta) -> None:

        self.__nomeHost = nomeHost
        self.__porta = porta


    def SendHTTPData(self, url, data):

        try:

            connection = http.client.HTTPConnection(self.__nomeHost,self.__porta,timeout=10)
            
            connection.request("GET", url + "?" + data)
            
            response = connection.getresponse()

            print(response.read().decode())

            connection.close()

            return response.status
    
        except:
            return 500

                