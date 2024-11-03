import pandas as pd

# Cargar los datos
data_path = r'C:\Users\sergi\OneDrive\Escritorio\Bootcamp_DataAnalyst\Temario\Modulo_2\TASMANIA\Data\data_Tasmania.csv'
data = pd.read_csv(data_path)

def filtrar_propiedades(ocupantes, barrio, precio_maximo):
    # Filtrar por número de ocupantes
    filtrado = data[data['ocupantes'] >= ocupantes]
    
    # Filtrar por barrio
    if barrio:
        filtrado = filtrado[filtrado['barrio'] == barrio]
    
    # Filtrar por precio máximo
    filtrado = filtrado[filtrado['precio'] <= precio_maximo]
    
    return filtrado

# Ejemplo de uso
ocupantes = 3
barrio = 'Centro'
precio_maximo = 1000

resultados = filtrar_propiedades(ocupantes, barrio, precio_maximo)
print(resultados)