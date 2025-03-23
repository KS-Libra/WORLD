# Matriz 3D de temperaturas
temperaturas = [
    # Ciudad 1
    [
        # Semana 1
        [20, 22, 24, 21, 23, 25, 22],
        # Semana 2
        [21, 23, 25, 22, 24, 26, 23],
        # Semana 3
        [22, 24, 26, 23, 25, 27, 24]
          
    ],
    # Ciudad 2
    [
        # Semana 1
        [18, 20, 22, 19, 21, 23, 20],
        # Semana 2
        [19, 21, 23, 20, 22, 24, 21],
        # Semana 3
        [20, 22, 24, 21, 23, 25, 22]
        
    ],
    # Ciudad 3
    [
        # Semana 1
        [16, 18, 20, 17, 19, 21, 18],
        # Semana 2
        [17, 19, 21, 18, 20, 22, 19],
        # Semana 3
        [18, 20, 22, 19, 21, 23, 20]
        
    ]
]

# Calcular el promedio de temperaturas por ciudad y semana
for ciudad in range(len(temperaturas)):
    print(f"Ciudad {ciudad + 1}:")
    for semana in range(len(temperaturas[ciudad])):
        total_temperatura = 0
        for dia in range(len(temperaturas[ciudad][semana])):
            total_temperatura += temperaturas[ciudad][semana][dia]
        promedio_temperatura = total_temperatura / len(temperaturas[ciudad][semana])
        print(f"Semana {semana + 1}: {promedio_temperatura:.2f}°C")
    print()   