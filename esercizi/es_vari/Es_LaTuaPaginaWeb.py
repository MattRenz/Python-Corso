"""
Chiedi all'utetne il titolo 

Chiedi all'utetne il testo centrale 

Chiedi all'utente il testo interno

Open file

scrivi prima riga

"""


print("\n Impostazione pagina web")

print("\n Imposta la tua pagina web con: 1) Titolo pagina 2) Titolo centrale 3) COntenuto")

title = input("Titolo pagina: ")

h1 = input("Titolo h1: ")

p = input("Contenuto p: ")


title_HTML = f'<head><title>{title}</title></head>\n\n'

h1_HTML = f'<body><center><h1>{h1}</h1></center></body>\n\n'

p_HTML = f'<br><p>{p}</p>'

paginaHTML = "/home/studente15/Desktop/Data Scientist/Python/HTML/ES_LaTuaPaginaWeb.html"

lista = [title_HTML,h1_HTML,p_HTML]

file = open(paginaHTML, "w")

for i in lista:

    file.write(i)



