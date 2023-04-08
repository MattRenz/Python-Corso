def SalvaPassword(contenutoFile):
        
    nomeFile = "path" + "/pswd.csv"

    contenutoFile = contenutoFile
    
    file = open(nomeFile, "w")
    file.write(contenutoFile)
    file.close
