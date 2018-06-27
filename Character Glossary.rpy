screen wiki_pansy():

    tag menu

    use game_menu(_("First Princess Pansy")):

        text _p("""
            Age:

            Hobbies:

            Favorite Snacks: Cha siu bao

            BIO COMING SOON HERE

            {a=showmenu:wiki_index}Back to Index{/a}
            """)

define config.hyperlink_protocol = "showmenu"

screen wiki_rula():

    tag menu

    use game_menu(_("Warrior Princess Rula")):

        text _p("""
            Age:

            Hobbies:

            Favorite Snacks:

            BIO COMING SOON HERE

            {a=wiki_index}Back to Index{/a}
            """)
screen wiki_sable():

    tag menu

    use game_menu(_("Charming Princess Sable")):

        text _p("""
            Age:

            Hobbies:

            Favorite Snacks:

            BIO COMING SOON HERE

            {a=showmenu:wiki_index}Back to Index{/a}
            """)

define config.hyperlink_protocol = "showmenu"

screen wiki_aura():

    tag menu

    use game_menu(_("Witch Princess Aura")):

        text _p("""
            Age:

            Hobbies:

            Favorite Snacks:

            BIO COMING SOON HERE

            {a=showmenu:wiki_index}Back to Index{/a}
            """)

define config.hyperlink_protocol = "showmenu"

screen wiki_bea():

    tag menu

    use game_menu(_("Twin Princess Bea")):

        text _p("""
            Age:

            Hobbies:

            Favorite Snacks:

            Bea is the younger of the two twins. Bea is a power magician in her own right.

            {a=showmenu:wiki_index}Back to Index{/a}
            """)

define config.hyperlink_protocol = "showmenu"

screen wiki_mona():

    tag menu

    use game_menu(_("Twin Princess Mona")):

        text _p("""
            Age:

            Hobbies:

            Favorite Snacks:

            BIO COMING SOON HERE

            {a=showmenu:wiki_index}Back to Index{/a}
            """)

define config.hyperlink_protocol = "showmenu"

screen wiki_alice():

    tag menu

    use game_menu(_("Scholar Princess Alice")):

        text _p("""
            Age:

            Hobbies:

            Favorite Snacks:
            BIO COMING SOON HERE

            {a=showmenu:wiki_index}Back to Index{/a}
            """)

define config.hyperlink_protocol = "showmenu"

screen wiki_risby():

    tag menu

    use game_menu(_("Merchant Princess Risby")):

        text _p("""
            Age:

            Hobbies:

            Favorite Snacks:
            BIO COMING SOON HERE

            {a=showmenu:wiki_index}Back to Index{/a}
            """)

define config.hyperlink_protocol = "showmenu"

screen wiki_index():

    tag menu

    use game_menu(_("Wiki Index")):

        vbox:
            text _p("""
            • {a=wiki_pansy}First Princess Pansy{/a}{p}
            • {a=wiki_rula}Warrior Princess Rula{/a}{p}
            • {a=wiki_sable}Charming Princess Sable{/a}{p}
            • {a=wiki_aura}Witch Princess Aura{/a}{p}
            • {a=wiki_bea}Twin Princess Bea{/a}{p}
            • {a=wiki_mona}Twin Princess Mona{/a}{p}
            • {a=wiki_alice}Scholar Princess Alice{/a}{p}
            • {a=wiki_risby}Merchant Princess Risby{/a}{p}
            """)
