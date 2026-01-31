# # Variables

# Cajas -> Variables 
# Pueden variar en casi cualquier forma 
# Estan conformados por un nombre y un valor

print("Muejkej")

# Creacion de una variable

my_name = "Jose Guerra"

print(my_name)

var = 1
account_balance = 1000.0
client_name = 'Jose Guerra'

print(var, account_balance, my_name)

var = "3.14.2"
print("Python version: " + var)

var = 1
print("\n", var, end = " ", sep = "")
var = var + 2
print(var, end = "\n\n")

# Calculo de hipotenusa
co = 3.0
ca = 4.0
h = (co ** 2 + ca ** 2) ** 0.5
print("cateto opuesto =", co, "cateto adyacente =", ca, "hipotenusa =", h, sep = ", ")

# Utilizando f-strings :D
print(f"cateto opuesto = {co}, cateto adyacente = {ca}, hipotenusa = {h}")

# Imprimir resultados alineados tipo tabla
print("Imprimir resultados alineados tipo tabla\n")

print(f"{'Cateto opuesto':<20} = {co:>8.2f}")


