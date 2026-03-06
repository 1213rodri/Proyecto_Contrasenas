import re
import time
import subprocess
import sys
import tty
import termios
from rich.console import Console
from rich.live import Live
from rich.text import Text

console = Console()

def verificar_longitud(password):
    conta = 0
    if len(password) >= 12:
        conta += 20
    return conta


def verificar_mayusculas(password):
    conta = 0
    if any(c.isupper() for c in password):
        conta += 15
    return conta


def verificar_minusculas(password):
    conta = 0
    if any(c.islower() for c in password):
        conta += 15
    return conta


def verificar_numeros(password):
    conta = 0
    if any(c.isdigit() for c in password):
        conta += 15
    return conta


def verificar_simbolos(password):
    patron = r"[\W_]"
    conta = 0
    if any(re.search(patron, c) for c in password):
        conta += 15
    return conta


def verificar_patrones(password):
    patrones_comunes = [
        "0123", "1234", "2345", "3456", "4567", "5678", "6789", "7890",
        "9876", "8765", "7654", "6543", "5432", "4321", "3210",
        "012345", "123456", "234567", "345678", "456789", "567890",
        "0123456789", "9876543210",
        "0000", "1111", "2222", "3333", "4444", "5555",
        "6666", "7777", "8888", "9999",
        "00000", "11111", "22222", "33333", "44444", "55555",
        "66666", "77777", "88888", "99999",
        "abcd", "bcde", "cdef", "defg", "efgh", "fghi", "ghij",
        "hijk", "ijkl", "jklm", "klmn", "lmno", "mnop", "nopq",
        "opqr", "pqrs", "qrst", "rstu", "stuv", "tuvw", "uvwx",
        "vwxy", "wxyz",
        "abcde", "abcdef", "abcdefg",
        "zyxw", "yxwv", "xwvu", "wvut", "vuts", "utsr",
        "zyxwv", "zyxwvu",
        "aaaa", "bbbb", "cccc", "dddd", "eeee", "ffff",
        "gggg", "hhhh", "iiii", "jjjj", "kkkk", "llll",
        "mmmm", "nnnn", "oooo", "pppp", "qqqq", "rrrr",
        "ssss", "tttt", "uuuu", "vvvv", "wwww", "xxxx",
        "yyyy", "zzzz",
        "qwer", "wert", "erty", "rtyu", "tyui", "yuio", "uiop",
        "asdf", "sdfg", "dfgh", "fghj", "ghjk", "hjkl",
        "zxcv", "xcvb", "cvbn", "vbnm",
        "qwerty", "qwertyu", "qwertyui", "qwertyuiop",
        "asdfgh", "asdfghj", "asdfghjk", "asdfghjkl",
        "zxcvbn", "zxcvbnm",
        "qaz", "wsx", "edc", "rfv", "tgb", "yhn", "ujm",
        "qazwsx", "qazwsxedc",
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
        "123456", "1234567", "12345678", "123456789", "1234567890",
        "000000", "111111", "222222", "333333", "444444",
        "555555", "666666", "777777", "888888", "999999",
        "112233", "123123", "321321", "456456", "789789",
        "159753", "147258", "258369", "369258",
        "abc123", "abc1234", "password1", "password123",
        "admin123", "user123", "root123", "pass123",
        "qwerty123", "asdf123", "iloveyou1",
        "welcome1", "hello123", "test123",
        "2000", "2001", "2002", "2003", "2004", "2005",
        "2006", "2007", "2008", "2009", "2010", "2011",
        "2012", "2013", "2014", "2015", "2016", "2017",
        "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025",
        "0101", "0102", "0103", "1201", "1231",
        "!!!!", "????", "....", "----", "____", "////",
        "!!!!!", "?????", ".....", "-----",
        "aabbcc", "112233", "aaa111", "abc", "xyz",
        "pass", "clave", "secret", "secreto",
    ]

    conta = 0
    if any(patron in password.lower() for patron in patrones_comunes):
        return conta
    conta += 20
    return conta


def calcular_puntaje(password):
    puntaje  = verificar_longitud(password)
    puntaje += verificar_mayusculas(password)
    puntaje += verificar_minusculas(password)
    puntaje += verificar_numeros(password)
    puntaje += verificar_simbolos(password)
    puntaje += verificar_patrones(password)
    return puntaje

def construir_barra(password, puntaje):
    if puntaje <= 20:
        color = "red"
        nivel = "Muy débil"
    elif puntaje <= 40:
        color = "orange3"
        nivel = "Débil"
    elif puntaje <= 60:
        color = "yellow"
        nivel = "Media"
    elif puntaje <= 80:
        color = "green"
        nivel = "Fuerte"
    else:
        color = "bright_green"
        nivel = "Muy fuerte"

    asteriscos     = "*" * len(password)
    bloques_llenos = int(puntaje / 5)
    bloques_vacios = 20 - bloques_llenos

    texto = Text()
    texto.append(f"Contraseña: {asteriscos}\n")
    texto.append("Fortaleza:  ")
    texto.append("█" * bloques_llenos, style=color)
    texto.append("░" * bloques_vacios, style="grey50")
    texto.append(f"  {puntaje}/100 — {nivel}", style=color)

    return texto


def input_password_live():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    password = ""

    try:
        tty.setraw(fd)
        with Live(console=console, refresh_per_second=20) as live:
            live.update(construir_barra(password, 0))

            while True:
                ch = sys.stdin.read(1)

                if ch in ("\r", "\n"):
                    print()
                    break
                elif ch in ("\x7f", "\x08"):
                    if password:
                        password = password[:-1]
                elif ch == "\x03":
                    raise KeyboardInterrupt
                else:
                    password += ch

                puntaje = calcular_puntaje(password)
                live.update(construir_barra(password, puntaje))

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return password

def input_password_oculta():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    password = ""

    sys.stdout.write("Contraseña: ")
    sys.stdout.flush()

    try:
        tty.setraw(fd)

        while True:
            ch = sys.stdin.read(1)

            if ch in ("\r", "\n"):
                print()
                break
            elif ch in ("\x7f", "\x08"):
                if password:
                    password = password[:-1]
                    sys.stdout.write("\b \b")
                    sys.stdout.flush()
            elif ch == "\x03":
                raise KeyboardInterrupt
            else:
                password += ch
                sys.stdout.write("*")
                sys.stdout.flush()

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return password

def main():
    subprocess.run("clear", shell=True)
    console.print(" Bienvenido al Registro\n", style="bold cyan")

    while True:
        user = input("Ingrese su usuario: ")

        if len(user) == 0:
            console.print("Error: El usuario no puede estar vacío.\n", style="red")
            continue
        if " " in user:
            console.print("Error: El usuario no puede contener espacios.\n", style="red")
            continue

        password = input_password_live()
        puntaje  = calcular_puntaje(password)

        if user == password:
            console.print("Error: El usuario debe ser diferente a la contraseña.\n", style="red")
            continue

        if user.lower() in password.lower():
            console.print("Error: La contraseña no puede contener el nombre de usuario.\n", style="red")
            continue

        if puntaje >= 61:
            console.print("\nRegistro exitoso.\n", style="bold green")
            break
        else:
            console.print("Intente con una contraseña más segura (necesita ser Fuerte o Muy fuerte).\n", style="yellow")

    time.sleep(3)
    subprocess.run("clear", shell=True)

    console.print(" Inicio de Sesión\n", style="bold cyan")
    intentos     = 0
    max_intentos = 3

    while intentos < max_intentos:
        user2     = input("Ingrese su usuario: ")
        password2 = input_password_oculta()

        if user2 == user and password2 == password:
            console.print("\nSesión iniciada exitosamente.", style="bold green")
            break
        elif user2 != user and password2 == password:
            intentos += 1
            console.print(f"El usuario no coincide. Intento {intentos}/{max_intentos}.\n", style="red")
        elif user2 == user and password2 != password:
            intentos += 1
            console.print(f"La contraseña no coincide. Intento {intentos}/{max_intentos}.\n", style="red")
        else:
            intentos += 1
            console.print(f"Usuario y contraseña incorrectos. Intento {intentos}/{max_intentos}.\n", style="red")

    if intentos == max_intentos:
        console.print("Demasiados intentos fallidos. Acceso bloqueado.", style="bold red")

if __name__ == "__main__":
    main()
