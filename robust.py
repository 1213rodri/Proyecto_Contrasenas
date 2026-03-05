""" 

El | import re | esto nos servira para poder validar si es que hay un simbolo en la contrasena
a diferencia de otros metodos es el mas completo

El | import subprocess | nos ayuda a poder limpiar la temrninal despues de que el usuario haya completado el registro

El | import time | nos ayuda a dar 5 segundos de espera entre el cambio del registro al inicio de sesion


Para consultar mas del proyecto seguir el siguiente link en caso de actualizaciones: https://github.com/1213rodri/Proyecto_Contrasenas
"""

import re 
import time
import subprocess
import getpass

def verificar_longitud(password):
    conta=0
    if len(password)>=12:
        conta += 20

    return conta

"""
En esta seccion de verificar_longitud, utilizamos la funcion de [len] para poder saber la cantidad de caracteres que tenia la contrasena
en dado caso de que la contrasena fuera menor de 12,no se sumarian los 20 puntos
"""


def verificar_mayusculas(password):
    conta = 0
    if any(c.isupper() for c in password):
        conta += 15

    return conta

"""
En esta seccion de verificar_mayusculas, se utilizaron los metodos [any] y [isupper], que a continuacion explico el por que de cada uno
[any]= Es una herramienta de Python que sirve para verificar condiciones en un conjunto de datos (como una lista o una cadena)
[isupper]= Sirve para verificar si un carácter o una cadena de texto están completamente en mayúsculas,
(en este caso para validar si al menos 1 es mayuscula)
[any] se utilizo de la misma forma para los demas requisitos.
"""


def verificar_minusculas(password):
    conta = 0
    if any(c.islower() for c in password):
        conta += 15

    return conta

"""
En esta seccion se repitio el procedimiento como las mayusculas, a diferencia de que se utilizo el metodo [islower]
[islower]= Sirve para verificar si un carácter o una cadena de texto están completamente en minúsculas.

"""


def verificar_numeros(password):
    conta = 0
    if any(c.isdigit() for c in password):
        conta += 15

    return conta

"""
Exactamente lo mismo que los anteriores, pero para números. 
El método isdigit() devuelve True si el carácter es un dígito numérico ('0' al '9') y False si es una letra, un símbolo o un espacio [2].

"""


def verificar_simbolos(password):
    patron = r"[\W_]"
    conta=0
    if any(re.match(patron,c) for c in password):
        conta += 15
    
    return conta

"""
En esta seccion de verificar_simbolos, se utilizo el modulo [re] (expresiones regulares) junto con [any].
El patron r"[\W_]" detecta cualquier caracter que NO sea letra o numero, es decir simbolos como !@#$%^&*
[re.match]= Intenta encontrar una coincidencia del patron al inicio del string, en este caso cada caracter individual.
Se itera sobre cada caracter [c] de la contrasena, y si al menos uno coincide con el patron, se suman 15 puntos.
"""


def verificar_patrones(password):
    patrones_comunes = [
    # Secuencias numéricas
    "0123", "1234", "2345", "3456", "4567", "5678", "6789", "7890",
    "9876", "8765", "7654", "6543", "5432", "4321", "3210",
    "012345", "123456", "234567", "345678", "456789", "567890",
    "0123456789", "9876543210",

    # Repeticiones numéricas
    "0000", "1111", "2222", "3333", "4444", "5555",
    "6666", "7777", "8888", "9999",
    "00000", "11111", "22222", "33333", "44444", "55555",
    "66666", "77777", "88888", "99999",

    # Secuencias alfabéticas
    "abcd", "bcde", "cdef", "defg", "efgh", "fghi", "ghij",
    "hijk", "ijkl", "jklm", "klmn", "lmno", "mnop", "nopq",
    "opqr", "pqrs", "qrst", "rstu", "stuv", "tuvw", "uvwx",
    "vwxy", "wxyz",
    "abcde", "abcdef", "abcdefg",
    "zyxw", "yxwv", "xwvu", "wvut", "vuts", "utsr",
    "zyxwv", "zyxwvu",

    # Repeticiones alfabéticas
    "aaaa", "bbbb", "cccc", "dddd", "eeee", "ffff",
    "gggg", "hhhh", "iiii", "jjjj", "kkkk", "llll",
    "mmmm", "nnnn", "oooo", "pppp", "qqqq", "rrrr",
    "ssss", "tttt", "uuuu", "vvvv", "wwww", "xxxx",
    "yyyy", "zzzz",

    # Teclado QWERTY horizontal
    "qwer", "wert", "erty", "rtyu", "tyui", "yuio", "uiop",
    "asdf", "sdfg", "dfgh", "fghj", "ghjk", "hjkl",
    "zxcv", "xcvb", "cvbn", "vbnm",
    "qwerty", "qwertyu", "qwertyui", "qwertyuiop",
    "asdfgh", "asdfghj", "asdfghjk", "asdfghjkl",
    "zxcvbn", "zxcvbnm",

    # Teclado QWERTY vertical
    "qaz", "wsx", "edc", "rfv", "tgb", "yhn", "ujm",
    "qazwsx", "qazwsxedc",

    # Palabras comunes en contraseñas
    "password", "passwd", "pass", "contraseña",
    "admin", "administrator", "root", "user", "usuario",
    "login", "logon", "access", "acceso",
    "welcome", "bienvenido", "hola", "hello",
    "letmein", "letmein1", "opensesame",
    "monkey", "dragon", "master", "shadow",
    "sunshine", "princess", "football", "soccer",
    "baseball", "batman", "superman", "spiderman",
    "michael", "jessica", "jennifer", "thomas",
    "iloveyou", "loveyou", "te amo", "amor",

    # Contraseñas numéricas muy usadas
    "123456", "1234567", "12345678", "123456789", "1234567890",
    "000000", "111111", "222222", "333333", "444444",
    "555555", "666666", "777777", "888888", "999999",
    "112233", "123123", "321321", "456456", "789789",
    "159753", "147258", "258369", "369258",

    # Combinaciones comunes
    "abc123", "abc1234", "password1", "password123",
    "admin123", "user123", "root123", "pass123",
    "qwerty123", "asdf123", "iloveyou1",
    "welcome1", "hello123", "test123",

    # Fechas y años comunes
    "2000", "2001", "2002", "2003", "2004", "2005",
    "2006", "2007", "2008", "2009", "2010", "2011",
    "2012", "2013", "2014", "2015", "2016", "2017",
    "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025",
    "0101", "0102", "0103", "1201", "1231",

    # Símbolos repetidos
    "!!!!", "????", "....", "----", "____", "////",
    "!!!!!", "?????", ".....", "-----",

    # Otros patrones obvios
    "aabbcc", "112233", "aaa111", "abc", "xyz",
    "pass", "clave", "secret", "secreto",
    ]
    conta=0
    if any(patron in password for patron in patrones_comunes):
        return conta
    conta += 20
    return conta

"""
En esta seccion de verificar_patrones, se utilizo una lista llamada [patrones_comunes] que contiene
secuencias numericas, alfabeticas, palabras frecuentes y combinaciones tipicas que hacen debil una contrasena.
[any]= Recorre la lista y verifica si alguno de esos patrones esta contenido dentro de la contrasena con el operador [in].
Si se encuentra un patron, se devuelve 0 puntos. Si no se encuentra ninguno, se suman 20 puntos.

(

El diccionario en parte fue obtenido de fuentes de google o github:
SecLists (GitHub) — Github.com/danielmiessler/SecLists — colección enorme de wordlists usadas en pentesting, incluye contraseñas comunes reales filtradas de brechas de seguridad.
RockYou wordlist  — Rockyou.txt — es la lista de contraseñas más famosa en ciberseguridad, proviene de una brecha real de 2009 con millones de contraseñas reales.
OWASP — owasp.org — Tiene documentación sobre contraseñas débiles y patrones comunes en su proyecto de autenticación.
Have I Been Pwned — haveibeenpwned.com/Passwords — base de datos de contraseñas comprometidas en brechas reales, mantenida por Troy Hunt.

)

"""



def calcular_puntaje(password):
    puntaje  = verificar_longitud(password)
    puntaje += verificar_mayusculas(password)
    puntaje += verificar_minusculas(password)
    puntaje += verificar_numeros(password)
    puntaje += verificar_simbolos(password)
    puntaje += verificar_patrones(password)
    return puntaje 

"""

En esta seccion de calcular_puntaje, se llaman todas las funciones anteriores pasandoles la contrasena.
Cada funcion devuelve su puntaje parcial (0 o su valor maximo) y se van acumulando en la variable [puntaje].
Al final se retorna el puntaje total que puede ir de 0 a 100.

"""


def clasificar_nivel(puntaje):
    if puntaje>=0 and puntaje<=20:
        print("Su contrasena es muy debil")
    elif puntaje>=21 and puntaje<=40:
        print("Su contrasena es debil")
    elif puntaje>=41 and puntaje<=60:
        print("Su contrasena es media")
    elif puntaje>=61 and puntaje<=80:
        print("Su contrasena es fuerte")
    elif puntaje>=81 and puntaje<=100:
        print("Su contrasena es muy fuerte")


"""
En esta seccion de clasificar_nivel, se recibe el puntaje calculado y se clasifica en 5 niveles:
Muy debil (0-20), Debil (21-40), Media (41-60), Fuerte (61-80), Muy fuerte (81-100).
Se utilizan condicionales [if/elif] con [and] para verificar que el puntaje este dentro del rango correcto.
Se uso [and] en lugar de [or] porque ambas condiciones deben cumplirse al mismo tiempo para pertenecer al rango.
"""






def main():
    subprocess.run("clear", shell=True)
    print("Bienvenido al registro")

    user = input("Ingrece su usuario: ")
    while True:
        password = getpass.getpass(prompt='Contraseña: ', echo_char='*')
        puntaje = calcular_puntaje(password)
        clasificar_nivel(puntaje)
        if user==password:
            print("Error: su usuario debe de ser diferente a la contrasena")
        else:
            if puntaje >= 61:
               print("Registro exitoso")
               break
            else:
               print("Intente con una contrasena mas segura\n")

    time.sleep(5)        
    subprocess.run("clear", shell=True)
    print("Inicio de sesion")

    while True:
        user2=input("Ingrece su ususario:  ")
        password2 = getpass.getpass(prompt='Contraseña: ', echo_char='*')
        
        if user2 == user and password2==password:
            print("Inicio de sesion exitosamente")
            break
        elif user2 != user and password2==password:
            print("El usurio no coincide, intente nuevamente.")
        elif user2 == user and password2 != password:
            print("La contrasena no coincide, intente nuevamente.")
        else:
            print("Error en las credenciales")

"""
En esta seccion de main, se le da la bienvenida al usuario y se solicita su nombre de usuario.
Luego entra en un ciclo [while True] que seguira pidiendo la contrasena hasta que sea lo suficientemente segura.
En cada iteracion se calcula el puntaje, se clasifica el nivel y si el puntaje es >= 61 (fuerte o muy fuerte)
se muestra el mensaje de inicio de sesion exitoso y se rompe el ciclo con [break].
"""


if __name__ == "__main__":
    main()





"""

Este condicional verifica que el archivo se este ejecutando directamente y no siendo importado como modulo desde otro archivo.
Si se importara desde otro archivo, __name__ tendria el nombre del modulo y main() no se ejecutaria automaticamente.
Solo cuando se ejecuta directamente __name__ vale "__main__" y se llama a la funcion main() para iniciar el programa.

"""
