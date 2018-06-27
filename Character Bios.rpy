define na = Character("Narrator", who_font="CaviarDreams_Bold.ttf")

define pa = Character("First Princess Pansy", color="#660033", who_font="CaviarDreams_Bold.ttf", image="Pansy_Neutral")
define ta = Character("Taylor") #Pansy Political Advisor
define ti = Character("Tiffany") #Pansy Knight

define ru = Character("Warrior Princess Rula", color="#DBB1CD", who_font="CaviarDreams_Bold.ttf")
define gi = Character("Giles") #Rula Political Advisor
define gn = Character("Guard Nathan", image="GNathan_neutral") #Rula Knight

define sa = Character("Charming Princess Sable", color="#6b5b95", who_font="CaviarDreams_Bold.ttf")
define ma = Character("Malcom") #Sable Political Advisor
define ma = Character("Marilyn") #Sable Knight

define au = Character("Witch Princess Aurora", color="#800080", who_font="CaviarDreams_Bold.ttf")
define st = Character("Stacy") #Aurora Political Advisor
define hi = Character("Hilda") #Aurora Knight

define bm = Character("Star Princesses Bea & Mona", color="#8dc154", who_font="CaviarDreams_Bold.ttf")
define be = Character("Star Princess Bea", color="#bf8f01", who_font="CaviarDreams_Bold.ttf")
define mo = Character("Star Princess Mona", color="#002080", who_font="CaviarDreams_Bold.ttf")
define ni = Character("Nicodemus") #Bea & Mona Political Advisor
define am = Character("Ambrose") #Bea & Mona Knight

define al = Character("Scholar Princess Alice", color="#ff9000", who_font="CaviarDreams_Bold.ttf")
define ed = Character("Edward") #Alice Political Advisor
define si = Character("Sigmund") #Alice Knight

define ri = Character("Merchant Princess Risby", color="#007256", who_font="CaviarDreams_Bold.ttf")
define de = Character("Della") #Risby Political Advisor
define jo = Character("Josephine") # Risby Knight

define g1 = Character("Guard", color="#000000", who_font="CaviarDreams_Bold.ttf", image="Guard1_Neutral")
define g2 = Character("Guard", color="#000000" ,who_font="CaviarDreams_Bold.ttf", image="Guard2_Neutral")

##############################################################################

init python:
    xmax = config.screen_width
    ymax = config.screen_height
init -2 python:
    #declares a new style called "infoscreen"
    style.infoscreen = Style(style.default)
    style.infoscreen_text.size = 25
    style.infoscreen_window.background = "infoscreenBG.png"  #<-- This puts a custom background in the area that displays the text and picture
    style.infoscreen_frame.background = Frame("box.png", 10, 10) #<--same as above, but in the area that displays the buttons
    #style.infoscreen_button.idle_background = Frame("box2.png", 10, 10)
    style.infoscreen_button.hover_background = Frame("box3.png", 10, 10)
    style.infoscreen_button_text.idle_color = "#000000"
    style.infoscreen_button_text.hover_color = "#000000"
    style.infoscreen_button_text.selected_color = "#000000"
    style.infoscreen_button.top_padding = 5
    style.infoscreen_button.bottom_padding = 5
    #style.infoscreen_bar.left_bar = "bar_full-checks.png"
    style.infoscreen_bar.right_bar = "bar_empty-checks.png"
    style.infoscreen_bar.xmaximum = 209
    style.infoscreen_bar.ymaximum = 34
    style.infoscreen_bar.right_gutter = 0
    style.infoscreen_bar.left_gutter = 0
    style.infoscreen_bar.thumb = None

init python:

    class char:
        def __init__(self, names, bloodType, age, birthday, sign, likes, dislikes, dateable=False, images="" ):
            self.names = names
            self.bloodType = bloodType
            self.age = age
            self.birthday = birthday
            self.sign = sign
            self.likes = likes
            self.dislikes = dislikes
            self.dateable = dateable
            self.images = images

    class princess(char):
        def __init__(self, level=1, public=0, military=0, merchants=0, church=0, noble=0, *args, **kwargs):
            char.__init__(self, **kwargs)
            self.level = level
            self.public = public
            self.military = military
            self.merchants = merchants
            self.church = church
            self.noble = noble

    def earn(self, amount):
        self.level += amount
        self.public += amount
        self.military += amount
        self.merchants += amount
        self.church += amount
        self.noble += amount

    def lose(self, amount):
        self.level -= amount
        self.public -= amount
        self.military -= amount
        self.merchants -= amount
        self.church -= amount
        self.noble -= amount

    def normalize(self):
        if self.level > levelMax:
            self.level = levelMax
        if self.level < 1:
            self.level = 1

init:
    $ Pansy = princess(
        names="First Princess Pansy",
        bloodType="B",
        age="Adult",
        birthday="January 8th",
        sign="Sagittarius",
        likes="Chaschews & Milk",
        dislikes="Roses & slackers",
        dateable=False,
        images="",
        level="1",
        public="1",
        military="1",
        merchants="1",
        church="12",
        noble="5"
    )

    $ Rula = princess(
        names="Warrior Princess Rula",
        bloodType="",
        age="",
        birthday="",
        sign="",
        likes="",
        dislikes="Mint Chocolate Chip",
        dateable=False,
        images="",
        level="1",
        public="0",
        military="5",
        merchants="0",
        church="0",
        noble="3"
        )

    $ Sable = princess(
        names="Charming Princess Sable",
        bloodType="A",
        age="Adult",
        birthday="May 6th",
        sign="Aries",
        likes="",
        dislikes="",
        dateable=False,
        images="",
        level="1",
        public="5",
        military="1",
        merchants="1",
        church="1",
        noble="4"
        )

    $ Aurora = princess(
        names="Witch Princess Aurora",
        bloodType="",
        age="",
        birthday="",
        sign="",
        likes="",
        dislikes="",
        dateable=False,
        images="",
        level="1",
        public="0",
        military="0",
        merchants="0",
        church="0",
        noble="0"
        )

    $ Bea = princess(
        names="Star Princess Bea",
        bloodType="",
        age="",
        birthday="",
        sign="",
        likes="",
        dislikes="",
        dateable=False,
        images="",
        level="1",
        public="0",
        military="0",
        merchants="0",
        church="0",
        noble="5"
        )

    $ Mona = princess(
        names="Star Princess Mona",
        bloodType="",
        age="",
        birthday="",
        sign="",
        likes="",
        dislikes="",
        dateable=False,
        images="",
        level="1",
        public="0",
        military="0",
        merchants="0",
        church="0",
        noble="5"
        )

    $ Alice = princess(
        names="Scholar Princess Alice",
        bloodType="",
        age="",
        birthday="",
        sign="",
        likes="",
        dislikes="",
        dateable=False,
        images="",
        level="1",
        public="0",
        military="0",
        merchants="0",
        church="0",
        noble="5"
        )
    $ Risby = princess(
        names="Merchant Princess Risby",
        bloodType="",
        age="17",
        birthday="March 5th",
        sign="Aquarius",
        likes="Pistachicos & Midori sours",
        dislikes="Stuff",
        dateable=False,
        images="",
        level="1",
        public="1",
        military="0",
        merchants="5",
        church="1",
        noble="3"
        )


    $ print Pansy.names
    $ print Pansy.church
    $ print "Init complete"


init:

    default names = ""
    default bloodtype = ""
    default age = ""
    default birthday = ""
    default sign = ""
    default likes = ""
    default dislikes = ""
    default level =  ""
    default public = ""
    default military = ""
    default merchants = ""
    default church = ""
    default noble = ""
    default viewing = ""

screen profile_screen():
    tag menu
    zorder 10
    # creates a string for proper display of each fact (+some bars)
    $ characters = [Pansy, Rula, Sable, Aurora, Bea, Mona, Alice, Risby]
    for i in characters:
        $ character = i
        if viewing == character.names:
            python:
              names = "Name: " + character.names
              bloodType = "Blood Type: " + character.bloodType
              age = "Age: " + character.age
              birthday = "Date of Birth: " + character.birthday
              sign = "Sign: " + character.sign
              likes = "Likes: " + character.likes
              dislikes = "Dislikes: " + character.dislikes
              level = "Level:" + character.level
              public = "Public:" + character.public
              military = "Military:" +character.military
              merchants = "Merchants:" + character.merchants
              church = "Church:" + character.church
              noble = "Nobel:" + character.noble
#actually displays everything
    frame xminimum 240 xmaximum 240 yminimum ymax:
        style_group "infoscreen"
    #    vbox: #yalign 0.5 xalign 0.5:
    #        for i in character:
                textbutton i.names action [SetVariable("viewing", i.names), LogMessage(i.names), LogMessage(viewing)]:
                    background Solid("#FF0000")
    #                xminimum 220 xmaximum 220 yminimum 50
    #                xmargin 10 ymargin 10
        textbutton "Pansy" action SetVariable("viewing", Pansy.names ) ypos 0.1
        textbutton "Rula" action SetVariable("viewing", Rula.names ) ypos 0.2
        textbutton "Sable" action SetVariable("viewing", Sable.names ) ypos 0.3
        textbutton "Aurora" action SetVariable("viewing", Aurora.names ) ypos 0.4
        textbutton "Bea" action SetVariable("viewing", Bea.names ) ypos 0.5
        textbutton "Mona" action SetVariable("viewing", Mona.names ) ypos 0.6
        textbutton "Alice" action SetVariable("viewing", Alice.names ) ypos 0.7
        textbutton "Risby" action SetVariable("viewing", Risby.names ) ypos 0.8

        textbutton "Return" action Return() ypos 0.9:
            text_color "#FF0000"
    window xanchor 0 xpos 240 yalign 0 xminimum 784 xmaximum 784 yminimum ymax ymaximum ymax:
        style_group "infoscreen"
        vbox spacing 10:
            vbox:
                text names
                text bloodtype
                text age
                text birthday
                text sign
            vbox xmaximum 500:
                text likes
                text dislikes
