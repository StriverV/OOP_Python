import pyautogui as pg
import time as t

n = int(input())

t.sleep(10)

for i in range (n+1):                    
    for j in range (i):                               
        pg.write("# ",interval = 0.25)                                    
    pg.press('enter')   

