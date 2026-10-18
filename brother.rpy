label outside_step_brother_room_scene:
    # During morning and afternoon, door is slightly open and you peek to see him sleeping
    if game_time.is_morning() or game_time.is_afternoon():
        scene scene_madd_knock_home_morning_afternoon
        with fade
        show madd think at left_small
        with dissolve
        x "I notice the door is slightly open..."
        show madd curious at left_small
        with dissolve
        x "Let me peek through..."
        
        scene scene_brother_morning_afternoon_room_sleeping
        with fade
        show madd shocked at left_small
        with dissolve
        x "I can see my brother sleeping in his room. He looks peaceful when he's asleep..."
        
        if access_to_brother_room:
            show madd think at left_small
            x "( He said I could use his room and computer during the morning when he's sleeping. )"
            menu:
                "Enter the room quietly":
                    jump step_brother_room_scene_brother_sleeping
                "Leave and come back later":
                    jump home_areas
        else:
            show madd uncertain at left_small
            x "I should probably come back later when he's awake."
            
            jump home_areas
    
    # Evening and night, knock and he tells you to come in
    python:
        if game_time.is_evening():
            knock_scene = "scene_madd_knock_home_evening"
        else:
            knock_scene = "scene_madd_knock_home_night"
    scene expression knock_scene
    with fade
    show madd think at left_small
    with dissolve
    x "I am outside my Step Brother's Room. Should I knock?"
    menu:
        "Knock on the door":
            show brother creepy at right_small
            brother_says "Come in!"
            jump step_brother_room_scene
        "Go back to lobby":
            jump home_areas

label step_brother_room_scene:
    # Choose scene based on time of day
    python:
        if game_time.is_morning() or game_time.is_afternoon():
            brother_room_scene = "scene_brother_room_morning_afternoon"
        elif game_time.is_evening():
            brother_room_scene = "scene_brother_room_evening"
        else:  # night
            brother_room_scene = "scene_brother_room_night"
    
    scene expression brother_room_scene
    with fade
    
    # Reset daily counter if it's a new day
    if game_time.hour < last_brother_talk_hour and last_brother_talk_hour != -1:
        $ brother_talk_today = False
    
    "I am in my Step Brother's Room. It feels unwelcoming."
    
    menu:
        "Ask to sleep in his room" if (("madd_home_room" in locked_home_areas or madd_room_got_unlocked) and not access_to_brother_room) or (brother_protects_madd_from_dad>0):
            jump ask_brother_to_sleep_in_room
        
        "Sleep in his room" if access_to_brother_room and (game_time.is_night() or game_time.is_evening()):
            jump sleep_in_brother_room
        
        "Run away from home" if access_to_brother_room:
            if madd_willpower<80:
                show madd distressed at left_small
                x "I'm too exhausted to run away right now. I need to rest first."
                jump step_brother_room_scene
            if not main_door_key_found and "home_main_door" in locked_home_areas:
                show madd distressed at left_small
                x "The main door is locked and I don't know where the key to the main door is..."
                jump step_brother_room_scene
            if (research_cram_schools >= 3 and madd_money>=2800):
                jump runaway_from_brother_room
            else:
                show madd think at left_small
                x "I don't have enough money or haven't researched enough to run away yet."
                jump step_brother_room_scene
        
        "Talk to him" if not brother_talk_today:
            if madd_willpower<20:
                show madd distressed at left_small
                x "I'm too exhausted to talk to him right now. I need to rest first."
                call advance_time_and_check(minutes=10) from _call_advance_time_and_check
                jump step_brother_room_scene

            $ brother_talk_today = True
            jump talk_to_brother
        
        "Talk to him" if brother_talk_today:
            scene scene_brother_room
            with fade
            show brother creepy at right_small
            with fade
            show madd stressed at left_small
            x "I dont want to talk to him for the day. Maybe after i've slept "
            call advance_time_and_check(minutes=10) from _call_advance_time_and_check_1
            jump step_brother_room_scene
        
        "Listen to his demands" if research_cram_schools < 3 and demands_brother < 2:
            scene scene_brother_room
            with fade
            show brother creepy at right_small
            with fade
            x "I dont wanna listen to this creep."
            call advance_time_and_check(minutes=10) from _call_advance_time_and_check_2
            jump step_brother_room_scene
        
        "Listen to his demands" if research_cram_schools >= 3 and demands_brother < 2:
            scene scene_brother_room
            with fade
            show brother at right_small
            with fade
            x "I need to talk to him to know his demands."
            call advance_time_and_check(minutes=10) from _call_advance_time_and_check_3
            jump step_brother_room_scene
        
        "Listen to his demands" if research_cram_schools < 3 and demands_brother >= 2:
            scene scene_brother_room
            with fade
            show brother creepy at right_small
            with fade
            x "I have no reason to give in to his demands."
            call advance_time_and_check(minutes=10) from _call_advance_time_and_check_4
            jump step_brother_room_scene
        
        "Listen to his demands" if research_cram_schools >= 3 and demands_brother >= 2:
            if madd_willpower<20:
                show madd distressed at left_small
                x "I'm too exhausted to listen to his demands right now. I need to rest first."
                call advance_time_and_check(minutes=10) from _call_advance_time_and_check_5
                jump step_brother_room_scene
            jump brother_listen_to_demands
        
        "Go back to lobby":
            call advance_time_and_check(minutes=5) from _call_advance_time_and_check_6
            jump home_areas


#TALK TO BROTHER SCENES 


label talk_to_brother:
    scene scene_brother_room_brother_playing_on_pc
    with fade
    $ renpy.call_in_new_context("_hide_windows")
    show brother at right_small
    with dissolve
    brother_says "Not now, I'm in the middle of a game."
    
    show madd worried at left_small
    x "It will only take a moment. I really need to talk to you about something important."
    
    show brother dismissive at right_small
    brother_says "I said not now! Can't you see I'm busy? This is my room!"
    
    show madd sad at left_small
    x "I know, but... I really need some way to earn money. It's important."
    
    show brother calculating at right_small
    brother_says "What the fuck is so important ??"
    
    x "(The sudden intensity of his reaction catches me off guard.)"
    x " Brother please ?"
    
    show brother calculating at right_small
    brother_says "Money, huh? What do you even need money for you stay at home all the time."
    
    show madd hopeful at left_small
    x " I need it to buy a playstation to play Resident Evil."
    
    show brother obsessed at right_small
    brother_says "What !? I didnt know you were a gamer."
    brother_says "Alright, fine lets discuss while playing Street Fighter..."
    
    if renpy.random.random() < 0.5:
        jump talk_to_brother_level_1_event_1
    else:
        jump talk_to_brother_level_1_event_2


label talk_to_brother_level_1_event_1:
    scene scene_brother_room_brother_playing_on_pc
    with fade
    $ renpy.call_in_new_context("_hide_windows")
    show brother obsessed at right_small
    with dissolve
    show madd curious at left_small
    with fade
    x "( Brother points his controller at me )"


    scene scene_brother_room_sitting_in_room_gaming_on_pc_to_edge_of_bed
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd hesitant at left_small
    x "( Then he moved from the gaming chair to the edge  of the bed)"
    show brother predatory at right_small
    with dissolve
    brother_says "You were a gamer right... Show me what you got"
    show madd nervous at left_small
    x "(He was pointing his controller at me with his other hand patting the area between his legs... )"
    x "(He wanted me to sit between his legs on the bed... This is inappropriate... but I need the money... )"
    x "Alright..."
    show madd conflicted at left_small
    x "( I approach him slowly and sat between his legs )"
    show madd flustered at left_small
    x "( The proximity feels suffocating, but I try to act natural )"
    x "( I can feel his gaze on me, tracking my every movement )"
    # Scene: Initial vulnerability - sitting on bed with brother preparing to manipulate her


    scene scene_brother_event1_gaming_control
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd nervous at left_small
    x "( As I start playing, he moves closer to me , his legs clamping around mine to keep me in place )"
    show madd shocked at left_small
    x "( This doesn't feel right, but the money... I need the money )"
    show madd trembling at left_small
    x " (He brings his arms under mine as i hold the controller )"
    show madd stressed at left_small
    x "( My heart begins racing uncontrollably )"

    show madd flustered at left_small
    x "( his hands holding the controller with mine )"
    show madd horrified at left_small
    x "( Oh God... what is happening? )"
    show madd uncertain at left_small
    brother_says "Relax, just let me guide your hands."
    show madd blush at left_small
    x "(i can feel his body pressed against mine... )"
    show madd flustered at left_small
    x "( his arm is brushing against my chest... )"
    show madd paralyzed at left_small
    x "( That's... that's not accidental )"
    show madd conflicted at left_small
    brother_says "You're doing great... just like that."
    show brother leering at right_small
    x "( He leans in closer, his breath on my shoulder )"
    show madd horrified at left_small
    x "( This is beyond uncomfortable now )"
    show madd deep blush at left_small
    x "(i can feel his breath on my neck... )"
    show madd stressed at left_small
    x "( I want to move away but I'm frozen )"
    show madd paralyzed at left_small
    brother_says "I thought you were a gamer ? how are you so bad at this ?"
    show madd confused at left_small
    x " ( His words are mocking, but i know  he is using this as an excuse to touch me )"
    show madd trembling at left_small
    x "( His hand moves to mine, guiding it to the X button... )"
    show madd conflicted at left_small
    x "( His hand lingers on mine... )"
    show madd shocked at left_small
    x " (Sudenly i feel it, something pointy touching my butt  ...its his bulge pressing against my back... )"
    show madd paralyzed at left_small
    x "( Oh God. This is really happening. )"
    show madd horrified at left_small
    x "( My heart is racing... )"
    show madd stressed at left_small
    x " ( i dare not speak )"
    

    scene scene_brother_room_talk_level1_grope_start
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd shocked at left_small
    x "( Without warning, his hand shoots up to my chest. He doesn't ask—he simply reaches out and grabs. His palm presses firmly against my breast through the fabric of my shirt, and the shock of his touch steals my breath. )"
    show brother debased at right_small
    brother_says "Now you're doing great... just like that."
    show madd paralyzed at left_small
    x "( This is really happening. My own step brother is... groping me. )"
    show madd flustered at left_small
    x "( His fingers dig into the fabric of my shirt, groping at my breast through the material. The cloth presses against my skin as he squeezes I can feel every contour of his palm, every squeeze of his fingers. )"
    show madd distressed at left_small
    with dissolve
    x "( The sensation is overwhelming. I feel utterly trapped, my butt being trapped betweem his legs and his arms holding me there. There's nowhere to go. No escape. )"
    show madd trembling at left_small
    x "( I cannot bring myself to speak. I cannot protest. I cannot move. I'm frozen in place, paralyzed by a mixture of fear, shame, and confusion. )"
    show madd horrified at left_small
    x "( His grip intensifies around my breast, his fingers pressing and kneading through my shirt. )"

    show brother sadistic at right_small
    brother_says "Looks like you enjoy gaming as much as me , sweet sister. "
    show madd nauseated at left_small
    x "( No. That's not true. I don't want this. I don't enjoy this. )"
    show madd violated at left_small
    with dissolve
    x "( I am allowing this. I am permitting my own brother to grope my breasts through my clothes, to violate my body with his hands, all because I need his money. I have sold my dignity for financial survival. Every squeeze of his hand is a reminder of how low I've sunk. )"
    

    # Scene: The moment of sexual violation - brother's predatory breach of trust


    show brother sadistic at right_small
    brother_says "Let's try the next level, shall we ?"
    show madd violated at left_small
    x " ( i dare not respond )"
    show madd processing at left_small
    with dissolve
    x "(Suddenly I feel his grip loosen )"
    show madd hopeful at left_small
    with dissolve
    x "(Thank god he is letting go... )"
    x "(Then he suddenly aims for under my shirt )"
    
    
    scene scene_brother_event1_hand_under_shirt
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    x "( He is sliding his hands inside my shirt now.... His cold hands are now directly on my skin )"
    show madd traumatized at left_small
    with dissolve
    x "( I am frozen in shock... )"
    show madd paralyzed at left_small
    with dissolve
    x "( I can't believe this is happening. I feel like a prostitute, letting my own brother touch me like this... )"
    show madd self loathing at left_small
    with dissolve
    x "( i feel his hands climbing up slowly, i knew he was aiming for my breasts but the slow, deliberate way he's doing it is making it even worse... )"
    show madd distressed at left_small
    with dissolve
    x "( Suddenly, I gather all my strength )"
    show madd determined at left_small
    with dissolve
    x "( I suddenly push him away and stand up)"
    show brother shocked at right_small
    brother_says"What the hell Maddie? We were just getting to the fun part... "
    show madd paralyzed at left_small
    x "( I am in shock...How can he say such things so casually )"
    show madd stressed at left_small
    x "I... I should go now."
    x "(I fix my displaced shirt )"
    show brother mocking at right_small
    brother_says "Fine, Come back when you wanna play again. I'll be waiting... "
    show madd anxious at left_small
    x "(as i was leaving , he suddenly speaks up )"
    show brother greedy at right_small
    brother_says "Oh, and by the way... if you ever need money, I will give you 100 bucks if you let me play with the joysticks on your chest  "
    brother_says "Without the shirt next time... "
    show madd traumatized at left_small
    x "(how can he even put these into words... how can he treat this encounter so casually)"
    # Scene: Madd's traumatic escape from her abuser - emotional and physical departure
    
    scene scene_brother_event1_madd_escape
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    x "( I hurriedly leave the room, my mind racing... )"
    show madd violated at left_small
    x " ( What just happened...? )"
    show madd self loathing at left_small
    x "( I need to get away from this place... )"
    show madd depressed at left_small
    x "(i feel so dirty... )"
    $ last_brother_talk_hour = game_time.hour
    $ demands_brother += 1
    $ character_relations["brother"]["lust"] = max(100, character_relations["brother"]["lust"] + 10)
    $ character_relations["brother"]["intimacy"]+=3
    $ character_relations["brother"]["friend"]+=1
    $ character_relations["brother"]["touched_madd"] += 1
    $ character_relations["brother"]["groped_madd"] += 1
    $ character_relations["brother"]["undressed_madd"] += 1
    $ journal_event_set_done("Brother", "Gaming Session (Event 1)")
    $ journal_event_show("Brother", "Bare Ass (Demands)")
    $ journal_event_show("Brother", "Bare Breast (Demands)")
    call advance_time_and_check(minutes=120) from _call_advance_time_and_check_10
    $ madd_willpower=max(madd_willpower-20,0)
    jump home_areas


label talk_to_brother_level_1_event_2:
    scene scene_brother_room_brother_playing_on_pc
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show brother predatory at right_small
    with dissolve
    show madd curious at left_small
    with fade
    x "(he points his controller at me )"
    show madd hesitant at left_small
    x "(he is sitting on his gaming chair )"
    show madd distressed at left_small
    x "( Something about his expression makes my stomach twist, but I ignore the warning feeling )"
    show brother lustful at right_small
    brother_says "Here take this controller and I will teach you how to play."
    x "(He says with one hand holding the controller out to me, while his other hand is resting on his thigh signaling me to sit between his legs on the chair )"
    x "(I have to endure this if I want the money, but the thought of sitting between his legs on the chair makes my skin crawl... )"
    show madd conflicted at left_small
    x "Alright..."
    show madd anxious at left_small
    x "( Why do I feel so hesitant? He's just offering to teach me a game... )"
    show madd conflicted at left_small
    x "( As I take the controller and start to sit away from him, he stops me )"
    show madd worried at left_small
    brother_says "Sit right here... between my legs. That way I can guide you better."
    show brother dominant at right_small
    x "( That sounded more of a command than a request )"
    show madd hesitant at left_small
    x "( Sit on his lap? That feels... wrong. My face flushes with embarrassment at the suggestion )"
    show madd nervous at left_small
    x "( i hesitantly sit on his lap )"
    
    
    scene scene_brother_event2_lap_trapped
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd paralyzed at left_small
    x "( Maybe I'm overreacting. Maybe I'm seeing evil where there's none. )"
    show madd confused at left_small
    x "( I lower myself onto his lap, feeling unbearably self-conscious. Am I sitting in the right place? Is this weird? )"
    show madd distressed at left_small
    x "( The positioning feels intimate and wrong all at once )"
    show brother dominant at right_small
    brother_says "See, it wasnt so bad, was it? Now I can show you how to play properly while keeping you warm and comfortable."
    show brother debased at right_small
    # Scene: Trapped on his lap - the beginning of manipulation and physical entrapment
    show madd uncertain at left_small
    x "( As I start playing, he wraps his arms around me from behind )"
    show madd stressed at left_small
    x "( I'm completely enclosed, his body surrounding mine )"
    show madd nervous at left_small
    x "( His hands holding the controller with mine )"
    x "( Why is my heart racing like this? Focus on the game, just focus on the game )"
    show brother possessive at right_small
    brother_says "Just relax, let me guide your hands."
    show madd conflicted at left_small
    x "( I nod but I can barely focus )"
    show madd distressed at left_small
    x "( His hand moves to mine, guiding it to the shoot button... )"


    scene scene_brother_event2_thigh_grope
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd shocked at left_small
    x "( Suddenly, he pulls his hand away and puts them on my thighs )"
    show brother debased at right_small
    x "( His hands are now directly on my legs )"
    show brother perverted at right_small
    brother_says "Now relax and practice another gun."
    show madd horrified at left_small
    x "( My entire body goes rigid. This is no longer ambiguous. This is intentional )"
    show madd paralyzed at left_small
    x "( Panic floods through me, but I say nothing. The shame of admitting what's happening is almost worse than the act itself )"
    show madd distressed at left_small
    x "( I can feel the heat of his palms through my pants )"
    show madd shocked at left_small
    x "( This is beyond any excuse now )"
    show madd trembling at left_small
    # Scene: Escalating violation - brother moves from thighs to buttocks

    show madd trembling at left_small
    x "(slowly his hand rounds my thigh... touching my ass... )"
    show madd distressed at left_small
    x "( I can feel the weight of his palm against me through my clothes )"
    show madd paralyzed at left_small
    x "( Shame burns through me like fire. How did I let this happen? Why didn't I stop him sooner? )"
    show madd self loathing at left_small
    x "( I'm the one at fault here. I came to him. I asked for money. )"
    show brother perverted at right_small
    x "( His fingers dig in, squeezing deliberately )"
    show brother sadistic at right_small
    brother_says "That's it. Remember in shooting games slow is smooth and smooth is fast " 
    show madd traumatized at left_small
    x "( I knew this phrase wasnt for any shooting game but it was him signaling his intensions for me  )"
    x "( I feel complicit in my own violation just by staying here )"
    show madd helpless at left_small
    x "( I have no way out )"
    # Scene: Madd completely frozen and helpless - trapped in violation
    show madd horrified at left_small
    x "( The shame is suffocating. What if someone finds out? What if I'm blamed for this? )"
    show madd shocked at left_small
    x "( I have never felt more powerless in my entire life )"
    show madd helpless at left_small
    x "( Suddenly, he stops touching me and I thank God this is finally over )"
    show madd hopeful at left_small
    x "( Maybe that's all. Maybe he was just... testing me. )"


    scene scene_brother_event2_frozen_violation
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    x "( But my hope dies as quickly as it was born when I feel his hand moving toward the waistband of my shorts )"
    show madd distressed at left_small
    x "( He's trying to reach my bare skin... to touch me in a way that cannot be mistaken for anything innocent )"
    x "(He's trying to undress me right here while i sit on his lap)"
    show madd paralyzed at left_small
    x "(He lowers my shorts as cold air hits my skin...My butt was completely out in the open now as he starts caressing my naked skin )"
    x "(If i dont stop this, if i let it happen He will only get more emboldened. He will push further and further until there's nothing left for me to protect )"
    x "( No. Not this. I have to stop this now or I'll never forgive myself )"
    show madd determined at left_small
    x "( My survival instinct finally overrides my fear )"
    show brother sadistic at right_small
    brother_says "That's it Maddie...you're getting the hang of it"


    # Scene 3: Most impactful moment - reaching for bare skin, moment of resistance
    scene scene_madd_moment_of_resistance_talk_event_2_madd_gets_up
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    x "( With every ounce of strength I can muster, I surge with energy and push myself up )"
    show madd angry at left_small
    x "( I'm finally using my voice, even if it's wordless )"
    show madd stressed at left_small
    x "( As I stand up, I feel both relief and a deeper layer of shame... shame that I let it go this far )"
    show madd violated at left_small
    x "( But also... pride that I finally said no )"
    show brother shocked at right_small
    x "( He's stunned that i stopped it .I can see it in his eyes )"

    # Scene 4: Escaping and feeling ashamed
    show madd violated at left_small
    x "( I feel so violated... so dirty... and everything reminds me that my mom isn't here to protect me anymore )"
    show madd depressed at left_small
    x "( Ever since she died, I've been completely alone in this house with him and his dad)"
    show madd distressed at left_small
    x "( I am utterly vulnerable, i bowed my head in apology for leaving...I know i shouldnt be apologizing )"
    show madd stressed at left_small
    with dissolve
    x "I... I should go now."
    show madd anxious at left_small
    x "( I can barely look at him )"
    show brother vindictive at right_small
    brother_says "Tch. Fine Come back when you wanna play again. I'll be waiting... "
    show madd anxious at left_small
    x "( His words drip with menace... as if this is some kind of game to him )"
    show madd horrified at left_small
    x "( As I move toward the door, terror and shame war inside me )"
    show madd horrified at left_small
    x "( I have to get out. I have to get away from him. )"
    show brother possessive at right_small
    brother_says "Oh, and by the way... if you ever need money, I will give you 200 bucks if you let me touch your soft ass some more..."
    show brother greedy at right_small
    x "( He's leaning back in his chair, arms spread, like he owns the whole room )"
    show madd shocked at left_small
    x "( My blood runs cold. He's offering me money? He's trying to make this a transaction? How can he say something so casually? )"
    show brother possessive at right_small
    brother_says "Without any clothing in between next time. Heh heh heh..."
    show madd paralyzed at left_small
    x "( His laughter is cruel and mocking, echoing in my ears )"
    show madd self loathing at left_small
    x "( The humiliation is complete. Not only did he violate me, but now he's reducing it to a financial proposition )"
    show madd broken at left_small
    x "( I can't even look at him anymore. If I do, I might break completely )"
    show brother laugh at right_small
    brother_says "Get out now."
    # Scene 5: Processing trauma alone
    
    scene scene_dad_event1_rejection_despair
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd violated at left_small
    x "( I hurriedly leave the room, my mind racing with a thousand thoughts and emotions )"

    show madd self loathing at left_small
    x "( The self-hatred is overwhelming. I should have said no. I should have fought harder. I should have... what? What could I have done? )"

    show madd depressed at left_small
    x "( How am I supposed to face him again? How am I supposed to live in this house? )"

    $ last_brother_talk_hour = game_time.hour
    $ demands_brother += 1
    $ character_relations["brother"]["lust"] = max(100, character_relations["brother"]["lust"] + 10)
    $ character_relations["brother"]["intimacy"]+=3
    $ character_relations["brother"]["touched_madd"] += 2
    $ character_relations["brother"]["groped_madd"] += 2
    $ character_relations["brother"]["friend"]+=1
    $ journal_event_set_done("Brother", "Lap Trap (Event 2)")
    $ journal_event_show("Brother", "Bare Ass (Demands)")
    $ journal_event_show("Brother", "Bare Breast (Demands)")
    call advance_time_and_check(minutes=120) from _call_advance_time_and_check_11
    $ madd_willpower=max(madd_willpower-20,0)
    jump home_areas




#LISTEN TO DEMANDS  BROTHER SCENES


label brother_listen_to_demands:
    scene scene_brother_room_brother_playing_on_pc
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show brother at right_small
    with dissolve
    brother_says "Finally, you're willing to listen."
    
    show madd stressed at left_small
    x "What do you want?"
    
    show brother predatory at right_small
    brother_says "I want something only women have. i want to touch it. "
    
    show madd horrified at left_small
    x "What do you mean?"
    
    show brother leering at right_small
    brother_says "I want to touch you. Your body. However I want, whenever I want."
    
    show madd shocked at left_small
    x "That's... that's disgusting. No."
    
    show brother arrogant at right_small
    brother_says "Very well, go on ahead . Get out of the room."    
    show madd depressed at left_small
    x "( What can i do here. If i go out i will not have any money to escape . I think about my parents. Mom wanted me to be an engineer. Dad would have been proud. )"
    
    show madd uncertain at left_small
    x "( If I don't get out of this house, those dreams die with me. )"

    $ madd_willpower=max(madd_willpower-20,0)
    
    show brother sadistic at right_small
    menu:
        "Let him touch your bare breast for 200 dollars" :
            jump let_him_touch_bare_breast
        
        
        "Let him touch your bare ass for 200 dollars" :
            jump let_him_touch_bare_ass
        
        
        "Refuse and leave":
            show madd angry at left_small
            x "No. I'd rather die than let you touch me like that."
            
            show brother vindictive at right_small
            brother_says "Your loss. You'll regret this."

            $character_relations["brother"]["anger"] +=10
            show madd stressed at left_small
            x "( I need to find another way... )"
            call advance_time_and_check(minutes=10) from _call_advance_time_and_check_9
            jump step_brother_room_scene

label let_him_touch_bare_breast:
    show madd conflicted at left_small
    x "( I can't believe I'm doing this. I'm letting him touch my bare breast)"
    show madd resigned at left_small
    x "(But i have to do it for money. I have no choice.)"
    scene brother_let_him_touch_bare_breast_intro
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd trembling at left_small
    show brother lustful at right_small
    x "(my heart pounded so hard when he pushes his char back and stands right next to me with his lustful eyes on my chest)"
    show brother sadistic at right_small
    brother_says "Finally giving in, huh maddie? I knew you couldn't resist the money. You just sold your dignity for cash"
    show madd distressed at left_small
    x "(The words stung, but I can't let him see that. I have to stay strong.)"
    
    scene brother_let_him_touch_bare_breast_pull_shirt  
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show brother predatory at right_small
    x "(his hands move to my tshirt , pulling it softly up)"
    show brother leering at right_small
    x "(His eyes locked on my own, waiting for my reaction.)"
    show brother obsessed at right_small
    brother_says "I want to see the way you look when I touch you. " 
    brother_says "I want to drink in the sight of you exposing yourself to me. It's going to be so hot."
    show madd flustered at left_small
    x "(My face flushed with embarrassment, but I can't back out now. I have to go through with it.)"

    scene brother_let_him_touch_bare_breast_pull_shirt_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd horrified at left_small
    x "(He lifted it slowly ,revealing my skin inch by inch. )"
    show madd paralyzed at left_small
    x "(Immediately i covered my chest with my arms, trying to hide myself from him.  that's how vulnerable I felt)"

    scene brother_let_him_touch_bare_breast_pull_shirt_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")


    show madd violated at left_small
    x "(Once the tshirt was parted ways wiht my chest, he swiftly reached out the rest of the way )"
    show brother possessive at right_small
    x "(He stood there for a moment, just looking at me showing me my tshirt like it was a prize he just won. )"
    show brother dominant at right_small
    brother_says "See this maddie ?  To think this small piece of cloth was the only thing standing between you and me. "
    brother_says "This small thing in my hand is my claim to you. "

    scene brother_let_him_touch_bare_breast_pull_shirt_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show brother debased at right_small
    x "(As he said that he sniffed the shirt, and I could see the lust in his eyes. It was like he was savoring the scent of my skin on the fabric. )"
    show madd self loathing at left_small
    x "(It was so creepy, but I couldn't look away. Although it shouldnt impact me in any way, the fact that he was sniffing my shirt like an animal made me so much more embarassed  )"
    show brother obsessed at right_small
    brother_says "I can smell you on this shirt, maddie. I can smell your skin, your scent. It's intoxicating. I want to keep it forever."
    show madd distressed at left_small
    x "(I wanted to disappear. I wanted to crawl into a hole and never come out. But I couldn't. I had to stay there and endure his words and actions.)"

    scene brother_let_him_touch_bare_breast_pull_shirt_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show brother smirk at right_small
    x "(After a moment, he finally placed the shirt down on the bed and looked back at me with a satisfied smirk. )"
    show brother sadistic at right_small
    brother_says "Now time for the main course, maddie. "
    show madd paralyzed at left_small
    x "(I was still covering my chest with my arms but he didnt care . He just reached out and grabbed my breast on top of my arms and squeezed it firmly. )"
    show brother leering at right_small
    brother_says "AHhh, you feel so good, maddie. Your skin is so soft. "
    show madd deep blush at left_small
    x "(He was slowly but firmly kneading my breast, and I could feel the heat rising in my face. )"
    x "(Suddenly he got more aggressive, and shouted )"
    show brother dominant at right_small
    brother_says "Put your arms down, maddie. I am paying for this, so you will do as I say. "
    show madd trembling at left_small
    x "(I was so scared, but I couldn't disobey him. I slowly lowered my arms, exposing my breast to him. )"

    scene brother_let_him_touch_bare_breast_pull_shirt_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd conflicted at left_small
    x "(As soon as I did that, he immediately went back to kneading my breast, but this time he was more aggressive. He was squeezing it harder and faster, and I could feel the pleasure and pain mixing together in a way that made me feel so conflicted. )"
    show madd self loathing at left_small
    x "(i was in my stepbrother's room, letting him touch my bare breast for money. )"
    show madd distressed at left_small
    x "(Is becoming an engineer really worth this? Is it worth selling myself like this? )"
    show brother mocking at right_small
    brother_says "You look so hot when I touch you like this, maddie. I can see the pleasure on your face, even though you're trying to hide it"
    show madd horrified at left_small
    x "(The worst part was that he was staring at my face the whole time, watching for any signs of pleasure. )"
    show madd violated at left_small
    x "(He was enjoying this so much, and it made me feel even more ashamed. )"
    show brother lecherous at right_small
    brother_says "These are such good hand warmers, maddie. I could just sit here and touch you all day. "
    show brother perverted at right_small
    brother_says "Touching my step sister's breast like this, it's like a dream come true for me. Maybe next time i will suck on them too, what do you think ? "
    show madd stressed at left_small
    x "(I wanted to scream at him, to tell him to stop, but I controlled myself. )"
    show madd resigned at left_small
    x "Uh.... I... I don't think that's a good idea. Let's just stick to the breast touching for now. "
    show brother mocking at right_small
    brother_says "You're no fun, maddie. But fine, we'll take it one step at a time. "
    show madd traumatized at left_small
    x "(It went on like this for a while, with him kneading my breast and making lewd comments, and me trying to endure it without breaking down. )"
    show madd hopeful at left_small
    x "(Finally ,after what felt like an eternity, he stopped and let go of my breast. )"
    show brother smirk at right_small
    brother_says "That was amazing maddie. Here's your 200 dollars. You earned it. "

    $ madd_money += 200
    $ stat_notification = "Received 200 dollars (From Brother) 💰"
    $ renpy.pause(2.0)
    $ stat_notification = ""


    show madd shaken at left_small
    x "(I accepted the money with trembling hands, feeling a mix of relief and shame. )"
    show madd broken at left_small
    x "(I just let my stepbrother touch my bare breast for money. I don't know how I'm going to face him after this, he knows  that i just sold myself to him. )"
    show madd determined at left_small
    x "(But I have to keep going. I have to endure this if I want to achieve my dreams. )"
    


    scene scene_brother_breast_aftermath
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd weeping at left_small
    x "(I looked down at my chest, then at the 200 dollars in my hand, and i realized i just swapped my dignity for cash to my own stepbrother. )"
    x "(Tears streamed down my face as I grappled with the reality of what I had just done and walked out of his room, trying to hold back my sobs. )"

    $ journal_event_set_done("Brother", "Bare Breast (Demands)")
    $ character_relations["brother"]["intimacy"]+=5
    $ character_relations["brother"]["undressed_madd"] += 1
    $ character_relations["brother"]["groped_madd"] += 1
    $ character_relations["brother"]["friend"]+=1
    $ last_brother_talk_hour = game_time.hour
    $ demands_brother += 1
    $ journal_event_set_done("Brother", "Bare Breast (Demands)")

    call advance_time_and_check(minutes=120) from _call_advance_time_and_check_12
    $ madd_willpower=max(madd_willpower-20,0)
    jump home_areas


label let_him_touch_bare_ass:
    scene scene_brother_room_brother_playing_on_pc
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd conflicted at left_small
    with dissolve
    x "( I swallow hard, the words stuck in my throat )"
    show madd resigned at left_small
    x "I... I'll do it. For 200 dollars."
    show madd hesitant at left_small
    x "(He gets up from his chair and says )"
    show brother lustful at right_small
    with dissolve
    brother_says "Excellent choice, now come here .I am gonna enjoy this so much."
    show madd trembling at left_small
    x "(He was standing there with his arms open , i knew what i had to do )"


    scene brother_let_him_touch_bare_butt_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd trembling at left_small
    with dissolve
    x "(i went straight in his arms as his arms wrapped around me locking me in place)"
    show madd resigned at left_small
    x "(I had made my choice to let him touch me, there was no escape now)"
    show brother possessive at right_small
    with dissolve
    brother_says "You look so adorable Maddie...I am gonna enjoy playing with your ass"
    show madd horrified at left_small
    x "(As he says that his hands goes down to my ass and starts squeezing it through my shorts )"
    show madd self loathing at left_small
    x "(What the heck am i thinking? Letting my own stepbrother touch my ass? I am so messed up)"


    scene brother_let_him_touch_bare_butt_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show brother perverted at right_small
    with dissolve
    brother_says "Mmmm...now to touch it properly"
    show madd shocked at left_small
    with dissolve
    x "(As he says that i feel his hands pull down my shorts as as shiver runs down my spine)"
    show madd paralyzed at left_small
    x "(This is really gonna happen, i am really gonna let him touch my bare butt)"
    show madd self loathing at left_small
    x "(I cant even blame him for this, i came to his room for money in exchange for letting him touch me, i am the one who made this happen)"


    scene brother_let_him_touch_bare_butt_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd violated at left_small
    with dissolve
    x "(With a swift motion he removes my shorts and as the cold air hits my bare skin i realize how vulnerable i am right now)"
    show madd paralyzed at left_small
    x "(In my stepbrother's room, with me in almost hugging position, and my bare ass exposed to him)"
    show brother dominant at right_small
    with dissolve
    brother_says "That's it Maddie, let me explore your cute little ass"
    show madd trembling at left_small
    x "(His hands start to caress my bare skin, the hot sensation of his touch a sharp contrast to the cold air)"


    scene brother_let_him_touch_bare_butt_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd conflicted at left_small
    with dissolve
    x "(My whole body is trembling with a mix of fear and excitement as his hands continue to explore my bare butt)"
    show madd confused at left_small
    x "(Why am i excited? This is my stepbrother, this is wrong! But i cant help the feelings that are coursing through me)"
    show madd distressed at left_small
    x "(My whole body was sweating, my heart was pounding, and i felt like i was on the edge of losing control)"
    show brother sadistic at right_small
    with dissolve
    brother_says "just touching it makes me so hard Maddie...Once i start putting my dick in between your cheeks, i am gonna lose it"
    show madd horrified at left_small
    x "(What the heck is he saying? Is he saying he is gonna eventually put his dick inside me ?? This is getting out of hand, this is really wrong)"
    show madd violated at left_small
    x "(He is supposed to be my stepbrother, not my lover, not my sexual partner, not anything like that! But here i am, letting him touch me, letting him say these things to me, and i cant even stop it)"


    scene brother_let_him_touch_bare_butt_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    with dissolve
    x "(Suddenly he gets rougher, his hands start to squeeze my ass harder )"
    show madd overwhelmed at left_small
    x "(As he squeezes and stretches my cheeks apart i feel my butthole getting more and more exposed to the room and to him)"
    show madd helpless at left_small
    x "(God how long is it gonna last? How long is he gonna keep touching me like this? )"
    show madd broken at left_small
    x "(he kept playing with my ass for what felt like an eternity, his hands never leaving my skin, his touch never getting any softer)"
    show madd resigned at left_small
    x "(My body was a playhouse for his hands, and i was completely at his mercy, unable to do anything but let him continue)"
    show madd traumatized at left_small
    x "(Finally after what felt like hours, he stopped touching me and just held me in his arms, his hands still resting on my bare skin)"
    show brother obsessed at right_small
    with dissolve
    brother_says "That was amazing Maddie, your ass is just perfect, I could play with it all day"
    show brother leering at right_small
    brother_says "Just touching it feels so heavenly, if i ever get the chance to put my cock in your vaginal area, i am gonna lose it"
    show madd nauseated at left_small
    x "(How can he say that to his step sister? and not even feel a hint of guilt or shame? )"
    show madd shaken at left_small
    x "(He let me go as i finally picked up my shorts and put them back on, but the memory of his touch and his words lingered in my mind )"

    scene brother_let_him_touch_bare_butt_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd shaken at left_small
    with dissolve
    x "(He handed me 200 dollars as i sat on his bed still fixing my clothes )"
    $ madd_money += 200
    $ stat_notification = "Received 200 dollars (From Brother) 💰"
    $ renpy.pause(2.0)
    $ stat_notification = ""
    show brother greedy at right_small
    with dissolve
    brother_says "Worth much more than that Maddie, I would even pay a million dollars to have your virginity, but for now, this will do"
    show madd processing at left_small
    x "(....)"
    show madd horrified at left_small
    x "(The hell !! He just said he would pay a million dollars for my virginity? This is more than just talking about touching my ass, this is talking about having a sexual relationship with me! )"
    show madd distressed at left_small
    x "(Does this idiot even want to put a baby in me? Does he even care about the consequences of his actions? )"

    scene scene_dad_event1_rejection_despair
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    x "( I stumble out of his room, my legs barely holding me up )"
    
    show madd depressed at left_small
    x "( What have I become? )"
    
    show madd paralyzed at left_small
    x "( Have I really fallen so far that I'd sell my body to my abuser for money? )"
    
    show madd self loathing at left_small
    x "( And worse... have I already accepted that I'll do it again? )"
    
    show madd focused at left_small
    x "( Yes. And I'll do it again if it means getting out of here. )"
    
    show madd determined at left_small
    x "( That's what survival looks like )"
    
    show madd determined at left_small
    x "( Every degradation is a price I'm paying for my freedom )"
    
    show madd self loathing at left_small
    x "( Even if it means he gets to use every part of me. )"
    
    show madd conflicted at left_small
    x "( And I will make it worth it... somehow )"

    $ journal_event_set_done("Brother", "Bare Ass (Demands)")
    $ character_relations["brother"]["intimacy"]+=5
    $ character_relations["brother"]["undressed_madd"] += 1
    $ character_relations["brother"]["groped_madd"] += 2
    $ character_relations["brother"]["friend"]+=1
    $ last_brother_talk_hour = game_time.hour
    $ demands_brother += 1
    call advance_time_and_check(minutes=120) from _call_advance_time_and_check_13
    $ madd_willpower=max(madd_willpower-20,0)
    jump home_areas



#Kitchen MISS  BROTHER SCENES


label miss_event_brother:
    scene scene_kitchen_minigame_madd_standing
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd think at left_small
    x "(I was busy cooking some quick meals for myself and i heard some movement in the kitchen.)"
    x "(Footsteps ... Someone was in the kitchen with me, i didnt bother checking who it was, i just wanted to finish cooking.)"

    scene scene_miss_event_brother_misses_brother_approaching_madd
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd think at left_small
    show brother predatory at right_small
    x "(I continued cooking, but then i heard some footsteps behind me and it came to a stand still right next to me, close enough that i could feel the warmth radiating off his body and catch the stale smell of him.)"
    x "(Someone was standing right next to me)"
    brother_says "Smells really good in here "
    show madd worried at left_small
    x "(I recognized the voice, it was my brother . what was he doing here ?)"
    x "Oh, thank you, i just made some quick meals for myself"

    scene scene_miss_event_brother_misses_brother_neck_kissing_madd
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd shocked at left_small
    show brother lustful at right_small
    x "(Suddenly he wrapped his arms around me and kissed my neck, i was so surprised that i didnt know how to react.)"
    x "(What the hell is going on ? Why is he doing this ? I felt his wet lips on my neck, the scratch of his stubble grazing my skin right after, and i was frozen in place)"

    scene scene_miss_event_brother_misses_brother_neck_kissing_madd_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd disgusted at left_small
    show brother horny at right_small
    brother_says "So Maddie...What are you cooking ?"
    x "(right after he said that, he kissed my neck again, his kiss would last long enough for me to feel his tongue dragging slowly across my skin )"
    x "(He wasnt just using his lips, he was using his tongue as well, leaving a wet trail that went cold almost immediately, it was so disgusting and i wanted to push him away )"
    x "Um..nothing just cutting some vegetables for a salad"
    x "(Disgusting disgusting disgusting, why the hell are you kissing your step sister like that ? Filthy pig )"

    scene scene_miss_event_brother_misses_brother_neck_kissing_madd_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    show brother lecherous at right_small
    x "(suddenly his kisses became more aggressive, like he took a bite of my neck, the pressure of his teeth digging in just enough to sting)"
    brother_says "Werent you gonna offer me some ?"
    x "(I looked back at him and i saw him moving his tongue up and down at me like a snake does to its prey, a string of his saliva still connecting his lips to my neck )"
    x "(I quickly turned around back focusing on the cutting board, i didnt want to look at his lustful face)"
    x "Yeah...Sure...Once im done with this , I'll make you something to eat"
    x "(now he was straight up licking my neck, no more just kissing, he was licking my neck like a dog licks its owner but i guess he was the owner and I was the dog in this situation)"
    x "(What do i do ? how can i escape this ? I cant just push him away, he is stronger than me )"
    show madd nervous at left_small
    x "(Ah i do have  a knife in my hand, maybe i can use it to defend myself if he tries to do something more than just licking my neck )"
    x "(I cant risk anything too severe, i just want to get him off of me and get out of the kitchen as soon as possible )"

    scene scene_miss_event_brother_misses_brother_neck_kissing_madd_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd nervous at left_small
    show brother dominant at right_small
    brother_says "Okay now lift your arms up Maddie..."
    x "(he was heavily breathing on my neck, the heat of his breath hitting the wet spots his saliva had left, making my skin crawl)"
    x "(i put my knife down on the counter,  i didnt wanna risk hurting myself or him, and i slowly lifted my arms up, my hands trembling slightly)"
    x "(He goes back to kissing my neck , well at least he wasnt soiling my neck with his tongue anymore, but it was still nasty)"
    show madd conflicted at left_small
    x "(i realize that by doing what he said, i was giving him consent to do whatever he wanted to me)"
    x "(Maybe i shouldnt have lifted my arms up, but i was so scared that i just did what he said without thinking about it)"

    scene scene_miss_event_brother_misses_brother_neck_gropping_madd
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    show brother lustful at right_small
    x "(Suddenly his hands landed on my breasts, he was groping me over my shirt, the fabric bunching under his grip, the rough heat of his palms pressing through the thin material)"
    x "(He started squeezing my breasts, each squeeze pushing the breath out of me a little, i could feel his fingers digging into my skin )"
    brother_says "You have such nice breasts Maddie, i wish i could touch them more often"
    x "(Why is my own step brother doing this to me ? And why is he enjoying it so much )"
    show madd paralyzed at left_small
    x "(I just closed my eyes hoping its a bad dream and that when i open them, he will be gone and this will all be over)"
    x "(The good or bad part about a dream is sooner or later you have to wake up)"
    x "(And i was about to wake up to a reality far worse than any nightmare i could have imagined)"

    scene scene_miss_event_brother_misses_brother_neck_gropping_madd_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd disgusted at left_small
    show brother perverted at right_small
    x "(my whole body was sweating profousely due to the fear and disgust i was feeling )"
    brother_says "You are sweating so much Maddie, your scent is driving me crazy, i want to smell you all day"
    x "(He was taking deep breaths of my neck, like he was trying to get the scent of me into his lungs )"
    brother_says "I bet your armpits smell really good too, can i smell them ?"
    x "(What the hell? how can he ask to smell my armpits ? how do i even respond to that ? )"
    x "Umm...please dont do that"
    x "I...I havent showered in a while, so i dont think they smell good"
    x "(I was trying to come up with an excuse to get him to stop asking me to do disgusting things like that, but it didnt work)"
    brother_says "Pfft, that makes it even better. Adds more to the flavor, might even start licking your armpits too"
    x "(WHAT THE HELL ?! He is actually considering licking my armpits ?! And that too right after me lying about not showering ?!)"
    x "(how can any human be so deranged to even think about licking someone elses armpits ?! )"
    brother_says "Nevermind , my little friend is getting too excited, i need to hurry before it explodes so lets get to the main course"

    x "(He's gonna undress me...I know it. this is my last chance to stop him)"
    if character_relations["brother"]["intimacy"] < 15:
        menu:
            "Try to stop him" :
                if madd_willpower+2*(15-character_relations["brother"]["intimacy"]) >= character_relations["brother"]["lust"]:
                    show madd angry at left_small
                    x "You are my step brother, you shouldnt be doing this . Move your hands away from me before I call dad."
                    show brother shocked at right_small
                    brother_says "What? Why? I thought you liked it when I touched you like this ?"
                    brother_says "Tch..this aint over, I will get my revenge"
                    x "(His grip on me loosened as he stopped groping me, but the damage was already done. I could feel the heat of his touch lingering on my skin, and the memory of it burned in my mind)"
                    x "(I heard his footsteps as he angrily walked out of the kitchen, leaving me alone with my thoughts )"
                    $ character_relations["brother"]["anger"] +=20
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_96
                    $ character_relations["brother"]["intimacy"]+=5
                    call advance_time_and_check(minutes=120) 
                    $ madd_willpower=max(madd_willpower-20,0)
                    jump cooking_complete
                else:
                    $character_relations["brother"]["lust"]=0
                    $character_relations["brother"]["anger"] +=20
                    show madd trembling at left_small
                    x "(I wanted to stop him, but i was so scared that i couldnt even say anything, my voice was trembling and my body was shaking)"
                    x "(I just stood there, letting him do whatever he wanted to me, hoping that it would be over soon )"
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_97
        



    scene scene_miss_event_brother_misses_brother_undressing_madd
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd paralyzed at left_small
    show brother horny at right_small
    x "(Right after he said that, he started lifting up my shirt slowly )"
    x "(He lifted them up enough to expose my stomach and he says )"
    brother_says "Your hot body is making me so horny Maddie, i want to see more of it"
    x "(Now with my arms raised , he quickly lifted up my shirt and exposed my breasts  )"

    scene scene_miss_event_brother_misses_brother_undressing_madd_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    show brother dominant at right_small
    x "(Cold air hit my exposed skin all at once and my whole body tensed up, goosebumps rising on my stomach and sides)"
    x "(In the kitchen, with my shirt lifted up exposing my breasts, and my arms raised up in the air, i was practically offering myself to him )"
    x "(His hands ran over my exposed skin slowly, the callused roughness of his palms dragging across my ribs...not touching my breasts for now...But i knew it was only a matter of time)"

    scene scene_miss_event_brother_misses_brother_undressing_madd_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd violated at left_small
    show brother dominant at right_small
    x "(Finally his hands landed on my breasts, the warmth of his palms a sharp contrast to the cold air, he started squeezing them gently )"
    brother_says "These are so soft Maddie , you shouldnt hide them away, you should show them off more often" 
    x "(i wanted to scream and cry at the same time, his hands were running all over my breasts, and i was just standing there letting him do it)"
    x "(I lowered my arms down a bit trying to reason with him , hoping this doesnt escalate to something worse )"
    show madd angry at left_small
    x "You are my step brother, you shouldnt be doing this " 
    x "(His Grip on my breasts tightened a lot, as if he wanted to hurt me)"
    brother_says "Put your arms back up stupid bitch" 
    show madd trembling at left_small
    x "(Due to the sudden shift in his tone and the grip on my breasts, i put my arms back up)"

    scene scene_miss_event_brother_misses_brother_undressing_madd_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small
    show brother sadistic at right_small
    x "(As my arms were raised up again, his grip on my breasts loosened a bit, and he started kneading them with his fingers)"
    x "(Finally the pain from his grip on my breasts was gone, but i knew that reasoning with him was useless, so i just stayed quiet and let him do whatever he wanted to me)"
    x "(His breathing was getting heavier and heavier, it was very close to my neck and collarbone, it was slowly going towards my armpits )"
    x "(I had to say something to get him to stop, fuk it i will risk it)"
    show madd angry at left_small
    x "You really are a filthy pig arent you ? Trying to get off by groping your step sister , smelling her neck and armpits ? You are disgusting, you should be ashamed of yourself"
    x "(His groping stopped for a moment, and i could hear anger in his breathing)"
    show madd horrified at left_small
    brother_says "Fucking bitch , how dare you call me that ?  I was gonna stop after this but now you are really pissing me off"

    scene scene_miss_event_brother_misses_brother_removing_his_jeans
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    show brother vindictive at right_small
    brother_says "Filthy pig?? huh? Wait until i show you how filthy i am"
    x "(Suddenly i heard the metallic sound of his zipper, slow and deliberate, and i knew that things were about to get a lot worse)"
    brother_says "Maybe not today but i will make you eat my armpits "
    brother_says "I will shove your face in my armpits and make you smell them until you beg me to stop, It will fill your lungs until you pass out. That's when i will start fucking you "
    x "(All of these threats were making me so scared, maybe i should have just let him do whatever he wanted to me instead of trying to fight back )"

    x "(He's pulling out his manhood ...Oh god...If I want to threaten him with anything right now might be the last time)"
    x "(I dont know what he will do to me once it is out)"
    if character_relations["brother"]["intimacy"] < 40:
        menu:
            "Puff your chest and beat it loudly to show him you are not scared" :
                if madd_willpower+2*(40-character_relations["brother"]["intimacy"]) >= character_relations["brother"]["lust"] :
                    show madd angry at left_small
                    x "Keep your pants on you fucking creep. If you even touch me lightly with that thing, I will scream and call dad right here. Do you understand me ?"
                    show brother shocked at right_small
                    brother_says "Argh...You think Dad don't want to do the same thing to you ? You think Dad is not a filthy pig like me ? You are such a fucking idiot, you have no idea how the world works do you ?"
                    brother_says "Fair enough, you are not worth my time right now, but mark my words"
                    brother_says "He will treat you much worst than I ever did....and in the end you would have to pick between my love or his abuse"
                    brother_says "Or killing yourself"
                    x "(What the fuck did he just say...that's not gonna be my future no fucking way!!)"
                    x "(His grip on me loosened as he stopped groping me, but the damage was already done. I could feel the heat of his touch lingering on my skin, and the memory of it burned in my mind)"
                    x "(I heard his footsteps as he angrily walked out of the kitchen, leaving me alone with my thoughts )"
                    $ character_relations["brother"]["anger"] +=20
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_98
                    $ character_relations["brother"]["intimacy"]+=5
                    call advance_time_and_check(minutes=120) 
                    $ madd_willpower=max(madd_willpower-20,0)
                    jump cooking_complete
                else:
                    $character_relations["brother"]["lust"]=0
                    $character_relations["brother"]["anger"] +=20
                    show madd trembling at left_small
                    x "Keep your pants on you fucking creep. If you even touch me lightly with that thing, I will scream and call dad right here. Do you understand me ?"
                    show brother sadistic at right_small
                    with dissolve
                    brother_says "Go ahead call him dear sister."
                    brother_says "I'm sure he wont get turned on by seeing your naked body on full display like this, and then seeing me with my pants down"
                    brother_says "You had a knife in your hand but you still didnt stop me did you slut ? "
                    brother_says "Can't you see it ? All evidence points to the fact that you let it get this far you ."
                    x "(Tch... He's right about that. I had the knife in my hand.. I could have used it to threaten him but i did fuck-all with the only time i had the upper hand)"
                    x "I...I.."
                    x "(Words no longer came out of my mouth as i hear a laughter from him)"
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_99


    scene scene_miss_event_brother_misses_brother_removing_his_jeans_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd anxious at left_small
    show brother dominant at right_small
    x "(I heard the sound of his jeans dropping and the heat near my lower back changed immediately, like a wall of warmth pressing close without touching yet)"
    x "(I knew his dick was now exposed and he was about to use it on me, i could almost feel the air shift between us )"
    x "(I was still holding on to my brave face, but inside i was shaking with fear)"
    brother_says "Apologize to me right now, or this goes inside your baby making hole "
    x "(He wasnt lying, i could feel his dick near my back, it wasnt touching me...yet..but i could feel its presence)"

    scene scene_miss_event_brother_misses_brother_removing_his_jeans_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd trembling at left_small
    show brother calculating at right_small
    x "(Finally i let go of my brave face, and i started begging him to not put his dick inside me )"
    x "Please...Please dont do this...I am sorry for calling you a filthy pig..."
    x "I will do anything you want, just please dont put anything inside me..."
    x "(His motions slowed down a bit,  i could sense that he was considering my plea )"
    brother_says "Fine...Then i will rub one out on your back until i am satisfied. "
    brother_says "And you better not try to stop me, or i will make you regret it."
    show madd relieved at left_small
    x "(I was so relieved that he wasnt gonna put his dick inside me, so i just nodded my head in agreement)"

    scene scene_miss_event_brother_misses_brother_rubbing_his_manhood_on_madd
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd paralyzed at left_small
    show brother sadistic at right_small
    brother_says "Heh, Good girl, now just stay still and let me do what i need to do"
    x "(I stayed still, trying to not make any sudden movements that might anger him)"
    x "(And thats when i felt it ... his warm thick dick pressing flat against the bare skin of my lower back, the weight of it unmistakable)"
    x "(The heat radiating from it, the rigid hardness of it, as soon as it touched my skin every other smell in the room hit me at once - the garlic still burning low on the stove, his sweat, and underneath all of it the raw musky smell of his dick)"
    x "(As soon as he had pulled down his jeans, the smell of his dick was filling the air but i hadnt really noticed it until it was rubbing against me. )"
    x "(The fact that he was originally gonna put his dick inside me but then decided to rub it on my back instead made me relieved and even more accepting of the situation )"
    x "(I felt him using my back to pull his foreskin back and forth, it was so disgusting feeling the texture of his dick on my skin)"
    x "(All this while he was still groping my breasts, and i was just standing there as if i wasnt a participant in this)"
    brother_says "That's it Maddie, that's what you're good for...Letting men stronger than you use your body for their pleasure..."
    x "(His words were demeaning and humiliating, i was too scared of backlash to say anything back)"

    scene scene_miss_event_brother_misses_brother_rubbing_his_manhood_on_madd_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd nauseated at left_small
    show brother horny at right_small
    x "(I felt his dick grow right on my skin, pulsing slightly with each movement, his foreskin being pulled back more and more, the wetness spreading across my lower back in slow streaks)"
    x "(Even though i was wearing shorts , i felt his balls slapping against my buttocks)"
    x "(It was leaking precum and all of it was depositing on my back, the smell of his cock getting stronger and stronger )"
    x "(AS if his foreskin was holding back a dam of intense smell and as it was being pulled back, the dam was breaking and releasing all the smell at once )"
    x "(I knew what it was ...he was rubbing the dick cheese out of his cock on my back, that's why it smelled so bad and it was so wet )"
    x "(In the middle of kitcehn, I was there letting my step brother paint my back with his dick cheese, and i was there just standing not even fighting back...The overwhelming scent of him filling my lungs )"
    show madd self loathing at left_small
    x "(And i didnt say a word...what kind of pathetic bitch am i ?)"
    brother_says "That's it maddie, I am close to cumming now"

    scene scene_miss_event_brother_misses_brother_rubbing_his_manhood_on_madd_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    show brother sadistic at right_small
    x "(I could feel his dick throbbing against my back, and i knew he was close to cumming )"
    x "(He finally started shooting his load, and i could feel the hot sticky liquid being released onto my back)"
    x "(It was soo viscous and thick, the heat of it burning against my spine for a second before it started sliding downward like slow glue, and the smell hit the back of my throat and made me gag )"
    x "(Some of it landed on my sides , some of it landed on my shorts and through the gap between my shorts and my skin, it was getting on my buttocks as well )"
    x "(I just stood there, letting him finish cumming on my back, the smell was so overwhelming that i just wanted to run away and take a shower but i couldnt move )"
    brother_says "AHH, That's it Maddie, shower in my cum let it soak into your skin. Let the world know that you are mine"
    x "(Cant believe the words coming out of his mouth, it was like ever since Mom died people in this house got infected with some kind of brain disease that made them say the most disgusting things )"
    show madd overwhelmed at left_small
    x "(He kept cumming for a while, painting me with cum and I was his canvas, his masterpiece, his cum art )"
    x "(Finally he was done, and i was left there standing in a pool of his cum, the smell was so strong that it was making me want to vomit )"
    x "(His penis still stayed on my back as he stopped moving it, like an animal who has finished his prey off and is now just resting on it )"

    scene scene_miss_event_brother_misses_brother_rubbing_his_manhood_on_madd_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd traumatized at left_small
    show brother contemptuous at right_small
    brother_says "Remember this maddie , Remember what happens when you call me a filthy pig, this is what happens, you get covered in my cum "
    brother_says "God you smell like my dick cheese , whos the filthy pig now ?"
    x "(His words struck me like a ton of bricks, i was so humiliated and degraded, i just wanted to disappear )"
    show madd self loathing at left_small
    x "Sorry...I am sorry for calling you that...I am the filthy pig...Please forgive me..."
    x "(I was so desperate for forgiveness that i was willing to admit to being a filthy pig, even though i did nothing wrong )"
    x "(Why am i begging for anything? It shopuld be me who should be angry at him for doing this to me. Is this how women live ?)"
    x "(Just accepting abuse and begging for forgiveness ? I thought i was stronger than that, but here i am begging for forgiveness from the person who just sexually abused me )"
    brother_says "Filthy pig , covered in my cum, even your shorts are filthy now. Go clean yourself up and take a shower , you stink of my sock that i used to masterbate. Serves you right..."
    show madd shaken at left_small
    x "(With that he left the kitchen , leaving me there standing in a pool of his cum, i put on my shirt again )"

    scene scene_miss_event_brother_misses_brother_leaving_kitchen
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd shaken at left_small
    x "(AS i put on my shirt i realized wearing it was the worst mistake, the wet warmth of his cum was still on my back and the fabric pressed it flat against my skin, trapping it there.)"
    x "(The smell was right there under my shirt now, i could feel it slowly cooling against me. Usually i would think before doing something like that but i was still in shock.)"
    x "(same with my shorts , the cum that founds its way snuggling between the gaps of my shorts was on my butt slowly trickling down it . It was all so humiliating )"
    x "(Like i had just lost a war and the enemy was painting me with their flags)"
    show madd depressed at left_small
    x "(I tried to divert my mind and continued cooking knowing this will not be the end of his attempts at conquering me ...)"


    $character_relations["brother"]["lust"]=0
    $ character_relations["brother"]["touched_madd"] += 4
    $ character_relations["brother"]["groped_madd"] += 4
    $ character_relations["brother"]["undressed_madd"] += 1
    $ character_relations["brother"]["intimacy"]+=7
    $ journal_event_set_done("Brother", "Kitchen Ambush (Miss Event)")

    call advance_time_and_check(minutes=120) 
    $ madd_willpower=max(madd_willpower-20,0)
    
    jump cooking_complete


#SHOWER  BROTHER SCENES

label brother_walks_in_shower:
    scene scene_brother_walks_in_home_bathroom_madd_in_towel
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd uncertain at left_small
    x "(I'm wrapped in my towel, just stepping out of the shower.)"
    
    show madd shocked at left_small
    x "(The bathroom door opens without a knock.)"
    
    show brother fixated at right_small
    brother_says "Ah Knew i heard someone in the shower"
    
    show madd horrified at left_small
    x "(He's not surprised. He's not apologetic. This wasn't an accident.)"
    
    show madd trembling at left_small
    x "(He immediately puts his arms around my wet shoulder)"

    

    if character_relations["brother"]["lust"] >= 30:
        jump shower_brother_touches_madd
    else:
        jump shower_nothing_happens_brother
    
    jump home_areas


label shower_brother_touches_madd:
    scene scene_brother_walks_in_home_bathroom_madd_in_towel_both_hands_on_shoulders
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd shocked at left_small
    x "(Suddenly both his hands are on my shoulders, gripping me tightly.)"
    show madd horrified at left_small
    x "(What is his problem? He should be leaving the bathroom, not touching me)"
    x "(The grip is deliberate - there is nothing accidental about this)"
    show madd nervous at left_small
    x "Why...Why are you here? "
    show brother fixated at right_small
    brother_says "I just wanted to see you.."
    show madd distressed at left_small
    x "(He's staring at me with this weird look in his eyes, like he's trying to imagine me naked or something)"

    scene scene_brother_walks_in_home_bathroom_madd_in_towel_both_hands_on_shoulders_kiss 
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    x "(Suddenly his face is right next to mine)"
    show brother leering at right_small
    brother_says "Looking Good Maddie! Fresh out of the shower"
    show madd shocked at left_small
    x "(His face leans in on me, and before I can even react, his lips are on my cheeks )"
    show brother lustful at right_small
    x "(Then he gives this wide smile as if it was just an innocent kiss, but I can feel the lust in his eyes and the way he's touching me)"
    show madd distressed at left_small
    x "(What the fuck is wrong with him? Kissing me while I'm in a towel? )"
    show madd angry at left_small
    x "What are you doing? Please stop.."
    x "This is really making me uncomfortable.."
    show brother angry at right_small
    x "(Suddenly he gets mad and grabs me tighter )"
    brother_says "I call you beautiful and you tell me to stop? "
    show brother dominant at right_small
    brother_says "Ungrateful..bitch"

    scene scene_brother_walks_in_home_bathroom_madd_in_towel_both_hands_on_shoulders_pulling_towel_away
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    x "(He suddenly starts pulling my towel away from my body , while his other hand is still gripping my shoulder)"
    show madd paralyzed at left_small
    x "(He pulls my towel away only for a second exposing my bare chest, and i pull it back immediately covering myself)"
    x "(Cold air hit my skin for that fraction of a second - it felt like an eternity)"
    show madd trembling at left_small
    x "(My eyes meeting his, I can see the lust and anger in his eyes, and I know he's not going to stop until he gets what he wants)"  
    x "Please stop ... you should not be doing this.."
    show brother possessive at right_small
    brother_says "I'll tell you what i can do " 
    show madd distressed at left_small
    x "(He says that in angry tone and starts pulling my towel again )"   
    x "(I could try scaring him off by yelling at him or using Dad's name but that will anger him more)"
    
    if character_relations["brother"]["intimacy"] < 15:
        menu:
            "Fuck it. I'm in the bathroom — the sound will carry. Time to make some noise." :
                if madd_willpower+(15-character_relations["brother"]["intimacy"]) >= character_relations["brother"]["lust"]:
                    show madd angry at left_small
                    x "I said stop it, you fucking creep! If you don't get your hands off me right now, I'm going to start screaming 'rape' at the top of my lungs!"
                    x "The walls are thin — Dad will hear every single word. Do you understand me?!"
                    show brother shocked at right_small
                    brother_says "W-What the fuck did you just say...?"
                    x "I mean it! One more touch and I start screaming. Loud. Right now."
                    brother_says "Fine. You win this round, you little bitch."
                    brother_says "But mark my words — this isn't over. Next time Dad isn't around, I'm going to make you regret opening that fucking mouth."
                    x "(with that he let go of my towel and left the bathroom as i kept my eyes on him the whole time like a prey keeping an eye on her predator)"
                    $ character_relations["brother"]["anger"] +=20
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_100
                    $ character_relations["brother"]["intimacy"]+=3
                    call advance_time_and_check(minutes=120) 
                    $ madd_willpower=max(madd_willpower-20,0)
                    jump bathroom_scene
                else:
                    $character_relations["brother"]["lust"]=0
                    $character_relations["brother"]["anger"] +=20
                    show madd trembling at left_small
                    x "(I open my mouth... but nothing comes out at first. My voice is shaking so badly I can barely speak.)"
                    x "P-Please... stop... I-I'll tell Dad... I swear I will..."
                    show brother sadistic at right_small
                    with dissolve
                    brother_says "Hah. Go ahead."
                    brother_says "What do you think will happen once he walks in and sees you in your birthday suit."
                    brother_says "You think a man like him will save you? Seeing you in this state he might just push you in the shower stall and pretend that you are Emily"
                    
                    show madd paralyzed at left_small
                    x "(My blood runs cold. He doesn't even sound worried...And he's not wrong...Dad is not a man i can rely on to save me )"
                    x "(The only reason he would rescue me from him is so he could have me all to himself)"
                    brother_says "I can see it in your face , you know I'm speaking the truth"
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_101




    scene scene_brother_walks_in_home_bathroom_madd_in_towel_both_hands_on_shoulders_pulling_towel_away_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd violated at left_small
    x "(This time he manages to pull my towel away exposing my whole body to him, and I can feel his eyes all over me)"
    show madd paralyzed at left_small
    x "(I couldnt hold on to the towel anymore, and I just let it go, )"
    show brother leering at right_small
    brother_says "Damn you are so hot Maddie, "
    show brother lustful at right_small
    brother_says "I just want to touch you.."
    show madd trembling at left_small
    x "(And immediately after that he starts groping my body, squeezing my breasts and running his hands all over me)"
    x "(My arms moved instinctively to cover myself but his hands were already there - already claiming every inch of me)"
    show madd resigned at left_small
    x "(I just took a deep breath and tried to stay calm knowing that if i react in any way he might get more aggressive)"

    scene scene_brother_walks_in_home_bathroom_madd_in_towel_groped_by_brother
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd weeping at left_small
    x "(But my mind was so tormented by what was happening that I couldn't even think straight, my eyes were filled with tears and I just wanted it to end)"
    show madd distressed at left_small
    x "(My brother saw the tears in my eyes and he started mocking me, )"
    show brother mocking at right_small
    brother_says "Aww are you crying? "
    show brother possessive at right_small
    brother_says "All of this is mine...All of your body is mine.."
    show madd traumatized at left_small
    x "(He says while running his hands all over my body , going from one breast to the other )"
    x "(Each pass of his hands felt like it was erasing something of who I was)"
    show madd paralyzed at left_small
    x "(Suddenly his ot her hand come behind my back and starts squeezing my other breast)"

    scene scene_brother_walks_in_home_bathroom_madd_in_towel_groped_by_brother_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    x "(With both his hands on my breasts, he starts squeezing them hard, and I can feel the pain mixed with the pleasure)"
    show brother sadistic at right_small
    brother_says "Why so sad Maddie ? "
    brother_says "Dont like when your step brother touches you? "    
    show madd self loathing at left_small
    x "(He says that in a mocking tone, and I can feel the anger building up inside me but i didnt say a word )"
    show madd paralyzed at left_small
    x "(He was playing with my body like a toy, i was like a doll to him, a doll that he could do whatever he wanted with)"
    show madd horrified at left_small
    x "(He was squeezing both of my breasts hard as if hoping milk would come out, and I could feel the pain and humiliation of it all)"

    scene scene_brother_walks_in_home_bathroom_madd_in_towel_groped_by_brother_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd weeping at left_small
    x "(He continues to grope me , squeezing my breast, strethcing them, making them bounce in his hands, and I can feel the tears streaming down my face)"
    show madd broken at left_small
    x "(Why is this happening to me? Why is my own brother doing this to me? )"
    show brother obsessed at right_small
    brother_says "Dont cry Maddie" 
    brother_says "Once i put a baby in you, I will do this everyday to milk you like a cow, and you will love it.."  
    show madd nauseated at left_small
    x "(He says that in a very creepy tone, and I can feel the disgust and fear building up inside me)"
    show madd horrified at left_small
    x "(The sheer audacity of him saying that to me, like he thinks I'm already his property )"
    show brother perverted at right_small
    brother_says "I will drink most of your milk even more than your baby will "
    show madd violated at left_small
    x "(This dude has serious issues, saying that to your own sister, like he's already planning on impregnating you and then drinking your breast milk like it's some kind of delicacy )"

    scene scene_brother_walks_in_home_bathroom_madd_in_towel_groped_by_brother_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show brother dominant at right_small
    x "(He says in angry tone again)"
    brother_says "Next time you tell me to stop, I will make sure you regret it..Say that you understand me Maddie.." 
    show madd trembling at left_small
    x "(I was so scared at this point that I just nodded my head in agreement )"
    show madd submissive nod at left_small
    show brother possessive at right_small
    brother_says "Good girl , hope you have a good day...Sooner or later your life will be all about pleasing me, and you will learn to love it.."
    show madd broken at left_small
    x "(He started mocking me again with these words while making me feel like I'm already his property, like I'm already his slave )"    
    show madd shaken at left_small
    x "(Finally he lets go of me and i sigh in relief, but the damage is already done, I can feel the humiliation and disgust still lingering in my mind)"
    show madd traumatized at left_small
    x "(the psychological damage of this encounter is going to stay with me for a long time , i dont know how to deal with it, i just want to forget it i ever lived here)"

    $ character_relations["brother"]["lust"] += 15
    $ character_relations["brother"]["intimacy"] +=5
    $ character_relations["brother"]["touched_madd"] += 3
    $ character_relations["brother"]["groped_madd"] += 3
    $ character_relations["brother"]["undressed_madd"] += 1
    $ character_relations["brother"]["friend"] += 1
    $ last_brother_talk_hour = game_time.hour
    $ madd_willpower = max(madd_willpower - 15, 0)
    $ journal_event_set_done("Brother", "Bathroom Ambush (Shower)")

    jump shower_nothing_happens_brother
    

label shower_nothing_happens_brother:
    show brother arrogant at right_small
    brother_says "Its nice seeing you...all dripping wet...but I have to go now. See ya later."
    
    show madd broken at left_small
    x "( I don't answer. I can't. I just stare at the floor as he leaves )"
    
    show madd self loathing at left_small
    x "( I need to leave this place. )"
    
    hide brother
    with dissolve

    $ character_relations["brother"]["lust"] += 5
    $ character_relations["brother"]["intimacy"] += 3
    
    $ madd_willpower = max(madd_willpower - 10, 0)
    call advance_time_and_check(minutes=120) from _call_advance_time_and_check_15
    
    jump home_areas



# ASK TO SLEEP IN  BROTHER SCENES AND RESEARCH THERE 


label ask_brother_to_sleep_in_room:
    scene expression brother_room_scene
    with fade
    
    show madd anxious at left_small
    with dissolve
    x "( The room is dark except for the glow of his gaming monitor. I can hear the sounds of gunfire and explosions from his headphones. )"
    
    show madd nervous at left_small
    x "( He gets up from his gaming chair, pulling off his headphones. The sudden silence feels oppressive. )"
    
    show madd worried at left_small
    x "( He reaches for the light switch. I flinch instinctively as the harsh fluorescent lights flood the room. )"
    
    scene ask_brother_to_sleep_in_room_standing_face_to_face
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd hesitant at left_small
    with dissolve
    x "( He's standing now, towering over me. His eyes scan me up and down. I feel exposed even though I'm fully clothed. )"
    
    show madd nervous at left_small
    x "Hey... um, brother?"
    
    show brother vindictive at right_small
    with dissolve
    brother_says "What now? Can't you see I'm busy?"
    
    show brother serious at right_small
    brother_thinks "( Interrupting my game for what? This better be important. )"
    
    show madd uncertain at left_small
    x "( My voice comes out smaller than I intended. Almost a whisper. )"
    
    show madd anxious at left_small
    x "I know, but... I was wondering if... maybe can i sleep here tonight?"
    
    show brother calculating at right_small
    brother_thinks "( She wants something from me... this is my chance. )"
    
    show brother predatory at right_small
    brother_thinks "( She's asking. Begging, really. That means I have leverage. )"
    
    scene ask_brother_to_sleep_in_room_standing_face_to_face_pull_and_neck_lick
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd shocked at left_small
    x "( Before I can react, before I can even blink, he reaches out and pulls me toward him. )"
    
    show madd paralyzed at left_small
    x "( His hands grip my waist with bruising force. I'm suddenly in his arms, chest pressed against him. )"
    
    show madd horrified at left_small
    x "( I can feel his heartbeat. Or is that mine? Everything is pounding, rushing. )"
    
    show brother possessive at right_small
    brother_thinks "( Got her. She came to me. She's asking for a favor. Perfect. )"
    
    show madd trembling at left_small
    x "( His face is moving closer, descending toward my neck. One hand releases my waist and tangles in my hair. )"
    
    show madd distressed at left_small
    x "( He grips my hair firmly, pulling it back. My head arches involuntarily. The position strains my neck muscles. )"
    
    show madd anxious at left_small
    x "( I tilt my head up instinctively, exposing my throat to him like prey surrendering to a predator. )"
    
    show madd conflicted at left_small
    x "( I'm not giving him access... I'm trying to avoid him reaching my face... but it looks like submission... like I'm offering myself to him... )"
    
    show brother amused at right_small
    brother_says "Why would you want that?"
    
    show brother smirk at right_small
    brother_thinks "( Look at her squirm. She needs me. She has nowhere else to go. )"
    
    show madd nervous at left_small
    x "( My throat is dry. The words come out hesitant, broken. )"
    
    show madd worried at left_small
    if brother_protects_madd_from_dad>0:
        x "Because..you defended me from dad...I feel safe when i am in room with you"
    else:
    
        x "Because... my door is locked and I don't want to sleep with step dad..."
    
    scene ask_brother_to_sleep_in_room_standing_face_to_face_pull_and_neck_lick_extended
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show brother possessive at right_small
    brother_thinks "( She's desperate. Trapped between dad and me. Nowhere to go. No escape. )"
    
    show brother lecherous at right_small
    brother_thinks "( The perfect prey. Cornered. Helpless. )"
    
    show madd shocked at left_small
    x "( I feel something wet on my neck. Something warm and slick sliding across my skin. )"
    
    show madd horrified at left_small
    x "( He's... he's licking my neck. His tongue traces a slow path from my collarbone upward. )"
    
    show madd nauseated at left_small
    x "( The wetness, the heat, the pressure of his mouth against my throat. I want to pull away but his grip is iron. )"
    
    show brother lecherous at right_small
    brother_thinks "( Her skin tastes sweet. Slightly salty from nervous sweat. The way she shivers when my tongue touches her... delicious. )"
    
    show madd distressed at left_small
    x "( I need to endure this. I need a place to sleep. I can't go back to dad's room. )"
    
    show madd resigned at left_small
    x "( This is still better than the alternative. Better than being with dad. This is just... licking. Just touching. I can survive this. )"
    
    show madd trembling at left_small
    x "( He pulls my hair even more back, forcing my head into an unnatural arch. My spine bends painfully. )"
    
    show madd paralyzed at left_small
    x "( He licks my neck aggressively now, his tongue pressing harder, his mouth almost sucking at my skin. )"

    show brother dominant at right_small
    brother_says "First of all, I sleep during the morning. So you can sleep here at night."
    
    show madd anxious at left_small
    x "( His breath is hot against my neck as he speaks. Each word sends puffs of warm air across my wet skin. )"
    
    show madd nervous at left_small
    x "Oh... okay... thank you—"
    
    show brother predatory at right_small
    brother_says "Wait, I'm not done."
    
    show brother smirk at right_small
    brother_thinks "( Not so fast. She doesn't get off that easy. There's more I want from her. )"
    
    scene ask_brother_to_sleep_in_room_standing_face_to_face_pull_and_neck_lick_extended_aggressive
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd shocked at left_small
    x "( I feel his teeth now. Sharp points pressing into the soft flesh of my neck. )"
    
    show madd horrified at left_small
    x "( He's biting me. Gently at first, but I can feel the threat of more pressure. More pain. )"
    
    show madd distressed at left_small
    x "( The sensation sends chills through my body. Cold rushes down my spine even as his mouth burns against me. )"
    
    show brother smirk at right_small
    brother_says "I play games at night. Pretty much all night. Keyboard clicking, mouse clicking, voice chat. It gets loud."
    
    show brother amused at right_small
    brother_thinks "( Let's see if she's desperate enough to accept even this. )"
    
    show madd trembling at left_small
    x "( His tongue traces along my neck again. From the bite mark upward toward my jaw. )"
    
    show madd anxious at left_small
    x "( I have to focus. Have to answer. Can't let him think I'm too affected. )"
    
    show madd nervous at left_small
    x "That's... that's fine. I can deal with some noise."
    
    show brother possessive at right_small
    brother_thinks "( She's accepting everything. The noise, my touch, my teeth on her skin. She's mine. )"
    
    show brother lecherous at right_small
    brother_says "If you're okay with that noise while you're trying to sleep, then sure. You can crash here at night."
    
    show madd relieved at left_small
    x "( Finally. A place to sleep. Away from dad. )"
    
    show madd shocked at left_small
    x "( He bites again. Harder this time. I feel his teeth sink in slightly. )"
    
    show madd trembling at left_small
    x "( He's marking me. Like an animal marking territory. The bite will leave a bruise. )"
    
    show madd hesitant at left_small
    x "Thank you... And... one more thing?"
    
    show brother fixated at right_small
    brother_says "What is it?"
    
    show brother think at right_small
    brother_thinks "( What else does she want? What else can I take from her? )"
    
    show madd nervous at left_small
    x "( His arms are still around me, holding me against him. I can feel every contour of his body. )"
    
    show madd anxious at left_small
    x "Since I'm staying here sometimes... would it be okay if I used your computer? Just for research when you're sleeping?"
    
    show brother mocking at right_small
    brother_thinks "( She wants to use my computer? That means she'll be spending even more time in my room. More opportunities. )"
    
    show brother calculating at right_small
    brother_thinks "( I can monitor what she researches. Control what she sees. Maybe even... )"
    
    scene ask_brother_to_sleep_in_room_standing_face_to_face_pull_and_kiss_initial
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd shocked at left_small
    x "( Suddenly I feel him shift. His face moves up from my neck. )"
    
    show madd paralyzed at left_small
    x "( His face is directly in front of mine now. So close I can see every pore, every eyelash. )"
    
    show madd distressed at left_small
    x "( His tongue emerges from his mouth, wet and glistening. It's moving toward my lips. )"
    
    show madd horrified at left_small
    x "( I had to accept it. Or I would be stuck with sleeping in dad's room, which I absolutely can't accept. )"
    
    show madd resigned at left_small
    x "( So I open my mouth for him to enter. Surrendering. Submitting. )"
    
    show madd nauseated at left_small
    x "( His tongue immediately enters my mouth. I can taste his saliva, metallic and warm. His breath washes over my face. )"
    
    show madd distressed at left_small
    x "( He's licking my whole mouth as if eating it whole. His tongue explores every surface - my teeth, my gums, the roof of my mouth. )"
    
    show madd trembling at left_small
    x "( He started licking the side of my lips, tracing the edges where lip meets skin. He's marking the whole area. )"   
    
    scene ask_brother_to_sleep_in_room_standing_face_to_face_pull_and_kiss_initial_extended
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd paralyzed at left_small
    x "( His tongue keeps circling around my lips, tracing every corner, every curve. Over and over. )"
    
    show brother lecherous at right_small
    brother_says "My computer, huh?"
    
    show brother amused at right_small
    brother_thinks "( She can barely speak with my tongue in her mouth. Perfect. )"
    
    show madd anxious at left_small
    x "( I try to answer clearly, but my voice is muffled, distorted. )"
    
    show madd nervous at left_small
    x "I mean, only when you're sleeping in the morning. I wouldn't touch it when you're gaming."
    
    show brother possessive at right_small
    brother_thinks "( More time in my room. More opportunities. This keeps getting better and better. )"
    
    show madd shocked at left_small
    x "( His tongue goes back inside my mouth, plunging deeper this time. )"
    
    show madd horrified at left_small
    x "( I can feel him licking the roof of my mouth, pressing against my teeth, trying to reach deeper. )"
    
    show madd nauseated at left_small
    x "( It's invasive. Violating. Like he's trying to consume me from the inside. )"
    
    show brother greedy at right_small
    brother_says "Fine. You can use it during the morning when I'm asleep. But don't mess with my settings or install anything weird."
    
    show brother lecherous at right_small
    brother_thinks "( I'll set up monitoring software later. Watch everything she does. )"
    
    show madd relieved at left_small
    x "I won't! I promise. Thank you so much, brother!"
    
    show brother dominant at right_small
    brother_thinks "( She's grateful. She's accepting my touch. She has no idea what she just agreed to. )"
    
    show brother possessive at right_small
    brother_thinks "( She's mine now. In my room, using my things, under my control. )"
    
    scene ask_brother_to_sleep_in_room_standing_face_to_face_pull_and_kiss_initial_extended_and_lick_neck
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd distressed at left_small
    x "( One final deep kiss. His tongue pressing against mine with almost painful force. )"
    
    show madd paralyzed at left_small
    x "( Then he pulls back and moves down again to my neck. His tongue lapping at the skin he already marked. )"
    
    show madd trembling at left_small
    x "( I can still taste him in my mouth. The wetness around my lips is starting to dry, sticky and uncomfortable. )"
    
    scene ask_brother_to_sleep_in_room_standing_face_to_face_pull_and_kiss_initial_extended_and_lick_neck_can_i_stay_tonight
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd anxious at left_small
    x "( He's licking me aggressively again, his tongue pressing hard against my throat. )"
    
    show madd distressed at left_small
    x "( He pulls my hair and arches my back once more. My spine screams in protest. This is the time to ask him. )"
    
    show madd nervous at left_small
    x "Please... can I stay tonight?"

    show brother dismissive at right_small
    brother_says "Yeah, yeah. Now go. I need to get back to my game."
    
    show brother manipulative at right_small
    brother_thinks "( I've got a raid starting in five minutes. But first... )"
    
    show madd shocked at left_small
    x "( As he said that, he immediately went after my lips with his tongue again, moving with sudden urgency. )"
    
    show madd paralyzed at left_small
    x "( Almost penetrating it with hurry, forcing his tongue as deep as it will go. )"
    
    scene ask_brother_to_sleep_in_room_standing_final_kiss
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd horrified at left_small
    x "( He had to get back to his game, so he's using this one last moment to fully consume me. )"
    
    show madd distressed at left_small
    x "( His tongue is deep inside me, reaching toward my throat. I gag slightly but he doesn't stop. )"
    
    show madd trembling at left_small
    x "( I couldn't help but moan slightly. A small sound of discomfort that he probably interprets as pleasure. )"

    show madd shocked at left_small
    x "( He releases me suddenly. The absence of his grip makes me stumble, my legs weak. )"
    
    show madd shaken at left_small
    x "( I catch myself against the doorframe, breathing hard. )"
    
    show madd processing at left_small
    x "( At least I have a place to sleep now. And access to a computer for research. That's what matters. )"
    
    show madd uncertain at left_small
    x "( But the feeling of his tongue on my neck, in my mouth. His teeth. His hands in my hair. )"
    
    show madd worried at left_small
    x "( What did I just agree to? What will he expect next time? )"
    
    show madd resigned at left_small
    x "( This is the price I have to pay. It's still better than the alternative. I keep telling myself that. )"
    
    # Set flag that Madd can now sleep in brother's room
    $ access_to_brother_room = True
    $ character_relations["brother"]["intimacy"] +=7
    $ character_relations["brother"]["kissed"] += 5
    $ character_relations["brother"]["touched_madd"] += 3
    $ character_relations["brother"]["friend"]+=5
    call advance_time_and_check(minutes=120) from _call_advance_time_and_check_16
    $ madd_willpower=max(madd_willpower-20,0)
    $ journal_event_set_done("Brother", "Ask to Sleep in Brother's Room")
    $ journal_event_show("Madd", "Redo Research: Cram School")
    $ journal_event_show("Brother", "Morning Claim")
    $ journal_event_show("Brother", "Wake Up: Full Claim")

    jump step_brother_room_scene


label step_brother_room_scene_brother_sleeping:
    scene scene_brother_room_morning_afternoon_brother_sleeping
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd nervous at left_small
    with dissolve
    x "( I need to be quiet this is not my room and he looks like he's still sleeping. )"
    
    "You are in your Step Brother's Room while he sleeps. You can see him breathing peacefully in his bed."
    
    menu:
        "Use his computer":
            call advance_time_and_check(minutes=10) from _call_advance_time_and_check_17
            jump use_brother_computer

        "Leave quietly":
            show madd relieved at left_small
            x "( I should go before I accidentally wake him up. )"
            jump home_areas


label use_brother_computer:
    scene scene_brother_room_morning_afternoon_madd_on_pc
    with fade
    
    show madd focused at left_small
    with dissolve
    x "( His computer is right here... what should I do? )"
    
    menu:
        "Research":
            if madd_willpower<=30:
                show madd stressed at left_small
                x "( My willpower is too low to focus on research right now... )"
                jump use_brother_computer
            else:
                jump research_cram_schools_brother
        
        "Check what he has on his PC":
            if madd_willpower<=30:
                show madd stressed at left_small
                x "( My willpower is too low to focus on that right now... )"
                jump use_brother_computer
            else:
                jump check_brother_pc_contents
        
        "Play games on his PC":
            jump play_games_brother_pc
        
        "Go back":
            jump step_brother_room_scene_brother_sleeping


label check_brother_pc_contents:
    scene scene_brother_room_morning_afternoon_madd_on_pc
    with fade
    
    show madd curious at left_small
    with dissolve
    x "( Let me see what kind of stuff he has on here... )"
    
    show madd uncertain at left_small
    x "( I open his folders... )"
    
    scene scene_brother_room_morning_afternoon_madd_on_pc_close_up_check_pc_content
    with fade

    show madd shocked at left_small
    x "( Oh... )"
    
    show madd processing at left_small
    x "( step sis stolen from step dad by step son , step brother impregnates step sis , step sis stuck in step bro's dorm... )"
    
    show madd resigned at left_small
    x "( Folders full of... that kind of content. )"
    
    show madd think at left_small
    x "( Am I shocked? )"
    
    show madd uncertain at left_small
    x "( Not really... given everything that's been happening... )"
    
    show madd sad at left_small
    x "( I guess this explains a lot about his behavior. )"
    
    show madd resigned at left_small
    x "( He's been fantasizing about this... about me... probably for a long time. )"
    
    show madd distressed at left_small
    x "( I close the folders quickly before I see anything more disturbing. )"
    
    $ character_relations["brother"]["intimacy"] += 1
    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_18
    $ madd_willpower=max(0,madd_willpower-30)
    $ character_relations["brother"]["friend"]+=1
    jump use_brother_computer


label play_games_brother_pc:
    scene scene_brother_room_morning_afternoon_madd_on_pc
    with fade
    
    show madd curious at left_small
    with dissolve
    x "( Let me see what games he has... )"
    
    show madd stand at left_small
    x "( I browse through his game library...I dont like any of them  )"
    
    show madd shocked at left_small
    x "(Let me search online games for female protagonist....)"
    x "(hmm What's this? 'X-Change Life'? )"
    
    show madd uncertain at left_small
    x "( Never heard of it... let me try it. )"
    
    "You launch the game and start playing..."
    
    $ game_time.advance_time(hours=1)
    
    show madd think at left_small
    x "( This game is...super interesting. It's about transformation and... )"
    
    show madd processing at left_small
    x "( Wait... what if... )"
    
    show madd stressed at left_small
    x "( What if I had been born a boy instead? )"
    
    show madd uncertain at left_small
    x "( What would my life have been like? )"
    
    show madd hopeful at left_small
    x "( And then... after Mom's death... )"
    
    show madd think at left_small
    x "( I managed to leave this place and go to a boys only dorm. )"
    
    show madd focused at left_small
    x "( Away from Step-dad. Away from his son. Finally free. )"
    
    show madd relieved at left_small
    x "( I could focus on my studies... become an engineer... make Mom proud... )"
    
    show madd stressed at left_small
    x "( But then... )"
    
    show madd uncertain at left_small
    x "( And then some rich douche who can afford expensive drugs drugged me... )"
    
    show madd shocked at left_small
    x "( Drugged me into becoming a girl... and somehow made it permanent. )"
    
    show madd horrified at left_small
    x "( My body... changed... reshaped... feminized... )"
    
    show madd distressed at left_small
    x "( And I couldn't reverse it. No matter what I tried. )"
    
    show madd trembling at left_small
    x "( Then Step-dad comes to visit me and finds out I'm a beautiful girl... )"
    
    show madd paralyzed at left_small
    x "( Similar to his dead wife... )"
    
    show madd nauseated at left_small
    x "( The way he would look at me... that recognition in his eyes... )"
    
    show madd anxious at left_small
    x "( And he starts getting more and more affectionate towards me. )"
    
    show madd violated at left_small
    x "( Not as a step-child... but as a replacement for her. )"
    
    show madd distressed at left_small
    x "( And then he actively visits me every weekend... )"
    
    show madd stressed at left_small
    x "( Trying to up the ante... pushing boundaries... demanding more... )"
    
    show madd horrified at left_small
    x "( And if I refuse... he would cut my funding... )"
    
    show madd helpless at left_small
    x "( Making it impossible for me to survive. )"
    
    show madd paralyzed at left_small
    x "( I'd have no money for food... for tuition... for anything. )"
    
    scene scene_brother_room_morning_afternoon_madd_on_pc_thoughts_after_game_1
    with fade

    show madd resigned at left_small
    x "( He would surely force me back home and then keep me here... )"
    
    show madd traumatized at left_small
    x "( Probably raw dog me every night until he was satisfied. )"
    
    scene scene_brother_room_morning_afternoon_madd_on_pc_thoughts_after_game_2
    with fade

    show madd broken at left_small
    x "( Night after night... claiming me... using me... )"
    
    show madd weeping at left_small
    x "( He would get back his beautiful wife... or a twisted version of her... )"
    
    scene scene_brother_room_morning_afternoon_madd_on_pc_thoughts_after_game_3
    with fade

    show madd violated at left_small
    x "( And also the satisfaction of making me submit. )"
    
    show madd self loathing at left_small
    x "( Of breaking me completely. Of owning me in every way possible. )"
    
    show madd anxious at left_small
    x "( No... no... what am I thinking? )"
    
    show madd stressed at left_small
    x "( This is too extreme... too brutal... )"
    
    show madd trembling at left_small
    x "( Even for them... right? )"
    
    show madd uncertain at left_small
    x "( But the game made it seem so... plausible... )"
    
    show madd distressed at left_small
    x "( I hope nothing like that happens... )"
    
    show madd determined at left_small
    x "( I need to stop playing this. I need to stop thinking about this. )"
    
    show madd focused at left_small
    x "( I quickly close the game and turn off the screen. )"
    
    scene scene_brother_room_morning_afternoon_madd_on_pc_thoughts_after_game_4
    with fade   

    show madd relieved at left_small
    x "( That was... disturbing. My imagination is running too wild. )"
    
    show madd resigned at left_small
    x "( I need to focus on reality... as terrible as it already is. )"

    x "( I close the game and got up from the desk. )"

    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_19
    $ madd_willpower=max(0,madd_willpower-30)
    $ character_relations["brother"]["intimacy"]+=1
    $ character_relations["brother"]["friend"]+=1
    
    jump step_brother_room_scene_brother_sleeping



label research_cram_schools_brother:
    scene scene_brother_room_morning_afternoon
    with fade
    show madd focused at left_small
    with dissolve
    x "Time to research cram schools. I need to find the best option for me to escape this situation and get into a good university."
    if research_cram_schools == 0:
        jump research_cram_schools_brother_1
    elif research_cram_schools == 1:
        jump research_cram_schools_brother_2
    elif research_cram_schools == 2:
        jump research_cram_schools_brother_3
    else:
        show madd think at left_small
        x "I've already researched everything I need about cram schools. So I will study other things now."
        $ madd_willpower_max += 5
        $madd_willpower=max(0,madd_willpower-30)
        jump step_brother_room_scene_brother_sleeping


label research_cram_schools_brother_1:
    
    scene scene_brother_room_morning_afternoon_madd_on_pc
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd focused at left_small
    x "I sit down at his computer and begin searching for the best cram schools in the area."
    
    show madd think at left_small
    x "( The screen glows... this is my way out. This is how I change my life. )"
    
    show madd uncertain at left_small
    x "My fingers move across the keyboard, clicking through websites and reviews. There are so many options..."
    
    # Brother starts snoring
    scene scene_brother_room_morning_afternoon_madd_on_pc_brother_snoring
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    
    show madd shocked at left_small
    x "( What... is that snoring? He's so loud! )"
    
    show madd distressed at left_small
    x "( How am I supposed to concentrate with this noise? )"
    
    show madd focused at left_small
    x "( ugh i need to focus on my research  )"
    
    show madd curious at left_small
    x "Each school has its own reputation, its own promises. But one name keeps appearing in every search result: Akira Cram School."
    
    show madd shocked at left_small
    x "( When I click on their page, the first thing that jumps out is their results. 98 Percent of their students get into top universities. 98 Percent is a lot! )"
    
    show madd hopeful at left_small
    x "They have state-of-the-art facilities, renowned instructors, a curriculum designed specifically for the university entrance exams..."
    
    show madd think at left_small
    x "( This is it. This is exactly what I need. A place that gets results. A place that could actually change my future. )"
    
    show madd worried at left_small
    x "But then I scroll down to the fees section and my heart sinks."
    
    scene scene_brother_room_morning_afternoon_madd_on_pc_madd_shocked_school_prices
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd horrified at left_small
    x "Entrance fee: 2,000 dollars. Monthly tuition: 500 dollars. Additional materials: 200 dollars."

    show madd distressed at left_small
    x "( 2,000 dollars just to start. I dont have that kind of money. My hands are trembling. )"
    
    show madd depressed at left_small
    x "I close that tab and search for female-only cram schools. There have to be cheaper options."
    
    show madd uncertain at left_small
    x "I find several female-only schools. They're cheaper - entrance fees around 800-1200 dollars. But when I look at their results..."
    
    show madd conflicted at left_small
    x "( Only 67 percent acceptance rate to top universities. Only 67 percent. That's a massive difference. )"
    
    show madd sad at left_small
    x "I stare at the screen for a long time, my mind racing with calculations. With the female schools, I'd have more money left over, but the quality is so much lower..."
    
    x "( What's the point of saving money if I don't actually make it into a good university? )"
    
    show madd think at left_small
    x "( Dad always said: 'If you're going to do something, do it right. Never settle for mediocre when you can have excellence.' )"
    
    show madd focused at left_small
    x "I'm going to do this. I'm going to get into the best school, the one with the best results, the one that actually matters."
    
    show madd angry at left_small
    x "( If I'm escaping this hellhole, I'm not doing it halfway. I'm going to make it count. )"


    show madd determined at left_small
    x "I'm going to enroll in the 2,000 dollars. I'm going to tough it out. But I need to get the money"
    
    show madd relieved at left_small
    x "( Like Dad said... if you're going to do it, do it right. )"
    
    show madd think at left_small
    x "The best costs the most. And I'm worth paying for."
    
    # Brother wakes up and approaches
    
    scene scene_brother_room_morning_afternoon_madd_on_pc_brother_standing_groping_madd
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd focused at left_small
    x "Now I need to find a place to stay near the school."
    
    show madd shocked at left_small
    x "( Wait... I feel something on my chest... )"
    


    # Remove headphones
    show madd horrified at left_small
    x "( I was shocked, I didnt notice him standing next to me )"
    

    scene scene_brother_room_morning_afternoon_madd_on_pc_brother_standing_groping_madd_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")


    show brother creepy at right_small
    with dissolve
    brother_says "Good morning, little sis."
    
    show madd paralyzed at left_small
    x "( He's standing right next to me! His hands are... they're on my breasts! )"
    
    brother_says "You looked so focused. I didn't want to disturb you."
    
    show madd distressed at left_small
    x "( His hands are running over my breasts through my clothes... squeezing them gently... )"
    
    brother_thinks "So soft... even through the fabric."
    
    show madd nervous at left_small
    x "I... I was just researching..."
    
    scene scene_brother_room_morning_afternoon_madd_on_pc_brother_standing_groping_madd_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    brother_says "Researching what? "
    
    show madd shocked at left_small
    x "( I cant tell him ! )"
    x "About benefits of chia seeds ."
    

    scene scene_brother_room_morning_afternoon_madd_on_pc_brother_standing_groping_madd_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    brother_says "Well i dont care , whatever."
    
    brother_says "As long as you keeps being a good girl for me."
    
    show madd distressed at left_small
    x "( His hands keep moving... I can feel his fingers tracing the outline of my breasts... )"
    
    $ madd_willpower = max(0, madd_willpower - 30)
    $ character_relations["brother"]["intimacy"] +=3
    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_20
    brother_says "You can use my computer anytime you want. Just remember... everything has a price."
    
    scene scene_brother_room_morning_afternoon_madd_on_pc_brother_standing_groping_madd_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show brother smirk at right_small
    brother_says "Now get back to your research. I'll leave you alone."
    
    hide brother
    with dissolve
    
    show madd distressed at left_small
    x "( My heart is pounding... I need to finish this and get out of here. )"
    
    $ research_cram_schools = 1
    $ stat_notification = "Research Progress: 1/3 - Chosen Akira Cram School"
    $ renpy.pause(2.0)
    $ stat_notification = ""
    $ character_relations["brother"]["groped_madd"] += 1
    $ character_relations["brother"]["touched_madd"] += 1
    $ character_relations["brother"]["friend"]+=1
    $ journal_event_set_done("Madd", "Redo Research: Cram School")
    $ journal_event_show("Madd", "Redo Research: Boys Hostel")
    
    jump step_brother_room_scene_brother_sleeping


label research_cram_schools_brother_2:
    
    scene scene_brother_room_morning_afternoon_madd_on_pc_close_up
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd uncertain at left_small
    x "I open the computer again. This time, I need to find a place to live near Akira Cram School."
    
    show madd think at left_small
    x "( If I have to commute for hours every day, I'll lose so much time. I need to be close. )"
    
    # Put on headphones immediately
    show madd focused at left_small
    x "(God will his snoring ever stop.. )"
    
    x "I search for hostels and shared housing near the school. The results flood in..."
    
    scene scene_brother_room_morning_afternoon_madd_on_pc_research_2_hostel_price_shock
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd shocked at left_small
    x "Girls-only hostels near the cram school: 800 dollars per month."
    
    show madd horrified at left_small
    x "( 800 dollars EVERY MONTH. That's... that's insane. )"
    
    show madd distressed at left_small
    x "I do the math in my head. If I pay for the cram school, I don't have any money. I can't afford 800 for rent."
    
    show madd paralyzed at left_small
    x "( Why is everything so expensive? How am I supposed to escape if every option is impossible? )"
    
    show madd uncertain at left_small
    x "I scroll down further in my search, almost mechanically. And then something catches my eye."
    
    scene scene_brother_room_morning_afternoon_madd_on_pc_research_2_hostel_price_shock_boys_hostel
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd shocked at left_small
    x "Boys-only hostels near the cram school."
    
    show madd think at left_small
    x "I click on the first one. The monthly rent: 200 dollars."
    
    show madd horrified at left_small
    x "( 200 dollars? That's... that's a quarter of the girls' hostels. How is that even possible? )"
    
    scene scene_brother_room_morning_afternoon_madd_on_pc_research_2_pass_as_boy_thought
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd conflicted at left_small
    x "( What if... what if I could pass as a boy? )"
    
    show madd think at left_small
    x " My hair is long... but I could hide it under a cap. The right clothes could hide my shape."
    
    show madd focused at left_small
    x "I need to do this. I need a fake certificate, a fake name, a fake identity."
    
    show madd determined at left_small
    x "I make my decision. I'm going to do this. I'm going to create a fake identity and live as a boy."
    
    # Brother approaches from behind
    scene scene_brother_room_morning_afternoon_madd_on_pc_research_2_brother_hand_on_hair
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd focused at left_small
    x "( Wait... what's that in my hair... )"
    
    show madd shocked at left_small
    x "( Hands... running through my hair... )"
    
    # Remove headphones
    show madd horrified at left_small
    x "( I know it's him. He's awake now, isn't he. )"
    
    show brother creepy at right_small
    with dissolve
    
    show madd paralyzed at left_small
    x "( He's standing right behind me. )"
    
    brother_says "Your hair is so soft."
    
    show madd paralyzed at left_small
    x "( His hands are on me... I'm frozen. )"
    
    scene scene_brother_room_morning_afternoon_madd_on_pc_research_2_brother_kiss_cheek
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd distressed at left_small
    x "( He's leaning down close... )"

    brother_says "Good morning, little sis."
    
    show madd distressed at left_small
    x "( He's leaning closer... his face is inches from mine... )"
    
    show madd nervous at left_small
    x "I... I'm just..."
    
    show madd shocked at left_small
    x "( He just kissed my cheek! )"
    
    show madd trembling at left_small
    x "( My heart is racing. This is how it starts. )"
    
    
    scene scene_brother_room_morning_afternoon_madd_on_pc_research_2_brother_kiss_lips
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show brother creepy at right_small
    brother_says "Such a good girl."
    
    show madd horrified at left_small
    x "( He's moving closer to my lips... his face is getting closer and closer... )"
    
    show madd paralyzed at left_small
    x "( His lips are on mine... )"
    
    show madd distressed at left_small
    x "( The kiss is harder now. More desperate. )"
    
    scene scene_brother_room_morning_afternoon_madd_on_pc_research_2_brother_kiss_lips_forced_standup
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd distressed at left_small
    x "( His tongue is forcing its way into my mouth... )"
    x "( His hands pull at my hair, making me stand up. My chair scrapes against the floor. )"

    show madd horrified at left_small
    x "( It's going deeper... all the way to my throat... I can't breathe... )"

    show madd paralyzed at left_small
    x "He then turns my head using the grip on my hair and starts licking my neck."
    
    show madd distressed at left_small
    x "( His tongue is wet and hot on my skin. I feel like I can't move. )"

    scene scene_brother_room_morning_afternoon_madd_on_pc_research_2_brother_licking_neck_with_bite
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd horrified at left_small
    x "(I feel his mouth on my neck... I can't stop him. )"
    x "(If I push him away, he'll kick me out. And then I'd have to sleep with Dad again. )"
    x "(So I just... freeze. Let him do what he wants. )"
    x "(He licks my neck harder, moving all over my skin. )"

    show madd shaken at left_small
    x "( This is real. This is happening. )"

    scene scene_brother_room_morning_afternoon_madd_on_pc_research_2_brother_licking_neck_with_bite_brother_comment
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd paralyzed at left_small
    x "(Now he's biting down... I want to pull away but I can't. )"

    show brother sadistic at right_small
    brother_says "So warm... so sweet..."
    
    show madd distressed at left_small
    x "( His mouth is all over me. I'm gagging. )"
    x "(I just realized... his hands have been on my chest this whole time. I was so focused on what he was doing to my neck that I didn't even notice. )"
    
    show madd trembling at left_small
    x "(His hands are all over me. He keeps licking and biting my neck, harder and harder. )"
    x "(The only sound I make is these broken moans... not because I like it, but because it's the only thing I can do. )"
    
    show madd shaken at left_small
    x "( My body is betraying me. Even though my mind is screaming, my body reacts. )"
    
    scene scene_brother_room_morning_afternoon_madd_on_pc_research_2_brother_licking_neck_back_to_kiss_comment
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd distressed at left_small
    x "(He pulls my head up and forces his lips on me again. )"
    
    show madd paralyzed at left_small
    x "(His tongue goes into my mouth. I don't fight. What's the point? They always get what they want. )"
    
    show madd helpless at left_small
    x "(He's breathing hard... like he's trying to swallow me whole. )"
    
    show madd violated at left_small
    x "(It doesn't hurt... not really. But the feeling... it's wrong. So wrong. )"
    
    show madd shaken at left_small
    x "(Finally he pulls away. )"
    
    # Brother pulls back
    show brother smirk at right_small
    brother_says "Mmm. You taste good in the morning."
    
    show madd paralyzed at left_small
    x "(I fall back into the chair. My legs are shaking. He was holding me up the whole time. )"
    x "( I can feel his taste in my mouth. His hands were all over me. )"

    show madd distressed at left_small
    x "( I'm gasping for air... my throat hurts... )"
    
    show madd trembling at left_small
    x "( I can still feel him on me. )"
    

    scene scene_brother_room_morning_afternoon_madd_on_pc_research_2_brother_leaves
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show brother possessive at right_small
    brother_says "Keep working on your research. I'll be watching."
    
    show madd distressed at left_small
    x "( Watching. He's always watching. )"
    
    hide brother
    with dissolve
    
    show madd distressed at left_small
    x "( My whole body is shaking... I need to finish this... )"
    
    show madd focused at left_small
    x "( I turn back to the computer. My hands won't stop trembling. As i hear the bed croak , he must have gotten back in bed. )"
    
    x "(I finish my research as i get up from the computer back in his room.)"
    $ research_cram_schools = 2
    $ stat_notification = "Research Progress: 2/3 - Found boys hostel, committed to plan"
    $ renpy.pause(2.0)
    $ stat_notification = ""
    $ madd_willpower = max(0, madd_willpower - 30)
    $ character_relations["brother"]["intimacy"] += 5
    $ character_relations["brother"]["kissed"] += 3
    $ character_relations["brother"]["touched_madd"] += 1
    $ character_relations["brother"]["groped_madd"] += 1
    $ character_relations["brother"]["friend"]+=2
    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_21
    $ journal_event_set_done("Madd", "Redo Research: Boys Hostel")
    $ journal_event_show("Madd", "Redo Research: Escape Budget")
    
    jump step_brother_room_scene_brother_sleeping

label research_cram_schools_brother_3:
    
    scene scene_brother_room_morning_afternoon_madd_on_pc_close_up
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd think at left_small
    with dissolve
    x "I pull out my notebook and a calculator. It's time to see if this plan is actually feasible."
    
    show madd nervous at left_small
    with dissolve
    x "( My hands are trembling as I write. If the numbers don't work out... there's no plan. There's no escape. )"
    
    # Put on headphones immediately


    scene scene_brother_room_morning_afternoon_r3_calculating_costs
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")


    show madd focused at left_small
    with dissolve
    x "Let me break down the numbers. Everything depends on this calculation."
    
    show madd uncertain at left_small
    with dissolve
    x "Cram school entrance fee: 2,000 dollars."
    
    show madd worried at left_small
    with dissolve
    x "Boys-only hostel rent per month: 200 dollars. But they'll want a deposit first."
    
    show madd distressed at left_small
    with dissolve
    x "A deposit is typically 2-4 months worth of rent. So that's 400 to 800 dollars."
    
    show madd think at left_small
    with dissolve
    x "( Let's calculate conservatively. 2,000 for cram school + 800 for hostel deposit = 2,800 dollars minimum. )"
    
    scene scene_brother_room_morning_afternoon_r3_how_to_get_2800_dollars
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd horrified at left_small
    with dissolve
    x "That's 2,800 dollars just to get started."
    
    show madd paralyzed at left_small
    with dissolve
    x "( I only have [madd_money] dollars right now. I need [2800 - madd_money] more. I am completely broke! )"
    
    show madd focused at left_small
    with dissolve
    x "So the critical amount is 2,800 dollars. That's my target. That's my escape fund."
    
    show madd distressed at left_small
    with dissolve
    x "( How am I supposed to get 2,800 dollars? )"
    
    show madd think at left_small
    with dissolve
    x "I know there's money hidden in the house. Not much, but maybe enough. My stepfather keeps extra cash hidden in different places."
    
    show madd conflicted at left_small
    with dissolve
    x "( Am I really going to steal from him? What choice do I have? )"
    
    scene scene_brother_room_morning_afternoon_r3_determined_to_leave
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd determined at left_small
    with dissolve
    x "I make my decision. I will find the money and I will steal it if I have to."
    
    show madd determined at left_small
    with dissolve
    x "( I'm not a thief. But I'm also not going to waste away in this house. )"
    x "I need at least 2,800 dollars to escape. My stepfather has hidden money around this house. I just need to find it."
    
    show madd anxious at left_small
    with dissolve
    x "( First, I need to find where he's kept it. That's going to be risky. )"
    
    show madd worried at left_small
    with dissolve
    x "But there's still the matter of getting there. The hostel is 20-30 kilometers away."
    
    show madd think at left_small
    with dissolve
    x "( Can I take a bus? No... that costs money. Money I need for the deposit and school. )"
    
    show madd resigned at left_small
    with dissolve
    x "That leaves only one option: I walk."
    
    show madd nervous at left_small
    with dissolve
    x "( 20-30 kilometers on foot. Carrying a backpack with everything I own. In the summer sun. )"
    
    # Brother approaches
    scene scene_brother_room_morning_afternoon_r3_brother_approaches_madd_standing
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd uncertain at left_small
    with dissolve
    x "( Suddenly... I feel something. A shadow. A presence. )"
    
    show madd shocked at left_small
    with dissolve
    x "( I feel hands on my shoulders... )"
    
    show madd shocked at left_small
    with dissolve
    x "( No... not again... )"

    
    show brother creepy at right_small
    with dissolve
    
    show madd paralyzed at left_small
    with dissolve
    x "( He's standing right next to me... His body is warm. Too warm. )"
    
    brother_says "Finished with your research ?"
    
    show madd distressed at left_small
    with dissolve
    x "I... I'm almost done..."
    x "( My voice comes out smaller than I intended. )"
    
    show brother possessive at right_small
    with dissolve
    x "( I can feel him smiling behind me. That awful, satisfied smile. )"
    
    scene scene_brother_room_morning_afternoon_r3_brother_inital_kiss
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show brother dominant at right_small
    with dissolve
    brother_says "Good. Because it's time for you to repay me."
    
    show madd shocked at left_small
    with dissolve
    x "( What? )"
    x "( There's no time to process what he means. )"
    
    # Brother kisses her with tongue
    show madd horrified at left_small
    with dissolve
    x "( His lips are on mine again... his tongue forcing its way in... )"
    x "( I taste cigarettes. Alcohol. Him. )"
    
    scene scene_brother_room_morning_afternoon_r3_brother_inital_kiss_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")


    brother_thinks "She knows what's coming. She's not even fighting anymore."
    
    show madd paralyzed at left_small
    with dissolve
    x "( His tongue is deep in my mouth... I can't breathe... )"
    
    # Brother pulls back
    show brother creepy at right_small
    with dissolve
    x "( I can finally breathe, but the air still feels contaminated with him. )"
    
    show madd distressed at left_small
    with dissolve
    x "( Finally... he pulled back... I need air... )"
    
    # Brother starts lowering his jeans
    scene scene_brother_room_morning_afternoon_r3_brother_pull_madd_lower_jeans
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show brother dominant at right_small
    with dissolve
    show madd shocked at left_small
    with dissolve
    
    brother_says "Now for the real payment."
    x "( His voice is different now. Colder. More commanding. )"
    
    show madd horrified at left_small
    with dissolve
    x "(As soon as he says that, he pulls me by my hair. There's no gentleness in it. Just possession.)"
    x "(Leading me closer to his body. Now my body is right next to his crotch.)"
    

    show madd paralyzed at left_small
    with dissolve
    x "( Then he starts unbuttoning his pants and lowering it . Slowly but surely i see his thick dick. )"
    
    scene scene_brother_room_morning_afternoon_r3_brother_pull_madd_lower_jeans_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    with dissolve
    x "(I was close enough to sense the heat coming from his pants and the smell was overwhelming ! But something about that smell made me want to lean in closer to his pants.)"    
    x "(I saw his thick dick in its full glory , it was massive ! )"


    show brother possessive at right_small
    with dissolve
    brother_says "You've been using my room, my computer, my protection. Everything has a price."
    
    show madd distressed at left_small
    with dissolve
    x "I... I don't..."
    
    # Brother roughly guides her face
    show madd shocked at left_small
    with dissolve
    x "( His hand is on the back of my head... he's pushing me down... )"
    x "( I can't move. There's nowhere to go but where he wants me to )"
    
    show brother cruel at right_small
    with dissolve
    brother_says "I helped you stay in my room. I let you use my things. It's your duty to obey the room owner's demands."
    
    show brother possessive at right_small
    with dissolve
    brother_says "You should learn to please the man that provides for you."
    x "( His voice is matter-of-fact. Like he's explaining a basic fact of life. )"
    
    show madd horrified at left_small
    with dissolve
    x "( He's guiding my face toward his dick.)"
    x "( The heat is more intense now. The smell is suffocating. )"
    
    show madd paralyzed at left_small
    with dissolve
    x "( The smell... it's so strong... I don't want to... )"
    
    show brother dominant at right_small
    with dissolve
    brother_says "Open your mouth."
    
    show madd distressed at left_small
    with dissolve
    x "( I... I can't... )"
    x "( I don't want this. Every part of me is screaming no. )"
    
    show brother dominant at right_small
    with dissolve
    brother_says "I said open your mouth. Unless you want to sleep in the hallway again?"
    
    show madd nervous at left_small
    with dissolve
    x "( He'll... he'll kick me out of his room... )"
    x "( And if I don't have his room, I don't have a place to hide from Dad. )"
    
    show madd conflicted at left_small
    with dissolve
    x "( I... I have to... )"
    x "( The thought sickens me, but the alternative is worse. )"
    
    scene scene_brother_room_morning_afternoon_r3_brother_forcing_dick_deep_in_madd_mouth
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")  
    # Madd reluctantly complies
    show madd horrified at left_small
    with dissolve
    x "( I... I open my mouth... )"
    x "( It feels like I'm betraying myself. Like I'm giving him permission. )"
    
    show brother dominant at right_small
    with dissolve
    brother_says "Good girl. Now start."
    x "( That tone again. Like I'm a pet he's training. )"
    
    show madd distressed at left_small
    with dissolve
    x "( The smell... it's overwhelming... but I have to do this... )"
    x "( I move my head forward. Just an inch at first. )"
    
    show brother obsessed at right_small
    with dissolve
    brother_thinks "So obedient. She's learning fast."
    
    show madd paralyzed at left_small
    with dissolve
    x "( I... I start moving... )"
    x "( Slow. Mechanical. Like I'm watching someone else do this. )"
    
    show brother obsessed at right_small
    with dissolve
    brother_says "That's it. Just like that."
    x "( Encouraging. Like I'm doing well. Like this is something to be proud of. )"
    
    show madd horrified at left_small
    with dissolve
    x "( I can taste... it's so bitter... )"
    x "( Salt and something else. Something distinctly him. )"
    
    show brother obsessed at right_small
    with dissolve
    brother_thinks "She's actually doing it. She's mine now."
    x "( His hand grips my hair tighter. More possessive. )"
    
    show madd distressed at left_small
    with dissolve
    x "( Please... let this be over soon... )"
    x "( My eyes are watering. Tears are mixing with everything else. )"
    
    show brother obsessed at right_small
    with dissolve
    brother_says "I'm gonna go all the way."
    x "( A promise. Or a threat. I'm not sure anymore. )"
    
    scene scene_brother_room_morning_afternoon_r3_brother_forcing_dick_deep_in_madd_mouth_deeper
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd paralyzed at left_small
    with dissolve
    x "( His hand is gripping my hair... forcing the rhythm... )"
    x "( He's controlling everything. My pace. My breathing. How deep I go. )"
    
    show brother obsessed at right_small
    with dissolve
    brother_says "God this feels so good. If you wake me up with this I will let you stay forever."
    x "( A deal with the devil. Except the devil is my brother. )"
    
    show madd paralyzed at left_small
    with dissolve
    x "(He kept fucking my mouth. I had no choice but to endure. My face buried in his crotch. The only thing I could breathe was his pheromones.)"
    x "(It's overwhelming. Invasive. I'm drowning in him.)"
    
    scene scene_brother_room_morning_afternoon_r3_brother_forcing_dick_deep_in_madd_mouth_deeper_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd paralyzed at left_small
    with dissolve
    x "(He was using his hand on the back of my head to ensure his cock goes all the way in, touching the back of my throat.)"
    x "(The reflex kicks in automatically. My body wants to reject him. But I force it down. My face was slamming in his crotch and his scrotum each time he pushed my head all the way down.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(Not sure if it was the pheromones rushing in my system or the power dynamics of him blackmailing me to suck his dick... but I can't deny I was a bit turned on by the whole ordeal.)"
    x "(The realization makes me hate myself even more.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I felt his cock getting bigger in my mouth. I know what that means. He's getting close.)"
    x "(I knew he was at his limit and about to... to drown me in his cum at any minute now.)"

    scene scene_brother_room_morning_afternoon_r3_brother_forcing_dick_deep_in_madd_mouth_deeper_cum
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd horrified at left_small
    with dissolve
    x "( No... he's going to make me drink it all, isn't he? Why do all men want that? )"
    x "( Is this what being a woman means? Being a vessel? )"
    

    # Brother finishes
    show brother obsessed at right_small
    with dissolve
    brother_says "Swallow it all."
    x "( Not a request. A command. )"
    
    show madd distressed at left_small
    with dissolve
    x "(As soon as he said it, I felt hot streams running in my mouth. It was viscous, salty, and something else.)"
    x "(It's too much. Way too much.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "( I didn't hate the taste completely, but the amount was so much it was leaking out of my mouth.)"
    x "( The reality hits me. I'm swallowing my brother's cum. This is really happening. )"
    x "( I... I can feel it... in my mouth... it's so thick... )"
    
    show brother obsessed at right_small
    with dissolve
    brother_thinks "Perfect. She swallowed every drop."
    x "( He's watching. Observing every reaction. Recording this moment in his mind. )"
    
    show madd distressed at left_small
    with dissolve
    x "( I'm gagging... but I force myself to swallow... )"
    x "( The taste lingers. I can still feel it coating my throat. )"

    # Brother pulls back
    show brother obsessed at right_small
    with dissolve
    x "( He steps back like he's admiring his work. )"
    
    show brother possessive at right_small
    with dissolve
    brother_says "Good girl. You're learning your place."
    x "( My place. Beneath him. Serving him. )"
    
    show madd paralyzed at left_small
    with dissolve
    x "( I'm gasping... coughing... the taste won't go away... )"
    x "( I can still feel him. Taste him. I don't think I'll ever be clean again. )"
    
    show brother possessive at right_small
    with dissolve
    brother_says "You can use my room and computer anytime you want. As long as you remember who owns this room."
    x "( The price tag on everything. That's what he's saying. )"
    
    scene scene_brother_room_morning_afternoon_r3_aftermath_cum_on_madd
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show brother cruel at right_small
    with dissolve
    brother_says "Now clean yourself up and finish your research."
    x "( Dismissed. Like I'm a used toy. He then pulls up his pants as i reset my position on chair but there is cum in my mouth , my hair , my shirt. I was marked by him. )"
    x "(As he pulls my face closer to his one last time .)"
    show brother dominant at right_small
    with dissolve
    brother_says "Remember this juice of love i gave you , I will give you lots of my juice the longer you stay in my room darling ."

    hide brother
    with dissolve

    x "(With that he went back to his bed .)"

    show madd paralyzed at left_small
    with dissolve
    x "( My throat hurts... my jaw aches... I feel sick... )"
    x "( I'm disgusted with myself. With my body. With what I just did. )"
    
    show madd paralyzed at left_small
    with dissolve
    x "( But I got what I needed. I have my plan. I just need to execute it. )"
    x "( Swallowing the shame. The humiliation. Pushing it down. )"
    
    show madd conflicted at left_small
    with dissolve
    x "( 2,800 dollars. That's all I need. Then I'm gone from this nightmare. )"
    x "( And I'll never have to do anything like this again. )"
    
    $ research_cram_schools = 3
    $ stat_notification = "Research Progress: 3/3 - Full escape plan complete"
    $ renpy.pause(2.0)
    $ stat_notification = ""
    $ madd_willpower = max(0, madd_willpower - 30)
    $ character_relations["brother"]["intimacy"] +=7
    $ character_relations["brother"]["kissed"] += 1
    $ character_relations["brother"]["touched_madd"] += 1
    $ character_relations["brother"]["oral_sex"] += 1
    $ character_relations["brother"]["friend"]+=5
    $ character_relations["brother"]["lust"] = 0
    $ character_relations["brother"]["anger"] = 0
    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_22
    $ journal_event_set_done("Madd", "Redo Research: Escape Budget")
    $ journal_event_show("Brother", "Escape Night")
    
    jump step_brother_room_scene_brother_sleeping


# RUNAWAY FROM HOME BROTHER SCENES 



label runaway_from_brother_room:
    scene expression brother_room_scene
    with fade
    show madd determined at left_small
    x "( I've reached my breaking point. With my plan in place and the funds secured, it's time to escape this hell. )"
    show madd focused at left_small
    x "( This is my only chance—my final opportunity to reclaim my life and future. )"
    x "(I waited till nightfall )"
    
    scene scene_brother_room_madd_sleep_sitting_on_bed
    with fade

    show madd anxious at left_small
    x "( But I need to complete my cram school enrollment and finalize the payment first. )"
    
    show madd nervous at left_small
    x "( I'll have to ask him for access to his computer... )"

    if game_time.is_evening():
        $ hours_to_night = 24 - game_time.hour
        call advance_time_and_check(hours=hours_to_night) from _call_advance_time_and_check_23
    elif 20 <= game_time.hour < 24:
        $ hours_to_late_night = 24 - game_time.hour
        call advance_time_and_check(hours=hours_to_late_night) from _call_advance_time_and_check_24
    # If between 00:00 and 03:59, do nothing

    scene scene_runaway_from_brother_room_stand_next_to_brother_1
    with Dissolve(2.0)

    show brother calculating at right_small
    with dissolve

    x "(I approach him carefully—he's absorbed in an FPS game, his fingers moving rapidly across the keyboard.)"

    show madd hesitant at left_small
    x "Um... brother? Can I use your computer for a bit? It's really important."
    
    show brother dismissive at right_small
    brother_says "Not now. I'm in the middle of an important ranked match."
    
    scene scene_runaway_from_brother_room_stand_next_to_brother_2
    with fade

    show madd worried at left_small
    x "Please, it's urgent. I really need just a few minutes—"
    
    show brother angry at right_small
    brother_says "Nothing is more important than this. Leave me alone."
    
    show madd sad at left_small
    x "..."
    
    x "( I look down, my hands trembling with desperation and frustration. )"
    
    show brother think at right_small
    brother_says "..."
    
    brother_thinks "( She looks so desperate... I could use this situation to my advantage. )"
    
    show brother smirk at right_small
    brother_says "...Actually, fine. But come sit on my lap while you use it."
    
    show madd shocked at left_small
    x "( What...? That's... But I need to do this... What choice do I have? )"
    
    show madd resigned at left_small
    x "( If this is the price I have to pay for escape, then so be it. )"
    
    scene scene_runaway_from_brother_room_stand_next_to_brother_3
    with fade    

    show brother dominant at right_small
    brother_says "You heard me—on my lap. That's the deal."
    
    show madd anxious at left_small
    x "O...okay... I don't have a choice, do I?"
    
    x "(He pulls me close with surprising strength, lifting me effortlessly and settling me onto his lap.)"
    
    show madd shocked at left_small
    x "( Oh! )"
    
    scene scene_runaway_from_brother_room_sitting_on_brother_lap_1
    with fade

    show madd focused at left_small
    x "(I force myself to focus on the task at hand, navigating to the cram school's website while his hands begin to wander across my body.)"

    x "Please , let me finish this first.."

    show madd worried at left_small
    x "(This is my final night here. I need to complete this before I leave forever.)"

    x "(Without hesitation, he brushes my hair aside, exposing my neck directly.)"
    
    show brother possessive at right_small
    brother_says "Like i care"
    
    show madd paralyzed at left_small
    x "(I feel his wet tongue against my skin immediately—hot, insistent, claiming.)"
    x "(So this is how it works: access granted in exchange for my body. A fair transaction, I suppose.)"
    x "(As long as he doesn't take things further, I can endure this and finish the enrollment.)"

    scene scene_runaway_from_brother_room_sitting_on_brother_lap_2
    with fade
    
    show madd focused at left_small
    x "(I push forward with the application, clicking through required fields while my brother continues his assault on my neck.)"
    
    show madd uncertain at left_small
    x "Almost there..."
    
    x "(His saliva coats my neck, and the bitter scent of his body fills my nostrils. It's revolting, yet I force myself to remain composed.)"
    
    show madd stressed at left_small
    x "(There are moments when his aggression intensifies, and I must pause to regain control—to prevent myself from succumbing to panic or worse, acceptance.)"
    
    show madd focused at left_small
    x "(Just a bit longer... I'm almost done.)"

    scene scene_runaway_from_brother_room_sitting_on_brother_lap_3
    with fade
    
    show madd determined at left_small
    $ madd_money -= 2000
    $ paid_school_fees = True
    x "(With a final click, I confirm the payment. Two thousand dollars transferred. My tuition is secured.)"
    
    show madd relieved at left_small
    x "It's... it's finished."
    
    x "(It's done. My years of planning, my research, my sacrifice—it all culminates in this moment. I've officially enrolled in Akira Cram School. My path to freedom is now cemented.)"
    
    x "(By now, my brother has moved his hands to my chest, groping through my clothes. I'm too drained from everything to resist properly anymore.)"
    
    show madd resigned at left_small
    x "(Let him have his moment. After tonight, he won't see me again. This is the final toll I'll pay in this house.)"
    
    show madd hopeful at left_small
    x "(Despite everything that's happened here, I feel a strange sense of accomplishment welling inside me. )"
    
    show madd think at left_small
    x "(My brother may be twisted, but he isn't pure cruelty like my father. There's some small redeeming quality in him—a difference I've come to recognize.)"

    scene scene_runaway_from_brother_room_sitting_on_brother_lap_get_up_kiss
    with fade

    show madd relieved at left_small
    x "(I carefully push myself up from his lap, and surprisingly, he doesn't resist.)"
    
    x "(I lean down and kiss his cheek softly—a genuine gesture of gratitude.)"
    
    show madd submissive nod at left_small
    x "Thank you for all you've done for me."
    
    x "(If I had been alone with my father in this house, I'd have been nothing but a vessel for his deranged desires by now. At least my brother provided shelter and resources, even if the price was my dignity.)"
    
    show brother shocked at right_small
    brother_thinks "( What... what is this feeling coursing through me? )"
    
    show brother think at right_small
    brother_thinks "( She's... she's so beautiful. What have I been doing to her all this time? )"
    
    show madd uncertain at left_small
    x "(I notice embarrassment coloring his face. He looks almost... vulnerable. Does he genuinely feel remorse?)"

    scene scene_runaway_from_brother_room_sitting_on_brother_apologizes
    with fade
    
    show brother think at right_small
    brother_thinks "( I've wasted my entire life as an outcast, and I've taken my bitterness out on this poor girl who lost her mother. )"
    
    show brother serious at right_small
    brother_thinks "( She's grieving and suffering under our father's abuse, and I've only added to her pain. I've been terrible to her. )"
    
    show brother shocked at right_small
    brother_says "Maddie..."
    
    show brother obsessed at right_small
    brother_says "Maddie im sorry for all ive done to you"
    
    show madd shocked at left_small
    x "( Is he apologizing? Does my innocent gesture of gratitude trigger actual guilt in him? )"
    
    x "( Perhaps he's never experienced genuine affection or appreciation. Maybe his twisted behavior stems from deep loneliness rather than pure malice. )"
    
    show madd conflicted at left_small
    x "( I feel an unexpected pang of sympathy for him—pathetic as he is. )"
    
    show brother serious at right_small
    brother_says "I've done such horrible things to you..."
    
    show madd uncertain at left_small
    x "( He sounds genuinely remorseful. Maybe... maybe I should accept his apology. )"
    
    show madd relieved at left_small
    x "It's okay. You've also helped me when I had nowhere else to turn."
    
    show madd happy at left_small
    x "I forgive you."
    
    x "(I give him my best smile, and I see moisture glistening in his eyes. He's actually crying.)"
    
    scene scene_runaway_from_brother_room_sitting_on_brother_where_are_you_going
    with fade
    
    show brother think at right_small
    brother_thinks "( No... no, I can't soften now. Not after everything. I have to maintain control. )"
    
    show brother dominant at right_small
    brother_thinks "( The world respects power and dominance, not kindness. My father proved that by keeping a woman like her interested. )"
    
    show brother calculating at right_small
    brother_thinks "( If I want someone like Maddie, I need to be the dominant one. Gentleness gets nowhere. )"
    
    show madd confused at left_small
    x "( His expression suddenly hardens. What just happened to him? )"
    
    x "( Well, regardless—I need to prepare. It's time to leave this place. )"
    
    show brother possessive at right_small
    brother_says "Where exactly do you think you're going?"
    
    show madd shocked at left_small
    x "What?"
    
    x "(The sudden shift in his tone—from apologetic to commanding—catches me off guard as he pulls me back onto his lap with surprising force.)"
    
    show madd paralyzed at left_small
    x "(I'm now facing him directly, our bodies pressed uncomfortably close. This position makes me feel impossibly vulnerable.)"
    
    show brother dominant at right_small
    x "(His hands grip my waist firmly, preventing any attempt to escape.)"

    scene scene_runaway_from_brother_room_sitting_on_brother_lap_facing_him_face_lick_1
    with fade
    
    show madd distressed at left_small
    x "( My voice drops to barely a whisper. I can sense the shift—he's no longer remorseful. What triggered this sudden change? )"
    
    show madd trembling at left_small
    x "W-what are you doing?"
    
    x "( He doesn't answer. Instead, his lips find my face, and I feel his hot breath against my skin. )"
    
    show madd horrified at left_small
    x "( His wet tongue follows, and it's not long before he's forcing it into my mouth, claiming me without permission. )"
    
    scene scene_runaway_from_brother_room_sitting_on_brother_lap_facing_him_face_lick_2
    with fade

    show madd paralyzed at left_small
    x "( I can taste the saliva dripping from his tongue directly into my mouth. He tastes bitter, invasive. )"
    
    x "( I try to turn my head away, to create distance, but he follows my movement, closing the gap immediately. )"
    
    show madd anxious at left_small
    x "( I can't make a sound—not now, not with my father sleeping somewhere in this house. If he wakes up and finds me like this, I'll be trapped here forever. )"
    
    show madd resigned at left_small
    x "( So I stop fighting. It's my last night anyway. Let him take what he wants. )"
    
    scene scene_runaway_from_brother_room_sitting_on_brother_lap_facing_him_face_lick_3
    with fade

    show madd distressed at left_small
    x "( He continues licking my face while I desperately try to maintain some distance between us. )"
    
    show madd paralyzed at left_small
    x "( His hand gradually moves to the back of my head, pressing me closer, trapping me in his assault. )"
    
    show madd helpless at left_small
    x "( I'm a prey caught in the jaws of a predator, being devoured alive. There's no escape. )"
    
    x "( The room is silent except for my soft, involuntary moans and the wet sound of his tongue against mine. )"
    
    show madd violated at left_small
    x "( This is utterly humiliating. )"
    
    x "( After what feels like an eternity, he finally stops. )"
    
    scene scene_runaway_from_brother_room_sitting_on_brother_lap_facing_him_neck_lick_1
    with fade
    
    show madd shocked at left_small
    x "( Without warning, his hand grips my hair, jerking my head back sharply. My neck is suddenly exposed and vulnerable. )"
    
    show madd distressed at left_small
    x "( His tongue strikes my neck immediately—hot, wet, and relentless. )"
    
    x "( His saliva coats my skin, spreading across my entire neck. )"
    
    show madd overwhelmed at left_small
    x "( It's not just the physical sensation—his scent fills my nostrils, overwhelming my senses and filling the entire room. )"
    
    scene scene_runaway_from_brother_room_sitting_on_brother_lap_facing_him_neck_lick_2
    with fade
    
    show madd shaken at left_small
    x "( He finally releases my hair and pulls me into an embrace, like a lover would. His lips continue their assault on my neck. )"
    
    show madd anxious at left_small
    x "( I'm growing tired of resisting. My strength is fading. )"
    
    scene scene_runaway_from_brother_room_sitting_on_brother_lap_facing_him_neck_lick_3
    with fade
    
    show madd resigned at left_small
    x "( At this point, I simply surrender. I close my eyes as he pulls my hair again, raising my neck higher. )"
    
    show madd anxious at left_small
    x "( He licks my face one more time before returning to my neck. I'm too drained to fight anymore. )"
    
    show madd focused at left_small
    x "( I need to preserve my energy for the escape. That's what matters. )"
    
    x "( After an eternity, he finally stops. )"

    scene scene_runaway_from_brother_room_sitting_on_brother_lap_facing_him_lift_shirt_madd_top_naked
    with fade
    
    show madd nervous at left_small
    x "( He stares at me intensely, his eyes burning with hunger. )"
    
    show madd anxious at left_small
    x "( His hands move down to the hem of my shirt and begin to lift it. )"
    
    show madd paralyzed at left_small
    x "( I freeze. My body won't obey my mental commands to resist. )"
    
    show madd resigned at left_small
    x "( I'm too exhausted to fight, and I need to conserve my remaining strength for what comes after. So I lift my shirt just enough to ease his way. )"
    
    x "( He exposes my entire chest to the cool air of the room. )"
    
    show madd shocked at left_small
    x "( He's smiling like a child on Christmas morning, looking at my breasts like they're the greatest treasure he's ever found. )"

    scene scene_runaway_from_brother_room_sitting_on_brother_lap_facing_him_lift_shirt_madd_top_naked_first_lick_boobs_1
    with fade
    
    show madd distressed at left_small
    x "( Without hesitation, he lowers his head and begins to kiss my breasts. )"
    
    show madd trembling at left_small
    x "( His kisses start soft and gentle, but quickly become more passionate and demanding as he kisses every surface. )"
    
    show madd conflicted at left_small
    x "( I feel his tongue licking my nipples, making them harden despite my disgust. I can't help but moan softly. )"
    
    x "( I can sense his intense enjoyment—he continues licking and sucking like he's consuming something sacred. )"
    
    show madd processing at left_small
    x "( He mumbles something unintelligible while he does this. I strain to hear... is he saying 'mother'? )"
    
    show madd shocked at left_small
    x "( Wait... is that it? Does he associate my breasts with maternal comfort? Was he raised without a mother figure? )"
    
    scene scene_runaway_from_brother_room_sitting_on_brother_lap_facing_him_lift_shirt_madd_top_naked_first_lick_boobs_2
    with fade    
    
    show madd distressed at left_small
    x "( Now he's clamping my breasts with both hands, squeezing hard while his tongue continues its assault. )"
    
    show madd paralyzed at left_small
    x "( He's sucking them desperately, as if they're his only source of sustenance. His tongue swirls around my nipples, making them impossibly harder. )"
    
    x "( If I were lactating, I'm certain he would drain me completely. )"
    
    show madd violated at left_small
    x "( Here I am, in the middle of the night, in my brother's room, getting my breasts sucked by him. This is my reality now. )"
    
    x "( The only sounds are his sucking and licking, and my involuntary moans. My neck and face are covered in his saliva. What a mess. )"
    
    show madd shaken at left_small
    x "( After an eternity, he finally pulls away, his face wearing an expression of complete satisfaction. )"
    


    show madd relieved at left_small
    x "( He helps me lower my shirt back down. For a moment, I feel a small measure of relief. )"

    scene scene_runaway_from_brother_room_sitting_on_brother_lap_facing_him_that_was_amazing
    with fade
    show madd shocked at left_small
    with dissolve
    x "( Then he immediately buries his face in my covered chest, trying to bite through the fabric. He's trying to inhale my scent like an animal. )"
    
    show brother obsessed at right_small
    brother_says "That was incredible, Maddie. Your breasts are absolutely perfect. I can't believe I've been missing out on this."
    
    show madd uncertain at left_small
    x "( I can hear him breathing heavily, his voice filled with primal desire. His behavior is becoming increasingly animalistic. )"
    
    show brother fixated at right_small
    brother_says "If you had let me do this sooner, we could have avoided all this tension between us."
    
    show madd think at left_small
    x "( He's looking at me with such adoration, such intensity. I can see that he genuinely cares for me in his own twisted way. Perhaps he truly does want to make up for lost time. )"
    
    x "( I nod in agreement. If I play my cards right, I can use his feelings to my advantage. Right now, I need him more than ever. )"
    
    show madd focused at left_small
    x "( Now is the time to ask for those clothes. I'm still sitting on his lap, and he's in a giving mood. This is my opportunity. )"

    $ character_relations["brother"]["kissed"] += 3
    $ character_relations["brother"]["groped_madd"] += 1
    $ character_relations["brother"]["undressed_madd"] += 1
    $ character_relations["brother"]["touched_madd"] += 1
    $ character_relations["brother"]["friend"]+=3
    $ character_relations["brother"]["lust"] = 0
    $ character_relations["brother"]["anger"] = 0
    $ character_relations["brother"]["intimacy"] += 5

    jump runaway_brother_room_request_clothes


label runaway_brother_room_request_clothes:
    scene scene_runaway_brother_room_request_clothes_ask_for_clothes
    with fade
    show madd nervous at left_small
    with dissolve
    x "( I need to ask him carefully... this is critical. )"
    
    show madd anxious at left_small
    x "Um... I need some of your clothes. Loose, baggy stuff. And a cap if you have one."
    
    brother_says "What do you need that for?"


    scene scene_runaway_brother_room_request_clothes_ask_for_clothes_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd uncertain at left_small
    x "I need to... I need to look like a boy. Th. It's the only affordable option."
    
    show brother serious at right_small
    with dissolve
    
    brother_says "Oh... I understand. Yeah, I can definitely help with that."
    
    show madd shocked at left_small
    x "Really? Just like that? No conditions?"
    
    show madd think at left_small
    x "( He's so different from father. When father wants something, he takes it—demanding more and more without giving. But my brother... he actually offers help. )"
    
    show madd relieved at left_small
    x "( I suppose there's more to him than just the predator I've come to know. Perhaps he's not entirely lost. )"

    show brother leering at right_small
    brother_says "Yeah, no problem. Let me grab some clothes from my closet for you."
    
    show madd submissive nod at left_small
    x "( Finally, he releases his grip on me and I can stand up. )"

    jump runaway_brother_room_gives_clothes


label runaway_brother_room_gives_clothes:
    scene scene_runaway_brother_room_gives_clothes_brother_madd_face_to_face
    with fade

    show brother mocking at right_small
    with dissolve
    show madd submissive nod at left_small
    with dissolve
    
    x "He walks over to his closet and starts pulling out clothes."
    
    show brother leering at right_small
    brother_says "Here, I got some t-shirts, athletic wear, cargo pants. The stuff I don't wear often."
    
    show madd happy at left_small
    x "( He spreads them out on the bed. Oversized t-shirts, loose athletic wear, and baggy cargo pants. )"
    
    show brother mocking at right_small
    brother_says "These should work perfectly for what you need. And here's a cap too."
    
    show madd submissive nod at left_small
    x "Thank you so much! This is... this is really kind of you."
    
    show brother deceptive at right_small
    brother_says "No problem."
    x "(He doesnt say a word and just walks outside . By himself !)"
    show madd relieved at left_small
    x "( He's... leaving? He's actually going to let me have privacy? )"
    
    hide brother
    with dissolve
    
    x "( I listen as his footsteps fade down the hallway. I'm alone. )"
    
    scene scene_runaway_brother_room_gives_clothes_madd_changing_clothes_madd_girl_clothes
    with fade

    show madd processing at left_small
    x "I cant believe he actually left ,maybe there is some good in him."
    
    x "(I start by removing my clothes slowly parting ways with them , i wont be wearing them anytime soon..)"
    x "( I get to changing into his clothes. First the t-shirt. It's oversized, swallowing my frame completely. )"
    show madd hopeful at left_small
    x "( The neckline hangs loose, the sleeves extend past my elbows. My entire torso is hidden now. )"
    
    show madd boy relieved at left_small
    x "( I pull on his underwear. I cant believe it. But if anyone at the dorm notices my panties its not gonna end wel for me."
    x " (I have to wear his sweaty underwear.  They fit differently than my panties, looser. )"
    
    show madd boy anxious at left_small
    x "( Now the cargo pants. They're huge, I have to cinch them tight with a belt just to keep them up. )"
    
    show madd boy nervous at left_small
    x "( No curves visible. No shape. Just a generic male silhouette. )"
    
    x "( Finally, I pull on the cap, tucking my hair underneath. )"
    
    scene scene_runaway_brother_room_gives_clothes_madd_changing_clothes_boy_clothes_now
    with fade
    
    show madd boy conflicted at left_small
    x "( I catch my reflection in his mirror. The person looking back is a stranger. A boy. )"
    
    show madd boy processing at left_small
    x "( Short hair hidden under the cap, loose t-shirt, oversized jeans. My face is the only giveaway—softer features—but with this expression, I might just read as a scared kid. )"
    
    show madd boy uncertain at left_small
    x "( I look like a boy now. That's... good. That's what I needed. )"
    
    show madd boy determined at left_small
    x "( I open the door and tell him im done. As he enters his room. )"
    $got_male_clothes=True

    scene scene_runaway_brother_room_gives_clothes_madd_changing_clothes_boy_clothes_now_thank_you_brother
    with fade
    x "Thank you ,  for the clothes ."
    show brother deceptive at right_small
    with dissolve
    brother_says "So how do they fit?"
    
    show madd boy blush at left_small
    x "They fit fine"
    
    show brother mocking at right_small
    brother_says "Remember you are wearing a part of me now heh"
    
    show madd boy relieved at left_small
    x "( Apart from his last gross comment , i genuinely appreciate his help. )"

    show madd boy happy at left_small
    x "It is goodbye then , Brother "
    x "(I tried to give my best smile and i could see his face turn sorrow hearing me say that i was surprised he didnt try to stop me.)"
    brother_says "Goodluck Sis , hope you achieve what you want."

    x "(I left his room with my backpack with my other belongings. )"
    $ stat_notification = "Escape clothes obtained from brother"
    $ renpy.pause(2.0)
    $ stat_notification = ""
    $ journal_event_set_done("Brother", "Escape Night")

    if "home_main_door" in locked_home_areas:
        jump continue_runaway_preparation_brother_room
    else :
        x "( With the clothes secured, I head towards the front door. )"
        jump outside_home




label continue_runaway_preparation_brother_room:
    scene scene_home_lobby_area_night
    with fade
    
    $ locked_home_areas.remove("home_main_door") if "home_main_door" in locked_home_areas else None
    

    show madd boy focused at left_small
    with dissolve
    x "( Now I need to get the keys from Dad's room. The final piece. )"
    
    show madd boy determined at left_small
    x "( I know he sleeps deeply. This should be straightforward. )"

    scene scene_continue_runaway_preparation_brother_room_keys_from_dads_room
    with fade
    
    show madd boy nervous at left_small
    x "( I slip into Dad's room silently, moving with practiced care. The darkness is thick here. )"
    
    show madd boy focused at left_small
    x "( The keys are in the second drawer, exactly where I've seen him place them countless times. )"
    
    show madd boy anxious at left_small
    x "( My hand trembles slightly as I open the drawer. The metal scrapes—barely audible, but it sounds like thunder in this silence. )"
    
    show madd boy relieved at left_small
    x "( My fingers find the keys. Cold, solid, real. This is it. )"
    
    show madd boy determined at left_small
    x "( The keys to my escape are finally in my hands. )"
    
    show madd boy focused at left_small
    x "( I slip out of his room without a sound and move toward the front main door. My heart is racing. )"
    
    scene scene_continue_runaway_preparation_brother_room_keys_main_door
    with fade

    show madd boy anxious at left_small
    x "( This is my chance. My only chance. My freedom is waiting on the other side of this door. )"
    
    show madd boy uncertain at left_small
    x "( I take a deep breath at the threshold. Am I really doing this? )"
    
    show madd boy determined at left_small
    x "( Yes. I insert the key into the lock and turn it. The mechanism clicks. )"
    
    show madd boy shocked at left_small
    x "( It works. The door swings open slowly, revealing the cool night air beyond. )"
    x "IT WORKED , i cant believe it worked ! "
    
    show madd boy relieved at left_small
    x "( I'm free. I'm actually free. )"
    
    show madd boy hopeful at left_small
    x "( I step outside, breathing in the fresh air like it's the first breath of my new life. )"
    $ journal_event_set_done("Madd", "Stealing the Keys")

    jump outside_home


# WAKING UP IN  BROTHER  ROOM AFTER SLEEP SCENES 



label madd_wake_up_brother_morning_tries_anal:
    scene madd_wakes_up_in_brothers_bed
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd shocked at left_small
    with dissolve
    x "(I open my eyes slowly and i see brother standing right next to me .)"
    
    show madd anxious at left_small
    with dissolve
    x "(He is pointing  his fingers at me , i can see the anger in his eyes.)"
    
    show brother angry at right_small
    with dissolve
    brother_says "Maddie...I cant get it out of my head..."
    
    show madd confused at left_small
    with dissolve
    x "huh , what  are you talking about ?"
    
    show brother vindictive at right_small
    with dissolve
    brother_says "When dad was fucking you in the ass, you were moaning like a bitch in heat..."
    
    show madd shocked at left_small
    with dissolve
    x "(what !!? what am i supposed to say to that ..)"
    
    show madd nervous at left_small
    with dissolve
    x "I... I just got caught up in the moment..."
    
    show brother calculating at right_small
    with dissolve
    brother_says "No... you were enjoying it."
    
    show brother dominant at right_small
    with dissolve
    brother_says "You were enjoying it like a complete slut. You knew I was right there watching. And yet you went wild getting fucked by your own stepdad."
    
    show madd conflicted at left_small
    with dissolve
    x "(I need to fight back... if I don't, he'll start demanding the same thing from me.)"
    
    show madd angry at left_small
    with dissolve
    x "So what if I enjoyed it?! What's it to you anyway?!"
    
    show madd nervous at left_small
    with dissolve
    x "(The words are out before I can stop them... please don't let him get angrier...)"


    scene madd_wake_up_brother_morning_tries_anal_brother_jumps_in_bed 
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show brother possessive at right_small
    with dissolve
    brother_says "You let him do it. So why not me?"
    
    show madd shocked at left_small
    with dissolve
    x "(Before I can react, he lunges onto the bed and yanks me back against him.)"
    
    show madd distressed at left_small
    with dissolve
    x "(Then his lips are on my face, my neck ,kissing me roughly, desperately.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I should've seen this coming...)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(There's no way I can say no now. Not after admitting I enjoyed what happened with Dad.)"
    
    show madd helpless at left_small
    with dissolve
    x "(And now I have to face the consequences...)"

    scene madd_wake_up_brother_morning_tries_anal_brother_jumps_in_bed_licks_neck_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd resigned at left_small
    with dissolve
    x "(I'm trapped in his arms now. His tongue drags across my neck—wet, insistent.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(There's no stopping this... so I might as well surrender to whatever he wants.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I close my eyes, trying to relax despite everything.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(His hands slide to my chest, cupping and squeezing—them softly.)"

    scene madd_wake_up_brother_morning_tries_anal_brother_jumps_in_bed_licks_neck_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd anxious at left_small
    with dissolve
    x "(He keeps licking my neck, then pauses just long enough to speak.)"
    
    show brother lustful at right_small
    with dissolve
    brother_says "You liked it, didn't you?"
    
    show madd shocked at left_small
    with dissolve
    x "(Another wet lick across my skin before he continues.)"
    
    show brother mocking at right_small
    with dissolve
    brother_says "When he shoved his cock in your ass, you little slut."
    
    show madd horrified at left_small
    with dissolve
    x "(I... I don't know what to say to that. So I just lie there, frozen.)"
    
    show madd uncertain at left_small
    with dissolve
    x "(I'm not going to confirm it. I can't give him more ammunition. But I don't know how to respond.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(The word 'slut' echoes in my mind. Is that really what I am?)"
    
    scene madd_wake_up_brother_morning_tries_anal_brother_jumps_in_bed_licks_neck_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd distressed at left_small
    with dissolve
    x "(After those cruel words, his licks become more aggressive—almost desperate.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(His lust overtakes him. Saliva drips from his mouth onto my neck as he laps at my skin.)"
    
    show madd processing at left_small
    with dissolve
    x "(He saw how my body reacted in the kitchen when Dad took my ass. He watched me come undone.)"
    
    show madd resigned at left_small
    with dissolve
    x "(And now he's trying to recreate that same response. He knows I'm submissive. He's weaponizing that knowledge against me.)"

    scene madd_wake_up_brother_morning_tries_anal_brother_jumps_in_bed_licks_neck_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd overwhelmed at left_small
    with dissolve
    x "(His tongue runs from the base of my neck all the way up to my chin, then back down. Over and over.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(My neck is drenched in his saliva now. The scent of him—masculine, musky—fills my nose.)"
    
    show madd violated at left_small
    with dissolve
    x "(I should be disgusted. Part of me is. But there's another part... a sick, corrupted part... that finds it arousing.)"

    scene madd_wake_up_brother_morning_tries_anal_brother_jumps_in_bed_licks_neck_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd anxious at left_small
    with dissolve
    x "(I can feel his arousal growing. His movements become more frantic, more possessive.)"
    
    show madd shocked at left_small
    with dissolve
    x "(Suddenly, he grabs my face and turns it toward him. His tongue attacks my face now—licking, nipping with his teeth.)"
    
    show madd distressed at left_small
    with dissolve
    x "(He's trying to devour me. That's what it feels like. Like he wants to consume every inch of me.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(His tongue pushes past my lips, and suddenly we're kissing—fierce and hungry. It's overwhelming... and shamefully, it's turning me on.)"
    
    show madd processing at left_small
    with dissolve
    x "(I'm starting to understand something about myself. Everyone in this family is aggressive. Dominant. Predatory.)"
    
    show madd resigned at left_small
    with dissolve
    x "(And my body... it responds to that. It craves submission. It gets wet from being controlled.)"
    
    show madd broken at left_small
    with dissolve
    x "(If I stay here, they'll both use me. Dad and brother. Over and over. And I'll let them. I'll be completely theirs.)"
    
    show madd traumatized at left_small
    with dissolve
    x "(Eventually, one of them will get me pregnant. I'll be stuck here forever—a live-in breeding toy for them to share.)"


    scene madd_wake_up_brother_morning_tries_anal_brother_jumps_in_bed_kisses
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd shocked at left_small
    with dissolve
    x "(He slows down suddenly. The kisses become softer, more deliberate.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I'm caught off guard by the shift. But... I hate to admit it... I like this better.)"
    
    show madd inheat at left_small
    with dissolve
    x "(One hand cups the back of my head. The other wraps around my waist, pulling me against him.)"

    scene madd_wake_up_brother_morning_tries_anal_brother_jumps_in_bed_kisses_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd anxious at left_small
    with dissolve
    x "(He pulls back just an inch, then pushes his tongue deep into my mouth.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(It goes so deep I can feel it touching the back of my throat. I'm running out of air, but god... it feels good.)"
    
    show madd shaken at left_small
    with dissolve
    x "(My lungs scream for oxygen. Instinctively, my hand grabs at his shirt, trying to push him away.)"
    
    show madd helpless at left_small
    with dissolve
    x "(But he doesn't budge. He keeps kissing me, claiming my mouth completely.)"

    scene madd_wake_up_brother_morning_tries_anal_brother_jumps_in_bed_kisses_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd relieved at left_small
    with dissolve
    x "(Finally, he eases up. His tongue traces my lips gently now, teasingly.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(This is... actually pleasant. The gentleness is unexpected.)"
    
    show madd disgusted at left_small
    with dissolve
    x "(I can smell his morning breath—stale, bitter. It should revolt me.)"
    
    show madd inheat at left_small
    with dissolve
    x "(But my body's been conditioned. Any scent from a dominant male... it arouses me now.)"
    
    show madd processing at left_small
    with dissolve
    x "(Whether it's Dad or my brother, their breath, their sweat, their cum—it all works on me the same way.)"
    
    show madd broken at left_small
    with dissolve
    x "(Armpits, crotch, mouth, feet—doesn't matter. If it's from a man who dominates me, my body responds.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I become submissive. Compliant. Eager to please them however they want.)"

    scene madd_wake_up_brother_morning_tries_anal_brother_jumps_in_bed_kisses_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd anxious at left_small
    with dissolve
    x "(He keeps tracing my lips with his tongue, then stops completely.)"
    
    show brother obsessed at right_small
    with dissolve
    brother_says "I still remember the moans you made when Dad fucked you hard in the ass."
    
    show madd processing at left_small
    with dissolve
    x "(Oh no... he's jealous. Actually jealous of his own father.)"
    
    show madd uncertain at left_small
    with dissolve
    x "(Is that what's driving this? Jealousy? Competition? Is that why he's being so aggressive?)"
    
    show madd shocked at left_small
    with dissolve
    x "(Before I can process it fully, his tongue plunges back into my mouth—deep, almost reaching my throat.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(This isn't a kiss anymore. He's trying to  claim me, erase Dad's mark on me.)"

    scene madd_wake_up_brother_morning_tries_anal_brother_jumps_in_bed_pulls_closer_roughly
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd shocked at left_small
    with dissolve
    x "(Suddenly, he yanks me closer—hard. The movement is fueled by anger and jealousy.)"
    
    show brother angry at right_small
    with dissolve
    brother_says "Why did you let him do it... Maddie?"
    
    show madd distressed at left_small
    with dissolve
    x "(He presses kisses to my shoulders—rough, possessive.)"
    
    show brother vindictive at right_small
    with dissolve
    brother_says "And right in front of me, too?"
    
    show madd anxious at left_small
    with dissolve
    x "(Now he's kissing my neck and shoulders. He's trying to make me feel guilty for what happened with Dad.)"
    
    show madd angry at left_small
    with dissolve
    x "(How is any of that my fault? I didn't ask for it to happen!)"

    scene madd_wake_up_brother_morning_tries_anal_brother_jumps_in_bed_pulls_closer_roughly_turns_madd_around
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd shocked at left_small
    with dissolve
    x "(In one swift motion, he flips me around and latches onto my neck again.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I'm exhausted. There's no point fighting anymore. No point trying to stop this.)"
    
    show madd inheat at left_small
    with dissolve
    x "(My body gives in completely. Soft moans escape my lips as I respond to his touch.)"
    
    show brother obsessed at right_small
    with dissolve
    x "(He knows I'm moaning now. I can feel his satisfaction. He's proud of himself for breaking me down like this.)"

    scene madd_wake_up_brother_morning_tries_anal_brother_jumps_in_bed_turned_around_neck_lick_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd helpless at left_small
    with dissolve
    x "(I'm completely wrapped in his arms. He kisses and licks my neck while I lie here, trapped.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(There's nowhere to go. He can do whatever he wants to me. And my body... it's responding to his touch.)"


    scene madd_wake_up_brother_morning_tries_anal_brother_jumps_in_bed_turned_around_neck_lick_1_5_dialogue
    with dissolve
    
    show brother obsessed at right_small
    with dissolve
    brother_says "God, you're so beautiful, Maddie."
    
    show brother lustful at right_small
    with dissolve
    brother_says "No wonder every male in this house wants to put a baby in you."
    
    show madd horrified at left_small
    with dissolve
    x "(The words hit me like ice water.)"
    
    show madd traumatized at left_small
    with dissolve
    x "(Eventually, I might actually end up pregnant. With my stepdad's baby... or my stepbrother's.)"
    
    show madd broken at left_small
    with dissolve
    x "(If it's a boy... will he want to breed me too? When he grows up?)"
    
    show madd processing at left_small
    with dissolve
    x "(If he inherits their genes, he'll have the same twisted desires. The same need to dominate and claim me.)"

    scene madd_wake_up_brother_morning_tries_anal_brother_jumps_in_bed_turned_around_neck_lick_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd submissive nod at left_small
    with dissolve
    x "(He keeps going, his hand sliding slowly up to my neck.)"
    
    show madd inheat at left_small
    with dissolve
    x "(He knows he's in complete control. Of the situation. Of me. And I... I love that he's in control.)"
    
    show madd broken at left_small
    with dissolve
    x "(I've learned something terrible about myself. My body craves helplessness. It gets off on being dominated by people who have power over me.)"

    scene madd_wake_up_brother_morning_tries_anal_brother_jumps_in_bed_pulls_back_to_bed_side_cuddling
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd relieved at left_small
    with dissolve
    x "(After a few more kisses, he eases me back onto the bed—sideways, spooning position. He wraps himself around me.)"
    
    show madd uncertain at left_small
    with dissolve
    x "(The landing is soft. Comfortable, even. Maybe... maybe this isn't so bad after all?)"

    scene scene_brother_room_madd_sleep_now_morning_brother_laying_beside_bed_cuddling_fck_you_so_hard
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd anxious at left_small
    with dissolve
    x "(We lie like this for a while. Then he starts kissing my neck again... and stops abruptly.)"
    
    show brother dominant at right_small
    with dissolve
    brother_says "I'm gonna fuck you so hard, Maddie."
    
    show brother possessive at right_small
    with dissolve
    brother_says "Next time Dad fucks you, you'll be thinking of me instead."
    
    show madd shocked at left_small
    with dissolve
    x "(He turns my head toward him and kisses me deeply again.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I know what's coming. He's going to do the same thing Dad did to me. And I won't have a choice. No opportunity to say no.)"

    scene madd_wake_up_brother_morning_tries_anal_brother_jumps_in_bed_pulls_back_to_bed_side_cuddling_spanking
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd anxious at left_small
    with dissolve
    x "(He lifts my leg slightly and his hand finds my ass, rubbing it in slow circles.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I can't deny it anymore—I'm loving his touch on my butt. I know it's wrong. But my brain's been completely rewired by this father-son duo.)"
    
    show madd nervous at left_small
    with dissolve
    x "(After a minute, he hooks his fingers into the waistband of my shorts and starts sliding them down—slowly, deliberately.)"
    x "(Fuck fuck fuck... If I dont stop this i will be naked in his room , and i dont know what he'll do to me after that .)"
    if character_relations["brother"]["intimacy"] < 15:
        menu:
            "I know he's jealous of Dad, might as well use that against him" :
                if madd_willpower+( 15- character_relations["brother"]["intimacy"]) >= character_relations["brother"]["lust"]:
                    show madd angry at left_small
                    x "I already told you I liked what dad did to me, You will never be him ! "
                    x "So leave me alone right fucking now or I will tell anything you do to me to dad . He will kick your ass to the streets."
                    show brother shocked at right_small
                    brother_says "W-What the fuck did you just say...?"
                    brother_says "You prefer him over me...after all he's done to you?"
                    brother_says "is that it ? tch...the day you come to regret saying this will soon be upon you maddie. Mark my words"
                    x "(There is actual sadness in his words, like he has just lost a battle he was preparing for a long time.)"
                    x "(I quickly got out of the bed , fixed my clothes and went out to the lobby area avoiding this nightmare)"
                    $ character_relations["brother"]["anger"] +=20
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_102
                    $ character_relations["brother"]["intimacy"]+=5
                    call advance_time_and_check(minutes=120) 
                    $ madd_willpower=max(madd_willpower-20,0)
                    jump home_areas
                else:
                    $character_relations["brother"]["lust"]=0
                    $character_relations["brother"]["anger"] +=20
                    show madd trembling at left_small
                    x "I already told you I liked what dad did to me, You will never be him ! "
                    x "So leave me alone right fucking now or I will tell anything you do to me to dad . He will kick your ass to the streets."
                    show brother sadistic at right_small
                    with dissolve
                    brother_says "Hah.You think I am stupid , dont you slut ?"
                    brother_says "If you really liked his abuse why are you sleeping in my bed instead of next to him ?"
                    x "(Fuck, he saw right through me.)"
                    brother_says "I know you are scared , scared that if you slept next to him he might just put his dick in your pussy and fuck you till your belly swells with his child"
                    show madd paralyzed at left_small
                    x "(Am i that readable...I froze hearing his words. )"
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_103    

    scene madd_wake_up_brother_morning_tries_anal_brother_spooning_position_madd_bottom_naked
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd resigned at left_small
    with dissolve
    x "(My shorts are completely off now. I'm lying in my stepbrother's bed fully naked)"
    
    show madd helpless at left_small
    with dissolve
    x "(He has full access to my lower body. He could take off my top too, and I wouldn't say a word...)"
    
    show madd anxious at left_small
    with dissolve
    x "(His hand lands on my butt cheek, fingers spreading it gently, exposing me.)"

    scene madd_wake_up_brother_morning_tries_anal_brother_spooning_position_madd_bottom_naked_brother_removes_his_shorts
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd nervous at left_small
    with dissolve
    x "(He pulls back briefly to remove his own shorts, then returns to his position behind me.)"
    
    show madd anxious at left_small
    with dissolve
    x "(His hand lands on my ass again, squeezing gently.)"
    
    show madd shocked at left_small
    with dissolve
    x "(I can't see it, but I feel it—the temperature near my anus changes. There's heat radiating from something.)"
    
    show madd trembling at left_small
    with dissolve
    x "(His cock. It's so hot I can feel it from inches away, the heat alone telling me how hard he is.)"

    show madd resigned at left_small
    with dissolve
    x "(He's going to put it in my ass. I can't stop him. Just because he watched Dad do it to me, now he thinks he gets to do it too.)"

    x "(this might be my last chance to stop him from putting his dick in me. I know he compares himself to dad , i could use it against him)"
    if character_relations["brother"]["intimacy"] < 60:
        menu:
            "Humiliate him" :
                if madd_willpower+2*(60-character_relations["brother"]["intimacy"]) >= character_relations["brother"]["lust"]:
                    x "(I push my butt back so i could get a feel of his dick on me, just so i could make it more believable. Holy fuck was it big and hard but i kept my composure)"
                    show madd blush at left_small
                    x "Ha, what is that pathetic size...Dad is so much bigger than you "
                    x "Even though you are older than me by many years , I should be calling you little brother by the looks of it"
                    x "Dad's dick was so big , it rearranged my insides. I could tell my asshole isnt gonna feel a thing with yours inside me "
                    x "Okay go ahead 'little brother' go relief yourself, i wont feel a thing but this is wasting precious time i could have dad inside me . "
                    show brother shocked at right_small
                    brother_says "W-What the ..."
                    x "(I could sense his anger and humiliation as his grip on me loosened)"
                    x "(I knew i hit a nerve there, he let go of me completely I used this opportunity to escape)"
                    brother_says "you fucking slut ! I wasnt even fully hard you hear me "
                    x "Yea yea, tell yourself that but remember .."
                    x "There is no exercise to be a weak pussy with a small dick"
                    x "(He stood there paralyzed , i knew that was the nail in the coffin as i immediately seized the opportunity to get out of bed)"
                    x "(I fixed my clothes and went out to the lobby area avoiding this nightmare)"
                    $ character_relations["brother"]["anger"] +=20
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_104
                    $ character_relations["brother"]["intimacy"]+=7
                    call advance_time_and_check(minutes=120) 
                    $ madd_willpower=max(madd_willpower-20,0)
                    jump home_areas
                else:
                    $character_relations["brother"]["lust"]=0
                    $character_relations["brother"]["anger"] +=20
                    show madd trembling at left_small
                    x "(I push my butt back so i could get a feel of his dick on me, just so i could make it more believable. Holy fuck was it big and hard )"
                    x "(As soon as i touched it my body froze...That thing is gonna be inside me...no way)"
                    x "( I was gonna grind my butt to his and then make fun of his dick , hoping he would feel humiliated and let go but instead i was the one who froze)"
                    show brother sadistic at right_small
                    with dissolve
                    brother_says "Time to make you moan like you did for dad Maddie"
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_105   



    scene madd_wake_up_brother_morning_tries_anal_brother_spooning_position_madd_naked_brother_naked_first_insertion
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd shocked at left_small
    with dissolve
    x "(And then... it happens.)"
    
    show madd distressed at left_small
    with dissolve
    x "(He pushes into my ass—slowly, deliberately. I feel every inch as he sinks deeper.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(The heat from his cock spreads through my insides. I can feel the texture of it, the warmth, the thickness as it fills me completely.)"
    
    show madd trembling at left_small
    with dissolve
    x "(He starts to move—gentle thrusts at first. Pleasure and pain mix together, impossible to separate.)"
    
    show madd anxious at left_small
    with dissolve
    x "(My body struggles to adjust. At first, it feels like I'm being plugged up from the inside. I can barely breathe.)"
    
    show madd relieved at left_small
    with dissolve
    x "(But as he keeps thrusting, the pain fades. Pleasure starts to take over.)"

    scene madd_wake_up_brother_morning_tries_anal_brother_spooning_position_madd_naked_brother_naked_first_insertion_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd inheat at left_small
    with dissolve
    x "(He picks up the pace gradually. By now, I'm completely adjusted to him. No more pain—just pure pleasure.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(His cock is slick now—coated in my body's natural fluids and his precum. The slide becomes easier, smoother.)"
    
    show madd resigned at left_small
    with dissolve
    x "(My hips start moving on their own, pushing back to meet his thrusts. Like we're synchronized. Like we were made to fit together.)"
    
    show madd inheat at left_small
    with dissolve
    x "(I'm moaning now. Softly at first, then louder as the pleasure builds. There's no escape from this. I'm completely at his mercy. And I love it.)"
    
    show brother lustful at right_small
    with dissolve
    brother_says "Maddie, you like it, don't you?"
    
    show madd submissive nod at left_small
    with dissolve
    x "(I can't even speak. All I can do is moan and nod.)"
    
    show brother dominant at right_small
    with dissolve
    brother_says "I know you do. You were made for this. Made to be fucked like this."
    
    show madd broken at left_small
    with dissolve
    x "(His words send shivers down my spine. I don't want to admit it, but he's right. I was made for this. Made to be fucked by my stepbrother and stepfather.)"
    
    show brother obsessed at right_small
    with dissolve
    x "(His hands spread my ass cheeks wider, giving him even better access. Making it easier for him to thrust deeper.)"
    
    show brother possessive at right_small
    with dissolve
    brother_says "I'll fuck you until you love it. Until you can't live without it. Until you beg me for more."
    
    show madd traumatized at left_small
    with dissolve
    x "(Somehow, I know he means it. And instead of being terrified... I'm excited. The thought of being fucked by him every day... it thrills me.)"
    
    show madd resigned at left_small
    with dissolve
    x "(My body wants to be their toy. His and Dad's. I want to be used and abused by them.)"

    scene madd_wake_up_brother_morning_tries_anal_brother_spooning_position_madd_naked_brother_naked_first_insertion_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd inheat at left_small
    with dissolve
    x "(My whole body feels like it's on fire. Fluids leak from both my ass and my pussy. My nipples are hard and aching. I'm gasping for breath.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(I can still smell his saliva all over me. His scent is everywhere—on my skin, in my nose. It makes me feel bonded to him somehow.)"
    
    show madd blush at left_small
    with dissolve
    x "(I'm in a state of complete bliss. I never want this to end.)"
    
    show madd resigned at left_small
    with dissolve
    x "(His big hands gripping my ass. His cock buried deep inside me. His breath hot on my neck. His saliva marking my skin. It's all perfect.)"
    
    show madd broken at left_small
    with dissolve
    x "(Perfect for a submissive girl like me. A girl who just wants to be fucked and used by her stepbrother and stepfather.)"
    
    show madd anxious at left_small
    with dissolve
    x "(I feel his cock swell inside me, twitching. I know what's coming.)"
    
    show brother dominant at right_small
    with dissolve
    brother_says "I'm going to cum inside you, Maddie."
    
    show madd conflicted at left_small
    with dissolve
    x "(I should be scared. I should beg him to stop. But instead, I feel a surge of excitement at the thought of him filling me.)"
    
    show madd inheat at left_small
    with dissolve
    x "(I want his seed deep inside me.)"
    
    show brother possessive at right_small
    with dissolve
    brother_says "Remember—you're in my bed. I'm fucking you in the ass. And I'm going to cum inside you. You have no choice but to accept it."
    
    show brother mocking at right_small
    with dissolve
    brother_says "I won't wash the blanket or the sheets. Next time you sleep here, you'll be lying in the cum I left inside you."
    
    show madd shocked at left_small
    with dissolve
    x "(His words make me even more excited. The thought of him marking me, claiming me... I never thought I'd enjoy it. But now I can't wait.)"
    
    show brother obsessed at right_small
    with dissolve
    brother_says "For now, I'll cum in your ass. But once you've fermented enough of my cum inside you, I'll start cumming in your pussy."
    
    show brother vindictive at right_small
    with dissolve
    brother_says "I'll put a baby in you before Dad does. And then he'll have to deal with the fact that you're carrying my child, not his."
    
    show madd horrified at left_small
    with dissolve
    x "(The thought of being pregnant with his child... it terrifies and excites me at the same time.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(As soon as he says it, he gets more aggressive—pounding into me harder, faster, like a man possessed.)"

    scene madd_wake_up_brother_morning_tries_anal_brother_spooning_position_madd_naked_brother_naked_climax_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd shocked at left_small
    with dissolve
    x "(That's when I feel it—hot spurts of cum shooting deep into my ass.)"
    
    show madd inheat at left_small
    with dissolve
    x "(As he starts cumming, his thrusts become erratic and desperate. My moans get louder as the pleasure peaks.)"
    
    show madd blush at left_small
    with dissolve
    x "(I love it. The hot, sticky fluid filling me up. It's like a drug I can't get enough of.)"
    
    show madd broken at left_small
    with dissolve
    x "(I love cum. It doesn't even matter whose it is. I just want to be filled with it, to feel it dripping out of me.)"
    
    show madd inheat at left_small
    with dissolve
    x "(In my pussy, my ass, my mouth—I love it all.)"
    
    show madd processing at left_small
    with dissolve
    x "(I'll let both my stepbrother and stepfather cum inside me. Maybe even at the same time.)"
    
    show madd shocked at left_small
    with dissolve
    x "(The thought makes my heart skip a beat. A wave of excitement washes over me.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(Being filled with both of them at once... I never thought I'd want that. But now I can't wait for it.)"
    
    show madd resigned at left_small
    with dissolve
    x "(They'll probably fight over who gets my pussy. They want the bragging rights of being the one who knocks me up. But I don't care who cums where, as long as they both fill me.)"

    scene madd_wake_up_brother_morning_tries_anal_brother_spooning_position_madd_naked_brother_naked_climax_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd overwhelmed at left_small
    with dissolve
    x "(He doesn't stop. Even while cumming, he keeps pounding into me—trying to drive his cum deeper with each thrust.)"
    
    show madd processing at left_small
    with dissolve
    x "(It's like he's planting more than just his seed. He's planting an idea.)"
    
    show madd broken at left_small
    with dissolve
    x "(The idea that this taboo, forbidden act is something I should embrace. That I'm meant to be fucked by him. That I should enjoy it.)"
    
    show madd shocked at left_small
    with dissolve
    x "(There's so much cum. More than I thought possible. I feel it leaking out of my ass, dripping onto the sheets.)"
    
    show madd worried  at left_small
    with dissolve
    x "(Finally, after what feels like forever, he stops thrusting. His cock stays buried deep inside me. I'm left panting, covered in his fluids.)"
    
    show madd processing at left_small
    with dissolve
    x "(It feels like I've been through some kind of ritual. Like I've been initiated into some secret society of people who enjoy taboo things.)"
    
    show brother obsessed at right_small
    with dissolve
    brother_says "God, that was amazing, Maddie. You took my cum so well."
    
    show madd worried at left_small
    with dissolve
    x "(I just lie here with him, still trying to catch my breath and understand what just happened.)"
    
    show brother possessive at right_small
    with dissolve
    brother_says "I know you enjoyed it. I could see it in your face. You were loving every second of it."
    
    show brother dominant at right_small
    with dissolve
    brother_says "Now let it rest inside you. Let your ass get used to it... because we'll be doing this very frequently from now on."
    
    show madd submissive nod at left_small
    with dissolve
    x "(I nod. It might look like a submissive gesture rather than enthusiasm. But the truth is... I'm actually excited about being fucked by him every day. About having his cum inside me all the time.)"
    
    show madd relieved at left_small
    with dissolve
    x "(I feel his cock finally soften inside me. He pulls out slowly, leaving me feeling hollow and empty.)"
    
    show brother possessive at right_small
    with dissolve
    brother_says "Don't worry. I'll give you another dose of cum soon. For now, just enjoy being filled with mine. And know that you're mine now."
    
    show madd uncertain at left_small
    with dissolve
    x "(I nod again. He grabs the blanket and drapes it over me, then gets out of bed.)"
    
    show madd shocked at left_small
    with dissolve
    x "(Wait—his cum is still dripping out of me! Why is he covering me with the blanket?!)"
    
    show brother mocking at right_small
    with dissolve
    brother_says "Now lie there for a while. Let the cum dry on you. I'll sleep after you've absorbed it all."
    
    hide brother
    with dissolve
    
    show madd processing at left_small
    with dissolve
    x "(With that, he leaves the room. I stare up at the ceiling, still trying to process everything that just happened.)"

    scene madd_wake_up_brother_morning_tries_anal_brother_spooning_position_madd_naked_brother_naked_climax_aftermath
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd horrified at left_small
    with dissolve
    x "I can't believe I let him cum inside me..."
    
    show madd disgusted at left_small
    with dissolve
    x "(I peek under the blanket. The smell of his cum rushes into my nose—strong, musky, overwhelming.)"
    
    show madd anxious at left_small
    with dissolve
    x "(I'm still lying here, covered in his fluids.)"
    
    show madd distressed at left_small
    with dissolve
    x "It's still leaking out of me..."
    
    show madd processing at left_small
    with dissolve
    x "The whole room smells like him. His cum, his saliva, his sweat—it's all over me and the sheets."
    
    show madd conflicted at left_small
    with dissolve
    x "But somehow... I don't hate the smell. I actually kind of like it. Is my submissive nature making me enjoy the scent of his cum? The sweaty musk of his cock? His saliva?"
    
    show madd self loathing at left_small
    with dissolve
    x "Why? Why do I like it?"
    
    show madd worried at left_small
    with dissolve
    x "(With that thought, I close my eyes and drift back to sleep.)"

    
    scene madd_wakes_up_in_brothers_bed
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show brother mocking at right_small
    with dissolve
    brother_says "Hope you liked sleeping in the bed where I fucked you."
    
    show madd shocked at left_small
    with dissolve
    x "(I'd forgotten I'm still covered in his cum. The smell is still thick in the room.)"
    
    show madd processing at left_small
    with dissolve
    x "(I'm not horny anymore. My head is clear. And the reality of what just happened hits me like a freight train.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I can't deny it happened. But I also can't believe I let it happen.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I just look at him and nod, not sure what else to say.)"
    
    show brother dismissive at right_small
    with dissolve
    brother_says "Now get up. It's my turn to sleep."
    
    show madd uncertain at left_small
    with dissolve
    x "(I get up from the bed. He flips the mattress over and climbs in, leaving me standing there in the middle of the room.)"

    # Stats update after anal sex scene
    $ character_relations["brother"]["lust"] = 0
    $ character_relations["brother"]["anger"] = 0
    $ character_relations["brother"]["intimacy"] += 9
    $ character_relations["brother"]["kissed"] += 5
    $ character_relations["brother"]["groped_madd"] += 2
    $ character_relations["brother"]["undressed_madd"] += 1
    $ character_relations["brother"]["touched_madd"] += 2
    $ character_relations["brother"]["anal_sex"] += 1
    $ character_relations["brother"]["anal_creampie"] += 1
    $ character_relations["brother"]["friend"]+=5
    $ journal_event_set_done("Brother","Morning Claim")
    $ journal_event_show("Brother", "Wake Up: Full Claim")
    $ madd_willpower = max(0, madd_willpower - 45)
    $ stat_notification = "Brother's intimacy increased significantly"
    $ renpy.pause(2.0)
    $ stat_notification = ""
    call advance_time_and_check(minutes=90) 

    jump step_brother_room_scene




label dream_sequence_2_moms_memory_brother_helps:
    scene brother_standing_over_maddie_watching_her_sleep
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show brother fixated at right_small
    brother_thinks "God, she's so cute when she sleeps..."
    show brother predatory at right_small
    brother_thinks "I could do all sorts of things to her while she sleeps and she wouldn't even know it..."
    hide brother
    scene black
    with fade
    show madd confused at left_small
    with dissolve
    x "(Huh... where am I?)"
    x "(I hear groans and moans coming from somewhere.)"
    scene family new
    with dissolve
    show madd horrified at left_small

    x "(It's Mom! She's standing between Dad and Brother!)"
    x "(Suddenly they start getting rough with her — pulling at her clothes.)"
    scene dream_sequence_2_moms_memory_brother_helps_mom_getting_roughed_up
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd angry at left_small
    x "HEY! STOP IT!!"
    x "What are you doing to Mom?!"
    show madd distressed at left_small
    x "(I kept screaming but no voice came out of my mouth.)"
    x "(Her shirt was torn off her shoulder, her bare skin exposed.)"
    x "(The sounds she was making were getting louder and louder.)"
    show madd horrified    at left_small
    x "(But they weren't moans of pleasure — they were cries for help.)"

    scene dream_sequence_2_moms_memory_brother_helps_mom_getting_roughed_up_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    x "(They started licking her skin and pulling her in opposite directions.)"
    x "(Tears streamed down her face as she heaved ragged, desperate breaths.)"
    x "(Then both of them started licking her neck and every inch of her exposed skin.)"
    show madd angry at left_small
    x "No, no, no — please stop it!"
    x "Can't you fucking see you're hurting her?!"

    scene dream_sequence_2_moms_memory_brother_helps_mom_getting_roughed_up_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    x "(They're pulling her roughly now, trying to drag her to the bed...)"
    show madd angry at left_small
    x "Nooo! Please, leave her alone!"
    show madd determined at left_small
    x "(Suddenly she manages to shake them off and bolts out the door with them chasing after her.)"
    x "Run, Mom! Get away from these bastards... There are better people out there who will treat you right!"
    show madd shaken at left_small
    x "(She tricks them and runs straight to my room — it's me, younger me.)"
    x "(She fixes her shirt and hair, clears her throat before speaking so I won't see her scars or hear the trembling in her voice.)"
    show madd self loathing at left_small
    x "(I remember this moment... she was asking how I was, and I told her to get out of my room and leave me alone.)"

    scene dream_sequence_2_moms_memory_brother_helps_mom_in_maddies_room
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    x "(Despite everything she had just been through, she still cared enough to check on me.)"
    show madd self loathing at left_small
    x "(She reassured me she just wanted to know if I was okay — and I responded by calling her a prostitute who gets fucked by everyone.)"
    show madd angry at left_small
    x "SHUT UP, STUPID BITCH! You don't know what she went through!"

    scene dream_sequence_2_moms_memory_brother_helps_mom_in_maddies_room_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd self loathing at left_small
    x "(She pleads with me again, saying she does all of this for me.)"
    x "(And I called her a groupie who gets fucked by everyone.)"
    x "(As the words leave my mouth, tears start rolling down her face and she begins to sob.)"
    show madd traumatized at left_small
    x "SHUT THE FUCK UP, MADDIE! You disgusting, ungrateful little whore!"
    x "(I kept screaming at myself inside my head, but not a single sound came out.)"

    scene dream_sequence_2_moms_memory_brother_helps_mom_in_maddies_room_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd weeping at left_small
    x "(My dream-self tells her to get out after calling her a slut — and Mom weakly walks out of my room.)"
    x "(She enters the kitchen. Her face looks devastated and hollow, like all the life has been drained out of her.)"
    x "(Her steps are slow and heavy. She picks up a bottle of alcohol and takes a long, deep gulp.)"
    show madd self loathing at left_small
    x "MADDIE, you cunt! You deserve everything bad that happens to you! You deserve to be used like a piece of meat!"
    show madd weeping at left_small
    x "(She finishes the whole bottle in one pull, then grabs another and does the same.)"

    scene dream_sequence_2_moms_memory_brother_helps_mom_in_kitchen_death
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd weeping at left_small
    x "(She keeps drinking, emptying another bottle while tears roll endlessly down her face — a broken, hollow soul.)"
    x "(She drinks and drinks until her body gives out.)"
    x "(She weakly staggers out of the kitchen, takes two steps into the lobby, then crumples to the floor.)"
    show madd traumatized at left_small
    x "NOOO! This is where I found her the next morning, passed out in the lobby!"
    show madd broken at left_small
    x "Mom, please wake up! Please! I was just a stupid kid — I didn't understand what was happening."
    x "I'm sorry. I never knew how hard it was for you. I'm sorry for everything I ever said to you."
    show madd weeping at left_small
    x "(The dream begins to fade. There are still things I need to say before it does.)"
    x "I'm so sorry... for every single disgusting thing I ever said to you."
    x "Calling you a prostitute... a groupie... a slut... a whore who gets fucked by everyone... screaming at you to get the fuck out of my room... I was a cruel, selfish, ungrateful little cunt."
    show madd broken at left_small
    x "You had just escaped them... after everything Dad and Brother did to you... you were broken, shaking, and you still came to check on me. You said you did it all for me... and I didn't even give you that."
    x "I didn't understand. I didn't see your pain. I didn't see how much you sacrificed... how much you loved me."
    show madd weeping at left_small
    x "I love you, Mom. I always loved you. You weren't any of those things I called you. You were the strongest person in the world."
    x "I just didn't see it..."
    x "Please forgive me... please know I'm sorry. I was wrong. So fucking wrong about everything."

    scene dream_sequence_2_moms_memory_brother_helps_maddie_last_message
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    x "Mom... Mom, I miss you... I'm sorry... please come back..."
    hide madd broken
    show brother shocked at right_small
    brother_thinks "Huh... this whole time, she was just an orphan missing her mom."
    show brother serious at right_small
    brother_thinks "God, what a horrible person I am for even thinking of doing something like that to her."
    brother_thinks "I'm sorry, Emily... I did terrible things to you... I wish I could take it all back..."
    show brother think at right_small
    brother_thinks "But for now... I'll make sure to take care of Maddie and be there for her... just like Emily was there for me."
    show brother serious at right_small
    "He takes out his phone and opens a private banking app, fingers moving quietly in the dark."
    brother_thinks "She'll never know who sent it. That's fine. She doesn't need to know."
    python:
        if "unknown" not in contacts_met:
            contacts_met.append("unknown")
        receive_message("unknown", "[[BANK ALERT] $3,000.00 has been credited to your account from: Anonymous Transfer. Ref #4829-AX. The funds are available immediately. No sender details on file.")
    brother_thinks "Study well, Maddie... This world is a cruel place... but I hope I can help you find some happiness in it... just like Emily did for me."
    hide brother

    
    $ journal_event_set_done("Madd", "Dream: Mom's Last Night")
    $ character_relations["brother"]["intimacy"] += 10
    jump brother_sleeping_after_dream




label madd_wake_up_brother_morning_escalations_vaginal:
    
    scene madd_wake_up_brother_morning_foot_on_bed 
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd confused at left_small
    show brother fixated at right_small

    x "(I slowly open my eyes to see brother standing right next to my bed, staring at me.)"
    x "(How long has he been there?)"
    x "(I stood up and as i am sitting up, he puts his foot on the bed  )"
    brother_says "My feet is dirty Maddie"
    x "(I look down at his feet , the sight of his dirty feet makes me feel disgusted. )"
    x "What am i supposed to do with that? Why are you showing me that ?"
    x "(He looks at me with a blank expression and says nonchalantly )"
    brother_says "Clean it obviously"
    x "(I am taken aback by his response, feeling a mix of anger and confusion. I can't believe he expects me to clean his dirty feet.)"

    scene madd_wake_up_brother_morning_foot_on_bed_madd_resisting
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd angry at left_small
    show brother entitled at right_small
    x "(I put my hands right above his foot , just to push them away from the bed )"
    x "What do you think I am ? Your Footmat ? I am not going to clean your dirty feet !"
    x "(I manage to push his foot away from the bed, as i see anger begin to build up in his eyes. )"
    brother_says "I let you sleep in my bed, I let you stay in my room, And i Save you from Dad."
    brother_says "While you hungrily munch on dad's foot, I'm the one who actually saves you from him."
    x "(His words hit me like a punch to the gut. I can't believe he would say something so cruel and manipulative.)"
    x "but...I...I was forced to put dad's foot in my mouth, I didn't have a choice!"
    brother_says "Oh please, don't act like you had no choice. I saw how much you enjoyed it. You were practically begging for more."
    x "(I didnt have any response to his words, I just stood there in silence, feeling a mix of shame and anger. )"
    x "(I have no words to defend myself against his accusations, i just look down at the floor in shame )"

    x "(I can see the anger boiling in his eyes, if i am gonna act tough now is the time)"

    if character_relations["brother"]["intimacy"] < 40:
        menu:
            "Insult his foot and his hygiene": 
                if madd_willpower+2*( 40- character_relations["brother"]["intimacy"]) >= character_relations["brother"]["lust"]:
                    show madd angry at left_small
                    x "At least dad's foot is cleaner than yours ! Your feet are so dirty they could probably give me a disease !"
                    x "If you do anything to me I'm telling dad i caught something when you forced me to lick your feet"
                    show brother shocked at right_small
                    brother_says "You fucking bitch..."
                    x "(He took time to check his own foot and even though i couldnt see it i could tell it was nasty as hell by his reaction to seeing his own foot)"
                    brother_says "Tch...Fine..but dont think you can get away from me little sis."
                    x "(I quickly got out of the bed , fixed my clothes and went out to the lobby area avoiding this nightmare)"
                    $ character_relations["brother"]["anger"] +=20
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_106
                    $ character_relations["brother"]["intimacy"]+=3
                    call advance_time_and_check(minutes=120) 
                    $ madd_willpower=max(madd_willpower-20,0)
                    jump home_areas
                else:
                    $character_relations["brother"]["lust"]=0
                    $character_relations["brother"]["anger"] +=20
                    show madd trembling at left_small
                    x "At least dad's foot is cleaner than yours ! Your feet are so dirty they could probably give me a disease !"
                    x "If you do anything to me I'm telling dad i caught something when you forced me to lick your feet"
                    show brother sadistic at right_small
                    with dissolve
                    brother_says "Is that so?"
                    x "(He takes a moment to check his own foot, and even though I can't see it, I can tell from his reaction that it's filthy.)"
                    x "(Then a sinister smile appears on his face, and i know what it means)"
                    brother_says "You're not  wrong little sis, my feet are pretty dirty... and that's why you're going to clean them for me."
                    brother_says "I am not retarded , if you liked him abusing you so much you wouldn't be sleeping in my room would you"
                    show madd paralyzed at left_small
                    x "(Fucking hell he saw right through it, just how disgusting is his foot ...i didnt even see it earlier but i know i cant avoid it anymore )"
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_107    


    scene madd_wake_up_brother_morning_foot_on_bed_madd_resisting_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    show brother cruel at right_small
    x "(Suddenly he jumps up puts his foot on the bed and grabs my head )"
    x "(Then he forces my head down towards his foot, pressing it against his foot making my lips touch his dirty foot )"
    brother_says "I said Clean it, Maddie. Now."
    x "(The stench slams into me instantly — thick, sour, and nauseating. His calloused dirt-magnet feet reek of old sweat, dried mud, and something rotten that clings to the ridges of his soles )" 
    x" (I can feel the grime pressing against my lips, the rough calluses scraping my skin while the smell floods my nose and throat.)"
    x "(I gag hard, eyes watering, but his hand is locked behind my head, forcing me to breathe it in deeper. Every breath pulls more of that filthy, humid foot-stink into my lungs.)"
    x "(My stomach twists. I want to scream, to shove him away, but the taste of his dirty sole is already seeping between my lips…)"   
    x "(The humiliation hits harder because it's him. My stepbrother. The one who 'saved' me. And now he's making me breathe in every inch of his grime like I belong to his feet.)"

    scene madd_wake_up_brother_morning_foot_on_bed_madd_foot_kissing_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd disgusted at left_small
    show brother dominant at right_small
    x "(I knew there was no way out of this. I start kissing the nail of his big toe seeing that was the only part of his foot that was somewhat less dirty than the rest. )"
    x "(He grabs my hair roughly and leans over me)"
    brother_says "Clean it well, Maddie. "
    x "(This is where it got worse , i had to use my tongue to clean the dirt from his foot, I put out my tongue and put it under the big toe and took it whole in my mouth )"
    x "(The smell is heavy and musky, like damp earth mixed with the sharp bite of skin that's been trapped in shoes for days. It clings to the inside of my nose with every breath.)"
    x "(But the taste is so much worse. My tongue slides under his big toe and the flavor explodes — salty, bitter, and gritty with dirt that scrapes against my mouth like sand. It's foul and coating my tongue instantly.)"
    x "(Knowing it's my stepbrother's foot makes it feel even more disgusting  and now I'm forced to lick and taste every filthy inch of him.)"
    x "(The contact my tongue makes with his skin is revolting. The rough calluses are like sandpaper against my tongue, not only is it dirty but also physically uncomfortable. )"
    x "(But i have no choice , i continue to use my tongue to touch his calloused skin with my tongue )"
    
    scene madd_wake_up_brother_morning_foot_on_bed_madd_foot_kissing_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    show brother dominant at right_small
    x "(he starts forcing my mouth closer to his foot, as saliva starts to mix with the grime on his foot, creating a thick, foul slurry that coats my tongue and fills my mouth with the stench of his dirty feet.)"
    x "(But it was a blessing in disguise that the saliva made it easier for my tongue to glide over the rough skin. It was still disgusting, but at least it reduced the friction and made it slightly more bearable)"

    scene madd_wake_up_brother_morning_foot_on_bed_madd_foot_kissing_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small
    show brother sadistic at right_small
    x "(He was staring directly down at me, his eyes filled with a mix of anger and satisfaction as he watched me obey his command )"
    x "(I continued to focus on the big toe, trying to clean it as best as I could, I would take it in my mouth and use my tongue to scrape the dirt off but it was a losing battle. )"
    x "(his foot was an endless source of filth, the cracks and crevices of his skin seemed to trap more and more dirt .)"
    brother_says "that's it, Maddie. Keep going. Clean it like you cleaned dad's foot. Show me how much you enjoyed that."
    x "( Asshole ,  as if i had a choice in the matter. you and your abusive father had me cornered and were holding my head to clean dad's foot. )"
    x "(How can you possibly compare the two? )"
    x "(I didnt respond to his words, knowing full well only way it ends is if i continue to obey him. )"

    scene madd_wake_up_brother_morning_foot_on_bed_madd_foot_kissing_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    show brother mocking at right_small
    x "(After sucking on his big toe for what felt like an eternity, I could feel my tongue growing numb from the constant contact with his filthy skin. The taste was so overpowering that it seemed to seep into every corner of my mouth, leaving a lingering stench that I couldn't escape.)"
    x "(I moved on to the webbing between his toes , it was as bad if not worse than the big toe, the dirt and grime seemed to be even more concentrated there, and the taste was even more intense. )"
    x "(Does this guy ever shower ?? how can someone be this dirty ? fucking disgusting )"
    brother_says "Not my footmat eh Maddie ? I will make you my footmat and you will like it. "
    brother_says "If i ever join the gym , first thing I will do is run my sweaty feet all over your pretty face . Bitch like you who get pounded by their own father deserve to be treated like a footmat. "
    x "(Like his fatass ever goes to the gym, he is just a lazy slob who sits on PC all day and eats junk food, but The threat of his sweaty gym feet all over my face… the way he called me a footmat and threw Dad in my face like that… it's so cruel, so humiliating.)"
    x "( The smell… that thick, cheesy, musky stench that used to make me gag and twist my stomach… it's not hitting me as hard anymore. My nose is getting used to it. )"
    x "(My body is adapting to the constant assault of his foot-stink, just like it adapted to dad's ...Fuck not again....)"
    x "(Wait… is this whole thing just a sick setup? Forcing me to lick and breathe in his filthy feet over and over… is he trying to get my body used to his smell first? So when he finally tries to force himself inside me, my body won't reject him like it should?)"
    x "(The thought makes my skin crawl. My own stepbrother… using my mouth on his dirty soles as some kind of twisted training, getting me addicted to his scent so he can slide into my pussy without me fighting as hard. It's so creepy, so calculated.)"
    x "(Just like Dad did after I cleaned his feet… he tried to force himself in. Is this the same pattern? Is my stepbrother grooming me with his feet so my body accepts him as 'normal' before he takes the next step?)"

    scene madd_wake_up_brother_morning_foot_on_bed_madd_foot_kissing_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd traumatized at left_small
    show brother condescending at right_small
    x "(No no no , with each passing second my senses are being dulled, my body is getting more and more used to the stench and taste of his filthy feet. I can feel myself slipping deeper into this nightmare, becoming more and more desensitized to the humiliation and degradation.)"
    x "(My mouth is autonomously taking in his toes inside, my tongue moving on its own accord to clean the dirt off, even as my mind screams in protest. )"
    brother_says "That's right Maddie , all it Takes is a little push...See how obedient you can be when you just give in and accept it ?"
    brother_says "You know sis , I had a respectable view of all women few years back...then i saw how most of your kind picked other guys over me just because how i looked"
    x "(What the fuck , if you want me to feel bad for you at least stop trying to force your foot in my mouth while you say it )"
    x "(Wait perhaps i could learn something from this... if i get to know him better , maybe i can manipulate him . Maybe even against Dad ! Oh how sweet it would be to turn the tables on the two of them and make them suffer like they made me suffer. )"

    scene madd_wake_up_brother_morning_foot_on_bed_madd_foot_kissing_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd think at left_small
    show brother dominant at right_small
    x "(He continued forcing my head so that my tongue could reach the base of the webbing between his toes. The good thing is that the skin there is all soft and folded, the bad part is it is full of dirt that's been trapped for days. )"
    x "(I keep thinking... if I just take it and act like I'm giving in, maybe I can figure him out better. Learn what makes him tick.  This might be my only shot to turn things around at least with him )"
    x "(I keep licking into that tight fold, my tongue scraping out more of the filth. The smell keeps hitting me fresh every time I breathe, but it's not making me gag as hard now. My body is getting used to it... and that thought scares me more than anything.)"
    x "(The webbing is easier on the tongue due to its softness but the taste is fouler than the big toe, I had to make my choice which part of his foot to focus on without him getting angry at me)"

    scene madd_wake_up_brother_morning_foot_on_bed_madd_foot_kissing_7
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd conflicted at left_small
    show brother angry at right_small
    x "(I move away from the webbing of the foot and put his toe in my mouth again sucking on it with as much force as I can then slowly moved my tongue to the ball of his foot )"
    x "(Was it his forceful hand or my tongue getting used like that but involuntarily moans start escaping my lips )"
    brother_says "Fucking disgusting, Maddie. You women are all like that...Never give the good guy a chance but when someone starts treating you like trash, you eat it up. "
    brother_says "You might not know it about Dad , but he used to be a real good person before..."
    x "(He suddenly paused as if he himself was sorrowful about his father, but then he continued with a smirk )"
    brother_says "Before he experienced the real world and learned that his whole life, all his efforts to be a respectable person were all for nothing. "
    x "(He suddenly got angry again, his eyes flashing with rage as his hands reached for something in his shorts )"

    scene madd_wake_up_brother_morning_foot_on_bed_madd_foot_kissing_8
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    show brother cruel at right_small
    x "(his hands suddenly get a hold of my hair again and he starts pulling it hard, his other hand pulls out his cock and he holds it in my hand while still forcing my head down to his foot )"
    brother_says "Its you fucking women who ruined the world, you and your disgusting obsession with looks. Now look at yourself"
    brother_says "Earlier you said 'im not your footmat' bitches like you are gonna be what i ask them to be . If i ask you to be a toilet and drink my piss, you will do it. "
    brother_says "If i ask you to hold my cock in your mouth while i play counter strike, you will obey . And when you do everything I say, I will use my dick to fuck you like a good little footmat. "
    brother_says " A very pregnant footmat , Maybe You're already pregnant with dad's baby  ? Maybe you are already carrying his child in your belly, and that's why you let him do whatever he wants to you. "
    x "(The disgust is overwhelming. Not just at what he's saying, but at how broken he sounds underneath all that rage. He really thinks the world — and every woman in it — ruined him just because girls didn't pick him. He's just another angry, lonely guy who got rejected too many times and decided every woman deserves to be treated like trash.)"
    x "(I actually feel sorry for him in this moment. Under all the threats and the cruelty, I can hear the pain. The guy who used to respect women until life kicked him in the teeth. Now he's taking it all out on me because I'm the only one he can control. It's pathetic... and terrifying for me  at the same time.)"
    brother_says "That's ...the only way... to get back at the world for treating me like that..."
    x "(There was actual sorrow in his voice as he said that, and i could tell he believed all of it .)"
    brother_says "Only way to ensure my future son wont go through what i did..."
    x "(His hands suddenly got rough again)"
    brother_says "Is to pick a mother which is insanely beautiful . So if he gets your looks, the world will treat him better than it treated me. "
    x "(The way he said that... the way he talked about his future son... it was like he was talking about a trophy, not a human being. He just wants a pretty face to show off, someone who can give him a son with good face . It's so shallow, so twisted.)"
    x "(With that he put his dick back in his shorts but i finally get it  )"

    scene madd_wake_up_brother_morning_foot_on_bed_madd_foot_kissing_9
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd sad at left_small
    show brother dominant at right_small
    x "(I continue cleaning his filth with a broken look on my face, I had a better understanding of him now )"
    x "(But the resistance inside me was diminishing rapidly, I felt so bad for him that I wanted to comfort him, to tell him that he's not worthless, that he's not a monster. Difficult it may be with the way he's treating me, I still want to reach out to him in some way. )"
    x "(No child starts out as a monster. Maybe he worked hard to become something , hoping one day someone would see past his looks and treat him with kindness. But instead, it never got better for him .)"
    x "(I knew he was in one of the top colleges in the country studying computer science, I dont know what happened after that but he also got very rich with cryptocurrency and stocks, but it seems like all that success just made him more bitter and resentful. )"
    x "( Life is so unfair, isn't it? He had so much potential, but instead of using it to build a better life for himself, he let his bitterness consume him. Now he's taking it out on me)"
    x "( Its all a vicious cycle. He was hurt by the world, so he hurts me. I was hurt by him and Dad, maybe in the future I will hurt someone else. It's so sad, so tragic.)"
    x "( I wish..i could break this cycle. I wish I could find a way to heal him)"
    x "( I can never genuinely love someonlike like him but i guess only way to break the cycle is to pretend to love him, to show him kindness and compassion even when he doesn't deserve it. )"

    scene madd_wake_up_brother_morning_foot_on_bed_madd_foot_kissing_10
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small
    show brother possessive at right_small
    x "(After my internal thoughts , i started to feel a strange sense of empathy for him. I actually started serving him with my tongue like I was doing it out of love, not just obedience. )"
    x "(I could feel the grip of his hand on my hair loosen slightly, as if he could sense the change in my attitude. )"
    brother_says "That's right Maddie , show your owner some love. "

    scene madd_wake_up_brother_morning_foot_on_bed_madd_foot_kissing_11
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd submissive nod at left_small
    show brother dominant at right_small
    x "( My brain was no longer registering this smell as something disgusting, it was just... there. A constant background presence that I had to deal with, but it wasn't making me gag anymore. )"
    x "( You cant blame a man for not cleaning his feet when all he's faced in his life is neglect and rejection. )"
    x "(Hearing his painful voice as he talked about his past, his bitterness snapped something motherly inside  me. )"

    scene madd_wake_up_brother_morning_foot_on_bed_madd_foot_kissing_12
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd flustered at left_small
    show brother possessive at right_small
    x "(I wasn't just cleaning his foot anymore. I was serving it with real passion now, my tongue moving with purpose, sucking on his toes harder, licking deeper into every crease like I actually wanted to please him. My head wasn't being forced as much anymore — I was pressing my face into his sole on my own.)"
    x "(The smell hit me the same as always but it didn't make me sick. It was just... his smell. Thick and heavy and all over my face, and for the first time it felt right instead of wrong. Like I was supposed to be breathing it in while I took care of him.)"
    x "(My thoughts about his foot completely flipped. It wasn't gross anymore. It was the part of him that needed the most love, the part everyone else ignored. Licking it clean felt good now because it meant I was giving him something no one else ever did — real acceptance, even the dirty parts.)"
    x "(Every lick was me telling him he wasn't worthless. Every breath of that strong foot smell was me showing him that someone could care about him exactly like this. It gave me this warm feeling in my chest, like I was finally doing something good in the world instead of just surviving it.)"    

    scene madd_wake_up_brother_morning_foot_on_bed_madd_foot_kissing_13
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd processing at left_small
    show brother possessive at right_small
    brother_says "Good girl , I dont know why you were so resistant at first, but I'm glad you finally understand. You belong to me, Maddie. You're my footmat "
    x "(The words didnt hurt me anymore, they just felt... a hurting mans way to cope with his pain.  )"
    brother_says "You know, Dad bagged your Mom just like this... he treated her like a footmat, made her clean his feet even his asshole, and then he fucked her like a dog. And you know what? She loved it. She loved being treated like that, she loved being his assmat. "
    brother_says "And they ended up getting married...That's when i learned the true way the world works. "
    x "(is that it? Is that why he's treating me like this ? Learning from his dad's example? Is he trying to recreate that dynamic with me so he could feel like he's in control for once )"
    x "(That along with the fact that he wants to put a baby in me ...yeah that part is really fucking creepy and I cant help him with that )"
    brother_says "You will learn your place by my side and you will like it just like your mom did. "
    x "(as he says that he puts a larger part of his foot in my mouth, forcing me to take in more of the stench and filth.)"

    scene madd_wake_up_brother_morning_foot_on_bed_madd_foot_kissing_14
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd inheat at left_small
    show brother sadistic at right_small
    x "(With the larger part of his foot in my mouth, i was almost completely overwhelmed due to the intensity . As if all  the oxygen in the room was being replaced by the stench of his foot, only taste lingered in my mouth was the foul flavor of his filth. )"
    x "(but i endured it and kept a constant eye contact with him, trying to show him that i was doing this for him, not just because i had to. )"
    brother_says "heh, the way you're looking at me right now... it's like you're actually enjoying this. fucking women are all the same "
    x "(Even with everything so twisted and wrong, something deep inside me was pulling me to submit. My womanly brain was kicking in hard, telling me this was what I was meant for — to give in, to serve, to let him own me completely so the world could be a better place. It was scary how natural it felt now.)"
    x "(I was actually liking the taste now. That foul, dirty flavor that used to make me gag wasn't foul anymore. It was rich and heavy and all him. Every time my tongue dragged across his skin, the taste filled my mouth like something I was supposed to swallow, something that made me feel closer to him instead of disgusted.)"
    x "(The smell was the same way. That thick, heavy stench that used to choke me was now wrapping around my head like a warm blanket. Breathing it in deep made my whole body feel soft and submissive. It wasn't disgusting — it was his, and I wanted more of it. I wanted it to stay in my nose and lungs so I could carry him with me.)"
    x "(My brain kept telling me to give in harder. As a woman, this was what I needed — to stop fighting and just let him take control. The more I submitted, the more that warm feeling in my chest grew. I wasn't just enduring it anymore. I was craving it. Craving the way his foot tasted, the way his smell made my head spin in the best way.)"
    x "(and it was justifying all that under the pretext that it was for him, that I was doing this to make him feel better about himself. )"

    scene madd_wake_up_brother_morning_foot_on_bed_madd_foot_kissing_15
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd salivating at left_small
    show brother lustful at right_small
    x "(He pushes his foot deep into my mouth one more time, making sure to get every inch of his filth inside me. I could feel it some of his dead skin and dirt was already on my face but i actually liked it now, it was proof that I was doing something right )"
    x "(Something my body was craving more and more with each passing second. To be covered in his filth, to be filled with his stench . )"
    brother_says "Fuck this is actually making me hard, Maddie. I never thought I'd get off on this, but seeing you like this... it's turning me on. "
    brother_says "I wish i could have been the one to take your virginity "
    x "(The way he said that... it was like a twisted confession. He's already made it clear that he wants to be the one to impregnate me perhaps even if dad is the one who got me pregnant, he will wait for me to give birth and then try to put his seed in me. It's so creepy, so possessive.)"
    brother_says "Well you're open for all holes now, aren't you slut? "
    x "(He's trying to shame me for doing things with Dad, but he wants to be the one to do those things with me. what a hypocrite. )"
    x "(With that he pulls back his foot from my mouth, leaving me gasping for air but also feeling this strange sense of loss. I had gotten used to the feeling of his filth in my mouth, and now that it was gone, I felt empty and desperate for more.)"

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd anxious at left_small
    show brother possessive at right_small
    x "(He pulls away my blanket and climbs into bed right next to me)"
    x "(Then he pulls me into his lap, wrapping his arms around me and holding me close. I can feel the heat of his body against mine, and the smell of his foot still lingers on my face, making the whole situation even more intense.)"
    x "(I could feel his hardon pressing against my thigh, and I knew what he wanted. But I was still so scared, so unsure of how to respond. )"
    brother_says "This is your sole duty now, Maddie. Satisfy me in every way you can. "
    brother_says "I know you're already a good daughter to Dad , but now you need to be a good sister to me too. "
    x "(I had my eyes lowered to the floor, but I could feel his gaze on me, and I knew he was waiting for me to say something. )"

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd shocked at left_small
    show brother dominant at right_small
    x "(Suddenly there is a look of anger in his eyes, as he growls . As soon as his voice raised i was so scared i was looking directly at him, trying to figure out what i did wrong )"
    brother_says "Well since you want to be such a good family member, I am gonna fuck you too, Maddie. I'm gonna fuck you like a good brother should. "
    x "(As soon as he finished his sentence , he got closer to me and without any warning, he started kissing me. )"
    x "(It wasnt a gentle kiss, it was rough and desperate, parting my lips and forcing his tongue inside. My body was already conditioned to take his filth, so it didn't fight back as much as I expected.  My mouth opened up and let his tongue in, even as my mind screamed in protest. )"
    x "(The taste of his tongue was just as bad as his foot, but it was also... different. It was warm and wet and alive, unlike the cold, dead filth of his foot. )"
    x "(Seeing that i offered no resistance, he slowed down the kiss, his tongue moving more gently now trying to connect with my body instead of just forcing himself in. )"

    label WHAT_HAPPENS_NEXT:
    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd conflicted at left_small
    show brother possessive at right_small
    x "(He slowly lifts my body , i felt so weak and helpless in his arms, but at the same time there was this strange sense of comfort. Like being taken care of, even if it was in the most twisted way possible. )"
    brother_says "I wanted to be your first time, Maddie. "
    x "(He moved his leg from the floor to the bed, and then he laid me down on the mattress, still holding me close and lowered me back onto his  lap. )"
    x "(After my lungs and mouth were filled with his foot-stench for so long, the taste of his tongue was actually kind of... nice? the texture definitely was an upgrade from his foot )"
    brother_says "imagine if i was your first, Maddie. We could have had something really special, you and me. "
    x "(there was a hint of sadness in his voice as he said that, like he was mourning the fact that he missed out on being the one to take my virginity. )"
    if madd_is_virgin:
        x "(Where the fuck did he get that  idea that I lost my virginity to Dad ? was it the moans from his room that made him think that ? or did he just assume that because of how much I was time i was spending with Dad ? )"
    else:
        x "(I was so confused by his statement, I had no idea where he learned that I lost my virginity to Dad. But maybe he made two and two together, seeing how much time I was spending with Dad and hearing the moans from his room, he just assumed that I lost it to him. )"
        x "(He wasnt wrong, but it was not by choice. I was forced into it, and it was a traumatic experience that I wish I could forget. )"
    x "(his hands continue to run on my body as he talks like a desperate man trying to hold onto something that slipped through his fingers. )"

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    show brother cruel at right_small
    brother_says "but you had to give your virginity to dad didnt you ? You had to let him fuck you like a dog, and you just took it. "
    brother_says "I bet you didnt even fight back , you fucking slut. I heard your moans... Sounded like a bitch was getting put down. "
    if madd_is_virgin:
        x "(He's wrong... I'm not... I haven't... but if he thinks I already gave it away, is he going to try to 'claim' what he thinks is left? Or punish me for 'choosing' Dad first? )"
        x "(But if i tell him now that I'm still a virgin, he will definitely try to take it from me himself, and that thought terrifies me even more. )"
    else:
        x "(It wasn't by choice... Dad forced me... but the way I screamed and begged at the end... how can I ever explain that? Brother will never believe me. He'll think I wanted it. )"
        x "(And now he's got me on his lap, kissing me, rubbing that hard dick against my thigh... knowing I'm already 'broken in'... Is he going to make me admit it? Make me tell him how much I came while Dad was inside me? )"

    x "(He put his hand behind my head again and grabbed a fistful of my hair, pulling it back making my head arch up and exposing my neck to him. )"
    x "(He then started kissing and biting on my neck, his teeth sinking into my skin and leaving marks. )"

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd trembling at left_small
    show brother dominant at right_small
    x "(He started licking from the bottom of my neck up to my jawline, his tongue tracing over the sensitive skin and leaving a trail of wetness in its wake. )"
    x "( The words he was saying were all leading up to one thing, and I knew it. He wanted to take it to the next level. He wanted to fuck me. )"
    x "(My hands were involuntarily clutching the blanket, gripping it tightly as if it could somehow protect me from what was coming. )"

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small
    show brother dominant at right_small
    x "(The room was silent except for the sound of his tongue on my skin and the heavy breathing between us. I could still feel the hardon pressing against my thigh )"
    x "(the sound of his tongue smacking against my skin was almost hypnotic, lulling me into a strange state of submission. The wet and warm trail of his tongue was like a signal to my body, telling it to relax and let go. )"    

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_7
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    show brother vindictive at right_small
    brother_says "I lost all hope when i heard you moaning Maddie. I knew you were getting fucked by Dad and the moans you were making ...I had heard those moans before, it definitely did not belong to someone who was hating it. "
    brother_says "I wanted to be the one to break you, Maddie. I wanted to be the first one to make you scream like that... the one who took your virginity."
    brother_says "But when I heard those moans coming from his room... the way you were begging and crying out... I knew it was already over. I felt so fucking hopeless. Like everything I wanted was stolen right out from under me."
    x "(Right after saying those words , laying out all his feelings of loss and despair, he started spanking me )"
    x "(It wasnt a hard spanking, but more like when you are punishing a child for doing something wrong. It was like he was punishing me for 'choosing' Dad over him, for giving away what he wanted to be the one to have. )"
    x "(While his tongue stayed on my neck, the smell of his saliva mixed with the stench of his foot still on my face, creating this overwhelming sensory experience  )"
    brother_says "Fuck , whatever now... now that my hopes of having you all to myself are completely shattered, I might as well just fuck you like a dog. "
    brother_says "First i will make you clean me like one..."

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_armpit_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    show brother dominant at right_small
    x "(After he says that , he removes his shirt shownig his excessively hairy body )"
    x "(The sight of his hairy chest and armpits made me feel sick, the hand behind my neck started pushing my head up towards his armpit. Fucking disgusting ...i just cleaned his foot, now i have to clean his armpit ? )"
    x "(The closer my face gets, the stronger it hits me — that thick, sour, cheesy musk that only builds up when a guy hasn't showered in days. It's heavy and humid, like warm spoiled milk mixed with sweat and old deodorant that's long since given up.)"
    x "(The heat is radiating off it in waves. His armpit is literally steaming from being trapped under his shirt all night. I can feel the warmth on my cheeks before I even touch it.)"
    x "(And the smell... fuck... it's getting worse with every inch. That deep, masculine stench that clings to the back of your throat. It's so strong I can already taste it on my tongue and he hasn't even forced me in yet.)"
    x "(Every second my face gets pushed closer, another second of my resistance dies. I can feel it happening — the part of me that still says 'no' is getting quieter and quieter. Soon there won't be anything left but the broken girl who licks whatever she's told to lick.)"
    x "(The heat... the smell... it's wrapping around my head like a fog. I can already feel my brain starting to go soft, just like it did with his feet. My body is learning to accept it. To crave the filth. To need it.)"
    x "(I don't want this... but my face is still moving closer. And some sick part of me is already preparing to open my mouth.)"


    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_armpit_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    show brother cruel at right_small
    brother_says "go on clean it, Maddie. Bitches like you who want to get pregnant by their own father deserve to be treated like this. "
    x "( I dont know how much longer I can hold on to my sanity. The way he said that... the way he threw Dad in my face like that... )"
    x "(I wanted to stay away from his armpit as much as possible, i started licking near the edge of it, trying to avoid the center where the smell was strongest. )"
    x "(I mustnt let him see that my resistance is fading, the more i get closer to the armpit, the more i feel like giving in )"
    x "(I was holding on to my breath...as long as i still had some ounce of sanity left, i didnt want to breathe in that stench. )"
    brother_says "Stupid Bitch, Didnt i told you to clean it ?  Get in there deep , I want it shiny with your saliva. "
    x "(That's when i knew there was no way to avoid this..)"

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_armpit_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd traumatized at left_small
    show brother dominant at right_small
    x "(He finally forces my face right into the hairy mess. The wet, sticky hair presses against my nose and lips.)"
    x "(The heat is insane. His armpit is burning hot against my face, like a furnace of sweat and musk. I can feel it seeping into my skin.)"
    x "(He pushes my head into his armpit, no way out anymore. I couldnt hold my breath anymore,I have to inhale... and when I do, the full force of his armpit stench floods my lungs. It's so strong it makes my head spin.)"
    x "(My tongue slowly starts moving on its own, pressing against the sweaty skin and trying to spread my saliva around like he said. The taste hits next as the wet hair brushes my lips — salty, bitter, and so fucking nasty. My stomach lurches but I don't pull away. I can't.  )"
    x "(But for some reason, my body was loving it. The more I licked, the more that warm feeling in my chest grew. )"

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_armpit_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd inheat at left_small
    show brother sadistic at right_small
    x "(my eyes closed as I gave in to the sensation, letting my tongue slowly explore the sweaty terrain of his armpit. I was now heavyly breathing in the stench, letting it fill my lungs and wash over me. It was like I was drowning in it, but instead of panicking, I found myself sinking deeper into this strange pleasure.)"
    x "(With closed eyes it was almost as if my body was trying to disassociate from the reality that this was my brother's armpit but instead a potential mate's scent that I was supposed to be enjoying. )"
    x "(The more his armpit stench mixed with the stench of his foot along with the two tastes mixing in my mouth, the more i was accepting that letting him put his dick in me was inevitable. I was already so far gone, so desensitized to his filth, that the thought of him taking it to the next level didn't seem as terrifying as it should have been. )"
    brother_says "Look at you, Maddie. You're really getting into it now. I'm sure you would have been a great footmat for Dad too."

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_armpit_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd flustered at left_small
    show brother dominant at right_small
    x "(I was ashamed of how right he was. My breathing was heavy and ragged , it was trying to inhale as much of his stench as possible, and my tongue was moving faster and more eagerly than ever before. )"
    x "(I could see small drops of sweat forming on his skin, and my brain instantly associated that it wanted to drink it directly from the source)"
    x "(His messy armpit hair was now completely soaked with sweat and my tongue was lapping it up like a thirsty animal. Some of the hair was getting stuck in my mouth, some of it being stuck in my nose and i was loving every second of it. )"
    
    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_armpit_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd salivating at left_small
    show brother dominant at right_small
    x "(it was getting super sweaty now, the smell was getting even stronger and more intoxicating. I could feel his sweat in my hair, on my skin, in my mouth. I couldn't get enough of it... )"
    x "(And just like my mind wanted , i was drinking sweat directly from the source now, my tongue lapping up the salty liquid as it dripped down his skin. )"
    x "(The hair was now completely drenched, sticking to my face and making it even harder to breathe but every breath felt like a hit of pure pleasure. )"
    x "(Fuck ...Fuck...Fuck...I am losing myself in this, but I don't want to stop. )"

    scene black 
    with dissolve
    x "(I dont remember how long i continued to lick his armpit, it never stopped being pleasurable )"
    
    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_armpit_7
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd inheat at left_small
    show brother dominant at right_small
    x "(Its been an hour now, I was still hungrily licking his armpit, my face completely soaked with his sweat and filth. )"
    x "(I was so lost in the sensation that I didn't even notice when he stopped talking and just let me be. )"

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_armpit_8
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd submissive nod at left_small
    show brother mocking at right_small
    brother_says "Pathetic slut, you've been doing this for almost an hour now and you dont get tired at all"
    brother_says "My filth is your nutrition, isn't it ? You just keep licking and licking like a good little footmat. "
    x "(The way he said that... it was like he was mocking me for how much I was enjoying it. Like he couldn't believe that I could actually like his filth so much. )"

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_armpit_9
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd shocked at left_small
    show brother sadistic at right_small
    brother_says "You know what Freak ? My asshole is even filthier than anything else. I bet you would love to clean that too, wouldn't you ? "
    x "(The thought of his asshole SHOULD make me want to vomit, but instead it just made me feel this twisted sense of excitement. Something is breaking inside me, and, I dont know if this was temporary or permanent)"
    brother_says "During night you can sit under my chair with only your face on my chair while I use your face as my seat with your tongue inside my asshole, you can be my human toilet. "    
    brother_says "And I mean really filthy, Maddie. I'm talking about the kind of asshole that hasn't been washed in days. Thick, dark hair matted with full of ass sweat. When I sit on your face, that hot, sweaty ring is going to press right against your nose and mouth, smearing all that filth across your pretty face."
    brother_says "My asssweat is really strong, Maddie. I bet you would love to taste it, wouldn't you ? When I sit on your face, the sweat is going to drip down into your mouth directly like dripping honey. I do get really sweaty when i play CS ."
    brother_says "You'll have to push your tongue deep inside — past the rim, into the tight, wrinkled hole. It'll taste like pure concentrated ass: salty, metallic, earthy, with chunks of whatever I ate the day before still clinging to the walls. You'll lick and suck and swallow every single bit of it while I play counter-strike or watch porn. And when I need to piss? You'll open your mouth and take it straight from the source, gulping it down like the desperate little toilet you are."
    brother_says "Hours and hours with your face buried in my crack, tongue cleaning my dirty asshole, breathing nothing but my rank. You'll start craving it. Begging for it. Just like you did with Dad's feet."
    x "(Oh my fucking god...)"
    x "(The images flood my mind instantly — my face trapped under his chair, nose buried in that hairy, unwashed crack, tongue shoved deep inside his filthy asshole, tasting every bitter, rotten inch while he ignores me and plays games. The smell... that thick, choking, cheesy-sour stench coating my lungs for hours... the taste of his but sweat sliding down my throat for hours...)"
    x "(Just one match of CS is around 90 minutes, imagining myself spending hours like that with his asshole on my face...  )"
    x "(My pussy clenches so hard I almost moan out loud. I can feel myself getting soaked just thinking about it. The thought of being used like that — completely degraded, completely owned, my only purpose being his personal human toilet — it's making my head spin with sick, twisted excitement.)"
    x "(My body wants it. It fucking want it so bad it scares me. It wants to be under that chair all night, face buried in his dirty ass, tongue working like a good little toilet while he treats me like furniture. My body want the taste, the smell, the humiliation... it want him to break me completely.)" 

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_armpit_10
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd inheat at left_small
    show brother dominant at right_small
    x "(Hearing that my body turned on heat instantly, my pussy was dripping wet and my nipples were hard as rocks. I was licking it with all intention now, my tongue moving faster and more eagerly than ever before. )"
    x "(As if my body was trying to please him so that he REWARDS me with the chance to lick his asshole. How low can I go if my body is considering that a reward ? )"
    x "(All of my senses were on fire now, the taste of his armpit sweat, the smell of his filth, the feel of his hair against my skin... and my brain thoughts about his asshole... it was all mixing together into this overwhelming cocktail of sensations that was making me lose my mind. )"
    x "(Fuck fuck fuck...what is happening to me ? It  was as if i was a dinner that he was preparing for an hour, and now  it was finally ready, I dont know if i would be able to say no to anything he wanted to do to me. )"
    brother_says "Did you just get turned on by the thought of being my human toilet, Maddie ? What a pathetic little slut you are. I bet you would love making out with my asshole while I play CS, wouldn't you ? "
    x "(My head burried itself deeper into his armpit, trying to hide the fact that I was blushing and trembling with arousal. )"
    brother_says " Well whatever your lunch time is over, now I will fuck you like a pet."
    x "(as he says that he pulls my head out of his armpit and kisses my neck as his hands wander down to my shorts pulling them)"

    
    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_penetration_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    show brother lustful at right_small
    x "(Cold air hits my skin as he tears off my shorts, exposing my bare legs and pussy to him. his hardon directly pressing my crotch now, making it impossible to ignore what he wants. )"
    x "(His hands dangerously close to my pussy and asshole. He uses his fingers to spread the area around my asshole making it expand )"
    brother_says "Damn i can feel the heat coming from your asshole on my fingers, Maddie. It's so tight and warm "
    brother_says "Your slut pussy is already soaking wet too. I can feel it on my fingers as well. Were you this dirty of a whore before you started fucking Dad ? "    
    x "(His crude words hit me like a slap... but instead of anger, a shameful heat floods my core. My pussy clenches around nothing, betraying me completely. I hate how my body responds to his degradation... )"
    x "(I was never like this before... but after everything with Dad, and now this... am I really turning into their dirty little whore? The thought makes me tremble with a mix of horror and unwanted arousal... )"
    brother_says "Time to begin, Maddie. I'm going to fuck you like the whore you are. I'm going to take you right here on my bed, where you sleep. Next time you sleep here you will be reminded of how you belong to me"
    brother_says "and when you imagine me fucking you, you will think about how you belong to me. You will think about how you gave your virginity to Dad but now you're mine. "
    x "(After he said that he removes his shorts and he didnt waste a second before his dick tip was already pressing against my wet pussy, teasing the entrance. )"

    if character_relations["brother"]["intimacy"] < 80:
        menu:
            "Stand your ground" :
                if madd_willpower+2*(80- character_relations["brother"]["intimacy"]) >= character_relations["brother"]["lust"]:
                    show madd angry at left_small
                    x "If you put it in, I am telling dad that.."
                    x "(Cmon Maddie, think...think what would scare him)"
                    x "That you tried to kill his child that is inside me so you could replace him."
                    show brother shocked at right_small
                    brother_says "You fucking bitch...I didnt try to kill no child"
                    x "(I could sense him hesitating , now's the time )"
                    x "Not only will he be pissed I am willing to bet he would report you to the cops thinking i was pregnant"
                    brother_says "This will not end well for you , you lying whore ...."
                    brother_says "I will have my way one way or another"
                    x "(he says that as his grip on me loosens , I push myself away from his grip eager to get away from him)"
                    x "(I quickly got out of the bed , fixed my clothes and went out to the lobby area avoiding this nightmare)"
                    brother_says "I will remember this Maddie , This is not over !!!!"
                    $ character_relations["brother"]["anger"] +=20
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_108
                    $ character_relations["brother"]["intimacy"]+=7
                    call advance_time_and_check(minutes=120) 
                    $ madd_willpower=max(madd_willpower-20,0)
                    jump home_areas
                else:
                    $character_relations["brother"]["lust"]=0
                    $character_relations["brother"]["anger"] +=20
                    show madd trembling at left_small
                    x "At least dad's dick is pretty big , I love him inside me so much ! "
                    x "If you do anything to me I'm telling dad i caught something when you tried to force yourself in my pussy"
                    show brother sadistic at right_small
                    with dissolve
                    brother_says "Is that so?"
                    x "(He takes a moment to think)"
                    x "(Then a sinister smile appears on his face, and i know what it means)"
                    brother_says "I am not retarded , if you liked him abusing you so much you wouldn't be sleeping in my room would you"
                    show madd paralyzed at left_small
                    x "(Fucking hell he saw right through it, just how disgusting is his foot ...i didnt even see it earlier but i know i cant avoid it anymore )"
                    x "(Shit, there is really no way to stop him now...I'm all out of ideas)"
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_109    

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_penetration_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd traumatized at left_small
    show brother possessive at right_small
    x "(The tip was now inside me, i could feel it was still far from its full length or girth but it was already stretching me in a way that made me feel like I was being filled up. )"
    x "(Oh god... his dicks tip is actually inside me. My brother cock — the same guy whose dirty feet I just licked for an hour, whose sweaty armpit I drank from — is pushing into my pussy. The head is stretching me open right now.)"
    x "( This is the boundary. The one that was never supposed to be crossed. Family. Brother. Even if step, it's still brother. And now he's inside me. There's no undoing this. No going back to 'we're just siblings' or 'this never happened.' I let it happen — or my body did — and now it's real. Irreversible. Forever. Every time I look at him, every time I sleep in this bed, I'll remember exactly how his tip felt sliding in. How I crossed that line and can never uncross it.)"
    x "(The heat... fuck, the heat is insane. His penis is burning hot inside me, throbbing and pulsing like it's alive, flooding my insides with this deep, heavy warmth. It's so different from the cold, grimy filth of his feet or the sour musk of his armpit — this is living heat, claiming me from the inside out. I can feel it radiating through my walls, making my whole lower body feel soft and full and owned. My pussy is clenching around it on its own, squeezing that heat deeper like it wants more.)"
    x "( I hate how good the warmth feels. It's betraying me, turning this violation into something my body is already craving. The stretch, the burn, the way it's heating me up from within... it's making me drip even more around him. I'm getting wetter for my own brother's penis and I can't stop it.)"    
    brother_says "Wow you were even wetter than I thought, Maddie. But fuck your pussy is top tier, what the fuck... I can feel how tight it is around me, it's like you're made for me. "
    brother_says "I bet anyone who has been inside you would say the same thing, but I know for sure that Dad would say that too. He probably thought he was the only one who could fit inside you, but look at you now... you're all stretched out and filled up by me. " 
    brother_says "Maybe your first child will not be with me , but I will make sure to put my seed in you at least once."
    x "(he really wants to impregnate me, doesn't he? How long has he been fanatasizing about this? Did he start fantasizing about it after he found out I lost my virginity to Dad? Or was it always there, lurking in the back of his mind, waiting for the right moment to come out?)" 
    brother_says "Fuck time to go deeper, Maddie. I want to feel you stretched around my whole length, I want to feel you completely filled up by me. "
    x "(I gulped hard as he started pushing in deeper )"
    
    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_penetration_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd conflicted at left_small
    show brother horny at right_small
    x "(With his hands under my ass and other tightly gripping my neck, He started lifting my hips up and down, fucking me harder and deeper. As his dick went in deeper inside me involuntarily moans started escaping my lips )"
    x "(The room was full of the clapping sound of his hips slapping against mine, the wet squelching noise of my pussy being filled up, and the desperate moans that were coming from me)"
    x "(He's controlling everything now. His hands are locked under my ass and around my neck, lifting my hips up and down his dick in this slow, deliberate rhythm. Not fast. Not rough. Just... steady. Deep. Every time he pulls me up I feel the thick head drag along my walls, almost slipping out, then he lowers me back down so I sink onto him inch by inch until I'm completely full again.)"
    x "( The heat is everywhere. That burning, throbbing heat of his penis buried inside me, pulsing against my cervix with every slow drop.)"
    x "(And the whole time I'm thinking the same thing on repeat: this is my brother. My stepbrother. His dick is inside my pussy. I'm being fucked by family. Incest. Pure, filthy, irreversible incest. The same guy whose dirty feet I licked clean, whose sweaty armpit I drank from like a desperate animal... now he's balls-deep in me, pumping me up and down like I'm nothing but a warm hole for him to use.)"
    x "( Every slow thrust is a reminder that the boundary is gone. I crossed it. My body crossed it. And now there's no going back. I'm letting my brother fuck me on his bed while I moan like a whore.)"
    x "(The rhythm is killing me. Slow enough that I feel every single inch, every vein, every throb of that heat stretching me open again and again. My pussy is gripping him so tight, sucking him back in every time he lifts me. The wet sounds are getting louder, sloppier. My own juices are coating his shaft, making it easier for him to slide in and out while he controls the pace like he owns me.)"
    x "( And the worst part? It feels good. The heat, the stretch, the way his dick kisses my deepest spots on every downstroke... my body is loving it even while my mind is screaming that this is wrong. So fucking wrong.)"
    brother_says "Fuck listen to you, Maddie. Moaning like that while your own brother is inside you. You love it, don't you? Your tight little pussy is sucking me in like it was made for family dick."
    brother_says "I can't believe I've been holding back all this time... watching you with Dad, hearing you moan for him, knowing I could have been the one stretching you out like this. Fuck, I was so stupid. Should've just taken you the first time I heard your moans in the house. This feels too good to have waited."   

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_penetration_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd inheat at left_small
    show brother dominant at right_small
    x "(I was so lost in the sensation that I didn't even notice when he started speeding up his thrusts. )"    
    x "(Family bonds... they seemed like such a fragile illusion now. All the years of pretending we were just step-siblings, all the rules society drilled into us — they melted away the second his dick started moving faster inside me. I don't care anymore. I don't want to fight it. All I want is to give in to him completely, to surrender to his lust, to let him use me however he wants. Let him fuck his sister like the whore my body has made me)"
    x "(I keep wondering... what exactly broke me? Was it the thick, sour stench of his dirty feet that I licked for so long? Was it the salty, sweaty taste of his armpit that I drank like it was the best thing I'd ever had? Or was it the constant threat of becoming his human toilet — the way he described sitting on my face for hours while he played games? Maybe it was all of it combined. The filth, the smell, the degradation, the slow conditioning... it all worked. It turned me into this.)"
    x "(And right now... I feel so fucking good. Better than I have any right to feel. My whole body is buzzing with this forbidden pleasure. The heat, the stretch, the way he's using me like I'm nothing but his personal fucktoy... I don't want it to stop. I want to stay in this place forever. Lost in his arms, impaled on his  cock, moaning like a broken sister who finally accepted her place. No more guilt. No more fighting. Just this. Just him. Just giving in completely.)"
    
    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_penetration_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd inheat at left_small
    show brother lustful at right_small
    x "(My moans have completely changed now. They're no longer desperate or reluctant — they're soft, needy, almost... infantile. Like a baby crying and begging for its mother, except I'm not begging for milk or comfort. I'm begging for more of my brother's cock. Every time he slams me down I let out these pathetic, whimpering sounds that sound exactly like a helpless baby reaching for what it wants most. And what I want most right now is him. Deeper. Harder. All of him.)"
    x "(That's when it hits me — he's still not going all the way in. Even with the faster pace, even with how full I already feel, I can tell he's holding back. His cock is hitting a spot inside me that makes my eyes roll back, but there's still more. So much more.)"
    x "( The realization makes my whole body shiver with excitement. If this already feels this good... what would it feel like if he gave me every single inch? If he buried himself to the hilt and claimed the deepest parts of his sister? The thought alone makes my pussy clench violently around him.)"
    brother_says " I'm gonna knock you up, Maddie. If Dad didn't already put a baby in that belly of yours, then I will. I'm gonna fill my sister with my seed until it takes. You're gonna carry my child and there's nothing you can do about it now."
    x "( The thought of him knocking me up — of my own brother breeding me, of carrying his baby while Dad might have already done the same — it's too much. My body starts shaking.)"
    x "( The combination of his filthy promise, the realization that he's still not fully inside me, and the overwhelming heat of his dick pounding into me pushes me right to the edge. I'm so close to cumming. So fucking close. My pussy is fluttering around him, my moans turning into high-pitched, baby-like whimpers as the orgasm builds faster than I can control.)"

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_penetration_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd flustered at left_small
    show brother horny at right_small
    x "(His lips are moving up from my neck now, trailing hot, wet kisses along my jaw until they finally reach my mouth. He doesn't ask. He just takes. His tongue pushes past my lips, invading my mouth the same way his dick is invading my pussy — deep, possessive, and hungry.)"
    x "(I can't hold it anymore. The combination of his tongue in my mouth, his dick pounding into me, the filthy words about breeding me, and the realization that he's still not even fully inside — it's too much. My body shatters. I start cumming hard around my brother's dick, my pussy clamping down and pulsing violently as wave after wave of forbidden pleasure crashes through me. My moans turn into high-pitched, broken cries against his lips as I cum for him.)"
    x "(Oh god... I just came. I just came on my brother's dick. My own stepbrother's cock is inside me and I just had an orgasm from it. The thought hits me like a truck even as my body keeps twitching and squeezing around him.)"
    x "( I came from incest. From being fucked by family. And he knows. I can feel it in the way his grip tightens, in the way he groans into my mouth. He knows exactly what just happened. There's no going back from this. No pretending anymore. I came for my brother. I'm his now in every possible way.)"
    brother_says "Fuck... your pussy just went crazy on me, Maddie. You came so fucking hard I felt you squirting all over my balls. Look at the mess you made, you filthy little thing."
    brother_says "I knew those baby-like moans meant you were about to lose it. And now you're shaking and dripping all over your brother's cock like a good little sister should. That's exactly what I wanted."
    brother_says "You couldn't stop it even if you tried, could you? Your body just gave up and came for me. Perfect. Absolutely perfect."
    x "(His words are making the orgasm last even longer. He's right. I squirted for him. I came so hard for my own brother that I couldn't stop it. And now he knows exactly how broken I am for him. There's no going back. The line is completely gone. I'm a sister who cums on her brother's dick...)"
    brother_says "Remove your shirt, Maddie. I want to feel your body against mine. Skin to skin. I want your breast pressed against my chest while I fuck you. Take it off. Now."

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_penetration_7
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd flustered at left_small
    show brother debased at right_small
    x "(Even while I'm still shaking from the orgasm, his command makes something inside me obey instantly. My hands move on their own, pulling my shirt up and off. The second the fabric is gone and my bare skin meets his, the heat between us becomes almost unbearable. Chest to chest, brother to sister, nothing between us anymore. And I can already feel him getting even harder inside me, like the full contact is driving him wild too.)"
    x "(His greasy, fat chest is now pressed completely against my body. No shirt, no barrier — just his sweaty, hairy skin rubbing directly against my breasts, my stomach, my entire front. I can feel every roll of fat, every patch of thick hair, every bead of sweat smearing onto me. It's disgusting. So fucking disgusting. His body is soft and clammy in all the wrong places, yet here I am, chest to chest with my own brother while his dick is still buried inside me.)"
    x "(His stench was already deep in my lungs from licking his feet and armpit for so long, but now it's physical. I can feel it on my skin. His sweat is mixing with mine, his greasy chest sliding against my body with every thrust, transferring that thick, musky, unwashed smell directly onto me. It's coating me. Marking me.)"
    x "( I can feel the wetness of his sweat between us, the way his fat presses and molds against my smaller frame. It's revolting... and yet in this moment it feels so fucking good.)"
    x "(Being in full contact with his fat, sweaty body is making me lose my mind in the best way. The heat, the weight, the way his greasy skin sticks to mine — it's filthy, it's wrong, it's everything I should hate. But right now, with his cock still throbbing inside me after I just came for him, it feels perfect. Like I was always meant to be pressed against this disgusting, sweaty brother of mine.)"
    x "( His fat chest against my body, his stench all over me inside and out... I don't want to pull away. I want to stay like this forever, glued to him, covered in him.)"
    x "(Every time he moves, I feel his fat shift and rub against me, smearing more of his sweat onto my skin. It's so gross... but the more I feel it, the more my body relaxes into it. Like my brain has finally accepted that this is what I need now. My brother's greasy, fat, sweaty body pressed fully against mine while he fucks me. And the worst part? I love how disgusting it feels. I love being this close to his filth.)"

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_penetration_8
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd helpless at left_small
    show brother dominant at right_small

    x "(Because I came so hard, something changed. My pussy is even wetter now, more relaxed, more accepting — and his cock is sliding in deeper with every thrust. He's not holding back anymore. The head is hitting places it couldn't reach before, stretching me further, filling me completely.)"
    x "( His thrusts have become deeper, heavier, more deliberate, like my orgasm gave him permission to finally claim more of the space inside me . I can feel him bottoming out now, his fat body pressing harder against mine with every powerful stroke.)"
    x "(That's when it hits me — it's morning. The sun is up. The whole world is awake. People are starting their day, walking outside, living normal lives... while I'm in here getting fucked by my own brother. The only sounds in the entire room are the loud, wet clapping of my ass cheeks every time his hips slam into me, the obscene squelching of my soaked pussy being stretched around his dick, and my own desperate, broken moans echoing off the walls.)"
    x "(The reverberation is humiliating. Every clap, every wet slap, every moan bounces around the room and comes back to me louder than it should. It feels like the whole house can hear it.. I'm so humiliated... but my body is still loving every second of it.)"

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_penetration_9
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    show brother possessive at right_small
    brother_says "I'll pump my load straight into your womb today, Maddie. Every drop is going where it belongs. And when your belly grows, everyone will know I was the one who put it there. I'm going to make sure everyone knows exactly how you sounded while I was doing it. Every pathetic, high-pitched moan. Every time you cried out like a desperate animal. I'll tell them all how their sweet little Maddie begged her own brother to breed her."
    brother_says "The whole world will turn on you. Your friends, your college teachers, everyone who ever smiled at you — they'll all look at you with disgust. You'll become the girl who got knocked up by her stepbrother. The family whore who couldn't keep her legs closed for her own blood. No one will ever want you again."
    brother_says "And when you're completely alone, when the entire world has thrown you away like garbage... only me and Dad will still take you in. We'll be the only ones who still want you. The only ones who'll keep filling you up, one after the other. You'll spend the rest of your life getting passed between us — pregnant with my baby one year, then his the next. No escape. No choice. Just endless cycles of our cum and our children growing inside you."
    brother_says "You'll hate it at first. But eventually you'll realize this is the only place left for you. The only people who will ever 'love' you again are the two men who ruined you. And you'll thank us for it. Because without us, you'll have nothing. No future. No dignity. Just us. Forever."
    brother_says "You know what else I'm thinking? Maybe one day I'll bring Dad in here and we'll both fuck you at the same time. Double vaginal. Both our dick stretching that tight little pussy together. We'll see whose cum gets there first and knocks you up. A little competition between father and son. Wouldn't that be fun?"
    brother_says "Imagine both of us pumping into you at once, filling you up until you're overflowing. One of us will win. One of us will plant our seed deeper. And you'll just lie there and take it like the good little family toy you are."
    x "(The image his words paint is so horrifying it makes my blood run cold. Both of them inside me at the same time... their bodies pressed against me from both sides, their dicks rubbing together inside my pussy, competing to see who can breed me first. The thought is so wrong, so violating, so far beyond anything I ever imagined could happen to me. It's not just incest anymore. It's something even darker.)"
    x "(And yet... somewhere deep in the broken part of me that's been slowly accepting all of this, a small voice whispers that this is probably where I'm heading. That this might actually become my life. Being used by both of them together. Being their shared plaything. The terror is real, but so is this strange, heavy resignation settling in my chest. Like I've already lost the war and now I'm just waiting to see how deep the defeat goes.)"


    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_penetration_10
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small
    show brother dominant at right_small
    x "(I can't remember how long he's been going at it. Minutes? Hours? Time has completely dissolved. My body has been nothing but a warm, wet sleeve for his dick, bouncing up and down on his lap while the morning sun pours through the window. My mind is fogged with sweat, cum, and the constant, rhythmic slap of skin on skin. I don't even know if I've cum again or if I'm still riding the same endless wave from before.)"
    brother_says "Fuck... my whole body's getting soaked. Can you feel it? My chest, my stomach, even my back — everything's dripping. And my asshole... yeah, that's probably sweating too. I can feel the hair back there getting all wet and matted. Every time I thrust into you, I can feel it clinging to my skin."
    brother_says "When I'm finally done pumping every last drop of my seed deep inside that pussy of yours, I'm gonna make you clean it. With your tongue of course. You're gonna get on your knees, spread my cheeks, and lick every drop of that hot, salty ass-sweat off my hairy hole while it's still fresh."
    brother_says "And don't you dare miss a single spot. I want to feel that pretty little tongue of yours dragging through every sweaty crease, sucking the filth right out of my crack like it's the best thing you've ever tasted. Because after today, that's exactly what it is — your new favorite flavor. Brother sweat. Fresh from the source."
    x "( He's not just threatening anymore — he's describing it like it's already decided. Me on my knees, face buried between his fat, sweaty cheeks, tongue working overtime to clean his unwashed asshole while his fresh cum is still leaking out of me. The image is so vile, so completely degrading... and yet my body betrays me again. My pussy clenches hard around him at the thought, like it's already preparing to obey.)"
    x "(His pace suddenly changes — deeper, rougher, more urgent. I can feel him swelling inside me, getting closer . The sweat from his body is dripping onto mine now, mixing with everything else. And all I can think about is what's coming next. Not just his cum... but what comes after. The moment he pulls out and pushes my face into his crack. The moment I finally taste the one part of him I've been dreading... and craving... the most.)"

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_penetration_11
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd inheat at left_small
    show brother sadistic at right_small
    x "(Suddenly everything changes. His hands grip my hips like vices and he starts slamming me down onto his dick with brutal, merciless speed. No more slow, teasing thrusts — this is raw, violent pounding. Every time he drives upward, his fat body slaps against mine with a loud, wet crack that echoes through the room. My insides are being rearranged. I can feel his thick dick battering my cervix with every savage thrust, stretching me so wide it burns in the most fucked-up way.)"
    x "(My pussy is making the most obscene, wet sounds I've ever heard — loud, sloppy, squelching noises every time he pulls out and slams back in. It feels like my walls are being scraped raw, yet somehow I'm still dripping, still clenching around him like my body has completely given up and decided this is what it was made for. The heat is unbearable. His cock feels like it's burning me from the inside, throbbing and swelling as he uses me like a fleshlight.)"  
    x "(My moans have completely transformed. They're no longer soft or baby-like. Now they're loud, broken, animalistic screams that tear out of my throat with every brutal thrust. High-pitched, desperate wails that sound like I'm being destroyed — and I am. My voice cracks, turns hoarse, then rises again as he pounds even harder. I sound like a whore being ruined. A sister being broken. And I can't stop. I can't even try to stay quiet.)"
    brother_says "Fuck yes... listen to you. Screaming like a broken little whore. Your pussy is gripping me so fucking tight now. You love this, don't you? Love getting pounded like this by your own brother."
    x "(I can't even answer. All that comes out is another loud, broken moan as he slams me down especially hard. My vision is blurring. My body is shaking uncontrollably. And somewhere in the back of my mind, I realize this is it. This is the moment I completely lose whatever was left of the old me. The girl who resisted is gone. All that's left is this drooling, screaming, cock-hungry sister who wants nothing more than to be used like this forever.)"   

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_penetration_12
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd traumatized at left_small
    show brother dominant at right_small
    x "(His hands suddenly shift. The one gripping the back of my neck slides down my spine, rough and possessive, until it settles on my lower back. The other hand — the one that was controlling my hip — moves lower, fingers sliding between my ass cheeks. I feel one thick, sweaty finger press against my tight, untouched hole. Before I can even process what's happening, he pushes it inside me.)"
    x "(The intrusion is sudden and shocking. His finger forces its way past the tight ring, knuckle-deep in my asshole while his cock continues slamming into my pussy at brutal speed. The sensation is overwhelming — being filled in both holes at once. My ass clenches involuntarily around his finger, trying to push it out, but he just curls it inside me, using it like a hook to control my body.)"
    x "(He uses the grip in my ass to move me exactly how he wants. Every time he wants me to drop harder onto his dick, he pulls down with the finger buried in my asshole, forcing me to take him even deeper. It feels so wrong, so dirty, so completely violating — and yet my body is reacting like it's the most natural thing in the world. My pussy is gushing around his pounding dick, and now my ass is greedily squeezing his finger like it wants more.)"
    brother_says "Fuck... your tight little asshole is sucking my finger too. You really are a filthy little sister, aren't you? Getting finger-fucked in the ass while your brother destroys your pussy. I can feel both your holes clenching at the same time. You're loving this, you sick little whore."    

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_penetration_13
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd inheat at left_small
    show brother sadistic at right_small

    x "(He doesn't stop. Not even for a second. His hips keep slamming upward with the same brutal, punishing force while his finger stays buried deep in my asshole, curling and twisting inside me . Every thrust makes his finger push deeper, and every time he yanks down with that hooked grip, my body obeys like it's been trained for this. I'm being fucked in both holes at once and I can barely think straight anymore.)"
    brother_says "I'm being so generous right now, Maddie. Look at me — giving you pleasure with my finger in your tight little asshole while my dick destroys your pussy. Most brothers wouldn't be this nice. But I'm making you feel good, aren't I? You're dripping all over me, clenching around both my cock and my finger like a desperate little slut."
    brother_says "So it's only fair you return the favor. When I'm done filling you up, you're gonna push that pretty tongue of yours all the way deep inside my asshole. I want to feel it buried in there, licking and sucking like you actually want to be in there. Fair deal, right? My asshole might stink, but it's still cleaner than a whore's pussy. And we both know that's exactly what you are now."
    x "(His words are so cruel, so twisted, and yet my body reacts instantly. The idea of being forced to tongue-fuck his sweaty, unwashed asshole while his cum is still leaking out of me should make me want to vomit — but instead my pussy clenches even harder around his pounding cock.)"
    x "( He's right. This is what I've become. A sister who gets off on the idea of licking her brother's filthy asshole clean. And the worst part is... I know I'm going to do it. I know I'm going to push my tongue as deep as it can go and taste every inch of him.)"


    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_penetration_14
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    show brother possessive at right_small
    x "(Without warning, he suddenly yanks his finger out of my asshole. The sudden emptiness makes me gasp — my ass feels strangely hollow and needy after being filled for so long. Before I can even process the loss, he wipes his dirty finger across my back, leaving a wet, slimy trail of my own ass juices smeared across my skin. I can feel it dripping down my spine, marking me like some kind of filthy trophy.)"
    x "(Then he wraps both arms around me in a crushing bear hug, pulling me tight against his fat, sweaty body. My  breasts squished against his soft gut, and my entire body is trapped in his grip. There's no escaping now. No more bouncing up and down on his lap — he's holding me completely still while he starts slamming upward into me with brutal, punishing force.)"
    x "(And this time... he's going all the way in. Every savage thrust buries his entire dick inside me — balls-deep, stretching me wider than I thought possible. I can feel the head battering my cervix with every brutal slam, his thick shaft scraping every inch of my walls. The fullness is overwhelming. I can feel him in my stomach. In my soul. There's nowhere left for him to go — he's claimed every part of me.)"
    x "(My moans have completely changed again. They're no longer broken screams or animalistic wails. Now they're soft, feminine, completely submissive whimpers — high-pitched, breathy little sounds that sound like a woman who's finally accepted her place.)"
    x "( Every time he slams into me, a sweet, helpless moan escapes my lips. 'Ah... ahh... nngh...' They sound like they belong to a girl who's being properly fucked by the man who owns her. And I hate how natural they feel. How right they sound coming out of my mouth.)"
    brother_says "YES... that's it. Those are the moans. The exact same ones I heard coming from Dad's room. That sweet, broken little voice... that perfect submissive whimper. Fuck, Those sounds… fuck. I finally pulled the same pathetic little moans out of you that Dad did. I win.. I'm feeling so fucking good right now, Maddie. You have no idea how long I've waited to hear my own sister moan like a proper little whore for me."
    x "( He's actually proud that he managed to break me down to the same level as Dad did. And the worst part? I hate how right this feels. My body isn't fighting anymore. It's welcoming him. Preparing itself for his seed.)"
    x "( Welcoming the fact that I'm becoming exactly what he wants me to be.. My moans keep coming — soft, feminine, completely surrendered. I sound like a woman who's finally found her purpose. And as he holds me in that crushing bear hug, slamming into me with everything he has, I realize... this is it. There's no going back. I'm not Maddie anymore. I'm just the girl who lets her brother use her however he wants. And these soft, submissive moans are the sound of me finally giving up.)"
    brother_says "Keep making those sounds for me, little sister. Keep moaning like that while I fill you up. This pussy belongs to me now. I own it. I own you. There's no walking away from this"

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_penetration_15
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    show brother horny at right_small
    x "(I can feel it happening. His dick is throbbing violently inside me now — harder, thicker, hotter than before. It's swelling to its absolute limit, stretching me even wider as it pulses and jerks against my walls. Every vein is standing out, every inch of him is rock-hard and twitching like it's about to explode. He's getting bigger inside me. I can feel him growing, claiming even more space in my already-overstuffed pussy.)"
    x "(And I know exactly why. He got this excited because he finally broke me. Because he heard those soft, submissive moans come out of my mouth — the exact same ones I made for Dad. He's proud of himself. I can feel it in the way his dick is throbbing, in the way his arms tighten around me in that crushing bear hug. He's proud that he managed to turn his sister into the same broken, moaning little whore that Dad did. And that pride is making him lose control.)"
    brother_says "Fuck... fuck, Maddie... I can't... I can't hold it anymore. Your moans... those perfect little sounds... they're driving me insane. I got you to make them. Me. Not Dad. Me. I'm so fucking proud right now. I broke you just as good as he did. And now... now I'm gonna cum. I'm gonna cum inside you, little sister. I can't stop it. I don't want to stop it."
    brother_says "I'm gonna fill you up. I'm gonna pump every drop of my seed deep into that sister pussy. Right now. I can't control myself anymore. You're mine. You're fucking mine and I'm gonna breed you just like he did."
    x "(His words are desperate, ragged, completely unhinged. I can feel his entire body shaking as he fights to hold back for just a few more seconds. His dick is pulsing so hard inside me it feels like it's going to burst.)"
    x "( And I know it's coming. Any second now, he's going to flood me. He's going to pump his cum deep into my womb while holding me in this crushing embrace, and there's nothing I can do to stop it. Nothing I want to do to stop it. Because this is what I am now. His cum-dump. His breeding sister. And as his dick throbs one last time, impossibly thick and hard, I realize... I'm ready for it. I'm ready to be filled by my own brother.)"
    x "(My soft, feminine moans keep coming — sweet, submissive little whimpers that only make him throb harder. 'Ah... ahh... please...' I don't even know what I'm begging for anymore. For him to cum? For him to stop? For him to never stop? It doesn't matter.)"
    x "( Because in a few seconds, it's going to happen. And when it does, I'll finally be his in the most permanent way possible. Marked from the inside out. And the thought makes my pussy clench around him one last time, squeezing that throbbing, swollen dick like it's trying to milk him dry before he even starts.)"

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_penetration_16
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    show brother debased at right_small

    x "(And then it happens. His dick suddenly swells to its absolute limit inside me — impossibly thick, burning hot, and pulsing like a second heartbeat. I feel the first powerful jet of cum explode deep against my cervix, so thick and heavy it feels like liquid fire slamming into my womb. Then another. And another.)"
    x "( Each spurt is stronger than the last, flooding my insides with wave after wave of scorching, sticky seed. I can feel it — the pressure building, the warmth spreading through every inch of my pussy, coating my walls, filling every crevice until my womb is completely full.)"
    x "( It's so much. Too much. I can feel it leaking out around his dick, dripping down my pussy in thick, warm rivulets, but he just keeps cumming, keeps pumping more and more of his load into me like he's trying to mark me from the inside out.)"
    x "(The sensation is overwhelming. My pussy is clenching and milking him on its own, squeezing and fluttering around his throbbing dick like it's trying to pull every last drop deeper into my womb. The heat is spreading through my core, filling me with a heavy, liquid fullness I've never felt before.)"
    x "( It feels like his cum is claiming me permanently. Like his cum is rewriting my body from the inside. And the worst part? My pussy is actually thanking him for this. Clenching and squeezing like it's grateful to be filled by my own brother's cock.)"
    x "(The realization hits me like a truck as the last spurts finally slow. I might be carrying his child now. My stepbrother's baby might be growing inside me. The same brother who spent the entire morning turning me into his personal fucktoy, who made me lick his filthy feet and armpit, who just finger-fucked my ass while he destroyed my pussy.)"
    x "( And if anyone finds out... if my friends, anyone from college, anyone from my old life finds out that I let my own stepbrother creampie me... that I moaned for him like a broken little whore while he bred me... my life is over. I'll be the girl who fucked her brother. The family slut. The one who got pregnant by her stepbrother. No one will ever look at me the same way again.)"
    x "(And then there's Dad. What will Dad do when he finds out? When he finds out that I let his own son cum inside me? That I let him breed me? Will he be angry? Will he punish me for 'cheating' on him with his son? Or will he just laugh and join in?)"
    x "( Will he make me take both of them at the same time, competing to see whose cum stays inside me longer? The thought makes my stomach twist with shame... but my pussy clenches again at the idea. I'm so fucked. So completely, irreversibly fucked. And there's no going back now. This is my new normal. Being filled, marked, and used by my own brother. And the scariest part? I don't even want to fight it anymore.)"
    brother_says "Fuck... fuck yes, Maddie... take it all. Every single drop. You have no idea how good that felt. How long I've been waiting to do this. I did it. I made my own sister moan like a broken bitch for me. Just like she does for Dad.. And now I'm inside you. My cum is inside you. I just bred my own sister. How fucked up is that? And I'm not even close to done with you. I'm so fucking happy I could die right now."
    brother_says "And I'm not pulling out. Not for a long time. I'm gonna stay buried inside you all day, keeping you full and warm. The day has just started and you're already leaking my cum. You're stuck with me, little sister. My cock, my cum, my rules. Forever."
    x "(But he doesn't stop. Even after he's finished cumming, even after he's pumped every drop of his seed deep inside me, he keeps thrusting. Slow, deep, lazy strokes that push his softening dick through the thick mess of his own cum.)"
    x "( I can feel it — the way his cock is shrinking inside me in real time. Every few seconds it gets a little smaller, a little softer, but he keeps moving, keeps sliding that half-hard length through the warm, sloppy mixture of his cum and my juices. It feels so strange. So intimate. So completely filthy. Like he's stirring his own load inside me, making sure it stays deep.)"
    x "(My body is still reacting even as my mind starts to slip away. My pussy keeps clenching weakly around him, still trying to milk whatever's left.)"
    x "( I can feel his cum being pushed around inside me with every slow thrust, the warmth spreading even deeper as he lazily fucks his own load into my womb. And all the while, I can feel him shrinking. From that impossibly thick, rock-hard monster that was stretching me to my limit... to something smaller, softer, more manageable. But he still doesn't pull out. He just keeps going, slow and steady, like he wants to stay inside me forever.)"
    x "(My eyes finally close. I can't fight it anymore. The exhaustion, the warmth of his cum inside me, the slow, rhythmic thrusting of his softening cock... it's all too much. I pass out completely, my body going limp in his arms. Everything goes dark.)"
    
    scene black
    with dissolve
    show madd broken at left_small
    x "(I don't know how long I'm out — seconds? Minutes? Hours? Time doesn't exist anymore.)"
    x "(After a while, I feel my head being gently lowered onto a pillow. My body is moved, shifted, arranged. I'm still unconscious, eyes still closed, but I can feel everything happening to me. Then... a few seconds later... an absolute, horrid stench assaults my nose.)"
    x "( It's so thick, so heavy, so overwhelmingly foul that even in my unconscious state, my body reacts. I know exactly what it is. His ass. My brother's sweaty, unwashed asshole. The same one he promised he'd make me clean. The stench is so strong it feels like it's burning my nostrils — thick, cheesy, sour, and completely masculine. It fills my lungs with every shallow breath I take.)"
    x "(I feel the hair first. His thick, sweaty ass hair brushing against my face, tickling my cheeks, my nose, my lips. Then I feel the heat. His bare, hot asshole pressing down directly onto my nose, swallowing the tip of it completely.)"
    x "( The wrinkled, sweaty ring clenches slightly around my nose like it's trying to suck me in. I can feel the warmth of it, the wetness, the filth. And I breathe it in. I can't stop myself. Even unconscious, my body inhales the disgusting stench of my brother's unwashed asshole. It fills my nose, my throat, my lungs. And I still can't move. I can't open my eyes. I can't turn away. I'm completely at his mercy.)"
    x "(But then it goes deeper. His asshole clenches harder, and I feel my nose being sucked further inside — the wrinkled, hot, sweaty ring stretching around the bridge of my nose, swallowing more of it. The heat is insane. It's like sticking my face into a furnace of pure, concentrated body odor. Humid, heavy, and so thick I can almost taste it.)"
    x "( Every breath I take is pulled directly from the source — hot, moist air that has been trapped inside his ass all night, marinating in his sweat and filth. It coats the inside of my nose instantly, thick and slimy, like it's physically painting my nasal passages with his stench.)"
    x "( And the worst part? It feels like it's dripping down the back of my throat, settling on my tongue even though my mouth is closed. The smell is so strong, so concentrated, that just breathing it in makes my tongue feel coated — heavy, sour, and completely overwhelmed by the taste of his unwashed crack. I can feel it on my tongue. I can taste it. And I can't stop breathing it in.)"
    show brother possessive at right_small
    brother_says "Even if you're asleep, Maddie... even if you're completely knocked out... I'm still gonna use your body to clean me. Your tongue might not be awake yet, but your face is. And I'm gonna rub my whole filthy, sweaty ass all over it while you sleep. You're gonna wake up smelling like my crack. Tasting like my sweat. And you'll thank me for it. Sleep well, little sister. "
    x "(Those are the last words I hear before I finally fall completely asleep. His hot, hairy asshole still wrapped around my nose, sucking it deeper with every clench. His thick, sweaty ass hair tickling my face.)"
    x "( The horrid, concentrated stench filling my lungs and coating my tongue with every breath. And somewhere in the deepest, most broken part of my mind, I know... when I wake up, his filth will be all over me. On my face. In my nose. On my lips. And I will have done nothing to stop it.)"
    x "( Because this is what I am now. His personal, unconscious, ass-cleaning sister. And as the darkness takes me completely, I feel him start to slowly grind his sweaty crack across my face, rubbing his filth into my skin like he's marking his property. And I let him. Because I have no choice anymore. Because I belong to him now. Even in my sleep.)"

    scene madd_wake_up_brother_morning_brother_in_bed_maddie_lap_penetration_aftermath
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd traumatized at left_small
    x "(I finally wake up. My eyes feel heavy, my body feels used and sore in ways I've never felt before. The first thing I notice is the warmth still leaking out of me — thick, sticky cum slowly dripping from my pussy onto the sheets. My brother's cum. It's been inside me all night, and it's still coming out. I can feel it sliding down my pussy every time I shift.)"
    x "(But the second thing I notice is the smell. It's everywhere. My nose, my lungs, my hair, my skin — everything reeks of my brother's ass. That thick, cheesy, sour, unwashed stench is still clinging to me. I can taste it on my tongue. I can feel it coating the inside of my nose and throat. No matter how many times I breathe, it's still there. It's like his asshole is still pressed against my face.)"
    x "(I pull the blanket up to my nose and try to smell it, hoping  to smell anything other than his raw ass. But it's useless. The blanket smells like sweat and sex, but the dominant, overwhelming scent is still his ass. My lungs are full of it. My nasal passages are coated with it. It's not just on me — it's inside me. I breathed it in for hours while I was unconscious, and now it's part of me.)"
    x "(I lie there in silence, staring at the ceiling, wondering... how long was my nose actually inside his asshole? How long did he keep my face buried in his crack while I was passed out? An hour? Two hours? even more? I have no idea.)"
    x "( All I know is that the smell is so deep in my system that I can still taste it. Still feel it. And I know that when I see him today, he's going to want more. He's going to want my tongue this time. And I'm going to give it to him. Because this is who I am now. His sister. His toy. His personal ass-cleaning slut. And there's no going back.)"
    x "(Fuck..better not think of that , I dont want to experience that again... I got up from the bed and left the room hoping to avoid any contact with my brother.)"

    # CHARACTER UPDATES: madd_wake_up_brother_morning_escalations_vaginal
    $ character_relations["brother"]["lust"] = 0
    $ character_relations["brother"]["anger"] = 0
    $ character_relations["brother"]["intimacy"] += 10
    $ character_relations["brother"]["kissed"] += 5
    $ character_relations["brother"]["groped_madd"] += 3
    $ character_relations["brother"]["undressed_madd"] += 1
    $ character_relations["brother"]["touched_madd"] += 5
    $ character_relations["brother"]["vaginal_sex"] += 1
    $ character_relations["brother"]["vaginal_creampie"] += 1
    $ character_relations["brother"]["friend"] += 3
    $ madd_willpower = max(0, madd_willpower - 60)
    $ stat_notification = "Brother's dominance has fully claimed Madd"
    $ renpy.pause(2.0)
    $ stat_notification = ""
    call advance_time_and_check(minutes=180) 
    $ journal_event_set_done("Brother", "Wake Up: Full Claim")

    jump home_areas 


