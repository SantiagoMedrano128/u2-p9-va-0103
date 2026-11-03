import matplotlib.pyplot as plt
import numpy as np
# Santiago Medrano NC = 0103
materias = ['Vision A','Machine L','Lenguaje N','Pensamiento M','Ingles']
calificaciones = [9,10,8,9,9]

plt.pie(calificaciones, labels=materias, autopct = '% 1.1f%%')
plt.title("Grafica de Pie 0103")
plt.show()
print("Santiago Medrano NC = 0103")