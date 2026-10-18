# ============================================
# ROMAN CHARACTER INTERACTIONS
# ============================================

label interact_roman_room:
    """Room interaction with Roman (Room 202)"""
    $ current_location = "roman_room"
    call roman_room_show_menu from _call_roman_room_show_menu
    
    $ game_time.advance_time(minutes=5)
    return



label interact_roman_mess_hall(meal):
    """Mess hall interaction with Roman"""
    if "roman" not in met_characters:
        $ met_characters.append("roman")
        $ character_relations["roman"]["friend"] += 5
        $ current_location = "floor_1"

        show madd boy think at left_small
        with dissolve
        x "(I spot a chubby, intimidating guy sitting alone, his presence dominating the table. He looks at me with a stern, almost dismissive glare.)"
        x "(He does not look friendly, but I know I should introduce myself. He seems important—and dangerous to ignore.)"
        show roman evil smile at right_small
        with dissolve
        roman_says "Well, what do we have here? Another new face. You must be the new resident."
        show madd boy try to dodge at left_small
        with dissolve
        x "Y-yeah, I just moved in. Im [mainname]."
        show roman smirk at right_small
        with dissolve
        roman_says "Im Roman. Room 202. My brother Mayank is the manager here, so that makes me management too. Around here, what I say goes."
        show madd boy nervous at left_small
        with dissolve
        x "Oh, so youre Mayanks brother?"
        show roman stern at right_small
        with dissolve
        roman_says "thats right."
        show madd boy smile at left_small
        with dissolve
        x "Nice to meet you, Roman."
        show roman angry at right_small
        with dissolve
        roman_says "Jesus kid, dont they teach you manners? You call me Sir."
        show madd boy embarassed at left_small
        with dissolve
        x "Y-Yes, Sir."
        show roman lustful looks smirk at right_small
        with dissolve
        roman_says "Good. Now, if you want things to go smoothly, you'll do as youre told. My brother and I run everything here."
        show madd boy blush at left_small
        with dissolve
        x "Ill keep that in mind, Sir."
        show roman evil smile at right_small
        with dissolve
        roman_says "Smart. Now get out of my sight unless you have something useful to say."
        $ character_relations["roman"]["dominance"] += 2
        $ madd_dominance -= 1
        $ game_time.advance_time(minutes=15)
        return

label intercept_roman:
    """Interception scene with Roman - randomly chooses grab type based on relationship stats"""
    # Check if Roman has very high identity and lust (Level 3 - most aggressive)
    if character_relations["roman"]["identity"] > 10 and character_relations["roman"]["lust"] > 20:
        # 80% chance of Level 3, 20% chance of Level 2
        $ rand_chance = renpy.random.randint(1, 100)
        if rand_chance <= 20:
            # Level 2 events (lower tier probability)
            $ grab_type = renpy.random.randint(1, 2)
            if grab_type == 1:
                call intercept_roman_level_2_grab_ass from _call_intercept_roman_level_2_grab_ass
            else:
                call intercept_roman_level_2_grab_waist from _call_intercept_roman_level_2_grab_waist
        else:
            # Highest probability of new aggressive events (Level 3)
            $ grab_type = renpy.random.randint(1, 10)
            if grab_type <= 4:
                call intercept_roman_level_3_spank_ass from _call_intercept_roman_level_3_spank_ass
            elif grab_type <= 8:
                call intercept_roman_level_3_neck_sniff from _call_intercept_roman_level_3_neck_sniff
            elif grab_type == 9:
                call intercept_roman_level_2_grab_ass from _call_intercept_roman_level_2_grab_ass_1
            else:
                call intercept_roman_level_2_grab_waist from _call_intercept_roman_level_2_grab_waist_1
    # Check if Roman has high identity and lust (Level 2)
    elif character_relations["roman"]["identity"] > 5 and character_relations["roman"]["lust"] > 20:
        # 80% chance of Level 2, 20% chance of Level 1
        $ rand_chance = renpy.random.randint(1, 100)
        if rand_chance <= 20:
            # Level 1 events (lower tier probability)
            $ grab_type = renpy.random.randint(1, 3)
            if grab_type == 1:
                call intercept_roman_level_1_grab_wrist from _call_intercept_roman_level_1_grab_wrist
            elif grab_type == 2:
                call intercept_roman_level_1_grab_shoulder from _call_intercept_roman_level_1_grab_shoulder
            else:
                call intercept_roman_level_1_grab_neck from _call_intercept_roman_level_1_grab_neck
        else:
            # Higher probability of grabbing ass/waist (level 2)
            $ grab_type = renpy.random.randint(1, 10)
            if grab_type <= 4:
                call intercept_roman_level_2_grab_ass from _call_intercept_roman_level_2_grab_ass_2
            elif grab_type <= 8:
                call intercept_roman_level_2_grab_waist from _call_intercept_roman_level_2_grab_waist_2
            elif grab_type == 9:
                call intercept_roman_level_1_grab_wrist from _call_intercept_roman_level_1_grab_wrist_1
            else:
                call intercept_roman_level_1_grab_shoulder from _call_intercept_roman_level_1_grab_shoulder_1
    else:
        # Original 3 options with equal probability (Level 1)
        $ grab_type = renpy.random.randint(1, 3)
        if grab_type == 1:
            call intercept_roman_level_1_grab_wrist from _call_intercept_roman_level_1_grab_wrist_2
        elif grab_type == 2:
            call intercept_roman_level_1_grab_shoulder from _call_intercept_roman_level_1_grab_shoulder_2
        else:
            call intercept_roman_level_1_grab_neck from _call_intercept_roman_level_1_grab_neck_1
    
    return

label intercept_roman_level_1_grab_wrist:
    """Interception scene - Roman grabs Madds wrist"""
    scene scene_grabwrist_roman_hallway_level1 with dissolve
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Hey there, [mainname]. youre being too loud. And why are you always rushing around?"
    show madd boy flustered at left_small
    with dissolve
    x "R-Roman! What? I was not being loud, I was just..."
    show madd boy confused at left_small
    with dissolve
    x "(He steps closer, and I feel trapped.)"
    show roman evil smile at right_small
    with dissolve
    roman_says "I told you to call me Sir. Did i not make myself clear?"
    show madd boy uncomfortable at left_small
    with dissolve
    x " (He steps closer, and I feel trapped.)"
    show madd boy flustered at left_small
    with dissolve
    x " I am sorry , Sir. I did not mean to disrespect you."
    show roman evil smile at right_small
    with dissolve
    roman_says "(Perfect. Another chance to correct her. Shes so easy to manipulate with a little authority.)"
    roman_says "do not talk back to me. As the warden here, I decide whats loud and what is not."
    roman_says "(Ill make her understand whos in control here. Starting with something small... something she will not even realize is calculated.)"
    show madd boy confused at left_small
    with dissolve
    x "(Confused? But I did not... I was not even...)"
    
    x "(Before I can finish, he grabs my wrist firmly.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "(Perfect. Her skin is so soft, so responsive. She does not even realize how much power I have over her right now.)"
    show madd boy flustered at left_small
    with dissolve
    roman_says "( This wrist is so small and delicate ) "
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Take it slow. do not rush. You need to learn patience."
    show madd boy flustered at left_small
    with dissolve
    x "(His grip tightens slightly as he pulls me closer.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(Im confused. I was not rushing... was I? His hand is warm, and hes holding me in place.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Understand?"
    roman_says "(Shes genuinely confused. She does not know why I stopped her. She thinks she did something wrong. thats exactly what I want.)"
    show madd boy anxious at left_small
    with dissolve
    x "(He does not let go, just holds my wrist, making his point clear.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says"(I can feel her pulse racing under my fingers. Shes scared and confused. Perfect. thats when shes most malleable.)"
    show madd boy blush at left_small
    with dissolve
    roman_says " ( Such soft skin. I could get used to this. ) "
    roman_says "(Im going to break her gentle nature down piece by piece, and she will not even realize its happening.)"
    $ character_relations["roman"]["identity"] += 1
    $ character_relations["roman"]["lust"] += 5
    show madd boy uncomfortable at left_small
    with dissolve
    x " i-Im sorry, Sir. Ill be more careful."
    show roman smirk at right_small
    with dissolve
    roman_says "Good. Now run along."
    show madd boy confused at left_small
    with dissolve
    x "(He finally releases me, but the confusion lingers. Did I really do something wrong?)"
    
    $ character_relations["roman"]["dominance"] += 1
    $ madd_dominance -= 1
    
    return

label intercept_roman_level_1_grab_shoulder:
    """Interception scene - Roman grabs Madds arm and shoulder"""
    scene scene_grabshoulder_roman_hallway_level1 with dissolve
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Hey there, [mainname]. youre being too loud. And why are you always rushing around?"
    show madd boy flustered at left_small
    with dissolve
    x "R-Roman...Sir! What? I was not being loud, I was just..."
    show madd boy nervous at left_small
    with dissolve
    x "(He steps closer, and I feel trapped.)"
    show roman evil smile at right_small
    with dissolve
    roman_says "do not talk back to me. As the warden here, I decide whats loud and what is not."
    show madd boy confused at left_small
    with dissolve
    x "(Confused? But I did not... I was not even...)"
    show madd boy worried at left_small
    with dissolve
    x "(He suddenly puts his big hand on my right shoulder, gripping it firmly.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Slow down. youre too hasty. The warden has to maintain order."
    show madd boy uncomfortable at left_small
    with dissolve
    x "(He gives a firm squeeze to my shoulder, making me flinch slightly.)"
    show madd boy try to dodge at left_small
    with dissolve
    x "(I try to step back, but his grip is strong. I was not rushing... was I?)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Listen to what I say."
    show madd boy blush at left_small
    with dissolve
    x "(His other hand reaches up and guides my chin to look at him.)"
    show madd boy flustered at left_small
    with dissolve
    x "(My heart is racing, but Im still confused about what I did wrong.)"
    $ character_relations["roman"]["lust"] += 1
    $ character_relations["roman"]["dominance"] += 2
    $ character_relations["roman"]["identity"] += 1
    show madd boy scared at left_small
    with dissolve
    x " i-Im sorry, Sir. Ill be more careful."
    show roman smirk at right_small
    with dissolve
    roman_says "Good. Now run along."
    show madd boy relieved at left_small
    with dissolve
    x "(He finally releases me, but the confusion lingers. Did I really do something wrong?)"
    
    $ character_relations["roman"]["dominance"] += 1
    $ madd_dominance -= 1
    
    return

label intercept_roman_level_1_grab_neck:
    """Interception scene - Roman grabs back of Madds neck"""
    scene scene_grabneck_roman_hallway_level1 with dissolve
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Hey there, [mainname]. youre being too loud. And why are you always rushing around?"
    show madd boy flustered at left_small
    with dissolve
    x "R-Roman! What? I was not being loud, I was just..."
    show madd boy confused at left_small
    with dissolve
    x "(He steps closer, and I feel trapped.)"
    show roman evil smile at right_small
    with dissolve
    roman_says "do not talk back to me. As the warden here, I decide whats loud and what is not."
    show madd boy confused at left_small
    with dissolve
    x "(Confused? But I did not... I was not even...)"
    show madd boy scared at left_small
    with dissolve
    x "(He reaches out and grabs the back of my neck gently but firmly.)"
    show roman evil smile at right_small
    with dissolve
    roman_says "I told you to call me Sir. Did I not make myself clear?"
    show madd boy uncomfortable at left_small
    with dissolve
    x " (He holds me in place with his hand. as his face moves closer to mine.)"
    show roman lustful looks smirk at right_small
    with dissolve
    show madd boy blush at left_small
    with dissolve
    roman_says "( This neck is so slender and delicate ) "
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Stop rushing. Learn to move with purpose, not panic."
    show madd boy scared at left_small
    with dissolve
    x "(His hand keeps me in place, and I can feel his warmth.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(But I was not panicking... I was just walking normally...)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "You need to be more aware of how you carry yourself."
    show madd boy blush at left_small
    with dissolve
    x "(His fingers press gently into the back of my neck, and I feel heat rise to my cheeks.)"
    show madd boy flustered at left_small
    with dissolve
    x "(Is he right? Or is he just... using this as an excuse?)"
    $ character_relations["roman"]["identity"] += 1
    $ character_relations["roman"]["lust"] += 1
    $ character_relations["roman"]["dominance"] += 1
    $ madd_dominance -= 1
    show madd boy scared at left_small
    with dissolve
    x " i-Im sorry, Sir. Ill be more careful."
    show roman smirk at right_small
    with dissolve
    roman_says "Good. Now run along."
    x "(He finally releases me, but the confusion lingers. Did I really do something wrong?)"
    
    $ character_relations["roman"]["dominance"] += 1
    $ madd_dominance -= 1

    
    return

label intercept_roman_level_2_grab_ass:
    """Interception scene - Roman grabs Madds ass (Level 2)"""
    scene  scene_grabass_roman_hallway_level2 with dissolve
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Hey there, [mainname]. youre being too loud. And why are you always rushing around?"
    show madd boy flustered at left_small
    with dissolve
    x "R-Roman! What? I was not being loud, I was just..."
    show madd boy confused at left_small
    with dissolve
    x "(He steps closer, and I feel trapped.)"
    show roman evil smile at right_small
    with dissolve
    roman_says "I told you to call me Sir. Did i not make myself clear?"
    show madd boy uncomfortable at left_small
    with dissolve
    x " (He steps closer, and I feel trapped.)"
    show madd boy flustered at left_small
    with dissolve
    x " I am sorry , Sir. I did not mean to disrespect you."
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "do not talk back to me. As the warden here, I decide whats loud and what is not."
    show madd boy confused at left_small
    with dissolve
    x "(Confused? But I did not... I was not even...)"
    
    x "(Before I can finish, his hand reaches down and grabs my ass firmly.)"
    show roman lustful looks smirk at right_small
    with dissolve
    show madd boy blush at left_small
    with dissolve
    roman_says "( Such a perfect shape... round and firm. ) "
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "You need to watch yourself. The way you move around here catches everyones attention."
    show madd boy embarassed at left_small
    with dissolve
    x "(His hand squeezes my ass, and I feel heat rush to my face.)"
    show madd boy blush at left_small
    with dissolve
    x "(What is he... is he really...?)"
    roman_says "Im being generous by giving you this warning personally."
    x "(His grip lingers, and I cannot move away.)"
    $ character_relations["roman"]["lust"] += 2
    $ character_relations["roman"]["dominance"] += 2
    $ character_relations["roman"]["identity"] += 1
    show madd boy scared at left_small
    with dissolve
    x " i-Im sorry, Sir. Ill be more careful."
    show roman smirk at right_small
    with dissolve
    roman_says "Good. Now run along."
    show madd boy relieved at left_small
    with dissolve
    x "(He starts to release me, but instead of letting go, his hand remains pressed against my ass, beginning to caress it slowly.)"
    show madd boy blush at left_small
    with dissolve
    x "(His palm slides across my cheek in deliberate circles, his fingers tracing the curve with agonizing slowness.)"
    show roman lustful looks smirk at right_small
    with dissolve
    show madd boy scared at left_small
    with dissolve
    x "(I try to move forward, but he keeps his hand firmly in place, continuing his caress.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(This is... this is beyond just a warning now. hes touching me like he owns me.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "(Such perfect skin... so soft and responsive...)"
    show madd boy flustered at left_small
    with dissolve
    x "(His hand gives one final squeeze, his fingers dragging deliberately across my ass as he slowly releases me.)"
    show madd boy blush at left_small
    with dissolve
    x "(Every second feels intentional, like hes memorizing the feel of me in his hand.)"
    show madd boy scared at left_small
    with dissolve
    x "(My face is burning. Did he... did he do that on purpose?)"
    x "(I can still feel his touch like a brand on my skin as I hurry away.)"
    
    $ character_relations["roman"]["dominance"] += 1
    $ madd_dominance -= 1
    
    return

label intercept_roman_level_2_grab_waist:
    """Interception scene - Roman grabs Madds waist (Level 2)"""
    scene  scene_grabwaist_roman_hallway_level2 with dissolve
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Hey there, [mainname]. youre being too loud. And why are you always rushing around?"
    show madd boy flustered at left_small
    with dissolve
    x "R-Roman...Sir! What? I was not being loud, I was just..."
    show madd boy nervous at left_small
    with dissolve
    x "(He steps closer, and I feel trapped.)"
    show roman evil smile at right_small
    with dissolve
    roman_says "do not talk back to me. As the warden here, I decide whats loud and what is not."
    show madd boy confused at left_small
    with dissolve
    x "(Confused? But I did not... I was not even...)"
    show madd boy worried at left_small
    with dissolve
    x "(He suddenly reaches down and puts his hands on my waist, gripping it firmly.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Slow down. youre moving too fast. The way you walk around here is... distracting."
    show madd boy uncomfortable at left_small
    with dissolve
    x "(His hands squeeze my waist, and I suddenly feel very small and fragile.)"
    show madd boy try to dodge at left_small
    with dissolve
    x "(I try to step back, but his grip is strong. I was not rushing... was I?)"
    roman_says "Listen to me carefully."
    x "(His hands pull me slightly closer, and I can feel how much larger and powerful he is. the face that he weighs double of mine is so intimidating)"
    show madd boy blush at left_small
    with dissolve
    x "(My heart is racing. This is so embarrassing... he can feel my curves through his palms. He knows...)"
    $ character_relations["roman"]["lust"] += 2
    $ character_relations["roman"]["dominance"] += 2
    $ character_relations["roman"]["identity"] += 2
    
    show madd boy scared at left_small
    with dissolve
    x " i-Im sorry, Sir. Ill be more careful."
    show roman smirk at right_small
    with dissolve
    roman_says "Good. Now run along."
    show madd boy relieved at left_small
    with dissolve
    x "(He starts to release me, but his hands linger on my waist for just a moment longer.)"
    show madd boy scared at left_small
    with dissolve
    x "(I try to step forward, but I can feel his resistance—he does not want me to go.)"
    show madd boy uncomfortable at left_small
    with dissolve
    x "(His grip tightens as if to prove a point: I belong to him, right here, whenever he wants.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(Finally, he lets me go, but not before his hands slide down to my hips, pressing me closer one last time.)"
    show madd boy blush at left_small
    with dissolve
    x "(The message is clear: this is just the beginning. He has marked me as his.)"
    x "(I walk away on shaky legs, acutely aware of where his hands just were, knowing Ill never forget this moment.)"    
    $ character_relations["roman"]["dominance"] += 1
    $ madd_dominance -= 1
    
    return

label intercept_roman_level_3_spank_ass:
    """Interception scene - Roman spanks Madds ass (Level 3 - Most Aggressive)"""
    scene  scene_spank_roman_hallway_level3 with dissolve
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Stop there ! [mainname]. youre being too loud and too loose."
    roman_says "(Time for phase two. I need to push her further, make her understand that I own her completely.)"
    show madd boy flustered at left_small
    with dissolve
    x "R-Roman! What? I was not being loud!"
    show madd boy confused at left_small
    with dissolve
    x "(He steps closer, and I feel trapped.)"
    show roman evil smile at right_small
    with dissolve
    roman_says " For the 100th time, i told you to call me Sir."
    roman_says "(Shes terrified. Perfect. Fear makes them compliant. This gentle little thing will not resist me.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "do not talk back. You need to learn respect."
    roman_says "(Im going to make her cry out. Im going to hear that sweet voice break.)"
    show madd boy scared at left_small
    with dissolve
    x "(Before I can say anything, his hand comes down hard on my ass with a loud CRACK! ) "
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "(Yes. That perfect sound. Everyone in this hallway will know exactly whats happening. And she'll have no choice but to accept it.)"
    show madd boy blush at left_small
    with dissolve
    x "(The sound echoes in the hallway. It was so loud... so clear...)"
    show madd boy embarassed at left_small
    with dissolve
    x "Ohhh-!!"
    x "(The cry escapes me before I can stop it—high and feminine, betraying exactly what he suspected about me.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "( That sound... that voice. Exactly what I wanted to hear. ) "
    roman_says "(Shes breaking. Soon she will not even try to resist anymore.)"
    show madd boy scared at left_small
    with dissolve
    x "(My ass is throbbing. The sting is intense. Everyone in this hallway heard that sound, heard me...)"
    show madd boy flustered at left_small
    with dissolve
    x "(What just happened...?) "
    $ character_relations["roman"]["lust"] += 3
    $ character_relations["roman"]["dominance"] += 3
    $ character_relations["roman"]["identity"] += 1
    
    show madd boy scared at left_small
    with dissolve
    x " i-Im sorry, Sir..."
    show roman smirk at right_small
    with dissolve
    roman_says "thats better. Remember this feeling. Maybe it'll teach you some manners."
    show madd boy blush at left_small
    with dissolve
    x "(But instead of releasing me, his hand stays firmly planted on my ass.)"
    show roman lustful looks smirk at right_small
    with dissolve
    show madd boy scared at left_small
    with dissolve
    x "(He squeezes it—hard—making me gasp. Then releases slightly. Then squeezes again.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(The intermittent squeezing is almost worse than the spank. its deliberate. Possessive.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "(Such perfect submission... I could do this all day.)"
    show madd boy flustered at left_small
    with dissolve
    x "(Another squeeze. Harder this time. hes testing how much I can take.)"
    show madd boy blush at left_small
    with dissolve
    x "(I try to pull away, but his grip only tightens, holding me in place.)"
    show madd boy scared at left_small
    with dissolve
    x "(Squeeze. Release. Squeeze. its rhythmic now, like hes claiming me with every press of his hand.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(My face is burning. The hallway suddenly feels very small.)"
    show roman lustful looks smirk at right_small
    with dissolve
    x "(Finally, after what feels like an eternity, he slowly releases me. His hand drags deliberately across my ass one last time.)"
    show madd boy relieved at left_small
    with dissolve
    x "(I hurry away, acutely aware of where his hand just was, knowing Ill feel that touch for hours.)"
    show madd boy blush at left_small
    with dissolve 
    x " (What have I gotten myself into...?)"
    x "( This was so humiliating , I hope no one heard that... )"
    $ madd_dominance -= 1
    
    return

label intercept_roman_level_3_neck_sniff:
    """Interception scene - Roman grabs Madd by the neck from behind and sniffs her (Level 3 - Most Aggressive)"""
    scene  scene_sniff_roman_hallway_level3 with dissolve
    show madd boy think at left_small
    with dissolve
    x "(Im walking through the hallway, lost in thought, not paying attention to my surroundings.)"
    x "(Suddenly, strong hands wrap around my neck from behind. I did not see him coming.)"
    show roman lustful looks smirk at right_small
    with dissolve
    show madd boy scared at left_small
    with dissolve
    x "(My heart stops. I freeze.)"
    roman_says "Where are you going in such a hurry?"
    show madd boy flustered at left_small
    with dissolve
    x "R-Roman! You scared me!"
    show madd boy confused at left_small
    with dissolve
    x "(I blurted out his name without thinking. Big mistake.)"
    show roman evil smile at right_small
    with dissolve
    x "(His grip on my neck tightens suddenly, cutting off my words.)"
    show madd boy scared at left_small
    with dissolve
    x "G-gah! R-Roman!"
    roman_says "I thought I told you to call me Sir."
    show madd boy blush at left_small
    with dissolve
    x "I-Im sorry, Sir! I did not mean to!"
    show roman lustful looks smirk at right_small
    with dissolve
    x "(His grip loosens, but he does not release me entirely. His hand remains firm on my neck, a constant reminder of whos in control.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(I can feel him moving closer, his face descending toward my neck and hair.)"
    show madd boy blush at left_small
    with dissolve
    x "(What is he doing...?)"
    x "(His breathing becomes audible against my skin as he slowly moves toward my neck.)"
    show madd boy scared at left_small
    with dissolve
    x "(Hes sniffing me. Deliberately. Slowly.)"
    x "(His nose brushes against my hair, and he inhales deeply.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "You smell different from the others."
    show madd boy blush at left_small
    with dissolve
    x "(His voice is low, almost reverent. His breath is warm against my neck.)"
    roman_says "This whole hostel reeks of sweat. Stale, male sweat. But you..."
    show madd boy scared at left_small
    with dissolve
    x "(He inhales again, deeper this time, his face buried in my hair.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(I can feel every breath, every second his nose lingers in my hair.)"
    show madd boy blush at left_small
    with dissolve
    x "I... I just showered, maybe thats why?"
    show madd boy flustered at left_small
    with dissolve
    x "(My voice comes out small, uncertain. Im trying to explain, but really Im just nervous.)"
    show madd boy scared at left_small
    with dissolve
    x "I-I can feel your breath on my neck... did I do something wrong?"
    show roman lustful looks smirk at right_small
    with dissolve
    show madd boy scared at left_small
    with dissolve
    x "(For a moment, he does not respond. He just continues breathing against my neck, his grip on my throat steady.)"
    $ character_relations["roman"]["lust"] += 3
    $ character_relations["roman"]["dominance"] += 3
    $ character_relations["roman"]["identity"] += 2
    
    show madd boy blush at left_small
    with dissolve
    x "(Then, slowly, he begins to release me. His hands slide down from my neck to my shoulders, lingering just long enough to make his point.)"
    show roman smirk at right_small
    with dissolve
    show madd boy relieved at left_small
    with dissolve
    x "(He finally steps back, and I can breathe again.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(But I can still feel where he was. His warmth. His breath. The imprint of his presence on my skin.)"
    show madd boy scared at left_small
    with dissolve
    x "(I glance back as I walk away, and hes watching me with that intense expression.)"
    
    $ character_relations["roman"]["dominance"] += 1
    $ madd_dominance -= 2
    
    return

label water_bottle_witness_roman:
    """Roman witnesses water bottle cap drop - randomly chooses between scenarios based on relationship stats"""
    # Check if Roman has very high identity and lust (Level 3 - most aggressive)
    if character_relations["roman"]["identity"] > 10 and character_relations["roman"]["lust"] > 20:
        # 80% chance of Level 3, 20% chance of Level 2
        $ rand_chance = renpy.random.randint(1, 100)
        if rand_chance <= 20:
            # Level 2 events
            $ event_type = renpy.random.randint(1, 2)
            if event_type == 1:
                call water_bottle_witness_roman_level2_grabs_ass from _call_water_bottle_witness_roman_level2_grabs_ass
            else:
                call water_bottle_witness_roman_level2_grabs_thighs from _call_water_bottle_witness_roman_level2_grabs_thighs
        else:
            $ event_type = renpy.random.randint(1, 10)
            if event_type <= 5:
                call water_bottle_witness_roman_level3_spank_ass from _call_water_bottle_witness_roman_level3_spank_ass
            else:
                call water_bottle_witness_roman_level3_sniffs_butt from _call_water_bottle_witness_roman_level3_sniffs_butt
    # Check if Roman has high identity and lust (Level 2 - more aggressive)
    elif character_relations["roman"]["identity"] > 5 and character_relations["roman"]["lust"] > 20:
        # 80% chance of Level 2, 20% chance of Level 1
        $ rand_chance = renpy.random.randint(1, 100)
        if rand_chance <= 20:
            # Level 1 events
            $ event_type = renpy.random.randint(1, 2)
            if event_type == 1:
                call water_bottle_witness_roman_level1_sees_butt from _call_water_bottle_witness_roman_level1_sees_butt
            else:
                call water_bottle_witness_roman_level1_jumps_ass from _call_water_bottle_witness_roman_level1_jumps_ass
        else:
            $ event_type = renpy.random.randint(1, 10)
            if event_type <= 5:
                call water_bottle_witness_roman_level2_grabs_ass from _call_water_bottle_witness_roman_level2_grabs_ass_1
            else:
                call water_bottle_witness_roman_level2_grabs_thighs from _call_water_bottle_witness_roman_level2_grabs_thighs_1
    else:
        # Level 1 events
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call water_bottle_witness_roman_level1_sees_butt from _call_water_bottle_witness_roman_level1_sees_butt_1
        else:
            call water_bottle_witness_roman_level1_jumps_ass from _call_water_bottle_witness_roman_level1_jumps_ass_1
    return

label water_bottle_witness_roman_level1_sees_butt:
    """Roman witnesses Madds butt and comments on it - she hears"""
    scene scene_drop_roman_waterbottle_level1 with dissolve
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Oh my... wow. thats some plump butt you have there."
    show madd boy blush at left_small
    with dissolve
    x "(did he just... comment on my butt?)"
    show madd boy embarassed at left_small
    with dissolve
    x "(I feel my face burning. He said that loud enough for me to hear. Did he do that on purpose?)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "( this should be interesting. )"
    show madd boy scared at left_small
    with dissolve
    x "(I can feel his eyes still on me. I quickly pick up my water bottle cap and secure it firmly, pretending I did not hear him.)"
    $ character_relations["roman"]["lust"] += 5
    $ character_relations["roman"]["identity"] += 1
    return

label water_bottle_witness_roman_level1_jumps_ass:
    """Roman witnesses Madds ass jumping as she picks up bottle cap and stands up"""
    scene scene_jumpbutt_roman_waterbottle_level1 with dissolve
    show madd boy think at left_small
    with dissolve
    x "(I drop my water bottle cap. As I bend down to pick it up, I feel someone watching me.)"
    x "(I grab the cap and quickly stand up, my body bouncing slightly as I straighten.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Mmm... now thats quite a view. That ass jumping around like that..."
    show madd boy blush at left_small
    with dissolve
    x "(Oh my god... he was watching the whole time.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(I can feel my cheeks burning. He saw everything—the way my body moved, the way it bounced.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "( Perfect. Just perfect. ) "
    show madd boy scared at left_small
    with dissolve
    x "(I feel my cheeks burning as I carefully pick up my cap and cap the bottle, standing there with nervous energy, not sure what to do next.)"
    $ character_relations["roman"]["lust"] += 5
    $ character_relations["roman"]["identity"] += 1
    return

label water_bottle_witness_roman_level2_grabs_ass:
    """Roman grabs Madds ass while shes bent down or standing after dropping bottle cap"""
    scene scene_grabass_roman_waterbottle_level2 with dissolve
    show madd boy think at left_small
    with dissolve
    x "(I drop my water bottle cap. As I bend down to pick it up, I feel someone watching me.)"
    x "(Im reaching for the cap when suddenly I feel hands on my ass.)"
    show roman lustful looks smirk at right_small
    with dissolve
    show madd boy shocked at left_small
    with dissolve
    x "(My heart jumps!)"
    roman_says "Did you drop something, boy?"
    show madd boy blush at left_small
    with dissolve
    x "(The question hangs in the air as his hands grip my ass firmly.)"
    show madd boy scared at left_small
    with dissolve
    x "(I try to straighten up, but his hands stay exactly where they are, not letting me move.)"
    show roman lustful looks smirk at right_small
    with dissolve
    x "(His fingers knead my ass with deliberate, possessive touches. hes not being subtle about it.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(Oh god... hes... hes touching me. Right here. What if someone sees?)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "( Mmm... so firm. So perfect. ) "
    show madd boy blush at left_small
    with dissolve
    x "(He squeezes harder, almost like hes testing the softness of my skin, his palms grinding against my ass.)"
    show madd boy flustered at left_small
    with dissolve
    x " I-I... yes, Sir... I dropped the cap..."
    show roman lustful looks smirk at right_small
    with dissolve
    x "(Finally, he releases me, but not before giving my ass one final possessive squeeze.)"
    show madd boy scared at left_small
    with dissolve
    show madd boy embarassed at left_small
    with dissolve
    x "(I pick up my cap with shaking hands and carefully seal the bottle, still processing what just occurred.)"
    $ character_relations["roman"]["lust"] += 5
    $ character_relations["roman"]["identity"] += 1
    return

label water_bottle_witness_roman_level2_grabs_thighs:
    """Roman grabs Madds inner thighs from behind"""
    scene  scene_grabthighs_roman_waterbottle_level2 with dissolve
    show madd boy think at left_small
    with dissolve
    x "(I drop my water bottle cap and bend down to pick it up, not noticing Roman approaching.)"
    x "(Suddenly, I feel strong hands grip my inner thighs from behind, sending an electric jolt through my body.)"
    show roman lustful looks smirk at right_small
    with dissolve
    show madd boy shocked at left_small
    with dissolve
    x "(Oh my god!)"
    roman_says "Did you spill water on the floor, boy?"
    show madd boy blush at left_small
    with dissolve
    x "(His hands are squeezing my inner thighs, his fingers pressing into the sensitive skin.)"
    show madd boy scared at left_small
    with dissolve
    x "(Im in such a compromising position—bent over, his hands all over my thighs...)"
    x "No, Roman, I did not spill water... it was just the cap..."
    show madd boy embarassed at left_small
    with dissolve
    x "(My voice comes out shaky and uncertain.)"
    show roman lustful looks smirk at right_small
    with dissolve
    x "(His grip tightens, and he pulls me slightly against him, making his point clear.)"
    roman_says "You need to call me Sir."
    show madd boy blush at left_small
    with dissolve
    x "Y-Yes, Sir! Im sorry, Sir! It was just the cap, Sir!"
    show madd boy flustered at left_small
    with dissolve
    x "(Im stammering, my cheeks burning as his hands continue to hold my thighs.)"
    show roman lustful looks smirk at right_small
    with dissolve
    x "(He gives my inner thighs one more squeeze before finally releasing me, his fingers dragging deliberately across my skin.)"
    show madd boy scared at left_small
    with dissolve
    show madd boy embarassed at left_small
    with dissolve
    show madd boy blush at left_small
    with dissolve
    x "(I grab my cap and stand there holding it, my legs still trembling slightly as I wait to see if anything else happens.)"
    $ character_relations["roman"]["lust"] += 5
    $ character_relations["roman"]["identity"] += 1
    return

label water_bottle_witness_roman_level3_spank_ass:
    """Roman spanks Madds ass while shes picking up the bottle cap (Level 3 - Most Aggressive)"""
    scene scene_spank_roman_waterbottle_level3 with dissolve
    show madd boy think at left_small
    with dissolve
    x "(I drop my water bottle cap and bend down to pick it up.)"
    x "(Im focused on grabbing it, not paying attention to my surroundings.)"
    show roman lustful looks smirk at right_small
    with dissolve
    show madd boy shocked at left_small
    with dissolve
    x "(Without warning, I feel a hard SMACK! across my ass!)"
    x "Oh!!"
    show madd boy blush at left_small
    with dissolve
    x "(I gasp, my face instantly burning red with embarrassment and shock.)"
    x "(That sound... that loud, clear smacking sound...)"
    show madd boy scared at left_small
    with dissolve
    x "(Oh god... I hope no one heard that. Please let me be alone...)"
    show madd boy embarassed at left_small
    with dissolve
    x "(I quickly straighten up, my cheeks on fire, acutely aware that everyone on this floor probably heard that.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "( That perfect response... ) "
    show madd boy blush at left_small
    with dissolve
    x "(I grab my cap with trembling fingers and screw it onto my bottle, my ass still throbbing from the impact, standing frozen in place.)"
    $ character_relations["roman"]["lust"] += 6
    $ character_relations["roman"]["identity"] += 2
    return

label water_bottle_witness_roman_level3_sniffs_butt:
    """Roman sniffs Madds butt while shes picking up the bottle cap (Level 3 - Most Aggressive)"""
    scene scene_sniffbutt_roman_waterbottle_level3 with dissolve
    show madd boy think at left_small
    with dissolve
    x "(I drop my water bottle cap and immediately bend down to pick it up.)"
    x "(Im reaching for it when I hear footsteps approaching from behind.)"
    show madd boy confused at left_small
    with dissolve
    x "(Im still bent over, focused on the cap...)"
    x "(Then I hear it—a distinct sniffing sound. Multiple times.)"
    show madd boy shocked at left_small
    with dissolve
    x "(What... what is that sound?)"
    x "(I glance under my body and see shoes and pants... Romans shoes and pants... very close to me.)"
    show madd boy blush at left_small
    with dissolve
    x "(Oh my god... is he...?)"
    show madd boy embarassed at left_small
    with dissolve
    x "(hes sniffing me. hes literally sniffing my butt right now while Im bent over.)"
    show madd boy scared at left_small
    with dissolve
    x "(I quickly grab the cap and stand up, my face burning red.)"
    show roman smirk at right_small
    with dissolve
    roman_says "Hmm, you do not smell so good from that angle."
    show madd boy flustered at left_small
    with dissolve
    x "I... what? Roman, I do not... thats...!"
    show madd boy embarassed at left_small
    with dissolve
    x "(I called him by his name. I shouldnt have.)"
    show roman evil smile at right_small
    with dissolve
    x "(Suddenly, I feel his strong hand wrap around my neck from behind.)"
    show madd boy scared at left_small
    with dissolve
    x "Ah-!"
    roman_says "Did I not make myself clear? its Sir. Not Roman."
    show madd boy blush at left_small
    with dissolve
    x "(His grip tightens, commanding and firm.)"
    show madd boy flustered at left_small
    with dissolve
    x "I-Im sorry, Sir! Im sorry, Sir!"
    show roman lustful looks smirk at right_small
    with dissolve
    x "(His grip loosens, and he releases me slowly.)"
    roman_says "thats better."
    show madd boy scared at left_small
    with dissolve
    x "(I grab my water bottle cap and quickly tighten it with trembling hands, unsure of what to do next.)"
    $ character_relations["roman"]["lust"] += 6
    $ character_relations["roman"]["identity"] += 2
    return

label water_cooler_intro_roman:
    """First meeting at water cooler"""
    scene scene_intro_roman_watercooler_level1 with dissolve
    show roman smile at right_small
    with dissolve
    show madd boy try to dodge at left_small
    with dissolve
    x "(I see a fat, stern-looking guy by the water cooler. He looks me up and down, not bothering to hide his judgment.)"
    x "Hi! Im Madd, I just moved in upstairs. Room 305."
    roman_says "Roman. Room 202. My brother and I run this place, so you better remember whos in charge."
    show madd boy smile at left_small
    with dissolve
    x "Nice to meet you, Sir."
    show roman smirk at right_small
    with dissolve
    roman_says "Ah, calling me Sir already? Good. You'll fit in just fine here."
    show roman lustful looks smirk at right_small
    with dissolve
    show madd boy uncomfortable at left_small
    with dissolve
    x "( I notice he sizing me up with a lustful look. His eyes linger on my brast long enough to make me uncomfortable.)"
    show madd boy try to dodge at left_small
    with dissolve
    x "uhm ... thanks, Sir."
    $ character_relations["roman"]["lust"] += 2
    $ character_relations["roman"]["identity"] += 1
    $ character_relations["roman"]["dominance"] += 1
    $ madd_dominance -= 1
    return

label water_cooler_talk_roman:
    """Casual conversation with Roman at water cooler (non-first meeting)"""
    # Check if Roman has very high lust and identity (Level 3 - most aggressive)
    if character_relations["roman"]["lust"] > 20 and character_relations["roman"]["identity"] > 10:
        # 80% chance of Level 3, 20% chance of Level 2
        $ rand_chance = renpy.random.randint(1, 100)
        if rand_chance <= 20:
            # Level 2 events
            $ event_type = renpy.random.randint(1, 2)
            if event_type == 1:
                call water_cooler_talk_roman_level2_waist from _call_water_cooler_talk_roman_level2_waist
            else:
                call water_cooler_talk_roman_level2_shoulder_to_neck from _call_water_cooler_talk_roman_level2_shoulder_to_neck
        else:
            $ event_type = renpy.random.randint(1, 2)
            if event_type == 1:
                call water_cooler_talk_roman_level3_spank from _call_water_cooler_talk_roman_level3_spank
            else:
                call water_cooler_talk_roman_level3_waist_to_ass from _call_water_cooler_talk_roman_level3_waist_to_ass
    # Check if Roman has high lust and identity (Level 2)
    elif character_relations["roman"]["lust"] > 20 and character_relations["roman"]["identity"] > 5:
        # 80% chance of Level 2, 20% chance of generic
        $ rand_chance = renpy.random.randint(1, 100)
        if rand_chance <= 20:
            # Generic conversation (no special requirements)
            call water_cooler_talk_roman_generic from _call_water_cooler_talk_roman_generic
        else:
            $ event_type = renpy.random.randint(1, 2)
            if event_type == 1:
                call water_cooler_talk_roman_level2_waist from _call_water_cooler_talk_roman_level2_waist_1
            else:
                call water_cooler_talk_roman_level2_shoulder_to_neck from _call_water_cooler_talk_roman_level2_shoulder_to_neck_1
    else:
        # Generic conversation
        call water_cooler_talk_roman_generic from _call_water_cooler_talk_roman_generic_1
    return

label water_cooler_talk_roman_generic:
    """Generic casual conversation with Roman at water cooler"""
    scene scene_casual_roman_watercooler_level1 with dissolve
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Hey there, [mainname]. Seems like were running into each other a lot. Not that Im complaining."
    show madd boy blush at left_small
    with dissolve
    x "Yeah, I guess we are. You come here a lot too?"
    show roman smile at right_small
    with dissolve
    roman_says "Only when I know certain people might be here. Coincidence, Im sure."
    show madd boy flustered at left_small
    with dissolve
    x "(hes looking at me in that intense way again.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "If you want me to show you around sometime, just say the word. My room is much bigger and better than others here."
    show madd boy blush at left_small
    with dissolve
    x "M-Maybe sometime."
    $ character_relations["roman"]["lust"] += 2
    $ character_relations["roman"]["identity"] += 1
    $ madd_lust += 1
    return

label water_cooler_talk_roman_level2_waist:
    """Roman puts hand on Madds waist and caresses while asking about the place (Level 2)"""
    scene  scene_grabwaist_roman_watercooler_level2 with dissolve
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Hey there, [mainname]. How is this place treating you? Any complaints so far?"
    show madd boy blush at left_small
    with dissolve
    x "its... its fine so far, Sir."
    show roman smile at right_small
    with dissolve
    x "(He reaches over and gently places his hand on my waist.)"
    show madd boy flustered at left_small
    with dissolve
    roman_says "Good. You know, you should visit my room sometime. I could show you how things really work around here."
    show madd boy blush at left_small
    with dissolve
    x "M-Maybe sometime, Sir."
    show roman lustful looks smirk at right_small
    with dissolve
    x "(His hand stays on my waist, and I can feel his intentions. hes not really interested in complaints—hes just using this as an excuse to touch me.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(His palm is warm against my side, and I feel very aware of how close he is.)"
    x "(Romans hand slowly moves lower on my waist, his fingers tracing along my hipbone. As he finally releases me, I cannot help but feel a little breathless)"
    $ character_relations["roman"]["lust"] += 3
    $ character_relations["roman"]["identity"] += 1
    $ madd_dominance -= 1
    return

label water_cooler_talk_roman_level2_shoulder_to_neck:
    """Roman puts hands on Madds shoulder then moves to neck while asking about the place (Level 2)"""
    scene scene_grabshoulderneck_roman_watercooler_level2 with dissolve
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Hey there, [mainname]. How are you liking it here so far?"
    show madd boy blush at left_small
    with dissolve
    x "its... its nice, Sir. Everyone has been welcoming."
    show roman smile at right_small
    with dissolve
    x "(He reaches up and places his hand on my shoulder.)"
    show madd boy flustered at left_small
    with dissolve
    roman_says "thats good to hear. You know, you should really visit my room sometime. I'd love to show you around more... privately."
    show madd boy blush at left_small
    with dissolve
    x "I... maybe..."
    show roman lustful looks smirk at right_small
    with dissolve
    x "(His hand slowly slides from my shoulder toward my neck. His fingers trace along the side of my neck with deliberate slowness.)"
    show madd boy scared at left_small
    with dissolve
    x "(This is... this is clearly not about the place or welcomes. His intentions are written all over his face.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(His hand is warm on my neck, and I feel trapped—not in a painful way, but in a way that makes me very aware of his presence.)"
    x "(I swallow hard, trying to steady my breathing as his fingers lightly trace the curve of my neck.)"
    x "(After what feels like an eternity, he finally withdraws his hand, leaving a tingling sensation where it rested.)"
    $ character_relations["roman"]["lust"] += 3
    $ character_relations["roman"]["identity"] += 1
    $ madd_dominance -= 1
    return

label water_cooler_talk_roman_level3_spank:
    """Roman spanks Madds butt and keeps his hand there while talking (Level 3)"""
    scene scene_spank_roman_watercooler_level3 with dissolve
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Hey there, [mainname]. How is this place treating you?"
    show madd boy blush at left_small
    with dissolve
    x "its been great, Sir. Everyone is very..."
    show madd boy shocked at left_small
    with dissolve
    x "(Before I can finish, I feel a sharp SMACK! across my ass.)"
    x "Oh!"
    show roman smirk at right_small
    with dissolve
    roman_says "You should be more careful standing around here alone. You never know who might want to surprise you."
    show madd boy blush at left_small
    with dissolve
    x "(His hand stays on my ass, squeezing possessively.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(This was not about how the place is treating me. This is exactly what he wanted—an excuse to touch me.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "You should visit my room sometime. I can make sure youre... properly taken care of."
    show madd boy flustered at left_small
    with dissolve
    x "I... Ill think about it, Sir."
    show madd boy blush at left_small
    with dissolve
    x "(His hand continues to knead my ass slowly, deliberately, making his intentions crystal clear.)"
    show madd boy scared at left_small
    with dissolve
    x "(He finally releases me, but not before giving one last possessive squeeze.)"
    $ character_relations["roman"]["lust"] += 4
    $ character_relations["roman"]["identity"] += 2
    $ madd_dominance -= 1
    return

label water_cooler_talk_roman_level3_waist_to_ass:
    """Roman puts hand on Madds waist and caresses toward her ass while talking (Level 3)"""
    scene scene_grabwaistass_roman_watercooler_level3 with dissolve
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Hey there, [mainname]. How are you settling in? Everything comfortable?"
    show madd boy blush at left_small
    with dissolve
    x "Yes, Sir. its been really nice so far."
    show roman smile at right_small
    with dissolve
    x "(He casually places his hand on my waist as if its the most natural thing in the world.)"
    show madd boy flustered at left_small
    with dissolve
    roman_says "You know, my room is much more comfortable than the rest of this place. You should come by sometime."
    show madd boy blush at left_small
    with dissolve
    x "M-Maybe sometime, Sir."
    show roman lustful looks smirk at right_small
    with dissolve
    x "(His hand does not stay at my waist. It slowly moves downward, his palm sliding from my waist toward my hips.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(His fingers are now caressing the curve of my hip, moving lower toward my ass with each passing second.)"
    show madd boy scared at left_small
    with dissolve
    x "(This is not innocent. hes clearly mapping out my body, enjoying the feel of me as he talks.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "( Such soft curves... ) I think you'd really enjoy visiting. its a big room with a TV and a comfortable mattress"
    show madd boy blush at left_small
    with dissolve
    x "(His hand is now blatantly on my ass, squeezing gently as he speaks.)"
    show madd boy flustered at left_small
    with dissolve
    x "(I cannot even formulate a response. All I can focus on is his hand and what hes doing to me.)"
    x " Maybe some other time , Sir."
    show madd boy scared at left_small
    with dissolve
    x "(Finally, he releases me, but his hand lingers for just a moment longer, making sure I know exactly what his intentions are.)"
    $ character_relations["roman"]["lust"] += 4
    $ character_relations["roman"]["identity"] += 2
    $ madd_dominance -= 1
    return

label interact_roman_mess_hall_met(meal):
    """Chat interaction with Roman in mess hall (already met)"""
    scene scene_messhall_breakfast
    with fade
    
    # Check if Roman has very high lust and identity (Level 3 - most aggressive)
    if character_relations["roman"]["lust"] > 20 and character_relations["roman"]["identity"] > 10:
        # 80% chance of Level 3, 20% chance of Level 2
        $ rand_chance = renpy.random.randint(1, 100)
        if rand_chance <= 20:
            # Level 2 events
            $ event_type = renpy.random.randint(1, 2)
            if event_type == 1:
                call interact_roman_mess_hall_level2_table_squeeze from _call_interact_roman_mess_hall_level2_table_squeeze
            else:
                call interact_roman_mess_hall_level2_neck_rest from _call_interact_roman_mess_hall_level2_neck_rest
        else:
            $ event_type = renpy.random.randint(1, 2)
            if event_type == 1:
                call interact_roman_mess_hall_level3_messy_spank from _call_interact_roman_mess_hall_level3_messy_spank
            else:
                call interact_roman_mess_hall_level3_close_sniff from _call_interact_roman_mess_hall_level3_close_sniff
    # Check if Roman has high lust and identity (Level 2)
    elif character_relations["roman"]["lust"] > 20 and character_relations["roman"]["identity"] > 5:
        # 80% chance of Level 2, 20% chance of Level 1
        $ rand_chance = renpy.random.randint(1, 100)
        if rand_chance <= 20:
            # Level 1 events
            $ mistake_chance = renpy.random.randint(1, 2)
            if mistake_chance == 1:
                call interact_roman_mess_hall_level1_name_mistake from _call_interact_roman_mess_hall_level1_name_mistake
            else:
                call interact_roman_mess_hall_level1_generic from _call_interact_roman_mess_hall_level1_generic
        else:
            $ event_type = renpy.random.randint(1, 2)
            if event_type == 1:
                call interact_roman_mess_hall_level2_table_squeeze from _call_interact_roman_mess_hall_level2_table_squeeze_1
            else:
                call interact_roman_mess_hall_level2_neck_rest from _call_interact_roman_mess_hall_level2_neck_rest_1
    else:
        # Check if Madd makes a mistake calling him Roman
        $ mistake_chance = renpy.random.randint(1, 3)
        if mistake_chance == 1:
            call interact_roman_mess_hall_level1_name_mistake from _call_interact_roman_mess_hall_level1_name_mistake_1
        else:
            call interact_roman_mess_hall_level1_generic from _call_interact_roman_mess_hall_level1_generic_1
    return

label interact_roman_mess_hall_level1_generic:
    """Generic chat interaction with Roman in mess hall"""
    scene scene_intro_roman_messhall_level1 with dissolve
    show madd boy blush at left_small
    with dissolve
    x "I approach Roman cautiously."
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "(Perfect. She always comes to me when I want her to. She does not even realize shes being conditioned.)"
    roman_says "Hey there. Come sit with me for a bit."
    show madd boy blush at left_small
    with dissolve
    x "Sure, Sir."
    x "(I sit down across from him.)"
    show roman smirk at right_small
    with dissolve
    roman_says "You know, you should really be more grateful to be around someone like me. My family essentially owns this place."
    roman_says "(Shes starting to understand the hierarchy. Soon she'll do anything I want just to maintain my approval.)"
    show madd boy blush at left_small
    with dissolve
    x "I... I know, Sir."
    show roman lustful looks smirk at right_small
    with dissolve
    x "(He reaches across the table and gently touches my arm.)"
    roman_says "(Shes responding to my touch. See how easy this is? A simple touch and she melts.)"
    show madd boy flustered at left_small
    with dissolve
    x "(His touch makes my skin tingle. He notices my reaction.)"
    show roman evil smile at right_small
    with dissolve
    roman_says "youre very responsive, arent you? I like that about you."
    show madd boy flustered at left_small
    with dissolve
    x "I-Im not sure what you mean..."
    $ character_relations["roman"]["friend"] += 1
    $ character_relations["roman"]["lust"] += 3
    $ character_relations["roman"]["identity"] += 1
    $ character_relations["roman"]["dominance"] += 1
    $ madd_dominance -= 1
    $ madd_secret_identity = max(madd_secret_identity - 2, 0)
    $ game_time.advance_time(minutes=20)
    return

label interact_roman_mess_hall_level1_name_mistake:
    """Madd calls Roman by his name instead of Sir, he gets angry and grabs her wrist"""
    scene scene_namemistake_roman_messhall_level1 with dissolve
    show madd boy blush at left_small
    with dissolve
    x "I approach Roman cautiously."
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Hey there. Come sit with me for a bit."
    show madd boy blush at left_small
    with dissolve
    x "Sure, Roman."
    x "(I sit down across from him.)"
    show madd boy confused at left_small
    with dissolve
    x "(Oh no... I just called him Roman instead of Sir. Mistake.)"
    show roman evil smile at right_small
    with dissolve
    x "(His expression immediately darkens. His hand shoots across the table and grabs my wrist firmly.)"
    show madd boy scared at left_small
    with dissolve
    x "Ah E"
    roman_says "We've been over this. What do you call me?"
    show madd boy blush at left_small
    with dissolve
    x "(His grip tightens on my wrist, not painfully, but commanding. Demanding.)"
    show madd boy flustered at left_small
    with dissolve
    x "I-Im sorry, Sir! I did not mean to"
    show roman smirk at right_small
    with dissolve
    x "(He holds my wrist for a moment longer, making his point clear, then slowly releases me.)"
    show madd boy scared at left_small
    with dissolve
    x "(I can still feel the pressure of his hand on my wrist, the reminder of his control.)"
    $ character_relations["roman"]["friend"] += 1
    $ character_relations["roman"]["lust"] += 3
    $ character_relations["roman"]["identity"] += 1
    $ character_relations["roman"]["dominance"] += 2
    $ madd_dominance -= 2
    $ madd_secret_identity = max(madd_secret_identity - 2, 0)
    $ game_time.advance_time(minutes=20)
    return

label interact_roman_mess_hall_level2_table_squeeze:
    """Roman grabs Madds inner thigh under the table while eating (Level 2)"""
    scene scene_grabthighs_roman_messhall_level2 with dissolve
    show madd boy blush at left_small
    with dissolve
    x "I approach Roman and sit down across from him with my plate of food."
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Hey there. Come eat with me."
    show madd boy blush at left_small
    with dissolve
    x "Sure, Sir."
    x "(I start eating, focused on my food.)"
    show roman smirk at right_small
    with dissolve
    roman_says "You know, its quite hot these days. Summer is here."
    show madd boy flustered at left_small
    with dissolve
    x "Y-Yes, it is pretty warm..."
    show roman lustful looks smirk at right_small
    with dissolve
    x "(Suddenly, I feel a hand on my inner thigh under the table.)"
    show madd boy shocked at left_small
    with dissolve
    x "(His fingers grip my thigh firmly, squeezing hard enough to make me trembling.)"
    show madd boy blush at left_small
    with dissolve
    roman_says "You should dress more freely since its summer. You might get sweaty in those clothes."
    show madd boy embarassed at left_small
    with dissolve
    x "(His hand continues to squeeze my inner thigh, clearly enjoying the feel of my soft skin.)"
    show madd boy flustered at left_small
    with dissolve
    x "(This is not about summer or fashion... this is him taking advantage of being under the table.)"
    show madd boy scared at left_small
    with dissolve
    x "(His grip finally releases, but Im left sitting here, trembling, very aware of what just happened.)"
    $ character_relations["roman"]["friend"] += 1
    $ character_relations["roman"]["lust"] += 4
    $ character_relations["roman"]["identity"] += 1
    $ character_relations["roman"]["dominance"] += 1
    $ madd_dominance -= 1
    $ madd_secret_identity = max(madd_secret_identity - 2, 0)
    $ game_time.advance_time(minutes=20)
    return

label interact_roman_mess_hall_level2_neck_rest:
    """Roman rests his hand on back of Madds neck while eating (Level 2)"""
    scene  scene_grabneck_roman_messhall_level2 with dissolve
    show madd boy blush at left_small
    with dissolve
    x "I approach Roman and sit down across from him with my plate."
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Hey there. Lets eat together."
    show madd boy blush at left_small
    with dissolve
    x "Sure, Sir."
    x "(I start eating, trying to enjoy my food.)"
    show roman smile at right_small
    with dissolve
    x "(I feel his heavy hand land on the back of my neck.)"
    show madd boy flustered at left_small
    with dissolve
    roman_says "So, hows the food? Do you like it?"
    show madd boy blush at left_small
    with dissolve
    x "its... its really good, Sir."
    show roman lustful looks smirk at right_small
    with dissolve
    x "(His hand stays on my neck, and his fingers begin to massage the skin gently but deliberately.)"
    show madd boy embarassed at left_small
    with dissolve
    roman_says "thats good. youre eating well. You need to keep your strength up."
    show madd boy scared at left_small
    with dissolve
    x "(His fingers continue to massage my neck, occasionally pressing into the muscles with surprising tenderness.)"
    show madd boy blush at left_small
    with dissolve
    x "(But I know his real intention. This is not about food or my health. This is about touching me, about asserting his claim over me.)"
    show madd boy flustered at left_small
    with dissolve
    x "(His hand finally releases from my neck, and I feel both relieved and strangely disappointed by its absence.)"
    $ character_relations["roman"]["friend"] += 1
    $ character_relations["roman"]["lust"] += 4
    $ character_relations["roman"]["identity"] += 1
    $ character_relations["roman"]["dominance"] += 1
    $ madd_dominance -= 1
    $ madd_secret_identity = max(madd_secret_identity - 2, 0)
    $ game_time.advance_time(minutes=20)
    return

label interact_roman_mess_hall_level3_messy_spank:
    """Roman spanks Madd for being messy at the table (Level 3)"""
    scene scene_spank_roman_messhall_level3 with dissolve
    show madd boy blush at left_small
    with dissolve
    x "I approach Roman and sit down to eat with him."
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Come, lets eat together."
    show madd boy blush at left_small
    with dissolve
    x "Sure, Sir."
    x "(I start eating, but as I reach for my glass, my hand shakes slightly and a drop of water spills onto the table.)"
    show madd boy scared at left_small
    with dissolve
    x "Oh! Im sorry, Sir! I did not mean to do that!"
    show roman evil smile at right_small
    with dissolve
    roman_says "thats messy. Very messy."
    show madd boy confused at left_small
    with dissolve
    x "(Before I can even process his words, he stands up abruptly.)"
    show madd boy shocked at left_small
    with dissolve
    x "(He pulls me up by my arm firmly, and without hesitation, his hand comes down hard on my ass with a loud SMACK!)"
    roman_says "(Perfect. Everyones looking. Everyone will know shes mine. She'll accept it because Im making it public.)"
    x "Oh E"
    show madd boy blush at left_small
    with dissolve
    x "(The spank echoes through the mess hall. Everyone must have heard that.)"
    show roman smirk at right_small
    with dissolve
    roman_says "You need to be more careful. cannot have you being messy around here."
    roman_says "(And now I get to touch her while everyone watches. Shes too humiliated to resist. This is exactly how to keep her obedient.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(His hand lingers on my ass, squeezing it possessively as if it was just an excuse to touch me.)"
    show madd boy scared at left_small
    with dissolve
    x "(Of course it was an excuse. The table was already dirtier than that tiny drop. This was about asserting his dominance, about touching me in front of everyone.)"
    roman_says "(Shes learning. That tiny drop, that pathetic mistake, its all the excuse I need. And everyone here knows it.)"
    show madd boy blush at left_small
    with dissolve
    x "(His grip finally releases, leaving me standing there, embarrassed and very aware of his touch.)"
    $ character_relations["roman"]["friend"] += 1
    $ character_relations["roman"]["lust"] += 5
    $ character_relations["roman"]["identity"] += 2
    $ character_relations["roman"]["dominance"] += 2
    $ madd_dominance -= 2
    $ madd_secret_identity = max(madd_secret_identity - 2, 0)
    $ game_time.advance_time(minutes=20)
    return

label interact_roman_mess_hall_level3_close_sniff:
    """Roman sniffs Madds face while pretending to smell her food (Level 3)"""
    scene scene_sniff_roman_messhall_level3 with dissolve
    show madd boy blush at left_small
    with dissolve
    x "I approach Roman and sit down with my plate."
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "Come, sit. Lets share a meal."
    show madd boy blush at left_small
    with dissolve
    x "Sure, Sir."
    x "(I start eating, bringing a fork with food to my mouth.)"
    show roman lustful looks smirk at right_small
    with dissolve
    x "(Suddenly, his hand lands on the back of my neck, holding me in place.)"
    show madd boy shocked at left_small
    with dissolve
    x "(What!!)"
    roman_says "What are you eating? Let me see."
    show madd boy flustered at left_small
    with dissolve
    x "I... its just some .."
    show roman smirk at right_small
    with dissolve
    x "(Before I can finish, hes leaning in close to my face, his nose almost touching my food.)"
    show madd boy blush at left_small
    with dissolve
    x "(But as his face comes closer, I realize his real target is not the food.)"
    x "(hes sniffing me—sniffing my face, my skin, while using the fork as a pretext.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(His breath is warm against my cheek as he inhales deeply, clearly savoring my scent.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "( Mmm... much better than the food... ) This food smell nice today. Im sure it has good ingredients."
    show madd boy scared at left_small
    with dissolve
    x "(His hand finally releases from my neck, but the intimacy of what just happened leaves me trembling.)"
    show madd boy blush at left_small
    with dissolve
    x "(He just sniffed me. He literally sniffed my face in the middle of the mess hall under the guise of smelling my food.)"
    $ character_relations["roman"]["friend"] += 1
    $ character_relations["roman"]["lust"] += 5
    $ character_relations["roman"]["identity"] += 2
    $ character_relations["roman"]["dominance"] += 2
    $ madd_dominance -= 2
    $ madd_secret_identity = max(madd_secret_identity - 2, 0)
    $ game_time.advance_time(minutes=20)
    return




# ============================================
# ROMAN ROOM LOCATIONS
# ============================================

label roman_room_show_description:
    scene scene_roman_room_night
    with fade
    x "Im in Romans room (Room 202). It has a commanding, dominant presence about it."
    return

label roman_room_show_menu:
    scene scene_roman_room_night
    with fade
    
    if "roman" not in met_characters:
        call roman_room_show_menu_first_meet from _call_roman_room_show_menu_first_meet
    else:
        call roman_room_show_menu_already_met from _call_roman_room_show_menu_already_met
    
    menu:
        "Leave the room":
            $ current_location = "floor_2"
            $ game_time.advance_time(minutes=1)
    
    return

label roman_room_show_menu_first_meet:
    """First meeting with Roman in his room"""
    scene scene_firstmeet_roman_room_level1 with dissolve
    $ met_characters.append("roman")
    $ character_relations["roman"]["friend"] += 10
    show madd boy think at left_small
    with dissolve
    x "I knock on the door and it swings open. A fat, stern man stands there, looking me up and down with a smirk."
    show roman stern at right_small
    with dissolve
    roman_says "What do you want?"
    show madd boy nervous at left_small
    with dissolve
    x "Hi, I wanted to introduce myself. Im [mainname]."
    show roman evil smile at right_small
    with dissolve
    roman_says "Roman. Room 202. Mayanks my brother, but do not get any ideas—I'm the one you answer to. Around here, you call me Sir."
    show madd boy flustered at left_small
    with dissolve
    x "Yes, Sir."
    show roman smirk at right_small
    with dissolve
    roman_says "Good. Now, unless you have something important to say, do not waste my time."
    roman_says "( Thinking... This one has a good shape...)"
    $ character_relations["roman"]["lust"] += 3
    $ character_relations["roman"]["identity"] += 1
    return

label roman_room_show_menu_already_met:
    """Interaction with Roman in his room (already met)"""
    # Check if Roman has very high lust and identity (Level 3)
    if character_relations["roman"]["lust"] > 20 and character_relations["roman"]["identity"] > 10:
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call roman_room_level3_history_tv from _call_roman_room_level3_history_tv
        else:
            call roman_room_level3_symbiotic_thighs from _call_roman_room_level3_symbiotic_thighs
    # Check if Roman has high lust and identity (Level 2)
    elif character_relations["roman"]["lust"] > 20 and character_relations["roman"]["identity"] > 5:
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call roman_room_level2_trip_grab_ass from _call_roman_room_level2_trip_grab_ass
        else:
            call roman_room_level2_sit_at_feet from _call_roman_room_level2_sit_at_feet
    # Level 1
    else:
        $ event_type = renpy.random.randint(1, 2)
        if event_type == 1:
            call roman_room_level1_gentle_back from _call_roman_room_level1_gentle_back
        else:
            call roman_room_level1_wrist_grab from _call_roman_room_level1_wrist_grab
    return

label roman_room_level1_gentle_back:
    """Roman gently touches Madds back and lets her sit at edge of sofa (Level 1)"""
    scene scene_gentletouch_roman_room_level1 with dissolve
    $ character_relations["roman"]["friend"] += 1
    show madd boy blush at left_small
    with dissolve
    x "I knock on Romans door."
    show roman smirk at right_small
    with dissolve
    roman_says "Come in."
    show madd boy blush at left_small
    with dissolve
    x "(I open the door and step inside.)"
    show roman smile at right_small
    with dissolve
    x "(He gently touches my back, his hand warm against my skin.)"
    show madd boy flustered at left_small
    with dissolve
    roman_says "Sit here with me for a bit."
    show madd boy blush at left_small
    with dissolve
    x "(He gestures to the edge of his sofa.)"
    x "(I sit down carefully at the very edge, not sure if I should fully relax.)"
    show madd boy nervous at left_small
    with dissolve
    x "(He does not offer me much space, leaving me to perch uncomfortably at the edge while he sprawls back.)"
    show roman lustful looks smirk at right_small
    with dissolve
    x "(His touch on my back lingers longer than necessary, and I realize his intention is not as innocent as it seems.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(But why would he do that? hes just being nice... right? I do not understand his real intentions.)"
    $ character_relations["roman"]["lust"] += 2
    $ character_relations["roman"]["identity"] += 1
    $ madd_dominance -= 1
    return

label roman_room_level1_wrist_grab:
    """Roman grabs and holds Madds wrist, then pulls her inside (Level 1)"""
    scene scene_grabwrist_roman_room_level1 with dissolve
    $ character_relations["roman"]["friend"] += 1
    show madd boy blush at left_small
    with dissolve
    x "I knock on Romans door."
    show roman smirk at right_small
    with dissolve
    roman_says "What do you want?"
    show madd boy flustered at left_small
    with dissolve
    x "I... I just wanted to introduce myself. Im [mainname]."
    show roman lustful looks smirk at right_small
    with dissolve
    x "(Before I can finish, he reaches out and grabs my wrist.)"
    show madd boy shocked at left_small
    with dissolve
    x "(His grip is firm but not painful, and he holds it for a long moment, just looking at me.)"
    show madd boy blush at left_small
    with dissolve
    roman_says "Come inside."
    show madd boy scared at left_small
    with dissolve
    x "(He gently pulls me into the room by my wrist, closing the door behind us.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(That grip... he held my wrist for so long. What was that about?)"
    show madd boy confused at left_small
    with dissolve
    x "(hes just... being authoritative, I guess? Showing me whos in control?)"
    show roman lustful looks smirk at right_small
    with dissolve
    x "(But I do not understand that he was just exploring the feel of my wrist, enjoying the softness of my skin.)"
    $ character_relations["roman"]["lust"] += 2
    $ character_relations["roman"]["identity"] += 1
    $ madd_dominance -= 1
    return

label roman_room_level2_trip_grab_ass:
    """Roman makes Madd trip on his shoe and grabs her ass (Level 2)"""
    scene scene_tripgrab_roman_room_level2 with dissolve
    $ character_relations["roman"]["friend"] += 1
    show madd boy blush at left_small
    with dissolve
    x "I knock on Romans door."
    show roman smirk at right_small
    with dissolve
    roman_says "Come in."
    show madd boy blush at left_small
    with dissolve
    x "(I open the door and step inside, but as I walk toward him sitting on the sofa, I catch my foot on something.)"
    show madd boy shocked at left_small
    with dissolve
    x "(its his shoe! I stumble forward, unable to catch my balance.)"
    x "Ah E"
    show madd boy scared at left_small
    with dissolve
    x "(I tumble forward across the sofa cushions, my ass exposed and vulnerable.)"
    show roman lustful looks smirk at right_small
    with dissolve
    x "(Before I can even process what happened, his large hands grab my ass firmly.)"
    show madd boy blush at left_small
    with dissolve
    roman_says "Careful there. You almost fell."
    show madd boy embarassed at left_small
    with dissolve
    x "(But hes not helping me up. His hands stay firmly on my ass as Im draped across the sofa, struggling to regain my balance.)"
    show madd boy scared at left_small
    with dissolve
    x "(Each movement I make to stand up just presses his hands deeper into my skin.)"
    show roman lustful looks smirk at right_small
    with dissolve
    x "(His fingers knead my ass slowly, deliberately, as if hes memorizing the shape and feel of me against the soft sofa cushions.)"
    show madd boy flustered at left_small
    with dissolve
    x "(Finally, I manage to push myself up properly, and his hands reluctantly release me.)"
    show madd boy scared at left_small
    with dissolve
    x "(Did he... did he do that on purpose? Make me trip? its hard to tell, and Im too embarrassed to ask.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(I do not realize that tripping me was exactly what he wanted—an excuse to touch me in that vulnerable position.)"
    $ character_relations["roman"]["lust"] += 3
    $ character_relations["roman"]["identity"] += 1
    $ madd_dominance -= 1
    return

label roman_room_level2_sit_at_feet:
    """Roman humiliates Madd by making her sit at his feet (Level 2)"""
    scene scene_sitfeet_roman_room_level2 with dissolve
    $ character_relations["roman"]["friend"] += 1
    show madd boy blush at left_small
    with dissolve
    x "I knock on Romans door."
    show roman smirk at right_small
    with dissolve
    roman_says "Come inside."
    show madd boy blush at left_small
    with dissolve
    x "(I step inside his room.)"
    show roman evil smile at right_small
    with dissolve
    roman_says "Sit over there by my feet. I need the space here."
    show madd boy confused at left_small
    with dissolve
    x "(He points to a spot on the floor near his feet while he sprawls across the sofa.)"
    show madd boy worried at left_small
    with dissolve
    x "(I sit down awkwardly on the floor while he settles back against the cushions, watching anime on his TV.)"
    show roman lustful looks smirk at right_small
    with dissolve
    x "(As we watch, I feel his foot randomly press against my back.)"
    show madd boy flustered at left_small
    with dissolve
    x "(hes touching me with his foot... just casually, as if its nothing. Sometimes he presses harder, sometimes just a light touch.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(This is humiliating, sitting on the floor while he lounges on the sofa above me, using his feet to touch my back whenever he feels like it.)"
    show roman lustful looks smirk at right_small
    with dissolve
    x "(His foot presses against me again, this time lingering for a moment longer, reminding me of his control.)"
    show madd boy scared at left_small
    with dissolve
    x "(Im confused. Why does he need so much space on the sofa? Why am I sitting with such little space? But I do not dare question him.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(I do not understand that this is intentional humiliation—hes establishing his dominance through this position, making me submissive while he lounges above me.)"
    $ character_relations["roman"]["lust"] += 3
    $ character_relations["roman"]["identity"] += 1
    $ madd_dominance -= 2
    return

label roman_room_level3_history_tv:
    """Roman pulls Madd in and dominates her with leg display on History TV (Level 3)"""
    scene scene_historydomination_roman_room_level3 with dissolve
    $ character_relations["roman"]["friend"] += 1
    show madd boy blush at left_small
    with dissolve
    x "I knock on Romans door."
    show roman smirk at right_small
    with dissolve
    roman_says "Get in here."
    roman_says "(Time to take full control. Shes learned to obey, now Ill teach her the meaning of true submission.)"
    show madd boy shocked at left_small
    with dissolve
    x "(He pulls me inside firmly, like he owns me.)"
    show roman evil smile at right_small
    with dissolve
    roman_says "(Shes mine now. Every inch of her. And shes starting to understand that.)"
    x "(Before I can even say hello, he sits me down next to him on the sofa.)"
    show madd boy flustered at left_small
    with dissolve
    roman_says "Watch this."
    roman_says "(Im going to make her see me as her complete superior. By the end of this evening, she'll be desperate for my approval.)"
    show madd boy blush at left_small
    with dissolve
    x "(The TV is playing a documentary about men fighting each other in ancient times, showing brutal dominance displays.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "See how they establish dominance? The stronger one always puts their weight on top."
    roman_says "(I already know what she'll think. She'll rationalize everything I do. thats what makes this so easy.)"
    show madd boy confused at left_small
    with dissolve
    x "(Before I can respond, he lifts his leg and places it directly on top of mine, his full weight pressing down on my thighs.)"
    show madd boy scared at left_small
    with dissolve
    x "(its a clear display of dominance, just like the TV.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "(Perfect. Shes not resisting. Shes accepting my dominance without question. Shes becoming exactly what I want her to be.)"
    roman_says "This is how men dominate each other. You understand?"
    show madd boy embarassed at left_small
    with dissolve
    x "(But this is not really about the TV or ancient dominance displays.)"
    show madd boy blush at left_small
    with dissolve
    x "(His leg is pressed against mine, heavy and deliberate, and I can feel his thigh muscle against my skin as we sit close together on the sofa.)"
    show madd boy scared at left_small
    with dissolve
    x "(This is about him dominating me, not about replicating TV. This is about control—he wants me to know that he owns this space, owns me.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "(Yes. She understands. By her reaction, shes starting to understand whos really in control.)"
    x "(His leg stays there, a constant reminder of his power over me.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(I do not fully understand his intentions. I think hes just... teaching me about dominance? But it feels so much more personal than that.)"
    $ character_relations["roman"]["lust"] += 4
    $ character_relations["roman"]["identity"] += 2
    $ madd_dominance -= 2
    return

label roman_room_level3_symbiotic_thighs:
    """Roman pulls Madd in and rubs her thighs under guise of comfort (Level 3)"""
    scene scene_grabthighs_roman_room_level3 with dissolve
    $ character_relations["roman"]["friend"] += 1
    show madd boy blush at left_small
    with dissolve
    x "I knock on Romans door."
    show roman smirk at right_small
    with dissolve
    roman_says "Get in here, you."
    roman_says "(Shes perfect. So trusting, so naive. She does not even know what Im really doing to her.)"
    show madd boy shocked at left_small
    with dissolve
    x "(He pulls me inside like Im a toy, his grip on my arm firm.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "(Im going to make her think I need her comfort. Then she'll willingly let me touch her anywhere I want.)"
    x "(He sits me down next to him on the sofa and turns on the TV.)"
    show madd boy flustered at left_small
    with dissolve
    roman_says "Look at this. A documentary about symbiotic relationships."
    roman_says "(Perfect cover. She'll believe anything as long as its on TV. Shes so easy to manipulate.)"
    show madd boy blush at left_small
    with dissolve
    x "(The show talks about how even the strongest creatures need comfort and support from others.)"
    show roman smirk at right_small
    with dissolve
    roman_says "Even the strongest men need some comfort."
    roman_says "(Now watch. She'll let her guard down because she thinks Im vulnerable. thats exactly what I want.)"
    show madd boy confused at left_small
    with dissolve
    x "(Before I can respond, he rests his head on my shoulder as we sit together on the sofa.)"
    show madd boy flustered at left_small
    with dissolve
    x "(His head is warm against me, and I feel oddly protective... until his hand reaches over and starts rubbing my inner thigh.)"
    roman_says "(Now I have her where I want her. Her defenses are down, and Im going to explore every inch of her while she thinks Im the one being comforted.)"
    show madd boy shocked at left_small
    with dissolve
    x "(What E)"
    show roman lustful looks smirk at right_small
    with dissolve
    x "(His fingers slide across the sensitive skin of my inner thigh, squeezing gently, exploring slowly.)"
    roman_says "(Shes not pulling away. Perfect. The gentle ones are always the most responsive once you break through their resistance.)"
    show madd boy blush at left_small
    with dissolve
    x "(This... this is not comfort. This is him exploring me, touching me intimately under the guise of needing comfort.)"
    show madd boy embarassed at left_small
    with dissolve
    x "(His hand continues its journey, fingers tracing the curve of my thigh, learning every detail of my body.)"
    show roman lustful looks smirk at right_small
    with dissolve
    roman_says "(Shes becoming mine completely. Soon she will not even remember what it was like to say no to me.)"
    roman_says "(Such perfect skin... so responsive... shes learning exactly how I like her to be...)"
    x "(His real intention is not comfort—its exploration. He wants to touch me, to know me, to own me.)"
    show madd boy scared at left_small
    with dissolve
    x "(But Im clueless about what hes really doing. I think he just... needs comfort? This is what comfort is supposed to be?)"
    show madd boy embarassed at left_small
    with dissolve
    x "(I do not realize that hes using the TV show as a cover for his exploration, as a pretext to touch me more and more.)"
    $ character_relations["roman"]["lust"] += 4
    $ character_relations["roman"]["identity"] += 2
    $ madd_dominance -= 2
    return
    
    return

label roman_room_bathroom_show_description:
    $ bg_image = get_location_image("room", game_time, character_meal_times)
    scene  bg_image
    with fade
    x "Im in Romans bathroom. its clean and well-maintained."
    return

label roman_room_bathroom_show_menu:
    x "Im in Romans bathroom. What would I like to do?"
    
    menu:
        "Go back to room":
            $ current_location = "roman_room"
    
    return



