# ============================================
# MADD'S ROOM (305) INTERACTIONS
# ============================================

# Room location description
label maddroom_show_description:
    $ bg_image = get_location_image("room", game_time, character_meal_times)
    scene expression bg_image
    with fade
    
    # Transition: Change from boyish appearance to real appearance when entering room from different location
    if previous_location != "room":
        show madd boy cool at left_small
        with dissolve
        x "I lock the door behind me."
        x "Living a double life is so tiring..."
        
        show madd think at left_small
        with dissolve
        x "I take off my disguise and let my real self show."
        $ game_time.advance_time(minutes=10)
    
    x "I'm in my room on the 3rd floor (305)."
    $ observation = get_characters_observation("hallway_3rd", game_time, character_meal_times, character_water_times, character_door_open_times, met_characters)
    if observation:
        x "[observation]"
    return

# Room menu
label maddroom_show_menu:
    x "What would I like to do?"
    
    menu:
        "Go to Bathroom":
            $ previous_location = "room"
            $ current_location = "madds_bathroom"
            $ game_time.advance_time(minutes=2)
        
        "Go outside the room":
            show madd think at left_small
            with dissolve
            x "Alright, gotta change clothes and tie my hair up."
            
            show madd boy think at left_small
            with dissolve
            x "Time to go back to being a guy..."

            show madd boy try to dodge at left_small
            with dissolve
            x "Ugh, I can never get used to this."
            
            $ previous_location = current_location
            $ current_location = "hallway_3rd"
            $ game_time.advance_time(minutes=10)
            call check_for_interception from _call_check_for_interception_7
        
        "Study in room":
            show madd think at left_small
            with dissolve
            x "I study for a while and improve my focus."
            $ game_time.advance_time(minutes=45)
            $ previous_location = "room"
            $ current_location = "room"
        
        "Eat in room" if inventory:
            show madd happy at left_small
            with dissolve
            x "I eat from my stored food."
            $ inventory.pop()
            $ game_time.advance_time(minutes=15)
            $ previous_location = "room"
            $ current_location = "room"
        
        "Sleep till next day":
            call maddroom_sleep_till_next_day from _call_maddroom_sleep_till_next_day
        
        "Wait":
            call maddroom_wait from _call_maddroom_wait
    
    return

# Wait in room
label maddroom_wait:
    x "I decide to wait for a bit."
    menu:
        "Wait 5 minutes":
            $ game_time.advance_time(minutes=5)
            x "I've waited 5 minutes."
            $ previous_location = "room"
            $ current_location = "room"
        "Wait 30 minutes":
            $ game_time.advance_time(minutes=30)
            x "I've waited 30 minutes."
            $ previous_location = "room"
            $ current_location = "room"
        "Wait 1 hour":
            $ game_time.advance_time(hours=1, minutes=0)
            x "I've waited 1 hour."
            $ previous_location = "room"
            $ current_location = "room"
        "Wait 3 hours":
            $ game_time.advance_time(hours=3, minutes=0)
            x "I've waited 3 hours."
            $ previous_location = "room"
            $ current_location = "room"
        "Wait 6 hours":
            $ game_time.advance_time(hours=6, minutes=0)
            x "I've waited 6 hours."
            $ previous_location = "room"
            $ current_location = "room"
        "Never mind":
            pass
    return

# Sleep till next day
label maddroom_sleep_till_next_day:
    scene scene_305_madd_sleep
    with fade
    x "I lie down on the bed and fall asleep."
    x "..."
    
    python:
        # Advance to 7:00 AM next day
        game_time.hour = 7
        game_time.minute = 0
        days_passed += 1
        
        # Reset all daily variables
        dad_talk_today = False
        listen_to_dad_demands_today = False
        brother_talk_today = False
        aftb_talk_today = False
        last_dad_talk_hour = -1
        showered_today = False
        cooked_today = False
        dad_morning_knock_count = 0
        
        # Increase lust of all characters by 10, and Madd's lust by min(corruption, 20)
        for character in character_relations:
            character_relations[character]["lust"] += 10
        
        madd_lust += min(corruption, 20)
        
        # Increase willpower
        madd_willpower = min(madd_willpower + 50, madd_willpower_max)
        
        # Reset daily counters
        water_fills_today = 0
        interceptions_today = 0
        mayank_visited_today = False
    
    x "I already feel sleepy, so I sleep through the night."
    
    scene scene 305 morning
    with fade
    show madd stand at left_small
    with dissolve
    x "I wake up as sunlight streams through the window. It's a new day."
    $ previous_location = "room"
    $ current_location = "room"
    return

# Bathroom in Madd's room
label maddroom_bathroom_show_description:
    $ bg_image = get_location_image("room", game_time, character_meal_times)
    scene expression bg_image
    with fade
    show madd relieved at left_small
    with dissolve
    x "I'm in the bathroom. It's clean and quiet."
    $ observation = get_characters_observation("madds_bathroom", game_time, character_meal_times, character_water_times, character_door_open_times, met_characters)
    if observation:
        x "[observation]"
    return

label maddroom_bathroom_show_menu:
    x "What would I like to do?"
    show madd think at left_small  
    with dissolve

    menu:
        "Take a shower":
            python:
                shower_scene = renpy.random.choice(["scene madd bathroom shower solo1", "scene madd bathroom shower solo2"])
            scene expression shower_scene
            with fade
            x "I take a refreshing shower."
            show madd relieved at left_small
            with dissolve
            x " it feels so good to not have your step family watching you shower for once."
            show madd happy at left_small
            with dissolve
            x "I feel much better now."


            $ game_time.advance_time(minutes=15)
            $ previous_location = "room"
            $ current_location = "madds_bathroom"
        
        "Go back to room":
            $ previous_location = "room"
            $ current_location = "room"
            $ game_time.advance_time(minutes=1)
            call check_for_interception from _call_check_for_interception_8
    
    return
