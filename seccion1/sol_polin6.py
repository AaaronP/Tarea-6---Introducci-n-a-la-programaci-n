def encontrar_soluciones(coeficientes):
    soluciones = []
    for x in range(-1000, 1001):  # Ampliado el rango de valores de x
        valor_polinomio = 0
        for i, coeficiente in enumerate(coeficientes[::-1]):
            print(coeficiente)
            valor_polinomio += coeficiente * (x**i)
        # Utilizar una tolerancia en lugar de igualdad exacta
        if valor_polinomio == 0:
            soluciones.append(x)
    return soluciones


# Ejemplo de uso
coeficientes = [1, 3, -1, -3]
soluciones = encontrar_soluciones(coeficientes)
print(soluciones)
