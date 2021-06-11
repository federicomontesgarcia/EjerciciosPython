import pandas as pd

ventas = pd.Series([15,12,21], index = ["Ene", "Feb", "Mar"])
print(ventas)

print()
print(ventas["Ene"])

print()
print(ventas.index)
print(ventas.values)

print()
ventas.name = "Ventas 2020"
print(ventas.name)

ventas.index.name = "Meses"
print(ventas)

print()
print(ventas.axes)
print(ventas.shape)

