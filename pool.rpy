# ============================================
# pool
# ============================================

label pool_scene:
    python:
        if game_time.is_morning():
            pool = "poolmor"
        elif game_time.is_afternoon():
            pool = "poolaft"
        elif game_time.is_evening():
            pool = "pooleve"
        else:  # night
            pool = "poolnig"
    
    scene expression pool
    with fade
    if personnage_actuel == "Dave":
        show dave happy at left_small
    else:
        show madd violated at left_small
    with dissolve
    p "Je n'ai rien a faire ici pour le moment."
    jump home_areas

label pool_lindsaypose:
    python:
        if game_time.is_morning():
            pool = "poolmor"
        elif game_time.is_afternoon():
            pool = "poolaft"
        elif game_time.is_evening():
            pool = "pooleve"
        else:  # night
            pool = "poolnig"

    scene expression pool
    with fade
    if personnage_actuel == "Dave":
        show dave happy at left_small
    else:
        show madd violated at left_small
    with dissolve
    p "Oh Lindsay est là !"
    scene lindsaypoolpose
    p "Elle test l'eau ou quoi ? xD"
    p "On fait quoi ?"
    menu:
        "Rester":
            scene lindsaypoolpose1
            p "Trop belle"
            jump home_areas
        "Retour":
            jump home_areas

    

label pool_mzellepose:
    python:
        if game_time.is_morning():
            pool = "poolmor"
        elif game_time.is_afternoon():
            pool = "poolaft"
        elif game_time.is_evening():
            pool = "pooleve"
        else:  # night
            pool = "poolnig"

    scene expression pool
    with fade
    if personnage_actuel == "Dave":
        show dave happy at left_small
    else:
        show madd violated at left_small
    with dissolve
    p "Oh Mzelle est là !"
    scene mzellepoolpose
    p "Elle se prépare à se reposer."
    p "On fait quoi ?"
    menu:
        "Rester":
            scene mzellepoolpose1
            p "Trop belle"
            jump home_areas
        "Retour":
            jump home_areas




