# ============================================
# Office
# ============================================

label office_scene:
    python:
        if game_time.is_morning():
            office = "officemor"
        elif game_time.is_afternoon():
            office = "officeaft"
        elif game_time.is_evening():
            office = "officeeve"
        else:  # night
            office = "officenig"
    
    scene expression office
    with fade
    if personnage_actuel == "Dave":
        show dave happy at left_small
    else:
        show madd violated at left_small
    with dissolve

    menu:
        "Aller sur le pc et étudier" if personnage_actuel == "Dave":
            jump research_cram_schools
     
        "Mission: Sauvetage 1" if convrocky == 1 and checkinfos == 1 and savelindsay == 0 and personnage_actuel == "Dave":
            jump lindsay_save

        "Mission: Sauvetage 2" if convrocky == 3 and checkinfos == 3 and savemzelle == 0 and personnage_actuel == "Dave":
            jump mzelle_save

        "Attendre ici":
            show madd think at left_small
            with dissolve
            x "How long should I wait here?"
            menu:
                "1 minute":
                    $ game_time.advance_time(minutes=1)
                    jump my_room_scene
                "5 minutes":
                    $ game_time.advance_time(minutes=5)
                    jump my_room_scene
                "15 minutes":
                    $ game_time.advance_time(minutes=15)
                    jump my_room_scene
                "30 minutes":
                    $ game_time.advance_time(minutes=30)
                    jump my_room_scene
                "1 heure":
                    $ game_time.advance_time(minutes=60)
                    jump my_room_scene
                "3 heures":
                    $ game_time.advance_time(minutes=180)
                    jump my_room_scene
                "6 heures":
                    $ game_time.advance_time(minutes=360)
                    jump my_room_scene
                "12 heures":
                    $ game_time.advance_time(minutes=720)
                    jump my_room_scene
        
        "Retour au lobby":
            jump home_areas

