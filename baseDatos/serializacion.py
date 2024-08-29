import pickle

def serializar(Babilon):
    file=open("baseDatos/temp/Datos.pickle","wb")
    pickle.dump(Babilon,file)
    file.close()

def deserializar():
    file=open("baseDatos/temp/Datos.pickle","rb")
    datos=pickle.load(file)
    return datos