# ============================================
# Intro Rocky
# ============================================

label rocky_intro:
    python:
        if game_time.is_morning():
            park_bg = "home_park_morning"
        elif game_time.is_afternoon():
            park_bg = "home_park_afternoon"
        elif game_time.is_evening():
            park_bg = "home_park_evening"
        else:  # night
            park_bg = "home_park_night"

    scene rockyintro
    with fade
    show dave happy
    x "Ah c'est Rocky"
    r "Yo Dave ! la forme ? merci d'être venus discutons..."
    x "Oui ca va, je t'écoute..."
    r "1"
    r "1"
    r "1"
    x "C'est vrai"
    r "1"
    x "2"
    r "1"
    $convrocky += 1
    call rocky_phone_intro2 from _call_rocky_phone_intro2
    jump outside_home
    

label rocky_talk:
    python:
        if game_time.is_morning():
            park_bg = "home_park_morning"
        elif game_time.is_afternoon():
            park_bg = "home_park_afternoon"
        elif game_time.is_evening():
            park_bg = "home_park_evening"
        else:  # night
            park_bg = "home_park_night"

    scene rockyintro
    with fade
    show dave happy
    x "Ah c'est Rocky"
    r "Yo Dave ! la forme ? tu te balades ?"
    x "Oui, je fais un tour."
    r "1"
    r "1"
    r "1"
    x "C'est vrai"
    r "1"
    x "2"
    r "1"
    call advance_time_and_check(minutes=10) 
    $convrocky += 1
    jump outside_home

label rocky_tier2:
    python:
        if game_time.is_morning():
            park_bg = "home_park_morning"
        elif game_time.is_afternoon():
            park_bg = "home_park_afternoon"
        elif game_time.is_evening():
            park_bg = "home_park_evening"
        else:  # night
            park_bg = "home_park_night"

    scene rockyintro
    with fade
    show dave happy
    x "Ah c'est Rocky"
    r "Yo Dave ! la forme ? peux tu chercher une autre meuf ?"
    x "Oui, bien sur."
    r "1"
    r "1"
    r "1"
    x "C'est vrai"
    r "1"
    x "2"
    r "1"
    $convrocky += 1
    call rocky_phone_save2 from _call_rocky_phone_save2
    jump outside_home

return