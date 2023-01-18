vocals = ("a", "e", "i", "o", "u")

string = "hola"


def vocaleliminar(string, vocals):
    output = string.replace(str(vocals), "") #no se como hacer que se canvie porque restando las vocales no va xd
    return output;


print(vocaleliminar(string, vocals))


