from sikuli import *

def openChrome():
    click(Pattern("1377039261983.png").similar(0.90).targetOffset(2,3))
    type( "www.nzgameshop.com" + Key.ENTER )
    wait( "1378794454522.png", 60 )