# ============================================
# FLOOR 1 (DINING & RECEPTION)
# ============================================

label floor_1_show_description:
    $ bg_image = get_location_image("floor_1", game_time, character_meal_times)
    scene expression bg_image
    with fade
    x "I'm on the 1st floor. The dining area and reception are here."
    $ observation = get_characters_observation("floor_1", game_time, character_meal_times, character_water_times, character_door_open_times, met_characters)
    if observation:
        x "[observation]"
    return

label reception_show_description:
    scene scene_madd_room_landlord_first_visit
    with fade
    x "I'm at the reception desk."
    return

label reception_show_menu:
    x "I'm at the reception. What would I like to do?"
    
    menu:
        "Talk to Mayank":
            $ mayank_in_reception = is_mayank_in_reception(game_time)
            if mayank_in_reception:
                x "I approach the reception desk."
                landlord_says "Oh, hello! What do you need?"
                x "Just checking in."
                landlord_says "Let me know if you need anything!"
            else:
                x "The reception is empty. Mayank is not here right now."
            $ game_time.advance_time(minutes=5)
        
        "Go back to floor":
            $ previous_location = current_location
            $ current_location = "floor_1"
    
    return

label tv_room_show_description:
    $ bg_image = get_location_image("floor_1", game_time, character_meal_times)
    scene expression bg_image
    with fade
    x "I'm in the TV room. There's a comfortable couch and a TV on the wall."
    return

label tv_room_show_menu:
    x "I'm in the TV room. What would I like to do?"
    
    menu:
        "Watch TV":
            show madd boy happy at left_small
            with dissolve
            x "I sit down and watch TV for a while."
            $ game_time.advance_time(minutes=30)
        
        "Go back to floor":
            $ previous_location = current_location
            $ current_location = "floor_1"
    
    return

label floor_1_show_menu:
    x "I'm on the 1st floor. The dining area and reception are here."
    
    menu:
        "Enter mess hall":
            call eat_at_mess_hall from _call_eat_at_mess_hall
            return
        
        "Visit Reception":
            $ previous_location = current_location
            $ current_location = "reception"
        
        "Visit TV Room":
            $ previous_location = current_location
            $ current_location = "tv_room"
        
        "Go to another floor":
            call explore_go_to_floor from _call_explore_go_to_floor
    
    return
