
temperatura_fahr = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(temperatura_fahr)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print("El valor en grados centigrados es:", round(cel))
except:
    print('Please enter a number')