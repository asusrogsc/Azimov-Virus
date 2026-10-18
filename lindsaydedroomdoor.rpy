# ============================================
# FLOOR 1 Lindsay
# ============================================

label lindsaybedroomdoor:

    scene lindsaybedroomdoor
    with fade
    show madd happy at left_small
    with dissolve
    x "Voici la chambre N1, que faire?"
    menu:
                "Toquer":
                    call advance_time_and_check(minutes=1) from _call_advance_time_and_check_59
                    jump outside_step_brother_room_scene
                
                "Ouvrir doucement la porte":
                    call advance_time_and_check(minutes=1) from _call_advance_time_and_check_60
                    jump outside_step_father_room_scene

                "Retourner au lobby":
                    jump home_areas

return
