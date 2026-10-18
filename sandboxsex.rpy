###############################################################################
# MODULAR SEX SCENE SYSTEM
# Based on SEX_TRANSITIONS.txt
###############################################################################

###############################################################################
# MAIN SCENE: FORCED IN DAD'S ROOM
###############################################################################

label forced_in_dads_room_on_bed:
    """Entry point for dad forcing Madd to his room"""
    
    # Setup scene
    scene dads_room
    
    # Dad drags Madd upstairs
    "Dad grabs your wrist tightly."
    dad "Come with me. Now."
    
    "He drags you up the stairs to his bedroom."
    "Before you can protest, he throws you onto his bed."
    
    # Start sex transition sequence
    call MADD_THROWN_ON_BED_STG_1
    
    # Continue to other stages...
    call MADD_THROWN_ON_BED_STG_2_UNDRESS
    call MADD_THROWN_ON_BED_STG_3_FINISH
    
    # Optional: Stage 4 - Further Humiliation
    if dad_intimacy > 40:
        call MADD_THROWN_ON_BED_STG_4_HUMILIATION
    
    return


###############################################################################
# STAGE 1: START TRANSITIONS (1-6 actions based on lust)
###############################################################################

label MADD_THROWN_ON_BED_STG_1:
    """Stage 1: START phase - dynamic number of actions based on lust"""
    
    # Determine number of actions based on dad's lust
    python:
        if dad_lust < 20:
            num_start_actions = renpy.random.randint(1, 2)
        elif dad_lust < 40:
            num_start_actions = renpy.random.randint(2, 3)
        elif dad_lust < 60:
            num_start_actions = renpy.random.randint(3, 4)
        elif dad_lust < 80:
            num_start_actions = renpy.random.randint(4, 5)
        else:
            num_start_actions = renpy.random.randint(5, 6)
        
        # Track which actions have been used to avoid repetition
        used_actions = []
        
        # Select appropriate action pool based on intimacy
        if dad_intimacy < 16:
            action_pool = "low_intimacy"
        elif dad_intimacy < 36:
            action_pool = "medium_intimacy"
        elif dad_intimacy < 66:
            action_pool = "high_intimacy"
        else:
            action_pool = "extreme_intimacy"
    
    # Execute the determined number of actions
    python:
        for i in range(num_start_actions):
            # Select random action from appropriate pool
            if action_pool == "low_intimacy":
                action = renpy.random.choice([
                    "touch_shoulder", "brush_hair", "hand_to_waist", 
                    "pull_closer", "touch_back", "hand_to_ass",
                    "touch_thigh", "press_body", "hand_to_breast",
                    "grope_breast", "grind_ass", "hand_between_legs",
                    "rub_pussy_clothes"
                ])
            elif action_pool == "medium_intimacy":
                action = renpy.random.choice([
                    "pull_close", "kiss_lips", "kiss_tongue", "kiss_neck",
                    "lick_jaw", "bite_ear", "bite_lips", "kiss_collarbone", 
                    "hand_under_shirt", "grope_breast_bare", "pinch_nipple", 
                    "hand_to_ass_under", "squeeze_ass", "hand_between_legs", 
                    "rub_pussy_panties", "circle_clit", "grind_pussy", 
                    "hand_in_panties", "touch_bare_pussy", "insert_finger"
                ])
            elif action_pool == "high_intimacy":
                action = renpy.random.choice([
                    "grab", "pull_hair", "hand_throat", 
                    "slap_ass", "tear_clothing", "spread_legs",
                    "insert_fingers", "finger_fuck", "finger_ass", 
                    "force_knees", "lick_armpit", "smell_armpit"
                ])
            else:  # extreme_intimacy
                action = renpy.random.choice([
                    "command_strip", "slap_face", "drag_hair", "force_knees",
                    "spit_face", "choke", "fingers_mouth",
                    "collar", "make_crawl", "verbal_degrade",
                    "record", "make_beg", "make_lick_armpit", "force_smell_armpit"
                ])
            
            # Avoid repeating same action
            if action not in used_actions:
                used_actions.append(action)
                renpy.call("MADD_thrown_On_Bed_Partner_dad_" + action)
    
    return


###############################################################################
# STAGE 1 ACTION LABELS - LOW INTIMACY (0-15)
###############################################################################

label MADD_thrown_On_Bed_Partner_dad_touch_shoulder:
    "Dad's hand lands on your shoulder."
    return

label MADD_thrown_On_Bed_Partner_dad_brush_hair:
    "He brushes your hair behind your ear, his fingers lingering."
    return

label MADD_thrown_On_Bed_Partner_dad_hand_to_waist:
    "His hand slides down to your waist."
    return

label MADD_thrown_On_Bed_Partner_dad_pull_closer:
    "He pulls you closer to him."
    return

label MADD_thrown_On_Bed_Partner_dad_touch_back:
    "His hand moves to your lower back."
    return

label MADD_thrown_On_Bed_Partner_dad_hand_to_ass:
    "His hand slides down to grab your ass."
    return

label MADD_thrown_On_Bed_Partner_dad_touch_thigh:
    "He touches your thigh, his hand warm through the fabric."
    return

label MADD_thrown_On_Bed_Partner_dad_press_body:
    "He presses his body against yours."
    return

label MADD_thrown_On_Bed_Partner_dad_hand_to_breast:
    "His hand moves to your breast, groping it over your clothes."
    return

label MADD_thrown_On_Bed_Partner_dad_grope_breast:
    "He gropes your breast firmly."
    return

label MADD_thrown_On_Bed_Partner_dad_grind_ass:
    "He grinds against your ass, letting you feel his hardness."
    return

label MADD_thrown_On_Bed_Partner_dad_hand_between_legs:
    "His hand moves between your legs."
    return

label MADD_thrown_On_Bed_Partner_dad_rub_pussy_clothes:
    "He rubs your pussy through your clothes."
    return


###############################################################################
# STAGE 1 ACTION LABELS - MEDIUM INTIMACY (16-35)
###############################################################################

label MADD_thrown_On_Bed_Partner_dad_pull_close:
    "Dad pulls you close to him."
    return

label MADD_thrown_On_Bed_Partner_dad_kiss_lips:
    "He kisses you on the lips."
    return

label MADD_thrown_On_Bed_Partner_dad_kiss_tongue:
    "His tongue pushes into your mouth as he kisses you deeply."
    return

label MADD_thrown_On_Bed_Partner_dad_kiss_neck:
    "He kisses along your neck."
    return

label MADD_thrown_On_Bed_Partner_dad_lick_jaw:
    "He licks along your jawline."
    return

label MADD_thrown_On_Bed_Partner_dad_bite_ear:
    "He bites your ear gently."
    return

label MADD_thrown_On_Bed_Partner_dad_bite_lips:
    "He bites your lips during the kiss."
    return

label MADD_thrown_On_Bed_Partner_dad_kiss_collarbone:
    "He kisses down to your collarbone."
    return

label MADD_thrown_On_Bed_Partner_dad_hand_under_shirt:
    "His hand slides under your shirt."
    return

label MADD_thrown_On_Bed_Partner_dad_grope_breast_bare:
    "He gropes your bare breast, skin on skin."
    return

label MADD_thrown_On_Bed_Partner_dad_pinch_nipple:
    "He pinches your nipple."
    return

label MADD_thrown_On_Bed_Partner_dad_hand_to_ass_under:
    "His hand slides under your clothes to grab your ass."
    return

label MADD_thrown_On_Bed_Partner_dad_squeeze_ass:
    "He squeezes your ass roughly."
    return

label MADD_thrown_On_Bed_Partner_dad_rub_pussy_panties:
    "He rubs your pussy through your panties."
    return

label MADD_thrown_On_Bed_Partner_dad_circle_clit:
    "His finger circles your clit through the fabric."
    return

label MADD_thrown_On_Bed_Partner_dad_grind_pussy:
    "He grinds against your pussy."
    return

label MADD_thrown_On_Bed_Partner_dad_hand_in_panties:
    "His hand slides into your panties."
    return

label MADD_thrown_On_Bed_Partner_dad_touch_bare_pussy:
    "He touches your bare pussy."
    return

label MADD_thrown_On_Bed_Partner_dad_insert_finger:
    "He inserts a finger inside you."
    return


###############################################################################
# STAGE 1 ACTION LABELS - HIGH INTIMACY (36-65)
###############################################################################

label MADD_thrown_On_Bed_Partner_dad_grab:
    "Dad grabs you forcefully."
    return

label MADD_thrown_On_Bed_Partner_dad_pull_hair:
    "He pulls your hair."
    return

label MADD_thrown_On_Bed_Partner_dad_hand_throat:
    "His hand wraps around your throat."
    return

label MADD_thrown_On_Bed_Partner_dad_slap_ass:
    "He slaps your ass hard."
    return

label MADD_thrown_On_Bed_Partner_dad_tear_clothing:
    "He tears at your clothing."
    return

label MADD_thrown_On_Bed_Partner_dad_spread_legs:
    "He spreads your legs apart."
    return

label MADD_thrown_On_Bed_Partner_dad_insert_fingers:
    "He inserts multiple fingers inside you."
    return

label MADD_thrown_On_Bed_Partner_dad_finger_fuck:
    "He finger fucks you."
    return

label MADD_thrown_On_Bed_Partner_dad_finger_ass:
    "He fingers your ass."
    return

label MADD_thrown_On_Bed_Partner_dad_force_knees:
    "He forces you to your knees."
    return

label MADD_thrown_On_Bed_Partner_dad_lick_armpit:
    "He lifts your arm and licks your armpit."
    return

label MADD_thrown_On_Bed_Partner_dad_smell_armpit:
    "He presses his face to your armpit and inhales deeply."
    return


###############################################################################
# STAGE 1 ACTION LABELS - EXTREME INTIMACY (66-100+)
###############################################################################

label MADD_thrown_On_Bed_Partner_dad_command_strip:
    dad "Strip. Now."
    return

label MADD_thrown_On_Bed_Partner_dad_slap_face:
    "He slaps your face."
    return

label MADD_thrown_On_Bed_Partner_dad_drag_hair:
    "He drags you by your hair."
    return

label MADD_thrown_On_Bed_Partner_dad_spit_face:
    "He spits on your face."
    return

label MADD_thrown_On_Bed_Partner_dad_choke:
    "He chokes you."
    return

label MADD_thrown_On_Bed_Partner_dad_fingers_mouth:
    "He shoves his fingers in your mouth."
    return

label MADD_thrown_On_Bed_Partner_dad_collar:
    "He puts a collar on you."
    return

label MADD_thrown_On_Bed_Partner_dad_make_crawl:
    dad "Crawl for me."
    return

label MADD_thrown_On_Bed_Partner_dad_verbal_degrade:
    dad "You're such a worthless slut."
    return

label MADD_thrown_On_Bed_Partner_dad_record:
    "He takes out his phone to record."
    return

label MADD_thrown_On_Bed_Partner_dad_make_beg:
    dad "Beg for it."
    return

label MADD_thrown_On_Bed_Partner_dad_make_lick_armpit:
    dad "Lick my armpit."
    "He forces your face into his armpit."
    return

label MADD_thrown_On_Bed_Partner_dad_force_smell_armpit:
    "He grabs your head and presses your face into his armpit."
    dad "Smell it."
    return


###############################################################################
# STAGE 2: UNDRESSING (based on lust level)
###############################################################################

label MADD_THROWN_ON_BED_STG_2_UNDRESS:
    """Stage 2: Undressing phase"""
    
    python:
        if dad_lust < 40:
            undress_type = "top_only"
        elif dad_lust < 66:
            undress_type = "bottom_only"
        else:
            undress_type = "both"
    
    if undress_type == "top_only":
        call MADD_undress_top_dad
    elif undress_type == "bottom_only":
        call MADD_undress_bottom_dad
    else:
        call MADD_undress_both_dad
    
    return


label MADD_undress_top_dad:
    """Remove top only"""
    "Dad pulls your shirt off."
    "He unhooks your bra."
    "Your breasts are now exposed."
    return

label MADD_undress_bottom_dad:
    """Remove bottom only"""
    "Dad pulls your pants down."
    "He slides your panties off."
    "Your pussy and ass are now accessible."
    return

label MADD_undress_both_dad:
    """Remove all clothes"""
    "Dad rips your top off."
    "He tears your bra away."
    "Your pants are yanked down."
    "He pulls your panties off roughly."
    "You're completely naked now."
    return


###############################################################################
# STAGE 3: FINISH (1-2 cumshots based on lust)
###############################################################################

label MADD_THROWN_ON_BED_STG_3_FINISH:
    """Stage 3: Finish phase - cumshot(s)"""
    
    python:
        # Determine number of cumshots based on lust
        if dad_lust < 70:
            num_cumshots = 1
        else:
            num_cumshots = 2
        
        # Determine activity type based on intimacy
        if dad_intimacy < 32:
            activity_type = "handjob"
        elif dad_intimacy < 48:
            activity_type = "blowjob"
        elif dad_intimacy < 66:
            activity_type = "anal"
        else:
            activity_type = "vaginal"
    
    # First cumshot
    if activity_type == "handjob":
        call MADD_finish_handjob_dad
    elif activity_type == "blowjob":
        call MADD_finish_blowjob_dad
    elif activity_type == "anal":
        call MADD_finish_anal_dad
    elif activity_type == "vaginal":
        call MADD_finish_vaginal_dad
    
    # Second cumshot if lust is high enough
    if num_cumshots == 2:
        "Dad isn't done yet..."
        
        # Second round can be same or different activity
        if activity_type == "blowjob":
            call MADD_finish_blowjob_round2_dad
        elif activity_type == "anal":
            call MADD_finish_anal_round2_dad
        elif activity_type == "vaginal":
            call MADD_finish_vaginal_round2_dad
    
    return


###############################################################################
# FINISH LABELS - HANDJOB
###############################################################################

label MADD_finish_handjob_dad:
    """Handjob finish"""
    "Dad makes you stroke his cock."
    "You jerk him faster."
    dad "I'm cumming..."
    
    python:
        cum_location = renpy.random.choice(["stomach", "breasts", "face", "hands"])
    
    if cum_location == "stomach":
        "He cums on your stomach."
    elif cum_location == "breasts":
        "He cums on your breasts."
    elif cum_location == "face":
        "He cums on your face."
    else:
        "He cums on your hands."
    
    return


###############################################################################
# FINISH LABELS - BLOWJOB
###############################################################################

label MADD_finish_blowjob_dad:
    """Blowjob finish - round 1"""
    "Dad pushes his cock into your mouth."
    "You suck him as he fucks your face."
    dad "Take it all..."
    
    python:
        # Determine cum location based on intimacy + lust
        if dad_intimacy < 38:
            cum_location = renpy.random.choice(["facial", "tongue", "lips"])
        else:
            cum_location = renpy.random.choice(["mouth", "swallow", "throat"])
    
    if cum_location == "facial":
        "He pulls out and cums on your face."
    elif cum_location == "tongue":
        "He pulls out and cums on your tongue."
    elif cum_location == "lips":
        "He cums on your lips."
    elif cum_location == "mouth":
        "He cums in your mouth."
        dad "Swallow it."
        "You swallow his cum."
    elif cum_location == "throat":
        "He cums down your throat."
    
    return

label MADD_finish_blowjob_round2_dad:
    """Blowjob finish - round 2"""
    "After a brief recovery, his cock hardens again."
    "He shoves it back in your mouth."
    "You suck him again, more sensitive this time."
    
    "He cums on your face this time, covering it."
    
    return


###############################################################################
# FINISH LABELS - ANAL
###############################################################################

label MADD_finish_anal_dad:
    """Anal finish - round 1"""
    "Dad positions you and pushes into your ass."
    "He fucks your ass hard."
    dad "Such a tight ass..."
    
    python:
        # Determine finish based on intimacy + lust
        if dad_lust < 70:
            anal_finish = renpy.random.choice(["ass_cheeks", "back", "asshole_external"])
        else:
            anal_finish = renpy.random.choice(["anal_creampie", "anal_creampie_drip"])
    
    if anal_finish == "ass_cheeks":
        "He pulls out and cums on your ass cheeks."
    elif anal_finish == "back":
        "He pulls out and cums on your back."
    elif anal_finish == "asshole_external":
        "He pulls out and cums on your asshole."
    elif anal_finish == "anal_creampie":
        "He cums deep in your ass."
    elif anal_finish == "anal_creampie_drip":
        "He cums in your ass and watches it drip out."
    
    return

label MADD_finish_anal_round2_dad:
    """Anal finish - round 2"""
    "Dad's cock is hard again."
    "He pushes back into your ass."
    "This time he's less controlled."
    
    "He cums deep inside your ass again."
    
    return


###############################################################################
# FINISH LABELS - VAGINAL
###############################################################################

label MADD_finish_vaginal_dad:
    """Vaginal finish - round 1"""
    "Dad spreads your legs and pushes into your pussy."
    "He fucks you hard."
    dad "Your pussy feels so good..."
    
    python:
        # Determine finish based on intimacy
        if dad_intimacy < 78:
            vaginal_finish = renpy.random.choice(["stomach", "breasts", "pussy_lips", "thighs"])
        elif dad_intimacy < 83:
            vaginal_finish = renpy.random.choice(["risky", "almost_inside", "accident"])
        else:
            vaginal_finish = renpy.random.choice(["creampie", "breeding", "deep_creampie"])
    
    if vaginal_finish == "stomach":
        "He pulls out and cums on your stomach."
    elif vaginal_finish == "breasts":
        "He pulls out and cums on your breasts."
    elif vaginal_finish == "pussy_lips":
        "He pulls out and cums on your pussy lips."
    elif vaginal_finish == "thighs":
        "He pulls out and cums on your thighs."
    elif vaginal_finish == "risky":
        "He pulls out at the last second, barely in time."
    elif vaginal_finish == "almost_inside":
        "He pulls out but some cum drips inside."
    elif vaginal_finish == "accident":
        dad "Oops... too late."
        "He cums inside you."
    elif vaginal_finish == "creampie":
        "He cums deep inside your pussy."
    elif vaginal_finish == "breeding":
        dad "I'm going to breed you..."
        "He cums as deep as possible inside you."
    elif vaginal_finish == "deep_creampie":
        "He grinds deep and cums inside you."
        "You feel his cum filling you up."
    
    return

label MADD_finish_vaginal_round2_dad:
    """Vaginal finish - round 2"""
    "Dad is hard again almost immediately."
    "He pushes back into your pussy."
    "This time he has less control."
    
    "He doesn't even try to pull out."
    "He cums deep inside you again."
    dad "You're mine..."
    
    return


###############################################################################
# STAGE 4: HUMILIATION (optional post-cum)
###############################################################################

label MADD_THROWN_ON_BED_STG_4_HUMILIATION:
    """Stage 4: Post-cum humiliation (optional)"""
    
    python:
        if dad_intimacy < 41:
            humiliation_level = "light"
        elif dad_intimacy < 71:
            humiliation_level = "moderate"
        else:
            humiliation_level = "extreme"
    
    if humiliation_level == "light":
        call MADD_humiliation_light_dad
    elif humiliation_level == "moderate":
        call MADD_humiliation_moderate_dad
    else:
        call MADD_humiliation_extreme_dad
    
    return


label MADD_humiliation_light_dad:
    """Light humiliation"""
    dad "Look at you, covered in my cum."
    "He takes a picture with his phone."
    dad "Don't clean up yet. I want to see it on you for a while."
    return

label MADD_humiliation_moderate_dad:
    """Moderate humiliation"""
    dad "Rub it into your skin."
    "You reluctantly spread his cum around."
    dad "Good girl. Now clean my cock with your mouth."
    "You suck him clean."
    return

label MADD_humiliation_extreme_dad:
    """Extreme humiliation"""
    dad "You belong to me now."
    "He makes you scoop his cum and eat it."
    dad "Say it. Say you're mine."
    "He records everything."
    return
