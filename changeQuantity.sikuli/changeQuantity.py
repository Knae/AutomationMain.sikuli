from sikuli import *
import os
import shutil

def changeQuantity0( dir, app ):
    screenshotsDir = dir
    img = capture(SCREEN)
    shutil.move(img, os.path.join(screenshotsDir, "changeQuantityToZero-Start.png"))
    r = Region(665,412,493,201) 
    prev = r.text()
    popup(prev )
    quantity = find(Pattern("1377740735076.png").targetOffset(-30,1))
    click(quantity)
    type( Key.DELETE )
    wait(2)
    type( Key.BACKSPACE )
    wait(2)
    type( "0" )
    quantity.click(Pattern("1377740779853.png").similar(0.90))
    wait(5)
    current = r.text()
    popup(current )
    if prev!=current:
        img = capture(SCREEN)
        shutil.move(img, os.path.join(screenshotsDir, "changeQuantityToZero-Success.png"))
    else:
        img = capture(SCREEN)
        shutil.move(img, os.path.join(screenshotsDir, "changeQuantityToZero-Fail.png"))
