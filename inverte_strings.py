def inverter_string(texto):
    invertida = ''
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    return invertida

# Teste com uma string
texto = input("Informe uma string: ")
print("String invertida:", inverter_string(texto))



