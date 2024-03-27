a = input("What would you like to drink? (tea, coffee, wine, nothing) ")
# it has to be in options to choose from


if a == "coffee":
    print(''' Here is your coffee, enjoy.
                        )     (
                 ___...(-------)-....___
             .-""       )    (          ""-.
       .-'``'|-._             )         _.-|
      /  .--.|   `""---...........---""`   |
     /  /    |                             |
     |  |    |                             |
      \  \   |                             |
       `\ `\ |                             |
         `\ `|                             |
         _/ /\                             /
        (__/  \                           /
     _..---""` \                         /`""---.._
  .-'           \                       /          '-.
 :               `-.__             __.-'              :
 :                  ) ""---...---"" (                 :
  '._               `"--...___...--"`              _.'
    \""--..__                              __..--""/
     '._     """----.....______.....----"""     _.'
        `""--..,,_____            _____,,..--""`
                      `"""----"""`
''')
    b = input("Would you like anything else? (croissant, cake, pastry) ")
    if b == "croissant":
        print('''
   ____                                    ?~~bL
  z@~ b                                    |  `U,
 ]@[  |                                   ]'  z@'
 d@~' `|, .__     _----L___----, __, .  _t'   `@j
`@L_,   "-~ `--"~-a,           `C.  ~""O_    ._`@
 q@~'   ]P       ]@[            `Y=,   `H+z_  `a@
 `@L  _z@        d@               Ya     `-@b,_a'
  `-@d@a'       )@[               `VL      `a@@'
    aa~'   ],  .a@'                qqL  ), ./~
    @@_  _z~  _d@[                 .V@  .L_d'
     "~@@@'  ]@@@'        __      )@n@bza@-"
       `-@zzz@@@L        )@@z     ]@@=%-"
         "~~@@@@@bz_    _a@@@@z___a@K
             "~-@@@@@@@@@@@@@@@@@@~"   
                `~~~-@~~-@@~~~~~'
        ''')
    if b == "cake" or b == "pastry":
        print('''  $$  $$  $$
    __||__||__||__
   | * * * * * * *|
   |* * * * * * * |
   | * * * * * * *|
   |______________|
          ''')

if a == "tea":
    print('''
         (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \
\_____________________/
    )
          ''')
    b = input("Would you like anything else? (croissant, cake, pastry) ")
    if b == "croissant":
        print('''
   ____                                    ?~~bL
  z@~ b                                    |  `U,
 ]@[  |                                   ]'  z@'
 d@~' `|, .__     _----L___----, __, .  _t'   `@j
`@L_,   "-~ `--"~-a,           `C.  ~""O_    ._`@
 q@~'   ]P       ]@[            `Y=,   `H+z_  `a@
 `@L  _z@        d@               Ya     `-@b,_a'
  `-@d@a'       )@[               `VL      `a@@'
    aa~'   ],  .a@'                qqL  ), ./~
    @@_  _z~  _d@[                 .V@  .L_d'
     "~@@@'  ]@@@'        __      )@n@bza@-"
       `-@zzz@@@L        )@@z     ]@@=%-"
         "~~@@@@@bz_    _a@@@@z___a@K
             "~-@@@@@@@@@@@@@@@@@@~"   
                `~~~-@~~-@@~~~~~'
        ''')
        if b == "cake" or b == "pastry":
            print('''  $$  $$  $$
    __||__||__||__
   | * * * * * * *|
   |* * * * * * * |
   | * * * * * * *|
   |______________|
          ''')


if a == "wine":
    print('''
     __
 __ {_/ 
 \_}\\ _
    _\(_)_
   (_)_)(_)_
  (_)(_)_)(_)
   (_)(_))_)  ____
    (_(_(_)  |    |  ____
     (_)_)   |~~~~| |    |
      (_)    '-..-' |~~~~|
               ||   '-..-'
              _||_    ||
             `""""`  _||_
                    `""""`''')

if a == "nothing":
    c = input("shall we go to next resturant?")
    if c == "yes":
        print("surely")
        d = input("What are you feeling like having?(momo,you decide)")
        if d == "momo":
            e = input("I know a great dumpling place. Up for a suprise?")
            if e == "yes":
                f = input(
                    "we sure did have fun. Would you like to continue our food date?(ok,no)")
                if f == "ok":
                    print("LETS GO TO MY PLACE. I am a great cook. Up for a suprise?")
                if f == "No":
                    g = input("let me make it up to you?(ok,no)")
                    if g == "ok":
                        print(
                            "LETS GO TO MY PLACE. I am a great cook. Up for a suprise?")
                    if g == "No":
                        f = input("preety please?(ok,no)")
            if e == "NO":
                f = input("Have some fate in me?(i will try,no)")
                if f == "i will try":
                    g = input(
                        "yaay, did you have fun?can we continue this date?")
                    if g == "ok":
                        print(
                            "LETS GO TO MY PLACE. I am a great cook. Up for a suprise?")
                    if f == "No":
                        g = input("let me make it up to you?(ok,no)")
                    if g == "ok":
                        print(
                            "LETS GO TO MY PLACE. I am a great cook. Up for a suprise?")
                    if g == "No":
                        h = input("preety please?(ok)")
                        if h == "ok":
                            print(
                                "LETS GO TO MY PLACE. I am a great cook. Up for a suprise?")
        if d == "you decide":
            print("LETS GO TO MY PLACE. I am a great cook. Up for a suprise?")
