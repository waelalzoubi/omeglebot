import pyautogui
from time import sleep
from tkinter import Button, Entry, Tk, StringVar

with open("info.txt") as f:
    info = f.read()

def main():
    global amount
    sleep(4)
    pyautogui.press("esc")
    for _ in range(int(amount.get())):
        sleep(0.3)
        # type info
        pyautogui.typewrite(info)
        sleep(0.3)
        # enter
        pyautogui.press("enter")
        sleep(0.3)
        # esc x 3
        x = pyautogui.screenshot().getpixel(pyautogui.position())
        if x[2] > 200 and x[0] < 200:
            x = pyautogui.position()
            pyautogui.click(x)
        else:
            for _ in range(3):
                pyautogui.press("esc")
    for _ in range(2):
        pyautogui.press("esc")

root = Tk()
amount = StringVar()
Entry(root, text=amount).pack()
Button(root, text="start", command=main).pack()
root.mainloop()
