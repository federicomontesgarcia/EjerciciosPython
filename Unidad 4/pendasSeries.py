import pandas as pd

d = {"Ene":7, "Feb":5, "Mar":3 }
s = pd.Series(d)
print(s)

print()
s = pd.Series(d, index = ["Abr", "Mar", "Feb", "Ene"],dtype=int)
print(s)

print()
s = pd.Series(7, index = ["Ene", "Feb", "Mar"])
print(s)