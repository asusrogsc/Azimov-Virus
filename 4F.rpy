# ============================================
# FLOOR 4 (TOP FLOOR)
# ============================================

label floor_4_show_description:
    $ bg_image = get_location_image("floor_4", game_time, character_meal_times)
    scene expression bg_image
    with fade
    x "I'm on the 4th floor. The top floor of the hostel. There are 7 rooms here."
    $ floor4_desc = "Room 404"
    $ floor4_desc += " (Mayank lives here)" if "mayank" in met_characters else " - the manager lives here"
    $ floor4_desc += "."
    x "[floor4_desc]"
    $ observation = get_characters_observation("floor_4", game_time, character_meal_times, character_water_times, character_door_open_times, met_characters)
    if observation:
        x "[observation]"
    return

label floor_4_show_menu:
    x "I'm on the 4th floor. There are 7 rooms here."
    
    menu:
        "Knock on Room 404" if "mayank" not in met_characters:
            call interact_mayank_room from _call_interact_mayank_room
        
        "Knock on Room 404 (Mayank)" if "mayank" in met_characters:
            call interact_mayank_room from _call_interact_mayank_room_1
        
        "Go to another floor":
            call explore_go_to_floor from _call_explore_go_to_floor_3
        
        "Go back to hallway":
            $ previous_location = current_location
            $ current_location = "hallway_3rd"
            $ game_time.advance_time(minutes=2)
            call check_for_interception from _call_check_for_interception_2
    
    return
