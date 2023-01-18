vocals = ("a", "e", "i", "o", "u")

string = "hola"


def vocaleliminar(string, vocals):
    output = string.replace(str(vocals), "")
    return output;


print(vocaleliminar(string, vocals))
