from sikuli import *

click(Pattern("1377037977721.png").similar(0.61))
wait( 5 )
addressBar = find(Pattern("1377038132799.png").similar(0.91))
click( addressBar.left() )
type( "www.nzgameshop.com" + Key.ENTER )
wait( "1378856465118.png", 30 )