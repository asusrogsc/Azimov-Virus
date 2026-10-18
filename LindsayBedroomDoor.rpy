# ============================================
# FLOOR 1 Lindsay
# ============================================

label lindsaybedroom_door:
    python:
        if game_time.is_morning():
            lindsaybedroomdoor = "lindsaybedroomdoormor"
        elif game_time.is_afternoon():
            lindsaybedroomdoor = "lindsaybedroomdooraft"
        elif game_time.is_evening():
            lindsaybedroomdoor = "lindsaybedroomdooreve"
        else:  # night
            lindsaybedroomdoor = "lindsaybedroomdoornig"


    scene expression lindsaybedroomdoor
    with fade
    if personnage_actuel == "Dave":
        show dave happy at left_small
    else:
        show madd violated at left_small
    with dissolve
    p "Voici la [nom_chambre_1], que faire?"
    menu:
                "Toquer":
                    if savelindsay == 0:
                        jump lindsaybedroom_door_toquer_personne
                    else: 
                        jump lindsaybedroom_door_toquer
                
                "Ouvrir doucement la porte":
                    if savelindsay == 0:
                        jump lindsaybedroom_door_enter
                    elif savelindsay == 1 and game_time.hour == 7 and game_time.minute <= 20:
                        jump lindsdancebedroom
                    else:
                        jump lindsaybedroom_door_enter_1

                "Attendre ici":
                    show madd think at left_small
                    with dissolve
                    p "How long should I wait here?"
                    menu:
                        "1 minute":
                            call advance_time_and_check(minutes=1)
                            jump lindsaybedroom_door
                        "5 minutes":
                            call advance_time_and_check(minutes=5)
                            jump lindsaybedroom_door
                        "15 minutes":
                            call advance_time_and_check(minutes=15)
                            jump lindsaybedroom_door
                        "30 minutes":
                            call advance_time_and_check(minutes=30)
                            jump lindsaybedroom_door
                        "1 hour":
                            call advance_time_and_check(minutes=60)
                            jump lindsaybedroom_door
                        "3 hours":
                            call advance_time_and_check(minutes=180)
                            jump lindsaybedroom_door
                        "6 hours":
                            call advance_time_and_check(minutes=360)
                            jump lindsaybedroom_door
                        "12 hours":
                            call advance_time_and_check(minutes=720)
                            jump lindsaybedroom_door
                        "never mind":
                            jump lindsaybedroom_door
                        "Retourner au lobby":
                            jump home_areas
                "Lobby":
                    jump home_areas

return

label lindsaybedroom_door_toquer_personne:
    python:
        if game_time.is_morning():
            lindsaybedroomdoor = "lindsaybedroomdoormor"
        elif game_time.is_afternoon():
            lindsaybedroomdoor = "lindsaybedroomdooraft"
        elif game_time.is_evening():
            lindsaybedroomdoor = "lindsaybedroomdooreve"
        else:  # night
            lindsaybedroomdoor = "lindsaybedroomdoornig"

    scene expression lindsaybedroomdoor
    with fade
    if personnage_actuel == "Dave":
        show dave happy at left_small
    else:
        show madd violated at left_small
    with dissolve
    p "Il n'y a personne."
    jump lindsaybedroom_door

return

label lindsaybedroom_door_toquer:
    python:
        if game_time.is_morning():
            lindsaybedroomdoor = "lindsaybedroomdoormor"
        elif game_time.is_afternoon():
            lindsaybedroomdoor = "lindsaybedroomdooraft"
        elif game_time.is_evening():
            lindsaybedroomdoor = "lindsaybedroomdooreve"
        else:  # night
            lindsaybedroomdoor = "lindsaybedroomdoornig"

    scene expression lindsaybedroomdoor
    with fade
    if personnage_actuel == "Dave":
        show dave happy at left_small
    else:
        show madd violated at left_small
    with dissolve
    p "Lindsay ne répond pas."
    jump lindsaybedroom_door

return

label lindsaybedroom_door_enter:
    python:
        if game_time.is_morning():
            lindsaybedroomscene = "lindsaybedroommorning"
        elif game_time.is_afternoon():
            lindsaybedroomscene = "lindsaybedroomafternoon"
        elif game_time.is_evening():
            lindsaybedroomscene = "lindsaybedroomevening"
        else:  # night
            lindsaybedroomscene = "lindsaybedroomnig"


    scene expression lindsaybedroomscene
    with fade
    if personnage_actuel == "Dave":
        show dave happy at left_small
    else:
        show madd violated at left_small
    with dissolve
    p "Il n'y a personne."
    jump lindsaybedroom_door

return

label lindsaybedroom_door_enter_1:
    python:
        if game_time.is_morning():
            lindsaybedroomscene = "lindsaybedroommorning"
        elif game_time.is_afternoon():
            lindsaybedroomscene = "lindsaybedroomafternoon"
        elif game_time.is_evening():
            lindsaybedroomscene = "lindsaybedroomevening"
        else:  # night
            lindsaybedroomscene = "lindsaybedroomnuit"

    scene expression lindsaybedroomscene
    with fade
    if personnage_actuel == "Dave":
        show dave happy at left_small
    else:
        show madd violated at left_small
    with dissolve
    p "Je regarde si Lindsay est là..."
    if game_time.is_night():
        scene lindsaybedroomsleep
        p "Oh, Lindsay est en train de dormir..."
        menu:
            "Rester":
                jump lindsaybedroom_sleeping
            "Retour":
                jump lindsaybedroom_door
    elif personnage_actuel == "Dave" and getattr(persistent, 'linds_corruption', 0) >= 25:
        scene lindsaybedroomsleep
        p "Je peux plus me retenir..."
        menu:
            "Me rapprocher":
                jump lindsaybedroom_sleepingcorr25
            "Retour":
                jump lindsaybedroom_door
    else:
        p "La chambre est vide pour le moment."
        jump lindsaybedroom_door

return

label lindsaybedroom_sleeping:
    scene lindsaybedroomsleep
    with fade
        
        # Vérification du personnage actif pour afficher le bon sprite
    if personnage_actuel == "Dave":
        show dave happy at left_small
    else:
        show madd violated at left_small
            
    with dissolve
    p "Elle est tellement belle ..."
    
    menu:
            "Observer":
                p "Oh elle bouge"
                hide dave 
                with dissolve        
                $ liste_videos = ["images/LindsayBedroom/lindssleeping1.webm", "images/LindsayBedroom/lindssleeping2.webm", "images/LindsayBedroom/lindssleeping3.webm"]
                $ video_choisie = renpy.random.choice(liste_videos)
                $ renpy.movie_cutscene(video_choisie)
                if getattr(persistent, 'linds_corruption', 0) >= 5:
                    p "Que fait elle ? Oh.."
                    scene lindsaybedroomsleep
                    $ liste_videos = ["images/LindsayBedroom/lindssleeping4.webm", "images/LindsayBedroom/lindssleeping5.webm"]
                    $ video_choisie = renpy.random.choice(liste_videos)
                    $ renpy.movie_cutscene(video_choisie)
                    p "Elle à l'air de faire un rêve cochon.. :)"
                    jump lindsaybedroom_sleeping
                else:
                    p "Finis pour aujourd'hui !"
                    jump lindsaybedroom_door
                    
            "Profiter" if getattr(persistent, 'linds_corruption', 0) >= 10:
                scene lindsaybedroomsleep1
                p "Oh oui"
                hide dave 
                with dissolve
                $ liste_videos = ["images/LindsayBedroom/lindssleeping11.webm", "images/LindsayBedroom/lindssleeping12.webm", "images/LindsayBedroom/lindssleeping13.webm", "images/LindsayBedroom/lindssleeping14.webm"]
                $ video_choisie = renpy.random.choice(liste_videos)
                $ renpy.movie_cutscene(video_choisie)
                p "Dur dur de résister ..."
                jump lindsaybedroom_door

            "Se régaler" if getattr(persistent, 'linds_corruption', 0) >= 15:
                scene lindsaybedroomsleep2
                p "Oh oui"
                hide dave 
                scene black with dissolve
                $ liste_videos = ["images/LindsayBedroom/lindssleeping21.webm", "images/LindsayBedroom/lindssleeping22.webm", "images/LindsayBedroom/lindssleeping31.webm", "images/LindsayBedroom/lindssleeping32.webm", "images/LindsayBedroom/lindssleeping41.webm", "images/LindsayBedroom/lindssleeping42.webm", "images/LindsayBedroom/lindssleeping51.webm", "images/LindsayBedroom/lindssleeping52.webm"]
                $ video_choisie = renpy.random.choice(liste_videos)
                $ renpy.movie_cutscene(video_choisie)
                if video_choisie in ["images/LindsayBedroom/lindssleeping31.webm", "images/LindsayBedroom/lindssleeping32.webm"]:
                    scene lindsaybedroomsleep3
                    p "Dur dur de résister ..."
                    jump lindsaybedroom_door
                elif video_choisie in ["images/LindsayBedroom/lindssleeping41.webm", "images/LindsayBedroom/lindssleeping42.webm"]:
                    scene lindsaybedroomsleep4
                    p "Dur dur de résister ..."
                    jump lindsaybedroom_door
                elif video_choisie in ["images/LindsayBedroom/lindssleeping51.webm", "images/LindsayBedroom/lindssleeping52.webm"]:
                    scene lindsaybedroomsleep5
                    p "Dur dur de résister ..."
                    jump lindsaybedroom_door
                else:
                    scene lindsaybedroomsleep2
                    p "Dur dur de résister ..."
                    jump lindsaybedroom_door

            "Retour":
                jump lindsaybedroom_door
return

label lindsaybedroom_sleepingcorr25:
    scene lindsaybedroomsleep
    with fade
        
        # Vérification du personnage actif pour afficher le bon sprite
    if personnage_actuel == "Dave":
        show dave happy at left_small
    else:
        show madd violated at left_small
            
    with dissolve
    p "Impossible de résister..."
    
    menu:
            "Regarder":
                p "C'est partit !"
                hide dave 
                with dissolve        
                $ liste_videos = ["images/LindsayBedroom/lindssleeping4.webm", "images/LindsayBedroom/lindssleeping5.webm", "images/LindsayBedroom/lindssleeping6.webm"]
                $ video_choisie = renpy.random.choice(liste_videos)
                $ renpy.movie_cutscene(video_choisie)
               # if lindscorr >= 10:
                p "Elle se tourne..."
                scene lindsaybedroom_sleeping1
                $ liste_videos = ["images/LindsayBedroom/lindssleeping11.webm", "images/LindsayBedroom/lindssleeping12.webm", "images/LindsayBedroom/lindssleeping13.webm"]
                $ video_choisie = renpy.random.choice(liste_videos)
                $ renpy.movie_cutscene(video_choisie)
                p "Elle à l'air de faire un rêve cochon.. :)"
                jump lindsaybedroom_sleepingcorr15
               # else:
                   # jump lindsaybedroom_sleepingcorr15
            "Rape":
                p "Oh oui"
                pause
                $ renpy.movie_cutscene("images/LindsayBedroom/Emy1.webm")
                jump lindsaybedroom_door
            "Rape2":
                p "Oh oui"
                pause
                $ renpy.movie_cutscene("images/LindsayBedroom/Elenagilbert2.webm")
                jump lindsaybedroom_door
            "Retour":
                jump lindsaybedroom_door
return

label elenamovie:

    scene lindsaybedroommorning
    with fade
    show madd happy at left_small
    with dissolve
    p "oh my god"
    show elena_movie
    pause
    $ renpy.movie_cutscene("images/LindsayBedroom/Elenagilbert3.webm")
    jump lindsaybedroom_door

return

label rockypeeklindsbedroomntr:
    python:
        if game_time.is_morning():
            lindsaybedroomdoor = "lindsaybedroomdoormor"
        elif game_time.is_afternoon():
            lindsaybedroomdoor = "lindsaybedroomdooraft"
        elif game_time.is_evening():
            lindsaybedroomdoor = "lindsaybedroomdooreve"
        else:  # night
            lindsaybedroomdoor = "lindsaybedroomdoornig"

    scene expression lindsaybedroomdoor
    show dave stressed
    with fade
    if peekedbed != game_time.day:
        $davelust += 1
        $rockylust += 1
        $ peekedbed = game_time.day
        "Rocky? pourquoi regarde t'il dans sa chambre... AH, Lindsay y est !"
        show lindssleeping1
        "Votre excitation augmente."
        jump home_areas
    else:
        "Raah, il est encore là..."
        jump home_areas

label rockypeeklindsbedroom:
    python:
        if game_time.is_morning():
            lindsaybedroomdoor = "lindsaybedroomdoormor"
        elif game_time.is_afternoon():
            lindsaybedroomdoor = "lindsaybedroomdooraft"
        elif game_time.is_evening():
            lindsaybedroomdoor = "lindsaybedroomdooreve"
        else:  # night
            lindsaybedroomdoor = "lindsaybedroomdoornig"

    scene expression lindsaybedroomdoor
    with fade
    show dave stressed at left_small
    with dissolve
    p "J'en peux plus, il faut que j'aille voir Lindsay !"
    scene lindsaybedroomsleep
    with fade
    if peekedbed != game_time.day:
        $rockylust += 1
        $ peekedbed = game_time.day
        p "Elle est incroyable !"
        show lindssleeping1
        "Votre excitation augmente."
        jump home_areas

label lindsdancebedroom:
    python:
        if game_time.is_morning():
            lindsaybedroomscene = "lindsaybedroommorning"
        elif game_time.is_afternoon():
            lindsaybedroomscene = "lindsaybedroomevening"
        elif game_time.is_evening():
            lindsaybedroomscene = "lindsaybedroomsoire"
        else:  # night
            lindsaybedroomscene = "lindsaybedroomnuit"

    scene expression lindsaybedroomscene
    with fade
    p "Je rentre dans la chambre, Lindsay est réveillée."
    menu:
        "Observer":
            $ liste_videos = ["images/LindsayBedroom/lindsdancemor.webm", "images/LindsayBedroom/lindshairmor.webm"]
            $ video_choisie = renpy.random.choice(liste_videos)
            $ renpy.movie_cutscene(video_choisie)
            p "Une vrai Déesse..."
            jump lindsaybedroom_door
        "Parler":
            jump lindsaybedroom_door
        "Retour":
            jump lindsaybedroom_door