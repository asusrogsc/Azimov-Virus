# ============================================
# NICKS CHARACTER INTERACTIONS
# ============================================

label interact_nicks_room:
    """Room interaction with Nicks (Room 201)"""
    $ current_location = "nicks_room"
    call nicks_room_show_menu from _call_nicks_room_show_menu
    
    $ game_time.advance_time(minutes=5)
    return

label interact_nicks_mess_hall(meal):
    """Mess hall interaction with Nicks"""
    if "nicks" not in met_characters:
        $ met_characters.append("nicks")
        $ character_relations["nicks"]["friend"] += 5
        $ current_location = "floor_1"
    
    show madd boy think at left_small
    with dissolve
    x "I approach Nicks at the mess hall."
    show nicks grin evil smile at right_small
    with dissolve
    nicks_says "Oh look, another new kid. I'm Nicks from Room 201, the smartest person in this hostel by a wide margin."
    show madd boy blush at left_small
    with dissolve
    x "That's... quite a claim. I'm [mainname]."
    show nicks smirk at right_small
    with dissolve
    nicks_says "It's not a claim, it's simply fact. I aced every exam that mattered. But don't expect to understand the intellectual conversations I have with the truly gifted."
    show madd boy blush at left_small
    with dissolve
    x "I'll keep that in mind."
    show nicks laugh at right_small
    with dissolve
    nicks_says "Good. Now get out of my way. I have actual intellectual pursuits to attend to."
    
    $ game_time.advance_time(minutes=15)
    return

label intercept_nicks:
    """Interception scene with Nicks"""
    show nicks smirk at right_small
    with dissolve
    nicks_says "Hold on, [mainname]. Where are you running off to so quickly?"
    show madd boy flustered at left_small
    with dissolve
    x "O-Oh, Nicks! I was just..."
    show nicks evil smile at right_small
    with dissolve
    nicks_says "Just what? You seem flustered. Something the matter?"
    show madd boy blush at left_small
    with dissolve
    x "(I notice he's standing very close to me.)"
    show nicks laugh at right_small
    with dissolve
    nicks_says "You know, it's quite amusing how easy you are to read. Your reactions are so... transparent."
    show madd boy flustered at left_small
    with dissolve
    x "I-I'm not sure what you mean..."
    show nicks grin evil smile at right_small
    with dissolve
    nicks_says "Of course you're not. That's part of what makes it fun."
    show nicks laugh at right_small
    with dissolve
    nicks_says "Fine, fine. Go on. But remember this moment next time we meet."
    return

label water_bottle_witness_nicks:
    """Nicks witnesses water bottle cap drop"""
    show nicks lustful looks at right_small
    with dissolve
    nicks_says "Whoa! Did you see that?!"
    return

label water_cooler_intro_nicks:
    """First meeting at water cooler"""
    show nicks smile at right_small
    with dissolve
    x_says "Hi! I'm Madd, I just moved in upstairs."
    nicks_says "Hey! I'm Nicks. Nice to meet you!"
    show madd boy happy at left_small
    with dissolve
    x_says "Nice to meet you!"
    return

label water_cooler_talk_nicks:
    """Casual conversation with Nicks at water cooler (non-first meeting)"""
    show nicks smirk at right_small
    with dissolve
    nicks_says "Hey, [mainname]. How's the water cooler treating you?"
    show madd boy blush at left_small
    with dissolve
    x "Pretty good. You know how it is - just trying to stay hydrated."
    show nicks laugh at right_small
    with dissolve
    nicks_says "Yeah, that's one way to look at it. Though I've noticed you seem to be here quite often."
    show madd boy flustered at left_small
    with dissolve
    x "Is that a problem?"
    show nicks grin evil smile at right_small
    with dissolve
    nicks_says "Not at all. In fact, I find your predictability... amusing. Very predictable."
    show madd boy blush at left_small
    with dissolve
    x "(He's right. I do come here a lot.)"
    $ character_relations["nicks"]["lust"] += 2
    $ character_relations["nicks"]["identity"] += 1
    $ madd_secret_identity = max(madd_secret_identity - 1, 0)
    return

label interact_nicks_mess_hall_met(meal):
    """Chat interaction with Nicks in mess hall (already met)"""
    scene scene_messhall_breakfast
    with fade
    show madd boy blush at left_small
    with dissolve
    x "I walk over to Nicks."
    show nicks smirk at right_small
    with dissolve
    nicks_says "Ah, [mainname]. Come to benefit from my intellectual presence?"
    show madd boy blush at left_small
    with dissolve
    x "Just wanted to say hi..."
    show nicks laugh at right_small
    with dissolve
    nicks_says "Sure. Well, try not to ask me anything too complex. I'm enjoying my [meal]."
    $ character_relations["nicks"]["friend"] += 1
    $ game_time.advance_time(minutes=20)
    return


# ============================================
# NICKS ROOM LOCATIONS
# ============================================

label nicks_room_show_description:
    $ bg_image = get_location_image("room", game_time, character_meal_times)
    scene expression bg_image
    with fade
    x "I'm in Nicks' room (Room 201). It's quite neat with books and study materials everywhere."
    return

label nicks_room_show_menu:
    $ bg_image = get_location_image("room", game_time, character_meal_times)
    scene expression bg_image
    with fade
    
    if "nicks" not in met_characters:
        $ met_characters.append("nicks")
        $ character_relations["nicks"]["friend"] += 10
        show madd boy think at left_small
        with dissolve
        x "I knock on the door and Nicks answers."
        show nicks smile at right_small
        with dissolve
        nicks_says "Yeah, what is it?"
        show madd boy blush at left_small
        with dissolve
        x "I'm your neighbor from upstairs. Just wanted to say hi."
        show nicks smirk at right_small
        with dissolve
        nicks_says "Another new person, huh? Well, I'm Nicks. Try to keep up with the smart people around here, okay?"
        show madd boy blush at left_small
        with dissolve
        x "I'll... try my best."
        show nicks grin evil smile at right_small
        with dissolve
        nicks_says "Yeah, most people do. Let's see how long you last."
    else:
        $ character_relations["nicks"]["friend"] += 1
        show madd boy blush at left_small
        with dissolve
        x "I knock on Nicks' door."
        show nicks smile at right_small
        with dissolve
        nicks_says "What do you want?"
        show madd boy blush at left_small
        with dissolve
        x "Just wanted to chat for a bit."
        show nicks laugh at right_small
        with dissolve
        nicks_says "Sure, if you don't take too long."
    
    menu:
        "Leave the room":
            $ current_location = "floor_2"
            $ game_time.advance_time(minutes=1)
    
    return

label nicks_room_bathroom_show_description:
    $ bg_image = get_location_image("room", game_time, character_meal_times)
    scene expression bg_image
    with fade
    x "I'm in Nicks' bathroom. It's clean and organized."
    return

label nicks_room_bathroom_show_menu:
    x "I'm in Nicks' bathroom. What would I like to do?"
    
    menu:
        "Go back to room":
            $ current_location = "nicks_room"
    
    return
