
from http.server import BaseHTTPRequestHandler, HTTPServer


studente = []

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

   # Implementiamo il metodo che risponde alle richieste GET

    def do_GET(self):

        print("Il client ha chiesto" + self.path)

        studente.append(self.path)
        
        self.send_response(200)

        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Studente aggiunto"
    
        self.wfile.write(bytes(message, "utf8"))
        return
    
    def run():
        print('Avvio del server...')

        IndirizzoIP = input("Indirizzo IP: ")
        porta = int(input("Porta: "))

        server_address = (IndirizzoIP, porta)
        httpd = HTTPServer(server_address, testHTTPServer_RequestHandler) 

        print('Server in esecuzione...')

        httpd.serve_forever()  
            
            
                    
                    
            
        
            
        


        
    