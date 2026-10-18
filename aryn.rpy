# ============================================
# ARYN CHARACTER INTERACTIONS
# ============================================

label interact_aryn_room:
    """Room interaction with Aryn (Room 307)"""
    $ bg_image = get_location_image("room", game_time, character_meal_times)
    scene expression bg_image
    with fade
    
    if "aryn" not in met_characters:
        $ met_characters.append("aryn")
        $ character_relations["aryn"]["friend"] += 10
        show madd boy cool at left_small
        with dissolve
        x "I knock on the door of Room 307."
        show aryn at right_small
        with dissolve
        aryn_says "Come in!"
        show madd boy try to dodge at left_small
        with dissolve
        x "Hi! I'm from Room 305 across from you. Thought I'd say hi."
        show aryn at right_small
        with dissolve
        aryn_says "Oh, hey! I'm Aryn. Great to meet you!"
        show madd boy happy at left_small
        with dissolve
        x "Great to meet you too!"
    else:
        $ character_relations["aryn"]["friend"] += 1
        show madd boy blush at left_small
        with dissolve
        x "I knock on Aryn's door."
        show aryn at right_small
        with dissolve
        aryn_says "Hey! How are you?"
        show madd boy happy at left_small
        with dissolve
        x "I'm good, just wanted to check in."
        show aryn at right_small
        with dissolve
        aryn_says "That's nice of you!"
    
    $ game_time.advance_time(minutes=5)
    return

label interact_aryn_mess_hall(meal):
    """Mess hall interaction with Aryn"""
    if "aryn" not in met_characters:
        $ met_characters.append("aryn")
        $ character_relations["aryn"]["friend"] += 5
        $ current_location = "floor_1"
    
    show madd boy think at left_small
    with dissolve
    x "I go over to Aryn."
    show aryn at right_small
    with dissolve
    aryn_says "Oh hi! I don't think we've met. I'm Aryn from Room 307."
    show madd boy blush at left_small
    with dissolve
    x "I'm [mainname]. Nice to meet you!"
    show aryn at right_small
    with dissolve
    aryn_says "Nice to meet you too! Welcome to the hostel!"
    show madd boy happy at left_small
    with dissolve
    x "Thanks! Good to meet you too!"
    
    $ game_time.advance_time(minutes=15)
    return

label water_cooler_intro_aryn:
    """First meeting at water cooler"""
    show aryn at right_small
    with dissolve
    x_says "Hi! I'm Madd, I just moved in upstairs."
    aryn_says "Hey! Nice to meet you!"
    show madd boy happy at left_small
    with dissolve
    x_says "Nice to meet you!"
    return

label water_cooler_talk_aryn:
    """Casual conversation with Aryn at water cooler (non-first meeting)"""
    show aryn at right_small
    with dissolve
    aryn_says "Oh, [mainname]! Hey! How's everything?"
    show madd boy happy at left_small
    with dissolve
    x "Pretty good! Just grabbing some water. You?"
    show aryn at right_small
    with dissolve
    aryn_says "Same here! It's always nice to see you around the place."
    show madd boy blush at left_small
    with dissolve
    x "Yeah, it's nice seeing you too."
    show aryn at right_small
    with dissolve
    aryn_says "I was actually thinking about organizing a small get-together for everyone in the rooms. You should come!"
    show madd boy happy at left_small
    with dissolve
    x "That sounds fun! I'd love to."
    show aryn at right_small
    with dissolve
    aryn_says "Great! I'll let you know when I'm planning it."
    $ character_relations["aryn"]["lust"] += 1
    $ character_relations["aryn"]["identity"] += 1
    $ madd_secret_identity = max(madd_secret_identity - 1, 0)
    return

label interact_aryn_mess_hall_met(meal):
    """Chat interaction with Aryn in mess hall (already met)"""
    scene scene_messhall_breakfast
    with fade
    show madd boy happy at left_small
    with dissolve
    x "I walk over to Aryn."
    show aryn at right_small
    with dissolve
    aryn_says "Oh, hey! I didn't expect to see you here!"
    show madd boy happy at left_small
    with dissolve
    x "Just grabbing a bite. Mind if I sit?"
    show aryn at right_small
    with dissolve
    aryn_says "Of course! Always happy to have company."
    show madd boy happy at left_small
    with dissolve
    x "How's your day going?"
    show aryn at right_small
    with dissolve
    aryn_says "Oh, you know, pretty busy. But talking to you makes it better!"
    show madd boy blush at left_small
    with dissolve
    x "Really? That's sweet."
    show aryn at right_small
    with dissolve
    aryn_says "Yeah! You're a good friend, you know that?"
    $ character_relations["aryn"]["friend"] += 1
    $ game_time.advance_time(minutes=20)
    return
