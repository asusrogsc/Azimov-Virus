# ============================================
# ABHI CHARACTER INTERACTIONS
# ============================================

label interact_abhi_room:
    """Room interaction with Abhi (Room 306)"""
    $ bg_image = get_location_image("room", game_time, character_meal_times)
    scene expression bg_image
    with fade
    
    if "abhi" not in met_characters:
        $ met_characters.append("abhi")
        $ character_relations["abhi"]["friend"] += 10
        show madd boy cool at left_small
        with dissolve
        x "I knock on the door of Room 306."
        show abhi smile at right_small
        with dissolve
        abhi_says "Who is it?"
        show madd boy try to dodge at left_small
        with dissolve
        x "It's me from next door, Room 305. Wanted to introduce myself."
        show abhi smile wide at right_small
        with dissolve
        abhi_says "Oh hey! I'm Abhi! Nice to finally meet you!"
        show madd boy happy at left_small
        with dissolve
        x "Nice to meet you too!"
    else:
        $ character_relations["abhi"]["friend"] += 1
        show madd boy blush at left_small
        with dissolve
        x "I knock on Abhi's door."
        show abhi smirk at right_small
        with dissolve
        abhi_says "Hey neighbor! What's up?"
        show madd boy happy at left_small
        with dissolve
        x "Just wanted to hang out for a bit."
        show abhi laugh at right_small
        with dissolve
        abhi_says "Always good to see you!"
    
    $ game_time.advance_time(minutes=5)
    return

label interact_abhi_mess_hall(meal):
    """Mess hall interaction with Abhi"""
    if "abhi" not in met_characters:
        $ met_characters.append("abhi")
        $ character_relations["abhi"]["friend"] += 5
        $ current_location = "floor_1"
    
    show madd boy think at left_small
    with dissolve
    x "I head over to Abhi."
    show abhi smile at right_small
    with dissolve
    abhi_says "Hey there! I'm Abhi from Room 306. You new?"
    show madd boy blush at left_small
    with dissolve
    x "Yeah, I'm [mainname]. Room 305."
    show abhi wide smile at right_small
    with dissolve
    abhi_says "Oh nice, you're right next to me! Welcome!"
    show madd boy happy at left_small
    with dissolve
    x "Thanks! Great to meet you!"
    show abhi smirk at right_small
    with dissolve
    abhi_says "Same! Maybe we'll hang out sometime."
    
    $ game_time.advance_time(minutes=15)
    return

label water_cooler_intro_abhi:
    """First meeting at water cooler"""
    show abhi smile at right_small
    with dissolve
    x_says "Hi! I'm Madd, I just moved in upstairs."
    abhi_says "Hey! I'm Abhi. Nice to meet you!"
    show madd boy happy at left_small
    with dissolve
    x_says "Nice to meet you!"
    return

label water_cooler_talk_abhi:
    """Casual conversation with Abhi at water cooler (non-first meeting)"""
    show abhi smile at right_small
    with dissolve
    abhi_says "Hey, [mainname]! Keeping hydrated?"
    show madd boy happy at left_small
    with dissolve
    x "Yeah, just refilling. You too?"
    show abhi smirk at right_small
    with dissolve
    abhi_says "You know it! The water cooler is the best place to take a break and chat for a bit."
    show madd boy blush at left_small
    with dissolve
    x "Yeah, I've noticed I come here pretty often."
    show abhi laugh at right_small
    with dissolve
    abhi_says "Nothing wrong with that! Keeps you healthy. So, how are you adjusting to the place?"
    show madd boy happy at left_small
    with dissolve
    x "Pretty well, actually. Everyone's been pretty nice."
    show abhi smile at right_small
    with dissolve
    abhi_says "That's good to hear! If you ever need anything or just want to hang out, just knock on my door!"
    $ character_relations["abhi"]["lust"] += 1
    $ character_relations["abhi"]["identity"] += 1
    $ madd_secret_identity = max(madd_secret_identity - 1, 0)
    return

label interact_abhi_mess_hall_met(meal):
    """Chat interaction with Abhi in mess hall (already met)"""
    scene scene_messhall_breakfast
    with fade
    show madd boy happy at left_small
    with dissolve
    x "I walk over to Abhi."
    show abhi smile at right_small
    with dissolve
    abhi_says "Hey! Come to join me for a meal?"
    show madd boy happy at left_small
    with dissolve
    x "Yeah, thought I'd say hi."
    show abhi laugh at right_small
    with dissolve
    abhi_says "Awesome! Pull up a chair. I was just thinking about how boring it gets eating alone."
    show madd boy blush at left_small
    with dissolve
    x "Well, you won't be alone anymore!"
    show abhi smirk at right_small
    with dissolve
    abhi_says "Great! So how's your day been treating you?"
    show madd boy happy at left_small
    with dissolve
    x "Pretty good, actually. Better now that I'm hanging out with you."
    show abhi smile at right_small
    with dissolve
    abhi_says "Aw, thanks buddy! That means a lot."
    $ character_relations["abhi"]["friend"] += 1
    $ game_time.advance_time(minutes=20)
    return
