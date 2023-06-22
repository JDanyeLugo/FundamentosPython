#Funciones en python
# def name-function(params):
# Codigo
# Return

#Funcion sin Parametros y sin retorno
def saludos():
    print("hola a todos")
saludos()

#Funciones con un parametro
def get_age_in_future(age):
    print(f" en tres años tendras { age + 3 } años")

get_age_in_future(39)
def suma(num1, num2):
    print(f"{num1}+{num2}={num1 + num2}")
suma(12, 35)

#funciones con parametros opcionales
def get_heroes(h1 = "Iroman", h2 = "Spiderman"):
    print([h1, h2])

get_heroes()
get_heroes("Batman")
get_heroes("Batman", "Superman")
get_heroes(h2="Batman", h1="Superman")

#Funciones con retorno
def title(texto):
    return texto.title()
text_changed = title ("hOlA MuNdO")
print(text_changed)