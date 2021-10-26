import matplotlib.pyplot as plt
import time 
from scipy import signal
 
# Función que se encarga de leer el archivo de entrada y llamar a la función principal. 
def reading(dir):
  file = open(dir,"r")
  string1 = file.read()
  lineas = string1.split('\n')
  num_actividades = int(lineas[0])
  
  actividades = [[0]*3]*num_actividades
  
  for i in range(num_actividades):
    aux = lineas[i+1]
    actividades[i]=aux.split(' ')
  file.close()

  for x in range(num_actividades):
    for y in range(1,3):
      actividades[x][y] = int(actividades[x][y])
  
  # Organizamos las actividades por la hora inicio de actividad. Complejidad: O(n * log(n))
  organized = sorted(actividades, key = lambda p: p[1])

  maximoActividades(organized)
  
# Esta función se encarga de encontrar el número máximo de actividades que no se cruzan.
def maximoActividades (actividades):

    # horarios es un array del tamaño del total de actividades. Aquí se almacenarán todas las actividades que no se cruzan. 
    # En Python, generalmente las variables llamadas '_' se usan para expresar que no serán usadas en sí.
    
    horarios = []

    totalActivities = len(actividades)

    for _ in range(totalActivities):
        horarios.append([])
    
    for i in range(totalActivities):
        for j in range(i):
            inicio = actividades[i][1]
            # inicio es la hora inicial de una actividad
            fin = actividades[j][2]
            # fin es la hora final de una actividad
            if fin <= inicio and len(horarios[i]) < len(horarios[j]):
                horarios[i] = horarios[j].copy()
                
        horarios[i].append(actividades[i])
    # Encontrar la lista escogiendo la lista de tamaño máximo, pues es la lista que encontró más actividades que no se cruzaran.
    finalActivities = []
    for ac in horarios:
           if len(finalActivities) < len(ac):
                  finalActivities = ac

    # Retorna todas las actividades que no se cruzan.
    writeOutput(totalActivities, finalActivities)

def writeOutput(totalActivities, finalActivities):
    with open("output.txt", "w") as f:
        print(totalActivities, file = f)
        for i in range(len(finalActivities)):
            print(finalActivities[i][0], file = f)
    f.close()

tiempos = []
for x in range(1000):
    inicio = time.time()
    aux = reading('./pruebas_actividades/sch'+str(x)+"1")
    final = time.time() - inicio
    tiempos.append(final)

b, a = signal.butter(8, 0.015, 'lowpass')   #Configuration filter 8 representa el orden del filtro.
filtedData = signal.filtfilt(b, a, tiempos)  #tiempos es la señal a filtrar


plt.plot(tiempos)
plt.plot(filtedData)
plt.xlabel("Número de prueba")
plt.ylabel("Tiempo en segundos")
plt.show()

#reading(directorio)












