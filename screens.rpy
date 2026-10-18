################################################################################
## Initialization
################################################################################

init offset = -1

## Ensure persistent.theme is always declared (also defaulted in themes.rpy)
default persistent.theme = "crimson"


# Transform for Discord button hover effect
transform discord_button_hover:
    zoom 1.0
    on selected:
        zoom 1.2, 0.2
    on deselected:
        zoom 1.0, 0.2

# Transform for Steam button hover effect
transform steam_button_hover:
    zoom 1.0
    on selected:
        zoom 1.2, 0.2
    on deselected:
        zoom 1.0, 0.2

# Modern textbox appear/disappear effect
transform textbox_appear:
    alpha 0.0 yoffset 15
    ease 0.25 alpha 1.0 yoffset 0

# Textbox idle state with subtle breathing
transform textbox_idle:
    alpha 0.92

# Choice button hover effects
transform choice_btn_idle:
    alpha 0.85 xoffset 0
    on hover:
        ease 0.15 alpha 1.0 xoffset 8
    on idle:
        ease 0.2 alpha 0.85 xoffset 0

# Choice list appear animation
transform choice_appear(delay=0.0):
    alpha 0.0 xoffset -30
    pause delay
    ease 0.3 alpha 1.0 xoffset 0

# Quick menu button hover
transform quick_btn_hover:
    alpha 0.6
    on hover:
        ease 0.1 alpha 1.0
    on idle:
        ease 0.2 alpha 0.6

# Main menu title reveal - slow fade from darkness
transform title_reveal:
    alpha 0.0 yoffset -10
    pause 0.3
    ease 1.2 alpha 1.0 yoffset 0

# Title decoration extends outward
transform title_deco_reveal:
    alpha 0.0 xzoom 0.0
    pause 0.8
    ease 0.8 alpha 0.7 xzoom 1.0

# Subtitle fades in after title
transform subtitle_reveal:
    alpha 0.0
    pause 1.0
    ease 0.6 alpha 0.6

# Menu buttons stagger in from left
transform menu_btn_appear(delay=0.0):
    alpha 0.0 xoffset -40
    pause delay
    ease 0.35 alpha 1.0 xoffset 0

# Menu button hover - crimson pulse
transform menu_btn_hover:
    alpha 0.85
    on hover:
        ease 0.15 alpha 1.0
    on idle:
        ease 0.25 alpha 0.85

# Corner decorations fade in slowly
transform corner_fade(delay=0.0):
    alpha 0.0
    pause delay
    ease 1.5 alpha 0.35

# Slow ambient drift for atmosphere
transform ambient_drift:
    alpha 0.15
    parallel:
        ease 8.0 alpha 0.25
        ease 8.0 alpha 0.15
        repeat


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    # Main dialogue window
    window:
        id "window"
        style "say_window"
        at textbox_idle

        # Left accent decoration
        add ("gui/themes/{}/textbox_accent_left.png".format(persistent.theme) if persistent.theme != "crimson" else "gui/textbox_accent_left.png") xpos 8 yalign 0.5

        # Right accent decoration
        add ("gui/themes/{}/textbox_accent_right.png".format(persistent.theme) if persistent.theme != "crimson" else "gui/textbox_accent_right.png") xalign 1.0 xoffset -8 yalign 0.5

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window is default

style say_window:
    xalign 0.5
    xsize 1400
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Frame("gui/textbox.png", 25, 10, 25, 10)  ## overridden at runtime by apply_theme()
    padding (55, 45, 55, 75)
    margin (0, 0, 0, 0)

style namebox:
    xpos gui.name_xpos
    xanchor 0.0
    xsize gui.namebox_width
    ypos gui.name_ypos
    yanchor 0.0
    ysize gui.namebox_height

    background Frame("gui/namebox.png", 15, 8, 15, 8)
    padding (20, 8, 20, 8)

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    outlines [(2, "#000000cc", 0, 0), (1, "#a0143044", 2, 2)]
    size 28

style say_dialogue:
    properties gui.text_properties("dialogue")

    xalign 0.5
    xsize 1280
    yalign 0.5
    text_align 0.5

    adjust_spacing False

    outlines [(1, "#000000cc", 1, 1)]
    color "#c8b8b0"
    line_spacing 6
    size 26

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        # Decorative header line above choices
        add ("gui/themes/{}/choice_header_decoration.png".format(persistent.theme) if persistent.theme != "crimson" else "gui/choice_header_decoration.png") xalign 0.5

        null height 12

        for idx, i in enumerate(items):
            textbutton i.caption action i.action at choice_appear(delay=idx * 0.08)


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.5
    yanchor 0.5

    spacing 12

style choice_button is default:
    xalign 0.5
    xsize 860
    ysize None
    yminimum 52
    background Frame("gui/button/choice_idle_background.png", 18, 12, 18, 12)
    hover_background Frame("gui/button/choice_hover_background.png", 18, 12, 18, 12)
    insensitive_background Frame("gui/button/choice_insensitive_background.png", 18, 12, 18, 12)
    padding (40, 12, 40, 12)
    margin (0, 0, 0, 0)

style choice_button_text is default:
    xalign 0.5
    yalign 0.5
    idle_color "#b09080ee"
    hover_color "#d4a050"
    insensitive_color "#403038"
    text_align 0.5
    size 24
    outlines [(1, "#000000cc", 1, 0)]


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        # Background bar
        add ("gui/themes/{}/quick_menu_bar.png".format(persistent.theme) if persistent.theme != "crimson" else "gui/quick_menu_bar.png") yalign 1.0

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("Back") action Rollback() at quick_btn_hover
            textbutton _("History") action ShowMenu('history') at quick_btn_hover
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True) at quick_btn_hover
            textbutton _("Auto") action Preference("auto-forward", "toggle") at quick_btn_hover
            textbutton _("Save") action ShowMenu('save') at quick_btn_hover
            textbutton _("Q.Save") action QuickSave() at quick_btn_hover
            textbutton _("Q.Load") action QuickLoad() at quick_btn_hover
            textbutton _("Prefs") action ShowMenu('preferences') at quick_btn_hover


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0
    yoffset -4
    spacing 8

style quick_button:
    background Frame("gui/button/quick_idle_background.png", 10, 6, 10, 6)
    hover_background Frame("gui/button/quick_hover_background.png", 10, 6, 10, 6)
    padding (14, 5, 14, 5)

style quick_button_text:
    size 16
    idle_color "#706068"
    hover_color "#d4a050"
    selected_color "#a01430"
    outlines [(1, "#000000aa", 0, 0)]


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    # Main menu navigation is now handled directly in screen main_menu()
    # This screen only provides in-game navigation

    if not main_menu:
        # In-game menu navigation - side positioned with themed styling
        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.5

            spacing gui.navigation_spacing

            textbutton _("History") action ShowMenu("history")
            textbutton _("Journal") action ShowMenu("journal")
            textbutton _("Save") action ShowMenu("save")
            textbutton _("Load") action ShowMenu("load")
            textbutton _("Preferences") action ShowMenu("preferences")
            if _in_replay:
                textbutton _("End Replay") action EndReplay(confirm=True)

            elif not main_menu:
                textbutton _("Main Menu") action MainMenu()

            textbutton _("About") action ShowMenu("about")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                textbutton _("Help") action ShowMenu("help")

            if renpy.variant("pc"):
                textbutton _("Quit") action Quit(confirm=not main_menu)

    # Also handle sub-menu navigation when accessed from the main menu.
    if main_menu and (renpy.get_screen("load") or renpy.get_screen("preferences") or renpy.get_screen("about") or renpy.get_screen("help")):
        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.5

            spacing gui.navigation_spacing

            textbutton _("Start") action Start()
            textbutton _("Load") action ShowMenu("load")
            textbutton _("Preferences") action ShowMenu("preferences")
            textbutton _("About") action ShowMenu("about")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                textbutton _("Help") action ShowMenu("help")

            if renpy.variant("pc"):
                textbutton _("Quit") action Quit(confirm=True)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    xminimum 300
    yminimum 44
    background Frame("gui/button/nav_idle_background.png", 8, 6, 8, 6)
    hover_background Frame("gui/button/nav_hover_background.png", 8, 6, 8, 6)
    padding (16, 8, 16, 8)

style navigation_button_text:
    font "DejaVuSans.ttf"
    size 22
    idle_color "#706068"
    hover_color "#d4a050"
    selected_color "#a01430"
    outlines [(1, "#000000aa", 1, 0)]
    yalign 0.5


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
## Enhanced with centered layout and advanced styling.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    tag menu

    # Background image
    add "main_menu_bg"

    # Dark atmospheric overlay
    add "gui/overlay/main_menu.png"

    # Corner decorations - themed
    add ("gui/themes/{}/corner_tl.png".format(persistent.theme) if persistent.theme != "crimson" else "gui/corner_tl.png") xpos 0 ypos 0 at corner_fade(0.5)
    add ("gui/themes/{}/corner_tr.png".format(persistent.theme) if persistent.theme != "crimson" else "gui/corner_tr.png") xalign 1.0 ypos 0 at corner_fade(0.8)
    add ("gui/themes/{}/corner_bl.png".format(persistent.theme) if persistent.theme != "crimson" else "gui/corner_bl.png") xpos 0 yalign 1.0 at corner_fade(1.1)
    add ("gui/themes/{}/corner_br.png".format(persistent.theme) if persistent.theme != "crimson" else "gui/corner_br.png") xalign 1.0 yalign 1.0 at corner_fade(1.4)

    # Main content - left-aligned for cinematic feel
    vbox:
        xpos 120
        yalign 0.45
        spacing 10

        # Title section
        vbox:
            spacing 6

            # Game title with dark theme
            text "{font=DejaVuSans-Bold.ttf}{size=72}{color=#c8a050}The{/color} {color=#8a1828}Azimov{/color} {color=#c0b8b0}Virus{/color}{/size}{/font}":
                at title_reveal
                outlines [(3, "#000000", 2, 2), (1, "#a0143088", 4, 4)]
                line_spacing 0

            # Thematic subtitle
            text "{font=DejaVuSans.ttf}{size=18}{color=#706060}{i}Ici, l'innocence est le premier péché, et le monde ne cesse de la punir.{/i}{/color}{/size}{/font}":
                at subtitle_reveal
                outlines [(1, "#00000088", 1, 1)]

            null height 4

            # Title decoration line (themed)
            add ("gui/themes/{}/title_decoration.png".format(persistent.theme) if persistent.theme != "crimson" else "gui/title_decoration.png") at title_deco_reveal

            null height 2

            # Version
            text "{font=DejaVuSans.ttf}{size=14}{color=#50404a}v[config.version]{/color}{/size}{/font}":
                at subtitle_reveal

        null height 40

        # Separator
        add ("gui/themes/{}/menu_separator.png".format(persistent.theme) if persistent.theme != "crimson" else "gui/menu_separator.png") at title_deco_reveal

        null height 20

        # Menu buttons with staggered appear
        vbox:
            spacing 8

            textbutton _("Nouvelle Partie"):
                style "main_menu_button"
                action Start()
                at menu_btn_appear(1.2)

            textbutton _("Continuer"):
                style "main_menu_button"
                action ShowMenu("load")
                at menu_btn_appear(1.35)

            textbutton _("Préférences"):
                style "main_menu_button"
                action ShowMenu("preferences")
                at menu_btn_appear(1.5)

            textbutton _("A propos"):
                style "main_menu_button"
                action ShowMenu("about")
                at menu_btn_appear(1.65)
            textbutton _("Support"):
                style "main_menu_button"
                action OpenURL("https://app.unifans.io/c/madd5")
                at menu_btn_appear(2.1)

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                textbutton _("Aide"):
                    style "main_menu_button"
                    action ShowMenu("help")
                    at menu_btn_appear(1.8)

            if renpy.variant("pc"):
                textbutton _("Quitter"):
                    style "main_menu_button"
                    action Quit(confirm=True)
                    at menu_btn_appear(1.95)



    # Discord logo button in bottom left
    button:
        xpos 20
        yalign 0.99
        xysize (64, 64)
        background None
        add Transform("gui/discord_button.png", xysize=(64, 64)):
            at discord_button_hover
        action OpenURL("https://discord.gg/xAa3YMSe4D")

    # Steam logo button next to Discord
    button:
        xpos 94
        yalign 0.99
        xysize (64, 64)
        background None
        add Transform("gui/steam_button.png", xysize=(64, 64)):
            at steam_button_hover
        action OpenURL("https://steamcommunity.com/tradeoffer/new/?partner=855455229&token=Vewegv5X")

    # Bottom right - atmospheric text
    text "{font=DejaVuSans.ttf}{size=12}{color=#302028}every choice leaves a mark{/color}{/size}{/font}":
        xalign 0.95
        yalign 0.97
        at subtitle_reveal


## Main menu button styles - corruption theme
style main_menu_button:
    xsize 360
    yminimum 50
    background Frame("gui/button/menu_idle_background.png", 10, 8, 10, 8)
    hover_background Frame("gui/button/menu_hover_background.png", 10, 8, 10, 8)
    padding (24, 10, 24, 10)

style main_menu_button_text:
    font "DejaVuSans.ttf"
    size 24
    idle_color "#908080"
    hover_color "#d4a050"
    selected_color "#a01430"
    outlines [(1, "#000000aa", 1, 0)]
    text_align 0.0
    xalign 0.0
    yalign 0.5


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True
    background None

style main_menu_vbox:
    xalign 0.0
    xoffset 120
    xmaximum 500
    yalign 0.5

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)
    color "#908080"

style main_menu_title:
    size 72
    bold True
    font "DejaVuSans-Bold.ttf"
    color "#c8a050"
    text_align 0.0
    xalign 0.0

style main_menu_version:
    size 14
    font "DejaVuSans.ttf"
    color "#50404a"
    text_align 0.0
    xalign 0.0

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 75
    color "#a01430"
    outlines [(2, "#000000aa", 1, 1)]
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45
    background Frame("gui/button/nav_idle_background.png", 8, 6, 8, 6)
    hover_background Frame("gui/button/nav_hover_background.png", 8, 6, 8, 6)
    padding (16, 8, 16, 8)
    xminimum 200

style return_button_text:
    font "DejaVuSans.ttf"
    size 22
    idle_color "#706068"
    hover_color "#d4a050"
    outlines [(1, "#000000aa", 1, 0)]


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            ## ── UI Theme Selector ─────────────────────────────────────────
            null height (2 * gui.pref_spacing)

            vbox:
                spacing 10

                label _("UI Theme")

                hbox:
                    spacing 16

                    ## Crimson (default – dark corruption)
                    button:
                        style "theme_swatch_button"
                        action Function(apply_theme, "crimson")
                        selected persistent.theme == "crimson"
                        hbox:
                            spacing 8
                            yalign 0.5
                            frame:
                                xysize (18, 18)
                                yalign 0.5
                                background "#a01430"
                            text _("Crimson"):
                                style "theme_swatch_text"
                                color (("#c8b8b0" if persistent.theme != "crimson" else "#d4a050"))

                    ## Ocean (deep teal / cyan)
                    button:
                        style "theme_swatch_button"
                        action Function(apply_theme, "ocean")
                        selected persistent.theme == "ocean"
                        hbox:
                            spacing 8
                            yalign 0.5
                            frame:
                                xysize (18, 18)
                                yalign 0.5
                                background "#0a8fa0"
                            text _("Ocean"):
                                style "theme_swatch_text"
                                color (("#b0d8e8" if persistent.theme != "ocean" else "#00ddff"))

                    ## Forest (dark green / lime)
                    button:
                        style "theme_swatch_button"
                        action Function(apply_theme, "forest")
                        selected persistent.theme == "forest"
                        hbox:
                            spacing 8
                            yalign 0.5
                            frame:
                                xysize (18, 18)
                                yalign 0.5
                                background "#1a7a3a"
                            text _("Forest"):
                                style "theme_swatch_text"
                                color (("#b8d8a8" if persistent.theme != "forest" else "#a0e040"))

                    ## Violet (deep purple / magenta)
                    button:
                        style "theme_swatch_button"
                        action Function(apply_theme, "violet")
                        selected persistent.theme == "violet"
                        hbox:
                            spacing 8
                            yalign 0.5
                            frame:
                                xysize (18, 18)
                                yalign 0.5
                                background "#8030c0"
                            text _("Violet"):
                                style "theme_swatch_text"
                                color (("#d0b8e8" if persistent.theme != "violet" else "#e060ff"))

                    ## Ghost (transparent / black text)
                    button:
                        style "theme_swatch_button"
                        action Function(apply_theme, "ghost")
                        selected persistent.theme == "ghost"
                        hbox:
                            spacing 8
                            yalign 0.5
                            frame:
                                xysize (18, 18)
                                yalign 0.5
                                background "#cccccc88"
                            text _("Ghost"):
                                style "theme_swatch_text"
                                color (("#444444" if persistent.theme != "ghost" else "#111111"))

            ## ─────────────────────────────────────────────────────────────

            null height (2 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## Theme swatch buttons ########################################################

style theme_swatch_button:
    background Frame("gui/button/nav_idle_background.png", 8, 6, 8, 6)
    hover_background Frame("gui/button/nav_hover_background.png", 8, 6, 8, 6)
    selected_background Frame("gui/button/nav_hover_background.png", 8, 6, 8, 6)
    padding (14, 8, 14, 8)
    yminimum 38

style theme_swatch_text:
    font "DejaVuSans.ttf"
    size 20
    yalign 0.5
    idle_color "#908080"
    hover_color "#d4a050"
    selected_color "#d4a050"
    outlines [(1, "#000000aa", 1, 0)]


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()
            textbutton _("Journal") action ShowMenu("journal")


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

################################################################################
## HOSTEL EXPLORATION SCREEN
################################################################################

screen exploration_menu(location_name, current_time):
    modal True
    
    frame:
        xsize 400
        ysize 600
        xpos 50
        ypos 100
        background Frame("gui/button/choice_selected_background.png", 12, 12)
        
        vbox:
            spacing 15
            xfill True
            
            # Title and Time Display
            text location_name style "label_text" size 24 color "#ffffff"
            text "[current_time]" style "gui_text" size 20 color "#ffff99"
            
            # Empty space
            null height 20
            
            # Navigation Buttons
            textbutton "Go Back to Room":
                action Jump("go_to_room")
                style "button" text_style "button_text"
            
            textbutton "Go Outside":
                action Jump("go_outside_room")
                style "button" text_style "button_text"
            
            textbutton "Go to Bathroom":
                action Jump("go_bathroom")
                style "button" text_style "button_text"
            
            textbutton "Take a Shower":
                action Jump("take_shower")
                style "button" text_style "button_text"
            
            # Floor Navigation
            textbutton "Go to 1st Floor (Dining)":
                action Jump("go_to_floor_1")
                style "button" text_style "button_text"
            
            textbutton "Go to 2nd Floor":
                action Jump("go_to_floor_2")
                style "button" text_style "button_text"
            
            textbutton "Go to 4th Floor":
                action Jump("go_to_floor_4")
                style "button" text_style "button_text"
            
            textbutton "Go to Reception":
                action Jump("go_to_reception")
                style "button" text_style "button_text"
            
            # Action Buttons
            $ meal = game_time.get_meal_available()
            if meal:
                textbutton "Eat [meal.capitalize()]":
                    action Jump("eat_meal")
                    style "button" text_style "button_text"
            else:
                textbutton "Dining Area Closed (No meals available)":
                    action NullAction()
                    style "button" text_style "button_text"
            
            textbutton "Talk to Mayank (Reception)":
                action Jump("interact_with_mayank")
                style "button" text_style "button_text"
            
            textbutton "Rest in Room":
                action Jump("rest_in_room")
                style "button" text_style "button_text"


            
            # Action Buttons
            $ meal = game_time.get_meal_available()
            if meal:
                textbutton "Eat [meal.capitalize()]":
                    action [Function(game_time.advance_time, minutes=20 if meal == "breakfast" else 25 if meal == "lunch" else 30), Function(renpy.jump, "hostel_exploration")]
                    style "button" text_style "button_text"
            else:
                textbutton "Dining Area Closed (No meals available)":
                    action NullAction()
                    style "button" text_style "button_text"
            
            textbutton "Talk to Mayank (Reception)":
                action [SetVariable("current_location", "reception"), Function(game_time.advance_time, minutes=5), Function(renpy.jump, "hostel_exploration")]
                style "button" text_style "button_text"
            
            textbutton "Rest in Room":
                action [SetVariable("current_location", "room"), Function(game_time.advance_time, hours=1), Function(renpy.jump, "hostel_exploration")]
                style "button" text_style "button_text"