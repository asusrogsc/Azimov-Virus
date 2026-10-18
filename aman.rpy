# ============================================
# AMAN CHARACTER INTERACTIONS
# ============================================

label interact_aman_room:
    """Room interaction with Aman (Room 301) - calls level-based events"""
    scene scene_room_aman
    with fade
    
    if "aman" not in met_characters:
        $ met_characters.append("aman")
        $ character_relations["aman"]["friend"] += 10
        show madd boy cool at left_small
        with dissolve
        x "I knock on the door of Room 301."
        show aman wide smirk at right_small
        with dissolve
        show aman lustful smile at right_small
        with dissolve
        aman_says "Yes?"
        show aman lustful smile at right_small
        with dissolve
        show madd boy try to dodge at left_small
        with dissolve
        x "Hi, I'm Madd from Room 305. Just thought I'd introduce myself."
        show madd boy cool at left_small
        with dissolve
        show aman wide smirk at right_small
        with dissolve
        aman_says "Oh, another new resident. I'm Aman. Welcome to the hostel."
        show aman lustful smile at right_small
        with dissolve
        show madd boy blush at left_small
        with dissolve
        x "Thanks. It's... quite different here."
        show madd boy nervous at left_small
        with dissolve
        show aman wide smile at right_small
        with dissolve
        aman_says "(Why is this guy so andogenous-looking?)"
        show aman lustful smirk at right_small
        with dissolve
        show amam disgusted at right_small
        with dissolve
        aman_says "(I hate their kind around here.But maybe he can clean my room, he looks poor enough.)"
        show aman scheming at right_small
        with dissolve
        show aman smile at right_small
        with dissolve
        aman_says "Well if you need a job, I could use some help around my room. Its a boys only area, so its hard to find a maid."
        show aman smirk at right_small
        with dissolve
        show madd boy surprised at left_small
        with dissolve
        x "Uh, sure. I mean, I could help out sometimes."
        show madd boy hesitant at left_small
        with dissolve
        x "(This can't be too bad, right? A little cleaning work for some extra cash...)"
        show madd boy thinking at left_small
        with dissolve
        x "(and i need a job to pay for this place anyway...)"
        show madd boy resigned at left_small
        with dissolve
        show aman smirk at right_small
        with dissolve
        aman_says "Great. Once a day should suffice. Just knock and come in."
        show aman pleased at right_small
        with dissolve
        show aman wide smile at right_small
        with dissolve
        aman_says "But there is a condition. You have to wear a maid outfit while you clean."
        show aman lustful smile at right_small
        with dissolve
        aman_says "I like to see my help looking the part, if you know what I mean."
        show aman predatory at right_small
        with dissolve
        show madd boy cool at left_small
        with dissolve
        x "I... guess that's fine."
        show madd boy uncertain at left_small
        with dissolve
        x "(Well, I did agree to help out. I can handle a silly outfit.)"
        show madd boy resigned at left_small
        with dissolve
        show aman grin at right_small
        with dissolve
        aman_says "Excellent. I'll see you tomorrow then."
        show aman satisfied at right_small
        with dissolve
        show aman smile at right_small
        with dissolve
        aman_says "(I am gonna annoy the hell out of this one. I hate faggots.)"
        show aman evil smile at right_small
        with dissolve
    
    else:
        # Level-based room interaction based on relationship stats
        x "I knock on the door of Room 301 again."
        show madd boy cool at left_small
        with dissolve
        show aman lustful smile at right_small
        with dissolve
        aman_says "Oh, it's you again. Here to clean my room?"
        with dissolve
        menu:
            "Yes, Aman. I'm here to clean.":
                show aman lustful smile at right_small
                with dissolve 
                aman_says "(Points to the cabinet ) There is maid apron at the top of the cabinet pick it up and get started"
                show aman commanding at right_small
                with dissolve
                show madd boy disgusted at left_small
                with dissolve
                x "( I get the maid apron and put it on)"
                show madd boy reluctant at left_small
                with dissolve
                show aman lustful smirk at right_small
                with dissolve
                aman_says "(Whoa , this guy actually looks like a woman in that outfit , maybe he is one of those trap guys )"
                show aman amused at right_small
                with dissolve
                aman_says "Well , get to work then . Dont take too long "
                show aman commanding at right_small
                with dissolve
                show madd boy submissive at left_small 
                with dissolve
                x "Um, Sorry Aman, I just wanted to ask..."
                show madd boy nervous at left_small
                with dissolve
                x " Can i have gloves and a mask too ?"
                show madd boy hesitant at left_small
                with dissolve
                show aman mocking at right_small
                with dissolve
                aman_says "Why ? You afraid of getting dirty ?"
                show aman taunting at right_small
                with dissolve
                aman_says "use your hands like a normal person."
                show aman dismissive at right_small
                with dissolve
                x "O-Okay... "
                x "(I guess I have no choice . I need the money. )"
                x " ( I see him walk towards his gaming chair and start playing a game on his computer )"

                # Call level-based events based on relationship stats
                if character_relations["aman"]["identity"] > 10 and character_relations["aman"]["lust"] > 20:
                    # Level 3 events
                    $ event_type = renpy.random.randint(1, 2)
                    if event_type == 1:
                        call interact_aman_room_level_3_event_1 from _call_interact_aman_room_level_3_event_1
                    else:
                        call interact_aman_room_level_3_event_2 from _call_interact_aman_room_level_3_event_2
                elif character_relations["aman"]["identity"] > 5 and character_relations["aman"]["lust"] > 10:
                    # Level 2 events
                    $ event_type = renpy.random.randint(1, 2)
                    if event_type == 1:
                        call interact_aman_room_level_2_event_1 from _call_interact_aman_room_level_2_event_1
                    else:
                        call interact_aman_room_level_2_event_2 from _call_interact_aman_room_level_2_event_2
                else:
                    # Level 1 events
                    $ event_type = renpy.random.randint(1, 2)
                    if event_type == 1:
                        call interact_aman_room_level_1_event_1 from _call_interact_aman_room_level_1_event_1
                    else:
                        call interact_aman_room_level_1_event_2 from _call_interact_aman_room_level_1_event_2
            "Not right now.":
                call interact_aman_room_decline from _call_interact_aman_room_decline




    $ game_time.advance_time(minutes=5)
    return

label interact_aman_room_decline:
    """Decline to clean Aman's room"""
    show aman annoyed at right_small
    with dissolve
    aman_says "Then why did you knock?"
    show aman annoyed at right_small
    with dissolve
    show madd boy embarassed at left_small
    with dissolve
    x "Sorry, I thought you might need me."
    show madd boy nervous at left_small
    with dissolve
    show aman smirk at right_small
    with dissolve
    aman_says "Need you for what exactly?"
    show aman mocking at right_small
    with dissolve
    show madd boy try to dodge at left_small
    with dissolve
    x "Nothing, never mind."
    show madd boy flustered at left_small
    with dissolve
    show aman smile at right_small
    with dissolve
    aman_says "If i need you, I will call you."
    show aman dismissive at right_small
    with dissolve
    show aman condescending at right_small
    with dissolve
    aman_says "Oh wait, your poor ass probably can't even afford a phone."
    show aman mocking laugh at right_small
    with dissolve
    show madd boy disgusted at left_small
    with dissolve
    x "(This guy..)"
    show madd boy annoyed at left_small
    with dissolve
    show madd boy apologetic at left_small
    with dissolve
    x "I'm sorry. I will clean your room later."
    show madd boy submissive at left_small
    with dissolve
    return

label interact_aman_mess_hall(meal):
    """Mess hall interaction with Aman - First meeting in mess hall"""
    if "aman" not in met_characters:
        $ met_characters.append("aman")
        $ character_relations["aman"]["friend"] += 10
        $ current_location = "floor_1"
    
    show madd boy cool at left_small
    with dissolve
    x "I approach Aman at the mess hall."
    show madd boy cool at left_small
    with dissolve
    show aman lustful smile at right_small
    with dissolve
    aman_says "Ah, a new resident. I'm Aman from Room 301."
    show aman wide smirk at right_small
    with dissolve
    show madd boy try to dodge at left_small
    with dissolve
    x "Hi, I'm [mainname]. Nice to meet you."
    show madd boy cool at left_small
    with dissolve
    show aman lustful looks at right_small
    with dissolve
    aman_says "(Why is this guy so andogenous-looking?)"
    show aman lustful looks at right_small
    with dissolve
    show aman disgusted at right_small
    with dissolve
    aman_says "(I hate their kind around here. But maybe he can clean my room, he looks poor enough.)"
    show aman scheming at right_small
    with dissolve
    show aman smile at right_small
    with dissolve
    aman_says "You know, I must say there's quite a difference in station between people here."
    show aman arrogant smile at right_small
    with dissolve
    show madd boy blush at left_small
    with dissolve
    x "What do you mean by that?"
    show madd boy confused at left_small
    with dissolve
    show aman wide smirk at right_small
    with dissolve
    aman_says "Well, my family's quite wealthy - we're in the import business, quite successfully. Not everyone can say their family maintains that kind of status, you understand?"
    show aman arrogant smile at right_small
    with dissolve
    show madd boy blush at left_small
    with dissolve
    x "(He's talking down to me like I'm beneath him...)"
    show madd boy intimidated at left_small
    with dissolve
    x "I... see what you mean."
    show madd boy nervous at left_small
    with dissolve
    show aman smile at right_small
    with dissolve
    aman_says "I'm sure you do. Be aware of your place in the hierarchy."
    show aman condescending smile at right_small
    with dissolve
    x "(This guy is insufferable... but I need to stay professional.)"
    show madd boy resigned at left_small
    with dissolve
    show aman smirk at right_small
    with dissolve
    aman_says "Actually, I have a proposition for you."
    show aman commanding at right_small
    with dissolve
    show madd boy uncertain at left_small
    with dissolve
    x "A proposition?"
    show madd boy hesitant at left_small
    with dissolve
    aman_says "Well, if you need a job, I could use some help around my room. It's a boys only area, and it's hard to find a maid."
    show aman casual at right_small
    with dissolve
    show madd boy surprised at left_small
    with dissolve
    x "(A job? Here?)"
    show madd boy hopeful at left_small
    with dissolve
    x "Uh, sure. I mean, I could help out sometimes."
    show madd boy hesitant at left_small
    with dissolve
    x "(This could be good money... I need to pay for my room anyway.)"
    show madd boy thinking at left_small
    with dissolve
    show aman smirk at right_small
    with dissolve
    aman_says "Great. Once a day should suffice. Just knock and come in."
    show aman pleased at right_small
    with dissolve
    aman_says "But there is a condition. You have to wear a maid outfit while you clean."
    show aman lustful smile at right_small
    with dissolve
    aman_says "I like to see my help looking the part, if you know what I mean."
    show aman predatory at right_small
    with dissolve
    show madd boy uncertain at left_small
    with dissolve
    x "I... guess that's fine."
    show madd boy uncomfortable at left_small
    with dissolve
    x "(A maid outfit? That's... unusual. But it's just an outfit.)"
    show madd boy resigned at left_small
    with dissolve
    show aman grin at right_small
    with dissolve
    aman_says "Excellent. Come by my room, 301, whenever you're ready."
    show aman satisfied at right_small
    with dissolve
    aman_says "(I am gonna have fun with this one. He looks like he'd make a great maid.)"
    show aman evil smile at right_small
    with dissolve
    show madd boy blush at left_small
    with dissolve
    x "(Why do I feel like I just made a mistake?)"
    show madd boy worried at left_small
    with dissolve
    
    $ game_time.advance_time(minutes=15)
    return

label intercept_aman:
    """Interception scene with Aman - calls level-based events based on relationship stats"""
    # Check if Aman has very high identity and lust (Level 3)
    if character_relations["aman"]["identity"] > 10 and character_relations["aman"]["lust"] > 20:
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call intercept_aman_level_3_event_1 from _call_intercept_aman_level_3_event_1
        else:
            call intercept_aman_level_3_event_2 from _call_intercept_aman_level_3_event_2
    # Check if Aman has high identity and lust (Level 2)
    elif character_relations["aman"]["identity"] > 5 and character_relations["aman"]["lust"] > 10:
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call intercept_aman_level_2_event_1 from _call_intercept_aman_level_2_event_1
        else:
            call intercept_aman_level_2_event_2 from _call_intercept_aman_level_2_event_2
    else:
        # Level 1 events
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call intercept_aman_level_1_event_1 from _call_intercept_aman_level_1_event_1
        else:
            call intercept_aman_level_1_event_2 from _call_intercept_aman_level_1_event_2
    
    return

label water_cooler_talk_aman:
    """Casual conversation with Aman at water cooler - calls level-based events"""
    # Check relationship levels to determine event type
    if character_relations["aman"]["identity"] > 10 and character_relations["aman"]["lust"] > 20:
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call water_cooler_talk_aman_level_3_event_1 from _call_water_cooler_talk_aman_level_3_event_1
        else:
            call water_cooler_talk_aman_level_3_event_2 from _call_water_cooler_talk_aman_level_3_event_2
    elif character_relations["aman"]["identity"] > 5 and character_relations["aman"]["lust"] > 10:
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call water_cooler_talk_aman_level_2_event_1 from _call_water_cooler_talk_aman_level_2_event_1
        else:
            call water_cooler_talk_aman_level_2_event_2 from _call_water_cooler_talk_aman_level_2_event_2
    else:
        # Level 1 events
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call water_cooler_talk_aman_level_1_event_1 from _call_water_cooler_talk_aman_level_1_event_1
        else:
            call water_cooler_talk_aman_level_1_event_2 from _call_water_cooler_talk_aman_level_1_event_2
    
    return

label interact_aman_mess_hall_met(meal):
    """Chat interaction with Aman in mess hall (already met) - calls level-based events"""
    scene scene_messhall_breakfast
    with fade
    
    # Check relationship levels to determine event type
    if character_relations["aman"]["identity"] > 10 and character_relations["aman"]["lust"] > 20:
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call interact_aman_mess_hall_met_level_3_event_1 from _call_interact_aman_mess_hall_met_level_3_event_1
        else:
            call interact_aman_mess_hall_met_level_3_event_2 from _call_interact_aman_mess_hall_met_level_3_event_2
    elif character_relations["aman"]["identity"] > 5 and character_relations["aman"]["lust"] > 10:
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call interact_aman_mess_hall_met_level_2_event_1 from _call_interact_aman_mess_hall_met_level_2_event_1
        else:
            call interact_aman_mess_hall_met_level_2_event_2 from _call_interact_aman_mess_hall_met_level_2_event_2
    else:
        # Level 1 events
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call interact_aman_mess_hall_met_level_1_event_1 from _call_interact_aman_mess_hall_met_level_1_event_1
        else:
            call interact_aman_mess_hall_met_level_1_event_2 from _call_interact_aman_mess_hall_met_level_1_event_2
    
    $ game_time.advance_time(minutes=20)
    return


# ============================================
# INTERACT_AMAN_ROOM LEVEL EVENTS
# ============================================

label interact_aman_room_level_1_event_1:
    """interact_aman_room Level 1 Event 1 - Spitting gum humiliation"""
    scene scene_room_aman
    with fade
    
    show aman sitting at right_small
    with dissolve
    x "I start cleaning Aman's room, dusting the furniture and shelves."
    show madd boy working at left_small
    with dissolve
    x "I carefully rearrange his things back in their proper places."
    show madd boy focused at left_small
    with dissolve
    x "After about fifteen minutes of work, I finish up the room."
    show madd boy satisfied at left_small
    with dissolve
    x "I pick up the garbage bin and head toward the door."
    show madd boy cool at left_small
    with dissolve
    show aman gaming at right_small
    with dissolve
    scene scene_aman_gum_spit_setup 
    with dissolve
    aman_says "Hey, wait a second."
    show aman calling at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "Huh? What is it?"
    show madd boy hesitant at left_small
    with dissolve
    show aman mocking smile at right_small
    with dissolve
    aman_says "Before you leave, take this too."
    show aman commanding at right_small
    with dissolve
    x "Take what? I don't see anything..."
    show madd boy uncertain at left_small
    with dissolve
    show aman predatory at right_small
    with dissolve
    aman_says "Hold out your hand. Now."
    show aman cold at right_small
    with dissolve
    show madd boy obedient at left_small
    with dissolve
    x "I hesitantly hold out my hand."
    show madd boy nervous at left_small
    with dissolve
    show aman smirking at right_small
    with dissolve
    aman_says "(Let's teach this one a lesson about their place.)"
    show aman evil smile at right_small
    with dissolve
    scene scene_aman_gum_spit_hands
    with dissolve

    x "Before I can even process what's happening, he spits his chewing gum directly onto my open hand."
    show madd boy shocked at left_small
    with dissolve
    x "The slimy, wet gum lands on my palm with a disgusting sensation."
    show madd boy disgusted at left_small
    with dissolve
    x "I can still feel the moisture from his saliva coating my skin..."
    show madd boy horrified at left_small
    with dissolve
    aman_says "Well? What are you waiting for? Throw it away."
    show aman dismissive at right_small
    with dissolve
    show madd boy humiliated at left_small
    with dissolve
    x " (My face flushes in embarrassment and disgust.)"
    show madd boy shamed at left_small
    with dissolve
    x "(This is so disgusting... I can't believe he just did that...)"
    show madd boy traumatized at left_small
    with dissolve
    aman_says "What's that look on your face? You got a problem?"
    show aman contemptuous at right_small
    with dissolve
    show madd boy flustered at left_small
    with dissolve
    scene scene_aman_gum_spit_hands_aftermath
    x "N-No, I... of course not..."
    show madd boy submissive at left_small
    with dissolve
    show aman cold smile at right_small
    with dissolve
    aman_says "Know your place. You're nothing but hired help."
    show aman arrogant at right_small
    with dissolve
    show madd boy defeated at left_small
    with dissolve
    aman_says "But here, for your services..."
    show aman taunting at right_small
    with dissolve
    x "(He casually tosses a crumpled thirty dollar bill at me.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(The money falls to the floor.)"
    show madd boy shocked at left_small
    with dissolve
    x "(I stand there for a moment, frozen in disbelief.)"
    show madd boy embarrassed at left_small
    with dissolve
    aman_says "Pick it up. That's what you're here for, isn't it?"
    show aman sneering at right_small
    with dissolve
    show madd boy degraded at left_small
    with dissolve
    x "(I slowly bend down and pick up the crumpled bill off the floor.)"
    show madd boy submissive at left_small
    with dissolve
    x "(The humiliation of having to pick up money he threw at me, mixed with the disgusting feeling of his spit still on my hand...)"
    show madd boy defeated at left_small
    with dissolve
    x "This is unbearable."
    show madd boy traumatized at left_small
    with dissolve
    aman_says "Now get out of my sight."
    show aman dismissive at right_small
    with dissolve
    show aman smirk at right_small
    with dissolve
    x "(I slowly make my way to the door, eager to leave his room. As he goes back to rushing B in counter strike, I can't help but feel a mix of anger and humiliation.)"
    show madd boy embarrassed at left_small
    with dissolve

    
    $ character_relations["aman"]["dominance"] += 3
    $ character_relations["aman"]["identity"] += 2
    $ madd.money += 30
    $ madd_dominance -= 2
    $ madd_secret_identity -= 1
    $ game_time.advance_time(minutes=25)
    return

label interact_aman_room_level_1_event_2:
    """interact_aman_room Level 1 Event 2 - Gaming distraction"""
    scene scene_room_aman
    with fade
    
    show aman gaming at right_small
    with dissolve
    x "(I begin cleaning Aman's room while he sits completely absorbed in his game.)"
    show madd boy working at left_small
    with dissolve
    x "The sound of gunfire and explosions from Counter Strike fills the room."
    show madd boy focused at left_small
    with dissolve
    x "I carefully navigate around his cluttered desk and start dusting."
    show madd boy diligent at left_small
    with dissolve
    aman_says "NOOO! Damn it! Why would you peek mid without window smoke CYKA?!"
    show aman frustrated at right_small
    with dissolve
    show madd boy startled at left_small
    with dissolve
    x "He suddenly jumps up from his gaming chair, clearly frustrated."
    show madd boy observant at left_small
    with dissolve
    aman_says "I died! Those noobs..."
    show aman angry at right_small
    with dissolve
    show madd boy nervous at left_small
    with dissolve
    x "I work my way to cleaning under his bed, bending down to dust and sweep the area."
    show madd boy bent over at left_small
    with dissolve
    show aman looking at right_small
    with dissolve
    aman_says "(Wait... what...)"
    show aman staring at right_small
    with dissolve
    scene scene_aman_madd_clean_underbed_stare
    with dissolve
    x "I'm focused on cleaning and don't notice him staring at me."
    show madd boy unaware at left_small
    with dissolve
    aman_says "(His ass is... actually pretty nice...)"
    show aman aroused at right_small
    with dissolve
    show aman conflicted at right_small
    with dissolve
    aman_says "(No, no, no... What am I thinking? This is a man... I hate faggots...)"
    show aman disgusted at right_small
    with dissolve
    x "(I continue cleaning, unaware of the internal conflict happening behind me.)"
    show madd boy working at left_small
    with dissolve
    show aman confused at right_small
    with dissolve
    aman_says "(I need to stop this. I'm not like that... I'm normal...)"
    show aman defensive at right_small
    with dissolve
    scene scene_aman_madd_clean_underbed_stare_2
    with dissolve
    aman_says "Hurry up with the cleaning."
    show aman dismissive at right_small
    with dissolve
    show madd boy obedient at left_small
    with dissolve
    x "(He quickly turns back to his gaming setup and sits down heavily ready for next round I suppose.)"
    show aman gaming intensely at right_small
    with dissolve
    aman_says "Get back to work. And stay out of my way."
    show aman cold at right_small
    with dissolve
    show madd boy compliant at left_small
    with dissolve
    x "I finish cleaning under the bed and continue with the rest of the room."
    show madd boy dutiful at left_small
    with dissolve
    
    $ character_relations["aman"]["lust"] += 1
    $ character_relations["aman"]["identity"] += 1
    $ madd.money += 30
    $ game_time.advance_time(minutes=15)
    return

label interact_aman_room_level_2_event_1:
    """interact_aman_room Level 2 Event 1 - Sock sorting humiliation"""
    scene scene_room_aman
    with fade
    
    show aman gaming at right_small
    with dissolve
    x "(I'm cleaning Aman's room when I hear him cursing at the screen.)"
    show madd boy working at left_small
    with dissolve
    aman_says "DAMN IT! Dust 2 again!"
    show aman frustrated at right_small
    with dissolve
    x "(He jumps up from his gaming chair in anger.)"
    show aman angry at right_small
    with dissolve
    show madd boy startled at left_small
    with dissolve
    aman_says "I need to cool off for a minute."
    show aman annoyed at right_small
    with dissolve
    scene scene_aman_fetch_socks
    with dissolve
    x "(He walks over to his cabinet and pulls out a large bag of worn socks.)"
    show aman commanding at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "What are those for? "
    show madd boy uncertain at left_small
    with dissolve
    aman_says "These socks need sorting. I wear a lot of socks, and I don't have time to check which ones are fresh."
    show aman dismissive at right_small
    with dissolve
    show madd boy attentive at left_small
    with dissolve
    aman_says "That's what I pay you for. I want you to smell each one and tell me—is it clean enough for my feet?"
    show aman casual at right_small
    with dissolve
    x "(He speaks about this like it's a perfectly normal task.)"
    show madd boy shocked at left_small
    with dissolve
    x "Wait... you want me to... smell your socks?"
    show madd boy horrified at left_small
    with dissolve
    aman_says "That's exactly what I want. I'm rich enough to only wear new socks. If they smell bad, they go in the trash."
    show aman arrogant at right_small
    with dissolve
    show madd boy disgusted at left_small
    with dissolve
    x "(He doesn't even wait for me to respond, just dumps the pile in front of me.)"
    show madd boy overwhelmed at left_small
    with dissolve
    aman_says "Get started. I want this done before you leave."
    show aman demanding at right_small
    with dissolve
    show madd boy resigned at left_small
    with dissolve
    x "(I look at the pile of socks with dread.)"
    show madd boy anxious at left_small
    with dissolve
    x "(This is degrading... but I need this job. I need the money.)"
    show madd boy ashamed at left_small
    with dissolve
    x "(I pick up the first sock with two fingers, holding it at arm's length.)"
    show madd boy reluctant at left_small
    with dissolve
    scene scene_aman_room_madd_sock_smelling
    with dissolve
    x "(I bring it to my nose and take a whiff.)"
    show madd boy trembling at left_small
    with dissolve
    x "(Oh god... this one reeks. It smells like sweat and feet... absolutely foul.)"
    show madd boy gagging at left_small
    with dissolve
    x "(I toss it into the trash bin without hesitation.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(I pick up the second sock.)"
    show madd boy determined at left_small
    with dissolve
    x "(This one is even worse. The smell is so pungent it makes my eyes water.)"
    show madd boy revolted at left_small
    with dissolve
    x "(Into the trash it goes.)"
    show madd boy mechanical at left_small
    with dissolve
    x "(And another... and another...)"
    show madd boy numb at left_small
    with dissolve
    x "(I work through the pile methodically, my mind trying to disconnect from what I'm doing.)"
    show madd boy dissociating at left_small
    with dissolve
    x "(Sock after sock, the stench assaults my senses.)"
    x "(Most of them smell horrible. Acrid, musty, rotten... the stench coating the inside of my nostrils.)"
    show madd boy despondent at left_small
    with dissolve
    x "(I throw away pair after pair, my disgust growing with each one.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(My face flushes hot with shame. This is so degrading.)"
    show madd boy shamed at left_small
    with dissolve
    x "(I find only one pair that doesn't smell completely offensive.)"
    show madd boy relieved at left_small
    with dissolve
    x "(I place that single pair aside carefully.)"
    show madd boy submissive at left_small
    with dissolve
    show aman watching at right_small
    with dissolve
    aman_says "Done already?"
    show aman smirking at right_small
    with dissolve
    show madd boy nervous at left_small
    with dissolve
    x "(I nod, not trusting my voice.)"
    show madd boy silent at left_small
    with dissolve
    show aman mocking at right_small
    with dissolve
    aman_says "So how did they smell? Be specific."
    show aman cruel at right_small
    with dissolve
    show madd boy flustered at left_small
    with dissolve
    x "I... they were... most of them were quite foul."
    show madd boy embarrassed at left_small
    with dissolve
    x "The smell was unbearable... sweat and..."
    show madd boy voice wavering at left_small
    with dissolve
    aman_says "Exactly. That's why I paid for you to do this instead of doing it myself."
    show aman condescending at right_small
    with dissolve
    show madd boy degraded at left_small
    with dissolve
    aman_says "Only one pair was acceptable? Pathetic."
    show aman dismissive at right_small
    with dissolve
    x "He notices my disgust written all over my face."
    show madd boy cant hide it at left_small
    with dissolve
    show aman contemptuous at right_small
    with dissolve
    aman_says "If you're gonna be disgusted, be disgusted by your family. At least my socks are worth something."
    show aman cruel smile at right_small
    with dissolve
    aman_says "You weren't born rich like me. That's the real source of your shame."
    show aman arrogant at right_small
    with dissolve
    show madd boy broken at left_small
    with dissolve
    x "(His words cut deeper than any physical blow could.)"
    show madd boy defeated at left_small
    with dissolve
    x "(He's right. I'm not from a wealthy family. I'm poor, desperate, and willing to degrade myself for money.)"
    show madd boy self loathing at left_small
    with dissolve
    aman_says "Now clean up this trash and get out of my sight."
    show aman dismissive at right_small
    with dissolve
    show madd boy compliant at left_small
    with dissolve
    x "(I obey without a word.)"
    show madd boy robotic at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 4
    $ character_relations["aman"]["lust"] += 2
    $ character_relations["aman"]["identity"] += 2
    $ madd_dominance -= 3
    $ madd_secret_identity -= 2
    $ madd.money += 30
    $ game_time.advance_time(minutes=20)
    return

label interact_aman_room_level_2_event_2:
    """interact_aman_room Level 2 Event 2 - Physical groping"""
    scene scene_room_aman
    with fade
    
    show aman gaming at right_small
    with dissolve
    x "(I'm cleaning Aman's room while he sits absorbed in his gaming chair.)"
    show madd boy working at left_small
    with dissolve
    aman_says "Tch... stupid teammates..."
    show aman frustrated at right_small
    with dissolve
    x "(The sound of explosions and gunfire echoes through the room.)"
    show madd boy focused at left_small
    with dissolve
    x "(I continue my work, dusting shelves and organizing.)"
    show madd boy diligent at left_small
    with dissolve
    aman_says "NOOO!"
    show aman angry at right_small
    with dissolve
    show madd boy startled at left_small
    with dissolve
    x "(He jumps up from his seat suddenly.)"
    show aman frustrated at right_small
    with dissolve
    x "I died. Damn it all."
    show madd boy nervous at left_small
    with dissolve
    scene scene_aman_madd_clean_underbed_stare
    with dissolve
    x "(I work my way to the area under his bed, bending down low to clean properly.)"
    show madd boy bent over at left_small
    with dissolve
    show aman staring at right_small
    with dissolve
    aman_says "(Wait... that's...)"
    show aman aroused at right_small
    with dissolve
    x "(I'm focused on cleaning and don't realize he's watching me.)"
    show madd boy unaware at left_small
    with dissolve
    aman_says "(Their body is actually... really nice. That ass is...)"
    show aman tempted at right_small
    with dissolve
    x "(I continue dusting under the bed, completely oblivious.)"
    show madd boy working at left_small
    with dissolve
    show aman approaching at right_small
    with dissolve
    scene scene_aman_room_grope_underbed
    with dissolve
    x "(Suddenly, I feel a hand on my lower back.)"
    show madd boy startled at left_small
    with dissolve
    show aman touching at right_small
    with dissolve
    aman_says "You need to go deeper. The corner over there is still dirty."
    show aman commanding at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "(His hand slides down from my back to my ass."
    show madd boy shocked at left_small
    with dissolve
    x "(Is he... touching me?)"
    show madd boy uncertain at left_small
    with dissolve
    show aman groping at right_small
    with dissolve
    aman_says "Clean it properly. Don't leave any spots."
    show aman possessive at right_small
    with dissolve
    show madd boy tense at left_small
    with dissolve
    x "(His hand squeezes my ass, and I feel my face burning."
    show madd boy embarrassed at left_small
    with dissolve
    x "(His touch is intrusive, invasive... making my skin crawl.)"
    show madd boy uncomfortable at left_small
    with dissolve
    show aman feeling at right_small
    with dissolve
    aman_says "(God... their body really is great... soft and...)"
    show aman conflicted at right_small
    with dissolve
    x "(Im frozen, unable to move or speak."
    show madd boy paralyzed at left_small
    with dissolve
    scene scene_aman_room_grope_underbed
    with dissolve
    x "(He continues touching me, his hand lingering far longer than necessary.)"
    show madd boy violating sensation at left_small
    with dissolve
    show aman struggling at right_small
    with dissolve
    scene scene_aman_madd_clean_underbed_stare_2
    with dissolve
    aman_says "(No... stop thinking like this... they're a man... I hate faggots... I'm not like this...)"
    show aman disgusted at right_small
    with dissolve
    show aman conflicted at right_small
    with dissolve
    show madd boy still frozen at left_small
    with dissolve
    aman_says "Get to work."
    show aman abrupt at right_small
    with dissolve
    x "(His hand suddenly disappears as if nothing happened.)"
    show madd boy relieved but traumatized at left_small
    with dissolve
    show aman returning at right_small
    with dissolve
    x "(He walks back to his gaming chair abruptly.)"
    show aman cold at right_small
    with dissolve
    aman_says "And don't get in my way again."
    show aman dismissive at right_small
    with dissolve
    show madd boy compliant at left_small
    with dissolve
    x "(I slowly continue cleaning under the bed, my heart still racing.)"
    show madd boy shaken at left_small
    with dissolve
    x "(What just happened? Did he really just...)"
    show madd boy processing at left_small
    with dissolve
    x "(I try to ignore the feeling of his touch still on my skin. As I finish cleaning, I can't help but feel violated and humiliated. But he throws 40 dollars my way for the job.)"
    show madd boy disturbed at left_small
    with dissolve
    
    $ character_relations["aman"]["lust"] += 3
    $ character_relations["aman"]["identity"] += 2
    $ madd_dominance -= 2
    $ madd_secret_identity -= 1
    $ madd.money += 40
    $ game_time.advance_time(minutes=15)
    return

label interact_aman_room_level_3_event_1:
    """interact_aman_room Level 3 Event 1 - Gum spitting on face"""
    scene scene_room_aman
    with fade
    
    show aman gaming at right_small
    with dissolve
    x "(I've finished cleaning Aman's room thoroughly, dusting every surface and rearranging his belongings.)"
    show madd boy working at left_small
    with dissolve
    x "(I pick up the garbage bin, ready to leave after completing my work.)"
    show madd boy satisfied at left_small
    with dissolve
    show aman gaming at right_small
    with dissolve
    aman_says "Hey, wait."
    show aman calling at right_small
    with dissolve
    show madd boy turning at left_small
    with dissolve
    x "(I turn back toward him, wondering what he wants.)"
    show madd boy uncertain at left_small
    with dissolve
    aman_says "Take this too."
    show aman smirking at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "(What could he possibly—)"
    show madd boy questioning at left_small
    with dissolve
    scene scene_aman_gum_spit_setup
    with dissolve
    x "(Before I can even ask what he means, I feel something wet and disgusting hit my face.)"
    show madd boy shocked at left_small
    with dissolve
    scene scene_aman_gum_spit_face
    with dissolve
    x "(His chewing gum, covered in his saliva, splatters directly onto my forehead.)"
    show madd boy horrified at left_small
    with dissolve
    x "(No... he didn't...)"
    show madd boy disbelieving at left_small
    with dissolve
    x "(The spit surrounding the gum is thick and wet, trickling slowly down my cheek.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(I can feel it... oh god, this is so revolting...)"
    show madd boy gagging at left_small
    with dissolve
    show aman laughing at right_small
    with dissolve
    scene scene_aman_gum_spit_face_aftermath
    with dissolve
    aman_says "Ha! Ha! Ha!"
    show aman cruel laughter at right_small
    with dissolve
    show madd boy traumatized at left_small
    with dissolve
    aman_says "I might not be hitting headshots in Counter Strike, but surely in real life."
    show aman mocking at right_small
    with dissolve
    show madd boy broken at left_small
    with dissolve
    x "(That joke... that horrible, disgusting joke...)"
    show madd boy anguished at left_small
    with dissolve
    x "(I can't even respond. I'm too humiliated, too violated.)"
    show madd boy numb at left_small
    with dissolve
    aman_says "Get out of my sight."
    show aman dismissive at right_small
    with dissolve
    show madd boy silent at left_small
    with dissolve
    x "(I say nothing. There's nothing to say.)"
    show madd boy defeated at left_small
    with dissolve
    x "(I wipe my face with the back of my hand, trying to clean away the spit.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(I leave the room without a word, my entire body trembling with shame and disgust.)"
    show madd boy devastated at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 5
    $ character_relations["aman"]["lust"] += 3
    $ character_relations["aman"]["identity"] += 1
    $ madd_dominance -= 4
    $ madd_secret_identity -= 3
    $ madd.money += 50
    $ game_time.advance_time(minutes=15)
    return

label interact_aman_room_level_3_event_2:
    """interact_aman_room Level 3 Event 2 - Underwear smell threat"""
    scene scene_room_aman
    with fade
    
    show aman gaming at right_small
    with dissolve
    x "I'm cleaning Aman's room while he sits glued to his gaming chair."
    show madd boy working at left_small
    with dissolve
    aman_says "DAMN IT! Inferno again!"
    show aman frustrated at right_small
    with dissolve
    show madd boy startled at left_small
    with dissolve
    x "He suddenly jumps up from his seat in frustration."
    show aman angry at right_small
    with dissolve
    show madd boy nervous at left_small
    with dissolve
    aman_says "I need a break from this shit."
    show aman annoyed at right_small
    with dissolve
    x "He walks over to his cabinet and pulls out a handful of underwear."
    show aman commanding at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "(What is he doing now?)"
    scene aman_room_underwear_fetching
    show madd boy alarmed at left_small
    with dissolve
    aman_says "These need sorting too. Just like the socks."
    show aman arrogant at right_small
    with dissolve
    show madd boy horrified at left_small
    with dissolve
    aman_says "I don't have time to check which ones are fresh. That's what I pay you for."
    show aman dismissive at right_small
    with dissolve
    show madd boy appalled at left_small
    with dissolve
    aman_says "Tell me—is this one clean enough for me to wear?"
    show aman casual at right_small
    with dissolve
    x "(He wants me to smell his dirty underwear...)"
    show madd boy revolted at left_small
    with dissolve
    x "(This is beyond degrading. This is absolutely vile.)"
    show madd boy ashamed at left_small
    with dissolve
    aman_says "I'm rich enough to only wear new underwear. If they smell bad, they go in the trash."
    show aman arrogant at right_small
    with dissolve
    show madd boy resigned at left_small
    with dissolve
    x "He dumps the pile on the floor in front of me."
    show madd boy overwhelmed at left_small
    with dissolve
    aman_says "Get started."
    show aman demanding at right_small
    with dissolve
    show madd boy obedient at left_small
    with dissolve
    x "I pick up the first pair of underwear with two fingers, my stomach churning."
    show madd boy trembling at left_small
    with dissolve
    scene aman_room_underwear_smelling
    with dissolve
    x "I bring it to my nose and sniff."
    show madd boy gagging at left_small
    with dissolve
    x "(Oh god... this one is foul. Pure sweat and... something else. Something sweet.)"
    show madd boy confused at left_small
    with dissolve
    x "(I don't know what that smell is, but it's vile.)"
    show madd boy nauseated at left_small
    with dissolve
    x "Into the trash it goes."
    show madd boy mechanical at left_small
    with dissolve
    x "I continue with the next pair."
    show madd boy determined at left_small
    with dissolve
    x "(This one... also bad. That same sweet tint mixed with sweat...)"
    show madd boy disgusted at left_small
    with dissolve
    x "(And this one... god, this one is even worse...)"
    show madd boy despondent at left_small
    with dissolve
    x "I work through the pile, throwing away five pairs that reek."
    show madd boy dissociating at left_small
    with dissolve
    x "Out of seven, only two are somewhat acceptable."
    show madd boy exhausted at left_small
    with dissolve
    x "(I can't believe I just did that. I smell these things from his body...)"
    show madd boy humiliated at left_small
    with dissolve
    show aman watching at right_small
    with dissolve
    aman_says "Done?"
    show aman casual at right_small
    with dissolve
    show madd boy nervous at left_small
    with dissolve
    x "I nod, unable to speak."
    show madd boy silent at left_small
    with dissolve
    show aman smirking at right_small
    with dissolve
    aman_says "How did they smell?"
    show aman curious at right_small
    with dissolve
    show madd boy flustered at left_small
    with dissolve
    x "Foul... but a little sweet."
    show madd boy embarrassed at left_small
    with dissolve
    show aman suddenly angry at right_small
    with dissolve
    aman_says "What did you say?"
    show aman furious at right_small
    with dissolve
    show madd boy frightened at left_small
    with dissolve
    x "(Oh no... did I say something wrong?)"
    show madd boy panicked at left_small
    with dissolve
    x "Suddenly, his hand grabs the back of my neck forcefully."
    show madd boy shocked at left_small
    with dissolve
    show aman aggressive at right_small
    with dissolve
    aman_says "That's the smell of sweat from hard work to get you rich, you ungrateful bitch."
    show aman menacing at right_small
    with dissolve
    show madd boy terrified at left_small
    with dissolve
    x "(His grip is tight... he's really angry...)"
    show madd boy fearful at left_small
    with dissolve
    aman_says "I remember you asking me for a mask earlier. A MASK."
    show aman contemptuous at right_small
    with dissolve
    aman_says "Now if you don't wanna start wearing my underwear as a mask, get the fuck out of here before I make you."
    show aman threatening at right_small
    with dissolve
    show madd boy devastated at left_small
    with dissolve
    x "(He's... he's threatening to...)"
    show madd boy horrified at left_small
    with dissolve
    x "(I need to leave. Now.)"
    show madd boy desperate at left_small
    with dissolve
    x "His hand releases me, and I scramble to my feet."
    show madd boy scrambling at left_small
    with dissolve
    show aman dismissive at right_small
    with dissolve
    aman_says "Get out."
    show aman cold at right_small
    with dissolve
    show madd boy fleeing at left_small
    with dissolve
    x "I rush out of the room, my heart pounding in my chest."
    show madd boy panicked at left_small
    with dissolve
    x "(That threat... oh my god... he was serious...)"
    show madd boy shaken at left_small
    with dissolve
    x "(What would he have done if I didn't leave?)"
    show madd boy traumatized at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 5
    $ character_relations["aman"]["lust"] += 4
    $ character_relations["aman"]["identity"] += 1
    $ madd_dominance -= 4
    $ madd_secret_identity -= 3
    $ madd.money += 50
    $ game_time.advance_time(minutes=20)
    return


# ============================================
# INTERCEPT_AMAN LEVEL EVENTS
# ============================================

#images done 
label intercept_aman_level_1_event_1:
    """intercept_aman Level 1 Event 1 - The Scent Approval"""
    scene scene_hostel_hallway
    with fade
    
    show madd boy walking at left_small
    with dissolve
    x "(I'm walking down the hallway, minding my own business.)"
    show madd boy unaware at left_small
    with dissolve
    show aman dressed at right_small
    with dissolve
    x "(Aman stops me suddenly.)"
    scene scene_aman_intercepts_madd_basic_block
    with dissolve
    show madd boy startled at left_small
    with dissolve
    x "(He's dressed unusually well—nicer clothes than I've ever seen him wear.)"
    show madd boy observant at left_small
    with dissolve
    x "(His appearance is polished, expensive-looking, completely different from his usual casual wear.)"
    show madd boy confused at left_small
    with dissolve
    aman_says "Hey, stop."
    show aman commanding at right_small
    with dissolve
    show madd boy nervous at left_small
    with dissolve
    x "(His tone is direct, but not harsh. It's just a command.)"
    show madd boy uncertain at left_small
    with dissolve
    aman_says "I'm meeting a high-tier girl tonight."
    show aman confident at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "(High-tier? What does that mean? Is she important?)"
    show madd boy uncertain at left_small
    with dissolve
    aman_says "I need a second opinion."
    show aman casual at right_small
    with dissolve
    show madd boy surprised at left_small
    with dissolve
    x "(He's asking... asking me... for my opinion?)"
    show madd boy hopeful at left_small
    with dissolve
    x "(For a moment, I feel something shift. Maybe this is a real conversation.)"
    show madd boy attentive at left_small
    with dissolve
    show aman holding at right_small
    with dissolve
    show scene_aman_intercepts_madd_perfume_smell
    with dissolve

    x "(He holds his wrist up to my nose.)"
    show madd boy leaning at left_small
    with dissolve
    x "(I lean in, my nose nearly touching his wrist.)"
    show madd boy surprised at left_small
    with dissolve
    x "(The scent that hits me is... actually nice.)"
    show madd boy pleased at left_small
    with dissolve
    x "(It's expensive-smelling, high-end, sophisticated.)"
    show madd boy appreciative at left_small
    with dissolve
    x "(Not what I expected from someone like him.)"
    show madd boy confused at left_small
    with dissolve
    x "(For a moment, it feels like a normal interaction—just someone asking a friend for an opinion.)"
    show madd boy hopeful at left_small
    with dissolve
    aman_says "(She'll love this. High-end cologne always makes a good first impression. This girl is worth the investment.)"
    show aman confident at right_small
    with dissolve
    show madd boy waiting at left_small
    with dissolve
    x "(He's waiting for me to respond.)"
    show madd boy speaking at left_small
    with dissolve
    x "It... it smells really good."
    show madd boy pleased at left_small
    with dissolve
    x "(My voice is cautious, but genuine.)"
    show madd boy hopeful at left_small
    with dissolve
    x "(Maybe he'll thank me. Maybe this will be a moment of actual human connection.)"
    show aman smirking at right_small
    with dissolve
    aman_says "Of course it does."
    show aman arrogant at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "(His tone shifts instantly.)"
    show madd boy deflating at left_small
    with dissolve
    aman_says "It costs more than your monthly salary."
    show aman cruel at right_small
    with dissolve
    show madd boy devastated at left_small
    with dissolve
    x "(There it is.)"
    show madd boy broken at left_small
    with dissolve
    x "(The moment of connection, shattered.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(He wasn't asking for my opinion as a person. He was reminding me of my place.)"
    show madd boy ashamed at left_small
    with dissolve
    x "(Everything about me—my salary, my worth, my existence—is beneath him.)"
    show madd boy defeated at left_small
    with dissolve
    x "(And he needed me to know it, even in this moment of asking for 'help.)')"
    show madd boy numb at left_small
    with dissolve
    show aman walking at right_small
    with dissolve
    aman_says "(Let her see how much I'm worth. Let her understand the kind of man I am.)"
    show aman dismissive at right_small
    with dissolve
    x "(He walks away without another word.)"
    show madd boy standing at left_small
    with dissolve
    x "(I'm left standing in the hallway, momentarily confused by the interaction.)"
    show madd boy uncertain at left_small
    with dissolve
    x "(There was no insult, no physical humiliation... but the emotional sting is deeper.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(The cruelty of treating me almost like a person, then reminding me that I'm not.)"
    show madd boy broken at left_small
    with dissolve
    x "(His cologne lingers in my nostrils—a constant reminder of the gap between us.)"
    show madd boy defeated at left_small
    with dissolve
    $ character_relations["aman"]["dominance"] += 2
    $ madd_dominance -= 1
    $ game_time.advance_time(minutes=2)
    return
#image done 
label intercept_aman_level_1_event_2:
    """intercept_aman Level 1 Event 2 - The T-Shirt Buff"""
    scene scene_hostel_hallway
    with fade
    
    show madd boy walking at left_small
    with dissolve
    x "(I'm walking down the hallway when Aman suddenly steps in front of me.)"
    show madd boy startled at left_small
    with dissolve
    show aman stopping at right_small
    with dissolve
    aman_says "Stop."
    show aman commanding at right_small
    with dissolve
    show madd boy nervous at left_small
    with dissolve
    x "(I stop immediately, waiting to see what he wants.)"
    show madd boy attentive at left_small
    with dissolve
    show aman pointing at right_small
    with dissolve
    x "(He points down at his foot.)"
    show madd boy looking at left_small
    with dissolve
    x "(I follow his gaze to his expensive black leather shoes.)"
    show madd boy observant at left_small
    with dissolve
    x "(There's a small dull spot on the leather—barely noticeable.)"
    show madd boy confused at left_small
    with dissolve
    aman_says "Shine this. Right here."
    show aman demanding at right_small
    with dissolve
    show madd boy shocked at left_small
    with dissolve
    x "(He wants me to... shine his shoe?)"
    show madd boy uncertain at left_small
    with dissolve
    x "I... I don't have a cloth, Sir."
    show madd boy hesitant at left_small
    with dissolve
    show aman scoffing at right_small
    with dissolve
    aman_says "You're wearing one, aren't you?"
    show aman cold at right_small
    with dissolve
    show madd boy horrified at left_small
    with dissolve
    x "(My uniform... he wants me to use my uniform...)"
    show madd boy shocked at left_small
    with dissolve
    x "(The baggy T-shirt they make us wear.)"
    show madd boy panicked at left_small
    with dissolve
    aman_says "Your shirt. Use that."
    show aman commanding at right_small
    with dissolve
    show madd boy devastated at left_small
    with dissolve
    x "(My uniform... the only piece of clothing I have that's clean, that's presentable...)"
    show madd boy humiliated at left_small
    with dissolve
    aman_says "(This servant needs to understand their purpose. I'll show them what they're good for.)"
    show aman cruel at right_small
    with dissolve
    show madd boy trembling at left_small
    with dissolve
    x "(Slowly, I reach down and pull out the baggy tail of my oversized T-shirt.)"
    show madd boy ashamed at left_small
    with dissolve
    x "(The fabric is wrinkled from being tucked into my jeans.)"
    show madd boy embarrassed at left_small
    with dissolve
    x "(I look around nervously, hoping no one else is watching this.)"
    show madd boy panicked at left_small
    with dissolve
    x "(This is so humiliating.)"
    show madd boy defeated at left_small
    with dissolve
    show madd boy kneeling at left_small
    with dissolve
    scene scene_aman_intercept_madd_shoe_clean
    with dissolve
    x "(I kneel down on the hard floor in front of him.)"
    show madd boy submissive at left_small
    with dissolve
    x "(The cold tile presses against my knees.)"
    show madd boy uncomfortable at left_small
    with dissolve
    x "(I'm positioned directly at his feet, looking up at him from below.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(The power dynamic is unmistakable.)"
    show madd boy broken at left_small
    with dissolve
    show aman watching at right_small
    with dissolve
    x "(He watches me, his expression one of cold satisfaction.)"
    show madd boy frightened at left_small
    with dissolve
    x "(I bring my shirt to his shoe and begin to rub.)"
    show madd boy scrubbing at left_small
    with dissolve
    x "(The fabric catches slightly on the leather as I work.)"
    show madd boy concentrating at left_small
    with dissolve
    x "(I try to be gentle, but thorough.)"
    show madd boy resigned at left_small
    with dissolve
    x "(My uniform is getting dirty now—marked with whatever was on his shoe.)"
    show madd boy ashamed at left_small
    with dissolve
    show aman tapping at right_small
    with dissolve
    aman_says "(Good. They understand their place. Look at how obedient they are when properly motivated.)"
    show aman satisfied at right_small
    with dissolve
    x "(He taps his other foot impatiently against the floor, the sound echoing in my ears.)"
    show madd boy wincing at left_small
    with dissolve
    x "(The tapping is a constant reminder that I'm moving too slowly, not doing enough.)"
    show madd boy anxious at left_small
    with dissolve
    x "(I scrub harder, faster, desperate to satisfy him.)"
    show madd boy desperate at left_small
    with dissolve
    x "(My knees are aching from pressing against the hard floor.)"
    show madd boy aching at left_small
    with dissolve
    x "(The fabric of my shirt is getting dirtier by the second.)"
    show madd boy devastated at left_small
    with dissolve
    x "(This is my work uniform. I'm supposed to look presentable in this.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(And now it's stained with filth from his shoe.)"
    show madd boy broken at left_small
    with dissolve
    show aman nodding at right_small
    with dissolve
    aman_says "There. Now you're finally useful."
    show aman dismissive at right_small
    with dissolve
    show madd boy devastated at left_small
    with dissolve
    x "(Finally useful...)"
    show madd boy traumatized at left_small
    with dissolve
    x "(Is that all I am? Useful only when I'm cleaning his shoes with my own clothing?)"
    show madd boy ashamed at left_small
    with dissolve
    aman_says "Don't worry about the stain. It adds 'character' to a servant's look."
    show aman cruel smile at right_small
    with dissolve
    show madd boy shattered at left_small
    with dissolve
    x "(A servant's look.)"
    show madd boy broken at left_small
    with dissolve
    x "(That's what he thinks I am. A servant.)"
    show madd boy defeated at left_small
    with dissolve
    show aman walking at right_small
    with dissolve
    x "(He walks away without waiting for a response, without even acknowledging my effort.)"
    show madd boy kneeling at left_small
    with dissolve
    x "(I remain kneeling on the floor, looking down at my shirt.)"
    show madd boy devastated at left_small
    with dissolve
    x "(The stain is visible now—a dark mark on my uniform.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(Everyone who sees me will know what happened. Everyone will know I was on my knees.)"
    show madd boy ashamed at left_small
    with dissolve
    x "(Character... he said the stain adds character.)"
    show madd boy broken at left_small
    with dissolve
    x "(What kind of character does degradation add?)"
    show madd boy hollow at left_small
    with dissolve
    x "(I stand up slowly, my knees sore from the floor.)"
    show madd boy defeated at left_small
    with dissolve
    x "(This shirt will need to be washed. Or replaced. I can't afford to replace it.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(So I'll wear it with this stain, and everyone will see.)"
    show madd boy broken at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 2
    $ character_relations["aman"]["identity"] += 1
    $ madd_dominance -= 2
    $ madd_secret_identity -= 1
    $ game_time.advance_time(minutes=5)
    return
#images done
label intercept_aman_level_2_event_1:
    """intercept_aman Level 2 Event 1 - The Spittle Polish"""
    scene scene_hostel_hallway
    with fade
    
    show madd boy walking at left_small
    with dissolve
    x "(I'm walking down the hallway, trying to be invisible.)"
    show madd boy cautious at left_small
    with dissolve
    x "(But he appears again, blocking my path like before.)"
    show aman blocking at right_small
    with dissolve
    aman_says "You again."
    show aman commanding at right_small
    with dissolve
    show madd boy nervous at left_small
    with dissolve
    x "(My stomach drops.)"
    show madd boy frightened at left_small
    with dissolve
    x "(Not again. Please, not again.)"
    show madd boy resigned at left_small
    with dissolve
    aman_says "My shoes are dirty."
    show aman impatient at right_small
    with dissolve
    show madd boy submissive at left_small
    with dissolve
    x "(His voice is harsher this time.)"
    show madd boy afraid at left_small
    with dissolve
    x "(There's no pretense of politeness like last time.)"
    show madd boy trembling at left_small
    with dissolve
    x "(This is a demand, not a request.)"
    show madd boy broken at left_small
    with dissolve
    x "I... I don't have anything to clean them with, Sir."
    show madd boy hesitant at left_small
    with dissolve
    show aman cruel at right_small
    with dissolve
    x "(I can hear the pleading in my own voice.)"
    show madd boy ashamed at left_small
    with dissolve
    x "(I'm already begging before he's even done asking.)"
    show madd boy humiliated at left_small
    with dissolve
    show aman smirking at right_small
    with dissolve
    aman_says "(She already knows what's coming. Look at her—already terrified.)"
    show aman satisfied at right_small
    with dissolve
    show madd boy waiting at left_small
    with dissolve
    x "(He's looking directly at me now.)"
    show madd boy frightened at left_small
    with dissolve
    x "(His eyes are cold, amused by my fear.)"
    show madd boy panicked at left_small
    with dissolve
    show aman gathering at right_small
    with dissolve
    scene scene_aman_intercept_madd_shoe_spit_gathering
    with dissolve
    x "(He opens his mouth, and I watch in horror as he gathers saliva.)"
    show madd boy shocked at left_small
    with dissolve
    x "(I can see his tongue working inside his mouth.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(Oh God. Oh God, no.)"
    show madd boy horrified at left_small
    with dissolve
    show aman spitting at right_small
    with dissolve
    x "(He spits.)"
    show madd boy devastated at left_small
    with dissolve
    x "(A thick, wet, bubbly mess lands on the toe of his shoe.)"
    show madd boy sickened at left_small
    with dissolve
    x "(The glob glistens, still dripping slightly.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(I can see the saliva bubble forming at the edge of the leather.)"
    show madd boy revolted at left_small
    with dissolve
    aman_says "There's your cleaning agent."
    show aman cruel at right_small
    with dissolve
    show madd boy breaking at left_small
    with dissolve
    x "(His tone is mock-helpful, like he's just given me a gift.)"
    show madd boy humiliated at left_small
    with dissolve
    aman_says "Use your hands. Make it sparkle."
    show aman commanding at right_small
    with dissolve
    show madd boy devastated at left_small
    with dissolve
    x "(My hands...)"
    show madd boy nauseated at left_small
    with dissolve
    x "(He wants me to touch his spit with my bare hands.)"
    show madd boy paralyzed at left_small
    with dissolve
    x "(I can't move.)"
    show madd boy frozen at left_small
    with dissolve
    x "(My body is rebelling against what my mind knows is coming.)"
    show madd boy conflicted at left_small
    with dissolve
    aman_says "(She's hesitating. Good. The longer she stands there, the more the spit dries. She'll have to scrape it off.)"
    show aman malicious at right_small
    with dissolve
    show madd boy shaking at left_small
    with dissolve
    x "(I force my body to obey.)"
    show madd boy submissive at left_small
    with dissolve
    x "(My knees bend automatically now—I don't even think about it anymore.)"
    show madd boy ashamed at left_small
    with dissolve
    show madd boy kneeling at left_small
    with dissolve
    x "(I'm kneeling in front of him again, my eyes level with his foot.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(The spit is right there, waiting for me.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(I can see the individual cells of mucus glistening.)"
    show madd boy horrified at left_small
    with dissolve
    x "(This is saliva. This is from inside his mouth.)"
    show madd boy sickened at left_small
    with dissolve
    x "(And I'm about to touch it with my bare skin.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(My hand is shaking as I reach out.)"
    show madd boy trembling at left_small
    with dissolve
    x "(I'm trying to not think about where it came from.)"
    show madd boy broken at left_small
    with dissolve
    x "(Trying to dissociate.)"
    show madd boy numb at left_small
    with dissolve
    scene scene_aman_intercept_madd_shoe_clean_spit
    with dissolve
    x "(My fingertip makes contact.)"
    show madd boy devastated at left_small
    with dissolve
    x "(It's warm.)"
    show madd boy sickened at left_small
    with dissolve
    x "(Oh God, it's still warm.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(That means it's fresh. That means it just left his mouth.)"
    show madd boy horrified at left_small
    with dissolve
    x "(I start to rub, spreading his saliva across the leather.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(It's slick, sticky, viscous.)"
    show madd boy revolted at left_small
    with dissolve
    x "(My stomach is churning.)"
    show madd boy nauseous at left_small
    with dissolve
    x "(The taste of my own disgust is rising in my throat.)"
    show madd boy traumatized at left_small
    with dissolve
    show aman watching at right_small
    with dissolve
    aman_says "(Look at her. She's about to vomit. This is exactly what I wanted to see.)"
    show aman cruel smile at right_small
    with dissolve
    show madd boy broken at left_small
    with dissolve
    x "(His saliva is spreading, mixing with the dirt on his shoe.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(I'm creating a paste of his spit and shoe dust.)"
    show madd boy sickened at left_small
    with dissolve
    x "(And I'm doing it with my bare hands.)"
    show madd boy ashamed at left_small
    with dissolve
    x "(My skin is crawling.)"
    show madd boy horrified at left_small
    with dissolve
    x "(I can feel the microscopic bacteria from his mouth now coating my fingers.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(This is intimate in the most violating way.)"
    show madd boy broken at left_small
    with dissolve
    x "(I'm literally rubbing his bodily fluid into his shoe.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(And the worst part is that my hands are still shaking because I'm terrified he'll decide this isn't good enough.)"
    show madd boy fearful at left_small
    with dissolve
    aman_says "Harder. Make it shine."
    show aman impatient at right_small
    with dissolve
    show madd boy desperate at left_small
    with dissolve
    x "(I press harder, scrubbing.)"
    show madd boy obedient at left_small
    with dissolve
    x "(The leather is still wet with his spit.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(It's not absorbing anymore—it's just sitting there.)"
    show madd boy panicked at left_small
    with dissolve
    x "(He wants it to shine, but I'm just spreading his saliva around.)"
    show madd boy desperate at left_small
    with dissolve
    aman_says "(She's panicking. Perfect. Let her think she's failing. Let her feel that anxiety crawl up her spine.)"
    show aman satisfied at right_small
    with dissolve
    show madd boy anxious at left_small
    with dissolve
    x "(I keep scrubbing, even though it's hopeless.)"
    show madd boy defeated at left_small
    with dissolve
    x "(His saliva is starting to dry on my fingers now.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(It's getting sticky as it dries.)"
    show madd boy sickened at left_small
    with dissolve
    x "(Like glue made from his mouth.)"
    show madd boy horrified at left_small
    with dissolve
    x "(I'll be able to feel this dried spit on my skin for hours.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(I'll smell it on my hands.)"
    show madd boy ashamed at left_small
    with dissolve
    x "(Every time I lift my fingers to my face, I'll catch the scent of his saliva.)"
    show madd boy broken at left_small
    with dissolve
    show aman nodding at right_small
    with dissolve
    aman_says "There. Now that's service."
    show aman satisfied at right_small
    with dissolve
    show madd boy humiliated at left_small
    with dissolve
    x "(Finally, he seems satisfied.)"
    show madd boy numb at left_small
    with dissolve
    x "(But I'm not finished—the spit is still coating my fingers.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(It's drying into the creases of my skin.)"
    show madd boy disgusted at left_small
    with dissolve
    show aman walking at right_small
    with dissolve
    x "(He walks away without another word.)"
    show madd boy kneeling at left_small
    with dissolve
    x "(I remain on my knees in the hallway, staring at my hands.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(My fingers are still wet with his saliva.)"
    show madd boy horrified at left_small
    with dissolve
    x "(I can't wipe it on anything without staining myself further.)"
    show madd boy defeated at left_small
    with dissolve
    x "(So I sit here, wearing his spit on my hands, wondering how much lower I can go.)"
    show madd boy broken at left_small
    with dissolve
    x "(Wondering if this is the bottom, or if there's still further to fall.)"
    show madd boy numb at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 3
    $ character_relations["aman"]["lust"] += 1
    $ character_relations["aman"]["identity"] += 1
    $ madd_dominance -= 2
    $ madd_secret_identity -= 1
    $ game_time.advance_time(minutes=7)
    return
#images done
label intercept_aman_level_2_event_2:
    """intercept_aman Level 2 Event 2 - The Pheromone Test"""
    scene scene_hostel_hallway
    with fade
    
    show madd boy walking at left_small
    with dissolve
    x "(I'm trying to get past him quickly.)"
    show madd boy cautious at left_small
    with dissolve
    x "(But he's positioned himself against the wall, blocking my path.)"
    show aman blocking at right_small
    with dissolve
    scene scene_aman_intercepts_madd_basic_block
    with dissolve
    x "(There's nowhere to go around him.)"
    show madd boy nervous at left_small
    with dissolve
    show aman casual at right_small
    with dissolve
    aman_says "Hey, I need your honest opinion on something."
    show aman confident at right_small
    with dissolve
    show madd boy hesitant at left_small
    with dissolve
    x "(His tone is casual, almost friendly.)"
    show madd boy confused at left_small
    with dissolve
    x "(But his body language is calculated—he's pinning me against the wall.)"
    show madd boy nervous at left_small
    with dissolve
    x "(My instincts are screaming that something is wrong.)"
    show madd boy frightened at left_small
    with dissolve
    aman_says "I'm worried I smell too much like a winner."
    show aman arrogant at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "(What does that even mean?)"
    show madd boy uncertain at left_small
    with dissolve
    aman_says "All this grinding is making me wonder if I've crossed the line."
    show aman mock-concerned at right_small
    with dissolve
    show madd boy wary at left_small
    with dissolve
    x "(He's setting a trap.)"
    show madd boy frightened at left_small
    with dissolve
    x "(I can feel it in the air.)"
    show madd boy panicked at left_small
    with dissolve
    scene scene_aman_intercept_madd_armpit_smell
    with dissolve

    aman_says "I need you to check the intensity."
    show aman commanding at right_small
    with dissolve
    show madd boy horrified at left_small
    with dissolve
    show aman raising arm at right_small
    with dissolve
    x "(He raises his arm.)"
    show madd boy terrified at left_small
    with dissolve
    x "(His underarm is exposed.)"
    show madd boy sickened at left_small
    with dissolve
    x "(Oh God. He wants me to... to smell him.)"
    show madd boy shocked at left_small
    with dissolve
    x "(I try to step back, but the wall is already behind me.)"
    show madd boy trapped at left_small
    with dissolve
    show aman pressing at right_small
    with dissolve
    x "(He shifts his body, pinning me against the wall.)"
    show madd boy panicked at left_small
    with dissolve
    x "(His underarm is inches from my face now.)"
    show madd boy horrified at left_small
    with dissolve
    aman_says "(She's trapped now. No escape. She'll have to breathe in everything.)"
    show aman cruel at right_small
    with dissolve
    show madd boy trembling at left_small
    with dissolve
    x "(I can already smell it before my face is that close.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(A sharp, acrid scent of stale sweat and something chemical.)"
    show madd boy sickened at left_small
    with dissolve
    x "(Energy drinks. Red Bull or something similar.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(Mixed with the sour smell of unwashed skin.)"
    show madd boy horrified at left_small
    with dissolve
    aman_says "Lean in. Check it."
    show aman commanding at right_small
    with dissolve
    show madd boy shaking at left_small
    with dissolve
    x "(I lean in, my face moving toward his underarm.)"
    show madd boy reluctant at left_small
    with dissolve
    x "(Every instinct is screaming at me to resist.)"
    show madd boy terrified at left_small
    with dissolve
    x "(But I'm completely trapped.)"
    show madd boy broken at left_small
    with dissolve
    x "(My nose comes within inches of his armpit.)"
    show madd boy sickened at left_small
    with dissolve
    show aman pressing at right_small
    with dissolve
    x "(He keeps his arm pressed close, controlling how near I have to be.)"
    show madd boy trembling at left_small
    with dissolve
    x "(The smell is overwhelming now.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(It fills my nostrils, my sinuses, working its way into my lungs.)"
    show madd boy horrified at left_small
    with dissolve
    x "(I can taste it in the back of my throat.)"
    show madd boy gagging at left_small
    with dissolve
    x "(This is the smell of unwashed male sweat mixed with energy drinks.)"
    show madd boy sickened at left_small
    with dissolve
    x "(There's a hint of deodorant underneath, but it's been overpowered.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(This is raw, pungent, deeply human in the worst way.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(My body tries to pull away.)"
    show madd boy panicked at left_small
    with dissolve
    x "(I turn my head, desperate to escape the smell.)"
    show madd boy terrified at left_small
    with dissolve
    show aman shifting at right_small
    with dissolve
    aman_says "(Try to escape, did you? I'll follow you.)"
    show aman cruel at right_small
    with dissolve
    show madd boy trapped at left_small
    with dissolve
    x "(He shifts his body, staying with me.)"
    show madd boy helpless at left_small
    with dissolve
    scene scene_aman_intercept_madd_armpit_smell_aftermath
    with dissolve
    x "(His arm moves to keep his underarm in front of my face.)"
    show madd boy panicked at left_small
    with dissolve
    x "(I can't escape.)"
    show madd boy desperate at left_small
    with dissolve
    x "(There is nowhere to go.)"
    show madd boy defeated at left_small
    with dissolve
    show aman laughing at right_small
    with dissolve
    aman_says "Look at you! Your face is turning green."
    show aman amused at right_small
    with dissolve
    show madd boy gagging at left_small
    with dissolve
    x "(I gag involuntarily.)"
    show madd boy sickened at left_small
    with dissolve
    x "(He's right—I can feel the nausea rising.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(My stomach is churning violently.)"
    show madd boy traumatized at left_small
    with dissolve
    aman_says "(Beautiful. This is what humiliation looks like on her face. Pure revulsion.)"
    show aman satisfied at right_small
    with dissolve
    show madd boy horrified at left_small
    with dissolve
    x "(He's enjoying this.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(He's genuinely enjoying watching me suffer from the smell of his body.)"
    show madd boy broken at left_small
    with dissolve
    aman_says "Take a good whiff. Really get it in there."
    show aman cruel at right_small
    with dissolve
    show madd boy desperate at left_small
    with dissolve
    x "(I'm forced to breathe deeper.)"
    show madd boy choking at left_small
    with dissolve
    x "(The smell is so intense now that it's coating my throat.)"
    show madd boy sickened at left_small
    with dissolve
    x "(I can smell it in my hair, on my skin.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(This odor is going to linger on me for hours.)"
    show madd boy horrified at left_small
    with dissolve
    x "(I'll go into the mess hall smelling like his unwashed underarm.)"
    show madd boy ashamed at left_small
    with dissolve
    x "(Everyone will wonder where that smell came from.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(And I can't explain. I can't say he forced his body odor into my lungs.)"
    show madd boy broken at left_small
    with dissolve
    show aman mocking at right_small
    with dissolve
    aman_says "That's the smell of a 100-hour grind. Take a good whiff."
    show aman arrogant at right_small
    with dissolve
    show madd boy shattered at left_small
    with dissolve
    x "(A 100-hour grind.)"
    show madd boy numb at left_small
    with dissolve
    x "(That's what he calls his video game marathons.)"
    show madd boy devastated at left_small
    with dissolve
    x "(And I'm being made to experience it through his body odor.)"
    show madd boy humiliated at left_small
    with dissolve
    aman_says "It's the closest you'll ever get to being a pro."
    show aman cruel smile at right_small
    with dissolve
    show madd boy destroyed at left_small
    with dissolve
    x "(Being a pro...)"
    show madd boy broken at left_small
    with dissolve
    x "(He's saying the closest I'll ever get to his level is to smell him.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(I'm so beneath him that my entire existence is contained in experiencing his bodily functions.)"
    show madd boy shattered at left_small
    with dissolve
    x "(My face is definitely pale now.)"
    show madd boy gagging at left_small
    with dissolve
    x "(I'm still trying not to vomit.)"
    show madd boy sickened at left_small
    with dissolve
    show aman releasing at right_small
    with dissolve
    aman_says "(She's about to throw up. That's perfect. Let her remember this every time she gags from now on.)"
    show aman satisfied at right_small
    with dissolve
    x "(Finally, he steps back.)"
    show madd boy gasping at left_small
    with dissolve
    x "(I'm gasping for fresh air.)"
    show madd boy desperate at left_small
    with dissolve
    x "(The smell is still in my nostrils, still coating my throat.)"
    show madd boy sickened at left_small
    with dissolve
    show aman walking at right_small
    with dissolve
    aman_says "That's dedication. That's what separates champions from servants."
    show aman dismissive at right_small
    with dissolve
    show madd boy collapsed at left_small
    with dissolve
    x "(He walks away, leaving me gasping against the wall.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(My entire body is shaking from the nausea and panic.)"
    show madd boy broken at left_small
    with dissolve
    x "(I can still smell him on me.)"
    show madd boy horrified at left_small
    with dissolve
    x "(It's in my lungs, in my sinuses, embedded in the fibers of my clothing.)"
    show madd boy sickened at left_small
    with dissolve
    x "(I'll taste him every time I swallow for the next hour.)"
    show madd boy numb at left_small
    with dissolve
    x "(And I can't escape it or wash it away immediately.)"
    show madd boy defeated at left_small
    with dissolve
    x "(I have to carry him with me, his scent a constant reminder that my lungs, my body, my senses—all of it—are his to use.)"
    show madd boy shattered at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 3
    $ character_relations["aman"]["lust"] += 2
    $ character_relations["aman"]["identity"] += 1
    $ madd_dominance -= 2
    $ madd_secret_identity -= 2
    $ game_time.advance_time(minutes=8)
    return
#images done
label intercept_aman_level_3_event_1:
    """intercept_aman Level 3 Event 1 - The Scrotum Scratch"""
    scene scene_hostel_hallway
    with fade
    
    show madd boy walking at left_small
    with dissolve
    x "(I'm trying to stay invisible again.)"
    show madd boy cautious at left_small
    with dissolve
    x "(But he's there, as always, waiting.)"
    show aman blocking at right_small
    with dissolve
    show madd boy nervous at left_small
    with dissolve
    x "(My body goes rigid before my mind even registers the threat.)"
    show madd boy frightened at left_small
    with dissolve
    show aman excited at right_small
    with dissolve
    aman_says "Hey! Perfect timing."
    show aman bragging at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "(He seems in an unusually good mood.)"
    show madd boy wary at left_small
    with dissolve
    x "(That somehow makes it worse.)"
    show madd boy frightened at left_small
    with dissolve
    aman_says "I've got a date tonight. A real one. High-tier girl like I mentioned before."
    show aman arrogant at right_small
    with dissolve
    show madd boy listening at left_small
    with dissolve
    x "(Why is he telling me this?)"
    show madd boy uncertain at left_small
    with dissolve
    aman_says "She's gonna see something special. I'm carrying my team to a bedroom victory tonight."
    show aman crude at right_small
    with dissolve
    show madd boy disgusted at left_small
    with dissolve
    x "(The way he says it makes my skin crawl.)"
    show madd boy horrified at left_small
    with dissolve
    x "(He's talking about sex like it's a competition he's winning.)"
    show madd boy sickened at left_small
    with dissolve
    scene scene_aman_intercept_madd_scrotum_scratch_prep
    with dissolve

    aman_says "(This girl won't know what hit her. I need to be perfect tonight.)"
    show aman satisfied at right_small
    with dissolve
    show madd boy waiting at left_small
    with dissolve
    x "(I'm waiting for the demand.)"
    show madd boy resigned at left_small
    with dissolve
    x "(I know it's coming.)"
    show madd boy dread at left_small
    with dissolve
    show aman reaching at right_small
    with dissolve
    aman_says "But first, I need to make sure everything is... ready."
    show aman commanding at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "(Ready? For what?)"
    show madd boy nervous at left_small
    with dissolve
    aman_says "My natural scent needs to be perfect."
    show aman arrogant at right_small
    with dissolve
    show madd boy horrified at left_small
    with dissolve
    x "(His natural scent...)"
    show madd boy dread at left_small
    with dissolve
    show aman reaching down at right_small
    with dissolve
    scene scene_aman_intercept_madd_scrotum_scratch
    with dissolve
    x "(He's reaching toward his shorts.)"
    show madd boy terrified at left_small
    with dissolve
    x "(Oh God, no. No, he's not—)"
    show madd boy panicked at left_small
    with dissolve
    show aman scratching at right_small
    with dissolve
    x "(He reaches into his shorts.)"
    show madd boy shocked at left_small
    with dissolve
    x "(His hand goes directly into his groin, under his waistband.)"
    show madd boy sickened at left_small
    with dissolve
    aman_says "(Perfect. Look at her face. She knows exactly what I'm about to do.)"
    show aman cruel at right_small
    with dissolve
    show madd boy shaking at left_small
    with dissolve
    x "(He's scratching deliberately.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(I can see his entire forearm moving inside his shorts.)"
    show madd boy horrified at left_small
    with dissolve
    x "(This isn't casual. This isn't an accident.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(He's scratching his scrotum, deliberately stimulating his genitals through his shorts, and he's doing it while staring directly at me.)"
    show madd boy devastated at left_small
    with dissolve
    x "(The seconds stretch.)"
    show madd boy trembling at left_small
    with dissolve
    x "(Five seconds of scratching.)"
    show madd boy sickened at left_small
    with dissolve
    x "(Ten seconds.)"
    show madd boy gasping at left_small
    with dissolve
    x "(His hand is still moving inside his shorts, his eyes locked on my face.)"
    show madd boy panicked at left_small
    with dissolve
    aman_says "(How long can I make her watch? How much can I make her endure without breaking completely?)"
    show aman sadistic at right_small
    with dissolve
    show madd boy broken at left_small
    with dissolve
    x "(This is about power.)"
    show madd boy horrified at left_small
    with dissolve
    x "(This is about forcing me to witness his body, his intimacy, his complete disregard for my humanity.)"
    show madd boy shattered at left_small
    with dissolve
    show aman withdrawing at right_small
    with dissolve
    x "(Finally, he withdraws his hand.)"
    show madd boy gasping at left_small
    with dissolve
    x "(His fingers are still inside his shorts—I can see the outline of his hand.)"
    show madd boy sickened at left_small
    with dissolve
    x "(Those fingers have just been on his genitals.)"
    show madd boy traumatized at left_small
    with dissolve
    show aman thrusting at right_small
    with dissolve
    scene scene_aman_intercept_scrotum_scratch_finger_smell
    with dissolve
    aman_says "I can't show you my rich balls, obviously."
    show aman mocking at right_small
    with dissolve
    show madd boy horrified at left_small
    with dissolve
    x "(The degradation of that phrase hits me like a physical blow.)"
    show madd boy broken at left_small
    with dissolve
    x "(Rich balls. Wealthy genitals. Like his sexuality is a status symbol.)"
    show madd boy sickened at left_small
    with dissolve
    aman_says "But you can tell me if the scent is... inviting."
    show aman commanding at right_small
    with dissolve
    show madd boy panicked at left_small
    with dissolve
    x "(He's about to force his fingers at my face.)"
    show madd boy trembling at left_small
    with dissolve
    x "(I know what's coming.)"
    show madd boy desperate at left_small
    with dissolve
    show aman moving forward at right_small
    with dissolve
    x "(He thrusts his hand forward.)"
    show madd boy horrified at left_small
    with dissolve
    x "(His fingers, still damp from being inside his shorts, are pushed directly at my face.)"
    show madd boy gagging at left_small
    with dissolve
    x "(The smell hits me instantly.)"
    show madd boy sickened at left_small
    with dissolve
    x "(It's thick, musky, deeply male.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(There's sweat, there's the chemical smell of skin, there's something darker, something intimate.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(This is the smell of his genitals.)"
    show madd boy destroyed at left_small
    with dissolve
    x "(I'm being forced to smell the most intimate part of his body.)"
    show madd boy broken at left_small
    with dissolve
    aman_says "(Breathe it in. I know she can smell it. Look at that revulsion.)"
    show aman satisfied at right_small
    with dissolve
    show madd boy gagging at left_small
    with dissolve
    x "(I'm gagging, but I can't move away.)"
    show madd boy helpless at left_small
    with dissolve
    x "(He's keeping his hand there, forcing me to keep smelling.)"
    show madd boy traumatized at left_small
    with dissolve
    aman_says "You missed a spot. Smell here too."
    show aman cruel at right_small
    with dissolve
    show madd boy panicked at left_small
    with dissolve
    x "(He moves his fingers closer.)"
    show madd boy horrified at left_small
    with dissolve
    x "(His fingers are getting dangerously close to my lips.)"
    show madd boy sickened at left_small
    with dissolve
    x "(I'm frozen in place, my body refusing to cooperate with my mind's desperate need to escape.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(The smell is overwhelming now.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(It's coating my throat, filling my lungs.)"
    show madd boy gagging at left_small
    with dissolve
    x "(I can taste it now—the faint metallic taste of his genital odor in the back of my mouth.)"
    show madd boy sickened at left_small
    with dissolve
    aman_says "Delicate sensibilities, huh?"
    show aman mocking at right_small
    with dissolve
    show madd boy shattered at left_small
    with dissolve
    x "(He's mocking me for my revulsion.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(As if being disgusted by his genitals is weakness on my part.)"
    show madd boy broken at left_small
    with dissolve
    aman_says "This girl tonight is going to understand the difference between a real man and whatever you are."
    show aman dismissive at right_small
    with dissolve
    show madd boy devastated at left_small
    with dissolve
    scene scene_aman_intercept_scrotum_scratch_finger_smell_aftermath
    with dissolve
    x "(The comparison cuts deep.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(I'm not even human enough to compare with the girl he's going to be with.)"
    show madd boy shattered at left_small
    with dissolve
    x "(I'm a tool for him to test his scent on.)"
    show madd boy destroyed at left_small
    with dissolve
    show aman stepping back at right_small
    with dissolve
    aman_says "(Good. Her mind is breaking. I can see it happening.)"
    show aman satisfied at right_small
    with dissolve
    x "(He finally steps back.)"
    show madd boy gasping at left_small
    with dissolve
    x "(I'm gasping, trying to clear my lungs of his smell.)"
    show madd boy traumatized at left_small
    with dissolve

    x "(But it's embedded now.)"
    show madd boy sickened at left_small
    with dissolve
    x "(The scent of his genitals is coating my sinuses, my throat, clinging to the inside of my mouth.)"
    show madd boy broken at left_small
    with dissolve
    x "(I'll taste him every time I swallow for the next hour.)"
    show madd boy numb at left_small
    with dissolve
    show aman walking at right_small
    with dissolve
    aman_says "Have a nice day. Thanks for the... quality check."
    show aman dismissive at right_small
    with dissolve
    show madd boy collapsed at left_small
    with dissolve
    x "(He walks away like nothing happened.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(Like he didn't just force the intimate smell of his groin into my face.)"
    show madd boy shattered at left_small
    with dissolve
    x "(I'm standing in the hallway, my entire body trembling.)"
    show madd boy broken at left_small
    with dissolve
    x "(The smell is still there.)"
    show madd boy sickened at left_small
    with dissolve
    x "(His genital odor has been imprinted onto my olfactory system.)"
    show madd boy destroyed at left_small
    with dissolve
    x "(I have to go about my day carrying the smell of his scrotum inside my lungs.)"
    show madd boy numb at left_small
    with dissolve
    x "(Carrying a piece of his intimate body with me everywhere I go.)"
    show madd boy hollow at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 5
    $ character_relations["aman"]["lust"] += 2
    $ character_relations["aman"]["identity"] += 2
    $ madd_dominance -= 3
    $ madd_secret_identity -= 2
    $ game_time.advance_time(minutes=10)
    return

label intercept_aman_level_3_event_2:
    """intercept_aman Level 3 Event 2 - The Neck Contact"""
    scene scene_hostel_hallway
    with fade
    
    show madd boy walking at left_small
    with dissolve
    x "(I'm already feeling broken.)"
    show madd boy numb at left_small
    with dissolve
    x "(The encounter from before still hasn't worn off.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(His scent is still in my sinuses, still in my throat.)"
    show madd boy sickened at left_small
    with dissolve
    show aman blocking at right_small
    with dissolve
    aman_says "Again. Shoes need cleaning."
    show aman commanding at right_small
    with dissolve
    show madd boy resigned at left_small
    with dissolve
    x "(Again.)"
    show madd boy numb at left_small
    with dissolve
    x "(This has become routine now.)"
    show madd boy defeated at left_small
    with dissolve
    aman_says "(She's not even resisting anymore. She just obeys. This is perfect.)"
    show aman satisfied at right_small
    with dissolve
    show madd boy kneeling at left_small
    with dissolve
    x "(I kneel automatically.)"
    show madd boy submissive at left_small
    with dissolve
    x "(My body knows the motion by heart now.)"
    show madd boy broken at left_small
    with dissolve
    show madd boy waiting at left_small
    with dissolve
    x "(I'm waiting to see what twist he'll add this time.)"
    show madd boy dread at left_small
    with dissolve
    show aman gathering at right_small
    with dissolve
    aman_says "Let me make it easier for you."
    show aman cruel at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "(Easier?)"
    show madd boy wary at left_small
    with dissolve
    x "(Nothing about this is easy, and nothing about him is kind.)"
    show madd boy frightened at left_small
    with dissolve
    show aman spitting at right_small
    with dissolve
    x "(He gathers saliva again.)"
    show madd boy sickened at left_small
    with dissolve
    x "(But this time, it's a massive glob.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(Thicker than before, more loaded with mucus.)"
    show madd boy horrified at left_small
    with dissolve
    show aman spitting large at right_small
    with dissolve
    x "(He spits a huge, bubbly mess directly on his shoe.)"
    show madd boy gagging at left_small
    with dissolve
    x "(The amount is obscene—it glistens wetly on the leather.)"
    show madd boy sickened at left_small
    with dissolve
    aman_says "Go ahead. Use your hands."
    show aman commanding at right_small
    with dissolve
    show madd boy reaching at left_small
    with dissolve
    x "(I reach toward the shoe.)"
    show madd boy submissive at left_small
    with dissolve
    x "(But before I can touch it, he lifts his foot.)"
    show madd boy confused at left_small
    with dissolve
    aman_says "Wait. You missed a spot."
    show aman cruel at right_small
    with dissolve
    show madd boy startled at left_small
    with dissolve
    x "(Missed a spot?)"
    show madd boy fearful at left_small
    with dissolve
    x "(There's nothing else to clean yet.)"
    show madd boy nervous at left_small
    with dissolve
    show aman leaning at right_small
    with dissolve
    scene scene_aman_intercept_madd_shoe_spit_gathering
    with dissolve
    aman_says "Let me help you."
    show aman malicious at right_small
    with dissolve
    show madd boy panicked at left_small
    with dissolve
    x "(He's positioning his foot directly against the side of my neck.)"
    show madd boy terrified at left_small
    with dissolve
    x "(The spit-covered leather is pressing against my skin.)"
    show madd boy horrified at left_small
    with dissolve
    show aman rubbing at right_small
    with dissolve
    scene scene_aman_intercept_madd_shoe_clean_on_neck
    with dissolve
    x "(He rubs his shoe slowly across my neck.)"
    show madd boy gagging at left_small
    with dissolve
    x "(The wet warmth of his fresh saliva is transferring directly onto my skin.)"
    show madd boy sickened at left_small
    with dissolve
    x "(His spit is coating my neck like a mark.)"
    show madd boy traumatized at left_small
    with dissolve
    aman_says "(Look at how she's shaking. Absolute perfect submission.)"
    show aman cruel smile at right_small
    with dissolve
    show madd boy trembling at left_small
    with dissolve
    x "(He's marking me.)"
    show madd boy broken at left_small
    with dissolve
    x "(That's what this is—he's using his shoe to brand me with his saliva.)"
    show madd boy shattered at left_small
    with dissolve
    x "(His spit-covered leather is dragging down the side of my neck toward my collarbone.)"
    show madd boy devastated at left_small
    with dissolve
    x "(I can feel his saliva soaking into my skin, my clothes, embedding itself on me.)"
    show madd boy humiliated at left_small
    with dissolve
    show aman continuing at right_small
    with dissolve
    x "(He continues rubbing.)"
    show madd boy panicked at left_small
    with dissolve
    x "(The shoe moves down, down, toward my collarbone and the top of my chest.)"
    show madd boy gasping at left_small
    with dissolve
    x "(The spit is thick, still warm, still dripping.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(He's covering my collarbone with his saliva now.)"
    show madd boy sickened at left_small
    with dissolve
    x "(It soaks into the neckline of my shirt.)"
    show madd boy traumatized at left_small
    with dissolve
    aman_says "Perfect. Look at that."
    show aman laughing at right_small
    with dissolve
    show madd boy shattered at left_small
    with dissolve
    x "(He's laughing.)"
    show madd boy broken at left_small
    with dissolve
    x "(He's genuinely enjoying this—the sight of me covered in his saliva, the feel of me trembling beneath his foot.)"
    show madd boy destroyed at left_small
    with dissolve
    x "(My entire upper body is now marked with his spit.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(The saliva is starting to dry on my skin, tightening, creating a crust of his intimacy.)"
    show madd boy numb at left_small
    with dissolve
    show aman stepping back at right_small
    with dissolve
    aman_says "Now you're properly broken in."
    show aman satisfied at right_small
    with dissolve
    show madd boy collapsed at left_small
    with dissolve
    x "(Broken in.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(Like an object.)"
    show madd boy shattered at left_small
    with dissolve
    x "(Like something that needs to be trained and marked for use.)"
    show madd boy destroyed at left_small
    with dissolve
    aman_says "Every time you smell that leather today, you'll remember exactly who you're working for."
    show aman cruel at right_small
    with dissolve
    show madd boy broken at left_small
    with dissolve
    x "(The leather smell...)"
    show madd boy sickened at left_small
    with dissolve
    x "(My clothing is going to smell like his shoe.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(Every breath I take, every moment of the day, I'll smell the leather that's been rubbed against my skin with his saliva.)"
    show madd boy numb at left_small
    with dissolve
    x "(It's a scent that will follow me everywhere.)"
    show madd boy hollow at left_small
    with dissolve
    x "(A smell that belongs to him, and now it belongs to me.)"
    show madd boy devastated at left_small
    with dissolve
    show aman walking away at right_small
    with dissolve
    scene scene_aman_intercept_madd_shoe_clean_on_neck_aftermath
    with dissolve
    x "(He walks away, leaving me kneeling in the hallway.)"
    show madd boy collapsed at left_small
    with dissolve
    x "(My neck is sticky with his drying saliva.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(My collarbone is marked with his intimate fluid.)"
    show madd boy shattered at left_small
    with dissolve
    x "(And I can't wash it away immediately without drawing attention.)"
    show madd boy broken at left_small
    with dissolve
    x "(I have to walk around carrying his mark on my body.)"
    show madd boy destroyed at left_small
    with dissolve
    x "(Carrying his ownership of me visible on my skin.)"
    show madd boy numb at left_small
    with dissolve
    x "(The leather smell will cling to my clothes for days.)"
    show madd boy hollow at left_small
    with dissolve
    x "(Every time I move, every breath I take, I'll remember the exact moment he decided I was 'properly broken in.')"
    show madd boy devastated at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 5
    $ character_relations["aman"]["lust"] += 3
    $ character_relations["aman"]["identity"] += 2
    $ madd_dominance -= 4
    $ madd_secret_identity -= 3
    $ game_time.advance_time(minutes=7)
    return


# ============================================
# WATER_COOLER_TALK_AMAN LEVEL EVENTS
# ============================================
#images done
label water_cooler_talk_aman_level_1_event_1:
    """water_cooler_talk_aman Level 1 Event 1 - Elbow lean and water dumping"""
    scene scene_hostel_hallway
    with fade
    
    # SCENE 1: Aman approaches from phone browsing

    show madd boy filling at left_small
    with dissolve
    x "(I'm standing at the water cooler, filling my bottle with fresh water.)"
    show madd boy focused at left_small
    with dissolve
    x "(The cool liquid trickles slowly into the plastic container.)"
    show madd boy attentive at left_small
    with dissolve
    x "(I watch the water level rise, making sure it reaches the line I prefer.)"
    show madd boy diligent at left_small
    with dissolve
    show aman phone staring at right_small
    with dissolve
    scene scene_aman_water_cooler_talk_madd_level_1_event_1_start
    with dissolve
    x "(I don't notice Aman standing nearby, his eyes glued to his phone.)"
    show madd boy unaware at left_small
    with dissolve
    x "(He's been standing there the whole time, watching me.)"
    show madd boy innocent at left_small
    with dissolve
    x "(His focus is entirely on whatever skin-trading site he's browsing, but his position gives him a clear view of me at the cooler.)"
    show madd boy unsuspecting at left_small
    with dissolve
    show aman leaning at right_small
    with dissolve
    x "(Without warning, he leans his heavy elbow directly onto my shoulder.)"
    show madd boy shocked at left_small
    with dissolve
    x "(What the...?)"
    show madd boy flustered at left_small
    with dissolve
    x "(His weight presses down on me, using me as a literal piece of furniture to steady himself.)"
    show madd boy uncomfortable at left_small
    with dissolve
    aman_says "Don't move."
    show aman commanding at right_small
    with dissolve
    show madd boy obedient at left_small
    with dissolve
    x "(He's... using me as an armrest...)"
    show madd boy humiliated at left_small
    with dissolve
    x "(I freeze, my shoulders tensing under the pressure of his arm.)"
    show madd boy tense at left_small
    with dissolve
    x "(His eyes remain fixed on his phone, his thumbs typing frantically across the screen.)"
    show madd boy still at left_small
    with dissolve
    aman_says "Hmm... no, that skin's not worth it. Overpriced."
    show aman thinking at right_small
    with dissolve
    show madd boy silent at left_small
    with dissolve
    x "(He's just... talking to himself. Like I'm not even here.)"
    show madd boy resigned at left_small
    with dissolve
    x "(He continues typing, using me as his personal support while he browses.)"
    show madd boy degraded at left_small
    with dissolve
    x "(I don't dare move. The weight of his elbow pins me to my spot.)"
    show madd boy submissive at left_small
    with dissolve
    aman_says "Let me check the market price one more time..."
    show aman focused at right_small
    with dissolve
    x "(Another minute passes. Then another.)"
    show madd boy exhausted at left_small
    with dissolve
    scene scene_aman_water_cooler_talk_madd_level_1_event_1_armsrest_on_madd
    with dissolve
    x "(My shoulder is starting to hurt... but I can't say anything.)"
    show madd boy aching at left_small
    with dissolve
    show aman suddenly moving at right_small
    with dissolve
    x "(Finally, he removes his elbow and stands upright.)"
    show madd boy relieved at left_small
    with dissolve
    show aman realizing at right_small
    with dissolve
    aman_says "Actually, I'm thirsty."
    show aman casual at right_small
    with dissolve
    show madd boy uncertain at left_small
    with dissolve
    x "(He looks at the bottle in my hands—my half-filled bottle.)"
    show madd boy protective at left_small
    with dissolve
    show aman reaching at right_small
    with dissolve
    x "(Without asking, he simply takes it from my hands.)"
    show madd boy shocked at left_small
    with dissolve
    x "(Wait, he's just... taking my water?)"
    show madd boy confused at left_small
    with dissolve
    show aman pouring at right_small
    with dissolve
    scene scene_aman_water_cooler_talk_madd_level_1_event_1_pouring water
    with dissolve
    aman_says "This looks old."
    show aman dismissive at right_small
    with dissolve
    show madd boy horrified at left_small
    with dissolve
    x "(Before I can even protest, he dumps the entire contents of my bottle onto my shoes.)"
    show madd boy shocked at left_small
    with dissolve
    x "(The cool water splashes across my feet, soaking through my shoes.)"
    show madd boy appalled at left_small
    with dissolve
    x "(No... no, he didn't...)"
    show madd boy devastated at left_small
    with dissolve
    show aman arrogant at right_small
    with dissolve
    aman_says "(That was probably stale. Fill mine to the brim.)"
    show aman commanding at right_small
    with dissolve
    show madd boy flustered at left_small
    with dissolve
    aman_says "(If a single bubble is at the top, you're doing it again.)"
    show aman cold at right_small
    with dissolve
    show madd boy trembling at left_small
    with dissolve
    x "(He just... dumped my water on me. Just like that.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(He holds out his empty bottle toward me, waiting.)"
    show madd boy obedient at left_small
    with dissolve
    x "(I take his bottle with shaking hands and move to fill it.)"
    show madd boy submissive at left_small
    with dissolve
    x "(I hold it under the cooler's spout, watching as the water fills it.)"
    show madd boy focused at left_small
    with dissolve
    x "(I need to be careful. I can't mess this up.)"
    show madd boy anxious at left_small
    with dissolve
    x "(I watch the water level rise slowly.)"
    show madd boy concentrated at left_small
    with dissolve
    x "(As it gets closer to the brim, I slow down, being extremely careful.)"
    show madd boy precise at left_small
    with dissolve
    x "(The water reaches the very top, just touching the edge without overflowing.)"
    show madd boy satisfied at left_small
    with dissolve
    aman_says "(Perfect. Now clean up that mess.)"
    show aman commanding at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "(I take his bottle and look down at the puddle of water around my soaked shoes.)"
    show madd boy resigned at left_small
    with dissolve
    aman_says "I already pay you for things like this anyway."
    show aman dismissive at right_small
    with dissolve
    show madd boy defeated at left_small
    with dissolve
    x "(He pays me? I'm not even... I don't work for him like that...)"
    show madd boy protesting at left_small
    with dissolve
    x "(But I don't say anything. I just move to grab paper towels from the nearby dispenser.)"
    show madd boy compliant at left_small
    with dissolve
    x "(I bend down to start wiping up the water from the floor, soaking through my shoes.)"
    show madd boy working at left_small
    with dissolve
    show aman admiring at right_small
    with dissolve
    aman_says "(Wait... when they bend down like that...)"
    show aman tempted at right_small
    with dissolve
    aman_says "(Their figure is actually... kind of nice...)"
    show aman aroused at right_small
    with dissolve
    x "(I'm focused on cleaning, unaware of his gaze.)"
    show madd boy unaware at left_small
    with dissolve
    aman_says "(No... no, what am I thinking? They look so andogenous... I hate that type...)"
    show aman conflicted at right_small
    with dissolve
    aman_says "(Im not like that. I'm not attracted to... that.)"
    show aman disgusted at right_small
    with dissolve
    show aman turning at right_small
    with dissolve
    x "(He abruptly turns away, walking back down the hallway without another word.)"
    show aman cold at right_small
    with dissolve
    show madd boy humiliated at left_small
    with dissolve
    x "(He just... used me as furniture, dumped water on me, and walked away.)"
    show madd boy broken at left_small
    with dissolve
    x "(I continue cleaning up his mess, my wet shoes squelching against the floor.)"
    show madd boy defeated at left_small
    with dissolve
    x "(And he said he already pays me for this. Like I'm his permanent maid.)"
    show madd boy traumatized at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 2
    $ character_relations["aman"]["lust"] += 1
    $ character_relations["aman"]["identity"] += 1
    $ madd_dominance -= 2
    $ madd_secret_identity -= 1
    $ game_time.advance_time(minutes=10)
    return
#images done
label water_cooler_talk_aman_level_1_event_2:
    """water_cooler_talk_aman Level 1 Event 2 - Bottle 'cleaning' with finger"""
    scene scene_hostel_hallway
    with fade
    
    # SCENE 1: Player fills bottle, Aman appears and judges it
    scene scene_wc_aman_l1e2_bottle_full
    with dissolve
    show madd boy filling at left_small
    with dissolve
    x "(I'm at the water cooler, just finished filling my bottle.)"
    show madd boy satisfied at left_small
    with dissolve
    x "(The cool water glistens under the hallway lights.)"
    show madd boy proud at left_small
    with dissolve
    show aman appearing at right_small
    with dissolve
    scene scene_aman_water_cooler_talk_madd_level_1_event_1_start
    with dissolve
    x "(Aman suddenly appears, glancing at my bottle.)"
    show madd boy startled at left_small
    with dissolve
    aman_says "Step aside."
    show aman commanding at right_small
    with dissolve
    show madd boy obedient at left_small
    with dissolve
    x "(Without questioning, I move to the side to let him access the cooler.)"
    show madd boy compliant at left_small
    with dissolve
    show aman scrutinizing at right_small
    with dissolve
    aman_says "(Hey, that doesn't look clean.)"
    show aman critical at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "(What? My bottle? It's brand new...)"
    show madd boy uncertain at left_small
    with dissolve
    x "(He gestures toward my bottle dismissively.)"
    show madd boy questioning at left_small
    with dissolve
    show aman reaching at right_small
    with dissolve
    # SCENE 2: Aman takes bottle and inserts finger
    scene scene_aman_water_cooler_talk_madd_level1_event2_swirl_fingers_inside_madd_bottle
    with dissolve
    x "(Before I can even respond, he reaches over and takes the bottle from my hands.)"
    show madd boy shocked at left_small
    with dissolve
    show aman opening at right_small
    with dissolve
    aman_says "(Let me help you.)"
    show aman casual at right_small
    with dissolve
    show madd boy nervous at left_small
    with dissolve
    x "(He opens the bottle cap and looks inside.)"
    show madd boy apprehensive at left_small
    with dissolve
    show aman mocking at right_small
    with dissolve
    aman_says "(Yeah, see? Impurities. This needs fixing.)"
    show aman dismissive at right_small
    with dissolve
    show madd boy bewildered at left_small
    with dissolve
    x "(Impurities? It's fresh water from the cooler...)"
    show madd boy defensive at left_small
    with dissolve
    show aman inserting at right_small
    with dissolve
    x "(He sticks his index finger directly into my bottle.)"
    show madd boy horrified at left_small
    with dissolve
    x "(No... he's putting his finger in my water...)"
    show madd boy disgusted at left_small
    with dissolve
    aman_says "This should fix it."
    show aman casual at right_small
    with dissolve
    show madd boy revulsed at left_small
    with dissolve
    x "(He begins moving his finger in a slow, deliberate circular motion inside my bottle.)"
    show madd boy mortified at left_small
    with dissolve
    x "(This is disgusting... what is he doing?)"
    show madd boy violated at left_small
    with dissolve
    x "(He twirls his finger around and around, the water swirling around his digit.)"
    show madd boy traumatized at left_small
    with dissolve
    aman_says "There we go... that should purify it nicely."
    show aman smirking at right_small
    with dissolve
    show madd boy silent at left_small
    with dissolve
    x "(I watch in disbelief as he continues stirring the water with his bare finger.)"
    show madd boy numb at left_small
    with dissolve
    x "(I can't believe he's actually doing this to me...)"
    show madd boy powerless at left_small
    with dissolve
    show aman withdrawing at right_small
    with dissolve
    # SCENE 3: Aman withdraws finger, hands bottle back, walks away
    scene scene_aman_water_cooler_talk_madd_level1_event2_handover_bottle_to_madd
    with dissolve
    x "(Finally, he pulls his finger out of the water.)"
    show madd boy anxious at left_small
    with dissolve
    show aman capping at right_small
    with dissolve
    aman_says "(There you go. Much better now.)"
    show aman pleased at right_small
    with dissolve
    show madd boy devastated at left_small
    with dissolve
    x "(He caps the bottle and hands it back to me with an air of accomplishment.)"
    show madd boy mortified at left_small
    with dissolve
    x "(He just... contaminated my water... on purpose...)"
    show madd boy humiliated at left_small
    with dissolve
    x "(I take the bottle back from his hands, my skin crawling.)"
    show madd boy reluctant at left_small
    with dissolve
    x "(The water inside now has the faint scent of his skin on it.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(I can't drink this now... it's ruined...)"
    show madd boy resigned at left_small
    with dissolve
    show aman walking at right_small
    with dissolve
    x "(Aman walks away without another word, leaving me standing there with my contaminated bottle.)"
    show madd boy broken at left_small
    with dissolve
    x "(What kind of person does that? Just... sticks their finger in someone's water?)"
    show madd boy betrayed at left_small
    with dissolve
    x "(I look down at the bottle in my hands, and I realize I'll have to empty it and refill.)"
    show madd boy defeated at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 1
    $ character_relations["aman"]["lust"] += 1
    $ character_relations["aman"]["identity"] += 1
    $ madd_dominance -= 1
    $ madd_secret_identity -= 1
    $ game_time.advance_time(minutes=5)
    return
#images done
label water_cooler_talk_aman_level_2_event_1:
    """water_cooler_talk_aman Level 2 Event 1 - Sweaty towel judgement"""
    scene scene_hostel_hallway
    with fade
    
    # SCENE 1: Aman approaches sweaty with towel from workout

    show aman post workout at right_small
    with dissolve
    x "(I'm at the water cooler when I notice Aman standing nearby.)"
    show madd boy aware at left_small
    with dissolve
    x "(He has a towel draped over his shoulders, dark with sweat.)"
    show madd boy observant at left_small
    with dissolve
    scene scene_aman_water_cooler_talk_madd_level_1_event_1_start
    with dissolve    
    x "(He looks like he just ran a marathon... he's soaked.)"
    show madd boy uncomfortable at left_small
    with dissolve
    show aman wiping at right_small
    with dissolve
    x "(He grabs the towel and rubs it vigorously over his neck and chest.)"
    show madd boy uneasy at left_small
    with dissolve
    scene scene_aman_water_cooler_talk_madd_level2_event1_rubs_towel_underarm
    with dissolve
    x "(The movement is rough and aggressive, working the fabric against his sweaty skin.)"
    show madd boy nervous at left_small
    with dissolve
    show aman lifting at right_small
    with dissolve
    aman_says "Hmm..."
    show aman focused at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "(He lifts his shirt and starts wiping his underarms with the towel, the fabric disappearing under the fabric of his shirt.)"
    show madd boy disturbed at left_small
    with dissolve
    x "(Oh god... he's just... rubbing that towel all over his body...)"
    show madd boy disgusted at left_small
    with dissolve
    show aman pulling at right_small
    with dissolve
    x "(He pulls the towel back out, now even more saturated with sweat.)"
    show madd boy horrified at left_small
    with dissolve
    show aman throwing at right_small
    with dissolve
    aman_says "Here, catch."
    show aman commanding at right_small
    with dissolve
    show madd boy shocked at left_small
    with dissolve
    # SCENE 2: Aman throws towel, player catches and smells it
    scene scene_aman_water_cooler_talk_madd_level_2_event_1_towel_in_madds_face
    with dissolve
    x "(Without warning, he throws the filthy, sweat-soaked towel directly at my face.)"
    show madd boy appalled at left_small
    with dissolve
    x "(The wet fabric hits me and clings to my skin.)"
    show madd boy gagging at left_small
    with dissolve
    x "(No... no, this is... this is his sweat...)"
    x "(The smell is overpowering... a mix of salt, musk, and something acrid.)"
    x "(I can feel the dampness of the towel against my face, soaking into my clothes.)"
    show madd boy revolted at left_small
    with dissolve
    aman_says "Tell me something, poor girl. You people have a good sense of smell for filth, right?"
    show aman mocking at right_small
    with dissolve
    show madd boy flustered at left_small
    with dissolve
    aman_says "Judge that towel for me. Can I reuse it?"
    show aman dismissive at right_small
    with dissolve
    show madd boy trembling at left_small
    with dissolve
    x "(He wants me to... smell his sweat towel?)"
    show madd boy humiliated at left_small
    with dissolve
    x "(This is absolutely disgusting... but what choice do I have?)"
    show madd boy resigned at left_small
    with dissolve
    x "(I reluctantly bring the towel closer to my face, my stomach churning with revulsion.)"
    show madd boy hesitant at left_small
    with dissolve
    x "(I take a breath and inhale the scent of his sweat.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(Oh my god... the smell is... it's overwhelming...)"
    show madd boy gagging at left_small
    with dissolve
    x "(Sweat and... something else... something pungent and acrid...)"
    show madd boy disgusted at left_small
    with dissolve
    x "(This towel reeks. It absolutely reeks.)"
    show madd boy broken at left_small
    with dissolve
    x "(I pull the towel away from my face, my eyes watering.)"
    show madd boy traumatized at left_small
    with dissolve
    aman_says "Well? What's the verdict?"
    show aman curious at right_small
    with dissolve
    show madd boy flustered at left_small
    with dissolve
    x "It... it smells full of sweat."
    show madd boy embarrassed at left_small
    with dissolve
    x "It's not good at all for reuse."
    show madd boy ashamed at left_small
    with dissolve
    show aman grinning at right_small
    with dissolve
    aman_says "You know what? You can have it then."
    show aman casual at right_small
    with dissolve
    show madd boy shocked at left_small
    with dissolve
    x "(He's... giving me his sweat towel?)"
    show madd boy horrified at left_small
    with dissolve
    aman_says "I'm sure you could use a good towel, being poor and all."
    show aman mocking at right_small
    with dissolve
    scene scene_aman_water_cooler_level2_event1_madd_holding_towel
    show madd boy degraded at left_small
    with dissolve
    x "(I'm holding his disgusting, sweat-soaked towel... and he's insulting me while doing it.)"
    show madd boy humiliated at left_small
    with dissolve
    show aman walking at right_small
    with dissolve
    x "(He turns and walks away without ever going near the water cooler.)"
    show madd boy defeated at left_small
    with dissolve
    x "(He never even wanted water... he just wanted to humiliate me with his towel.)"
    show madd boy broken at left_small
    with dissolve
    x "(I'm left standing there, holding his filthy towel, my face and hands covered in his sweat.)"
    show madd boy traumatized at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 3
    $ character_relations["aman"]["lust"] += 2
    $ character_relations["aman"]["identity"] += 1
    $ madd_dominance -= 2
    $ madd_secret_identity -= 1
    $ game_time.advance_time(minutes=10)
    return
#images done
label water_cooler_talk_aman_level_2_event_2:
    """water_cooler_talk_aman Level 2 Event 2 - Towel pickup and groping"""
    scene scene_hostel_hallway
    with fade
    
    # SCENE 1: Towel drops as Aman shifts weight
    scene scene_aman_water_cooler_talk_madd_level_1_event_1_start
    with dissolve
    show aman post workout at right_small
    with dissolve
    x "(Im standing by the water cooler when I see Aman standing nearby.)"
    show madd boy aware at left_small
    with dissolve
    x "(He has a towel draped over his shoulders from what looks like a workout.)"
    show madd boy observant at left_small
    with dissolve
    show aman moving at right_small
    with dissolve
    x "(As he shifts his weight, the towel suddenly slips off his shoulders and falls to the floor.)"
    show madd boy startled at left_small
    with dissolve
    show aman commanding at right_small
    with dissolve
    aman_says "Pick that up."
    show aman cold at right_small
    with dissolve
    show madd boy obedient at left_small
    with dissolve
    x "(He's not even asking... he's commanding me to pick it up.)"
    show madd boy nervous at left_small
    with dissolve
    x "(I don't want to imagine all the places that towel has been... his neck, his underarms, his back... all soaked in sweat...)"
    show madd boy uncomfortable at left_small
    with dissolve
    x "(But I have no choice.)"
    show madd boy resigned at left_small
    with dissolve
    # SCENE 2: Player bends down to pick up towel, Aman gropes
    scene scene_aman_water_cooler_level_2_event_2_towel_drop
    with dissolve
    x "(I bend down to pick up the towel from the floor.)"
    show madd boy bent over at left_small
    with dissolve
    show aman watching at right_small
    with dissolve
    aman_says "(Damn... that figure...)"
    show aman tempted at right_small
    with dissolve
    show madd boy unaware at left_small
    with dissolve
    x "(I'm focused on retrieving the towel, completely unaware of his gaze.)"
    show madd boy innocent at left_small
    with dissolve
    show aman approaching at right_small
    with dissolve
    scene scene_aman_water_cooler_level_2_event_2_touch_butt
    with dissolve
    x "(Suddenly, I feel a hand on my back as I'm bent over.)"
    show madd boy shocked at left_small
    with dissolve
    show aman caressing at right_small
    with dissolve
    aman_says "(Their butt is so soft... so feminine...)"
    show aman aroused at right_small
    with dissolve
    show madd boy flustered at left_small
    with dissolve
    x "(His hand slides down from my back to my ass, caressing it slowly.)"
    show madd boy embarrassed at left_small
    with dissolve
    x "(He's... he's touching me...)"
    show madd boy mortified at left_small
    with dissolve
    show aman groping at right_small
    with dissolve
    aman_says "(I don't want to let go... it feels so good...)"
    show aman conflicted at right_small
    with dissolve
    show madd boy uncomfortable at left_small
    with dissolve
    x "(His touch lingers, his hand continuing to caress my ass.)"
    show madd boy violated at left_small
    with dissolve
    x "(His grip tightens, as if he's reluctant to remove his hand.)"
    show madd boy disturbed at left_small
    with dissolve
    aman_says "(But wait... no... they look so andogenous... I don't like that type...)"
    show aman disgusted at right_small
    with dissolve
    aman_says "(I hate andogenous people. I'm not attracted to... that.)"
    show aman defensive at right_small
    with dissolve
    show madd boy silent at left_small
    with dissolve
    x "(His hand suddenly releases me, pulling away abruptly.)"
    show madd boy relieved at left_small
    with dissolve
    show aman turning at right_small
    with dissolve
    x "(He turns without a word and walks away down the hallway.)"
    show aman cold at right_small
    with dissolve
    show madd boy standing at left_small
    with dissolve
    x "(What just happened? He touched me and then... just left?)"
    show madd boy confused at left_small
    with dissolve
    x "(I straighten up, towel in hand, my face burning with humiliation and confusion.)"
    show madd boy ashamed at left_small
    with dissolve
    x "(I felt his touch on me... and for a moment, he didn't want to let go...)"
    show madd boy traumatized at left_small
    with dissolve
    
    $ character_relations["aman"]["lust"] += 2
    $ character_relations["aman"]["identity"] += 1
    $ madd_dominance -= 2
    $ madd_secret_identity -= 1
    $ game_time.advance_time(minutes=5)
    return
#images done
label water_cooler_talk_aman_level_3_event_1:
    """water_cooler_talk_aman Level 3 Event 1 - Towel with private area"""
    scene scene_hostel_hallway
    with fade
    
    # SCENE 1: Aman wipes towel over body including private areas
    scene scene_aman_water_cooler_talk_madd_level_1_event_1_start
    with dissolve
    show aman post workout at right_small
    with dissolve
    x "(I'm at the water cooler when I notice Aman standing nearby.)"
    show madd boy aware at left_small
    with dissolve
    x "(He has a towel draped over his shoulders, dark with sweat.)"
    show madd boy observant at left_small
    with dissolve
    x "(He looks like he just ran a marathon... he's soaked in sweat.)"
    show madd boy uncomfortable at left_small
    with dissolve
    show aman wiping at right_small
    with dissolve
    x "(He grabs the towel and rubs it vigorously over his neck and chest.)"
    show madd boy uneasy at left_small
    with dissolve
    x "(The movement is rough and aggressive, working the fabric against his sweaty skin.)"
    show madd boy nervous at left_small
    with dissolve
    show aman lifting at right_small
    with dissolve
    aman_says "So much sweat today..."
    show aman focused at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "(He lifts his shirt and starts wiping his underarms with the towel, the fabric disappearing under his clothing.)"
    show madd boy disturbed at left_small
    with dissolve
    scene scene_aman_water_cooler_talk_madd_level2_event1_rubs_towel_underarm
    with dissolve   
    x "(Oh god... he's just rubbing that towel all over his body...)"
    show madd boy disgusted at left_small
    with dissolve
    show aman pulling at right_small
    with dissolve
    x "(But he doesn't stop there.)"
    show madd boy shocked at left_small
    with dissolve
    x "(He reaches down and stuffs the towel into his shorts.)"
    show madd boy horrified at left_small
    with dissolve
    x "(What... what is he doing...?)"
    show madd boy appalled at left_small
    with dissolve
    aman_says "Gotta get everywhere..."
    show aman casual at right_small
    with dissolve
    scene scene_aman_water_cooler_talk_madd_level3_event1_rubs_towel_ass
    with dissolve

    show madd boy trembling at left_small
    with dissolve
    x "(He begins rubbing the towel against his ass and the area right under his scrotum, moving it back and forth deliberately.)"
    show madd boy gagging at left_small
    with dissolve
    x "(No... no, he's not... he's using that towel to wipe his... his private area...)"
    show madd boy nauseated at left_small
    with dissolve
    x "(I can't believe what I'm seeing.)"
    show madd boy disgusted at left_small
    with dissolve
    show aman pulling at right_small
    with dissolve
    # SCENE 2: Aman throws filthy towel at player's face

    x "(Finally, he pulls the towel out of his shorts, now completely saturated with his sweat and filth.)"
    show madd boy horrified at left_small
    with dissolve
    show aman throwing at right_small
    with dissolve
    aman_says "Here, catch."
    show aman commanding at right_small
    with dissolve
    show madd boy shocked at left_small
    with dissolve
    scene scene_aman_water_cooler_talk_madd_level_2_event_1_towel_in_madds_face
    with dissolve
    x "(He throws the disgustingly filthy towel directly at my face.)"
    show madd boy appalled at left_small
    with dissolve
    x "(The wet fabric hits me and clings to my skin, reeking of his most private areas.)"
    show madd boy gagging at left_small
    with dissolve
    x "(The moment the towel touches my face, the smell hits me like a physical force.)"
    show madd boy horrified at left_small
    with dissolve
    x "(Oh god... oh god, the smell...)"
    show madd boy nauseated at left_small
    with dissolve
    x "(It's a mixture of raw, unwashed sweat—acrid and pungent—mixed with something darker, something more intimate and vile.)"
    show madd boy revolted at left_small
    with dissolve
    x "(The stench of his crotch, his ass, everything between—it's all soaked into this towel.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(I can smell the salt of his sweat, the musk of his body, and something rank and organic that makes my stomach churn violently.)"
    show madd boy gagging at left_small
    with dissolve
    x "(My eyes water instantly from the assault of the odor.)"
    show madd boy horrified at left_small
    with dissolve
    x "(This is... this is absolutely vile... I can smell where this has been... every place on his body...)"
    show madd boy revolted at left_small
    with dissolve
    x "(I feel my face flushing hot with shame, my stomach twisting.)"
    show madd boy broken at left_small
    with dissolve
    x "(The worst part is that I can't escape it—the smell clings to my face, fills my nostrils, coats the inside of my mouth.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(I can taste it. I can actually taste his filth in the air.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(What kind of person does this? What kind of person am I for accepting this? I quickly pull the towel away from my face, my eyes watering profusely.)"
    show madd boy defeated at left_small
    with dissolve
    aman_says "Tell me something, poor girl. You people have a good sense of smell for filth, right?"
    show aman mocking at right_small
    with dissolve
    show madd boy flustered at left_small
    with dissolve
    aman_says "Judge that towel for me. Can I reuse it?"
    show aman dismissive at right_small
    with dissolve
    show madd boy trembling at left_small
    with dissolve
    x "(He wants me to smell this again... after it's been... in his shorts...)"
    show madd boy humiliated at left_small
    with dissolve
    scene scene_aman_water_cooler_talk_madd_level3_event1_rubs_towel_ass_smell_again
    with dissolve
    x "(I... I can't refuse. I know what choice I have to make.)"
    show madd boy resigned at left_small
    with dissolve
    x "(I reluctantly bring the towel closer to my face, my body shaking with revulsion.)"
    show madd boy hesitant at left_small
    with dissolve
    x "(I take a shallow breath and inhale the scent.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(Oh my god... the smell is... it's overwhelming... sweat and... and...)"
    show madd boy gagging at left_small
    with dissolve
    x "(I can smell where it's been... where it's been on his body... his most intimate places...)"
    show madd boy traumatized at left_small
    with dissolve
    x "(This is the worst thing I've ever smelled.)"
    show madd boy broken at left_small
    with dissolve
    x "(I pull the towel away from my face, my eyes watering profusely.)"
    show madd boy devastated at left_small
    with dissolve
    aman_says "Well? What's the verdict?"
    show aman curious at right_small
    with dissolve
    show madd boy flustered at left_small
    with dissolve
    x "It... it smells full of sweat."
    show madd boy embarrassed at left_small
    with dissolve
    x "It's not good at all for reuse."
    show madd boy ashamed at left_small
    with dissolve
    show aman grinning at right_small
    with dissolve
    aman_says "You know what? You can have it then."
    show aman casual at right_small
    with dissolve
    show madd boy shocked at left_small
    with dissolve
    x "(He's giving me... his filthy towel...)"
    show madd boy horrified at left_small
    with dissolve
    aman_says "I'm sure you could use it. Being poor and all."
    show aman mocking at right_small
    with dissolve
    show madd boy degraded at left_small
    with dissolve
    x "(He's insulting me while giving me this... this vile towel...)"
    show madd boy humiliated at left_small
    with dissolve
    show aman walking at right_small
    with dissolve
    x "(He turns and walks away without ever going near the water cooler.)"
    show madd boy defeated at left_small
    with dissolve
    x "(He never wanted water... this was all just to humiliate me... to make me smell where he's been most intimate...)"
    show madd boy broken at left_small
    with dissolve
    x "(I'm left standing there, holding the filthiest towel imaginable, feeling utterly violated and degraded.)"
    show madd boy traumatized at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 5
    $ character_relations["aman"]["lust"] += 3
    $ character_relations["aman"]["identity"] += 2
    $ madd_dominance -= 4
    $ madd_secret_identity -= 2
    $ game_time.advance_time(minutes=10)
    return
#images done
label water_cooler_talk_aman_level_3_event_2:
    """water_cooler_talk_aman Level 3 Event 2 - Hand washing in palms"""
    scene scene_hostel_hallway
    with fade
    
    # SCENE 1: Aman eating Cheetos and sucking fingers

    show aman eating at right_small
    with dissolve
    x "(I'm standing at the water cooler when I notice Aman walking toward me.)"
    show madd boy aware at left_small
    with dissolve
    scene scene_aman_water_cooler_level_3_event_2_aman_eating_cheetos
    with dissolve
    x "(He's eating something messy—looks like Cheetos or some kind of orange-dusted snack.)"
    show madd boy observant at left_small
    with dissolve
    x "(His fingers are completely covered in orange dust, the powder coating his skin.)"
    show madd boy uncomfortable at left_small
    with dissolve
    show aman tasting at right_small
    with dissolve
    aman_says "(Hmm... these are good...)"
    show aman satisfied at right_small
    with dissolve
    show madd boy nervous at left_small
    with dissolve
    x "(He brings his dust-covered fingers to his mouth.)"
    show madd boy flustered at left_small
    with dissolve
    x "(He sucks on them, tasting the cheeto dust and coating them with his saliva.)"
    show madd boy disturbed at left_small
    with dissolve
    show aman approaching at right_small
    with dissolve
    x "(He walks closer to me, his wet, saliva-coated fingers now glistening.)"
    show madd boy startled at left_small
    with dissolve
    show aman rubbing at right_small
    with dissolve
    aman_says "Let me just clean these on something useful..."
    show aman commanding at right_small
    with dissolve
    show madd boy shocked at left_small
    with dissolve
    # SCENE 2: Aman wipes fingers on player's shirt
    scene scene_aman_water_cooler_level_3_event_2_aman_eating_cheetos_wipe_fingers_on_madd_shirt
    with dissolve
    x "(Without warning, he reaches out and rubs his dirty, wet fingers directly on my shirt.)"
    show madd boy appalled at left_small
    with dissolve
    x "(The orange dust and his saliva smear across the fabric of my clothes.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(He's... he's wiping his fingers on me...)"
    show madd boy nauseated at left_small
    with dissolve
    x "(I feel the wetness seep into my shirt, the greasy residue coating my skin.)"
    show madd boy horrified at left_small
    with dissolve
    aman_says "Don't move. I need a sink, but you'll do."
    show aman cold at right_small
    with dissolve
    show madd boy trembling at left_small
    with dissolve
    x "(He's... he's treating me like I'm an object... like I'm a towel he can use...)"
    show madd boy humiliated at left_small
    with dissolve
    x "(I freeze, unable to move or protest.)"
    show madd boy frozen at left_small
    with dissolve
    show aman commanding at right_small
    with dissolve
    aman_says "Cup your hands together. Now."
    show aman demanding at right_small
    with dissolve
    show madd boy obedient at left_small
    with dissolve
    x "(He wants me to... cup my hands?)"
    show madd boy confused at left_small
    with dissolve
    x "(I slowly raise my hands in front of me, cupping them together like a bowl.)"
    show madd boy reluctant at left_small
    with dissolve
    show aman filling at right_small
    with dissolve
    # SCENE 3: Aman washes fingers in player's cupped hands
    scene scene_aman_water_cooler_level_3_event_2_aman_eating_cheetos_madd_cupped_hands_dip
    with dissolve
    x "(He reaches over to the water cooler and fills my cupped hands with cold water.)"
    show madd boy startled at left_small
    with dissolve
    x "(The water sits in my palms, pooling between my fingers.)"
    show madd boy uncertain at left_small
    with dissolve
    aman_says "Thank you for the sink."
    show aman casual at right_small
    with dissolve
    show madd boy flustered at left_small
    with dissolve
    x "(He plunges his dirty, greasy fingers directly into the water sitting in my hands.)"
    show madd boy shocked at left_small
    with dissolve
    x "(Oh god... his fingers... in my hands...)"
    show madd boy traumatized at left_small
    with dissolve
    show aman washing at right_small
    with dissolve
    x "(He begins rubbing his fingers together in my palms, washing away the orange dust and cheeto residue.)"
    show madd boy violated at left_small
    with dissolve
    x "(The greasy, dirty water swirls between my hands as he cleanses himself.)"
    show madd boy degraded at left_small
    with dissolve
    x "(This is... he's using me as a sink... as a washing bowl...)"
    show madd boy humiliated at left_small
    with dissolve
    x "(I can feel the grit of the dust, the slickness of the grease, the warmth of his skin.)"
    show madd boy numb at left_small
    with dissolve
    x "(I can't refuse. I never refuse. What crime did I commit to deserve this?)"
    show madd boy broken at left_small
    with dissolve
    x "(What did I do to deserve being treated like... like this?)"
    show madd boy anguished at left_small
    with dissolve
    show aman satisfied at right_small
    with dissolve
    x "(He continues washing his fingers in my cupped hands, completely unbothered by what he's making me do.)"
    show madd boy powerless at left_small
    with dissolve
    x "(I'm standing here, holding water in my hands while he uses me to clean himself...)"
    show madd boy defeated at left_small
    with dissolve
    x "(This is my life now. This is what I've become.)"
    show madd boy devastated at left_small
    with dissolve
    show aman withdrawing at right_small
    with dissolve
    x "(He finally withdraws his hands from my palms.)"
    show madd boy relieved at left_small
    with dissolve
    aman_says "There. Much better."
    show aman satisfied at right_small
    with dissolve
    show madd boy traumatized at left_small
    with dissolve
    x "(He walks away as if nothing happened, leaving me standing there with his dirty water dripping from my hands.)"
    show madd boy broken at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 5
    $ character_relations["aman"]["lust"] += 2
    $ character_relations["aman"]["identity"] += 2
    $ madd_dominance -= 4
    $ madd_secret_identity -= 2
    $ game_time.advance_time(minutes=10)
    return


# ============================================
# INTERACT_AMAN_MESS_HALL_MET LEVEL EVENTS
# ============================================
#images done
label interact_aman_mess_hall_met_level_1_event_1:
    """interact_aman_mess_hall_met Level 1 Event 1 - Human phone stand"""
    scene scene_messhall_breakfast
    with fade
    
    show aman eating at right_small
    with dissolve
    x "(I'm sitting at the mess hall table with Aman, who has his phone propped up on the table.)"
    show madd boy standing at left_small
    with dissolve
    scene scene_interact_aman_mess_hall_met_level_1_event_1_madd_told_to_hold_phone
    with dissolve
    
    aman_says "This is annoying. The stream keeps freezing when I look down."
    show aman frustrated at right_small
    with dissolve
    show madd boy attentive at left_small
    with dissolve
    aman_says "Stand here. And hold my phone at eye level. Exactly six inches from my face."
    show aman commanding at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "(He wants me to... hold his phone while he eats?)"
    show madd boy uncertain at left_small
    with dissolve
    show aman cold at right_small
    with dissolve
    aman_says "Now. A high-stakes match is about to start."
    show aman dismissive at right_small
    with dissolve
    show madd boy obedient at left_small
    with dissolve
    x "(I stand beside him and raise his phone to eye level, exactly six inches from his face.)"
    show madd boy submissive at left_small
    with dissolve
    # SCENE 1: Phone held aloft
    scene scene_interact_aman_mess_hall_met_level_1_event_1_madd_holding_phone
    with dissolve
    x "(My arm extends outward, holding the device steady.)"
    show madd boy focused at left_small
    with dissolve
    aman_says "Perfect. Don't move."
    show aman satisfied at right_small
    with dissolve
    show madd boy determined at left_small
    with dissolve
    x "(He goes back to eating, his eyes glued to the CS:GO tournament stream.)"
    show madd boy standing at left_small
    with dissolve
    x "(The match begins. Teams clash on the map, weapons firing, strategies unfolding.)"
    show madd boy attentive at left_small
    with dissolve
    x "(The match is intense, fast-paced. Aman is completely absorbed.)"
    show madd boy tired at left_small
    with dissolve
    x "(I need to stay still... I need to keep my arm steady...)"
    show madd boy concentrating at left_small
    with dissolve
    # SCENE 2: Arm trembling in agony
    scene scene_interact_aman_mess_hall_met_level_1_event_1_madd_holding_phone_trembling
    with dissolve
    x "(Minutes pass. Five minutes. Ten minutes.)"
    show madd boy aching at left_small
    with dissolve
    x "(My arm begins to tremble from the strain of holding the phone aloft.)"
    show madd boy shaking at left_small
    with dissolve
    x "(Oh god... my arm is starting to hurt...)"
    show madd boy struggling at left_small
    with dissolve
    x "(The weight of the phone, though not heavy, becomes increasingly unbearable in this position.)"
    show madd boy trembling at left_small
    with dissolve
    x "(Every muscle fiber in my shoulder and arm screams in protest.)"
    show madd boy exhausted at left_small
    with dissolve
    x "(The phone shakes slightly.)"
    show madd boy nervous at left_small
    with dissolve
    show aman noticing at right_small
    with dissolve
    aman_says "What the hell? The screen is shaking!"
    show aman angry at right_small
    with dissolve
    show madd boy frightened at left_small
    with dissolve
    x "(He looks at me with contempt.)"
    show madd boy panicked at left_small
    with dissolve
    aman_says "Keep it steady. This is a crucial round."
    show aman cold at right_small
    with dissolve
    show madd boy apologetic at left_small
    with dissolve
    x "(I'm sorry... I'm so sorry... I'm trying...)"
    show madd boy desperate at left_small
    with dissolve
    x "(I squeeze my muscles tighter, fighting through the pain to keep the phone perfectly still.)"
    show madd boy straining at left_small
    with dissolve
    x "(Another five minutes pass. My arm is now in absolute agony.)"
    show madd boy anguished at left_small
    with dissolve
    x "(The pain radiates from my shoulder down to my fingertips.)"
    show madd boy suffering at left_small
    with dissolve
    x "(Sweat begins to bead on my forehead from the effort.)"
    show madd boy exhausted at left_small
    with dissolve
    x "(I can feel every fiber of my arm burning, protesting, wanting to collapse.)"
    show madd boy torture at left_small
    with dissolve
    x "(The phone trembles again, just barely.)"
    show madd boy horrified at left_small
    with dissolve
    show aman furious at right_small
    with dissolve
    aman_says "Are you kidding me right now?!"
    show aman contemptuous at right_small
    with dissolve
    show madd boy terrified at left_small
    with dissolve
    aman_says "Hold. It. Still."
    show aman menacing at right_small
    with dissolve
    show madd boy trembling at left_small
    with dissolve
    x "(He's so angry... it's my fault... I'm making him miss the match...)"
    show madd boy guilty at left_small
    with dissolve
    x "(I grit my teeth and force my arm to stillness, even as every nerve ending screams.)"
    show madd boy enduring at left_small
    with dissolve
    x "(I become a statue. A human phone stand. That's all I am to him.)"
    show madd boy numb at left_small
    with dissolve
    # SCENE 3: Release and collapse
    scene scene_interact_aman_mess_hall_met_level_1_event_1_madd_holding_phone_return_phone
    with dissolve
    x "(More minutes tick by. My arm feels like it might snap.)"
    show madd boy broken at left_small
    with dissolve
    x "(The pain is so intense it's almost numb now, replaced by a dull, pervasive ache.)"
    show madd boy defeated at left_small
    with dissolve
    aman_says "Finally... they won. Great play."
    show aman satisfied at right_small
    with dissolve
    show madd boy barely conscious at left_small
    with dissolve
    aman_says "You can put the phone down now."
    show aman dismissive at right_small
    with dissolve
    show madd boy collapsing at left_small
    with dissolve
    x "(I lower my arm slowly, my entire limb shaking uncontrollably.)"
    show madd boy devastated at left_small
    with dissolve
    x "(Twenty minutes... I stood there for twenty minutes...)"
    show madd boy traumatized at left_small
    with dissolve
    x "(My arm hangs at my side, useless, throbbing with residual pain.)"
    show madd boy broken at left_small
    with dissolve
    x "(And to him, it was nothing. Just a convenience. Just another way to use me.)"
    show madd boy defeated at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 2
    $ madd_dominance -= 2
    $ game_time.advance_time(minutes=25)
    return
#images done
label interact_aman_mess_hall_met_level_1_event_2:
    """interact_aman_mess_hall_met Level 1 Event 2 - Silver spoon cleaning"""
    scene scene_messhall_breakfast
    with fade
    
    show aman eating at right_small
    with dissolve
    x "(I'm sitting across from Aman in the mess hall while he eats his meal.)"
    show madd boy watching at left_small
    with dissolve
    x "(He has his own custom silver spoon and fork—not the communal plastic utensils like everyone else.)"
    show madd boy observant at left_small
    with dissolve
    aman_says "Communal plastic is for losers. I bring my own silver."
    show aman arrogant at right_small
    with dissolve
    show madd boy unimpressed at left_small
    with dissolve
    x "(Of course he does...)"
    show madd boy resigned at left_small
    with dissolve
    # SCENE 1: Spoon covered in saliva
    scene scene_interact_aman_mess_hall_met_level_1_event_2_aman_eating_soup
    with dissolve
    x "(He dips his spoon into a thick, creamy soup.)"
    show madd boy aware at left_small
    with dissolve
    x "(As he eats, the soup clings to the silver, coating every surface.)"
    show madd boy uncomfortable at left_small
    with dissolve
    x "(I watch as he brings the spoon to his mouth, the metal disappearing between his lips.)"
    show madd boy nervous at left_small
    with dissolve
    x "(When he pulls it back out, it's completely covered in his saliva and leftover food particles.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(He repeats this over and over—spoon in his mouth, spoon out, glistening wet with his spit.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(The fork is no better, coated with cream and his saliva after he uses it to push food into his mouth.)"
    show madd boy appalled at left_small
    with dissolve
    aman_says "Finish your meal quickly."
    show aman commanding at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "(Why is he asking me to finish my meal quickly. Does he have any plans for me? He finishes his soup and sets the utensils down on the table.)"
    show madd boy uncertain at left_small
    with dissolve
    x "(The spoon and fork are now thoroughly covered in his saliva and the remnants of his meal.)"
    show madd boy dreading at left_small
    with dissolve
    show aman holding at right_small
    with dissolve
    aman_says "These are silver. You don't put silver in a dishwasher. You hand-clean it."
    show aman commanding at right_small
    with dissolve
    show madd boy horrified at left_small
    with dissolve
    x "(No... no, he's not...)"
    show madd boy mortified at left_small
    with dissolve
    x "(He holds out the wet, saliva-covered utensils directly toward me.)"
    show madd boy appalled at left_small
    with dissolve
    x "(He watches my face carefully, studying my reaction.)"
    show madd boy panicked at left_small
    with dissolve
    aman_says "Take them. You wouldn't want me to ruin my expensive silver in a dishwasher, would you?"
    show aman cold at right_small
    with dissolve
    show madd boy reluctant at left_small
    with dissolve
    x "(I reach out slowly and take the utensils into my bare hands.)"
    show madd boy trembling at left_small
    with dissolve
    # SCENE 2: Unwashed utensils transferred
    scene scene_interact_aman_mess_hall_met_level_1_event_2_aman_transfer_spoon
    with dissolve
    x "(The moment my skin touches them, I feel his drying saliva coating the metal.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(Oh god... oh god, his spit is on my hands...)"
    show madd boy nauseated at left_small
    with dissolve
    x "(The warmth of the utensils, still hot from his mouth, transfers to my palms.)"
    show madd boy horrified at left_small
    with dissolve
    x "(I can feel the sticky residue of his saliva coating my fingers and the inside of my hand.)"
    show madd boy gagging at left_small
    with dissolve
    x "(The sensation is sickening—intimate and violating all at once.)"
    show madd boy traumatized at left_small
    with dissolve
    aman_says "Pre-wipe them with your fingers. Get the food off."
    show aman commanding at right_small
    with dissolve
    show madd boy devastated at left_small
    with dissolve
    x "(He wants me to... to use my bare fingers...)"
    show madd boy humiliated at left_small
    with dissolve
    x "(I begin rubbing my fingers along the surface of the spoon and fork, wiping away the dried food particles.)"
    show madd boy submissive at left_small
    with dissolve
    x "(Every stroke of my finger across the metal spreads his saliva around.)"
    show madd boy broken at left_small
    with dissolve
    x "(I can taste it in the air—the faint taste of whatever he ate, mixed with the metallic taste of saliva.)"
    show madd boy numb at left_small
    with dissolve
    x "(My stomach churns as I work.)"
    show madd boy sickened at left_small
    with dissolve
    x "(The wet residue coats my fingers, and I can feel it drying slightly against my skin.)"
    show madd boy degraded at left_small
    with dissolve
    # SCENE 3: Forced cleaning ritual
    scene scene_interact_aman_mess_hall_met_level_1_event_2_madd_cleaning_utensils
    with dissolve
    x "(This is his saliva... his spit is all over my hands...)"
    show madd boy ashamed at left_small
    with dissolve
    show aman smirking at right_small
    with dissolve
    x "(He leans back and smirks, watching my face closely as I work.)"
    show madd boy disturbed at left_small
    with dissolve
    aman_says "Don't look so offended. My spit is probably the most expensive thing you've touched all day."
    show aman cruel smile at right_small
    with dissolve
    show madd boy devastated at left_small
    with dissolve
    x "(He's... he's taunting me while I clean his utensils with his spit on my hands...)"
    show madd boy broken at left_small
    with dissolve
    x "(The words hit harder than any physical blow could.)"
    show madd boy defeated at left_small
    with dissolve
    x "(He's right. I'm so poor that his spit is more valuable than anything I own.)"
    show madd boy self loathing at left_small
    with dissolve
    x "(I finish wiping the utensils, my hands now thoroughly coated in his dried saliva.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(The taste lingers in my mouth even though I haven't eaten anything.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(What did I do to deserve this? What crime did I commit?)"
    show madd boy anguished at left_small
    with dissolve
    x "(I stand there, holding his clean silver in my contaminated hands, feeling utterly violated and worthless.)"
    show madd boy devastated at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 2
    $ character_relations["aman"]["lust"] += 1
    $ character_relations["aman"]["identity"] += 1
    $ madd_dominance -= 2
    $ madd_secret_identity -= 1
    $ game_time.advance_time(minutes=15)
    return
#images done
label interact_aman_mess_hall_met_level_2_event_1:
    """interact_aman_mess_hall_met Level 2 Event 1 - Pre-licked plate"""
    scene scene_messhall_breakfast
    with fade
    
    show aman eating at right_small
    with dissolve
    x "(Aman finishes his steak, and the plate is covered in peppercorn sauce and grease.)"
    show madd boy attentive at left_small
    with dissolve
    x "(I wait to collect his plate, as is my job.)"
    show madd boy patient at left_small
    with dissolve
    show aman looking at right_small
    with dissolve
    # SCENE 1: Aman licks plate clean
    scene scene_interact_aman_mess_hall_met_level_2_event_1_aman_licks_plate
    with dissolve
    aman_says "I hate wasteful servants."
    show aman cold at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "(Wasteful? I'm just doing my job...)"
    show madd boy uncertain at left_small
    with dissolve
    show aman picking up at right_small
    with dissolve
    x "(Before I can reach for the plate, he picks it up himself.)"
    show madd boy startled at left_small
    with dissolve
    show aman licking at right_small
    with dissolve
    aman_says "This is perfectly good food."
    show aman casual at right_small
    with dissolve
    show madd boy horrified at left_small
    with dissolve
    x "(He brings the plate to his mouth and deliberately licks the surface clean.)"
    show madd boy shocked at left_small
    with dissolve
    show aman setting down at right_small
    with dissolve
    # SCENE 2: Rice served on saliva-coated plate
    scene scene_interact_aman_mess_hall_met_level_2_event_1_rice_on_saliva_plate
    with dissolve
    aman_says "Chef! Serve her rice. On this plate."
    show aman commanding at right_small
    with dissolve
    show madd boy panicked at left_small
    with dissolve
    x "(No... no, he's not...)"
    show madd boy horrified at left_small
    with dissolve
    x "(The chef looks uncomfortable but obeys, pouring rice onto the still-glossy, saliva-covered plate.)"
    show madd boy devastated at left_small
    with dissolve
    x "(The white rice lands on the wet surface, and I can see the patches where his spit isn't covered.)"
    show madd boy appalled at left_small
    with dissolve
    x "(There are glossy, translucent areas gleaming between the grains of rice.)"
    show madd boy sickened at left_small
    with dissolve
    show aman watching at right_small
    with dissolve
    aman_says "Eat."
    show aman cold at right_small
    with dissolve
    show madd boy trembling at left_small
    with dissolve
    x "(His cold, demanding stare pins me in place.)"
    show madd boy frozen at left_small
    with dissolve
    x "(I can't... I can't eat this...)"
    show madd boy desperate at left_small
    with dissolve
    x "(But I know I have no choice.)"
    show madd boy resigned at left_small
    with dissolve
    x "(I pick up the fork with shaking hands.)"
    show madd boy trembling at left_small
    with dissolve
    x "(Every nerve in my body is screaming at me not to do this.)"
    show madd boy horrified at left_small
    with dissolve
    x "(I scoop up some rice—rice that's touching his spit.)"
    show madd boy numb at left_small
    with dissolve
    x "(This is wrong... this is so wrong...)"
    show madd boy protesting at left_small
    with dissolve
    # SCENE 3: Forced consumption of contaminated meal
    scene scene_interact_aman_mess_hall_met_level_2_event_1_rice_on_saliva_plate_eating
    with dissolve
    x "(I bring the fork to my lips, and my stomach churns violently.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(I can already taste it—the metallic tang of his saliva mixed with the starchy blandness of rice.)"
    show madd boy gagging at left_small
    with dissolve
    x "(I close my eyes and put the rice in my mouth.)"
    show madd boy ashamed at left_small
    with dissolve
    x "(The moment I bite down, I taste him.)"
    show madd boy horrified at left_small
    with dissolve
    x "(His spit is salty and bitter, coating my tongue.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(I'm eating his spit... I'm putting his saliva in my body...)"
    show madd boy broken at left_small
    with dissolve
    x "(The rice itself tastes metallic—contaminated by him.)"
    show madd boy devastated at left_small
    with dissolve
    x "(I swallow hard, forcing the food down my throat despite the urge to gag.)"
    show madd boy self loathing at left_small
    with dissolve
    x "(The bitterness lingers on my tongue, in my throat, all the way down.)"
    show madd boy humiliated at left_small
    with dissolve
    show aman laughing at right_small
    with dissolve
    aman_says "Ha! Look at your face!"
    show aman cruel laughter at right_small
    with dissolve
    show madd boy defeated at left_small
    with dissolve
    aman_says "See? Now we're sharing. Isn't that what 'friends' do?"
    show aman mocking at right_small
    with dissolve
    show madd boy broken at left_small
    with dissolve
    x "(Friends? This isn't friendship... this is...)"
    show madd boy anguished at left_small
    with dissolve
    x "(I don't even know what to call this anymore.)"
    show madd boy numb at left_small
    with dissolve
    x "(I take another bite of the contaminated rice, mechanically chewing and swallowing.)"
    show madd boy robotic at left_small
    with dissolve
    x "(I've eaten worse. I'll eat worse. This is my life now.)"
    show madd boy defeated at left_small
    with dissolve
    x "(The taste of his saliva becomes familiar as I eat, bite after bite.)"
    show madd boy dissociating at left_small
    with dissolve
    x "(Each swallow is an act of degradation, and yet I continue.)"
    show madd boy traumatized at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 4
    $ character_relations["aman"]["lust"] += 2
    $ character_relations["aman"]["identity"] += 1
    $ madd_dominance -= 3
    $ madd_secret_identity -= 1
    $ game_time.advance_time(minutes=20)
    return
#images done
label interact_aman_mess_hall_met_level_2_event_2:
    """interact_aman_mess_hall_met Level 2 Event 2 - Sauce "upgrade" """
    scene scene_messhall_breakfast
    with fade
    
    show aman eating at right_small
    with dissolve
    x "(I'm sitting next to Aman as he eats ribs with his hands.)"
    show madd boy waiting at left_small
    with dissolve
    x "(His fingers are dripping with thick, red BBQ sauce—sticky and greasy.)"
    show madd boy observant at left_small
    with dissolve
    show aman finishing at right_small
    with dissolve
    x "(He finishes eating and looks over at me, noticing my clean, modest outfit.)"
    show madd boy aware at left_small
    with dissolve
    aman_says "Your clothes look so plain. Let me help."
    show aman casual at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "(What? Help with what?)"
    show madd boy uncertain at left_small
    with dissolve
    show aman reaching at right_small
    with dissolve
    # SCENE 1: Aman's greasy fingers reaching
    scene scene_interact_aman_mess_hall_met_level_2_event_2_aman_sauce_lick
    with dissolve
    x "(He doesn't reach for a napkin.)"
    show madd boy nervous at left_small
    with dissolve
    x "(Instead, he grabs my sleeve and the front of my chest area.)"
    show madd boy shocked at left_small
    with dissolve
    show aman wiping at right_small
    with dissolve
    x "(He vigorously wipes his sticky, greasy fingers onto my uniform.)"
    show madd boy appalled at left_small
    with dissolve
    x "(The thick BBQ sauce smears across the clean fabric, staining it red.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(He's... he's using me as a napkin...)"
    show madd boy gagging at left_small
    with dissolve
    x "(The grease seeps into the material, creating dark, wet patches.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(I can feel the sticky residue coating my skin underneath.)"
    show madd boy traumatized at left_small
    with dissolve
    # SCENE 2: Sauce smeared on face
    scene scene_interact_aman_mess_hall_met_level_2_event_2_aman_sauce_smear_madd_shirt
    with dissolve
    show aman continuing at right_small
    with dissolve
    x "(He does another pass, this time reaching higher, toward my face.)"
    show madd boy panicked at left_small
    with dissolve
    x "(His greasy fingers find my cheeks.)"
    show madd boy horrified at left_small
    with dissolve
    x "(He wipes the thick BBQ sauce across my face, smearing it from one cheek to the other.)"
    show madd boy gagging at left_small
    with dissolve
    x "(No... not my face...)"
    show madd boy revulsed at left_small
    with dissolve
    x "(The sauce is warm and sticky, cloying on my skin.)"
    show madd boy sickened at left_small
    with dissolve
    x "(It gets near my mouth, and I can taste it—sweet, spicy, and mixed with the lingering taste of his meal.)"
    show madd boy nauseated at left_small
    with dissolve
    # SCENE 3: Lingering touch and humiliation
    scene scene_interact_aman_mess_hall_met_level_2_event_2_aman_sauce_smear_madd_face
    with dissolve
    x "(Some of it gets into my mouth, and I gag involuntarily.)"
    show madd boy gagging at left_small
    with dissolve
    aman_says "Now your clothes are less filthy. They've been touched by someone with a seven-figure bank account."
    show aman smirking at right_small
    with dissolve
    show madd boy devastated at left_small
    with dissolve
    x "(He's claiming this is a gift? This degradation is a privilege?)"
    show madd boy broken at left_small
    with dissolve
    show aman lingering at right_small
    with dissolve
    x "(As he speaks, he doesn't pull his hand away immediately.)"
    show madd boy uncomfortable at left_small
    with dissolve
    x "(His greasy fingers linger on my shoulder and cheek.)"
    show madd boy flustered at left_small
    with dissolve
    aman_says "(They're so soft... so feminine...)"
    show aman tempted at right_small
    with dissolve
    show madd boy nervous at left_small
    with dissolve
    x "(He seems to be appreciating the feeling of my skin beneath his touch.)"
    show madd boy disturbed at left_small
    with dissolve
    x "(He's... he's enjoying this... enjoying humiliating me...)"
    show madd boy horrified at left_small
    with dissolve
    x "(His touch lingers, his greasy fingers tracing along my cheekbone.)"
    show madd boy violated at left_small
    with dissolve
    x "(The sensation is revolting—his filthy hands on my clean skin, the thick sauce coating my face.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(I want to scream... I want to run... but I can't move.)"
    show madd boy paralyzed at left_small
    with dissolve
    show aman pulling away at right_small
    with dissolve
    x "(He finally pulls his hand away, leaving grease smeared across my cheek.)"
    show madd boy devastated at left_small
    with dissolve
    aman_says "Much better. You should thank me."
    show aman dismissive at right_small
    with dissolve
    show madd boy broken at left_small
    with dissolve
    x "(Thank him? For violating me? For using me as a napkin?)"
    show madd boy humiliated at left_small
    with dissolve
    x "(I say nothing, unable to find words.)"
    show madd boy silent at left_small
    with dissolve
    x "(I just sit here, covered in his BBQ sauce—a visible mark of his degradation.)"
    show madd boy defeated at left_small
    with dissolve
    x "(The sauce is drying on my face, pulling at my skin.)"
    show madd boy uncomfortable at left_small
    with dissolve
    x "(The smell of it is strong and sweet, clinging to my nostrils.)"
    show madd boy numb at left_small
    with dissolve
    x "(This is who I am now. The girl covered in his filth. The girl he uses.)"
    show madd boy devastated at left_small
    with dissolve
    x "(I can still feel the lingering sensation of his fingers on my skin, the violation marking me.)"
    show madd boy broken at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 4
    $ character_relations["aman"]["lust"] += 3
    $ character_relations["aman"]["identity"] += 1
    $ madd_dominance -= 3
    $ madd_secret_identity -= 1
    $ game_time.advance_time(minutes=15)
    return
#images done
label interact_aman_mess_hall_met_level_3_event_1:
    """interact_aman_mess_hall_met Level 3 Event 1 - Bone pit disposal"""
    scene scene_messhall_breakfast
    with fade
    
    show madd boy eating at left_small
    with dissolve
    x "(I'm sitting with my simple bowl of rice, trying to eat quietly.)"
    show madd boy peaceful at left_small
    with dissolve
    show aman eating at right_small
    with dissolve
    x "(Aman is at his table nearby, eating bone-in chicken—expensive, pristine white meat.)"
    show madd boy aware at left_small
    with dissolve
    x "(He finishes with the first piece and extracts the bone from his mouth.)"
    show madd boy watching at left_small
    with dissolve
    show aman turning at right_small
    with dissolve
    x "(He doesn't look for a discard bowl.)"
    show madd boy confused at left_small
    with dissolve
    x "(Instead, he turns toward me.)"
    show madd boy startled at left_small
    with dissolve
    show aman spitting at right_small
    with dissolve
    aman_says "There's no room on my plate."
    show aman casual at right_small
    with dissolve
    show madd boy shocked at left_small
    with dissolve
    # SCENE 1: Bones accumulating
    scene scene_interact_aman_mess_hall_met_level_3_event_1_aman_spits_bones
    with dissolve
    x "(He spits the chewed, jagged bone directly into my rice bowl.)"
    show madd boy horrified at left_small
    with dissolve
    x "(The \"clink\" of bone hitting my plate echoes through the quiet mess hall.)"
    show madd boy appalled at left_small
    with dissolve
    x "(No... no, he didn't...)"
    show madd boy gagging at left_small
    with dissolve
    x "(The bone lands with a wet sound, surrounded by a halo of his warm saliva.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(I stare at the intrusion in my rice.)"
    show madd boy frozen at left_small
    with dissolve
    x "(This is my food... my meal... and he just...)"
    show madd boy disgusted at left_small
    with dissolve
    aman_says "(Use your plate to store them. You're my personal disposal unit.)"
    show aman commanding at right_small
    with dissolve
    show madd boy devastated at left_small
    with dissolve
    x "(Disposal unit... I'm not even a person to him...)"
    show madd boy humiliated at left_small
    with dissolve
    x "(He finishes another piece and I watch in horror as he turns toward me again.)"
    show madd boy terrified at left_small
    with dissolve
    show aman spitting again at right_small
    with dissolve
    x "(Another bone flies from his mouth into my bowl.)"
    show madd boy shocked at left_small
    with dissolve
    x "(\"Clink.\")"
    show madd boy violated at left_small
    with dissolve
    x "(And another.)"
    show madd boy numb at left_small
    with dissolve
    x "(\"Clink.\")"
    show madd boy broken at left_small
    with dissolve
    x "(Over and over, he spits his chewed bones into my rice.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(This is happening... this is really happening...)"
    show madd boy anguished at left_small
    with dissolve
    x "(Each bone lands with a wet, sickening sound.)"
    show madd boy gagging at left_small
    with dissolve
    x "(Each one is covered in his warm, glistening saliva.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(I try to push the bones to the side of my plate, stacking them together.)"
    show madd boy working at left_small
    with dissolve
    x "(I'll just eat around them... I have to... I have no choice...)"
    show madd boy resigned at left_small
    with dissolve
    x "(But as the bones pile up, something worse happens.)"
    show madd boy horrified at left_small
    with dissolve
    x "(His saliva begins to pool at the end of the plate where I've gathered the bones.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(The yellow-white liquid collects in a small, sickening puddle.)"
    show madd boy gagging at left_small
    with dissolve
    x "(Oh god... oh god, it's pooling... his spit is pooling on my plate...)"
    show madd boy traumatized at left_small
    with dissolve
    x "(And then, impossibly, it begins to seep back into my rice.)"
    show madd boy horrified at left_small
    with dissolve
    scene scene_interact_aman_mess_hall_met_level_3_event_1_aman_spits_bones_seeping_rice
    with dissolve
    x "(The saliva trickles across the plate, mixing with the grain, turning it into a filthy slurry.)"
    show madd boy revolted at left_small
    with dissolve
    x "(The rice swirls with his spit, becoming wet and glossy.)"
    show madd boy gagging at left_small
    with dissolve
    x "(I can't... I can't eat this... but I have to...)"
    show madd boy desperate at left_small
    with dissolve
    show aman watching at right_small
    with dissolve
    x "(He watches me, waiting to see what I'll do.)"
    show madd boy nervous at left_small
    with dissolve
    x "(His presence is suffocating, oppressive.)"
    show madd boy paralyzed at left_small
    with dissolve
    # SCENE 2: Forced consumption begins
    scene scene_interact_aman_mess_hall_met_level_3_event_1_aman_spits_bones_seeping_rice_madd_eats
    with dissolve
    x "(I know he expects me to continue eating.)"
    show madd boy resigned at left_small
    with dissolve
    x "(I know refusing is not an option.)"
    show madd boy defeated at left_small
    with dissolve
    x "(I pick up my spoon with trembling hands.)"
    show madd boy trembling at left_small
    with dissolve
    x "(I scoop up some rice—rice that's soaked in his saliva.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(This is his spit... I'm eating his spit... I'm eating his spit mixed with my food...)"
    show madd boy horrified at left_small
    with dissolve
    x "(I bring the spoon to my mouth.)"
    show madd boy hesitant at left_small
    with dissolve
    x "(The taste hits me immediately—a thick, coating saltiness that makes my entire body convulse.)"
    show madd boy gagging at left_small
    with dissolve
    x "(It's not just rice anymore. It's him. It tastes like him.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(I force myself to swallow, my throat fighting every inch of the way.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(I'm swallowing his spit... voluntarily... while he watches...)"
    show madd boy broken at left_small
    with dissolve
    x "(I continue eating, bite after bite.)"
    show madd boy mechanical at left_small
    with dissolve
    x "(Each spoonful is tainted, contaminated, flavored with his disgrace.)"
    show madd boy dissociating at left_small
    with dissolve
    x "(The saliva continues to seep into my rice, creating a viscous mixture.)"
    show madd boy numb at left_small
    with dissolve
    x "(I can see the liquid pooling around the bones—his waste, his filth, now part of my meal.)"
    show madd boy devastated at left_small
    with dissolve
    x "(What am I doing... what have I become...)"
    show madd boy anguished at left_small
    with dissolve
    # SCENE 3: Complete degradation
    scene scene_interact_aman_mess_hall_met_level_3_event_1_aman_spits_bones_seeping_rice_madd_eats_eating_complete
    with dissolve
    x "(I eat every grain of rice on my plate, every spoonful tainted with his saliva.)"
    show madd boy defeated at left_small
    with dissolve
    x "(This is my life... eating his spit mixed with my food... while he watches...)"
    show madd boy broken at left_small
    with dissolve
    x "(When my plate is finally empty, I set down the spoon.)"
    show madd boy hollow at left_small
    with dissolve
    x "(The bones remain, stacked in a pile—monuments to my degradation.)"
    show madd boy devastated at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 5
    $ character_relations["aman"]["lust"] += 2
    $ character_relations["aman"]["identity"] += 2
    $ madd_dominance -= 5
    $ madd_secret_identity -= 2
    $ game_time.advance_time(minutes=25)
    return

label interact_aman_mess_hall_met_level_3_event_2:
    """interact_aman_mess_hall_met Level 3 Event 2 - Silver inheritance"""
    scene scene_messhall_breakfast
    with fade
    
    show aman finishing at right_small
    with dissolve
    x "(Aman finishes a rich dessert, using his silver spoon and fork.)"
    show madd boy about to eat at left_small
    with dissolve
    x "(I'm about to pick up my own utensils to start my meal.)"
    show madd boy ready at left_small
    with dissolve
    # SCENE 1: Unwashed silver offered
    scene scene_interact_aman_mess_hall_met_level_1_event_2_aman_transfer_spoon
    with dissolve
    show aman sliding at right_small
    with dissolve
    aman_says "Stop."
    show aman commanding at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    x "(He slides his used, unwashed silver set toward me across the table.)"
    show madd boy shocked at left_small
    with dissolve
    x "(The spoon and fork glisten—wet with saliva and the remnants of his dessert.)"
    show madd boy horrified at left_small
    with dissolve
    aman_says "Use these. I'm tired of seeing you use that peasant plastic."
    show aman dismissive at right_small
    with dissolve
    show madd boy trembling at left_small
    with dissolve
    x "(No... no, I have to wash them... I can't eat with them like that...)"
    show madd boy panicked at left_small
    with dissolve
    x "(I stand up to walk to the kitchen sink.)"
    show madd boy desperate at left_small
    with dissolve
    show aman snapping at right_small
    with dissolve
    aman_says "No! Sit down. Eat with them as they are."
    show aman furious at right_small
    with dissolve
    show madd boy shocked at left_small
    with dissolve
    aman_says "If you wash them, you're insulting my 'flavor.'"
    show aman cold at right_small
    with dissolve
    show madd boy devastated at left_small
    with dissolve
    x "(He's... he's serious... he really wants me to eat with his unwashed utensils...)"
    show madd boy humiliated at left_small
    with dissolve
    x "(I feel tears welling up in my eyes—pure embarrassment, pure shame.)"
    show madd boy weeping at left_small
    with dissolve
    x "(This is... this is so degrading...)"
    show madd boy anguished at left_small
    with dissolve
    x "(I sit back down slowly, my hands shaking.)"
    show madd boy trembling at left_small
    with dissolve
    # SCENE 2: Forced consumption with saliva-coated utensil
    scene scene_interact_aman_mess_hall_met_level_3_event_2_aman_transfer_spoon_madd_eating
    with dissolve
    x "(I pick up the spoon.)"
    show madd boy hesitant at left_small
    with dissolve
    x "(The moment my lips touch it, I feel the warmth of his mouth still lingering on the silver.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(His warmth... on my lips... from his mouth...)"
    show madd boy gagging at left_small
    with dissolve
    x "(I can taste him immediately.)"
    show madd boy horrified at left_small
    with dissolve
    x "(The flavor of whatever he ate mixes with the unmistakable taste of his saliva.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(It's a salty, slightly sweet taste that coats my tongue.)"
    show madd boy revolted at left_small
    with dissolve
    x "(I force myself to eat, bringing a spoonful of my food to my mouth using his saliva-covered spoon.)"
    show madd boy breaking at left_small
    with dissolve
    x "(Every bite tastes like him.)"
    show madd boy numb at left_small
    with dissolve
    x "(The flavor of my food is masked, overridden by the constant reminder of him.)"
    show madd boy defeated at left_small
    with dissolve
    x "(Everything I eat tastes like his spit... I can't escape it...)"
    show madd boy desperate at left_small
    with dissolve
    x "(The texture of his saliva lingers on the silver—the coating never fully disappears.)"
    show madd boy gagging at left_small
    with dissolve
    x "(Each time I put the spoon in my mouth, I feel that sticky sensation.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(This is what he thinks of me... I'm so far beneath him that his discarded utensils are too good for me...)"
    show madd boy humiliated at left_small
    with dissolve
    x "(But they're still better than my \"peasant plastic.\")"
    show madd boy broken at left_small
    with dissolve
    x "(I eat slowly, mechanically, every bite a reminder of my lower status.)"
    show madd boy dissociating at left_small
    with dissolve
    x "(The warmth of his mouth on the silver never fully disappears.)"
    show madd boy numb at left_small
    with dissolve
    x "(It feels almost intimate—as if I'm consuming him.)"
    show madd boy disturbed at left_small
    with dissolve
    x "(The thought makes my stomach turn.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(I finish my meal, each spoonful a violation of my dignity.)"
    show madd boy defeated at left_small
    with dissolve
    # SCENE 3: Permanent possession of shame
    scene scene_interact_aman_mess_hall_met_level_3_event_2_aman_transfer_spoon_madd_eating_complete
    with dissolve
    x "(When I'm done, I try to hand the utensils back to him.)"
    show madd boy offering at left_small
    with dissolve
    show aman waving at right_small
    with dissolve
    aman_says "Keep them. I'm not going to use a tool used by a poor person."
    show aman dismissive at right_small
    with dissolve
    show madd boy shattered at left_small
    with dissolve
    x "(Keep them? He's... he's making me keep them...)"
    show madd boy devastated at left_small
    with dissolve
    x "(I'm left holding the silver utensils—symbols of his wealth, symbols of my inferiority.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(I hold them in my trembling hands, and the weight of them feels immense.)"
    show madd boy broken at left_small
    with dissolve
    x "(These are my inheritance. Not wealth. Not kindness. Just... reminders that I'm nothing to him.)"
    show madd boy anguished at left_small
    with dissolve
    x "(The taste of his saliva still lingers in my mouth.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(It will linger for the rest of the day... a permanent mark of my shame...)"
    show madd boy devastated at left_small
    with dissolve
    $ character_relations["aman"]["dominance"] += 5
    $ character_relations["aman"]["lust"] += 3
    $ character_relations["aman"]["identity"] += 2
    $ madd_dominance -= 5
    $ madd_secret_identity -= 2
    $ game_time.advance_time(minutes=20)
    return


# ============================================
# WATER_BOTTLE_WITNESS_AMAN
# ============================================

label water_bottle_witness_aman:
    """Aman witnesses water bottle cap drop - randomly chooses between scenarios based on relationship stats"""
    # Check if Aman has very high dominance and lust (Level 3 - most aggressive)
    if character_relations["aman"]["identity"] > 10 and character_relations["aman"]["lust"] > 20:
        $ event_type = renpy.random.randint(1, 10)
        if event_type <= 5:
            call water_bottle_witness_aman_level3_event_1 from _call_water_bottle_witness_aman_level3_event_1
        else:
            call water_bottle_witness_aman_level3_event_2 from _call_water_bottle_witness_aman_level3_event_2
    # Check if Aman has high dominance and lust (Level 2 - more aggressive)
    elif character_relations["aman"]["identity"] > 5 and character_relations["aman"]["lust"] > 20:
        $ rand_chance = renpy.random.randint(1, 100)
        if rand_chance <= 20:
            # Level 1 events
            $ event_type = renpy.random.randint(1, 2)
            if event_type == 1:
                call water_bottle_witness_aman_level1_event_1 from _call_water_bottle_witness_aman_level1_event_1
            else:
                call water_bottle_witness_aman_level1_event_2 from _call_water_bottle_witness_aman_level1_event_2
        else:
            $ event_type = renpy.random.randint(1, 10)
            if event_type <= 5:
                call water_bottle_witness_aman_level2_event_1 from _call_water_bottle_witness_aman_level2_event_1
            else:
                call water_bottle_witness_aman_level2_event_2 from _call_water_bottle_witness_aman_level2_event_2
    else:
        # Level 1 events
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call water_bottle_witness_aman_level1_event_1 from _call_water_bottle_witness_aman_level1_event_1_1
        else:
            call water_bottle_witness_aman_level1_event_2 from _call_water_bottle_witness_aman_level1_event_2_1
    return
#images done
label water_bottle_witness_aman_level1_event_1:
    """Level 1 Event 1 - The Confused Gaze"""
    scene scene_hostel_hallway
    with fade
    
    show madd boy bending at left_small
    with dissolve
    x "(I'm bending down to pick up my water bottle cap, focused on retrieving it from the floor.)"
    show madd boy concentrated at left_small
    with dissolve
    x "(My hand is inches away from the cap when I feel something change in the air.)"
    show madd boy aware at left_small
    with dissolve
    x "(There's a presence... someone watching me.)"
    show madd boy startled at left_small
    with dissolve
    x "(Every muscle in my body tenses instantly.)"
    show madd boy nervous at left_small
    with dissolve
    x "(A chill runs down my spine—that unmistakable sensation of being observed intensely.)"
    show madd boy uncomfortable at left_small
    with dissolve
    x "(I don't turn around. I can't. My heart is racing so hard I think it might break through my ribs.)"
    show madd boy frightened at left_small
    with dissolve
    x "(Who is it? Why are they staring at me like that?)"
    show madd boy frozen at left_small
    with dissolve
    show aman rounding at right_small
    with dissolve
    # SCENE 1: Aman's attraction moment
    scene   scene_aman_water_bottle_witness_level_1_event_1_aman_sees_madd_bent_over
    with dissolve
    x "(Aman rounds the corner, and his eyes immediately lock onto my figure.)"
    show aman admiring at right_small
    with dissolve
    x "(For just a moment, his 'gamer' brain shuts off completely.)"
    show madd boy trembling at left_small
    with dissolve
    x "(I can feel his gaze burning into me... studying me... appreciating me...)"
    show madd boy blushing at left_small
    with dissolve
    x "(It's not the gaze of contempt I'm used to. It's something else entirely.)"
    show madd boy confused at left_small
    with dissolve
    x "(It feels like... attraction. Pure, unguarded attraction.)"
    show madd boy flustered at left_small
    with dissolve
    x "(My breathing becomes shallow. The warmth in my cheeks intensifies.)"
    show madd boy embarrassed at left_small
    with dissolve
    x "(Does he... does he find me attractive? For just a second, I feel seen. Valued. Desirable.)"
    show madd boy hopeful at left_small
    with dissolve
    x "(Maybe he isn't just looking at me as something beneath him...)"
    show aman conflicted at right_small
    with dissolve
    x "(But then something shifts.)"
    show madd boy confused at left_small
    with dissolve
    x "(I can sense it—a change in his energy. Like he's suddenly snapping out of something.)"
    show aman disgusted at right_small
    with dissolve
    aman_says "You look so scrawny. Pathetic, really."
    show aman cold at right_small
    with dissolve
    show madd boy shocked at left_small
    with dissolve
    x "(His voice is harsh, dripping with disdain.)"
    show madd boy hurt at left_small
    with dissolve
    x "(The warmth I felt a moment ago turns ice cold.)"
    show madd boy devastated at left_small
    with dissolve
    aman_says "And weak. Poor people are always so weak."
    show aman mocking at right_small
    with dissolve
    # SCENE 2: Post-insult humiliation
    scene scene_aman_water_bottle_witness_level_1_event_1_aman_sees_madd_bent_over_after_insult
    with dissolve
    show madd boy broken at left_small
    with dissolve
    x "(He's looking at his phone now, deliberately avoiding my gaze.)"
    show madd boy confused at left_small
    with dissolve
    x "(What just happened? For a moment, he was looking at me differently... and now...)"
    show madd boy ashamed at left_small
    with dissolve
    x "(Did I imagine that? Was I seeing things?)"
    show madd boy humiliated at left_small
    with dissolve
    x "(Or is he running from something? Running from that moment of genuine attraction?)"
    show madd boy uncertain at left_small
    with dissolve
    x "(The emotional whiplash is dizzying.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(One second I felt valued. The next, I'm nothing but an object of his contempt.)"
    show madd boy defeated at left_small
    with dissolve
    x "(I straighten up slowly, cap in hand, and walk away.)"
    show madd boy numb at left_small
    with dissolve
    x "(But that moment will stay with me.)"
    show madd boy haunted at left_small
    with dissolve
    x "(That brief second where he looked at me like I was beautiful... before he remembered to hate me.)"
    show madd boy broken at left_small
    with dissolve
    
    $ character_relations["aman"]["identity"] += 1
    $ madd_dominance -= 1
    $ game_time.advance_time(minutes=3)
    return
#images done
label water_bottle_witness_aman_level1_event_2:
    """Level 1 Event 2 - The Canine Fetch"""
    scene scene_hostel_hallway
    with fade
    
    show madd boy reaching at left_small
    with dissolve
    x "(I'm reaching down for my water bottle cap, my fingers stretched toward it on the floor.)"
    show madd boy focused at left_small
    with dissolve
    x "(I'm completely focused on the task—just a simple reach, a simple retrieval.)"
    show madd boy unaware at left_small
    with dissolve
    show aman approaching at right_small
    with dissolve
    # SCENE 1: Kick impact and collapse
    scene scene_aman_water_bottle_witness_level_1_event_2_aman_kick_madd_and_cap
    with dissolve
    x "(Without warning, I feel a sharp impact against the back of my knees.)"
    show madd boy shocked at left_small
    with dissolve
    x "(A foot—his foot—strikes me with deliberate force.)"
    show madd boy crying out at left_small
    with dissolve
    x "Ah!"
    x "(My legs buckle instantly, unable to support my weight.)"
    show madd boy falling at left_small
    with dissolve
    x "(I collapse to the hard floor, my hands catching me partially as I hit the tiles.)"
    show madd boy writhing at left_small
    with dissolve
    x "(The impact sends a bolt of pain through my knees—sharp, stinging pain.)"
    show madd boy aching at left_small
    with dissolve
    x "(But the physical pain is nothing compared to the shame that floods through me.)"
    show madd boy ashamed at left_small
    with dissolve
    x "(I'm on the ground. On my hands and knees, literally.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(Before I can even process what's happening, I see my cap skittering across the hallway.)"
    show madd boy shocked at left_small
    with dissolve
    x "(He kicked it... he deliberately kicked it away from me...)"
    show madd boy devastated at left_small
    with dissolve
    x "(It slides twenty feet down the hall, coming to rest against the wall—impossibly far away.)"
    show madd boy desperate at left_small
    with dissolve
    show aman looming at right_small
    with dissolve
    aman_says "Don't get up."
    show aman commanding at right_small
    with dissolve
    show madd boy trembling at left_small
    with dissolve
    x "(His voice is ice.)"
    show madd boy frightened at left_small
    with dissolve
    x "(His shadow looms over me, pinning me in place more effectively than any physical restraint.)"
    show madd boy paralyzed at left_small
    with dissolve
    aman_says "You're already halfway there."
    show aman cruel at right_small
    with dissolve
    show madd boy confused at left_small
    with dissolve
    aman_says "Be a good dog and fetch it on your knees."
    show aman commanding at right_small
    with dissolve
    show madd boy horrified at left_small
    with dissolve
    x "(Did he just... did he just call me a DOG?)"
    show madd boy broken at left_small
    with dissolve
    x "(On my knees? He wants me to crawl... like an animal...)"
    show madd boy humiliated at left_small
    with dissolve
    x "(The sting in my knees is now joined by the heat of absolute degradation.)"
    show madd boy ashamed at left_small
    with dissolve
    x "(My dignity is slipping away with each passing second.)"
    show madd boy defeated at left_small
    with dissolve
    aman_says "If you're fast enough, I'll give you maybe a treat."
    show aman mocking at right_small
    with dissolve
    show madd boy numb at left_small
    with dissolve
    x "(A treat. Like a dog.)"
    show madd boy anguished at left_small
    with dissolve
    x "(I want to stand up. I want to walk away with my head held high.)"
    show madd boy conflicted at left_small
    with dissolve
    x "(But I can't. I'm frozen by his presence, by his power over me.)"
    show madd boy powerless at left_small
    with dissolve
    # SCENE 2: Mid-crawl degradation
    scene scene_aman_water_bottle_witness_level_1_event_2_madd_crawl_to_cap
    with dissolve
    x "(Slowly, painfully, I begin to crawl.)"
    show madd boy crawling at left_small
    with dissolve
    x "(My knees scrape against the cold tile floor.)"
    show madd boy wincing at left_small
    with dissolve
    x "(The pain is sharp, immediate, shooting through my kneecaps with each movement.)"
    show madd boy suffering at left_small
    with dissolve
    x "(I'm moving forward on my hands and knees, my body positioned exactly like an animal being commanded to fetch.)"
    show madd boy degraded at left_small
    with dissolve
    x "(Behind me, I can feel his eyes on my back. Watching. Enjoying.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(Each meter of hallway feels like a thousand.)"
    show madd boy exhausted at left_small
    with dissolve
    x "(The pain in my knees is building, becoming a dull throb mixed with sharp spikes.)"
    show madd boy aching at left_small
    with dissolve
    x "(But worse than the pain is the knowledge that people might see me like this.)"
    show madd boy panicked at left_small
    with dissolve
    x "(Crawling. Being treated like a dog. For his amusement.)"
    show madd boy broken at left_small
    with dissolve
    x "(I keep moving forward, forcing myself onward despite the screaming in my knees.)"
    show madd boy enduring at left_small
    with dissolve
    x "(I have to do this. I have to comply. That's what I am now.)"
    show madd boy numb at left_small
    with dissolve
    x "(Finally, I reach the cap.)"
    show madd boy reaching at left_small
    with dissolve
    # SCENE 3: Cap reached and retrieved
    scene scene_aman_water_bottle_witness_level_1_event_2_madd_crawl_to_cap_pickup_cap
    with dissolve
    x "(My hands are trembling as I pick it up.)"
    show madd boy devastated at left_small
    with dissolve
    show aman laughing at right_small
    with dissolve
    aman_says "Ha! Perfect form!"
    show aman cruel laughter at right_small
    with dissolve
    show madd boy shattered at left_small
    with dissolve
    x "(He's laughing at me. Genuinely enjoying my humiliation.)"
    show madd boy broken at left_small
    with dissolve
    x "(I push myself to my feet slowly, my knees screaming in protest.)"
    show madd boy standing at left_small
    with dissolve
    x "(My legs are shaking, barely supporting my weight.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(I look at the cap in my hand—now a symbol of my complete and total submission to him.)"
    show madd boy defeated at left_small
    with dissolve
    x "(This is what I've become. A dog. His plaything.)"
    show madd boy hollow at left_small
    with dissolve
    x "(The ache in my knees will remind me of this moment for days.)"
    show madd boy haunted at left_small
    with dissolve
    x "(Every time I kneel, every time I bend, I'll remember this.)"
    show madd boy broken at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 3
    $ character_relations["aman"]["identity"] += 1
    $ madd_dominance -= 3
    $ madd_secret_identity -= 1
    $ game_time.advance_time(minutes=5)
    return
#images done
label water_bottle_witness_aman_level2_event_1:
    """Level 2 Event 1 - The Saliva Sanitizer"""
    scene scene_hostel_hallway
    with fade
    
    show madd boy reaching at left_small
    with dissolve
    x "(I drop my water bottle cap near the water cooler, the plastic clattering softly against the tile.)"
    show madd boy bending at left_small
    with dissolve
    x "(I bend down to pick it up, my hand already reaching for the cap.)"
    show madd boy focused at left_small
    with dissolve
    show aman appearing at right_small
    with dissolve
    x "(Suddenly, his shadow falls over me, blocking the light.)"
    show madd boy startled at left_small
    with dissolve
    aman_says "Wait."
    show aman commanding at right_small
    with dissolve
    show madd boy frozen at left_small
    with dissolve
    x "(His voice stops me cold.)"
    show madd boy confused at left_small
    with dissolve
    aman_says "The floor is disgusting. It's covered in germs."
    show aman concerned at right_small
    with dissolve
    show madd boy uncertain at left_small
    with dissolve
    aman_says "Let me help you sanitize that."
    show aman casual at right_small
    with dissolve
    show madd boy hopeful at left_small
    with dissolve
    x "(Sanitize? Is he... is he actually going to help me?)"
    show madd boy waiting at left_small
    with dissolve
    x "(For a moment, I feel a flutter of something like gratitude.)"
    show madd boy naive at left_small
    with dissolve
    show aman preparing at right_small
    with dissolve
    # SCENE 1: Spit delivery
    scene scene_aman_water_bottle_witness_level_2_event_1_aman_spits_on_cap
    with dissolve
    x "(He opens his mouth and begins swishing something inside it vigorously.)"
    show madd boy confused at left_small
    with dissolve
    x "(What is he doing...?)"
    show madd boy suspicious at left_small
    with dissolve
    x "(The sound is wet, aggressive, deliberately exaggerated.)"
    show madd boy uneasy at left_small
    with dissolve
    show aman spitting at right_small
    with dissolve
    scene scene_aman_plate_lick_contact
    with dissolve
    x "(Before I can even process what's happening, he leans over and spits.)"
    show madd boy horrified at left_small
    with dissolve
    x "(A thick, bubbly glob of saliva shoots from his mouth and lands directly on my cap.)"
    show madd boy shocked at left_small
    with dissolve
    x "(The spit is warm, viscous, glistening in the light.)"
    show madd boy gagging at left_small
    with dissolve
    x "(It pools on the plastic surface, slowly beginning to dribble down the sides.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(My stomach turns violently.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(Did he just... did he really just spit on my cap?)"
    show madd boy devastated at left_small
    with dissolve
    x "(This is my water bottle. I drink from this every day.)"
    show madd boy trembling at left_small
    with dissolve
    show aman smirking at right_small
    with dissolve
    aman_says "There. My spit is cleaner than that floor."
    show aman mocking at right_small
    with dissolve
    show madd boy broken at left_small
    with dissolve
    x "(He's serious. He actually believes his spit is an improvement.)"
    show madd boy humiliated at left_small
    with dissolve
    aman_says "Put it back on. Don't let a drop go to waste."
    show aman commanding at right_small
    with dissolve
    show madd boy paralyzed at left_small
    with dissolve
    x "(Don't let a drop... go to waste...)"
    show madd boy anguished at left_small
    with dissolve
    x "(He wants me to use it. With his spit on it.)"
    show madd boy conflicted at left_small
    with dissolve
    x "(But I can't afford to waste it. I can't afford a new bottle. I need this to stay hydrated at work.)"
    show madd boy resigned at left_small
    with dissolve
    x "(The cold calculation is brutal: his spit or my thirst.)"
    show madd boy defeated at left_small
    with dissolve
    x "(There's no choice. Not really.)"
    show madd boy numb at left_small
    with dissolve
    x "(I reach down and pick up the cap with trembling fingers.)"
    show madd boy trembling at left_small
    with dissolve
    x "(The moment my skin touches it, I feel the slick, viscous texture of his saliva.)"
    show madd boy gagging at left_small
    with dissolve
    x "(It's thick and lukewarm, coating my fingertips.)"
    show madd boy horrified at left_small
    with dissolve
    x "(The sensation is revolting—intimate in the worst possible way.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(I can feel the individual droplets sliding across my skin.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(This is his saliva. His spit. It's on my hands now.)"
    show madd boy broken at left_small
    with dissolve
    x "(I bring the cap to the bottle, my hand shaking so badly I can barely grip it.)"
    show madd boy struggling at left_small
    with dissolve
    # SCENE 2: Cap sealed with spit inside
    scene scene_aman_water_bottle_witness_level_2_event_1_aman_spits_on_cap_seal_cap
    with dissolve
    x "(The spit-covered cap twists onto the bottle with a soft click.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(It's done. It's sealed now. His essence is locked inside my water bottle.)"
    show madd boy devastated at left_small
    with dissolve
    show aman watching at right_small
    with dissolve
    x "(He watches me with that grin, clearly enjoying every second of my discomfort.)"
    show madd boy ashamed at left_small
    with dissolve
    x "(I know what's coming now. Every time I drink from this bottle, I'll taste him.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(Every sip will be a reminder that I'm not even allowed to have clean water.)"
    show madd boy broken at left_small
    with dissolve
    x "(I hold the bottle in my hands, and my entire body shudders with disgust.)"
    show madd boy defeated at left_small
    with dissolve
    x "(This bottle is mine now. His saliva is part of my day. Part of me.)"
    show madd boy hollow at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 2
    $ character_relations["aman"]["lust"] += 1
    $ character_relations["aman"]["identity"] += 1
    $ madd_dominance -= 2
    $ madd_secret_identity -= 1
    $ game_time.advance_time(minutes=5)
    return
#images done
label water_bottle_witness_aman_level2_event_2:
    """Level 2 Event 2 - The Sweat Squeeze"""
    scene scene_hostel_hallway
    with fade
    
    show madd boy bending at left_small
    with dissolve
    x "(I'm bent over, reaching for something near the water cooler.)"
    show madd boy focused at left_small
    with dissolve
    x "(My back is exposed, my head down, completely vulnerable.)"
    show madd boy unaware at left_small
    with dissolve
    show aman toweled at right_small
    with dissolve
    x "(Aman appears, draped in a towel, his body glowing with heat from a recent workout.)"
    show madd boy startled at left_small
    with dissolve
    x "(I can see the sweat darkening the fabric—it's completely saturated.)"
    show madd boy nervous at left_small
    with dissolve
    show aman stretching at right_small
    with dissolve
    x "(He stops in front of me and stretches his arms wide, the towel spreading out like a banner.)"
    show madd boy confused at left_small
    with dissolve
    x "(What is he doing...?)"
    show madd boy wary at left_small
    with dissolve
    # SCENE 1: Towel wringing
    scene scene_aman_water_bottle_witness_level_2_event_2_aman_prepare_towel
    with dissolve
    show aman gripping at right_small
    with dissolve
    x "(He grips the towel tight with both hands.)"
    show madd boy alarmed at left_small
    with dissolve
    x "(Oh god... oh god, no...)"
    show madd boy panicked at left_small
    with dissolve
    show aman wringing at right_small
    with dissolve
    x "(He begins wringing it out—forcefully, deliberately, directly over my head.)"
    show madd boy horrified at left_small
    with dissolve
    x "(A stream of hot, salty sweat begins to pour down.)"
    show madd boy shocked at left_small
    with dissolve
    x "No! Stop!"
    x "(The warm liquid hits my hair first, cascading down my scalp in a torrent.)"
    show madd boy gasping at left_small
    with dissolve
    x "(It soaks into my hair, matting it against my head.)"
    show madd boy gagging at left_small
    with dissolve
    x "(The warmth is shocking—I wasn't expecting that sensation.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(It runs down the back of my neck, dripping inside my collar, soaking into my clothes.)"
    show madd boy trembling at left_small
    with dissolve
    x "(A few drops trickle down my face, and some get into my mouth.)"
    show madd boy gagging at left_small
    with dissolve
    x "(The taste hits me instantly—pungent, salty, undeniably him.)"
    show madd boy horrified at left_small
    with dissolve
    x "(It's not water. It's not clean. It's his sweat—the salt, the body odor, everything he's been secreting.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(My tongue tingles with the saltiness of it.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(This is inside my mouth now. I can taste him. I'm consuming him.)"
    show madd boy traumatized at left_small
    with dissolve
    show aman laughing at right_small
    with dissolve
    aman_says "Ha! Perfect!"
    show aman satisfied at right_small
    with dissolve
    show madd boy broken at left_small
    with dissolve
    x "(The sweat continues to stream down my back, soaking through my clothes.)"
    show madd boy shaking at left_small
    with dissolve
    x "(The fabric clings to my skin, and I feel marked by him.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(This is his filth... his essence... and it's all over me.)"
    show madd boy violated at left_small
    with dissolve
    show aman grinning at right_small
    with dissolve
    aman_says "Consider that a premium moisturizing treatment."
    show aman mocking at right_small
    with dissolve
    show madd boy defeated at left_small
    with dissolve
    aman_says "You usually have to pay for that kind of 'man-scent.'"
    show aman cruel laughter at right_small
    with dissolve
    show madd boy shivering at left_small
    with dissolve
    x "(The sweat is now beginning to dry on my skin, leaving behind salt residue.)"
    show madd boy uncomfortable at left_small
    with dissolve
    x "(It stings—my eyes are watering from the salt.)"
    show madd boy gagging at left_small
    with dissolve
    x "(I feel it in my eyes, burning, making me squint and tear up.)"
    show madd boy crying at left_small
    with dissolve
    x "(But I can't move. I can't wipe my face. I can't do anything but endure.)"
    show madd boy paralyzed at left_small
    with dissolve
    x "(The salt continues to burn, and the taste of him lingers in my mouth.)"
    show madd boy numb at left_small
    with dissolve
    x "(I'm frozen in this submissive position—bent over, soaked in his sweat, unable to protest.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(This is what I am to him. A towel. A receptacle for his filth.)"
    show madd boy broken at left_small
    with dissolve
    x "(The drying sweat is making my skin tight and itchy.)"
    show madd boy uncomfortable at left_small
    with dissolve
    # SCENE 2: Drying sweat aftermath
    scene scene_aman_water_bottle_witness_level_2_event_2_aman_sweat_aftermath
    with dissolve
    x "(I can smell it now—the distinct smell of male sweat, animal and primal.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(It's in my hair. On my clothes. In my mouth. On my skin.)"
    show madd boy devastated at left_small
    with dissolve
    x "(Everyone will see me like this. Everyone will know what happened to me.)"
    show madd boy ashamed at left_small
    with dissolve
    x "(I'm marked. Branded with his sweat.)"
    show madd boy broken at left_small
    with dissolve
    x "(This feeling will stay with me long after I wash—the memory of being used as a disposal unit for his body's waste.)"
    show madd boy hollow at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 3
    $ character_relations["aman"]["lust"] += 2
    $ character_relations["aman"]["identity"] += 1
    $ madd_dominance -= 2
    $ madd_secret_identity -= 1
    $ game_time.advance_time(minutes=5)
    return
#images done
label water_bottle_witness_aman_level3_event_1:
    """Level 3 Event 1 - The Spank and Spray"""
    scene scene_hostel_hallway
    with fade
    
    show madd boy bending at left_small
    with dissolve
    x "(I'm bent over at the water cooler, reaching for my bottle.)"
    scene scene_aman_water_bottle_witness_level_1_event_1_aman_sees_madd_bent_over
    with dissolve
    show madd boy focused at left_small
    with dissolve
    x "(My back is exposed, my rear end prominently positioned as I lean forward.)"
    show madd boy unaware at left_small
    with dissolve
    x "(I'm completely focused on my task, not paying attention to my surroundings.)"
    show madd boy peaceful at left_small
    with dissolve
    show aman approaching at right_small
    with dissolve
    # SCENE 1: Spank impact
    scene scene_aman_water_bottle_witness_level_3_event_1_aman_spank_madd
    with dissolve
    x "(Without warning, there's a sharp, stinging sensation across my buttocks.)"
    show madd boy shocked at left_small
    with dissolve
    x "(His hand connects with my ass in a hard, deliberate spank.)"
    show madd boy startled at left_small
    with dissolve
    x "(The shock sends a jolt through my entire body.)"
    show madd boy trembling at left_small
    with dissolve
    x "(Before I can think, before I can stop myself, a sound escapes from deep in my throat.)"
    show madd boy gasping at left_small
    with dissolve
    x "Ahhhh!"
    x "(A loud, high-pitched, unmistakably feminine moan.)"
    scene scene_aman_water_bottle_witness_level_1_event_1_aman_sees_madd_bent_over_after_insult
    with dissolve
    show madd boy horrified at left_small
    with dissolve
    x "(The moment the sound leaves my lips, I realize what I've done.)"
    show madd boy panicked at left_small
    with dissolve
    x "(That sound... it wasn't masculine at all. It was soft, vulnerable, feminine.)"
    show madd boy terrified at left_small
    with dissolve
    x "(Oh god... oh god, what if he noticed...?)"
    show madd boy spinning at left_small
    with dissolve
    x "(I spin around to face him, my face flushed with heat—part shame, part terror.)"
    show madd boy panicked at left_small
    with dissolve
    x "(My eyes widen, searching his face for recognition, for judgment, for proof that he's figured out the truth about me.)"
    show madd boy fearful at left_small
    with dissolve
    x "(Is he going to expose me? Is he going to...?)"
    show aman ready at right_small
    with dissolve
    x "(But he's already prepared.)"
    show madd boy shocked at left_small
    with dissolve
    x "(He takes a mouthful of water from the cooler.)"
    show aman swishing at right_small
    with dissolve
    x "(I watch as he begins swishing the water aggressively inside his mouth.)"
    show madd boy confused at left_small
    with dissolve
    x "(What is he...?)"
    show madd boy horrified at left_small
    with dissolve
    show aman spitting at right_small
    with dissolve
    # SCENE 2: Spit spray assault
    scene scene_aman_water_bottle_witness_level_3_event_1_aman_spit_water
    with dissolve
    x "(The moment I turn to face him fully, he spits.)"
    show madd boy blinded at left_small
    with dissolve
    x "Gah!"
    x "(A spray of water—mixed with his saliva—shoots directly from his mouth and hits my face with force.)"
    show madd boy coughing at left_small
    with dissolve
    x "(The water hits me hard enough to make me stumble backward.)"
    show madd boy gagging at left_small
    with dissolve
    x "(I can't see. My eyes are flooded with the liquid.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(Some of it gets into my mouth—I can taste it before I can even close my lips.)"
    show madd boy disgusted at left_small
    with dissolve
    x "(It's not just water.)"
    show madd boy horrified at left_small
    with dissolve
    x "(The taste is thick, intense, unmistakable. His saliva mixed with the water.)"
    show madd boy gagging at left_small
    with dissolve
    x "(He spit directly into my face—not from a bottle, but from his own mouth.)"
    show madd boy trembling at left_small
    with dissolve
    x "(I'm literally drinking his spit, involuntarily, forced to swallow his contempt directly from his mouth.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(The water drips down my face, but the taste remains on my tongue—his mouth's essence.)"
    show madd boy devastated at left_small
    with dissolve
    x "(I feel a deep, burning humiliation settling into my bones.)"
    show madd boy broken at left_small
    with dissolve
    x "(I was caught off guard, vulnerable, and now I'm literally consuming his disrespect—directly from his mouth.)"
    show aman stepping at right_small
    with dissolve
    aman_says "What was that sound?"
    show aman mocking at right_small
    with dissolve
    show madd boy panicked at left_small
    with dissolve
    x "(He steps into my space, his presence overwhelming.)"
    show madd boy frightened at left_small
    with dissolve
    aman_says "Sounded a bit... girly."
    show aman cruel smile at right_small
    with dissolve
    show madd boy terrified at left_small
    with dissolve
    x "(My heart stops. He knows. He's taunting me because he knows.)"
    show madd boy desperate at left_small
    with dissolve
    x "(Or does he? Is he just guessing?)"
    show madd boy confused at left_small
    with dissolve
    aman_says "I had to wash that sound out of your mouth."
    show aman smirking at right_small
    with dissolve
    show madd boy broken at left_small
    with dissolve
    x "(He's re-establishing the boundary. The 'bro' boundary.)"
    show madd boy ashamed at left_small
    with dissolve
    x "(He's reminding both of us that there was a moment of vulnerability, of something almost tender when he spanked me.)"
    show madd boy humiliated at left_small
    with dissolve
    x "(That moment of contact, that spark—he's aggressively erasing it by drowning me in his spit-water.)"
    show madd boy defeated at left_small
    with dissolve
    x "(The taste lingers on my tongue—his saliva mixed with water, a physical reminder of the boundary he's reasserting.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(I can still taste him. Even as he walks away, I can still taste his disrespect in my mouth.)"
    show madd boy numb at left_small
    with dissolve
    x "(That sound I made... it's burned into both of our memories now.)"
    show madd boy broken at left_small
    with dissolve
    x "(And the only way he knows to respond to it is by forcing me to drink his contempt.)"
    show madd boy hollow at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 4
    $ character_relations["aman"]["lust"] += 2
    $ character_relations["aman"]["identity"] += 2
    $ madd_dominance -= 3
    $ madd_secret_identity -= 2
    $ game_time.advance_time(minutes=5)
    return
#images done
label water_bottle_witness_aman_level3_event_2:
    """Level 3 Event 2 - The Human Chair"""
    scene scene_hostel_hallway
    with fade
    
    show madd boy standing at left_small
    with dissolve
    x "(I'm in the hallway near the water cooler, standing idly.)"
    show madd boy unaware at left_small
    with dissolve
    show aman exhausted at right_small
    with dissolve
    x "(Aman returns from what looks like a marathon workout session.)"
    show madd boy observant at left_small
    with dissolve
    x "(He's drenched in sweat, his clothes dark and clinging to his body.)"
    show madd boy uncomfortable at left_small
    with dissolve
    x "(The smell hits me even from a distance—heavy, pungent, unmistakably male.)"
    show madd boy nervous at left_small
    with dissolve
    x "(He looks exhausted, moving slowly, clearly desperate for relief.)"
    show madd boy wary at left_small
    with dissolve
    show aman noticing at right_small
    with dissolve
    x "(His eyes lock onto me.)"
    show madd boy startled at left_small
    with dissolve
    x "(I see the wheels turning in his mind.)"
    show madd boy frightened at left_small
    with dissolve
    show aman kicking at right_small
    with dissolve
    # SCENE 1: Kicked down
    scene scene_aman_water_bottle_witness_level_1_event_2_aman_kick_madd_and_cap
    with dissolve
    x "(Without a word, he kicks at my knees from behind.)"
    show madd boy shocked at left_small
    with dissolve
    x "(The sudden impact buckles my legs instantly.)"
    show madd boy falling at left_small
    with dissolve
    x "(I collapse to the floor onto all fours before I can even process what's happening.)"
    show madd boy gasping at left_small
    with dissolve
    x "Wh-What...?"
    x "(My hands are on the cold tile, my back is exposed, my rear end raised.)"
    show madd boy frightened at left_small
    with dissolve
    x "(I'm in the most vulnerable position imaginable.)"
    show madd boy panicked at left_small
    with dissolve
    show aman drinking at right_small
    with dissolve
    x "(He casually takes a sip of water from his bottle, as if he hasn't just forced me to the ground.)"
    show madd boy confused at left_small
    with dissolve
    x "(What is he doing...?)"
    show madd boy terrified at left_small
    with dissolve
    show aman sitting at right_small
    with dissolve
    # SCENE 2: Weight crushing down
    scene scene_aman_water_bottle_witness_level_3_event_2_aman_sits_on_madd
    with dissolve
    x "(Before I can say anything, before I can protest, he sits.)"
    show madd boy shocked at left_small
    with dissolve
    x "(He sits heavily on my back—his full body weight pressing down on me.)"
    show madd boy compressed at left_small
    with dissolve
    x "Oof!"
    x "(The air is forced from my lungs.)"
    show madd boy gasping at left_small
    with dissolve
    x "(The weight is crushing, immobilizing. I can barely breathe.)"
    show madd boy struggling at left_small
    with dissolve
    x "(My arms tremble with effort as they support both my weight and his.)"
    show madd boy aching at left_small
    with dissolve
    x "(He shifts his position, and I feel something press directly against the back of my neck and shoulders.)"
    show madd boy horrified at left_small
    with dissolve
    x "(His groin... his genitals... they're pressing against me through his thin shorts.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(The contact is unmistakable, intimate in the most violating way possible.)"
    show madd boy gagging at left_small
    with dissolve
    x "(I can feel the sweat-soaked fabric of his shorts against my skin.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(But it's not just the physical contact.)"
    show madd boy overwhelmed at left_small
    with dissolve
    x "(The smell is worse—infinitely worse.)"
    show madd boy choking at left_small
    with dissolve
    x "(The pungent scent of his sweat combined with the musk of his lower body, inches from my nose.)"
    show madd boy gagging at left_small
    with dissolve
    x "(It's suffocatingly intimate and absolutely foul.)"
    show madd boy desperate at left_small
    with dissolve
    x "(The smell is so overwhelming I can barely breathe.)"
    show madd boy suffocating at left_small
    with dissolve
    x "(Every breath I take is filled with him—his exertion, his body, his filth.)"
    show madd boy broken at left_small
    with dissolve
    x "Please... please get off me..."
    show madd boy begging at left_small
    with dissolve
    x "(My voice is muffled, small, pathetic.)"
    show madd boy ashamed at left_small
    with dissolve
    x "(Even as I beg, I'm drowning in shame at my own powerlessness.)"
    show madd boy humiliated at left_small
    with dissolve
    show aman ignoring at right_small
    with dissolve
    x "(He doesn't respond. He doesn't even acknowledge my pleas.)"
    show madd boy devastated at left_small
    with dissolve
    x "(Instead, I hear the sound of him unlocking his phone.)"
    show madd boy numb at left_small
    with dissolve
    aman_says "Stay still. My legs are killing me."
    show aman casual at right_small
    with dissolve
    show madd boy paralyzed at left_small
    with dissolve
    x "(He's completely relaxed, completely unbothered by my situation.)"
    show madd boy broken at left_small
    with dissolve
    x "(I'm not even a person to him. I'm furniture.)"
    show madd boy defeated at left_small
    with dissolve
    aman_says "At least your scrawny back is good for something."
    show aman dismissive at right_small
    with dissolve
    show madd boy shattered at left_small
    with dissolve
    x "(Even my pain, even my sacrifice, is an insult.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(My body is trembling under his weight, my arms screaming in agony.)"
    show madd boy suffering at left_small
    with dissolve
    x "(The smell continues to assault my senses—I can't escape it.)"
    show madd boy nauseated at left_small
    with dissolve
    x "(I'm trapped beneath him, forced to endure this, unable to move, unable to protest.)"
    show madd boy numb at left_small
    with dissolve
    x "(Minutes pass. Or are they seconds? Time feels distorted.)"
    show madd boy anguished at left_small
    with dissolve
    x "(My arms are shaking so badly I'm afraid I'll collapse and crush myself beneath him.)"
    show madd boy desperate at left_small
    with dissolve
    x "(I'm sobbing silently, my entire body wracked with tremors.)"
    show madd boy broken at left_small
    with dissolve
    # SCENE 3: Release - standing again
    scene scene_aman_water_bottle_witness_level_3_event_2_aman_gets_up_from_madd
    with dissolve
    show aman standing at right_small
    with dissolve
    x "(Finally, mercifully, he stands.)"
    show madd boy collapsing at left_small
    with dissolve
    x "(The moment his weight lifts, I collapse onto the floor completely.)"
    show madd boy gasping at left_small
    with dissolve
    x "(I'm breathing heavily, my entire body shaking uncontrollably.)"
    show madd boy trembling at left_small
    with dissolve
    show aman laughing at right_small
    with dissolve
    aman_says "Thanks for the chair."
    show aman walking away at right_small
    with dissolve
    show madd boy devastated at left_small
    with dissolve
    x "(He laughs—genuinely laughs—and walks away as if nothing happened.)"
    show madd boy shattered at left_small
    with dissolve
    x "(I'm left on the floor, unable to move, the scent of him still clinging to my neck, my shoulders, my skin.)"
    show madd boy broken at left_small
    with dissolve
    x "(It's like a brand. His sweat-soaked scent is a physical marking of my degradation.)"
    show madd boy traumatized at left_small
    with dissolve
    x "(I can still smell him. Even as I lie here, gasping for breath, I'm breathing in his musk.)"
    show madd boy numb at left_small
    with dissolve
    x "(This scent will linger on my skin, in my hair, on my clothes.)"
    show madd boy defeated at left_small
    with dissolve
    x "(Everyone who passes will know what happened to me.)"
    show madd boy hollow at left_small
    with dissolve
    x "(I am a piece of furniture. That is what I am to him.)"
    show madd boy broken at left_small
    with dissolve
    
    $ character_relations["aman"]["dominance"] += 5
    $ character_relations["aman"]["lust"] += 3
    $ character_relations["aman"]["identity"] += 2
    $ madd_dominance -= 4
    $ madd_secret_identity -= 2
    $ game_time.advance_time(minutes=10)
    return
