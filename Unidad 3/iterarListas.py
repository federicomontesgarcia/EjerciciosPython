preguntas = ['nombre', 'objetivo', 'sistema operativo']
respuestas = ['Leonardo', 'aprender Python y Plone', 'Linux']

for pregunta, respuesta in zip(preguntas, respuestas):
    print('¿Cual es tu {0}?, la respuesta es: {1}.'.format(
         pregunta, respuesta))

#___________________________
print(  )
mensaje = "Hola, como estas tu?"
mensaje.split() # retorna una lista

for palabra in mensaje.split():
    print(palabra)


