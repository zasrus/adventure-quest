
class ascii_art(object):
  def __init__(self) -> None:
     pass
    
  def art_list(choice_type='chest', option='chest2'):
    '''
    choice_type: chest, maps
    option: chest1, chest2, map1
    '''
    chest = {

    'chest1':'''
          __________
          /\____;;___'\\
          | /         /
          `. ())oo() .
          |\(%()*^^()^'\\
          %| |-%-------|
          % \ | %  ))   |
          %  \|%________|
          ''',
    'chest2':""" 
                 ____...------------...____
             _.-"` /o/__ ____ __ __  __ \o\_`"-._
           .'     / /                    \ \     '.
           |=====/o/======================\o\=====|
           |____/_/________..____..________\_\____|
           /   _/ \_     <_o#\__/#o_>     _/ \_  \\
           \ ______________\####/________________ /
            |===\!/========================\!/===|
            |   |=|          .---.         |=|   |
            |===|o|=========/     \========|o|===|
            |   | |         \() ()/        | |   |
            |===|o|======{'-.) A (.-'}=====|o|===|
            | __/ \__     '-.\---/.-'    __/ \__ |
            |============= .'.'^'.'.=============|
            |  _\o/   __  {.' __  '.} _   _\o/  _|
            |""""-""""""""""""""""""""""""""-""""|
            |____________________________________|
            """,
    'chest3':''' 
        *******************************************************************************
                |                   |                  |                     |
        _________|________________.=""_;=.______________|_____________________|_______
        |                   |  ,-"_,=""     `"=.|                  |
        |___________________|__"=._o`"-._        `"=.______________|___________________
                |                `"=._o`"=._      _`"=._                     |
        _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
        |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
        |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
        _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
        |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
        |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
        ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
        /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
        ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
        /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
        ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
        /______/______/______/______/______/______/______/______/______/______/_____ /
        *******************************************************************************
        '''
          }

    maps={
    'map1':'''
____________________________________________________________________
/ \-----     ---------  -----------     -------------- ------    -- \\
\_/_________________________________________________________________/
|~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
|  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
| | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
|  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
|~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
|  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' |  ~|
|~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~ ~~|
|    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
| ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
|  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
|~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
| ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
|  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
| ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
|~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
| ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
|~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
| ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~  ~~~|
|~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
|____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
/ \----- ----- ------------  ------- ----- -------  --------  -------\\
\_/__________________________________________________________________/
'''
    }


    if choice_type == 'chest':
        choice_type = chest
    elif choice_type == 'maps':
       choice_type=maps

    print(choice_type[option])

    #print(chest['chest1'])