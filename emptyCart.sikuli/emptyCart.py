from sikuli import *
import os
import shutil

def emptyCart( dir ):    
    screenshotsDir = dir
    wait( 2 )
    img = capture(SCREEN)
    shutil.move(img, os.path.join(screenshotsDir, "emptyCartDetection-Start.png"))
    click(find( Pattern("1378032858784.png").similar(0.80) ) )
    wait( "1378032917376.png", 60 )
    img = capture(SCREEN)
    if exists( "1378032917376.png"):
        shutil.move(img, os.path.join(screenshotsDir, "emptyCartDetection-Success.png"))
    else:
        shutil.move(img, os.path.join(screenshotsDir, "emptyCartDetection-Success.png"))