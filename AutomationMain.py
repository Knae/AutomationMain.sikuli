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


def  openBrowser(browserType):

    appObj = None
    
    
    if( browserType == "IE"):
        pass
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
    click(find( Pattern("1378032858784.png").similar(0.80) ) )
    wait( "1378032917376.png", 60 )
    img = capture(SCREEN)
    if exists( "1378032917376.png"):
        shutil.move(img, os.path.join(screenshotsDir, "emptyCartDetection-Success.png"))
    else:
        shutil.move(img, os.path.join(screenshotsDir, "emptyCartDetection-Success.png"))

def  closeBrowser( browserType, app):
    with app.window( ):
        closeButton = find( "1379601042082.png" )
        closeButton.highlight( 2 )
        click( closeButton )  

    
def runTests( app):
    emptyCart( scrDir )
    #removeItem( scrDir, app )

    
def testWithBrowser( browser):
    try:
       
        appS = openBrowser( browser)
        wait( 5 )
        click( Pattern("1379601986867.png").similar(0.90).targetOffset(-208,-2) )
        type( "www.nzgameshop.com" + Key.ENTER )
        wait( Pattern("1378794454522.png").similar(0.80) , 60 )
        #try:
        runTests( appS )
        #finally:
        closeBrowser( "Chrome" , appS )
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