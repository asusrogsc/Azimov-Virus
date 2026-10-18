# ============================================
# FLOOR 2 (ROOMS & WATER COOLER)
# ============================================

label floor_2_show_description:
    $ bg_image = get_location_image("floor_2", game_time, character_meal_times)
    scene expression bg_image
    with fade
    x "I'm on the 2nd floor. There are 7 rooms here and a water cooler."
    $ floor2_desc = "Room 201"
    $ floor2_desc += " (Nicks)" if "nicks" in met_characters else ""
    $ floor2_desc += " - has a water cooler outside, Room 202"
    $ floor2_desc += " (Roman)" if "roman" in met_characters else ""
    $ floor2_desc += ", Room 204"
    $ floor2_desc += " (Aftb)" if "aftb" in met_characters else ""
    $ floor2_desc += ", Room 205"
    $ floor2_desc += " (Jund)" if "jund" in met_characters else ""
    $ floor2_desc += ", Room 207"
    $ floor2_desc += " (Shas)" if "shas" in met_characters else ""
    $ floor2_desc += "."
    x "[floor2_desc]"
    $ observation = get_characters_observation("floor_2", game_time, character_meal_times, character_water_times, character_door_open_times, met_characters)
    if observation:
        x "[observation]"
    return

label floor_2_show_menu:
    $ character_outside = get_character_outside_door(game_time, character_door_open_times)
    
    menu:
        "Talk to [character_outside.capitalize()]" if character_outside and character_outside not in met_characters:
            if character_outside == "nicks":
                call interact_nicks_room from _call_interact_nicks_room
            elif character_outside == "roman":
                call interact_roman_room from _call_interact_roman_room
            elif character_outside == "aftb":
                call interact_aftb_room from _call_interact_aftb_room
            elif character_outside == "jund":
                call interact_jund_room from _call_interact_jund_room
            elif character_outside == "shas":
                call interact_shas_room from _call_interact_shas_room
        
        "Chat with [character_outside.capitalize()]" if character_outside and character_outside in met_characters:
            if character_outside == "nicks":
                call interact_nicks_room from _call_interact_nicks_room_1
            elif character_outside == "roman":
                call interact_roman_room from _call_interact_roman_room_1
            elif character_outside == "aftb":
                call interact_aftb_room from _call_interact_aftb_room_1
            elif character_outside == "jund":
                call interact_jund_room from _call_interact_jund_room_1
            elif character_outside == "shas":
                call interact_shas_room from _call_interact_shas_room_1
        
        "Check out other rooms on the floor":
            call explore_floor_2_rooms from _call_explore_floor_2_rooms
        
        "Fill water bottle - You've already filled twice today" if water_fills_today >= 2:
            show madd boy think at left_small
            with dissolve
            x "I've already filled my water bottle twice today. I should come back tomorrow."
        
        "Fill water bottle" if water_fills_today < 2:
            call floor_2_water_cooler_event from _call_floor_2_water_cooler_event
        
        "Go to another floor":
            call explore_go_to_floor from _call_explore_go_to_floor_1
        
        "Go back to hallway":
            $ previous_location = current_location
            $ current_location = "hallway_3rd"
            $ game_time.advance_time(minutes=2)
            call check_for_interception from _call_check_for_interception
    
    return

label explore_floor_2_rooms:
    x "Which room would I like to check out?"
    
    menu:
        "Knock on Room 201" if "nicks" not in met_characters:
            call interact_nicks_room from _call_interact_nicks_room_2
        
        "Knock on Room 201 (Nicks)" if "nicks" in met_characters:
            call interact_nicks_room from _call_interact_nicks_room_3
        
        "Knock on Room 202" if "roman" not in met_characters:
            call interact_roman_room from _call_interact_roman_room_2
        
        "Knock on Room 202 (Roman)" if "roman" in met_characters:
            call interact_roman_room from _call_interact_roman_room_3
        
        "Knock on Room 204" if "aftb" not in met_characters:
            call interact_aftb_room from _call_interact_aftb_room_2
        
        "Knock on Room 204 (Aftb)" if "aftb" in met_characters:
            call interact_aftb_room from _call_interact_aftb_room_3
        
        "Knock on Room 205" if "jund" not in met_characters:
            call interact_jund_room from _call_interact_jund_room_2
        
        "Knock on Room 205 (Jund)" if "jund" in met_characters:
            call interact_jund_room from _call_interact_jund_room_3
        
        "Knock on Room 207" if "shas" not in met_characters:
            call interact_shas_room from _call_interact_shas_room_2
        
        "Knock on Room 207 (Shas)" if "shas" in met_characters:
            call interact_shas_room from _call_interact_shas_room_3
        
        "Return to previous choice":
            pass
    
    return

label floor_2_water_cooler_event:
    """Handle water cooler and water bottle filling event on Floor 2"""
    $ characters_at_cooler = get_character_at_water_cooler(game_time, character_water_times)
    $ characters_outside_door = get_all_characters_outside_door(game_time, character_door_open_times)
    $ bottle_cap_drops = renpy.random.random() < (30 + madd_lust)/100.0 # 30% base chance + lust modifier
    
    python:
        # Check if it's a new day and reset counter
        if game_time.hour < last_water_fill_hour and last_water_fill_hour != -1:
            water_fills_today = 0
    
    show madd boy think at left_small
    with dissolve
    x "I go to fill my water bottle at the cooler."
    
    python:
        # Build witness list
        witnesses = []
        if characters_at_cooler:
            witnesses.extend(characters_at_cooler)
        if characters_outside_door:
            witnesses.extend(characters_outside_door)
        witnesses = list(set(witnesses))
    
    if bottle_cap_drops:
        # Bottle cap drops
        show madd boy flustered at left_small
        with dissolve
        x "Suddenly, the bottle cap slips from my hand and falls to the floor."
        scene scene_madd_boy_drop_bottle_cap
        with dissolve
        show madd boy drop bottle cap at left_small
        with dissolve
        show madd boy salivating at left_small
        with dissolve
        x "Oh no! My butt is showing when I bend down to pick it up!"
        
        if witnesses:
            $ secret_identity -= 1
            python:
                for witness in witnesses:
                    character_relations[witness]["lust"] += 4
                    character_relations[witness]["identity"] += 1
            
            # Pick a random witness
            $ chosen_witness = renpy.random.choice(witnesses)
            
            # Call specific witness event if met, otherwise call voices event
            if chosen_witness in met_characters:
                $ renpy.call("water_bottle_witness_" + chosen_witness)
            else:
                call water_bottle_witness_voices from _call_water_bottle_witness_voices
        else:
            x "I quickly pick it up, hoping no one saw that embarrassing moment."
        
        hide madd boy drop bottle cap
        show madd boy blush at left_small
        with dissolve
        
        # Check for unmet and met witnesses who saw the embarrassing moment
        python:
            unmet_witnesses = [w for w in witnesses if w not in met_characters]
            met_witnesses = [w for w in witnesses if w in met_characters]
        
        if unmet_witnesses or met_witnesses:
            x " What should I do?"
            menu:
                "Introduce myself" if unmet_witnesses:
                    call floor_2_water_bottle_introduce_myself from _call_floor_2_water_bottle_introduce_myself
                "Talk to them" if met_witnesses:
                    if len(met_witnesses) == 1:
                        $ witness_to_talk = met_witnesses[0]
                        $ renpy.call("water_cooler_talk_" + witness_to_talk)
                    else:
                        x "Which one of them should I talk to?"
                        python:
                            witness_to_talk = met_witnesses[0]
                            for char_name in met_witnesses[1:]:
                                if char_name < witness_to_talk:
                                    witness_to_talk = char_name
                        x "I'll talk to [witness_to_talk.capitalize()]."
                        $ renpy.call("water_cooler_talk_" + witness_to_talk)
                "Ignore them":
                    show madd boy crossarmed at left_small
                    with dissolve
                    x "I pretend I don't notice them watching and quickly leave."
        
        $ game_time.advance_time(minutes=3)
        $ water_bottle_full = True
        $ water_fills_today += 1
        $ last_water_fill_hour = game_time.hour
    else:
        # Normal water bottle filling
        if characters_at_cooler:
            if len(characters_at_cooler) == 1:
                $ char_name = characters_at_cooler[0]
                show madd boy blush at left_small
                with dissolve
                x "Oh, [char_name.capitalize()] is here too!"
                if char_name not in met_characters:
                    $ met_characters.append(char_name)
                    $ character_relations[char_name]["friend"] += 5
                    show madd boy blush at left_small
                    with dissolve
                    x "(Since we're both here, I introduce myself.)"
                    menu :
                        "Introduce myself":
                            $ renpy.call("water_cooler_intro_" + char_name)
                        "Just fill water bottle":
                            pass    
                else:
                    # Already met, offer to talk
                    menu:
                        "Talk to them":
                            $ renpy.call("water_cooler_talk_" + char_name)
                        "Just fill water bottle":
                            pass
            else:
                show madd boy smile at left_small
                with dissolve
                x "Oh, I see [', '.join([c.capitalize() for c in characters_at_cooler])] here at the cooler!"
                python:
                    for char_name in characters_at_cooler:
                        if char_name not in met_characters:
                            met_characters.append(char_name)
                            character_relations[char_name]["friend"] += 5
                
                # Check which ones are already met
                python:
                    already_met_at_cooler = [c for c in characters_at_cooler if c in met_characters]
                
                if already_met_at_cooler:
                    x "I've already met some of them. Should I talk to anyone?"
                    $ char_talk = already_met_at_cooler[0]
                    x "I'll talk to [char_talk.capitalize()]."
                    $ renpy.call("water_cooler_talk_" + char_talk)
        else:
            show madd boy think at left_small
            with dissolve
            x "No one else is here right now."
        
        $ game_time.advance_time(minutes=5)
        $ water_bottle_full = True
        $ water_fills_today += 1
        $ last_water_fill_hour = game_time.hour
    
    return

label water_bottle_witness_voices:
    """Madd hears unknown voices commenting on her while bent over picking up bottle cap"""
    show madd boy drop bottle cap at left_small
    with dissolve
    x "(As I'm bent over picking up the cap, I hear voices behind me...)"
    show madd boy flustered at left_small
    with dissolve
    x "(But I can't see who's talking. Are they... talking about me?)"
    
    # Voice 1
    x "(Voice): This dude's butt is so big..."
    show madd boy blush at left_small
    with dissolve
    x "(My face burns. I freeze, unable to move. Who said that?)"
    
    # Voice 2
    x "(Voice): Seriously... if I could, I would pull those pants down right now."
    show madd boy flustered at left_small
    with dissolve
    x "(W-what?! My heart is pounding in my chest. I can't believe what I'm hearing.)"
    
    # Voice 3
    x "(Voice): Slapping that butt would be such a good experience..."
    show madd boy embarrassed at left_small
    with dissolve
    x "(Oh my god... oh my god... this is so embarrassing. I'm still bent over and they're just... talking about my body like I'm not even here.)"
    show madd boy salivating at left_small
    with dissolve
    x "(I should stand up and leave, but my legs feel weak. What is happening to me? Why am I feeling... this way?)"
    show madd boy flustered at left_small
    with dissolve
    
    x "(I slowly straighten up, keeping my eyes down, not daring to look behind me.)"
    show madd boy blush at left_small
    with dissolve
    x "(I can feel their eyes on me as I hurry away, my skin burning with a mixture of shame and... something else.)"
    show madd boy nervous at left_small
    with dissolve
    x "(Who were they? I didn't recognize any of those voices...)"
    show madd boy thinking at left_small
    with dissolve
    x "(But now I know they're out there, and they were looking at me... like that.)"
    
    $ secret_identity -= 2
    $ corruption += 0.5
    $ madd_lust += 2
    
    return

label floor_2_water_bottle_introduce_myself:
    """Introduce myself after water bottle cap drop - calls water_cooler_intro for the witness"""
    show madd boy relieved at left_small
    with dissolve
    x "(Well, since they saw that, I might as well introduce myself.)"
    show madd boy smile at left_small
    with dissolve
    x "(God this is gonna be so embarrassing...)"
    python:
        for char_name in unmet_witnesses:
            met_characters.append(char_name)
            character_relations[char_name]["friend"] += 5
    
    if unmet_witnesses:
        $ char_name = unmet_witnesses[0]
        
        # Call the water cooler intro for this character
        $ renpy.call("water_cooler_intro_" + char_name)
    
    return
