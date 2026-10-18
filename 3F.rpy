# ============================================
# FLOOR 3 (HALLWAY & ROOMS)
# ============================================

label floor_3_show_description:
    $ bg_image = get_location_image("hallway_3rd", game_time, character_meal_times)
    scene expression bg_image
    with fade
    x "I'm in the 3rd floor hallway. I can see rooms around me."
    $ hallway_desc = "Room 301"
    $ hallway_desc += " (Aman)" if "aman" in met_characters else ""
    $ hallway_desc += ", Room 306"
    $ hallway_desc += " (Abhi)" if "abhi" in met_characters else ""
    $ hallway_desc += " is next to mine, Room 307"
    $ hallway_desc += " (Aryn)" if "aryn" in met_characters else ""
    $ hallway_desc += " is across from Abhi." if "abhi" in met_characters else "."
    x "[hallway_desc]"
    $ observation = get_characters_observation("hallway_3rd", game_time, character_meal_times, character_water_times, character_door_open_times, met_characters)
    if observation:
        x "[observation]"
    return

label floor_3_show_menu:
    x "I'm in the 3rd floor hallway. What would I like to do?"
    
    menu:
        "Go back to my room":
            $ previous_location = current_location
            $ current_location = "room"
            $ game_time.advance_time(minutes=1)
        
        "Check out other rooms on the floor":
            call explore_floor_3_rooms from _call_explore_floor_3_rooms
        
        "Go to another floor":
            call explore_go_to_floor from _call_explore_go_to_floor_2
        
        "Wait":
            x "I decide to wait here for a bit."
            menu:
                "Wait 5 minutes":
                    $ game_time.advance_time(minutes=5)
                    x "I've waited 5 minutes in the hallway."
                "Wait 30 minutes":
                    $ game_time.advance_time(minutes=30)
                    x "I've waited 30 minutes in the hallway."
                "Wait 1 hour":
                    $ game_time.advance_time(hours=1, minutes=0)
                    x "I've waited 1 hour in the hallway."
                "Wait 3 hours":
                    $ game_time.advance_time(hours=3, minutes=0)
                    x "I've waited 3 hours in the hallway."
                "Wait 6 hours":
                    $ game_time.advance_time(hours=6, minutes=0)
                    x "I've waited 6 hours in the hallway."
                "Never mind":
                    pass
            $ game_time.advance_time(minutes=1)
            call check_for_interception from _call_check_for_interception_1
    
    return

label explore_floor_3_rooms:
    x "Which room would I like to check out?"
    
    menu:
        "Knock on Room 301" if "aman" not in met_characters:
            call interact_aman_room from _call_interact_aman_room
        
        "Knock on Room 301 (Aman)" if "aman" in met_characters:
            call interact_aman_room from _call_interact_aman_room_1
        
        "Knock on Room 306" if "abhi" not in met_characters:
            call interact_abhi_room from _call_interact_abhi_room
        
        "Knock on Room 306 (Abhi)" if "abhi" in met_characters:
            call interact_abhi_room from _call_interact_abhi_room_1
        
        "Knock on Room 307" if "aryn" not in met_characters:
            call interact_aryn_room from _call_interact_aryn_room
        
        "Knock on Room 307 (Aryn)" if "aryn" in met_characters:
            call interact_aryn_room from _call_interact_aryn_room_1
        
        "Return to previous choice":
            pass
    
    return
