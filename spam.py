import pyautogui
import keyboard
from time import sleep

def spam(q, t, o):
    count = 0
    if o==True:
        while count < q:
            pyautogui.write("block")
            pyautogui.press("enter")
            sleep(t)
            if teste.is_pressed("alt+q"):
                break
            count += 1
            
    elif o==False:
        while count < q:
            pyautogui.write("block")
            pyautogui.press("enter")
            if keyboard.is_pressed("alt+q"):
                break
            count += 1

def main():
    quantidade = int(input("qts msgs --> "))
    tempo = float(input("tempo --> "))
    if tempo==0:
        argv = False
    sleep(3)
    spam(quantidade, tempo, argv)

if __name__== '__main__':
    main()
