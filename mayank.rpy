# ============================================
# MAYANK CHARACTER INTERACTIONS
# ============================================

label interact_mayank_room:
    """Room interaction with Mayank (Room 404 - Manager)"""
    scene scene_room_owners
    with fade
    
    if "mayank" not in met_characters:
        $ met_characters.append("mayank")
        $ character_relations["mayank"]["friend"] += 10
        show madd boy cool at left_small
        with dissolve
        x "I knock on the door of Room 404."
        show landlord smile wide at right_small
        with dissolve
        landlord_says "Come in!"
        show madd boy try to dodge at left_small
        with dissolve
        x "Hi Mayank, just thought I'd come by."
        show landlord happy at right_small
        with dissolve
        landlord_says "Oh, nice of you to visit! Make yourself at home."
        show madd boy happy at left_small
        with dissolve
        x "Thanks! Enjoying managing the hostel?"
        show landlord laugh at right_small
        with dissolve
        landlord_says "It keeps me busy, but I love it!"
    else:
        $ character_relations["mayank"]["friend"] += 1
        show madd boy blush at left_small
        with dissolve
        x "I knock on Mayank's door."
        show landlord smile wide at right_small
        with dissolve
        landlord_says "Hey! Good to see you. Everything okay?"
        show madd boy happy at left_small
        with dissolve
        x "Yeah, all good. Just wanted to check in."
        show landlord smile wide at right_small
        with dissolve
        landlord_says "That's great! Let me know if you need anything."
    
    $ game_time.advance_time(minutes=5)
    return
label check_mayank_visit:
    """
    Check if Mayank should visit Madd while waiting in the mess hall.
    """
    if should_mayank_visit(game_time):
        call mayank_visits_kitchen from _call_mayank_visits_kitchen
    return

label mayank_visits_kitchen:
    """
    Scene where Mayank visits Madd in the mess hall/kitchen during non-meal hours.
    """
    show madd boy cool at left_small
    with dissolve
    x "I'm sitting here relaxing when I hear footsteps approaching."
    
    show landlord smile wide at right_small
    with dissolve
    landlord_says "Ah, [mainname]! What are you doing out here at this hour?"
    
    show madd boy embarassed at left_small
    with dissolve
    x "M-Mayank! I was just... waiting around. Thought I might grab something later when the kitchen opens."
    
    show landlord laugh at right_small
    with dissolve
    landlord_says "Always thinking ahead, I see. That's good. The hostel needs residents who think responsibly about their meals."
    
    show madd boy happy at left_small
    with dissolve
    x "I try my best."
    
    show landlord smile wide at right_small
    with dissolve
    landlord_says "You know, it's nice to see you taking care of yourself. Most new residents just wander around aimlessly. You seem different."
    
    show madd boy blush at left_small
    with dissolve
    x "T-Thank you, sir. That's nice of you to say."

    show landlord evil smirk at right_small
    with dissolve
    landlord_says "well you certainly need to eat more , considering your... slender figure."
    show madd boy embarassed at left_small
    with dissolve
    x "(His eyes linger on me a bit longer than comfortable.)"
    show landlord smile wide at right_small
    with dissolve
    landlord_says "Don't worry, [mainname]. We'll make sure you get plenty of nutritious meals here. Just keep up the good work."
    show madd boy happy at left_small
    with dissolve
    x "I will, Sir. Thanks for looking out for me."

    
    show landlord happy at right_small
    with dissolve
    landlord_says "Keep it up. And don't hesitate to ask if you need anything from the management. That's what I'm here for."
    
    show madd boy happy at left_small
    with dissolve
    x "I will. Thank you, Mayank."
    
    # Update relationship
    $ character_relations["mayank"]["friend"] += 2
    $ character_relations["mayank"]["dominance"] += 1
    $ madd_dominance -= 0.5
    
    # Mark that Mayank visited today
    $ mayank_visited_today = True
    $ last_mayank_visit_hour = game_time.hour
    
    show landlord smile wide at right_small
    with dissolve
    landlord_says "Well, I should get back to the reception. See you around, [mainname]."
    
    hide landlord
    with dissolve
    
    show madd boy happy at left_small
    with dissolve
    x "That was unexpected, but... nice."
    
    $ game_time.advance_time(minutes=5)
    return

label check_if_mayank_in_room:
    """
    Check if Mayank is in his room (reception schedule check).
    If he's there, initiate interaction. Otherwise show he's not there.
    """
    $ mayank_in_room = is_mayank_in_reception(game_time)
    
    if mayank_in_room:
        # Mayank is at reception, not in his room
        x "I head to Mayank's room to find him."
        x "The room is empty. It seems Mayank is at the reception desk right now."
    else:
        # Mayank is likely in his room (after 16:00 or before 9:00)
        x "I knock on Mayank's door at Room 404."
        show landlord smile wide at right_small
        with dissolve
        landlord_says "Oh, hello [mainname]! Come in, come in!"
        call interact_mayank_room from _call_interact_mayank_room_2
    
    $ game_time.advance_time(minutes=5)
    return
