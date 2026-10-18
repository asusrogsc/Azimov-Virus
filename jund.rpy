# ============================================
# JUND CHARACTER INTERACTIONS
# ============================================

label interact_jund_room:
    """Room interaction with Jund (Room 205)"""
    $ bg_image = get_location_image("room", game_time, character_meal_times)
    scene expression bg_image
    with fade
    
    if "jund" not in met_characters:
        $ met_characters.append("jund")
        $ character_relations["jund"]["friend"] += 10
        show madd boy cool at left_small
        with dissolve
        x "I knock on the door of Room 205."
        show jund at right_small
        with dissolve
        jund_says "Who is it?"
        show madd boy try to dodge at left_small
        with dissolve
        x "Hi, I'm from the 3rd floor. Thought I'd introduce myself."
        show jund at right_small
        with dissolve
        jund_says "Oh, welcome! I'm Jund. Nice to have you around."
        show madd boy happy at left_small
        with dissolve
        x "Thanks! Great to meet you."
    else:
        $ character_relations["jund"]["friend"] += 1
        show madd boy blush at left_small
        with dissolve
        x "I knock on Jund's door."
        show jund at right_small
        with dissolve
        jund_says "Hey there! What's up?"
        show madd boy happy at left_small
        with dissolve
        x "Just wanted to say hi."
        show jund at right_small
        with dissolve
        jund_says "Always good to see you!"
    
    $ game_time.advance_time(minutes=5)
    return

label interact_jund_mess_hall(meal):
    """Mess hall interaction with Jund"""
    if "jund" not in met_characters:
        $ met_characters.append("jund")
        $ character_relations["jund"]["friend"] += 5
        $ current_location = "floor_1"
    
    show madd boy think at left_small
    with dissolve
    x "I approach Jund."
    show jund at right_small
    with dissolve
    jund_says "Hey! New guy, right? I'm Jund."
    show madd boy blush at left_small
    with dissolve
    x "Yeah, I'm [mainname]. Room 305."
    show jund at right_small
    with dissolve
    jund_says "Cool, cool. Welcome aboard!"
    show madd boy happy at left_small
    with dissolve
    x "Thanks! Good to meet you!"
    
    $ game_time.advance_time(minutes=15)
    return

label water_bottle_witness_jund:
    """Jund witnesses water bottle cap drop"""
    show jund at right_small
    with dissolve
    jund_says "Nice view!"
    return

label water_cooler_intro_jund:
    """First meeting at water cooler"""
    show jund at right_small
    with dissolve
    x_says "Hi! I'm Madd, I just moved in upstairs."
    jund_says "Oh, hey! I'm Jund. Good to meet you!"
    show madd boy happy at left_small
    with dissolve
    x_says "Nice to meet you!"
    return

label water_cooler_talk_jund:
    """Casual conversation with Jund at water cooler (non-first meeting)"""
    show jund at right_small
    with dissolve
    jund_says "Hey, [mainname]! How's life treating you?"
    show madd boy happy at left_small
    with dissolve
    x "Pretty good! Just trying to settle in and get to know everyone."
    show jund at right_small
    with dissolve
    jund_says "That's cool, man. This place is pretty chill once you get used to it."
    show madd boy blush at left_small
    with dissolve
    x "Yeah, I'm starting to see that."
    show jund at right_small
    with dissolve
    jund_says "If you ever need anything or just want to hang out, just let me know. I'm always around."
    show madd boy happy at left_small
    with dissolve
    x "Thanks, I appreciate that."
    $ character_relations["jund"]["lust"] += 1
    $ character_relations["jund"]["identity"] += 1
    $ madd_secret_identity = max(madd_secret_identity - 1, 0)
    return

label interact_jund_mess_hall_met(meal):
    """Chat interaction with Jund in mess hall (already met)"""
    scene scene_messhall_breakfast
    with fade
    $ character_relations["jund"]["friend"] += 1
    show madd boy blush at left_small
    with dissolve
    x "I head over to Jund."
    show jund at right_small
    with dissolve
    jund_says "Hey! Come join us!"
    show madd boy happy at left_small
    with dissolve
    x "Sure!"
    $ game_time.advance_time(minutes=20)
    return

