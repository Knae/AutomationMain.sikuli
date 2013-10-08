# works on all platforms
import os
import shutil
# get the directory containing your running .sikuli
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)

#import openChrome
#import emptyCart
#import removeItem

#import modifyQuantity

#import changeQuantity

#import closeChrome

#import openIE

scrDir = "C:\Users\Public\Pictures\SikluiScreenshots"

def addItem():
        click(Pattern("1378249278462.png").similar(0.80))
        wait( 5 )
        wait(Pattern("1378249376462.png").similar(0.90),60 ) 

def  openBrowser(browserType):

    appObj = None
    
    
    if( browserType == "IE"):
        appObj = App.open( "C:\Program Files (x86)\Internet Explorer\iexplore.exe")
    elif( browserType == "FireFox"):
        pass
    elif( browserType == "Chrome"):
        appObj = App.open( "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")    
    else:
        raise "openBrowser: unknown browser type=" + browserType

    if appObj == None:
        raise "openBrowser: browserType=" + browserType + " appObj == None" 
    
    return appObj

def emptyCart( dir ):    
    screenshotsDir = dir
    wait( 2 )
    img = capture(SCREEN)
    shutil.move(img, os.path.join(screenshotsDir, "emptyCartDetection-Start.png"))
    click( find ( "1376433305224.png" ) )
    wait( 5 )
    img = capture(SCREEN)
    if exists( "1378032917376.png"):
        shutil.move(img, os.path.join(screenshotsDir, "emptyCartDetection-Success.png"))
    else:
        shutil.move(img, os.path.join(screenshotsDir, "emptyCartDetection-Success.png"))

def removeItem( dir, app):
    screenshotsDir = dir
    addItem()
    addItem()
    addItem()
    addItem()
    click( find("1381229296133.png") )
    wait("1379457252245.png", 60)
    img = capture(SCREEN)
    shutil.move(img, os.path.join(screenshotsDir, "removeItem-Start.png"))
    prev = Region(701,415,442,59).text()
    remove = Region(701,415,442,59).right( 600 ).find(Pattern("1381231590519.png").similar(0.80)) 
    click( remove )   
    wait( 10 )
    current = Region(701,415,442,59).text()
    if prev!=current:
        img = capture(SCREEN)
        shutil.move(img, os.path.join(screenshotsDir, "removeItem-Success.png"))
    else:
        img = capture(SCREEN)
        shutil.move(img, os.path.join(screenshotsDir, "removeItem-Fail.png"))

def modifyQuantity( dir, app):
    img = capture(SCREEN)
    shutil.move(img, os.path.join(dir, "ModifyQuantityToZero-Start.png")) 
    quantity = find( Pattern("1381267338536.png").targetOffset(-30,-3) )
    click( quantity )
    type( Key.DELETE )
    wait(2)
    type( Key.BACKSPACE )
    wait(2)
    type( "4" )
    
    #r = Region(1288,406,104,60)
    prev = quantity.right( 500 ).text()
    
    quantity.click( "1377740779853.png" )
    wait( "1379457252245.png" )
    wait(5)
    current = quantity.right( 500 ).text()
    popup( prev +"\n" + current )
    img = capture(SCREEN)
    if prev!=current:
            #popup("Price changed")
            shutil.move(img, os.path.join(dir, "ModifyQuantityToZero-Success.png")) 
    else:
            #popup("Price not changed")
            shutil.move(img, os.path.join(dir, "ModifyQuantityToZero-Failed.png")) 

def changeQuantity0( dir, app ):
    screenshotsDir = dir
    img = capture(SCREEN)
    shutil.move(img, os.path.join(screenshotsDir, "changeQuantityToZero-Start.png"))
    r = Region(643,401,515,254) 
    prev = r.text()
    #popup(prev )
    quantity = r.right( 500 ).find(Pattern("1381267338536.png").targetOffset(-31,-1))
    
    click(quantity)
    type( Key.DELETE )
    wait(2)
    type( Key.BACKSPACE )
    wait(2)
    type( "0" )
    quantity.click( Pattern("1377740779853.png").similar(0.91) )
    wait(5)
    current = r.text()
    popup(current + "\n" + prev )
    if prev!=current:
        img = capture(SCREEN)
        shutil.move(img, os.path.join(screenshotsDir, "changeQuantityToZero-Success.png"))
    else:
        img = capture(SCREEN)
        shutil.move(img, os.path.join(screenshotsDir, "changeQuantityToZero-Fail.png"))


def  closeBrowser( app):
        closeButton = find( "1379601042082.png" )
        closeButton.highlight( 2 )
        click( closeButton )  

    
def runTests( app):
    emptyCart( scrDir )
    removeItem( scrDir, app )
    modifyQuantity( scrDir, app )
    changeQuantity0( scrDir, app )

    
def testWithBrowser( browser):
    try:
       
        appS = openBrowser( browser)
        wait( 5 )
        type( 'd', KEY_ALT )
        type( "www.nzgameshop.com" + Key.ENTER )
        wait( Pattern("1378794454522.png").similar(0.72) , 60 )
        #try:
        runTests( appS )
        #finally:
        closeBrowser( appS )
    except Exception,e:
        print "testWithBrowser: caught exception", e

def main():
    
    #testWithBrowser( "IE")    
    #testWithBrowser( "FireFox") 
    testWithBrowser( "Chrome")

main()



#reload(emptyCart)
#reload(removeItem)
#reload(modifyQuantity)
#reload(changeQuantity)
#import closeIE