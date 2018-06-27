label The_End:

na "Something prefacing the ending that the player has gotten. Full of If and else statements and jumps to appropriate"

if pansy_points > max(rula_points, sable_points, aurora_points, twins_points, alice_points, risby_points):
    #if merchant == 10
    jump pansy_ending
elif rula_points > max(pansy_points, sable_points, aurora_points, twins_points, alice_points, risby_points):
    jump rula_ending
elif sable_points  > max(pansy_points, rula_points, aurora_points, twins_points, alice_points, risby_points):
    jump sable_ending
elif aurora_points > max(pansy_points, rula_points, sable_points, twins_points, alice_points, risby_points):
    jump aurora_ending
elif twins_points > max(pansy_points, rula_points, sable_points, aurora_points, alice_points, risby_points):
    jump twins_ending
elif alice_points  > max(pansy_points, rula_points, sable_points, aurora_points, twins_points, risby_points):
    jump alice_ending
elif risby_points   > max(pansy_points, rula_points, sable_points, aurora_points, twins_points, alice_points):
    jump risby_ending
else:
    jump bad_ending

label pansy_ending:

    "Pansy becomes Queen"

label rula_ending:

    "Rula becomes Queen"

label sable_ending:

    "Sable becomes Queen"

label aurora_ending:

    "Aurora becomes Queen and brings Silvestris fully into the folds of Kathelm"

label twins_ending:

    "Bea & Mona become joint Queens and rule leading by the stars"

label alice_ending:

    "Alice becomes Queen"

label risby_ending:

    "Risby become Queen"

label bad_ending:

    "The kingdom decends into chaos and falls back into war."

show text "The End" with Pause (10)
hide text with dissolve

label Credits:

return
