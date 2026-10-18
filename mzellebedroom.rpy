# ============================================
# FLOOR 1 mzelle
# ============================================

label mzellebedroom_door:
    python:
        if game_time.is_morning():
            mzellebedroomdoor = "mzellebedroomdoormor"
        elif game_time.is_afternoon():
            mzellebedroomdoor = "mzellebedroomdooraft"
        elif game_time.is_evening():
            mzellebedroomdoor = "mzellebedroomdooreve"
        else:  # night
            mzellebedroomdoor = "mzellebedroomdoornig"


    scene expression mzellebedroomdoor
    with fade
    if personnage_actuel == "Dave":
        show dave happy at left_small
    else:
        show madd violated at left_small
    with dissolve
    p "Voici la [nom_chambre_2], que faire?"
    menu:
                "Toquer":
                    if savemzelle == 0:
                        jump mzellebedroom_door_toquer_personne
                    else: 
                        jump mzellebedroom_door_toquer
                
                "Ouvrir doucement la porte":
                    if savemzelle == 0:
                        jump mzellebedroom_door_enter
                    elif savelindsay == 1 and game_time.hour == 7 and game_time.minute <= 20:
                        jump lindsdancebedroom
                    else:
                        jump mzellebedroom_door_enter_1

                "Attendre ici":
                    show madd think at left_small
                    with dissolve
                    p "Combien de temps ?"
                    menu:
                        "1 minute":
                            call advance_time_and_check(minutes=1)
                            jump mzellebedroom_door
                        "5 minutes":
                            call advance_time_and_check(minutes=5)
                            jump mzellebedroom_door
                        "15 minutes":
                            call advance_time_and_check(minutes=15)
                            jump mzellebedroom_door
                        "30 minutes":
                            call advance_time_and_check(minutes=30)
                            jump mzellebedroom_door
                        "1 heure":
                            call advance_time_and_check(minutes=60)
                            jump mzellebedroom_door
                        "3 heures":
                            call advance_time_and_check(minutes=180)
                            jump mzellebedroom_door
                        "6 heures":
                            call advance_time_and_check(minutes=360)
                            jump mzellebedroom_door
                        "12 heures":
                            call advance_time_and_check(minutes=720)
                            jump mzellebedroom_door
                        "Laisse tomber":
                            jump mzellebedroom_door
                        "Retourner au lobby":
                            jump home_areas
                "Lobby":
                    jump home_areas

return

label mzellebedroom_door_toquer_personne:

    scene mzellebedroomdoor
    with fade
    show madd happy at left_small
    with dissolve
    p "Il n'y a personne."
    jump mzellebedroom_door

return

label mzellebedroom_door_enter:
    python:
        if game_time.is_morning():
            mzellebedroomscene = "mzellebedroommor"
        elif game_time.is_afternoon():
            mzellebedroomscene = "mzellebedroomaft"
        elif game_time.is_evening():
            mzellebedroomscene = "mzellebedroomeve"
        else:  # night
            mzellebedroomscene = "mzellebedroomnig"


    scene expression mzellebedroomscene
    with fade
    show madd happy at left_small
    with dissolve
    p "Il n'y a personne."
    jump mzellebedroom_door

return

label mzellebedroom_door_enter_1:
    python:
        if game_time.is_morning():
            mzellebedroomscene = "mzellebedroommorning"
        elif game_time.is_afternoon():
            mzellebedroomscene = "mzellebedroomevening"
        elif game_time.is_evening():
            mzellebedroomscene = "mzellebedroomsoire"
        else:  # night
            mzellebedroomscene = "mzellebedroomnuit"

    scene expression mzellebedroomscene
    with fade
    show dave happy at left_small
    with dissolve
    p "Je regarde si mzelle est là..."
    menu:
        "Jouer" if game_time.is_night:
            jump mzellebedroom_sleeping
        "Retour":
            jump mzellebedroom_door

return

label mzellebedroom_sleeping:
    scene mzellebedroomsleep
    with fade
    show dave happy at left_small
    with dissolve
    p "Oh, mzelle est en train de dormir..."
    menu:
            "Rape":
                p "Oh oui"
                pause
                $ renpy.movie_cutscene("images/LindsayBedroom/Emy1.webm")
                jump mzellebedroom_door
            "Rape2":
                p "Oh oui"
                pause
                $ renpy.movie_cutscene("images/LindsayBedroom/Elenagilbert2.webm")
                jump mzellebedroom_door
return

