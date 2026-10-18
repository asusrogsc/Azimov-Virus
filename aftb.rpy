# ============================================
# AFTB CHARACTER INTERACTIONS
# ============================================

label interact_aftb_room:
    """Room interaction with Aftb (Room 204)"""
    # Initialize aftb_talk_today if it doesn't exist
    if aftb_talk_today not in dir():
        $ aftb_talk_today = False
    
    # Reset daily counter if it's a new day
    if game_time.hour < last_aftb_talk_hour and last_aftb_talk_hour != -1:
        $ aftb_talk_today = False
    
    $ bg_image = get_location_image("room", game_time, character_meal_times)
    scene expression bg_image
    with fade
    
    if "aftb" not in met_characters:
        $ met_characters.append("aftb")
        $ character_relations["aftb"]["friend"] += 10
        show madd boy nervous at left_small
        with dissolve
        x "I knock on the door of Room 204."
        show aftb evil smirk at right_small
        with dissolve
        aftb_says "Yeah?"
        show madd boy shocked at left_small
        with dissolve
        x "Hey, I'm from upstairs. Just wanted to meet you."
        show aftb bite lips smile at right_small
        with dissolve
        aftb_says "Well, well. Another small guy trying to fit in around here. I'm Aftb. I'm sure you've noticed I'm built different."
        show madd boy blush at left_small
        with dissolve
        x "I... yeah, you look tall and seem strong."
        show aftb laugh at right_small
        with dissolve
        aftb_says "Damn right I am. Don't cause problems and we'll get along just fine. Got it?"
        show madd boy blush at left_small
        with dissolve
        x "Y-yes. I'll be careful."
        show aftb smirk at right_small
        with dissolve
        aftb_says "Also one more thing... I might be strong but I need help with my studies from time to time. So don't be surprised if I ask you for help now and then."
        show madd boy relieved at left_small
        with dissolve
        x "Oh, sure! I'd be happy to help."
        aftb_says "What did you say your room number was again?"
        show aftb smile at right_small
        with dissolve
        x "305."
        show aftb laugh at right_small
        with dissolve
        aftb_says "305, huh? I'll be sure to drop by sometime for that help. Well after cram school starts of course."
        show madd boy flustered at left_small
        with dissolve
        x "Great! Looking forward to it."
    else:
        $ character_relations["aftb"]["friend"] += 1
        $ bg_image = get_location_image("room", game_time, character_meal_times)
        scene expression bg_image
        with fade
        
        show madd boy blush at left_small
        with dissolve
        x "I knock on Aftb's door."
        show aftb smile at right_small
        with dissolve
        aftb_says "What's up?"
        show madd boy blush at left_small
        with dissolve
        x "Just wanted to check in on you."
        show aftb laugh at right_small
        with dissolve
        aftb_says "Still stronger than you, I'm sure."
        show madd boy blush at left_small
        with dissolve
        x "of that there's no doubt."
        show aftb smirk at right_small
        with dissolve
        x " ( he quickly glances down at my chest ) "
        show aftb bite lips smile at right_small
        with dissolve
        aftb_says "( Whoa is this guy on estrogen or something? Why does he have boobs even though he's so skinny? )"
        show madd boy relieved at left_small
        with dissolve
        aftb_says "Yo let me check your muscle strength. "
        show madd boy flustered at left_small
        with dissolve 
        x "(W-what? i couldn't react fast enough before he grabbed my wrist and quickly squeezed the area for bisceps muscle)"
        show aftb evil smirk at right_small
        with dissolve
        aftb_says "( Damn, even his arms are so slender and smooth. )"
        aftb_says "Huh, you really are weak. If you dont train your body, no girls will ever want you."
        show madd boy embarrassed at left_small
        with dissolve        
        x "I-I guess I should start working out more..... I do want more girls to like me."
        show aftb laugh at right_small
        with dissolve
        aftb_says "Sure you do. Just remember to help me out when I need it."
        show  madd boy relieved at left_small
        with dissolve
        x "O-of course!"
        
        # Menu for conversation options
        label aftb_room_talk_menu:
        menu:
            "Talk with Aftb" if aftb_talk_today == False:
                # Level-based room interaction based on relationship stats
                if character_relations["aftb"]["identity"] > 10 and character_relations["aftb"]["lust"] > 20:
                    # Level 3 events
                    $ event_type = renpy.random.randint(1, 2)
                    if event_type == 1:
                        call interact_aftb_room_when_met_level_3_event_1 from _call_interact_aftb_room_when_met_level_3_event_1
                    else:
                        call interact_aftb_room_when_met_level_3_event_2 from _call_interact_aftb_room_when_met_level_3_event_2
                elif character_relations["aftb"]["identity"] > 5 and character_relations["aftb"]["lust"] > 10:
                    # Level 2 events
                    $ event_type = renpy.random.randint(1, 2)
                    if event_type == 1:
                        call interact_aftb_room_when_met_level_2_event_1 from _call_interact_aftb_room_when_met_level_2_event_1
                    else:
                        call interact_aftb_room_when_met_level_2_event_2 from _call_interact_aftb_room_when_met_level_2_event_2
                else:
                    # Level 1 events
                    $ event_type = renpy.random.randint(1, 2)
                    if event_type == 1:
                        call interact_aftb_room_when_met_level_1_event_1 from _call_interact_aftb_room_when_met_level_1_event_1
                    else:
                        call interact_aftb_room_when_met_level_1_event_2 from _call_interact_aftb_room_when_met_level_1_event_2
                
                # Mark that we talked today
                $ aftb_talk_today = True
                $ last_aftb_talk_hour = game_time.hour
                jump aftb_room_talk_menu
            
            "Talk with Aftb - Already talked today" if aftb_talk_today == True:
                show madd boy blush at left_small
                with dissolve
                x "I've already talked to you enough today. I should give you some space."
                show aftb smile at right_small
                with dissolve
                aftb_says "Yeah, maybe. Come back tomorrow if you want to chat more."
                jump aftb_room_talk_menu
            
            "Ask about jobs":
                call aftb_ask_about_jobs from _call_aftb_ask_about_jobs
                jump aftb_room_talk_menu
            
            "Ask about fun activities around here":
                call aftb_ask_about_fun_activities from _call_aftb_ask_about_fun_activities
                jump aftb_room_talk_menu
            
            "Ask about which school you go to":
                call aftb_ask_about_school from _call_aftb_ask_about_school
                jump aftb_room_talk_menu
            
            "Never mind":
                show madd boy blush at left_small
                with dissolve
                x "Actually, I should get going. It was nice talking to you."
                show aftb smile at right_small
                with dissolve
                aftb_says "Alright, come by anytime."
        

    
    $ game_time.advance_time(minutes=5)
    return

label interact_aftb_mess_hall(meal):
    """Mess hall interaction with Aftb"""
    if "aftb" not in met_characters:
        $ met_characters.append("aftb")
        $ character_relations["aftb"]["friend"] += 5
        $ current_location = "floor_1"
    
    show madd boy think at left_small
    with dissolve
    x "I go over to Aftb."
    show aftb evil smirk at right_small
    with dissolve
    aftb_says "Well, well. Another weak little thing. I'm Aftb from Room 204. Probably the strongest person you'll encounter here."
    show madd boy blush at left_small
    with dissolve
    x "I'm [mainname]. Nice to meet you, Aftb."
    show aftb bite lips smile at right_small
    with dissolve
    aftb_says "Yeah? Well look at you, all skinny and fragile. You're going to have a hard time around here with all these strong guys. Good luck with that."
    show madd boy blush at left_small
    with dissolve
    x "I... I'll manage somehow."
    show aftb laugh at right_small
    with dissolve
    aftb_says "Sure you will, kid. Now if you don't mind, I have actual food to get to. Move."
    $ game_time.advance_time(minutes=15)
    return

label intercept_aftb:
    """Interception scene with Aftb - calls level-based events"""
    show aftb evil smirk at right_small
    with dissolve
    aftb_says "Hey! Where you going? Don't you want to hang with the strongest guy around?"
    show madd boy flustered at left_small
    with dissolve
    x "A-Aftb! I was just heading..."
    x "(He blocks my path with his broad frame.)"
    show aftb bite lips smile at right_small
    with dissolve
    aftb_says "You know, you're so small next to me. It's actually pretty cute."
    show madd boy blush at left_small
    with dissolve
    x "I... I appreciate the compliment..."
    x "(He reaches out and gently touches my arm.)"
    show aftb laugh at right_small
    with dissolve
    aftb_says "Yeah, look at how delicate you are. I could break this in a second if I wanted to."
    show madd boy flustered at left_small
    with dissolve
    x "(His touch makes me shiver. I feel so vulnerable.)"
    show aftb laugh at right_small
    with dissolve
    
    # Level-based events based on relationship stats
    if character_relations["aftb"]["identity"] > 10 and character_relations["aftb"]["lust"] > 20:
        # Level 3 events
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call intercept_aftb_level_3_event_1 from _call_intercept_aftb_level_3_event_1
        else:
            call intercept_aftb_level_3_event_2 from _call_intercept_aftb_level_3_event_2
    elif character_relations["aftb"]["identity"] > 5 and character_relations["aftb"]["lust"] > 10:
        # Level 2 events
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call intercept_aftb_level_2_event_1 from _call_intercept_aftb_level_2_event_1
        else:
            call intercept_aftb_level_2_event_2 from _call_intercept_aftb_level_2_event_2
    else:
        # Level 1 events
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call intercept_aftb_level_1_event_1 from _call_intercept_aftb_level_1_event_1
        else:
            call intercept_aftb_level_1_event_2 from _call_intercept_aftb_level_1_event_2
    
    return

label water_bottle_witness_aftb:
    """Aftb witnesses water bottle cap drop - calls level-based events"""
    show aftb evil smirk at right_small
    with dissolve
    aftb_says "Huh, interesting..."
    
    # Level-based events based on relationship stats
    if character_relations["aftb"]["identity"] > 10 and character_relations["aftb"]["lust"] > 20:
        # Level 3 events
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call water_bottle_witness_aftb_level_3_event_1 from _call_water_bottle_witness_aftb_level_3_event_1
        else:
            call water_bottle_witness_aftb_level_3_event_2 from _call_water_bottle_witness_aftb_level_3_event_2
    elif character_relations["aftb"]["identity"] > 5 and character_relations["aftb"]["lust"] > 10:
        # Level 2 events
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call water_bottle_witness_aftb_level_2_event_1 from _call_water_bottle_witness_aftb_level_2_event_1
        else:
            call water_bottle_witness_aftb_level_2_event_2 from _call_water_bottle_witness_aftb_level_2_event_2
    else:
        # Level 1 events
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call water_bottle_witness_aftb_level_1_event_1 from _call_water_bottle_witness_aftb_level_1_event_1
        else:
            call water_bottle_witness_aftb_level_1_event_2 from _call_water_bottle_witness_aftb_level_1_event_2
    
    return

label water_cooler_intro_aftb:
    """First meeting at water cooler"""
    show aftb smile at right_small
    with dissolve
    x_says "Hi! I'm Madd, I just moved in upstairs."
    aftb_says "Hi there! I'm Aftb!"
    show madd boy happy at left_small
    with dissolve
    x_says "Nice to meet you!"
    return

label water_cooler_talk_aftb:
    """Casual conversation with Aftb at water cooler (non-first meeting) - calls level-based events"""
    show aftb smile at right_small
    with dissolve
    aftb_says "Hey, [mainname]! Getting your water refill?"
    show madd boy happy at left_small
    with dissolve
    x "Yeah, just staying hydrated. How about you?"
    show aftb laugh at right_small
    with dissolve
    aftb_says "Same here! You know, it's nice seeing you around. You seem like a good guy."
    show madd boy blush at left_small
    with dissolve
    x "Thanks, I appreciate that."
    show aftb smile at right_small
    with dissolve
    
    # Level-based events based on relationship stats
    if character_relations["aftb"]["identity"] > 10 and character_relations["aftb"]["lust"] > 20:
        # Level 3 events
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call water_cooler_talk_aftb_level_3_event_1 from _call_water_cooler_talk_aftb_level_3_event_1
        else:
            call water_cooler_talk_aftb_level_3_event_2 from _call_water_cooler_talk_aftb_level_3_event_2
    elif character_relations["aftb"]["identity"] > 5 and character_relations["aftb"]["lust"] > 10:
        # Level 2 events
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call water_cooler_talk_aftb_level_2_event_1 from _call_water_cooler_talk_aftb_level_2_event_1
        else:
            call water_cooler_talk_aftb_level_2_event_2 from _call_water_cooler_talk_aftb_level_2_event_2
    else:
        # Level 1 events
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call water_cooler_talk_aftb_level_1_event_1 from _call_water_cooler_talk_aftb_level_1_event_1
        else:
            call water_cooler_talk_aftb_level_1_event_2 from _call_water_cooler_talk_aftb_level_1_event_2
    
    return

label interact_aftb_mess_hall_met(meal):
    """Chat interaction with Aftb in mess hall (already met) - calls level-based events"""
    scene scene_messhall_breakfast
    with fade
    show madd boy blush at left_small
    with dissolve
    x "I walk over to Aftb."
    show aftb smile at right_small
    with dissolve
    aftb_says "Oh hey! Come eat with me."
    show madd boy happy at left_small
    with dissolve
    x "Thanks!"
    x "(I sit down next to him.)"
    show aftb bite lips smile at right_small
    with dissolve
    aftb_says "You know, I've been meaning to ask. You sure you're not on some special diet or something? You're still so delicate."
    show madd boy blush at left_small
    with dissolve
    x "I-I eat fine, just not as much as you probably do..."
    show aftb laugh at right_small
    with dissolve
    x "(He suddenly flexes his arm, then reaches over and squeezes my shoulder.)"
    show madd boy flustered at left_small
    with dissolve
    x "(His grip is firm and confident. I feel so small compared to him.)"
    show aftb evil smirk at right_small
    with dissolve
    
    # Level-based events based on relationship stats
    if character_relations["aftb"]["identity"] > 10 and character_relations["aftb"]["lust"] > 20:
        # Level 3 events
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call interact_aftb_mess_hall_met_level_3_event_1 from _call_interact_aftb_mess_hall_met_level_3_event_1
        else:
            call interact_aftb_mess_hall_met_level_3_event_2 from _call_interact_aftb_mess_hall_met_level_3_event_2
    elif character_relations["aftb"]["identity"] > 5 and character_relations["aftb"]["lust"] > 10:
        # Level 2 events
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call interact_aftb_mess_hall_met_level_2_event_1 from _call_interact_aftb_mess_hall_met_level_2_event_1
        else:
            call interact_aftb_mess_hall_met_level_2_event_2 from _call_interact_aftb_mess_hall_met_level_2_event_2
    else:
        # Level 1 events
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call interact_aftb_mess_hall_met_level_1_event_1 from _call_interact_aftb_mess_hall_met_level_1_event_1
        else:
            call interact_aftb_mess_hall_met_level_1_event_2 from _call_interact_aftb_mess_hall_met_level_1_event_2
    
    $ game_time.advance_time(minutes=20)
    return


# ============================================
# INTERACT_AFTB_ROOM_WHEN_MET LEVEL 1 EVENTS
# ============================================

#Done WRITING

label interact_aftb_room_when_met_level_1_event_1:
    """Level 1 event 1 for interact_aftb_room (when MET) - Aftb focuses on Madd's body and invites her to gym"""
    show aftb smirk at right_small
    with dissolve
    aftb_says "Actually, come inside for a second. I want to talk to you about something."
    show madd boy think at left_small
    with dissolve
    x "Huh? Sure, what is it?"
    show aftb dominant at right_small
    with dissolve
    aftb_says "Just come in."
    
    # Madd walks in - Aftb watches her
    show aftb predatory gaze at right_small
    with dissolve
    show madd boy hesitant at left_small
    with dissolve
    x "(I step into his room and start to walk past him...)"
    
    # SCENE 1: Predatory observation moment
    scene scene_interact_aftb_room_event_1_scene_1
    with dissolve
    
    show aftb calculating at right_small
    with dissolve
    aftb_says "( Oh damn... look at that. The way those pants hug her curves... that butt is so perfectly round and slappable. I could literally just reach out right now and... )"
    aftb_says "( God, she has no idea how hot she looks from this angle. That ass is begging for attention. )"
    
    show aftb aroused at right_small
    with dissolve
    show madd boy flustered at left_small
    with dissolve
    x "(I suddenly feel his gaze on me as I walk past... it's so intense. I can feel his eyes burning into my body.)"
    show aftb intoxicated pleasure at right_small
    with dissolve
    show madd boy embarrassed at left_small
    with dissolve
    x "(W-why does it feel like he's staring at me? Am I imagining things?)"
    x "(I can feel the heat of his eyes tracing over my... oh god, my butt. He's definitely looking at my butt.)"
    show aftb slow burn at right_small
    with dissolve
    show madd boy nervous at left_small
    with dissolve
    
    # Aftb walks around her
    show aftb methodical at right_small
    with dissolve
    aftb_says "You know, I've been thinking about you lately."
    show madd boy confused at left_small
    with dissolve
    x "About... me? Why?"
    show aftb contemptuous at right_small
    with dissolve
    aftb_says "( Mmm, yeah, I've been thinking about that body of yours. The curves, the softness... )"
    show aftb commanding at right_small
    with dissolve
    aftb_says "You're still way too weak. And honestly, it's getting worse."
    show madd boy uncertain at left_small
    with dissolve
    x "W-worse? I'm working on myself..."
    show aftb possessive at right_small
    with dissolve
    aftb_says "You're not doing enough. You need proper nutrition and training."
    
    # He walks closer, Madd feels his presence
    # SCENE 2: Dominance and exposure moment
    scene scene_interact_aftb_room_event_1_scene_2
    with dissolve
    
    show aftb marked prey at right_small
    with dissolve
    show madd boy scared at left_small
    with dissolve
    x "(He's standing so close now... I can feel the heat radiating from his body. He's still looking... looking at my...)"
    show aftb merciless at right_small
    with dissolve
    aftb_says "( Seriously, if she just started working out, if she put on some gym clothes... tight workout gear that shows off those curves even more... god, I'd lose it. )"
    
    show aftb expectant at right_small
    with dissolve
    aftb_says "Do you know what's the secret to having a good physique?"
    show madd boy hesitant at left_small
    with dissolve
    x "I... no, I don't think so..."
    show aftb satisfied at right_small
    with dissolve
    aftb_says "Protein. You need a lot of it. Lean meats, eggs, supplements... the whole deal."
    show madd boy deep blush at left_small
    with dissolve
    x "(My heart is racing. Why is he telling me this? And why does he keep... looking at me like that?)"
    
    show aftb controlling at right_small
    with dissolve
    aftb_says "And you need to start training. Get into the gym."
    show madd boy conflicted at left_small
    with dissolve
    x "The gym? But I've never really trained before..."
    show aftb complete ownership at right_small
    with dissolve
    aftb_says "That's exactly why you need to start. Building muscle will change your entire body."
    aftb_says "( And I want to see exactly how much your body changes. I want to watch you transform in gym clothes... )"
    show madd boy submissive at left_small
    with dissolve
    
    show aftb observant at right_small
    with dissolve
    aftb_says "Look, I work at FitLife Gym. I could help you get started. Show you the proper form, the exercises, everything."
    show madd boy uncertain at left_small
    with dissolve
    x "You'd... you'd help me?"
    show aftb calculating at right_small
    with dissolve
    aftb_says "Yeah, why not. It would be good for me too - having someone to train with."
    aftb_says "( Someone with a body like that working out right in front of me... wearing minimal clothing... pushing themselves hard... )"
    show aftb anticipatory at right_small
    with dissolve


    # SCENE 3: Gym offer triumph moment
    scene scene_interact_aftb_room_event_1_scene_3
    with dissolve   
    show madd boy humiliated at left_small
    with dissolve
    x "(I feel so exposed right now. It's like he can see right through my clothes... like he's undressing me with his eyes.)"
    x "(But... but the way he's looking at me is making me feel... strange. Nervous, yes, but also... something else.)"
    show madd boy obedient at left_small
    with dissolve
    
    show aftb apex predator at right_small
    with dissolve
    aftb_says "So what do you say? Want me to help you get into shape?"
    show madd boy traumatized at left_small
    with dissolve
    x "I... I guess that would be nice. When... when could we start?"

    show aftb triumphant at right_small
    with dissolve
    aftb_says "Whenever you're ready. The gym is open most days. Just let me know."
    aftb_says "( And I'll make sure to give you the best view of everything while you work out. )"
    
    $ character_relations["aftb"]["lust"] += 3
    $ character_relations["aftb"]["dominance"] += 1
    $ character_relations["aftb"]["identity"] += 1
    $ madd_lust += 2
    $ madd_dominance -= 1
    $ secret_identity -= 0.5
    $ madd_corruption += 0.5
    
    return

label interact_aftb_room_when_met_level_1_event_2:
    """Level 1 event 2 for interact_aftb_room (when MET) - Aftb's room filled with his scent"""
    show aftb patient at right_small
    with dissolve
    aftb_says "Hey, come inside for a moment. I need to ask you about something."
    show madd boy think at left_small
    with dissolve
    x "Is it something important? Sure, I guess..."
    # SCENE 1: Madd overwhelmed by scent
    scene scene_interact_aftb_room_event_2_scene_1
    with dissolve    


    # Madd enters the room
    show aftb predatory gaze at right_small
    with dissolve
    show madd boy hesitant at left_small
    with dissolve
    x "(I step into his room and immediately... oh my god.)"
    show madd boy flustered at left_small
    with dissolve
    x "(The smell... it's so strong. Sweat, his sweat... it's everywhere.)"
    x "(On his bed, there's... oh god... his towels, his undergarments, t-shirts... all spread out to dry.)"
    show aftb aroused at right_small
    with dissolve
    show madd boy embarrassed at left_small
    with dissolve
    x "(The scent is coming from those... from him... it's so overwhelming.)"
    show madd boy shamed at left_small
    with dissolve
    x "(Why is this affecting me so much? My heart is racing... my face is burning... what is this smell doing to me?)"
    
    # SCENE 2: Madd affected and disoriented by pheromones
    scene scene_interact_aftb_room_event_2_scene_2
    with dissolve
    
    # Aftb watches her reaction
    show aftb calculating at right_small
    with dissolve
    aftb_says "You okay there?"
    show madd boy nervous at left_small
    with dissolve
    x "Y-yes, I'm fine. It's just... your room has quite a smell."
    
    # Aftb's internal monologue
    show aftb intoxicated pleasure at right_small
    with dissolve
    aftb_says " Yeah sorry about that. I've been training hard lately, so I tend to sweat a lot. Gotta keep my body in top shape, you know?" 
    aftb_says "( Heh, look at her. She's practically melting from my scent. )"
    aftb_says "( Just like in the animal kingdom... pheromones. Females react to the scent of a strong male. And I've been training hard - my body is just drenched in them. )"
    aftb_says "( Look how she's breathing... deeper, more desperate. Her pupils are dilating. She's being affected by my presence on a primal level. )"
    show aftb slow burn at right_small
    with dissolve
    aftb_says "( Perfect. I'm going to keep her in here as long as I can. Let her marinate in my scent. Let her body react without her mind understanding why. )"
    
    # Aftb sits down, gesturing for her to sit
    show aftb expectant at right_small
    with dissolve
    aftb_says "So, you ever think about life? Like, the meaning of it all?"
    show madd boy conflicted at left_small
    with dissolve
    x "(I'm trying to focus on what he's saying, but... that smell... it's intoxicating.)"
    x "(I can feel my legs getting weak. Is it hot in here? Why am I sweating?)"
    show madd boy confused at left_small
    with dissolve
    x "Um... the meaning of life? I suppose I have..."
    
    # SCENE 3: Aftb keeps her trapped - moment of captivity
    scene scene_interact_aftb_room_event_2_scene_3
    with dissolve
    
    # Madd tries to move toward the door
    show aftb methodical at right_small
    with dissolve
    show madd boy scared at left_small
    with dissolve
    x "(I need to get out of here. This is too much. I need air... fresh air...)"
    
    # Aftb quickly changes topic to keep her engaged
    show aftb commanding at right_small
    with dissolve
    aftb_says "Wait, before you go - have you heard about the monthly test coming up?"
    show madd boy hesitant at left_small
    with dissolve
    x "Monthly test? What test?"
    show aftb dominant at right_small
    with dissolve
    aftb_says "It's something all the cram schools participate in. Even though we go to different schools, there's this unified monthly assessment test that everyone takes."
    show madd boy uncertain at left_small
    with dissolve
    x "Oh... I didn't know about that. When is it?"
    show aftb possessive at right_small
    with dissolve
    aftb_says "2 months from now, I think. It's supposed to be pretty competitive. All the top students from different cram schools compete."
    
    # Aftb's continued internal monologue
    show aftb contemptuous at right_small
    with dissolve
    aftb_says "( That's it... stay a little longer... )"
    aftb_says "( God, I'm gonna get a new bitch I could use whenever I want. And it's gonna be so easy... )"
    aftb_says "( She's already responding to me on an instinctual level. Once I really start working on her, she'll be completely under my control. )"
    show aftb marked prey at right_small
    with dissolve
    aftb_says "( I can already imagine it - her in gym clothes, covered in sweat, completely dependent on me. She'll be mine to do whatever I want with. )"
    
    # Back to Madd's perspective
    show madd boy traumatized at left_small
    with dissolve
    x "(He's talking about the school event, but all I can focus on is... is him. His presence. His scent.)"
    x "(Why is my body reacting like this? I feel like I'm losing control...)"
    show madd boy dissociating at left_small
    with dissolve
    x "(The smell is getting stronger, or am I getting more sensitive to it?)"
    
    # Aftb continues talking to keep her there
    show aftb merciless at right_small
    with dissolve
    aftb_says "You should probably prepare for it. It's going to be challenging."
    show madd boy resigned at left_small
    with dissolve
    x "M-maybe... I'll think about it..."
    x "(He's just talking about the monthly test, but why does it feel like he's doing something to me?)"
    show madd boy obedient at left_small
    with dissolve
    x "(Why don't I want to leave? Why am I still standing here?)"
    
    # Another attempt to escape
    show madd boy humiliated at left_small
    with dissolve
    x "Um, I should probably go study... I need to prepare for ..."
    show aftb complete ownership at right_small
    with dissolve
    aftb_says "Oh, one more thing - do you think it's better to study alone or with a partner? I've been wondering about the philosophy of learning."
    show madd boy defeated at left_small
    with dissolve
    x "The philosophy of learning? I... I think both have their advantages..."
    show madd boy submissive at left_small
    with dissolve
    
    # Aftb's final internal thoughts
    show aftb apex predator at right_small
    with dissolve
    aftb_says "( Perfect. She's completely entranced. Her body knows what she really wants, even if her mind is still trying to deny it. )"
    aftb_says "( Soon... very soon, she'll be begging for my attention. And I'm going to give it to her in ways she can't even imagine. )"
    aftb_says "( She'll be my perfect little toy to satisfy whenever the urge strikes. )"
    
    # Madd finally forces herself to leave
    show madd boy shaken at left_small
    with dissolve
    x "(I force myself to stand up, even though my legs feel like jelly.)"
    x "I... I really need to go now. Thanks for the school info..."
    show aftb satisfied at right_small
    with dissolve
    aftb_says "Sure. Come by again sometime. We can study together."
    show madd boy trembling at left_small
    with dissolve
    x "(As I leave his room, the fresh air hits me, but I can still smell him on me... in me...)"
    x "(What just happened? What was that? Why do I feel so... affected?)"
    show madd boy broken at left_small
    with dissolve
    
    $ character_relations["aftb"]["lust"] += 4
    $ character_relations["aftb"]["identity"] += 1
    $ character_relations["aftb"]["dominance"] += 2
    $ madd_lust += 3
    $ madd_dominance -= 2
    $ secret_identity -= 0.5
    $ corruption += 0.5
    
    return


# ============================================
# INTERACT_AFTB_ROOM_WHEN_MET LEVEL 2 EVENTS
# ============================================

label interact_aftb_room_when_met_level_2_event_1:
    """Level 2 event 1 for interact_aftb_room (when MET)"""
    return

label interact_aftb_room_when_met_level_2_event_2:
    """Level 2 event 2 for interact_aftb_room (when MET)"""
    return


# ============================================
# INTERACT_AFTB_ROOM_WHEN_MET LEVEL 3 EVENTS
# ============================================

label interact_aftb_room_when_met_level_3_event_1:
    """Level 3 event 1 for interact_aftb_room (when MET)"""
    return

label interact_aftb_room_when_met_level_3_event_2:
    """Level 3 event 2 for interact_aftb_room (when MET)"""
    return


# ============================================
# INTERCEPT_AFTB LEVEL 1 EVENTS 
# ============================================
#Done WRITING

label intercept_aftb_level_1_event_1:
    """Level 1 event 1 for intercept_aftb - Aftb blocks path with pheromone strategy"""
    show aftb smile at right_small
    with dissolve
    aftb_says "Oh, perfect timing! I just got back from an intense workout session at the gym."
    show madd boy nervous at left_small
    with dissolve
    x "Oh, that's cool... I was just heading to..."
    
    # SCENE 1: Aftb blocks the path - the trap is set
    scene scene_intercept_aftb_level_1_scene_1
    with dissolve
    
    # Aftb blocks her path
    show aftb dominant at right_small
    with dissolve
    aftb_says "Wait, I haven't seen you in a while. How's your day been?"
    show madd boy hesitant at left_small
    with dissolve
    x "(He's blocking my way... I can't really leave without being rude.)"
    
    # Aftb steps closer
    show aftb predatory gaze at right_small
    with dissolve
    x "(He's moving closer... he's so close now...)"
    show madd boy embarrassed at left_small
    with dissolve
    x "(Oh god... the smell...)"
    
    # Aftb scratches his armpit deliberately
    show aftb calculating at right_small
    with dissolve
    aftb_says "Man, I'm still pretty sweaty from that workout. You know, I read somewhere in National Geographic that the body releases pheromones during exercise. Fascinating stuff, really."
    
    # SCENE 2: Aftb uses scent as a weapon - deliberate pheromone manipulation
    scene scene_intercept_aftb_level_1_scene_2
    with dissolve
    
    show madd boy confused at left_small
    with dissolve
    x "(W-why is he telling me this? And why is he... scratching his armpit like that?)"
    
    # Madd's internal thoughts
    show madd boy shamed at left_small
    with dissolve
    x "(The smell... it's so strong. I can feel it hitting me in waves every time he moves... every time he breathes...)"
    show madd boy trembling at left_small
    with dissolve
    x "(Oh god, did I just catch another whiff when he raised his arm? Did he... did he do that on purpose?)"
    show madd boy self loathing at left_small
    with dissolve
    x "(I want to leave so badly, but I can't just walk away. That would be so rude... he'd think I find him disgusting...)"
    show madd boy defeated at left_small
    with dissolve
    x "(But this... this is... it's affecting me...)"
    
    # Aftb's internal monologue
    show aftb plotting at right_small
    with dissolve
    aftb_says "( Perfect. I can see it in her eyes. She's catching my scent... my pheromones. Her pupils are dilating, her breathing is getting heavier. )"
    show aftb intoxicated pleasure at right_small
    with dissolve
    aftb_says "( She wants to leave, but she's too polite to do it. Too afraid of offending me. That's exactly what I need. )"
    show aftb methodical at right_small
    with dissolve
    aftb_says "( National Geographic had an entire episode on this. Animals use pheromones to establish dominance and trigger responses in potential mates. And she's responding perfectly. )"
    show aftb slow burn at right_small
    with dissolve
    aftb_says "( I'm going to keep her here, keep letting her breathe in my scent, my dominance. She'll be completely under my control without even realizing it. )"
    
    # Aftb continues talking casually
    show aftb expectant at right_small
    with dissolve
    aftb_says "So yeah, the workout was brutal. Really pushed myself today. You can probably tell from how much I'm sweating, huh?"
    show madd boy processing at left_small
    with dissolve
    x "(He's just making casual conversation, but... why does it feel like he's doing something to me?)"
    show madd boy scared at left_small
    with dissolve
    x "(Is he doing this on purpose? No... no, that would be crazy. He's just talking about his day.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(But he keeps standing so close... and that smell... I can't escape it...)"
    
    # Aftb deliberately shifts position
    show aftb possessive at right_small
    with dissolve
    aftb_says "Anyway, how about you? How's your day been? You look... flushed."
    show madd boy embarrassed at left_small
    with dissolve
    x "I-I'm fine. Just been busy."
    
    # Another whiff as he moves
    show madd boy dissociating at left_small
    with dissolve
    x "(Oh god... I just caught it again. His scent... it's so overwhelming. My legs feel weak.)"
    show madd boy numb at left_small
    with dissolve
    x "(What is wrong with me? Why can't I just excuse myself and leave?)"
    
    # Aftb's continued thoughts
    show aftb masterful at right_small
    with dissolve
    aftb_says "( Look at her squirm. She's trapped between wanting to stay and wanting to run. )"
    show aftb cruel at right_small
    with dissolve
    aftb_says "( This is exactly how dominance works in the animal kingdom. The stronger male marks his territory with his scent, and the female is drawn to it whether she consciously wants to be or not. )"
    show aftb inevitable at right_small
    with dissolve
    aftb_says "( Soon, she won't even be able to think straight when she's near me. She'll just be thinking about me, about my presence, about submitting. )"
    show aftb complete ownership at right_small
    with dissolve
    aftb_says "( I've already got her exactly where I want her - unable to leave, unable to speak up, just breathing in my dominance over her. )"
    
    # Madd tries to find an escape
    show madd boy nervous at left_small
    with dissolve
    x "Um... I really should get going. I have... I have something I need to do."
    
    # SCENE 3: Madd's surrender in the hallway - psychological dominance
    scene scene_intercept_aftb_level_1_scene_3
    with dissolve
    
    show aftb commanding at right_small
    with dissolve
    aftb_says "Oh, something important? You should take care of that then. But hey, come find me later, yeah? I enjoyed talking to you."
    show madd boy submissive at left_small
    with dissolve
    x "Y-yes, sure... I'll... I'll do that..."
    
    # As she tries to leave
    show madd boy paralyzed at left_small
    with dissolve
    x "(I finally manage to step around him, and the fresh air hits me like a relief. But even as I walk away...)"
    show madd boy processing at left_small
    with dissolve
    x "(I can still smell him on me. In me. The scent is clinging to my clothes, my hair...)"
    show madd boy confused at left_small
    with dissolve
    x "(What just happened? Did he... was he deliberately trying to... no, I'm imagining things.)"
    show madd boy desperate at left_small
    with dissolve
    x "(But if I'm honest with myself... I didn't completely hate it.)"
    show madd boy shaken at left_small
    with dissolve
    x "(What does that say about me?)"
    
    # Final thought from Aftb as she leaves
    show aftb smug at right_small
    with dissolve
    aftb_says "( She'll be back for more. They always do. )"
    show aftb apex predator at right_small
    with dissolve
    aftb_says "( She's already starting to respond to me on a primal level. This is just the beginning of her submission. )"
    
    $ character_relations["aftb"]["lust"] += 3
    $ character_relations["aftb"]["identity"] += 1
    $ character_relations["aftb"]["dominance"] += 3
    $ madd_lust += 3
    $ madd_dominance -= 2
    $ secret_identity -= 0.5
    $ corruption += 0.5
    
    return

label intercept_aftb_level_1_event_2:
    """Level 1 event 2 for intercept_aftb - Aftb marks Madd with his sweat through headphones"""
    show aftb aroused at right_small
    with dissolve
    aftb_says "Hey! Perfect, I just got back from the gym. Check this out."
    show madd boy think at left_small
    with dissolve
    x "Huh? What is it?"
    
    # Aftb takes off his headphones
    show aftb calculating at right_small
    with dissolve
    aftb_says "I was listening to this track while I was working out. It's so good. Here, take them and listen."
    show madd boy hesitant at left_small
    with dissolve
    x "Oh, um... I don't want to bother you if you're still listening..."
    
    # He insists
    show aftb commanding at right_small
    with dissolve
    aftb_says "Nah, come on. Just for a moment. I want to hear what you think about it."
    
    # SCENE 1: Aftb offers the sweat-soaked headphones - the marking begins
    scene scene_intercept_aftb_level_1_scene_2_1
    with dissolve
    
    show madd boy reluctant at left_small
    with dissolve
    x "(I reach out to take them reluctantly...)"
    
    # Madd notices the sweat
    x "(Oh... oh god...)"
    show madd boy flustered at left_small
    with dissolve
    x "(They're... they're soaking wet. Like, completely drenched in sweat.)"
    x "(The moisture is dripping... this is so gross... I can feel his sweat on my hands...)"
    show madd boy disgusted at left_small
    with dissolve
    
    # Madd's internal thoughts intensify
    x "(The smell... it's overpowering. One hour of continuous workout... his sweat has been marinating in these headphones for a full hour...)"
    show madd boy embarrassed at left_small
    with dissolve
    x "(How am I supposed to put these on? Won't I... won't I basically be rubbing his sweat all over my face and ears?)"
    x "(This is so... so intimate in the most uncomfortable way...)"
    show madd boy salivating at left_small
    with dissolve
    
    # Aftb's internal monologue
    show aftb smirk at right_small
    with dissolve
    aftb_says "( Perfect. She's looking at the headphones like they're disgusting. But she won't say anything because she doesn't want to hurt my feelings. )"
    aftb_says "( I've been wearing these for a full hour straight during my workout. They're absolutely soaked with my sweat. )"
    aftb_says "( This is exactly what I want. When she puts them on, my sweat - my essence, my scent, my mark - will transfer directly onto her skin. )"
    aftb_says "( It's like I'm rubbing myself all over her face and ears. She'll be wearing me. Literally wearing my sweat. )"
    aftb_says "( This is about establishing ownership. Making her familiar with my scent at such an intimate level. )"
    aftb_says "( She'll be self-conscious the whole time, thinking about my sweat on her skin, and that discomfort will create a psychological association with me. )"
    aftb_says "( This is marking. Just like in the animal kingdom. )"
    
    # Madd reluctantly puts them on
    show madd boy hesitant at left_small
    with dissolve
    x "(I can't refuse... that would be too rude. He's just trying to share music with me...)"
    x "(Deep breath. It's just sweat. Just... his sweat. On my ears. On my face. Mixing with my skin...)"
    
    # SCENE 2: Madd wears his sweat - intimate violation moment
    scene scene_intercept_aftb_level_1_scene_2_2
    with dissolve
    
    # The moment she puts them on
    show madd boy nervous at left_small
    with dissolve
    x "(As soon as I place them on my ears, I feel it... the moisture... the wetness...)"
    show madd boy shocked at left_small
    with dissolve
    x "(Oh my god... oh god... it's so wet... his sweat is transferring onto my skin... it's warm... it's like...)"
    x "(It's like he just... rubbed himself on me. All over my ears and the sides of my face.)"
    show madd boy flustered at left_small
    with dissolve
    x "(I can feel it seeping into my skin. His scent is right there, inches from my nose, on my face...)"
    show madd boy salivating at left_small
    with dissolve
    x "(This is so intimate and gross and... and why am I not stopping this?)"
    
    # Madd's shame and conflict
    show madd boy ashamed at left_small
    with dissolve
    x "(I should take them off. I should say something. But he's looking at me so expectantly...)"
    x "(If I refuse now, it would be so awkward. He'd know I find him disgusting. He'd think I'm rude.)"
    x "(So I'm just going to stand here... wearing his sweat on my face... like some kind of mark he's put on me.)"
    show madd boy embarrassed at left_small
    with dissolve
    
    # The music starts playing
    show scene russian music at center
    with dissolve
    x "(The music starts... it's... it's in Russian? I can't understand a word of it.)"
    x "(The beat is... okay, I guess? It's fast, energetic... but I can barely focus on it.)"
    show madd boy processing at left_small
    with dissolve
    x "(All I can focus on is the feeling of his sweat drying on my skin... the way it's making my ears itch... the persistent smell of him...)"
    
    # SCENE 3: After the marking - she carries him with her
    scene scene_intercept_aftb_level_1_scene_2_3
    with dissolve
    
    # Aftb talks to her while she's wearing his headphones
    show aftb dominant at right_small
    with dissolve
    aftb_says "So, how's your day been? You seem a little tense."
    show madd boy submissive at left_small
    with dissolve
    x "(He's asking how my day has been... while I'm literally wearing his sweat on my face...)"
    x "(This is so surreal.)"
    
    # Madd tries to respond
    show madd boy trembling at left_small
    with dissolve
    x "It's been... it's been okay. Pretty busy."
    show aftb possessive at right_small
    with dissolve
    aftb_says "Cool, cool. So what do you think of the song? Pretty good beat, right?"
    
    # Madd's lie
    show madd boy obedient at left_small
    with dissolve
    x "(I can barely understand the lyrics... the language is completely foreign... but if I say I don't like it, I'll hurt his feelings. I'll look ungrateful.)"
    x "Y-yeah, the beat is really... really good. Very energetic."
    show madd boy uncertain at left_small
    with dissolve
    x "(Even as I say it, I feel pathetic. I'm lying about a song I can't understand, while wearing his sweat, because I'm too polite to be honest.)"
    
    # Aftb's satisfaction
    show aftb smug at right_small
    with dissolve
    aftb_says "Right? I knew you'd like it. The artist is from Moscow. Pretty popular there."
    aftb_says "( She has no idea what they're singing about. She's just nodding along, pretending to like it. )"
    aftb_says "( But that's not the point. The point is she's wearing my mark right now. )"
    aftb_says "( Every time she feels that moisture on her skin, every time she smells me, she'll be reminded of this moment. )"
    aftb_says "( Her defenses are crumbling. She's so focused on being polite that she's sacrificing her own dignity. )"
    aftb_says "( This is exactly how I'm going to dominate her. Not through force, but through her own politeness and concern about hurting my feelings. )"
    aftb_says "( She'll keep doing things like this - things that make her uncomfortable - because she doesn't want to be rude. )"
    aftb_says "( Soon, being covered in my scent, being marked by me, won't even bother her. It'll become normal. Expected. )"
    
    # Madd's continued discomfort
    show madd boy uncomfortable at left_small
    with dissolve
    x "(How long am I supposed to wear these? How long until this is over?)"
    x "(The sweat is starting to feel sticky as it dries... it's clinging to my skin...)"
    show madd boy salivating at left_small
    with dissolve
    x "(And despite how gross this is, there's a part of me that... that doesn't want him to ask for them back.)"
    x "(That thought makes me feel even more ashamed.)"
    show madd boy conflicted at left_small
    with dissolve
    
    # Aftb continues casual conversation
    show aftb confident at right_small
    with dissolve
    aftb_says "You know, you should really come to the gym with me sometime. Get some exercise. You'd feel so much better."
    show madd boy scared at left_small
    with dissolve
    x "(Even as he's suggesting this, I realize what he's actually suggesting - that I come work out in close proximity to him, drenched in sweat...)"
    x "(Is that what he wants? To have me covered in sweat at the gym? To mark me over and over again?)"
    show madd boy nervous at left_small
    with dissolve
    
    # The moment drags on
    show madd boy defeated at left_small
    with dissolve
    x "(The music keeps playing in Russian... I still don't understand a word of it...)"
    x "(But I'm trapped here, wearing his scent, his mark, pretending to enjoy this.)"
    x "(When did I become someone who accepts this? When did I stop fighting back?)"
    show madd boy broken at left_small
    with dissolve
    
    # Finally, he asks for them back
    show aftb triumphant at right_small
    with dissolve
    aftb_says "Alright, I should probably get these back. But seriously, let me know about the gym, yeah?"
    show madd boy submissive at left_small
    with dissolve
    x "(I hand them back to him, and the feeling of the wet material leaving my ears is almost a relief... but also oddly empty...)"
    x "(But I can still smell him. The scent is still on my skin, on my face.)"
    show madd boy conflicted at left_small
    with dissolve
    x "(Even after giving them back, I'm still carrying a piece of him with me.)"
    
    # As she walks away
    x "(I can still feel the moisture on my ears... the subtle weight of his scent on my skin...)"
    show madd boy ashamed at left_small
    with dissolve
    x "(He marked me. And I let him. Because I was too polite to say no.)"
    x "(What is happening to me?)"
    show madd boy salivating at left_small
    with dissolve
    
    $ character_relations["aftb"]["lust"] += 4
    $ character_relations["aftb"]["identity"] += 1
    $ character_relations["aftb"]["dominance"] += 3
    $ madd_lust += 3
    $ madd_dominance -= 2
    $ secret_identity -= 0.5
    $ corruption += 0.5
    
    return


# ============================================
# INTERCEPT_AFTB LEVEL 2 EVENTS
# ============================================

label intercept_aftb_level_2_event_1:
    """Level 2 event 1 for intercept_aftb"""
    return

label intercept_aftb_level_2_event_2:
    """Level 2 event 2 for intercept_aftb"""
    return


# ============================================
# INTERCEPT_AFTB LEVEL 3 EVENTS
# ============================================

label intercept_aftb_level_3_event_1:
    """Level 3 event 1 for intercept_aftb"""
    return

label intercept_aftb_level_3_event_2:
    """Level 3 event 2 for intercept_aftb"""
    return


# ============================================
# WATER_BOTTLE_WITNESS_AFTB LEVEL 1 EVENTS
# ============================================

label water_bottle_witness_aftb_level_1_event_1:
    """Level 1 event 1 for water_bottle_witness_aftb - Aftb witnesses Madd bent over at water cooler"""
    
    # Set the location
    $ bg_image = get_location_image("floor_2_water_cooler", game_time, character_meal_times)
    scene expression bg_image
    with fade
    
    # Madd is bending over to get water
    show madd boy bent over at center
    with dissolve
    x "(I need to fill up my water bottle. I'm so thirsty...)"
    
    # SCENE 1: Aftb rounds the corner - predatory observation
    scene scene_water_bottle_witness_aftb_event_1_scene_1
    with dissolve
    
    # Aftb rounds the corner and sees Madd
    show aftb predatory gaze at right_small
    with dissolve
    show madd boy bent over at center
    with dissolve
    
    # Aftb's immediate physical reaction
    show aftb aroused at right_small
    with dissolve
    aftb_says "( What the— )"
    show aftb intoxicated pleasure at right_small
    with dissolve
    aftb_says "( Oh. Oh fuck. )"
    show aftb marked prey at right_small
    with dissolve
    aftb_says "( Is that... is that Madd bent over like that? )"
    
    # Aftb's arousal and explicit internal monologue
    show aftb slow burn at right_small
    with dissolve
    aftb_says "( Holy shit. Look at that ass. )"
    show aftb calculating at right_small
    with dissolve
    aftb_says "( The way those pants are fitting... the curve... I can see everything from this angle. )"
    show aftb merciless at right_small
    with dissolve
    aftb_says "( Fuck. I'm getting hard right now. Just from looking at that. )"
    show aftb possessive at right_small
    with dissolve
    aftb_says "( I need to bury myself in that. Soon. As soon as possible. )"
    show aftb contemptuous at right_small
    with dissolve
    aftb_says "( I want to own that. To claim that. To make her understand that ass belongs to me. )"
    show aftb masterful at right_small
    with dissolve
    aftb_says "( How would it feel to wake up with my dick inside that? Buried deep in that ass every morning? )"
    show aftb complete ownership at right_small
    with dissolve
    aftb_says "( She'd be mine. Completely mine. Used up, stretched out, permanently marked as belonging to me. )"
    
    # Aftb adjusts himself
    show aftb commanding at right_small
    with dissolve
    aftb_says "( I can feel myself getting hard in my pants. I need to say something. Something that lets her know I see her. That I want her. )"
    show aftb methodical at right_small
    with dissolve
    aftb_says "( But I don't want to scare her off completely. I need to play this carefully. )"
    show aftb plotting at right_small
    with dissolve
    aftb_says "( A comment. Something casual enough that she might laugh it off, but direct enough that she knows exactly what I'm looking at and what I'm thinking about. )"
    
    # SCENE 2: The crude comment - public objectification and marking
    scene scene_water_bottle_witness_aftb_event_1_scene_2
    with dissolve
    
    # Aftb makes his comment
    show aftb smirk at right_small
    with dissolve
    aftb_says "Damn. Nice ass, shawty."
    
    # Madd freezes in shock
    show madd boy shocked at center
    with dissolve
    x "(...)"
    show madd boy surprised at center
    with dissolve
    x "( Did he just... did Aftb just say that? Out loud? )"
    show madd boy horrified at center
    with dissolve
    x "( To me? About my... )"
    
    # Madd straightens up immediately
    show madd boy embarrassed at center
    with dissolve
    x "( Oh my god. I was bent over. He was looking at me bent over. )"
    show madd boy shamed at center
    with dissolve
    x "( He was staring at my... my ass. )"
    
    # Madd's intense shame
    show madd boy humiliated at center
    with dissolve
    x "( This is so embarrassing. I feel so exposed. So... objectified. )"
    show madd boy defeated at center
    with dissolve
    x "( He doesn't see me. He just sees... a body. A thing to be used. )"
    show madd boy self loathing at center
    with dissolve
    x "( And the way he said it... so casual... like he was commenting on the weather, not on my body. )"
    show madd boy processing at center
    with dissolve
    x "( Like it's completely normal to just... comment on someone's ass. )"
    
    # Madd wants to disappear
    show madd boy nervous at center
    with dissolve
    x "( I don't know what to say. I don't know how to respond to that. )"
    show madd boy scared at center
    with dissolve
    x "( If I say something, it'll make it worse. It'll make this interaction longer. )"
    show madd boy conflicted at center
    with dissolve
    x "( If I stay silent, maybe he'll just... leave. Maybe this will be over. )"
    show madd boy uncertain at center
    with dissolve
    x "( But if I say nothing, is that accepting it? Is that giving him permission to say things like that? )"
    
    # Madd remains silent, looking down
    show madd boy trembling at center
    with dissolve
    x "( I can feel my face burning. I'm so embarrassed. So humiliated. )"
    show madd boy shaken at center
    with dissolve
    x "( Everyone could have heard that. Anyone walking by could have heard him say that about me. )"
    show madd boy nervous at center
    with dissolve
    x "( What if someone did? What if people start talking about me because of this? )"
    
    # Aftb's continued internal monologue
    show aftb satisfied at right_small
    with dissolve
    aftb_says "( She's not saying anything. She's just standing there, embarrassed, not knowing what to do. )"
    show aftb triumphant at right_small
    with dissolve
    aftb_says "( Perfect. This is exactly what I want. )"
    show aftb dominant at right_small
    with dissolve
    aftb_says "( Her silence is consent. Her embarrassment is acceptance. )"
    show aftb cruel at right_small
    with dissolve
    aftb_says "( She's too shy to object, too polite to tell me off, too afraid of making it awkward. )"
    show aftb inevitable at right_small
    with dissolve
    aftb_says "( This is how I take control. Not through aggression, but through making her too uncomfortable to resist. )"
    show aftb patient predator at right_small
    with dissolve
    aftb_says "( She's realizing right now that her body is mine. That I can look at it whenever I want. That I can comment on it whenever I want. )"
    show aftb smug at right_small
    with dissolve
    aftb_says "( And she can't stop me because she's too much of a coward to say anything. )"
    show aftb contemptuous at right_small
    with dissolve
    aftb_says "( I like that in her. The fact that she's so helpless. So easy to dominate. )"
    
    # Madd finally moves
    show madd boy resigned at center
    with dissolve
    x "( I just need to get my water and leave. That's it. Just fill up and go. )"
    show madd boy scared at center
    with dissolve
    x "( Don't make eye contact. Don't say anything. Just get out of here. )"
    
    # Madd continues to feel exposed
    show madd boy dissociating at center
    with dissolve
    x "( But I can feel his eyes on me. Even as I'm facing away, filling up my bottle, I can feel his gaze on my back. )"
    show madd boy numb at center
    with dissolve
    x "( On my... on the part he was just commenting on. )"
    show madd boy paralyzed at center
    with dissolve
    x "( Is he still looking? Is he still checking me out? )"
    show madd boy desperate at center
    with dissolve
    x "( Why am I like this? Why can't I just turn around and tell him to stop? To respect me? )"
    show madd boy obedient at center
    with dissolve
    x "( But I know why. Because he's intimidating. Because he's stronger. Because if I upset him, he might... )"
    
    # Madd's fear mixed with something else
    show madd boy deep blush at center
    with dissolve
    x "( And there's something else too. Something I don't want to admit. )"
    show madd boy confused consent at center
    with dissolve
    x "( Some part of me... some small, shameful part of me liked being noticed like that. )"
    show madd boy submissive at center
    with dissolve
    x "( Not the disrespect. Not the objectification. But the attention. The fact that he was looking. )"
    show madd boy broken at center
    with dissolve
    x "( That's disgusting. That makes me disgusting. )"
    
    # Madd's continued internal shame
    show madd boy gagging at center
    with dissolve
    x "( I'm conflicted. I'm angry at him for saying something so crude. But I'm also... )"
    show madd boy dissociating at center
    with dissolve
    x "( Why am I thinking about whether he'll do it again? )"
    show madd boy weeping at center
    with dissolve
    x "( Why am I wondering if next time he'll do more than just comment? )"
    
    # Aftb speaks again, more casually
    show aftb observant at right_small
    with dissolve
    aftb_says "Water tastes good from that cooler, right? I like the cold. Refreshing."
    
    # Madd is confused by the sudden normalcy
    show madd boy confused at center
    with dissolve
    x "( What... what is he doing? )"
    show madd boy kneeling at center
    with dissolve
    x "( He just made that comment about my ass and now he's talking about water? )"
    show madd boy processing at center
    with dissolve
    x "( Is this supposed to make me think it's okay? That it was just a casual observation? )"
    show madd boy silent at center
    with dissolve
    x "( It wasn't casual. It was deliberate. He wanted me to hear it. )"
    
    # Madd finally turns around
    show madd boy resigned at center
    with dissolve
    x "( I turn around slowly, keeping my eyes down. I can't make eye contact with him. )"
    show madd boy shaken at center
    with dissolve
    x "( Not after that. Not after being humiliated like that. )"
    
    # Aftb watches her with satisfaction
    show aftb focused at right_small
    with dissolve
    aftb_says "( See? She's looking away. She's ashamed. She knows what I was looking at. She knows what I was thinking about. )"
    show aftb expectant at right_small
    with dissolve
    aftb_says "( And she's not stopping me. She's accepting it. )"
    show aftb anticipatory at right_small
    with dissolve
    aftb_says "( I'm going to break her down slowly. Comment by comment. Moment by moment. )"
    show aftb apex predator at right_small
    with dissolve
    aftb_says "( Until she believes that this is normal. That being objectified by me is just how things are. )"
    show aftb methodical at right_small
    with dissolve
    aftb_says "( Until she's so used to being marked that she doesn't even notice anymore. )"

    # SCENE 3: Madd's shameful departure - internalized objectification
    scene scene_water_bottle_witness_aftb_event_1_scene_3
    with dissolve

    # Madd clutches her water bottle and prepares to leave
    show madd boy defeated at center
    with dissolve
    x "( I need to get out of here. )"
    show madd boy traumatized at center
    with dissolve
    x "( But even as I'm walking away, I can feel the weight of that comment on me. )"
    show madd boy scared at center
    with dissolve
    x "( It's not going away. It's not going to just disappear. )"
    show madd boy ashamed at center
    with dissolve
    x "( He said it in public. Where anyone could hear. )"
    show madd boy self loathing at center
    with dissolve
    x "( And I did nothing. I said nothing. I just stood there and let it happen. )"
    

    
    # Stat changes
    $ character_relations["aftb"]["lust"] += 5
    $ character_relations["aftb"]["identity"] += 1
    $ character_relations["aftb"]["dominance"] += 4
    $ madd_lust += 2
    $ madd_dominance -= 3
    $ secret_identity -= 0.5
    $ corruption += 0.5
    
    return

label water_bottle_witness_aftb_level_1_event_2:
    """Level 1 event 2 for water_bottle_witness_aftb - Greek towel boy and hostel relief fantasy"""
    
    # Set the location
    $ bg_image = get_location_image("floor_2_water_cooler", game_time, character_meal_times)
    scene expression bg_image
    with fade
    
    # Madd is bending over to get water
    show madd boy bent over at center
    with dissolve
    x "(I need to fill up my water bottle. I'm so thirsty...)"
    
    # SCENE 1: The unwitting display - predatory observation and arousal
    scene scene_water_bottle_witness_aftb_event_2_scene_1
    with dissolve
    
    # Aftb rounds the corner and sees Madd
    show aftb predatory gaze at right_small
    with dissolve
    
    # Aftb's immediate physical reaction and arousal
    show aftb intoxicated pleasure at right_small
    with dissolve
    aftb_says "( Oh... oh fuck. )"
    show aftb slow burn at right_small
    with dissolve
    aftb_says "( Look at that ass. He's bent over... )"
    show aftb aroused at right_small
    with dissolve
    aftb_says "( Instant hard-on. Just like that. )"
    
    # Aftb's fantasy about Greek towel boys
    show aftb marked prey at right_small
    with dissolve
    aftb_says "( Ancient Greek warriors... they had towel boys. )"
    show aftb masterful at right_small
    with dissolve
    aftb_says "( Young, beautiful boys who would serve them. Worship them. )"
    show aftb possessive at right_small
    with dissolve
    aftb_says "( That's what I need. That's exactly what would be perfect right now. )"
    show aftb calculating at right_small
    with dissolve
    aftb_says "( Someone small, delicate... someone like him. )"
    
    # Explicit oral fantasies
    show aftb calculating at right_small
    with dissolve
    aftb_says "( I can picture it so clearly... him on his knees... )"
    show aftb merciless at right_small
    with dissolve
    aftb_says "( His mouth wrapped around my cock... )"
    show aftb slow burn at right_small
    with dissolve
    aftb_says "( While I'm eating, just sitting there... serving me... )"
    show aftb controlling at right_small
    with dissolve
    aftb_says "( Or while I'm studying at my desk... he'd be under there... )"
    show aftb cruel at right_small
    with dissolve
    aftb_says "( His lips... the way they'd feel... the way he'd struggle at first... )"
    show aftb inevitable at right_small
    with dissolve
    aftb_says "( He doesn't even know that's going to be his purpose. His role. )"
    
    # Aftb notices Madd's appearance
    show aftb observant at right_small
    with dissolve
    aftb_says "( He's actually good-looking too. In that delicate, submissive way. )"
    show aftb satisfied at right_small
    with dissolve
    aftb_says "( Perfect for what I need. )"
    show aftb anticipatory at right_small
    with dissolve
    aftb_says "( He has no idea what's coming for him. )"
    
    # Hostel context - need for relief
    show aftb plotting at right_small
    with dissolve
    aftb_says "( Being in a hostel... so many people... so much stress... )"
    show aftb focused at right_small
    with dissolve
    aftb_says "( You need relief. Real relief. )"
    show aftb authoritative at right_small
    with dissolve
    aftb_says "( I need someone to take care of that for me. )"
    show aftb methodical at right_small
    with dissolve
    aftb_says "( Someone I can use whenever I want. )"
    
    # SCENE 2: The fantasy made visible - imagined servitude and degradation
    scene scene_water_bottle_witness_aftb_event_2_scene_2
    with dissolve
    
    # Marking and possession fantasy
    show aftb complete ownership at right_small
    with dissolve
    aftb_says "( I'm going to mark him like a dog marks his territory. )"
    show aftb dominant at right_small
    with dissolve
    aftb_says "( Make him my hostel bitch. )"
    show aftb smug at right_small
    with dissolve
    aftb_says "( Everyone will know he belongs to me. )"
    show aftb commanding at right_small
    with dissolve
    aftb_says "( He'll be my relief. My stress outlet. )"
    show aftb triumphant at right_small
    with dissolve
    aftb_says "( That's his purpose in this hostel. That's what he's for. )"
    
    # Explicit possession thoughts
    show aftb apex predator at right_small
    with dissolve
    aftb_says "( The way he's bent over right now... I could just... )"
    show aftb patient predator at right_small
    with dissolve
    aftb_says "( But not yet. I need to be smart about this. )"
    show aftb calculating at right_small
    with dissolve
    aftb_says "( I need to break him down first. Make him understand his place. )"
    show aftb inevitable at right_small
    with dissolve
    aftb_says "( By the time I'm done with him, he'll want to serve me. )"
    
    # Aftb adjusts himself, feeling the physical arousal
    show aftb intoxicated pleasure at right_small
    with dissolve
    aftb_says "( I'm so hard right now. Just thinking about it. )"
    show aftb marked prey at right_small
    with dissolve
    aftb_says "( About having a personal boy in this hostel. )"
    show aftb complete ownership at right_small
    with dissolve
    aftb_says "( Someone to mark. Someone to own. )"
    
    # Aftb speaks to Madd, interrupting her
    show aftb commanding at right_small
    with dissolve
    aftb_says "Everything okay, shawty? You look thirsty."
    
    # Madd startles and straightens up
    show madd boy shocked at center
    with dissolve
    x "( Oh! )"
    show madd boy surprised at center
    with dissolve
    x "( He... he was there the whole time? )"
    
    # Madd's shame as she realizes he was watching
    show madd boy embarrassed at center
    with dissolve
    x "( He was watching me bent over. How long? )"
    show madd boy humiliated at center
    with dissolve
    x "( Oh god... this is so embarrassing... )"
    
    # Madd responds nervously
    show madd boy nervous at center
    with dissolve
    x "Y-yes, I'm... I'm okay. Everything's fine."
    
    # Aftb's internal satisfaction at her embarrassment
    show aftb satisfied at right_small
    with dissolve
    aftb_says "( Look at him blush. So flustered. So easy. )"
    show aftb smug at right_small
    with dissolve
    aftb_says "( He knows I was watching. He's embarrassed. )"
    show aftb cruel at right_small
    with dissolve
    aftb_says "( That's exactly how I want him. Embarrassed. Uncertain. Submissive. )"
    show aftb confident at right_small
    with dissolve
    aftb_says "( This is going to be so easy. )"
    
    # SCENE 3: The casual interaction aftermath - power dynamic established
    scene scene_water_bottle_witness_aftb_event_2_scene_3
    with dissolve
    
    # Madd's internal conflict
    show madd boy conflicted at center
    with dissolve
    x "( How long was he watching? )"
    show madd boy scared at center
    with dissolve
    x "( What was he looking at? )"
    show madd boy dissociating at center
    with dissolve
    x "( I feel so exposed... so vulnerable right now... )"
    show madd boy paralyzed at center
    with dissolve
    x "( Like he can see right through me... )"
    
    # Casual conversation begins
    show aftb expectant at right_small
    with dissolve
    aftb_says "So how's life treating you? Classes going okay?"
    
    # Madd tries to act normal but struggles
    show madd boy uncertain at center
    with dissolve
    x "( Why is he asking me this? After... after he was just watching me like that? )"
    show madd boy processing at center
    with dissolve
    x "( This is so strange. So confusing. )"
    
    show madd boy resigned at center
    with dissolve
    x "It's... it's been okay. Busy with studies and everything."
    
    # Aftb's internal monologue continues about possession
    show aftb plotting at right_small
    with dissolve
    aftb_says "( He's trying to act normal, but he's rattled. )"
    show aftb focused at right_small
    with dissolve
    aftb_says "( I like that. I like the power I have over him just by being here. )"
    show aftb methodical at right_small
    with dissolve
    aftb_says "( Imagine when I really start working on him. )"
    show aftb triumphant at right_small
    with dissolve
    aftb_says "( When I make him understand that I own him. )"
    
    # More explicit possession fantasy
    show aftb complete ownership at right_small
    with dissolve
    aftb_says "( In this hostel... in these tight spaces... )"
    show aftb dominant at right_small
    with dissolve
    aftb_says "( He'll be my personal bitch. Everyone will know it. )"
    show aftb possessive at right_small
    with dissolve
    aftb_says "( He'll wear my mark. My scent. )"
    show aftb apex predator at right_small
    with dissolve
    aftb_says "( His only purpose will be to serve me. To satisfy me. )"
    
    # Aftb continues the conversation, testing her obedience
    show aftb commanding at right_small
    with dissolve
    aftb_says "You know, you seem like the type who could use some help. A friend to hang out with. I could be that."
    
    # Madd feels the weight of his attention
    show madd boy conflicted at center
    with dissolve
    x "( Is he... is he offering friendship? )"
    show madd boy uncertain at center
    with dissolve
    x "( Or is there something else in the way he said that? )"
    show madd boy scared at center
    with dissolve
    x "( Something darker... something possessive... )"
    
    # Madd's conflicted response
    show madd boy obedient at center
    with dissolve
    x "Th-that would be nice. Thank you."
    show madd boy submissive at center
    with dissolve
    x "( Why did I agree so quickly? )"
    show madd boy defeated at center
    with dissolve
    x "( There's something about him that makes me say yes to everything. )"
    show madd boy numb at center
    with dissolve
    x "( Like I'm under his control already. )"
    
    # Aftb's triumph
    show aftb triumphant at right_small
    with dissolve
    aftb_says "( Already saying yes. Good. That's the attitude I need. )"
    show aftb expectant at right_small
    with dissolve
    aftb_says "( Compliance. Obedience. )"
    show aftb patient predator at right_small
    with dissolve
    aftb_says "( In a few weeks, he won't even question me. )"
    show aftb inevitable at right_small
    with dissolve
    aftb_says "( In a few weeks, he'll be on his knees, serving me, and he'll think it's his idea. )"
    
    # Final exchange
    show aftb satisfied at right_small
    with dissolve
    aftb_says "Alright, well, see you around then. I'll catch you later, shawty."
    
    # Madd feels relief mixed with dread
    show madd boy relieved at center
    with dissolve
    x "( He's leaving. Thank god. )"
    show madd boy processing at center
    with dissolve
    x "( But something about that interaction... )"
    show madd boy shaken at center
    with dissolve
    x "( Something about the way he looked at me... )"
    show madd boy trembling at center
    with dissolve
    x "( Like I'm his property already. )"
    
    # Madd's final internal monologue
    show madd boy self loathing at center
    with dissolve
    x "( Why do I feel like I just made a deal with the devil? )"
    show madd boy dissociating at center
    with dissolve
    x "( Why do I feel like my life just changed? )"
    
    show madd boy broken at center
    with dissolve
    x "( And the worst part... the absolutely worst part... )"
    show madd boy desperate at center
    with dissolve
    x "( There was a part of me that didn't hate being looked at like that. )"
    show madd boy deep blush at center
    with dissolve
    x "( Like I was something valuable. Something desired. )"
    show madd boy confused consent at center
    with dissolve
    x "( Even if it was in the most degrading way possible. )"
    
    # Stat changes - higher due to explicit fantasies and possession intentions
    $ character_relations["aftb"]["lust"] += 5
    $ character_relations["aftb"]["identity"] += 1
    $ character_relations["aftb"]["dominance"] += 5
    $ madd_lust += 2
    $ madd_dominance -= 4
    $ secret_identity -= 0.5
    $ corruption += 0.5
    
    return


# ============================================
# WATER_BOTTLE_WITNESS_AFTB LEVEL 2 EVENTS
# ============================================

label water_bottle_witness_aftb_level_2_event_1:
    """Level 2 event 1 for water_bottle_witness_aftb"""
    return

label water_bottle_witness_aftb_level_2_event_2:
    """Level 2 event 2 for water_bottle_witness_aftb"""
    return


# ============================================
# WATER_BOTTLE_WITNESS_AFTB LEVEL 3 EVENTS
# ============================================

label water_bottle_witness_aftb_level_3_event_1:
    """Level 3 event 1 for water_bottle_witness_aftb"""
    return

label water_bottle_witness_aftb_level_3_event_2:
    """Level 3 event 2 for water_bottle_witness_aftb"""
    return


# ============================================
# WATER_COOLER_TALK_AFTB LEVEL 1 EVENTS
# ============================================

label water_cooler_talk_aftb_level_1_event_1:
    """Level 1 event 1 for water_cooler_talk_aftb - Aftb watches Madd drink at water cooler"""
    
    # Set the location
    $ bg_image = get_location_image("floor_2_water_cooler", game_time, character_meal_times)
    scene expression bg_image
    with fade
    
    # Madd is drinking water from her bottle at the water cooler
    show madd boy nervous at center
    with dissolve
    x "(I'm so thirsty. Let me refill my bottle and take a quick drink...)"
    
    # SCENE 1: Madd drinks while Aftb watches - predatory focus on her throat
    scene scene_water_cooler_talk_aftb_event_1_scene_1
    with dissolve
    
    # Aftb is standing nearby, leaning against the wall
    show aftb patient at right_small
    with dissolve
    
    show aftb observant at right_small
    with dissolve
    aftb_says "Hey, refilling your bottle too, huh?"
    
    show madd boy hesitant at center
    with dissolve
    x "Oh, yeah... just getting some water."
    
    # Madd continues drinking, tilting her head back slightly
    show aftb predatory gaze at right_small
    with dissolve
    show madd boy embarrassed at center
    with dissolve
    x "(The water is cold and refreshing... I can feel it going down my throat...)"
    
    # SCENE 2: The moment of awareness - her throat becomes a target
    scene scene_water_cooler_talk_aftb_event_1_scene_2
    with dissolve
    
    # Aftb's eyes lock onto her throat
    show aftb aroused at right_small
    with dissolve
    
    # Aftb's explicit internal monologue about her throat and mouth
    show aftb intoxicated pleasure at right_small
    with dissolve
    aftb_says "( Oh... oh fuck... )"
    aftb_says "( Look at that throat. The way it's contracting as the water goes down... )"
    aftb_says "( I can see her swallowing. The muscles working. The way her mouth opens to take the liquid... )"
    
    show aftb calculating at right_small
    with dissolve
    aftb_says "( I want to shove my dick down that throat right now. )"
    aftb_says "( I want to feel her choking on me. Feel my cock sliding down her esophagus. )"
    
    # Aftb's possession fantasies intensify
    aftb_says "( She's drinking water right now... but soon... soon she'll be drinking something else. )"
    aftb_says "( My cum. Her mouth will be full of my essence. She'll be swallowing me. )"
    aftb_says "( Every drop of me. Every single drop will go into her body. I'll own her from the inside out. )"
    
    # Explicit marking fantasies
    show aftb merciless at right_small
    with dissolve
    aftb_says "( I want to mark her with my piss too. Fill her mouth with it. Make her drink it all. )"
    aftb_says "( Make her so full of me that she can taste nothing else. That water she's drinking now? )"
    aftb_says "( It's nothing compared to what I'll make her swallow. )"
    aftb_says "( She'll be so covered in my fluids that the entire hostel will smell me on her. )"
    
    # More degrading possession thoughts
    show aftb contemptuous at right_small
    with dissolve
    aftb_says "( Once she belongs to me completely, drinking my essence will be her job. )"
    aftb_says "( That's all that mouth will be good for. My personal cum dumpster. )"
    aftb_says "( She'll open her mouth, and I'll fill it with whatever I want - cum, piss, doesn't matter. )"
    aftb_says "( She'll swallow it all because that's what belongings do. )"
    aftb_says "( That's what she'll be - my property. My marked, owned, completely broken property. )"
    
    # SCENE 3: Her flustered departure - marked by his gaze alone
    scene scene_water_cooler_talk_aftb_event_1_scene_3
    with dissolve
    
    # Madd finishes drinking and notices his stare
    show madd boy flustered at center
    with dissolve
    x "(I finish my drink and finally notice... he's staring at me.)"
    
    show aftb possessive at right_small
    with dissolve
    show madd boy confused at center
    with dissolve
    x "(Why is he looking at me like that? It's so... intense. His eyes are so focused on... on my...)"
    
    # Madd's discomfort
    show aftb slow burn at right_small
    with dissolve
    show madd boy scared at center
    with dissolve
    x "(On my face? My mouth? Why is he looking at my mouth like that?)"
    x "(There's something so possessive in his gaze... something that makes me feel like I'm being... evaluated.)"
    
    show aftb patient predator at right_small
    with dissolve
    show madd boy nervous at center
    with dissolve
    
    # Aftb continues staring
    show aftb marked prey at right_small
    with dissolve
    aftb_says "( God, I can't stop thinking about it. )"
    aftb_says "( Her mouth. Those lips. That throat. The way she just swallowed that water so easily. )"
    aftb_says "( All that without any resistance, any hesitation. )"
    aftb_says "( That's the kind of obedience I need. That's the kind of submission I'm going to break her into. )"
    
    # Aftb breaks the silence with casual conversation
    show aftb focused at right_small
    with dissolve
    aftb_says "You know, the water quality here is pretty questionable. You shouldn't be drinking that stuff too much."
    
    # Madd looks at him, confused by the sudden normalcy
    show madd boy uncertain at center
    with dissolve
    x "Huh? The water? I mean... it tastes fine to me."
    
    # Aftb's internal monologue continues
    show aftb calculating at right_small
    with dissolve
    aftb_says "( She's trying to act normal. Trying to pretend she didn't notice how intensely I was staring. )"
    aftb_says "( But she noticed. I could see the discomfort. I could see her realizing something is off. )"
    aftb_says "( That's good. That means she's already starting to understand that she's not safe around me. )"
    aftb_says "( She's starting to feel that predatory energy. That ownership. )"
    
    # Aftb steps closer to the water cooler, positioning himself next to her
    show aftb methodical at right_small
    with dissolve
    aftb_says "Yeah, but there's a lot of impurities. Bacteria and stuff. It can make you sick if you're not careful."
    
    # Madd shifts uncomfortably
    show madd boy hesitant at center
    with dissolve
    x "Oh... I didn't know that. Should I be worried?"
    
    # Madd's internal confusion
    show aftb observant at right_small
    with dissolve
    show madd boy nervous at center
    with dissolve
    x "(Why is he suddenly concerned about the water quality? And why is he standing so close?)"
    x "(There's something about the way he's looking at me... like I'm... like I'm something he wants to consume.)"
    x "(That sounds crazy. He's just talking about water. But the way he's looking at my mouth...)"
    
    # Madd's shame spiral
    show aftb slow burn at right_small
    with dissolve
    show madd boy blush at center
    with dissolve
    x "(Oh god, why am I thinking about his eyes on my mouth?)"
    x "(Why do I keep thinking about the way he was staring at my throat when I was drinking?)"
    x "(What is wrong with me?)"
    
    show aftb satisfied at right_small
    with dissolve
    show madd boy ashamed at center
    with dissolve
    
    # Aftb's explicit thoughts continue
    show aftb cruel at right_small
    with dissolve
    aftb_says "( She's thinking about it. I can see it in her face. She's thinking about how I was watching her. )"
    aftb_says "( She's embarrassed. Flustered. )"
    aftb_says "( And that's only the beginning. )"
    aftb_says "( I'm going to make her so used to being watched that she won't even flinch anymore. )"
    aftb_says "( I'm going to make her so dependent on my attention, my marking, that she'll crave it. )"
    
    # More degrading fantasies
    show aftb commanding at right_small
    with dissolve
    aftb_says "( Right now she's drinking clean water from a bottle. )"
    aftb_says "( Soon she'll be drinking directly from me. My cock. My piss. Whatever I want to give her. )"
    aftb_says "( And she'll be grateful for it. Because by then, she'll belong to me completely. )"
    aftb_says "( She'll understand that her only purpose is to serve my needs. To take my mark. To become one with my essence. )"
    
    # Aftb reaches for the water dispenser, his arm brushing close to her
    show aftb confident at right_small
    with dissolve
    
    # Madd feels his proximity
    show aftb dominant at right_small
    with dissolve
    show madd boy flustered at center
    with dissolve
    x "(He's so close now... I can feel the heat from his body...)"
    x "(This is... this is making me feel so strange. So uncomfortable.)"
    
    show aftb smug at right_small
    with dissolve
    show madd boy salivating at center
    with dissolve
    x "(No. I'm not going to think about that. What is wrong with me?)"
    
    # Aftb speaks while getting his water
    show aftb contemptuous at right_small
    with dissolve
    aftb_says "You should probably start drinking bottled water instead. Or at least boiled water."
    
    # Madd responds weakly
    show madd boy obedient at center
    with dissolve
    x "Y-yeah, maybe you're right. I'll look into that."
    
    # Aftb's final internal monologue
    show aftb anticipatory at right_small
    with dissolve
    aftb_says "( Perfect. She's agreeing with me. She's already starting to depend on my guidance. )"
    aftb_says "( Soon, I'll be guiding her in much more intimate ways. )"
    aftb_says "( Her mouth. Her throat. Her entire body will be marked by me, filled with me. )"
    
    show aftb intoxicated pleasure at right_small
    with dissolve
    aftb_says "( The thought of her drinking my cum mixed with my piss... the degradation... the complete ownership... )"
    aftb_says "( God, I can't wait. )"
    
    # Madd tries to leave
    show madd boy desperate at center
    with dissolve
    x "(I need to get away from here. Away from him. Away from the way he's looking at me.)"
    x "(But even as I'm about to leave, I can feel his eyes on me again.)"
    x "(On my mouth. On my throat. Like he's imagining something about me.)"
    
    # Madd's final shame
    show aftb marked prey at right_small
    with dissolve
    show madd boy embarrassed at center
    with dissolve
    x "(What is he thinking about? Why does that look in his eyes make me feel like... like I'm about to be consumed?)"
    x "(And why... why does some small, disgusting part of me want to know?)"
    
    show aftb apex predator at right_small
    with dissolve
    show madd boy conflicted at center
    with dissolve
    
    # Aftb watches her leave
    show aftb satisfied at right_small
    with dissolve
    aftb_says "( Go ahead. Enjoy your water. )"
    aftb_says "( But soon, the only thing you'll be drinking is me. )"
    
    # Stat changes
    $ character_relations["aftb"]["lust"] += 4
    $ character_relations["aftb"]["identity"] += 1
    $ character_relations["aftb"]["dominance"] += 4
    $ madd_lust += 2
    $ madd_dominance -= 3
    $ secret_identity -= 0.5
    $ corruption += 0.5
    
    return

label water_cooler_talk_aftb_level_1_event_2:
    """Level 1 event 2 for water_cooler_talk_aftb - Aftb establishes owner-pet dynamic at water cooler"""
    
    # Set the location
    $ bg_image = get_location_image("floor_2_water_cooler", game_time, character_meal_times)
    scene expression bg_image
    with fade
    
    # Madd is drinking water from her plastic bottle at the water cooler
    show madd boy nervous at center
    with dissolve
    x "(I'm refilling my water bottle and taking a quick drink...)"
    
    # Aftb appears beside her
    show aftb observant at right_small
    with dissolve
    aftb_says "Hey, you there."
    
    show madd boy surprised at center
    with dissolve
    x "Oh, Aftb. Hi."
    
    # Aftb's eyes focus on her bottle
    show aftb observant at right_small
    with dissolve
    aftb_says "You know, you shouldn't keep water in plastic bottles too long. The chemicals leach into the water."
    
    # Madd looks at her bottle, confused
    show madd boy confused at center
    with dissolve
    x "Oh... I didn't know that. How long is too long?"
    
    # Aftb steps closer, his voice taking on a more commanding tone
    show aftb authoritative at right_small
    with dissolve
    aftb_says "Well, the longer it sits, the worse it gets. You should drink fresh water directly from the source when you can."
    
    # Madd nods, not sure where this is going
    show madd boy uncertain at center
    with dissolve
    x "I see... so what should I do instead?"
    
    # Aftb cups his hand under the water cooler tap
    show aftb commanding at right_small
    with dissolve
    aftb_says "Simple. You can drink directly from the tap here. Just cup your hand like this."
    
    # SCENE 1: Aftb establishes control - hand cupped under water, commanding presence
    scene scene_water_cooler_talk_aftb_event_2_scene_1
    with dissolve
    
    # He demonstrates, holding his cupped hand under the cooler
    x "(He's... he's holding his hand out to me...)"
    
    # Aftb's internal monologue about establishing control
    aftb_says "( Perfect. This is exactly what I need. )"
    aftb_says "( She's going to drink from my hand. )"
    aftb_says "( This is about establishing the hierarchy. I give orders, she obeys. )"
    aftb_says "( I decide what she drinks, how she drinks it, when she drinks it. )"
    aftb_says "( This is the beginning of the owner-pet dynamic. )"
    
    # More explicit ownership thoughts
    aftb_says "( She doesn't even realize what's happening right now. )"
    aftb_says "( She thinks I'm just being helpful. But I'm really establishing myself as her master. )"
    aftb_says "( Soon, drinking from my hand will become normal for her. )"
    aftb_says "( And then I can progress to other things. Other ways to mark her. Other ways to make her understand she belongs to me. )"
    
    # Aftb gestures for her to drink
    show aftb expectant at right_small
    with dissolve
    aftb_says "Go on. Drink from my hand. It's cleaner and fresher than keeping water in a plastic bottle."
    
    # Madd's immediate embarrassment
    show madd boy embarrassed at center
    with dissolve
    x "( Drink... from his hand? )"
    x "( But that's... that's so intimate... )"
    x "( Everyone around here could see... )"
    
    # Madd's shame spiral
    show madd boy blush at center
    with dissolve
    x "( Why am I feeling so flustered about this? It's just water. It's just his hand. )"
    x "( But there's something about the way he said it. Like it's not a request. Like it's an order. )"
    x "( Like I don't have a choice. )"
    
    # Madd hesitates
    x "I... um... that's... I don't know if I..."
    show madd boy nervous at center
    with dissolve
    
    # SCENE 2: Madd's internal conflict - hesitation before submission
    scene scene_water_cooler_talk_aftb_event_2_scene_2
    with dissolve
    
    # Aftb's internal response to her hesitation
    aftb_says "( She's hesitating. Uncomfortable. )"
    aftb_says "( Good. That discomfort is important. )"
    aftb_says "( It means she understands on some level that this is a power move. )"
    aftb_says "( But she won't refuse. She's too polite. Too concerned about being rude. )"
    aftb_says "( That's exactly the kind of weakness I can exploit. )"
    
    # Aftb applies gentle pressure
    show aftb smirk at right_small
    with dissolve
    aftb_says "Come on, it's not that big of a deal. Just drink from my hand. It's actually more practical this way."
    
    # Madd's internal conflict intensifies
    show madd boy conflicted at center
    with dissolve
    x "( He's right... it is more practical... )"
    x "( But why does it feel like I'm about to cross some kind of line? )"
    x "( Why does my heart feel like it's racing? )"
    
    # Madd finally relents
    x "O-okay... if you say so..."
    show madd boy reluctant at center
    with dissolve
    
    # Aftb's triumph
    aftb_says "( Yes. That's it. Obedience. )"
    aftb_says "( She's choosing to submit. Even though she's uncomfortable, even though she knows something is off about this, she's doing it anyway. )"
    aftb_says "( That's the key to breaking someone. Making them do things they're not comfortable with, one small step at a time. )"
    aftb_says "( Until they stop questioning. Until they just accept whatever I tell them to do. )"
    
    # More explicit ownership fantasies
    aftb_says "( Right now it's just water from my hand. )"
    aftb_says "( But soon it will be so much more. )"
    aftb_says "( My cum in her mouth. My piss for her to swallow. My entire essence for her to consume and become one with. )"
    aftb_says "( She'll be my pet. My property. My marked, owned, broken little thing. )"
    
    # Madd approaches, deeply embarrassed
    show madd boy humiliated at center
    with dissolve
    x "( This is so embarrassing... )"
    x "( What if someone sees us? What would they think? )"
    x "( What will they think of me if they see me... drinking from his hand like some kind of... )"
    show madd boy ashamed at center
    with dissolve
    
    # Aftb holds his cupped hand steady, filled with water from the cooler
    show aftb possessive at right_small
    with dissolve
    
    # SCENE 3: The power transfer - she drinks from his hand
    scene scene_water_cooler_talk_aftb_event_2_scene_3
    with dissolve
    
    # Madd leans in, her face flushing deeply
    show madd boy deep blush at center
    with dissolve
    x "( I'm actually... I'm actually going to do this... )"
    x "( Why? Why can't I just say no? Why am I so submissive to him? )"
    
    # Aftb's internal monologue about her submission
    aftb_says "( She's bending to my will without even knowing it. )"
    aftb_says "( This is beautiful. This is power. )"
    aftb_says "( I'm establishing the rules. I'm showing her where the hierarchy lies. )"
    aftb_says "( And she's accepting it. She's accepting that I'm in control. )"
    
    # Madd drinks from his hand
    show madd boy submissive at center
    with dissolve
    x "( The water... it's touching my lips... )"
    x "( I can feel his hand under my mouth... his skin... )"
    x "( Oh god... this is so strange... )"
    
    # The intimate moment
    x "( I'm drinking from his hand. Like a pet. Like he said. )"
    x "( And the worst part is... I feel so... so owned right now. )"
    show madd boy obedient at center
    with dissolve
    x "( His hand is under my mouth. I'm completely dependent on him at this moment. )"
    x "( If he moves his hand away, I have nothing. )"
    x "( I'm vulnerable. I'm submissive. I'm... his. )"
    
    # Aftb watches with intense satisfaction
    show aftb triumphant at right_small
    with dissolve
    aftb_says "( Perfect. Absolutely perfect. )"
    aftb_says "( She's drinking from my hand. She's accepting my authority over her. )"
    aftb_says "( This is the beginning of complete ownership. )"
    
    # Detailed fantasies about breaking her down
    aftb_says "( I can already see it... in a few weeks... )"
    aftb_says "( She'll be so conditioned to my orders that she won't even hesitate anymore. )"
    aftb_says "( 'Drink from my hand' and she'll be there immediately, mouth open, ready to accept whatever I give her. )"
    aftb_says "( 'Get on your knees' and she'll drop without question. )"
    aftb_says "( 'Take this in your mouth' and she'll do it, grateful for the attention, grateful for the ownership. )"
    
    # More degrading fantasies
    aftb_says "( By then, she won't even need water. She'll just need me. )"
    aftb_says "( She'll need to serve me. To be marked by me. )"
    aftb_says "( And she'll crave it. Every part of her will crave the degradation, the possession, the complete loss of control. )"
    aftb_says "( She'll be my perfect little pet. My hostel bitch. My owned, marked, completely broken property. )"
    
    # More possession-focused thoughts
    aftb_says "( The way she's looking at me right now... confused but compliant... )"
    aftb_says "( That's exactly how I want her. Never quite understanding why she's doing what I tell her, but doing it anyway. )"
    aftb_says "( That's the psychology of complete domination. Making someone submit so thoroughly that they don't even question it anymore. )"
    
    # Madd finishes drinking and pulls back
    show madd boy defeated at center
    with dissolve
    x "( I... I'm finished... )"
    x "( I just drank from his hand. I just did what he told me to do without even thinking about it. )"
    
    # Madd's deep shame
    show madd boy shaken at center
    with dissolve
    x "( What is happening to me? )"
    x "( Why did I do that so easily? Why didn't I refuse? )"
    x "( I feel like... like I just gave him permission to own me. )"
    show madd boy conflicted at center
    with dissolve
    x "( And the most disturbing part... some small part of me enjoyed that. Enjoyed the submissive feeling. )"
    x "( Enjoyed being told what to do. Enjoyed having no choice. )"
    
    # Aftb speaks casually after the act
    show aftb satisfied at right_small
    with dissolve
    aftb_says "See? Much better than plastic bottles, right? And it's good for you to listen to advice. Keeps you healthy."
    
    # The double meaning is not lost on either of them
    show madd boy paralyzed at center
    with dissolve
    x "Y-yes... thank you... for the advice..."
    
    # Aftb's final internal monologue
    aftb_says "( She called it 'advice.' As if this was innocent. As if I wasn't literally demonstrating ownership. )"
    aftb_says "( She's already reframing it in her mind to make it less terrifying. )"
    aftb_says "( That's the power of slow, methodical domination. )"
    aftb_says "( One small act of submission at a time, and before long, she won't even recognize the cage I've built around her. )"
    aftb_says "( She'll just think that listening to me, obeying me, serving me... is normal. )"
    aftb_says "( And by then, it will be too late for her to escape. She'll already be mine. )"
    
    # Madd tries to leave
    show madd boy desperate at center
    with dissolve
    x "( I need to get away from here. Away from him. )"
    x "( But even as I'm walking, I can still feel his hand on my lips. )"
    x "( Still taste the water that came from his touch. )"
    x "( Still feel the weight of what just happened. )"
    
    # Final thoughts
    show madd boy resigned at center
    with dissolve
    x "( I drank from his hand. )"
    x "( That's all it took. One small act of submission. )"
    x "( And now I feel like I belong to him. )"
    x "( What am I going to do? )"
    
    # Stat changes - higher dominance due to successful establishment of owner-pet dynamic
    $ character_relations["aftb"]["lust"] += 3
    $ character_relations["aftb"]["identity"] += 1
    $ character_relations["aftb"]["dominance"] += 5
    $ madd_lust += 2
    $ madd_dominance -= 4
    $ secret_identity -= 0.5
    $ corruption += 0.5
    
    return


# ============================================
# WATER_COOLER_TALK_AFTB LEVEL 2 EVENTS
# ============================================

label water_cooler_talk_aftb_level_2_event_1:
    """Level 2 event 1 for water_cooler_talk_aftb"""
    return

label water_cooler_talk_aftb_level_2_event_2:
    """Level 2 event 2 for water_cooler_talk_aftb"""
    return


# ============================================
# WATER_COOLER_TALK_AFTB LEVEL 3 EVENTS
# ============================================

label water_cooler_talk_aftb_level_3_event_1:
    """Level 3 event 1 for water_cooler_talk_aftb"""
    return

label water_cooler_talk_aftb_level_3_event_2:
    """Level 3 event 2 for water_cooler_talk_aftb"""
    return


# ============================================
# INTERACT_AFTB_MESS_HALL_MET LEVEL 1 EVENTS
# ============================================

label interact_aftb_mess_hall_met_level_1_event_1:
    """Level 1 event 1 for interact_aftb_mess_hall_met - Aftb watches Madd eat in mess hall"""
    
    # Set the mess hall scene
    scene scene_messhall_breakfast
    with fade
    
    # Madd sits down across from Aftb
    show madd boy happy at left_small
    with dissolve
    x "I find a seat across from Aftb and start setting down my food tray."
    
    # SCENE 1: Madd eats while Aftb watches her mouth - predatory focus on her eating
    scene scene_interact_aftb_mess_hall_met_event_1_scene_1
    with dissolve
    
    # Aftb is already seated, watching her
    show aftb observant at right_small
    with dissolve
    aftb_says "Hey, come sit here. I saved you a spot."
    
    show madd boy happy at left_small
    with dissolve
    x "Oh, thanks! That's nice of you."
    
    # Madd starts eating
    show aftb predatory gaze at right_small
    with dissolve
    show madd boy hesitant at left_small
    with dissolve
    x "(I begin eating, bringing food to my mouth...)"
    
    # Aftb's immediate fixation on her mouth
    show aftb aroused at right_small
    with dissolve
    
    # Aftb's explicit internal monologue about her mouth
    show aftb intoxicated pleasure at right_small
    with dissolve
    aftb_says "( Oh god... look at that... )"
    aftb_says "( The way she's eating... the way her mouth opens... )"
    aftb_says "( How her lips close around the fork... )"
    
    # Aftb's porn-inspired fantasies
    show aftb calculating at right_small
    with dissolve
    aftb_says "( This reminds me of a video I watched... )"
    aftb_says "( A girl, on her knees, mouth open, ready to take... )"
    aftb_says "( I wonder how her mouth would feel... )"
    aftb_says "( Wet, warm, tight... sliding up and down my cock... )"
    
    # Madd continues eating, unaware of his intense stare
    show madd boy uncertain at left_small
    with dissolve
    x "(I'm just eating my meal, not noticing how intently he's watching me...)"
    
    # Aftb's detailed fantasies escalate
    show aftb slow burn at right_small
    with dissolve
    aftb_says "( I can see her swallowing... )"
    aftb_says "( The muscles in her throat... the way her neck moves... )"
    aftb_says "( I want to feel my cock sliding down that throat... )"
    aftb_says "( I want to watch her eyes water as she gags on me... )"
    
    # SCENE 2: The moment of awareness - caught in his predatory gaze
    scene scene_interact_aftb_mess_hall_met_event_1_scene_2
    with dissolve
    
    # More explicit possession fantasies about the future
    show aftb possessive at right_small
    with dissolve
    aftb_says "( When I finally break her... when she's completely mine... )"
    aftb_says "( We won't eat in here anymore. We'll eat in my room. )"
    aftb_says "( Private. Just the two of us. )"
    aftb_says "( And her meals... her meals will come directly from me. )"
    
    # Detailed fantasy about feeding her
    show aftb contemptuous at right_small
    with dissolve
    aftb_says "( I'll chew the food first... nice and slow... )"
    aftb_says "( And then I'll spit it directly into her mouth... )"
    aftb_says "( She'll swallow what I've already chewed... what I've already processed... )"
    aftb_says "( She'll be eating my spit... my food... becoming one with me... )"
    
    # Madd takes another bite, and Aftb watches with intense focus
    show madd boy nervous at left_small
    with dissolve
    x "(I don't notice him staring at me as I take another bite...)"
    
    # Aftb's fantasies about her drinking
    show aftb merciless at right_small
    with dissolve
    aftb_says "( And as for drinking... )"
    aftb_says "( She won't need water. She won't need juice. )"
    aftb_says "( The only thing she'll drink is me. )"
    aftb_says "( My cum. My piss. Whatever I decide to give her. )"
    aftb_says "( That will be her sustenance. That will be her life. )"
    
    # More degrading fantasy scenarios
    show aftb methodical at right_small
    with dissolve
    aftb_says "( I picture her, completely dependent on me for everything... )"
    aftb_says "( Every bite of food... my spit. Every drink of water... my bodily fluids. )"
    aftb_says "( She'll be so thoroughly owned that she won't even be a separate person anymore. )"
    aftb_says "( She'll just be an extension of me. A tool for my satisfaction. )"
    
    # Aftb's internal monologue about control
    show aftb commanding at right_small
    with dissolve
    aftb_says "( Right now she's eating normal food, unaware of her fate... )"
    aftb_says "( But soon... soon she'll understand that her only purpose is to consume what I give her. )"
    aftb_says "( To take everything I put in her mouth without question. )"
    aftb_says "( To become so addicted to my essence that she can't imagine living without it. )"
    
    # More possession-focused thoughts
    show aftb focused at right_small
    with dissolve
    aftb_says "( The way she's chewing... the way her jaw moves... )"
    aftb_says "( I'm going to own that mouth. I'm going to own every part of her. )"
    aftb_says "( She'll be my meal dispenser's companion... no, worse... she'll be my waste disposal. )"
    aftb_says "( Everything I produce, everything I don't want, she'll consume. )"
    
    # Madd notices his gaze
    show aftb observant at right_small
    with dissolve
    show madd boy uncertain at left_small
    with dissolve
    x "(I suddenly feel like someone's watching me... I glance up...)"
    
    # Madd sees him staring
    show aftb satisfied at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "Um... is something wrong?"
    
    # Aftb's immediate response
    show aftb patient at right_small
    with dissolve
    aftb_says "What? No, nothing's wrong. I'm just watching you eat. You have a nice appetite."
    
    # Madd's innocent interpretation
    show madd boy blush at left_small
    with dissolve
    x "Oh... um... thanks, I guess?"
    
    # Madd doesn't understand the darker implications
    x "(He's just... complimenting my eating? That's... actually kind of sweet...)"
    show madd boy happy at left_small
    with dissolve
    
    # Aftb's internal response to her innocence
    show aftb calculating at right_small
    with dissolve
    aftb_says "( She has no idea. )"
    aftb_says "( She's completely innocent, completely unaware of what I'm thinking about her. )"
    aftb_says "( That innocence... that naivety... it makes me want her even more. )"
    aftb_says "( She's ripe for corruption. Ripe for ownership. )"
    
    # Aftb continues to watch as she eats
    show aftb predatory gaze at right_small
    with dissolve
    aftb_says "You should eat more, actually. Building strength requires fuel. Lots of fuel."
    
    # The double meaning is there but Madd misses it
    show madd boy nervous at left_small
    with dissolve
    x "Oh, okay. I'll eat more then."
    
    # Madd continues eating, still innocent
    show aftb slow burn at right_small
    with dissolve
    x "(I take larger bites, trying to follow his advice...)"
    
    # SCENE 3: Her continued eating under his possessive dominance
    scene scene_interact_aftb_mess_hall_met_event_1_scene_3
    with dissolve
    
    # Aftb's explicit final fantasies
    show aftb intoxicated pleasure at right_small
    with dissolve
    aftb_says "( Yes... eat more... )"
    aftb_says "( Build your strength... because when I own you completely, you're going to need all the energy you can get. )"
    aftb_says "( You'll be servicing me constantly... your mouth, your body, every part of you will be dedicated to my satisfaction. )"
    
    # More degrading possession thoughts
    show aftb apex predator at right_small
    with dissolve
    aftb_says "( I'm going to break her so thoroughly that she won't even remember what it was like to be free. )"
    aftb_says "( She'll think that serving me is the natural order. )"
    aftb_says "( That being owned by me is better than any other existence. )"
    aftb_says "( That her only worth is in how well she can satisfy me. )"
    
    # Aftb's final internal monologue
    show aftb complete ownership at right_small
    with dissolve
    aftb_says "( Right now she's sitting across from me, eating her meal, completely unaware. )"
    aftb_says "( But soon... very soon... the only meals she'll know are the ones I force into her mouth. )"
    aftb_says "( The only drinks she'll know are my bodily fluids. )"
    aftb_says "( She'll be my property. My owned, marked, broken property. )"
    aftb_says "( And by the time I'm done with her, she'll thank me for it. )"
    
    # Madd finishes her meal
    show madd boy satisfied at left_small
    with dissolve
    x "(I finish my meal, still unaware of what he's been thinking about...)"
    
    # Aftb speaks again
    show aftb triumphant at right_small
    with dissolve
    aftb_says "Good. You're eating well. You're going to need that strength. Trust me."
    
    # Madd nods, still innocent
    show madd boy obedient at left_small
    with dissolve
    x "Okay, I will. Thanks for the advice."
    
    # As they leave the mess hall
    show aftb expectant at right_small
    with dissolve
    x "(I have no idea what he meant by that, but I appreciate his concern for my health...)"
    show madd boy resigned at left_small
    with dissolve
    
    # Final Aftb internal monologue
    show aftb marked prey at right_small
    with dissolve
    aftb_says "( Soon. Very soon. )"
    aftb_says "( She won't be eating normal food anymore. She won't be drinking normal water. )"
    aftb_says "( She'll be mine. Completely. Utterly. Irrevocably. )"
    
    # Stat changes
    $ character_relations["aftb"]["lust"] += 4
    $ character_relations["aftb"]["identity"] += 1
    $ character_relations["aftb"]["dominance"] += 4
    $ madd_lust += 1
    $ madd_dominance -= 2
    $ secret_identity -= 0.5
    $ corruption += 0.5
    
    $ game_time.advance_time(minutes=30)
    return

label interact_aftb_mess_hall_met_level_1_event_2:
    """Level 1 event 2 for interact_aftb_mess_hall_met - Aftb teaches hand-eating to establish dominance"""
    
    # Set the mess hall scene
    scene scene_messhall_breakfast
    with fade
    
    # Madd sits down across from Aftb with her meal
    show madd boy happy at left_small
    with dissolve
    x "I find a seat across from Aftb in the mess hall."
    
    # Aftb watches her with interest
    show aftb observant at right_small
    with dissolve
    aftb_says "Hey, come join me."
    
    show madd boy happy at left_small
    with dissolve
    x "Oh, thanks!"
    
    # Madd picks up her spoon to start eating rice
    show madd boy uncertain at left_small
    with dissolve
    x "(I reach for my spoon to eat the rice...)"
    
    # Aftb suddenly stops her
    show aftb dominant at right_small
    with dissolve
    aftb_says "Wait, wait. What are you doing?"
    
    show madd boy confused at left_small
    with dissolve
    x "Um... eating? With a spoon?"
    
    # Aftb's internal monologue about the opportunity
    show aftb dominant at right_small
    with dissolve
    aftb_says "( Perfect. This is the perfect moment. )"
    aftb_says "( I can use her respect for different cultures against her. )"
    aftb_says "( She won't want to seem disrespectful. She won't want to offend me. )"
    aftb_says "( And I can use that to make her do exactly what I want. )"
    
    # Aftb explains with cultural authority
    show aftb commanding at right_small
    with dissolve
    aftb_says "You see, where I'm from, we don't use spoons to eat rice. We eat with our hands. It's how it's meant to be eaten."
    
    # Madd's curious response
    show madd boy think at left_small
    with dissolve
    x "Oh? Really? I didn't know that. How... how do you eat it with your hands?"
    
    # Aftb's internal satisfaction at her compliance
    show aftb calculating at right_small
    with dissolve
    aftb_says "( She's already interested. Already willing to learn. Already willing to let me guide her. )"
    aftb_says "( This is exactly how you break someone down. Through their politeness. Through their desire not to offend. )"
    
    # Aftb demonstrates
    show aftb methodical at right_small
    with dissolve
    aftb_says "It's simple. You take the rice in your hand like this..."
    
    # SCENE 1: Aftb extends his rice-filled hand - establishing command through culture
    scene scene_interact_aftb_mess_hall_met_event_2_scene_1
    with dissolve
    
    # Aftb takes rice in his hand
    x "(He's taking rice in his palm, showing me...)"
    
    # But instead of bringing it to his own mouth, he points it toward hers
    show aftb expectant at right_small
    with dissolve
    aftb_says "And then... you eat it."
    
    # He's pointing the rice-filled hand at Madd, not at his own mouth
    show aftb possessive at right_small
    with dissolve
    x "(...)"
    
    # Madd's immediate shock and embarrassment
    show madd boy shocked at left_small
    with dissolve
    x "( He's... he's pointing the rice at me... )"
    x "( Like he wants me to... to eat from his hand? )"
    
    # Madd's shame spiral
    show aftb patient predator at right_small
    with dissolve
    show madd boy ashamed at left_small
    with dissolve
    x "( But... but everyone in the mess hall can see... )"
    x "( This is so embarrassing... )"
    x "( He's asking me to eat from his hand... in front of everyone... )"
    
    # SCENE 2: Madd's internal conflict - hesitation before the power transfer
    scene scene_interact_aftb_mess_hall_met_event_2_scene_2
    with dissolve
    
    # Aftb's internal monologue about the power move
    show aftb contemptuous at right_small
    with dissolve
    aftb_says "( She's embarrassed. Shocked. )"
    aftb_says "( But she's not refusing. )"
    aftb_says "( Because she doesn't want to be disrespectful to my culture. )"
    aftb_says "( That's the key. Use her politeness against her. Use her respect against her. )"
    aftb_says "( Make her feel like she has no choice but to submit. )"
    
    # More of Aftb's explicit thoughts
    show aftb merciless at right_small
    with dissolve
    aftb_says "( This is step two of breaking her. )"
    aftb_says "( First, drinking from my hand at the water cooler. )"
    aftb_says "( Now, eating from my hand in front of witnesses. )"
    aftb_says "( Soon, she'll be so conditioned to taking things from my hand that she won't even hesitate. )"
    aftb_says "( She'll just open her mouth and accept whatever I give her. )"
    
    # Aftb waits with his hand extended
    show aftb smirk at right_small
    with dissolve
    
    # Madd's internal conflict
    show aftb marked prey at right_small
    with dissolve
    show madd boy conflicted at left_small
    with dissolve
    x "( I can't refuse... he's showing me his culture... )"
    x "( If I say no, it would be disrespectful... )"
    x "( But everyone's watching... )"
    x "( This is so humiliating... )"
    
    # Madd's shame intensifies
    show aftb slow burn at right_small
    with dissolve
    show madd boy ashamed at left_small
    with dissolve
    x "( I'm going to eat from his hand. In front of everyone. )"
    x "( People are going to see this. They're going to see me taking food from his hand like I'm his... )"
    x "( Like I belong to him... )"
    
    # Aftb's continued thoughts about ownership progression
    show aftb controlling at right_small
    with dissolve
    aftb_says "( Slowly but surely... )"
    aftb_says "( That's how it works. Small steps. Each one making the next one easier. )"
    aftb_says "( Soon she won't even remember what it felt like to have boundaries. )"
    aftb_says "( She'll just be mine. Completely, thoroughly mine. )"
    
    # More explicit possession fantasies
    show aftb intoxicated pleasure at right_small
    with dissolve
    aftb_says "( Right now it's rice from my hand in the mess hall. )"
    aftb_says "( But soon it will be much more. )"
    aftb_says "( My cock in her mouth. My cum on her tongue. My piss for her to swallow. )"
    aftb_says "( All in private. All marking her as mine. )"
    aftb_says "( And she'll accept it because by then, she'll believe that's her place. )"
    
    # Madd finally leans forward
    show madd boy conflicted at left_small
    with dissolve
    x "( I'm actually doing this... )"
    x "( I'm going to eat from his hand... )"
    
    # SCENE 3: The submission - she eats from his hand in public
    scene scene_interact_aftb_mess_hall_met_event_2_scene_3
    with dissolve
    
    # Aftb's satisfaction
    show aftb triumphant at right_small
    with dissolve
    aftb_says "( Yes... come on... take it... )"
    aftb_says "( Accept my offering... accept my control... )"
    
    # Madd takes a bite of the rice from his hand
    show aftb complete ownership at right_small
    with dissolve
    show madd boy obedient at left_small
    with dissolve
    x "( The rice is in my mouth... from his hand... )"
    x "( I can feel his palm... his skin... in my mouth... )"
    x "( This is so intimate... so possessive... )"
    
    # Madd's deep humiliation
    show aftb satisfied at right_small
    with dissolve
    show madd boy humiliated at left_small
    with dissolve
    x "( Everyone is watching. Everyone is seeing me eat from his hand. )"
    x "( They're probably thinking that I'm his... )"
    x "( That I belong to him... )"
    x "( And the worst part is... some small part of me feels like they're right. )"
    
    # Aftb's internal monologue of triumph
    show aftb apex predator at right_small
    with dissolve
    aftb_says "( Perfect. She did it. She actually did it. )"
    aftb_says "( She took food from my hand in front of witnesses. )"
    aftb_says "( That's a massive psychological victory. )"
    aftb_says "( Now she's marked as mine. At least in her own mind. )"
    
    # Madd pulls back after one bite
    show aftb observant at right_small
    with dissolve
    show madd boy nervous at left_small
    with dissolve
    x "Um... th-thank you... but for now... I'll stick with the spoon..."
    
    # Madd's continued embarrassment
    show aftb calculating at right_small
    with dissolve
    show madd boy hesitant at left_small
    with dissolve
    x "( I can't keep taking food from his hand... not in front of everyone... )"
    
    # But Madd makes a promise without realizing its significance
    x "But I... I'll try again later... when I'm more comfortable with the practice."
    
    show aftb patient at right_small
    with dissolve
    show madd boy nervous at left_small
    with dissolve
    
    # Aftb's internal response to her promise
    show aftb satisfied at right_small
    with dissolve
    aftb_says "( Oh, she said 'later.' She said she'll do it again. )"
    aftb_says "( She's already agreed to let me feed her again. )"
    aftb_says "( She's already accepting this as normal. )"
    aftb_says "( By the time 'later' comes, I'll have her so conditioned that she won't even question it. )"
    aftb_says "( She'll just open her mouth and accept. )"
    
    # More of Aftb's possession fantasies
    show aftb predatory gaze at right_small
    with dissolve
    aftb_says "( 'Later' could mean tomorrow... could mean this week... )"
    aftb_says "( Whenever it is, I'll be ready. )"
    aftb_says "( And each time she eats from my hand, the conditioning will deepen. )"
    aftb_says "( Until feeding is replaced with other acts of submission. )"
    aftb_says "( Until she's completely broken. )"
    
    # Aftb's satisfied response
    show aftb smile at right_small
    with dissolve
    aftb_says "Sure. No problem. You did great for your first time though. Really well."
    
    # The compliment carries deeper implications
    show aftb merciless at right_small
    with dissolve
    show madd boy humiliated at left_small
    with dissolve
    x "(...)"
    x "( Did he just... compliment me for eating from his hand? )"
    x "( Like that was some kind of achievement? )"
    
    # Madd's confused shame
    show aftb slow burn at right_small
    with dissolve
    x "( Why does a simple compliment make me feel so... owned? )"
    
    show aftb complete ownership at right_small
    with dissolve
    show madd boy conflicted at left_small
    with dissolve
    x "( And why do I feel like I want to do it again? )"
    x "( Why does the thought of eating from his hand 'later' make me feel flustered? )"
    
    # Aftb's final internal thoughts
    show aftb apex predator at right_small
    with dissolve
    aftb_says "( She's questioning herself now. )"
    aftb_says "( She's realizing that some part of her liked it. )"
    aftb_says "( That's the most important part of the conditioning. )"
    aftb_says "( When they start enjoying their own submission. )"
    aftb_says "( When they start craving the acts that degrade them. )"
    
    # Aftb speaks casually
    show aftb observant at right_small
    with dissolve
    aftb_says "So, when you're ready, just let me know. I'll teach you the proper way to eat with your hands."
    
    # The double meaning is clear to Aftb but not to Madd
    show aftb calculating at right_small
    with dissolve
    show madd boy nervous at left_small
    with dissolve
    x "O-okay... I will..."
    
    # Madd continues eating with her spoon
    show aftb patient predator at right_small
    with dissolve
    show madd boy uncertain at left_small
    with dissolve
    x "( I go back to using my spoon... but I can't stop thinking about his hand... )"
    x "( About how it felt... about how intimate and shameful it was... )"
    
    # Final observations
    show aftb intoxicated pleasure at right_small
    with dissolve
    x "( Why am I already thinking about doing it again? )"
    
    show aftb marked prey at right_small
    with dissolve
    show madd boy salivating at left_small
    with dissolve
    x "( There's something about the way he controls me... the way he makes me do things I'm embarrassed to do... )"
    x "( It's like he's slowly claiming ownership over my body... over my actions... )"
    x "( And I'm letting him. )"
    
    # Aftb watches her eat with satisfaction
    show aftb triumphant at right_small
    with dissolve
    aftb_says "( Yes. Yes, that's it. )"
    aftb_says "( Already thinking about it. Already anticipating the next time. )"
    aftb_says "( She's more broken than she even realizes. )"
    aftb_says "( Soon, very soon, she'll be completely mine. )"
    aftb_says "( And she'll think it's her idea. )"
    
    # Final Aftb monologue about his goals
    show aftb commanding at right_small
    with dissolve
    aftb_says "( One bite today. More bites tomorrow. And before long... )"
    aftb_says "( She won't need the spoon anymore. )"
    aftb_says "( She'll be completely dependent on me for every meal. )"
    aftb_says "( And by that point, feeding won't be the only thing she's dependent on me for. )"
    aftb_says "( She'll be mine in every way that matters. )"
    
    # Stat changes - higher dominance due to successful public marking
    $ character_relations["aftb"]["lust"] += 3
    $ character_relations["aftb"]["identity"] += 1
    $ character_relations["aftb"]["dominance"] += 5
    $ madd_lust += 2
    $ madd_dominance -= 4
    $ secret_identity -= 0.5
    $ corruption += 0.5
    
    $ game_time.advance_time(minutes=30)
    return


# ============================================
# INTERACT_AFTB_MESS_HALL_MET LEVEL 2 EVENTS
# ============================================

label interact_aftb_mess_hall_met_level_2_event_1:
    """Level 2 event 1 for interact_aftb_mess_hall_met"""
    return

label interact_aftb_mess_hall_met_level_2_event_2:
    """Level 2 event 2 for interact_aftb_mess_hall_met"""
    return


# ============================================
# INTERACT_AFTB_MESS_HALL_MET LEVEL 3 EVENTS
# ============================================

label interact_aftb_mess_hall_met_level_3_event_1:
    """Level 3 event 1 for interact_aftb_mess_hall_met"""
    return

label interact_aftb_mess_hall_met_level_3_event_2:
    """Level 3 event 2 for interact_aftb_mess_hall_met"""
    return

# ============================================
# AFTB ROOM CONVERSATION OPTIONS
# ============================================

label aftb_ask_about_jobs:
    """Ask Aftb about job opportunities"""
    show madd boy curious at left_small
    with dissolve
    x "Hey Aftb, do you know about any jobs nearby? I'm thinking about picking up some extra work."
    show aftb smile at right_small
    with dissolve
    aftb_says "Oh, jobs huh? Yeah, actually I work at a local gym nearby. It's called FitLife Gym."
    show madd boy interested at left_small
    with dissolve
    x "Really? Are they hiring?"
    show aftb smile at right_small
    with dissolve
    aftb_says "Yeah, actually they are hiring. But here's the thing..."
    show aftb calculating at right_small
    with dissolve
    aftb_says "They're specifically looking for female staff to work in the women's locker room and facilities."
    show madd boy blush at left_small
    with dissolve
    x "Oh... so I'm out of luck then since I'm..."
    show aftb smirk at right_small
    with dissolve
    aftb_says "Well, actually... you know, you could probably pass as female staff there if you tried hard enough."
    show madd boy flustered at left_small
    with dissolve
    x "(He's looking at me with that suggestive smirk again...)"
    show aftb bite lips smile at right_small
    with dissolve
    aftb_says "I'm just saying, you've got the looks for it. You could probably get the job if you applied."
    show madd boy blush at left_small
    with dissolve
    x "(My cheeks burn at his implication.)"
    show aftb laugh at right_small
    with dissolve
    aftb_says "Think about it. The pay is decent, and you'd be working in a nice environment. Plus, I could put in a good word for you."
    show madd boy embarrassed at left_small
    with dissolve
    x "I... I'll think about it."
    $ character_relations["aftb"]["lust"] += 2
    $ secret_identity -=1
    $ madd_lust += 2
    
    return

label aftb_ask_about_fun_activities:
    """Ask Aftb about fun activities around the hostel"""
    show madd boy curious at left_small
    with dissolve
    x "So, are there any fun activities around here? I want to make the most of my time."
    show aftb smile at right_small
    with dissolve
    aftb_says "Well, there's the usual stuff - hanging out, playing games, that kind of thing."
    show aftb smile at right_small
    with dissolve
    aftb_says "But actually, me and the boys sometimes gather for movie nights. We put on some films in the common room and just chill out."
    show madd boy interested at left_small
    with dissolve
    x "That sounds nice. What kind of movies do you usually watch?"
    show aftb smirk at right_small
    with dissolve
    aftb_says "All kinds, really. Action films, comedies, sometimes even some romantic stuff. It's pretty casual."
    show aftb smirk at right_small
    with dissolve
    aftb_says "We usually gather around 9 PM when it's dark outside. The atmosphere is nice, everyone's relaxed..."
    show aftb smirk at right_small
    with dissolve
    aftb_says "You should join us sometime. It would be good to have you there."
    show madd boy blush at left_small
    with dissolve
    x "I... that actually sounds fun. I'd like to come."
    show aftb satisfied at right_small
    with dissolve
    aftb_says "Great. Just show up around 9 if you're interested. Fair warning though - we don't hold back with jokes and commentary."
    show madd boy relieved at left_small
    with dissolve
    x "I can handle it."
    $ character_relations["aftb"]["friend"] += 2
    return

label aftb_ask_about_school:
    """Ask Aftb about which school he goes to"""
    show madd boy curious at left_small
    with dissolve
    x "So, which cram school do you go to anyway?"
    show aftb smile at right_small
    with dissolve
    aftb_says "Oh, I go to Riverside Cram Classes. It's pretty competitive, but the teachers are good."
    show madd boy think at left_small
    with dissolve
    x "Hmm, Riverside... that's different from my school. I go to Central Academy."
    show aftb focused at right_small
    with dissolve
    aftb_says "Central Academy, huh? Yeah, I've heard of it. Different curriculum and teaching methods, I'd imagine."
    show madd boy blush at left_small
    with dissolve
    x "Yeah, quite different. We focus more on practical applications."
    show aftb smile at right_small
    with dissolve
    aftb_says "Well, that's actually interesting. Different approaches could complement each other."
    show aftb focused at right_small
    with dissolve
    aftb_says "Hey, you know what? Maybe we should combine our knowledge sometime. Study together, share notes, that kind of thing."
    show madd boy happy at left_small
    with dissolve
    x "That sounds like a good idea. We could help each other out."
    show aftb smile at right_small
    with dissolve
    aftb_says "Yeah, exactly. I could use some fresh perspectives, and you might find some of my study methods useful too."
    show aftb confident at right_small
    with dissolve
    aftb_says "Plus, studying alone can get boring. Having a study partner would be nice."
    show madd boy relieved at left_small
    with dissolve
    x "I agree. Let's do that sometime."
    $ character_relations["aftb"]["friend"] += 3
    return
