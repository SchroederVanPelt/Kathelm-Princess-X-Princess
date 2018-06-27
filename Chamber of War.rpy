scene bg room
label Chamber_of_War1:
    scene black
na "You arrive at a large glass and stone building. An interesting combination of greek revival and modern archecture."
na "Outside of it are seveal guards dressed in similar uniforms."
"Confidently you stroll forward."
na "Dialogue that explains Nathan challenging you to a friendly dual"

if Political Advisor:
    jump CombatOne_Alt
else:
    call CombatOne

label CombatOneEnd:

show GNathan_surprised on left
"Nathan huffs out a breath"
gn "Not bad."
"He sticks out his hand for you to shake. You take it swapping the blade from one hand to the other."
p1 "Not bad yourself. Its been a while since I had a good workout."

label CombatOne_AltEnd:


return
