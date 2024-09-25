text1= "Punto numero 1"
print(text1)
name1 = "Valeria"
name2 = "Harrison"
age = 19
comidafav1 = "Lagsaña"
comidafav2 = "Las pastas"
presentation = (f"Hola, nosotros somos  {name1} y {name2},tenemos {age} años, la comida favorita de {name1} es la  {comidafav1} "
                f"y la de {name2} es {comidafav2}.")
print(presentation)

text2= "Punto numero 2"
print(text2)
nombreCompleto = input("Por favor, ingresa tu nombre completo: ")
letter_count = len(nombreCompleto.replace(" ", ""))
print(f"Hola, {nombreCompleto}! el nombre tiene {letter_count} letras, ignorando los espacios.")

text3= "Punto numero 3"
print(text3)
increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078
info = f"Las ventas de la empresa láctea aumentaron un {increaseSalesPercent:.2f}% y los ingresos crecieron un {revenueGrowthPercent:.2f}%."
print(info)

text4= "Punto numero 4"
print(text4)
mensajeSecreto = "aS!Ir waQm  VL!eDafrcnXi n=gS .P,yytahgoln.!"
decoded_message = mensajeSecreto[3::2]
print(decoded_message)

text5= "Punto numero 5"
print(text5)
text = 'Estamos haciendo una actividad practica que no enseña a manejar Python'
word_count = len(text.split())
print(f"Número de palabras en la frase: {word_count}")

text6= "Punto numero 6"
print(text6)
palabra = "Valeria y Harrison"
modified_word =palabra.replace("a", "e")
print(modified_word)

text7= "Punto numero 7"
print(text7)
sentence = "Un ejercicio para invertir el orden de la frae"
reversed_sentence = ' '.join(sentence.split()[::-1])
print(reversed_sentence)


