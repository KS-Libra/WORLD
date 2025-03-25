#calcular la temperatura promedio de una ciudad durante un período de tiempo
def calculate_average_temperature(city_data):
    """
    Calcula la temperatura promedio de múltiples ciudades y semanas.
    
    Args:
        city_data (list): Una lista de listas que contiene los datos de temperatura de cada ciudad.
                         Cada elemento de la lista principal representa una ciudad, y cada elemento
                         de la lista anidada representa las temperaturas de una semana.
    
    Returns:
        dict: Un diccionario que contiene la temperatura promedio de cada ciudad.
    """
    average_temperatures = {}
    
    for i, city_temps in enumerate(city_data):
        city_name = f"Ciudad {i+1}"
        total_temps = 0
        num_temps = 0
        
        for week_temps in city_temps:
            for temp in week_temps:
                total_temps += temp
                num_temps += 1
        
        average_temp = total_temps / num_temps
        average_temperatures[city_name] = average_temp
    
    return average_temperatures
# Datos de ejemplo
city_data = [
    # Ciudad 1
    [
        # Semana 1
        [20, 22, 24, 21, 23, 25, 22],
        # Semana 2
        [21, 23, 25, 22, 24, 26, 23],
        # Semana 3
        [22, 24, 26, 23, 25, 27, 24],
        # Nueva Semana 4
        [23, 25, 27, 24, 26, 28, 25]
    ],
    # Ciudad 2
    [
        # Semana 1
        [18, 20, 22, 19, 21, 23, 20],
        # Semana 2
        [19, 21, 23, 20, 22, 24, 21],
        # Semana 3
        [20, 22, 24, 21, 23, 25, 22],
        # Nueva Semana 4
        [21, 23, 25, 22, 24, 26, 23]
    ],
    # Ciudad 3
    [
        # Semana 1
        [16, 18, 20, 17, 19, 21, 18],
        # Semana 2
        [17, 19, 21, 18, 20, 22, 19],
        # Semana 3
        [18, 20, 22, 19, 21, 23, 20],
        # Nueva Semana 4
        [19, 21, 23, 20, 22, 24, 21]
    ]
]

average_temps = calculate_average_temperature(city_data)
print(average_temps)
