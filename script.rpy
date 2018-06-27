define cg1 = {"he", "she", "they"}
define cgp = {"him", "her", "them"}
define cgp2 = {"his", "her", "their"}
define cgp3 = {"his", "hers", "theirs"}
define cgp4 = {"himself", "herself", "themselves"}
define cg2 = {"Sir", "Lady", "Master"}
define p1 = Character("[PN]")

default gender = False
default Girl = False
default Boy = False
default Teenager = False
default YoungAdult = False
default Adult = False

default PoliticalAdviser = False
default Officer = False
default Private = False
default Student = False

default Felis = False
default Catus = False
default Silvestris = False
define home = ["Felis", "Catus", "Silvestris"]

define day_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] ## 2,3,4,5,6,0,1
define time_of_day = ["Morning", "Afternoon", "Evening", "Night"] ## 3,0,1,2
default day = 1
default tod = 1

default dow = day_of_week[day]
default time_now = time_of_day[tod]

default result = 0
default dialogue = renpy.count_dialogue_blocks()

init python:
    import re
    def sentence_case(text):
        sentences = re.findall('[^.!?]+[.!?](?:\s|\Z)', text)
        sentences = [x[0].upper() + x[1:] for x in sentences]
        return "".join(sentences)
        config.say_menu_text_filter = sentence_case

    def percent(): ## code for how much of the game has been played
        global result
        global dialogue
        seen = renpy.count_seen_dialogue_blocks()
        result = seen * 100 / dialogue
    def max_points(*values): ## code for points based Point-Based Endings
        return [ i for i, v in enumerate(values) if v == max(values) ]
    def advance_time(_time = 1):
        global tod, time_now, time_of_day, day
        new_days = (tod + _time) // 4 # // returns floored divisions, in other ways how many times the divider goes into the value, ignoring remainders

        tod = (tod + _time) % 4
        time_now = time_of_day[tod]

        advance_day(new_days) # add new days

    def advance_day(_day = 1):
        global day, dow, day_of_week
        day += _day
        dow = day_of_week[day % 7]

# The game starts here.

label start:

    $ pansy_points = 1
    $ rula_points = 1
    $ sable_points = 3
    $ aurora_points = 0
    $ twins_points = 1
    $ alice_points = 1
    $ risby_points = 1

    show screen show_points()


na "Testing something out h"

scene white
show text "It has been a harsh time these last few years. As territories clashed over claims to the kingdom. But now that has all come to a close."with Pause (4)
hide text with dissolve
show text "This has been a long time coming. After years of fighting the Blood Rose Wars are over. An alliance has been reached between the Felis, Catus and Silvestris kingdoms." with Pause (5)
hide text with dissolve
show text "But now they must choose a new ruler.Be it by luck or by magic each of the previously waring territories all had a handful of royal ladies suited for ruling."  with Pause (5)
hide text with dissolve
show text "To solidify the coming alliance the a decree was passed between the three territories." with Pause(4)
hide text with dissolve
show text "Each of the three kindoms would send their choosen ones to the newly formed Kathelm City and an election would be held. Whoever won would be crowned Queen of Kathelm, ruler of the three kingdom." with Pause(4)
hide text with dissolve
show text "Welcome to the newly formed Kingdom of Kathelm" with Pause (3)
hide text with dissolve
with Pause (2)


show text "[dow] [time_now]" with Pause (3)
hide text with dissolve
$ result = 0
$ dialogue = renpy.count_dialogue_blocks()
$ seen = renpy.count_seen_dialogue_blocks()

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

scene citystreet_noon

show screen show_day()

label PreludePt1:

na "You arrive in the kingdom of Kathelm just before the last of the revelry has died down."
na "People have been out in the streets since the news of the alliance broke."
na "There are not so hush whispers everywhere of who each kingdom is going to send as their representatiive"
na "You arrive in Kathelm a handful of days before each kingdom is poised to make their announment."
na "As you are making your way though the city you are approched."

show Guard1 at left

g1 "Hey you there, who are you?"

"You look around confused. Are they talking to you?"

$ PN = renpy.input("What is your name?")
$ PN = PN.strip()
if PN == "":
    $ PN="Q"

menu:
    "Are you a girl or boy?"

    "Girl":
        $Girl = True
        if Girl:
            $ cg1 = "she"
            $ cgp = "her"
            $ cgp2 = "her"
            $ cgp3 = "hers"
            $ cgp4 = "herself"
    "Boy":
        $Boy = True
        if Boy:
            $ cg1 = "he"
            $ cgp = "him"
            $ cgp2 = "his"
            $ cgp3 = "his"
            $ cgp4 = "himself"
    "Both":
        $gender = True
        if gender:
            $ cg1 = renpy.input("What are your prefered pronouns?")
            $ cg1 = cg1.strip()
            if cg1 == "":
                $ cg1 = "she"
                $ cgp = "her"
                $ cgp2 = "her"
                $ cgp3 = "hers"
                $ cgp4 = "herself"
            if cg1 == "he" or "him" or "He" or "Him":
                $ cg1 = "he"
                $ cgp = "him"
                $ cgp2 = "his"
                $ cgp3 = "his"
                $ cgp4 = "himself"
            elif cg1== "she" or "her" or "She" or "Her":
                $ cg1 = "she"
                $ cgp = "her"
                $ cgp2 = "her"
                $ cgp3 = "hers"
                $ cgp4 = "herself"
            else:
                $ cg1 = "they"
                $ cgp = "them"
                $ cgp2 = "their"
                $ cgp3 = "theirs"
                $ cgp4 = "themselves"

menu:
    "How old are you?"

    "Teenager":
        $ Teenager = True
        if Teenager:
            g1 "Little young to be out on your own ain't you?" #SKIP EVENTS NOT YET LISTED AS THEY ARE NOT OLD ENOUGH
        elif Boy or Girl or gender and Teenager:
            g1 "Where are your parents?" #Boy/Girl/Both Teenager
    "Young Adult":
        $ YoungAdult = True
        if Boy or Girl or gender and YoungAdult:
            g1 "Yes you. Are you new to town, I've never seen you before." #Boy/Girl/Both Young Adult
    "Adult":
        $ Adult = True
        if Girl and Adult:
            "You slowly walk over to the guard."
            g1 "Yes you ma'm" #Girl Adult
        elif Boy and Adult:
            "You slowly walk over to the guard."
            g1 "Yes you sir." #Boy Adult
        elif gender and Adult:
            "You slowly walk over to the guard."
            g1 "Yes you right there, are you new to Kathelm?" #Both Adult

g1 "So, where are you from?"

menu WhereAreYouFrom:
    "Felis":
        $home = "Felis"
        $ Felis = True
        $twins_points +=1
        $alice_points +=1
        $risby_points +=1
    "Catus":
        $home = "Catus"
        $ Catus = True
        $pansy_points +=1
        $sable_points +=1
        $rula_points +=1
    "Silvestris":
        $home = "Silvestris"
        $ Silvestris = True
        $aurora_points+=1

p1 "Oh, hi my name is [PN]. I'm from [home]."

show Guard1_Happy at left

g1 "What brings you to Kathelm [PN]?"

if YoungAdult or Adult:
    menu:
        "I'm a Political Advisor for Princess Pansy.":
            $ pansy_points += 1
            $ PoliticalAdviser = True
            if PoliticalAdviser:
                $ p1 = Character("Political Advisor [PN]")
            g1 "Heading off the castle then are you?"
            menu PansyRoutePt1:
                "Yes, I can't wait to start working on getting Princess Pansy to the throne":
                    $ pansy_points +=1
                    g1 "Well you probably don't need directions then given that its that big fancy building just up ahead."
                    hide Guard1_Happy
                    hide Guard1
                    jump PreludePt2
                "No, I don't start until tomorrow, I think I'm going to look around Kathlem a bit first.":
                    g1 "Enjoy your sightseeing then, and don't forget to find a place to stay for the night."
                    g1 "The best place in town is the Gilded Clover."
                    g1 "Or if you're looking for something less fancy, theres always the Kathelm Inn just around the way."
                    $ pansy_points -= 1
                    menu Directions:
                        "Ask for directions to the The Gilded Clover":
                            $ pansy_points +=1
                            jump GildedClover1
                        "Ask for directions to the Kathelm Inn":
                            $ pansy_points -= 1
                            jump Kathelm_Inn1
                        "You'll worry about places to stay later":
                            $ pansy_points -= 1
                            jump Kathelm_Town1
        "I was in the military and I'm coming home.":
            $ rula_points += 1
            $ Officer = True
            if Officer:
                    $ p1 = Character("Officer [PN]")
            g1 "Well then you'll be needing to check in over at the Chamber of War?"
            menu CheckIn1:
                "Yes, I was on my way there before you stopped me.":
                    g1 "Do you need directions?"
                    menu:
                        "Yes":
                            na "He gives you detailed directions that take you to the Chamber of War."
                            jump Chamber_of_War1
                        "No, I know where I'm going":
                            jump Chamber_of_War1
                "No, I have some business to attend to before hand":
                    jump chapter_oneRula
        "I am starting my studies at Kathelm University.":
            $ alice_points += 1
            $ Student = True
            if Student:
                $ p1 = Character("Student [PN]")
            g1 "Best of luck to you then [PN]"
            menu WhoNeedsLuck:
                "No luck needed just dedication and hardwork!":
                    $ alice_points += 1
                    g1 "Fair point [PN]"
                "Something mystical about the stars and the planets alignment guiding you":
                    $ twins_points += 1
                    g1 "Ah, a star gazer then?"
                    menu MysticPathPt1:
                        "Yes, I study the stars and the moons and the cosmos.":
                            $ twins_points += 1
                            $ alice_points -= 1
                        "It's one of my many courses of study.":
                            $ alice_points += 1
        "Come to see the creation of the new kingdom.":
            $ sable_points += 1
        "I looked to the stars for directions and this is where they led":
            $ twins_points += 1
        "I'm a merchant here to set up a new shop":
            $ risby_points += 1
        "Not really sure, just wandering and going to new places. Seeing the sights":
            $ aurora_points += 1

if Teenager:
    menu TeenagerRoutePt1:
        "I was in the military and I'm coming home.":
            $ rula_points += 1
            $ Private = True
            if Private:
                    $ p1 = Character("Private [PN]")
            na "The guard nods his head to you."
            g1 "Thankful it is over then I take?"
            menu optional_name:
                "Yes, the fighting was exhuasting. I for one am glad it is over":
                    $ pansy_points += 1
                "No"
                    #block of code to run
        "I am starting my studies at Kathelm University.":
            $ alice_points += 1
            $ Student = True
            if Student:
                $ p1 = Character("Student [PN]")
        "Come to pay my respects to the monarchy.":
            $ sable_points += 1
        "I looked to the stars for directions and this is where they led":
            $ twins_points += 1
        "Not really sure, just wandering and going to new places. Seeing the sights."

label PreludePt2:

na "You arrive at a grand looking building. It is a hodgepodge of greek revival and modern construction."
na "Outside of the building is ablaze with activity, people fetching and carrying things all over the place."
na "You once again are approched by a guard"

show Guard2
g2 "Its a lot to take in, can I help you find something?"
menu PansyRoutePt2:
    "I am looking for Princess Pansy.":
        g2 "Ah, I believe she is in with the the Senators right now."
        g2 "There is a lot of set up invovled with our new kingdom."
        g2 "And without a sitting monarch even more work to be done."
        p1 "Senators?"
        g2 "Yes, yes. Old fogy, eh hem, several older gentlemen and gentleladies from the three kingdoms."
        g2 "Theyre the temporary ruling power until a Queen can be choosen."
        p1 "When will a Queen be choosen?"
        g2 "Any day now I'm sure. Thats part of what theyre working on right now."
        hide Guard2
        jump PansyPrologue
    "No thank you I know where I'm going.":
        g2 "Well best of luck to you, I still get lost around this place."
        jump SablePrologue1



#Chapter One
label chapter_one:
label chapter_onePansy:
hide Guard1
show Pansy_Happy at right

pa "My name as many of you know is Pansy. I am the oldest of King Ghents daughters"

hide Pansy_Happy

label chapter_oneRula:

ru "Isn't my sister lovely?"

label chapter_oneSable:

sa "Hello everyone. I would like to submit myself to you the people and become your queen."

label chapter_oneAurora:

na "From the crowd a cloaked figure approaches. They are slight in stature"
au "Something cutting and witty."

label chapter_oneAlice:

al "Something wise and older sounding than her appeaerance belies"

label chapter_oneTwins:

bm "Something mysterious and cunning"
be "Nothing"
mo "Nothing"


label chapter_oneRisby:

ri "Something about power and money"

$ advance_time(1)
show text "[dow] [time_now]" with Pause (3)
hide text with dissolve

scene bg room
label chapter_two:

show text "CHAPTER TWO" with Pause(4)
hide text with dissolve

$ advance_time(1)
show text "[dow] [time_now]" with Pause (3)
hide text with dissolve

menu:
    "Do you have a preference for our future Queen?"
    "Princess Pansy has my backing, she's the most politically sauve of all the sisters":
        $ pansy_points += 1
        if pansy_points == 2:
            g1 "Well you've come at the right time then."
    "Princess Rula was a good leader for us during the war.":
        $ rula_points += 1
        if rula_points == 2:
            "You wax poetically about her battle prowess."
    "PRINCESS SABLE!":
        $ sable_points += 1
        if sable_points == 5:
            "You sigh involuntarily, hearts in your eyes. She's just so charming."
            "The guard smirks knowingly at you"
            g1 "Ah yes Princess Sable does have quite the following."
    "The twins rule, they would rule with magic & the stars on their side.":
        $ twins_points += 1
    "Princess Alice of course, she's the best suited to rule.":
        $ alice_points += 1
    "Not really sure, it really depends on the coming election":
        $ aurora_points += 1

label chapter_twoPansy:
label chapter_twoRula:
label chapter_twoSable:
label chapter_twoAurora:
label chapter_twoAlice:
label chapter_twoTwins:
label chapter_twoRisby:

scene bg room
label chapter_three:

show text "CHAPTER THREE" with Pause(4)
hide text with dissolve

"Here lay the start of chapter three"

$ advance_time(1)
show text "[dow] [time_now]" with Pause (3)
hide text with dissolve

label chapter_threePansy:
label chapter_threeRula:
label chapter_threeSable:
label chapter_threeAurora:
label chapter_threeAlice:
label chapter_threeTwins:
label chapter_threeRisby:

label chapter_four:

show text "CHAPTER FOUR" with Pause(4)
hide text with dissolve

"Here lay the start of chapter four"

$ advance_time(1)
show text "[dow] [time_now]" with Pause (3)
hide text with dissolve

label chapter_fourPansy:
label chapter_fourRula:
label chapter_fourSable:
label chapter_fourAurora:
label chapter_fourAlice:
label chapter_fourTwins:
label chapter_fourRisby:

label chapter_five:

show text "CHAPTER FIVE" with Pause(4)
hide text with dissolve

"Here lay the start of chapter five"

$ advance_time(1)
show text "[dow] [time_now]" with Pause (3)
hide text with dissolve

label chapter_fivePansy:
label chapter_fiveRula:
label chapter_fiveSable:
label chapter_fiveAurora:
label chapter_fiveAlice:
label chapter_fiveTwins:
label chapter_fiveRisby:


jump The_End

return
