import os
from GestoreStudioLegale.Servizi import Cliente

class Tools():

    def __init__(self):
        pass

    def leggi(self,file = 'Credenziali',n = 5):
        if os.path.isfile(f'GestoreStudioLegale/Dati/{file}.pickle'):
            with open(f'GestoreStudioLegale/Dati/{file}.pickle', 'r') as f:
                if n ==0 :
                    return f.read()
                stringa1 = f.read(n)
                #stringa1 = f.readline()
                #stringa2 = f.readline()
                #self.salvaAppend(stringa2)
                return stringa1

    def salva(self, stringa,file='Credenziali'):
        if os.path.isfile(f'GestoreStudioLegale/Dati/{file}.pickle'):
            with open(f'GestoreStudioLegale/Dati/{file}.pickle', 'w') as f:
                f.write(stringa)
                f.write('\n')

    def salvaAppend(self, stringa,file='Credenziali'): #per richiamarlo anche poi con la password
        if os.path.isfile(f'GestoreStudioLegale/Dati/{file}.pickle'):
            with open(f'GestoreStudioLegale/Dati/{file}.pickle', 'a') as f:
                f.write(stringa)
                f.write('\n')