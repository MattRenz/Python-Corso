
from http.server import BaseHTTPRequestHandler, HTTPServer


DB_Studenti = ""

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

   # Implementiamo il metodo che risponde alle richieste GET
    
    def do_GET(self):
        
        Url_Contenuto = self.path
        
        contenuto = Url_Contenuto.split("?")[1]

        Nome = contenuto.split("&")[0].split("=")[1].replace("+", " ")
        Cognome = contenuto.split("&")[1].split("=")[1].replace("+", " ")
        Email = contenuto.split("&")[2].split("=")[1]
        Matricola = contenuto.split("&")[3].split("=")[1]
        
        contenutoFile = f'{Nome};{Cognome};{Email};{Matricola}'

        self.SalvaStudente(contenuto, contenutoFile)
        
        print("Il client ha chiesto" + Url_Contenuto)
        
        self.send_response(200)

        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Studente aggiunto"
    
        self.wfile.write(bytes(message, "utf8"))
        return
        
        
    def run():
        print('Avvio del server...')

        server_address = ('127.0.0.1', 8081)
        httpd = HTTPServer(server_address, testHTTPServer_RequestHandler) 

        print('Server in esecuzione...')
    
        httpd.serve_forever()

    
    def SalvaStudente(self, contenuto, contenutoFile):

        contenuto = self.path.split("?")[1]

        # linux
        path = "/home/studente15/Desktop/Data Scientist/Python/PROGETTO_Segreteria_Server_versione3(MATTEO)/DB_STUDENTI"
        
        nomeFile = path + "/" + contenuto.split("&")[3].split("=")[1] + ".csv"

        with open(nomeFile, "w") as file:

            file.write(contenutoFile)
   



        
        
        
        
                
                
        
    
        
    


        
    