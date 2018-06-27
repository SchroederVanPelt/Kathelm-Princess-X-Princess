label CombatZero:
label testing:
screen simple_stats_screen:
    frame:
        xalign 0.99 yalign 0.05
        vbox:
            text "Guard Nathan" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value gn_hp
                    range gn_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[gn_hp] / [gn_max_hp]" size 16


    frame:
        xalign 0.01 yalign 0.05
        vbox:
            text "[PN]" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value p1_hp
                    range p1_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[p1_hp] / [p1_max_hp]" size 16

    text "Guard Nathan vs. [PN]" xalign 0.5 yalign 0.05 size 30



label CombatOne:

    $ p1_max_hp = 30
    $ gn_max_hp = 30
    $ p1_hp = p1_max_hp
    $ gn_hp = gn_max_hp

    show screen simple_stats_screen
    show GNathan_happy
    while (p1_hp > 0) and (gn_hp > 0):

        menu:
            "Attack!":
                $ gn_hp -= renpy.random.randint(1, 6)
                p1 "K-y-aaa!!!"
            "Defend!":
                $ gn_damage == renpy.random.randint(1,2)
                p1 "Gonna have to try hardered to hit me"
                gn "You're not so bad yourself"

        show GNathan_vhappy
        gn "How about this!"
        "Guard Nathan attacks with a swing of his sword"

        $ gn_damage = renpy.random.randint(1, 6)
        $ p1_hp -= gn_damage

        p1 "You hit hard!"
        gn "I'm good at what I do."

        show GNathan_panic
        menu:
            "Attack!":
                $ gn_hp -= renpy.random.randint(1, 6)
                p1 "K-y-aaa!!!"
            "Defend!":
                $ gn_damage == renpy.random.randint(1,2)
                p1 "Gonna have to try hardered to hit me"
                gn "You're defense is as good as your offense"
            "Parry":
                $ gn_damage == renpy.random.randint(1,3)
                gn "Fancy footwork you got there"
                p1 "Years of practice"

    if gn_hp <= 0:
        p1 "This was fun!"
        $ rula_points +=3
    if p1_hp <= 0:
        p1 "This was fun! You're a really good fighter."
        $ rula_points +=1

hide screen simple_stats_screen


return

label CombatTwo:
