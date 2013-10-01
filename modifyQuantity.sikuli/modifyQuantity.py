from sikuli import *
def modifyQuantity( dir, app):
    #cartAdd = find(Pattern("1376433625109.png").similar(0.91))
    #click( cartAdd )
    #wait("1376433659558.png", 60)
    #cartView = find("1376433305224.png")
    #click( cartView )
    #wait( "1376434734521.png", 60 )
    quantity = find( "1376434008176.png" )
    quantity.click( "1376434072666.png" )
    type( Key.DELETE )
    wait(2)
    type( Key.BACKSPACE )
    wait(2)
    type( "4" )
    
    r = Region(1354,481,33,21)
    prev = r.text()
    
    quantity.click( Pattern("1376436080789.png").similar(0.88) )
    wait( "1376434734521.png", 60 )
    wait(5)
    current = r.text()
    
    if prev!=current:
            popup("Price changed")
    else:
            popup("Price not changed")
