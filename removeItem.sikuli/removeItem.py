from sikuli import *
import os
import shutil

def modifyQuantity( dir, app):
    
    def addItem():
        click(Pattern("1378249278462.png").similar(0.80))
        wait( 5 )
        wait(Pattern("1378249376462.png").similar(0.90),60 )         
    
    screenshotsDir = dir
    additem()
    additem()
    additem()
    additem()
    click(Pattern("1378249570075.png").similar(0.80))
    wait("1379457252245.png", 60)
    img = capture(SCREEN)
    shutil.move(img, os.path.join(screenshotsDir, "removeItem-Start.png"))
    prev = app.Region(701,415,442,59).text()
    #prev = name.text()
    popup( prev )
    remove = app.Region(701,415,442,59).right( 300 ).find(Pattern("1378855370487.png").similar(0.80))
    click( remove )   
    wait( 10 )
    current = app.Region(701,415,442,59).text()
    #popup( current )
    if prev!=current:
        img = capture(SCREEN)
        shutil.move(img, os.path.join(screenshotsDir, "removeItem-Success.png"))
    else:
        img = capture(SCREEN)
        shutil.move(img, os.path.join(screenshotsDir, "removeItem-Fail.png"))
