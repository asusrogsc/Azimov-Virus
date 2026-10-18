label outside_step_father_room_scene:
    python:
        if game_time.is_morning() or game_time.is_afternoon():
            knock_scene = "scene_madd_knock_home_morning_afternoon"
        elif game_time.is_evening():
            knock_scene = "scene_madd_knock_home_evening"
        else:
            knock_scene = "scene_madd_knock_home_night"
    scene expression knock_scene
    with fade
    show madd think at left_small
    with dissolve
    x "I am outside Step Father's door. Should I knock or go back to the lobby?"
    menu:
        "Knock on the door":
            jump knock_step_father_room
        "Go back to lobby":
            jump home_areas    


label step_parent_room_scene:
    python:
        if game_time.is_morning():
            dad_room_scene = "scene_dad_room_morning"
        elif game_time.is_afternoon():
            dad_room_scene = "scene_dad_room_afternoon"
        elif game_time.is_evening():
            dad_room_scene = "scene_dad_room_evening"
        else:
            dad_room_scene = "scene_dad_room_night"
    scene expression dad_room_scene
    with fade
    
    # Reset daily counter if it's a new day
    if game_time.hour < last_dad_talk_hour and last_dad_talk_hour != -1:
        $ dad_talk_today = False
        $ listen_to_dad_demands_today = False
    
    "You are in Step Father and Mom's Room. You feel uncomfortable being here.He sits on the bed, looking at you."

    menu:
        "Talk to him" if not dad_talk_today:
            if madd_willpower<10:
                show madd distressed at left_small
                x "I'm too exhausted to talk to him right now. I need to rest first."
                call advance_time_and_check(minutes=10) from _call_advance_time_and_check_25
                jump step_parent_room_scene
            $ dad_talk_today = True
            jump talk_to_dad
        
        "Talk to him" if dad_talk_today:
            scene scene_dad_room_dad_sitting_on_bed
            with fade
            show madd stressed at left_small
            x "I dont want to talk to him for the day. Maybe after i've slept "
            call advance_time_and_check(minutes=10) from _call_advance_time_and_check_26
            jump step_parent_room_scene
        
        "Listen to his demands":
            scene scene_dad_room_dad_sitting_on_bed
            with fade
            
            if demands_dad >= 2 and research_cram_schools < 3:
                show madd uncertain at left_small
                x "There is no way I am fulfilling his demands"
                call advance_time_and_check(minutes=10) from _call_advance_time_and_check_27
                jump step_parent_room_scene
            
            if research_cram_schools >= 3 and demands_dad < 2:
                show madd uncertain at left_small
                x "I don't even know his demands. For that I need to talk to him"
                call advance_time_and_check(minutes=10) from _call_advance_time_and_check_28
                jump step_parent_room_scene
            
            if not (research_cram_schools >= 3 and demands_dad >= 2):
                show madd uncertain at left_small
                x "( I need to talk to him first to know his demands )"
                call advance_time_and_check(minutes=10) from _call_advance_time_and_check_29
                jump step_parent_room_scene
            

            
            if listen_to_dad_demands_today:
                show madd stressed at left_small
                x "I dont want to listen to his demands again today. Maybe after i've slept "
                call advance_time_and_check(minutes=10) from _call_advance_time_and_check_30
                jump step_parent_room_scene
            
            if madd_willpower < 20:
                show madd distressed at left_small
                x "I'm too exhausted to listen to his demands right now. I need to rest first."
                call advance_time_and_check(minutes=10) from _call_advance_time_and_check_31
                jump step_parent_room_scene
            
            if angry_dad_sofa_rimming_completed and character_relations["dad"]["lust"] >= 60:
                jump step_dad_rimming_2_aftermath

            $ listen_to_dad_demands_today = True
            jump listen_to_dad_demands
        
        "Clean his room":
            if madd_willpower<20:
                show madd distressed at left_small
                x "I'm too exhausted to clean his room right now. I need to rest first."
                call advance_time_and_check(minutes=10) from _call_advance_time_and_check_32
                jump step_parent_room_scene

            call clean_dad_room from _call_clean_dad_room
            jump home_areas
        
        "Go back to lobby":
            call advance_time_and_check(minutes=5) from _call_advance_time_and_check_33
            jump home_areas



label talk_to_dad:
    scene scene_dad_room_dad_sitting_on_bed
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad at right_small
    with dissolve
    dad_says "What are you doing in here?"
    
    show madd worried at left_small
    x "I... I needed to talk to you about something."
    
    show dad creepy at right_small
    dad_says "Speak up. "
    
    show madd nervous at left_small
    x "I need some money.  For supplies and ... other things."
    
    show dad calculating at right_small
    dad_says "Money, huh? Now, why would you need money for that ? "
    
    show madd uncertain at left_small
    x "( He's staring at me strangely... )"
    
    show dad creepy at right_small
    dad_thinks "(God, she looks so much like her mother. That same face... that same innocence before everything changed. That same vulnerability.)"
    
    show madd confused at left_small
    x "( Why is he looking at me like that? )"
    
    show dad laugh at right_small
    dad_says "Come here. Sit next to me on the bed. We can discuss this."
    
    show madd hesitant at left_small
    x "( My stomach twists at his invitation, but I need that money... )"
    
    show madd stressed at left_small
    x "( I take a few steps toward the bed )"
        
    show madd uncertain at left_small
    x "( I sit down on the edge of the bed, as far from him as I can )"
    
    show dad smirk at right_small
    dad_says "Don't be so nervous Maddie. I'm not going to hurt you. We are just going to have a little chat like normal people."
    
    x "(I nod and i sat close to him)"
    
    $ character_relations["dad"]["lust"]+=10
    $ character_relations["dad"]["intimacy"]+=1
    if renpy.random.random() < 0.5:
        jump talk_to_dad_level_1_event_1
    else:
        jump talk_to_dad_level_1_event_2

label talk_to_dad_level_1_event_1:
    scene scene_dad_talk_event1_madd_and_dad_sitting_on_bed
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad at right_small
    with dissolve
    
    show dad obsessed at right_small
    dad_says "You know, I was thinking... maybe I could help you with that money."
    
    show madd hopeful at left_small
    x "Really? You would?"
    x "(As he said that he moved a little closer to me , his arms come around me and he grabbed me in a hug.)"

    scene scene_dad_talk_event1_madd_and_dad_sitting_on_bed_hand_around_madd
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd uncertain at left_small
    x "( My stomach churns slightly at his hands touching my body )"
    
    show dad calculating at right_small
    dad_says "Of course. But help comes with a price, doesn't it?"
    
    show madd distressed at left_small
    x "What... what do you mean?"
    
    
    show dad lustful at right_small
    dad_says "I mean that you need to do something for me. Something... intimate. Something that shows you really appreciate how much I've done for you."

    show madd horrified at left_small
    x "( No... no, he's not... )"
    
    show madd paralyzed at left_small
    x "I don't understand what you mean..."
    
    dad_says "Don't be stupid. You know exactly what I'm asking. Your mother would have understood immediately."
    
    show madd horrified at left_small
    x "I'm not my mother!"
    
    show dad cruel at right_small
    dad_says "No, you're not. But you could be. And right now, you need me more than I need you."


    scene scene_dad_talk_event1_madd_and_dad_sitting_on_bed_hand_around_madd_hand_running_on_body 
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd paralyzed at left_small
    x "(His hands started running on my arms very near my chest. I was frozen in place, not knowing how to react.)"

    show dad mourning at right_small
    dad_says "I've been so lonely since Emily died"
    show madd disgusted at left_small
    x "(Now his hands were right under my chest , cupping my breasts. He was using my moms death as an excuse to touch me like this. I was so disgusted by him.)"
    show madd horrified at left_small
    x "(I have to stop this now !)"
    show madd distressed at left_small
    x "dad ,I miss her too but.."
    show madd shocked at left_small
    x "(Suddenly he squeezed my breasts making me pause for a moment. I was so shocked by his actions that I couldn't even speak.)"
    show madd horrified at left_small
    x "But i'm not her !"
    show madd violated at left_small
    x "(I stare at his hands on my chest for a moment not able to look him in the eyes as he touched my body)"
    show dad obsessed at right_small
    dad_says "Don't be like that Maddie .You bear a striking resemblance to your mother. I can't help but feel like I'm touching her when I touch you."
    show madd distressed at left_small
    x "I said I'm not her ! How many times do I have to say it ?!"
    show madd shaken at left_small
    x "(Something changed in that moment. He stopped touching me at least for the moment)"

    scene scene_dad_talk_event1_madd_and_dad_sitting_on_bed_hand_around_madd_hand_running_on_body_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    x "(Immediately after the short pause he got super aggressive with his hands. Playing with my breasts and squeezing them hard. )"
    show madd distressed at left_small
    x "(As if he stopped holding back completely. He was clearly showing his true intentions now. )"
    show dad hungry at right_small
    dad_says "You can make me so happy Maddie. "
    show madd trembling at left_small
    x "(He kept rubbing my breasts and squeezing them hard i didnt notice his face was very close to mine. I could feel his breath on my face as he says his next words)"
    show dad coercive at right_small
    dad_says "I can give you whatever you want "
    show madd conflicted at left_small
    x "(Reminding me of my money problem. I knew if i let him do what he wanted i would get money from him. But at what cost ? I was so conflicted in that moment. )"
    show madd horrified at left_small
    x "(No no absolutely not ! I can't let him do this to me. I am not for sale ! )"
    show madd distressed at left_small
    x "I....Not if this is the price !"
    show madd paralyzed at left_small
    x "(He kept manhandling my breasts as I said that. There was no stopping him )"
    show dad dominant at right_small
    dad_says "You think you can just say no to me ? You think you can just refuse me ?"
    show madd horrified at left_small
    x "(There was pure rage in his voice. He was angry that I was resisting him. I bet mom would have just let him do whatever he wanted to her Perhaps thats why she's dead now. )"
    show dad authoritative at right_small
    dad_says "You live under my roof. You eat my food. You wear the clothes i paid for. You owe me Maddie. You owe me for everything I've done for you. "
    show madd self loathing at left_small
    x "(I was just looking down , not able to look him in the eyes)"
    show dad possessive at right_small
    dad_says "I take what i want Maddie. You should have known that by now. "
    show madd shocked at left_small
    x "(Immediately after he said that his hands reached the hem of my shirt and started pulling it up. )"

    scene scene_dad_talk_event1_madd_and_dad_sitting_on_bed_hand_around_madd_hand_running_on_body_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    x "(Instinctively I looked up at him in shock as he pulled my shirt up. I couldn't believe what was happening. )"
    show dad sadistic at right_small
    dad_says "Yeah Look me in the eyes bitch while i take what i want from you !"
    show madd paralyzed at left_small
    x "(His other hand was holding me in place as he pulled my shirt up exposing my stomach slowly lifting it towards my chest. )"
    show madd violated at left_small
    x "(Purposefully he was making it as slow and as humiliating as possible. With every inch of my shirt that he pulled up I felt more and more violated. )"
    show madd trembling at left_small
    x "Please stop Dad... I am sorry for what i said !"
    show madd resigned at left_small
    x "I am grateful for everything you do for me !"
    show dad cruel at right_small
    dad_says "tch.. You should be !"
    show madd disgusted at left_small
    x "(With my shirt raised right under my chest , his hands went under my shirt just to get 1 squeeze of my breasts. Feeling his hot calloused hands on my skin was the most disgusting feeling in the world. )"
    show dad lecherous at right_small
    dad_says "Hmm your skin is so soft Maddie. You are right you are not your mother. You are so much better than her. "
    show madd horrified at left_small
    x "(What the hell is wrong with him ?! )"
    show dad calculating at right_small
    dad_says "So you needed money right ? I will give you money if you sleep next to me and let me touch you like this whenever i want. "


    show madd trembling at left_small
    x "( He's backing me into a corner... and I can't find a way out... )"
    
    show madd self loathing at left_small
    x "I... I can't do that."
    x "(I hurriedly got up, tryign to increase the distance between him and me )"
    
    # SCENE 2: His contempt at her refusal
    scene scene_dad_event1_refusal_contempt
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show dad cruel at right_small
    dad_thinks "(She'll change her mind. They always do. When you're hungry and homeless, morality doesn't matter anymore. She'll come begging within days.)"
    
    show dad mocking at right_small
    dad_says "That's your loss then. Get out. And don't bother asking me for money again. You're worthless to me if you won't even try to be useful."
    
    show madd shocked at left_small
    x "( His rejection cuts like a knife... )"
    
    show madd stressed at left_small
    x "( I feel the weight of his words like a physical blow... )"
    
    show madd helpless at left_small
    x "( I was so close to having what I needed... and he just took it away... )"
    
    # SCENE 3: Her despair in the hallway
    scene scene_dad_event1_rejection_despair
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd depressed at left_small
    x "( I leave his room, feeling more trapped than ever... )"
    
    show madd self loathing at left_small
    x "( And the worst part... is that I'm already thinking about coming back... )"
    
    $ journal_event_set_done("Dad", "Dad Gropes: Shirt Lifted")
    $ journal_event_show("Dad", "Sleep With Dad: Breast Night")
    $ journal_event_show("Dad", "Sleep With Dad: Ass Night")

    $ last_dad_talk_hour = game_time.hour
    $ demands_dad += 1
    $ character_relations["dad"]["intimacy"] += 3
    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_34
    $ madd_willpower=max(0,madd_willpower-10)

    jump home_areas


label talk_to_dad_level_1_event_2:
    scene scene_dad_talk_event1_madd_and_dad_sitting_on_bed
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad at right_small
    with dissolve
    
    show dad obsessed at right_small
    dad_says "You're a smart girl. I'm sure you can figure out what I want."
    
    show madd nervous at left_small
    x "( My heart is pounding... I know what he's implying... )"
    
    show madd worried at left_small
    x "I... I'm not comfortable with this."
    

    scene scene_dad_talk_event2_madd_and_dad_sitting_on_bed_hand_around_madd_hand_running_on_thighs
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd uncertain at left_small
    show dad fixated at right_small
    x "(I was sitting right next to him, I knew he wanted to close the gap between us . It was evident in the way he was looking at me. )"

    show madd paralyzed at left_small
    x "(Suddenly he put his hand on my thigh. I froze. and then he started rubbing it. I was so shocked, I couldn't even move. )"

    show dad mourning at right_small
    dad_says "You know I miss emily, "

    show madd anxious at left_small
    x "(He kept rubbing my thigh and his eyes set on my black shorts. )"

    show dad obsessed at right_small
    dad_says "And you remind me of her so much."

    show madd determined at left_small
    x "(I had to speak up...I had to distract him from his thoughts. )"
    x "But...I'm not her dad. She's gone."

    show madd horrified at left_small
    show dad lecherous at right_small
    x "(He looked up at me for a second then went back to looking at the area between my legs. )"
    x "(It was as if he was trying to see my vagina through the small gap between my shorts and my skin. )"

    show madd distressed at left_small
    x "(Knowing that there was no stopping him , i just got up and said )"
    x "I told you Dad , i am not comfortable with this. Can you just act like a normal dad and stop touching me like that ?"


    
    # SCENE 1: His nostalgic predatory gaze as he compares her to mother
    scene scene_dad_event2_mother_comparison
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show dad dominant at right_small
    dad_says "Comfort? Let me tell you about comfort. You're living in my house, eating my food, using my water. You owe me. You owe me everything."


    show madd distressed at left_small
    x "( He's right... I do owe him... don't I? )"
    
    show madd conflicted at left_small
    x "That's not... I mean, I'm grateful, but"
 
    show dad coercive at right_small
    dad_says "But what? You think you get to live here for free? You think you get to ask me for money without giving anything in return? Without showing your appreciation?"
    
    show madd shocked at left_small
    x "( Is he right? Do I owe him my body for shelter and food? )"
    
    show madd paralyzed at left_small
    x "I... I didn't mean it like that."
     
    show dad lecherous at right_small
    dad_says "Your mother never questioned me like this. She understood her place. She understood that a daughter's duty is to care for her father."
    
    show madd horrified at left_small
    x "( He's comparing me to Mom again... like I should want what she had... )"
    
    show dad hungry at right_small
    dad_says "Think about it. I can give you money. Lots of it. I just need someone to pretend to love me if it comes to that ."
    
    # SCENE 2: The temptation - he offers money and freedom
    scene scene_dad_event2_money_temptation
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd hopeful at left_small
    x "( He's offering me a way out... )"
    
    show madd hesitant at left_small
    x "( But at what cost? )"
    
    show madd distressed at left_small
    x "( What am I willing to do... to escape? )"
    
    show dad sadistic at right_small
    dad_says "Or you can refuse and keep begging me for scraps. Your choice."
    
    show madd horrified at left_small
    x "( The way he says 'your choice'... like I actually have one... )"
    
    show madd distressed at left_small
    x "( This isn't a choice... this is coercion... but what else can I do? )"
    
    # SCENE 3: Her coerced paralysis - the breakdown
    scene scene_dad_event2_coerced_paralysis
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd conflicted at left_small
    x "( Every option is a trap... every path leads to degradation... )"
    
    show madd stressed at left_small
    x "I need to think about this..."
    
    show dad mocking at right_small
    dad_thinks "(She'll be back. They always come back when they're desperate enough. And when she does, I'll finally get to do all the things I've been fantasizing about since the day she moved in.)"
    
    show dad greedy at right_small
    dad_says "Don't think too long. This offer won't last forever. And neither will my patience."
    
    show madd traumatized at left_small
    x "( His words carry a threat... or a promise... I can't tell which... )"
    
    show madd paralyzed at left_small
    x "( I stand up on shaking legs and leave the room )"
    
    show madd depressed at left_small
    x "( I feel more violated without even being touched... )"
    
    show madd self loathing at left_small
    x "( And the worst part... is that I'm already considering saying yes... )"
    
    $ journal_event_set_done("Dad", "Dad Gropes: Thigh Rub")
    $ journal_event_show("Dad", "Sleep With Dad: Breast Night")
    $ journal_event_show("Dad", "Sleep With Dad: Ass Night")
    $ last_dad_talk_hour = game_time.hour
    $ demands_dad += 1
    $ character_relations["dad"]["intimacy"] += 3
    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_35
    $ madd_willpower=max(0,madd_willpower-10)
    jump home_areas



label listen_to_dad_demands:
    scene scene_dad_room_dad_sitting_on_bed
    with fade
    show dad at right_small
    with dissolve
    dad_says "Finally, you came to listen."
    
    show madd stressed at left_small
    x "What do you want?"
    
    show dad creepy at right_small
    dad_says "I've been thinking about you. About how much you remind me of your mother."
    
    show madd horrified at left_small
    x "( Why does he keep comparing me to her? )"
    
    show dad calculating at right_small
    dad_says "Since she passed away, I've been so lonely. So very lonely."
    
    # SCENE 1: His emotional plea - vulnerability as manipulation
    scene scene_dad_event2_coerced_paralysis
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd uncertain at left_small
    x "I'm sorry... but I don't know how I can help with that."
    
    show dad creepy at right_small
    dad_says "There is something. Something simple that would help me immensely."
    
    show madd hesitant at left_small
    x "What... what is it?"
    
    show dad smirk at right_small
    dad_says "Just sleep next to me for one night. That's all. Just lay beside me and let me feel like I'm not alone."
    
    show madd shocked at left_small
    x "( Sleep next to him? That's... that seems wrong, but... )"
    
    show madd conflicted at left_small
    x "( He sounds so sad... so desperate... )"
        
    show madd uncertain at left_small
    x "( But if I do this, I'll have access to the room all night... )"
    
    show madd focused at left_small
    x "( Maybe I could find money hidden somewhere while he sleeps... )"
    
    show madd conflicted at left_small
    x "( Even if he's trying to trick me, at least I'd get something out of it. )"
    
    # SCENE 3: Her resignation - walking toward the bed
    scene scene_dad_demands_resignation
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd depressed at left_small
    x "( I'm becoming someone who weighs the value of their body... when did that happen? )"
    x "(My thoughts get muddled as he roughly pulls me to bed)"
    
    menu:
        "Sleep with him tonight (Breast focus)":              
            jump sleep_with_him_breast
        
        "Sleep with him tonight (Ass focus)":
            jump sleep_with_him_ass
        
        "Refuse and leave":
            show madd stressed at left_small
            x "I... I can't do that."
            
            show dad angry at right_small
            dad_says "Fine. Forget I asked. You're just like everyone else - selfish and cold."
            
            show madd distressed at left_small
            x "( The guilt washes over me... )"

            $ character_relations["dad"]["anger"]=min(character_relations["dad"]["anger"]+20,100)
            
            jump home_areas



label sleep_with_him_breast:
    scene scene_dad_demands_resignation
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad at right_small
    with dissolve
    
    show dad creepy at right_small
    dad_says "Thank you girl. You're a good daughter."
    
    show madd distressed at left_small
    x "( A good daughter? This doesn't feel good... )"
    
    show madd uncertain at left_small
    x "I just... I need you to know I'm doing this because"
    
    show dad creepy at right_small
    dad_says "I know. You're doing it because you care about me. Now, let's get some rest. Get into bed."
    
    show madd hesitant at left_small
    x "( I'm not sure what I'm doing this for anymore... )"
    
    show madd resigned at left_small
    x "( I lie down on the bed, keeping as much distance as I can )"
    
    show madd trembling at left_small
    x "( The bed feels enormous and suffocating at the same time )"
    
    show madd nervous at left_small
    x "( I can feel him watching me... studying me like I'm a piece of meat... )"
    
    scene madd_in_bed_with_dad
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show dad lecherous at right_small
    dad_says "You can move closer. I don't bite."
    
    show madd horrified at left_small
    x "( That's not really reassuring... )"
    
    show madd distressed at left_small
    x "( But I do as he asks, moving slightly closer )"
    
    show madd paralyzed at left_small
    x "( Every muscle in my body is tense... ready to run, but nowhere to go )"
    
    show madd anxious at left_small
    x "( I'm acutely aware of his proximity... his warmth... his intentions... )"
    
    show madd stressed at left_small
    x "( My heart is pounding so loud I'm sure he can hear it )"
    
    show madd paralyzed at left_small
    x "( Minutes pass... or are they hours? Time feels strange... )"
    
    show madd shocked at left_small
    x "( Suddenly, I feel his hand moving .His arm wraps around me from behind )"
    
    
    show madd distressed at left_small
    x "( He's pulling me closer... pressing his body against mine .  I freeze... I can feel his entire body against my back... )"
    
    
    show madd helpless at left_small
    x "( Oh God... I can feel him against me... hard and ready... )"
    
    show dad predatory at right_small
    dad_says "Heavens you're such a good Girl Maddie. You listen obediently to your daddy."
    
    scene scene_dad_breast_darkness_violation
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd paralyzed at left_small
    x "( His hand slowly moves up from my waist )"
    
    show madd distressed at left_small
    x "( I should say something... I should move away... but I'm frozen... )"
    
    show madd shocked at left_small
    x "( His hand continues upward... toward my breast )"
    
    show madd traumatized at left_small
    x "( This is really happening... in the darkness... in this bed... )"
    
    # MENU 1: Before through-clothes groping


    scene scene_dad_demands_breast_grope_through_clothes
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd horrified at left_small
    x "( His palm reaches the soft swell of my breast, still covered by fabric )"

    
    show madd distressed at left_small
    x "( I can feel the shape of his hand imprinted through my shirt...  )"
    x "( I was not wearing any bra and  that made his touch that much closer to my breast .)"
    
    show dad hungry at right_small
    dad_says "Fuck yes... I can feel those fat tits through your shirt, you little whore. So soft and warm for Daddy."

    show madd horrified at left_small
    x "(what the fuck his whole attitude went from pleading to dominant as soon as he got access to my body.)"
    x "(He just called me a whore while groping my tits... I feel disgusting... like a cheap piece of meat.)"
    
    show madd paralyzed at left_small
    x "( He's not pulling my shirt up yet... he's just... feeling... claiming through the layers )"
    
    show madd anxious at left_small
    x "( The pressure is building... my heart is pounding so hard I think it might break through my ribs )"
    
    show madd overwhelmed at left_small
    x "( His fingers flex... squeezing gently... testing the firmness... the texture through the fabric )"
    
    show dad lustful at right_small
    dad_says "I can feel your lungs expanding under my hand. I can feel your heartbeat racing. You're so responsive. I love it."
    
    show madd trembling at left_small
    x "( His other hand joins... both palms now pressing against my breasts from outside my shirt )"
    
    show madd distressed at left_small
    x "( It's so intimate... so invasive... even with the barrier of cloth between his skin and mine )"
    
    show dad desperate at right_small
    dad_says "Both your breasts at the same time...That's perfect. I can feel you so well. I can feel your body responding to me even when you're trying not to. It's like you're already mine."
    
    show madd violated at left_small
    x "( He's massaging me through the fabric... in slow, deliberate circles )"
    
    show madd shocked at left_small
    x "( Each movement sends a jolt through my entire body... unwanted sensations I don't know how to process )"
    
    
    show dad creepy at right_small
    dad_says "God, you really are just like your mother… same weak little moans, same slutty body that gets wet when it's used."
    
    show madd horrified at left_small
    x "( I can't believe he's comparing me to Mom even now... in this moment... while violating me )"

    
    show dad yearning at right_small
    dad_says " I want to feel your surrender Maddie  I want to know exactly when her resistance breaks.)"
    
    show madd paralyzed at left_small
    x "( His hands are kneading now... rhythmic... hypnotic... like he's trying to memorize every curve )"
    
    show madd distressed at left_small
    x "( And I'm trapped here... pinned by the weight of his hands and the weight of my own shame )"
    
    show madd anxious at left_small
    x "( His thumbs find my nipples through the fabric... rubbing... teasing... )"
    
    show madd shocked at left_small
    x "( I feel them harden involuntarily... my body betraying me... my body responding to his touch despite everything my mind is screaming )"
    
    show dad lustful at right_small
    dad_says "Look at that... your slutty little nipples are getting hard for me already. Your body knows who it belongs to, even if you're too stupid to admit it."

    show madd traumatized at left_small
    x "(Fuck... i was hoping he doesn't notice that. My own body is betraying me ....am i really a pathetic slut like he say I am I hate myself right now.)"
    
    show madd horrified at left_small
    x "( No... no, my body is betraying me... I'm not responding to him... I'm not... )"
    
    show madd self loathing at left_small
    x "( But the physical response is undeniable... the hardening... the heat building in my core... )"
    
    show madd distressed at left_small
    x "( And I want to die... I want to disappear into the mattress and never come back )"
    
    show dad dominant at right_small
    dad_says "These fat tits are mine now, Maddie. Every single night I'm going to maul them and suck them raw until you're crying and begging like the cheap whore you are. Got it?"
    
    show madd broken at left_small
    x "(His words are so cruel... but the worst part is I can't even argue back... I just lie here and take it like he expects...)"

    show madd paralyzed at left_small
    x "( He keeps massaging... keeps teasing... my breasts aching under his touch )"
    
    show madd trembling at left_small
    x "( Every nerve in my body is on fire... and I can't tell if it's from pleasure or revulsion or both )"
    
    show madd overwhelmed at left_small
    x "( The darkness makes it worse... I can't see his face... can't see his expression... I can only feel his hands and hear his breathing )"
    
    show madd horrified at left_small
    x "( His breathing is getting heavier... more labored... and I realize he's becoming more aroused from this )"
    
    show dad obsessed at right_small
    dad_says "Heh , I can hear the slight whimper in your breathing. You can try to stay silent... trying not to give me the satisfaction of knowing that you're affected by my touch... but I can hear it.)"
    
    show dad possessive at right_small
    dad_says "Fret not ,Soon you'll be making noise on her own. "
    
    show madd violated at left_small
    x "( Minutes pass like hours... or maybe just seconds... time has stopped meaning anything )"
    
    show madd distressed at left_small
    x "( He continues massaging through the fabric... and I can feel the wetness building between my legs... shameful... undeniable )"
    
    show madd self loathing at left_small
    x "( My body is preparing for something I don't want... and there's nothing I can do to stop it )"
    
    show dad hungry at right_small
    dad_says "You're beautiful. Your mother would have loved to see you like this."
    
    show madd horrified at left_small
    x "( His words hit like a physical blow... bringing me back to the reality of what's happening )"
    
    show madd distressed at left_small
    x "( He's still using my dead mother as a reference... still comparing our bodies... still lost in his delusion )"
    
    show madd traumatized at left_small
    x "( And I realize with horrifying clarity that this is only the beginning... )"
    
    show madd horrified at left_small
    x "( His fingers find the edge of my Tshirt... and I realize I can't breathe )"
    
    # MENU 2: Right when he starts lifting her shirt
    show madd shocked at left_small
    x "( He's going to expose me... he's going to pull my shirt off... )"
    
    show madd horrified at left_small
    x "( This is crossing a line... I am not wearing a bra, once my skin is bare... there's no going back... )"
    
    scene scene_dad_breast_darkness_violation
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    x "( His hands grip the hem of my shirt... pulling it upward... )"
    
    show madd horrified at left_small
    x "( I want to stop him... to pull it back down... but I'm completely paralyzed )"
    
    show dad desperate at right_small
    dad_says "Lift your arms, bitch. I want these worthless tits bare right now. No more hiding them from Daddy."

    show madd shocked at left_small
    x "(He called me a bitch... and I'm actually raising my arms... I'm letting him strip me... what the hell is wrong with me...)"
    
    show madd shocked at left_small
    x "( The fabric slides up over my ribs... my torso exposed to the darkness and to him )"
    
    show madd violated at left_small
    x "( My shirt is now above my chest , i was practically top naked )"
    
    scene scene_dad_breast_bare_grope
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show dad obsessed at right_small
    dad_says "The softness of your exposed skin. The warmth. Oh God, you're so beautiful. Even more beautiful than I imagined."
    
    show madd anxious at left_small
    x "( I can feel the cool air of the room against my bare skin... and the heat of his breath getting closer )"
        
    show madd distressed at left_small
    x "( His hands move across my bare skin for the first time... tracing lines down my sides )"
    
    show dad yearning at right_small
    dad_says "You feel so much like her... so soft... so perfect..."
    
    show madd distressed at left_small
    x "( His voice is filled with longing and lust... I can't tell where one ends and the other begins )"
    
    show madd violated at left_small
    x "( He thinks I'm her... my dead mother... and he's using me as a replacement for his dead wife )"
    
    show madd self loathing at left_small
    x "( I'm just a vessel for his fantasy... just a body to use... )"
    
    show dad greedy at right_small
    dad_says "Your breasts... God, they remind me so much of her . That same softness. That same perfect shape. I've been waiting for this for so long. "
    dad_says "Just so you know Maddie , even when your mother was alive I have wanted to do this to you."    

    show madd self loathing at left_small
    x "(He just admitted he wanted to molest me even while Mom was alive... I feel sick... but his hands won't stop squeezing...)"
    # MENU 3: Right after he gropes her bare breast
    show madd horrified at left_small
    x "( His hand cups my breast... squeezes... and I want to scream but my voice is trapped )"
    
    show madd shocked at left_small
    x "( Oh God... this is really happening... bare skin... direct contact... )"
    
    show madd horrified at left_small
    x "( There's no turning back from this... once he touches me like this... I'm his... )"
    
    show madd paralyzed at left_small
    x "( I'm completely trapped... under him... his weight pressing down... trapped by my own silence )"
    
    show madd self loathing at left_small
    x "( Why can't I say no? Why am I just lying here? Why am I allowing this? )"
    
    show madd distressed at left_small
    x "( Because saying no would mean admitting this is happening... and I can't face that )"
    
    show madd helpless at left_small
    x "( So I just lay here... frozen... accepting... becoming less human with each passing second... )"
    
    show dad debased at right_small
    dad_says "You've finally come to accept it havent you Maddie ? You know you belong to me now. You know this is what you deserve. You know that your body exists for my pleasure and nothing else."
    
    show dad lustful at right_small
    dad_says "(I'm going to own every inch of your body. I'm going to make you understand that you exists for my pleasure.)"
    
    show madd distressed at left_small
    x "(I cant reply to his words... I can't even think of a response... I'm just lying here... )"
    x "( The night stretches on... hour after hour )"
    
    show madd traumatized at left_small
    x "( His hands never stop moving... exploring... claiming... )"
    
    show madd violated at left_small
    x "( Sometimes he moans about how much I remind him of her... how he's missed this... how he's missed her... )"
    
    show madd self loathing at left_small
    x "( But I'm not her... and he doesn't love me... he's using me to pretend I'm a ghost... )"
    
    show dad possessive at right_small
    dad_thinks "(She's fucking mine. Every inch of this body exists for my desire and nothing else now.)"
    
    show madd distressed at left_small
    x "( His fingers pinch my nipples... twist... make me gasp despite myself )"
    
    show madd horrified at left_small
    x "( The pain mixes with something I don't want to feel... something sick in my stomach )"
    
    scene scene_dad_breast_bare_grope_neck_bite
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd paralyzed at left_small
    x "( His mouth finds my neck... he takes a bite of my neck then starts licking it)"
    
    show madd violated at left_small
    x "( He's marking me like I'm his property... and I'm letting him... The stench of his saliva assualting my nose and the feeling of his tongue on my skin is making me want to vomit... )"
    
    show dad horny at right_small
    dad_says "It's okay Maddie if you want to start slow. Slowly we will do much more vulgar things."
    
    show madd distressed at left_small
    x "( The night stretches on... hour after hour )"
    
    show madd traumatized at left_small
    x "( His hands never stop moving... exploring... claiming )"
    
    show madd violated at left_small
    x "( Sometimes he moans about how much I remind him of her... how much he loves me )"
    
    show madd self loathing at left_small
    x "( But I'm not her... and he doesn't love me... he's using me to pretend )"
    
    show dad creepy at right_small
    dad_thinks "(She's mine now. Every touch, every moment, she belongs to me. She has nowhere else to go. No one else to turn to.)"
    
    show madd distressed at left_small
    x "( Hours pass... or maybe minutes... time feels meaningless... )"
    
    show madd depressed at left_small
    x "( His hands finally slow down... his breathing becomes heavy... he's falling asleep )"
    
    show madd paralyzed at left_small
    x "( I lie completely still... waiting to make sure he's fully asleep )"
    
    show madd stressed at left_small
    x "( Minutes pass... I can hear his snores... )"
    
    show madd flustered at left_small
    x "( I carefully slip out from under his arm, my skin crawling with shame and violation )"
    
    show madd violated at left_small
    x "( I can still feel his hands on me... his mouth on my neck... )"
    
    show madd distressed at left_small
    x "( I move to the mirror and see the marks... the purple bruises he left... the claim he marked on my body... )"
    
    # SCENE 3: After violation - marks and shame in the mirror
    scene scene_dad_breast_aftermath_marks
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd self loathing at left_small
    x "( I feel so ashamed... so violated... but I need to search... while he's still asleep... )"
    
    show madd self loathing at left_small
    x "( I move quietly around the room, my skin still burning from his touch )"
    
    show madd conflicted at left_small
    x "( I search through drawers, careful not to make noise )"
    
    show madd distressed at left_small
    x "( Every movement feels like a betrayal... like I'm doing something wrong... )"
    
    show madd uncertain at left_small
    x "( But what was last night if not wrong? )"
    
    show madd focused at left_small
    x "( I check under the bed... behind the dresser... )"
    
    show madd stressed at left_small
    x "( My heart is pounding... I can feel his eyes on me even though he's sleeping )"
    
    show madd paralyzed at left_small
    x "( Minutes pass... 10... 15... 20... )"
    
    show madd distressed at left_small
    x "( I'm becoming exhausted... emotionally drained from the night... )"
    
    show madd distressed at left_small
    x "( There's nothing... no money... nothing of value... )"
    
    show madd depressed at left_small
    x "( I gave myself to him for nothing... )"
    
    show madd depressed at left_small
    x "( After about 30-40 minutes of searching, my body is giving out )"
    
    show madd depressed at left_small
    x "( I can barely stand anymore... the shame and exhaustion are too much )"
    
    scene madd_in_bed_with_dad
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd resigned at left_small
    x "( I carefully crawl back into bed, sliding under his arm )"
    
    show madd horrified at left_small
    x "( I'm terrified he'll wake up and know what I was doing )"
    
    show madd paralyzed at left_small
    x "( But he just pulls me closer in his sleep, his hand finding my breast again )"
    
    show madd violated at left_small
    x "( Even in sleep, he claims me... )"
    
    show madd depressed at left_small
    x "( I lie there, feeling the weight of his arm, the weight of my failure )"
    
    show madd depressed at left_small
    x "( By morning, I feel hollow... empty... completely drained of everything that made me human )"
    
    show madd distressed at left_small
    x "( When he finally stirs and wakes, I feel him releasing me )"
    
    show dad smirk at right_small
    dad_says "That was wonderful. You're a natural at this. Your mother would be so proud."
    
    show madd horrified at left_small
    x "( Proud? He thinks Mom would be proud that he violated her daughter? )"
    
    show madd shocked at left_small
    x "( Does he think this is normal? Does he think this is love? )"
    
    show dad possessive at right_small
    dad_says "We're doing this again tonight, and every fucking night after. I'm nowhere near done breaking that cunt of yours."
    dad_says "We will be done when i put a baby in your belly..."
    
    show madd traumatized at left_small
    x "( Not done with me...I knew his words werent idle threat , I knew he meant every word of it . Especially the part where he said he wanted to put a baby in me. )"
    
    show madd violated at left_small
    x "( I quickly get out of the bed, ashamed and violated beyond measure )"
    
    show madd self loathing at left_small
    x "( I got nothing out of this except... this... degradation... )"
    
    show madd distressed at left_small
    x "( I leave the room, feeling like the dirtiest, most worthless person in the world )"
    
    show madd traumatized at left_small
    x "( And the worst part... is that I know I'll come back... )"

    $ character_relations["dad"]["intimacy"]+=5
    $ character_relations["dad"]["lust"]=max(character_relations["dad"]["lust"]-50,0)
    $ character_relations["dad"]["anger"]=max(0,character_relations["dad"]["anger"]-20)
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["kissed"] += 1
    $ madd_willpower=max(0,madd_willpower-20)
    $ journal_event_set_done("Dad", "Sleep With Dad: Breast Night")

    call sleep_on_bed_dad_room from _call_sleep_on_bed_dad_room



label sleep_with_him_ass:
    scene scene_dad_demands_resignation
    with fade
    show dad at right_small
    with dissolve
        
    show dad predatory at right_small
    dad_says "Good little whore. Get in the fucking bed. Daddy's finally getting what he wants tonight."
    
    show madd hesitant at left_small
    x "( My legs feel like lead. Every step closer makes me want to vomit. )"
    
    show madd stressed at left_small
    x "( I force myself to lie down next to this disgusting pig… I hate myself so much right now. )"
    
    show madd resigned at left_small
    x "( I've made my choice... for better or worse... )"
    
    show madd conflicted at left_small
    x "( And I know exactly what it means... )"
    
    show dad possessive at right_small
    dad_says "That's it, you stupid bitch. Lie down like the obedient bitch you are. I don't hurt my property — I use it."
    
    show madd anxious at left_small
    x "( I try to keep distance between us, but the bed is narrow )"
    
    show madd nervous at left_small
    x "( I can feel the heat from his body... the weight of his presence... the intensity of his hunger )"
    
    show madd distressed at left_small
    x "( This whole situation feels unreal... like I'm watching it happen to someone else )"
    
    show madd paralyzed at left_small
    x "( But I know I'm very much here... very much his... )"
    
    show dad dominant at right_small
    dad_says "Now let's turn off the light and get some sleep."
    
    scene madd_in_bed_with_dad
    with fade
    $ renpy.call_in_new_context("_hide_windows")
    x "( The darkness falls... and with it, I feel my last bit of control slipping away )"
    
    show madd paralyzed at left_small
    x "( I lie perfectly still... trying to take up as little space as possible )"
    
    show madd horrified at left_small
    x "( But then I feel him move... turning toward me )"
    
    show madd horrified at left_small
    x "( In the darkness, I'm completely vulnerable... )"
    
    show madd shocked at left_small
    x "( His hand finds my hip... pulling me toward him )"
    
    show madd distressed at left_small
    x "( I'm drawn against his chest... his body enveloping mine )"
    
    show madd trembling at left_small
    x "( I can feel him... all of him... pressed against my back )"
    
    show madd horrified at left_small
    x "( Oh god... oh god... this is happening )"
    
    show dad creepy at right_small
    dad_thinks "(She's trembling. That arousal... that fear... it's intoxicating. She belongs to me now.)"
    
    # MENU 1: Before he gropes her ass through clothes
    show madd shocked at left_small
    x "( My stomach churns as his hand drifts lower... this is really happening. )"
    
    show madd horrified at left_small
    x "( He's going to touch me there... I can feel it coming... )"
    
    
    # SCENE 1: Groping her ass through clothes - violation begins
    scene scene_dad_demands_ass_grope_through_clothes
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd paralyzed at left_small
    x "( His hand slowly moves down from my hip... toward my ass )"
    
    show madd shocked at left_small
    x "( I can already feel where this is going... my skin crawls in dread. )"
    
    show madd horrified at left_small
    x "( Even through my shorts... his touch feels so invasive... so possessive... )"
    
    show dad lustful at right_small
    dad_says "Fuck… this ass is even better than your mother;s. So soft and tight. I'm going to ruin it tonight."
    
    show madd trembling at left_small
    x "( His filthy hand is groping my bare ass… I want to scream but nothing comes out. I feel so fucking violated. )"
    
    show madd distressed at left_small
    x "( The pressure is building... my heart is pounding so hard I think it might explode )"
    
    show madd anxious at left_small
    x "( His fingers flex... kneading through my shorts... exploring the curve... testing the firmness )"
    
    show dad possessive at right_small
    dad_says "Don't pretend you're asleep, you filthy slut. I know your cunt is already getting wet for me."
    dad_says "Even if you wont , i certainly will"
    
    show madd violated at left_small
    x "( It's so intimate... so invasive... even with the barrier of fabric between his skin and mine )"
    
    show madd shocked at left_small
    x "( Each squeeze sends a jolt through my entire body... unwanted sensations I don't know how to process )"
    
    show dad hungry at right_small
    dad_thinks "(The way her body is responding to my touch. The way she's breathing faster now. How long has it been since I've felt another body like this?)"
    
    show madd paralyzed at left_small
    x "( His other hand joins... both palms now pressing against my ass from outside my shorts )"
    
    show madd self loathing at left_small
    x "( I can't believe he's doing this... I can't believe I'm just lying here... accepting it... )"
    
    show dad desperate at right_small
    dad_thinks "(I'm squeezing both cheeks now. Both of her buttocks in my hands. She's real. She's here. This is happening.)"
    
    show madd distressed at left_small
    x "( He's massaging me through the fabric... in slow, deliberate circles... like he's memorizing the shape )"
    
    show madd helpless at left_small
    x "( And I'm completely trapped... pinned between his body and the mattress )"
    
    show dad obsessed at right_small
    dad_says "The softness. God, your body is even better than i imagined. How your muscles respond to my touch. You are even better than your mom.)"
    
    show madd horrified at left_small
    x "( He's comparing me to her again... even now... while violating me... )"
    
    show madd conflicted at left_small
    x "( And the worst part is... I understand he's broken... that he can't separate us in his mind anymore )"
    
    show madd helpless at left_small
    x "( But understanding doesn't stop the violation... understanding doesn't make this feel less wrong )"

    
    show madd paralyzed at left_small
    x "( His hands are kneading now... rhythmic... hypnotic... like he's trying to memorize every curve through the thin barrier of cloth )"
    
    show madd distressed at left_small
    x "( And I'm trapped here... pinned by the weight of his hands and the weight of my own shame )"
    
    show madd anxious at left_small
    x "( His thumbs find... even through my shorts... the crease between my cheeks... rubbing... teasing... )"
    
    show madd shocked at left_small
    x "( I feel my body respond involuntarily... my core heating... my body betraying me... )"
    
    show dad greedy at right_small
    dad_says "Ah , i feel it Maddie , I can hear your heavy breathing. You body is beginning to want this, even if her mind is screaming no"
    dad_says "Soon you will learn to love it . "
    
    show madd horrified at left_small
    x "( No... no, my body is betraying me... I'm not responding to him... I'm not... )"
    
    show madd self loathing at left_small
    x "( But the physical response is undeniable... the heat building... the shameful arousal... )"
    
    show madd distressed at left_small
    x "( And I want to die... I want to disappear into the mattress and never come back )"
    
    show dad fixated at right_small
    dad_says "you know what I want from you dont you Maddie"
    dad_says "I was never able to have a child with your mom , perhaps you can change that ."
    
    # MENU 2: Right when he starts pulling her shorts down
    show madd horrified at left_small
    x "(What the fuck ??  He's going to expose me... his hand is moving to my waistband...Does he really fantasize about me getting pregenant with his child ? )"
    
    show madd horrified at left_small
    x "( This is crossing a line... bare skin... direct contact... )"
    
    # SCENE 1.5: His hand moving into her shorts - violation escalation
    scene scene_dad_ass_shorts_invasion
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd paralyzed at left_small
    x "( His hands move lower... finding the waistband of my shorts )"
    
    show madd distressed at left_small
    x "( I should stop him... I should say something... but the words won't come )"
    
    show dad lustful at right_small
    dad_says "You knew I could've raped that tight little ass tonight, didn't you? yet you crawled in my bed like a whore"
    dad_says "Perhaps this was your intention all along? Are you secretly a slut for old man like me "
    x "(Shut the fuck up , as if this moment wasnt degrading enough his words are making it much more worst .)"

    scene scene_dad_ass_shorts_lower
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd shocked at left_small
    x "( His fingers slip inside... sliding down toward my ass )"
    
    show madd horrified at left_small
    x "( The intimate contact makes my skin crawl... makes my stomach turn with revulsion and shame )"
    
    show madd violated at left_small
    x "( But I still don't move... still don't speak... )"
    
    show madd self loathing at left_small
    x "( How did I let myself sink this low? I'm disgusting for allowing this. )"
    
    show dad horny at right_small
    dad_thinks "(She's completely exposed now. No shorts between my hands and her bare ass. God, she's exactly like her mother... the same curve... the same soft warmth...)"
    
    show dad greedy at right_small
    dad_says "You're so beautiful... just like your mother was... even better, actually. You're younger. Tighter."
    
    show madd traumatized at left_small
    x "( His words make it worse... like I'm not even myself... like I'm just a replacement for someone dead )"
    
    show madd distressed at left_small
    x "( His hand squeezes... gropes... pulls me against him more firmly )"
    
    # MENU 3: Right after he gropes her bare ass
    show madd horrified at left_small
    x "( His hand is about to touch bare skin... my completely exposed ass... )"
    
    show madd shocked at left_small
    x "( No turning back now... he's about to touch me directly. )"
    
    show madd horrified at left_small
    x "( There's no turning back from this... once he touches me like this... I'm completely his... )"
    
    
    # SCENE 2: Groping her bare buttocks - aggressive possession
    scene scene_dad_ass_bare_grope
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show dad lecherous at right_small
    dad_says  "I love this moment , i love your body . You're going to be mine in ways your mother never was. I'm going to own every inch of your body... I'm going to mark her so deeply she'll never forget who you belongs to...)"
    
    show madd violated at left_small
    x "( His other hand slides around my waist, trapping me completely against his body )"
    
    show madd helpless at left_small
    x "( I can't move forward... I can't move back... I'm pinned between his body and the mattress )"
    
    show madd horrified at left_small
    x "( His fingers explore... kneading... possessive... like he's memorizing every curve, every soft place where he can cause pain )"
    
    show madd paralyzed at left_small
    x "( Throughout the night, his hands never stop moving... never stop claiming me )"
    
    show madd distressed at left_small
    x "( He touches me constantly... like he's trying to prove to himself that I'm real... that she's not gone )"
    
    show madd self loathing at left_small
    x "( And the sickest part... is the way my body is responding... the warmth building... the shameful wetness... )"
    
    show madd helpless at left_small
    x "( And I just lie there... letting it happen... becoming less of a person with each touch )"
    
    show dad debased at right_small
    dad_says "I can tell your mental barriers are coming down . Soon you won't even try to resist anymore.  By next week, you won't need coercion anymore. I will make sure you will be begging for this. )"
    
    show madd distressed at left_small
    x "( Hours pass... or maybe minutes... time feels meaningless... )"
    
    show madd depressed at left_small
    x "( His hands finally slow down... his breathing becomes heavy and satisfied... he's falling asleep )"
    
    show madd paralyzed at left_small
    x "( I lie completely still... waiting to make sure he's fully asleep... )"
    
    show madd stressed at left_small
    x "( Minutes pass... I can hear his snores... the sound making my skin crawl )"
    
    show madd violated at left_small
    x "( I can still feel the places his hands have been... like invisible brands. )"
    
    show madd flustered at left_small
    x "( I carefully slip out from under his arm, my skin crawling with shame... with the evidence of what just happened... )"
    
    if stole_2000_dollars:
        show madd broken at left_small
        with dissolve
        x "( I had already stolen 2000 dollars from him , i dont know why i still slept with him .)"
        $ character_relations["dad"]["lust"]=max(character_relations["dad"]["lust"]-50,0)
        $ character_relations["dad"]["intimacy"]+=0.25
        $ character_relations["dad"]["anger"]=max(0,character_relations["dad"]["anger"]-10)
        $ madd_willpower=max(0,madd_willpower-20)
        call sleep_on_bed_dad_room from _call_sleep_on_bed_dad_room_1 

    show madd stressed at left_small
    x "( I feel so ashamed... so violated... but this is my chance to find money... to escape this... )"

    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd self loathing at left_small
    x "( I move quietly around the room, trying not to wake him )"
    
    show madd focused at left_small
    x "( I search through the nightstand drawers... nothing )"
    
    show madd conflicted at left_small
    x "( I check under the bed... behind the furniture... )"
    
    show madd stressed at left_small
    x "( My body is exhausted, my mind is broken, but I push forward )"
    
    show madd distressed at left_small
    x "( 10 minutes... 15 minutes... 20 minutes of searching... )"
    
    show madd uncertain at left_small
    x "( I'm running out of time and energy... )"
    
    show madd depressed at left_small
    x "( This is all for nothing... I gave myself... my body... for absolutely nothing... )"
    
    show madd stressed at left_small
    x "( I check one more drawer... behind some papers... my hands shaking with frustration )"
    
    show madd shocked at left_small
    x "( Wait... what's this? )"
    
    show madd hopeful at left_small
    x "( A USB drive... just sitting there... like it was waiting for me... )"
    
    # SCENE 3: The USB discovery - finding the wallet
    scene scene_dad_ass_usb_discovery
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd uncertain at left_small
    x "( I grab it with shaking hands and quietly leave the room )"
    
    show madd nervous at left_small
    x "( I need to get to my room... I need to check what's on this... )"
    
    show madd stressed at left_small
    x "( I move through the hallway, terrified he'll wake up and follow me )"
    
    show madd determined at left_small
    x "( I reach my room and close the door... lock it )"
    
    show madd focused at left_small
    x "( I plug the USB into my laptop and open it )"
    
    show madd shocked at left_small
    x "( Cryptocurrency wallet files... multiple encrypted wallets... )"
    
    show madd hopeful at left_small
    x "( The total value... is... 2000 dollars... exactly what I need... )"
    
    show madd relieved at left_small
    x "( This is... this is everything... )"
    
    show madd happy at left_small
    x "( Tears start streaming down my face... tears of relief... tears of hope... )"
    
    show madd submissive nod at left_small
    x "( I'm crying... actually crying from happiness and the terrible cost of this escape... )"
    
    show madd determined at left_small
    x "( I have what I need to escape... to get away from this house... from him... )"
    
    show madd focused at left_small
    x "( I carefully eject the USB and pocket it )"
    
    show madd hopeful at left_small
    x "( I wipe my tears and try to compose myself... )"
    

    if not stole_2000_dollars:
        $madd_money+=2000
        $stole_2000_dollars = True
        $stole_2000_dollars_date = game_time.get_date_string()
        $stole_2000_dollars_day = days_passed
    

    scene madd_in_bed_with_dad
    with fade
    show madd stressed at left_small
    x "( I need to go back to his room... I need to make sure he doesn't know what I did... )"
    
    x "( I quietly walk back through the hallway, feeling numb )"
    
    show madd nervous at left_small
    x "( My heart is still racing... but now it's with hope instead of pure fear )"
    
    show madd resigned at left_small
    x "( I slip back into bed next to him )"
    
    show madd paralyzed at left_small
    x "( His arm immediately wraps around me, pulling me back against his body )"
    
    show dad laugh at right_small
    dad_says "Mmm... that was exactly what I needed. You're learning so well. Soon you won't need any convincing at all."
    
    show madd determined at left_small
    x "( But now I know... it's almost over... )"
    
    show madd focused at left_small
    x "( I have the money... I can escape... very soon... )"
    
    show madd horrified at left_small
    x "( Again? No... I can't... I won't... )"
    
    show madd self loathing at left_small
    x "( But deep down, I know he's right... I probably will come back... if I can't get away fast enough... )"
    $ character_relations["dad"]["lust"]=max(character_relations["dad"]["lust"]-50,0)
    $ character_relations["dad"]["intimacy"]+=5
    $ character_relations["dad"]["anger"]=max(0,character_relations["dad"]["anger"]-10)
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ madd_willpower=max(0,madd_willpower-20)
    $ journal_event_set_done("Dad", "Sleep With Dad: Ass Night")
    call sleep_on_bed_dad_room from _call_sleep_on_bed_dad_room_2 


label step_dad_rimming_2_aftermath:
    # Step dad rimming 2 aftermath scene
    
    scene scene_dad_room_dad_sitting_on_bed
    with fade
    show dad smirk at right_small
    with dissolve
    
    dad_says "Hmm, remmber that time when you licked my ass?"
    
    show madd horrified at left_small
    x "um.. "
    
    show madd distressed at left_small
    x "(I can't believe he's asking me to do that again...)"
    
    show dad lustful at right_small
    dad_thinks "(She's uncomfortable. Good. That discomfort makes her vulnerable, and vulnerability is exactly what I need from her.)"
    
    dad_says "That was quite something."
    
    show madd trembling at left_small
    x "(My entire body is shaking at the memory...)"
    
    show dad predatory at right_small
    dad_says "I Want to do that again. Now."
    
    show madd shocked at left_small
    x "(The demand hits me like a physical blow...)"
    
    scene step_dad_rimming_2_aftermath_dad_standing_infront_of_madd
    with fade

    show madd paralyzed at left_small
    x "(I fell to the floor right next to the bed.)"
    
    show madd horrified at left_small
    x "(I look up at him, feeling a mix of nervousness and panic.)"
    


    show dad obsessed at right_small
    dad_thinks "(She's on the floor already... such perfect compliance. She's learning.)"
    dad_says "You're gonna lick my asshole just like last time ,and you're gonna like it. "
    
    show dad lecherous at right_small
    x "(I saw him move closer to me with a mischievous grin on his face.)"
    
    show madd horrified at left_small
    x "(then he turned around making his ass face me.)"
    
    scene  step_dad_rimming_2_aftermath_dad_standing_butt_facing_madd
    with fade

    show madd disgusted at left_small
    x "(I heard rustling sounds as he adjusted his position and lowered his pants just a little. I could see the crease of his ass but not the whole thing.)"
    
    show madd shocked at left_small
    x "(My heart raced as I saw his bare buttocks exposed to me. It was a fear tactic , him showing only parts of his ass where my face will be burried soon.)"
    
    show madd self loathing at left_small
    x "( I was reminded of the last time i woke up and he was lowering himself to my face. He then lowered his jeans more and removed it. )"
    scene step_dad_rimming_2_aftermath_dad_standing_butt_facing_madd_dad_naked
    with fade

    show madd helpless at left_small
    x "(He then started moving backwards, closer to my face.)"
    
    show madd paralyzed at left_small
    x "(I could not run away, I was frozen in place.)"
    
    show dad hungry at right_small
    dad_thinks "(Her helplessness is intoxicating. She's completely at my mercy.)"
    
    show madd anxious at left_small
    x "(As it got closer, I could feel the warmth and the scent of his skin.)"
    
    show madd disgusted at left_small
    x "( the same scent that I remembered from before. putrid yet oddly familiar.)"
    
    show madd horrified at left_small
    x "(I was inches away from his ass.)"
    
    show dad dominant at right_small
    dad_thinks "(She's trembling... perfect.)"
    
    scene step_dad_rimming_2_aftermath_dad_standing_butt_facing_madd_dad_naked_ass_touch_madd_face
    with fade

    show madd distressed at left_small
    x "(he moved backwards even more and now finally his ass touched my face.)"
    
    show madd violated at left_small
    x "(I could feel the texture of his skin against my face.)"
    
    show madd depressed at left_small
    x "(just like last time, the smell was overwhelming but slowly I started to get used to it.)"
    

    scene step_dad_rimming_2_aftermath_dad_standing_butt_facing_madd_dad_naked_ass_touch_madd_face_hand_behind_madd_head
    with fade
    show madd helpless at left_small
    x "(I felt a hand on the back of my head, pressing me closer to him.)"
    
    show madd distressed at left_small
    x "(My face was now burried in his ass cheeks.)"
    
    show dad greedy at right_small
    dad_thinks "(She's completely consumed by my scent now... she belongs to me.)"
    
    show madd distressed at left_small
    x "(It felt like there was no air left to breathe other than the smell coming from his asshole.)"
    
    show madd anxious at left_small
    x "(the heat coming from his asshole was intense.)"
    
    show dad possessive at right_small
    dad_says "That's it , just like that"
    
    scene step_dad_rimming_2_aftermath_dad_standing_butt_facing_madd_dad_naked_ass_touch_madd_face_hand_behind_madd_head_more_deep
    with fade

    show madd paralyzed at left_small
    x "(i could feel his hand gripping my head tightly. And my face went in deeper inside his ass. It was like all around me i could see his gigantic ass and the air was all coming from his asshole.)"
    
    show dad cruel at right_small
    dad_says "Now use your tongue. "
    
    show step_dad_rimming_2_aftermath_madd_licking_dad_butthole at topleft
    with Dissolve(2.0)

    show madd horrified at left_small
    x "(i hesitated for a moment but then I started to move my tongue near his asshole.)"
    
    show madd disgusted at left_small
    x "(The taste was indescribable, a mix of salty and bitter flavors that overwhelmed my senses.)"
    
    show madd self loathing at left_small
    x "(The taste on my tongue, the smell in my nose, it was as if I was eating something . The more i eat the more he gain control over me.)"
    
    show dad obsessed at right_small
    dad_thinks "(She's licking... she's actually doing it... I own her completely now.)"
    
    show madd depressed at left_small
    x "(I could feel his body tensing up as he let out a low moan.)"
    
    show dad lustful at right_small
    dad_says "Yes, just like that. You're doing great."
    
    show madd traumatized at left_small
    x "(My lungs were filling with the scent of his asshole, making it hard to think about anything else.)"
    
    show madd helpless at left_small
    x "(then suddenly his hand tightened on my head and I felt a sudden pressure.)"
    
    show dad lecherous at right_small
    dad_says "Now put your tongue inside my asshole. Clean it up for me."
    
    show step_dad_rimming_2_aftermath_madd_licking_dad_butthole_at_butthole at topleft
    with Dissolve(2.0)

    show madd horrified at left_small
    x "(I hesitated for a moment, but then I slowly moved my tongue closer to his asshole.)"
    
    show madd violated at left_small
    x "(I put my tongue at the entrance of his asshole hesitating another moment but then I felt him push my head forward.)"
    
    show dad dominant at right_small
    dad_thinks "(She's yielding completely... no more resistance... just obedience.)"
    
    show madd paralyzed at left_small
    x "(Using my tongue i started pushing inside his asshole. It was a tight fit but I managed to get a few inches in.)"
    
    show madd disgusted at left_small
    x "(The taste was even more intense now, a combination of salty, bitter, and musky flavors that made my head spin.)"
    
    show madd self loathing at left_small
    x "(i kept moving my tongue , making it wiggle so i can put it deeper inside his asshole.)"
    
    show dad obsessed at right_small
    dad_thinks "(God... her tongue... she's completely mine now...)"
    
    show step_dad_rimming_2_aftermath_madd_licking_dad_butthole_at_butthole_fully_inside at topleft
    with Dissolve(2.0)

    show madd traumatized at left_small
    x "(after a few minutes my tongue was fully inside his asshole. My nose was pressed on the crease of his ass cheeks.)"
    
    show dad greedy at right_small
    dad_says "that's a good submissive little bitch. You like that don't you?"
    
    show madd horrified at left_small
    x "(I continued licking inside his asshole, his words only demeaning me further. I was completely at his mercy.)"
    
    show madd self loathing at left_small
    x "(I can't say no to him. I'm his obedient submissive little daughter, after all.)"
    
    show madd distressed at left_small
    x "(I dont know if it was the humiliation or the pheromones, but I found myself getting more and more turned on.)"
    
    show dad possessive at right_small
    dad_thinks "(She's responding to me... to my dominance... she's starting to crave this...)"
    
    show madd conflicted at left_small
    x "(Licking his asshole, serving him like this... It was strangely exhilarating.)"
    
    show madd horrified at left_small
    x "(What am i becoming... A slave to his desires? A plaything for his pleasure? But why did it feel so right?)"
    
    show madd depressed at left_small
    x "(I pushed those thoughts aside . If i continued down this path, there was no turning back.)"
    
    show madd helpless at left_small
    x "(I continued licking inside his asshole, serving him completely. )"
    
    show madd stressed at left_small
    x "(the faster he came, the sooner this would be over.)"
    
    hide step_dad_rimming_2_aftermath_madd_licking_dad_butthole_at_butthole_fully_inside
    hide step_dad_rimming_2_aftermath_madd_licking_dad_butthole_at_butthole
    hide step_dad_rimming_2_aftermath_madd_licking_dad_butthole

    show dad hungry at right_small
    dad_thinks "(She's lost in me now... completely surrendered...)"
    
    show madd conflicted at left_small
    x "(but the smell, the taste... It was intoxicating. I found myself craving more of it.)"
    
    show dad fixated at right_small
    dad_thinks "(I'm about to come... she's driven me insane...)"
    
    show madd shocked at left_small
    x "(Suddenly, he tensed up, the asshole clenching around my tongue as he let out a guttural moan.)"
    
    show madd paralyzed at left_small
    x "(i knew what was coming next.)"
    
    show madd disgusted at left_small
    x "(his asshole started to contract rhythmically, I couldn't see it as my face was buried deep inside his asshole, but I could feel it.)"
    
    show dad desperate at right_small
    dad_says "AHH! YES! That feels AMAZING! LICK IT ALL OUT!"
    
    show dad possessive at right_small
    dad_thinks "(I'm coming... fuck i want to put it in her mouth but this position is too comfrotable.)"
    
    scene step_dad_rimming_2_aftermath_dad_cumming_ON_floor
    with fade

    show madd traumatized at left_small
    x "(i heard soft moans escape his lips as he came, on the floor .)"
    
    show madd horrified at left_small
    x "( the heat from his asshole increased momentarily and then slowly subsided as he finished.)"
    
    show madd violated at left_small
    x "(I felt the pressure on my head lessen as he pulled away slightly, giving me some relief.)"
    
    show madd disgusted at left_small
    x "(I pulled my tongue out of his asshole, tasting the salty residue .)"
    
    show dad creepy at right_small
    x "(he turned around , lifting his jeans slightly to cover his exposed buttocks.)"
    
    show dad smirk at right_small
    dad_says "Good job, now clean that up too."
    
    scene step_dad_rimming_2_aftermath_cleanup_time
    with fade

    show madd self loathing at left_small
    x "(He says that pointing to the mess on the floor. it was his cum, of course.)"
    
    show madd distressed at left_small
    x "(I was getting up to get some paper towels when he spoke again.)"
    
    show dad dominant at right_small
    dad_says "not so fast . Clean it with your tongue."
    
    show madd horrified at left_small
    x "(i hesitated for a moment, but the look in his eyes told me there was no room for refusal.)"
    
    show dad possessive at right_small
    dad_thinks "(She'll obey. She always obeys now.)"
    
    scene step_dad_rimming_2_aftermath_cleanup_time_licking_cum
    with fade

    show madd paralyzed at left_small
    x "(I got down on my hands and knees, leaning over to lick up the mess on the floor.)"
    
    show madd disgusted at left_small
    x "(the taste was salty and slightly bitter, but I obediently licked it all up.)"
    
    show madd traumatized at left_small
    x "(It all reminded me of that night , i first put my tongue in his asshole and then he shoved his cock in my mouth and came inside it. )"
    
    show madd horrified at left_small
    x "(Up close i saw it , his cum was very white and thick , it looked like cream )"
    
    show madd self loathing at left_small
    x "(i have read about this. It signifies high testosterone levels and good fertility .)"
    
    show madd anxious at left_small
    x "(If he puts this inside my pussy I might get pregnant easily .)"
    
    show madd worried at left_small
    x "(I should try to keep him away from my pussy if I don't want to get pregnant or lose my virginity .)"
    
    show madd depressed at left_small
    x "(I continued licking his cum off the floor  .)"
    
    show madd stressed at left_small
    x "(After a while i was finished licking all the cum off the floor. And i looked up at him .)"
    
    show dad creepy at right_small
    dad_says "There you go sweetie , you did a good job ."
    
    show dad smirk at right_small
    dad_thinks "( She looked very obedient now. She's learned her place.)"
    
    show madd helpless at left_small
    x "( He looked very satisfied now . )"
    
    show dad possessive at right_small
    dad_says "Now get out of here. "
    
    show madd traumatized at left_small
    x "(I got up and left the room quickly . )"

    $ character_relations["dad"]["intimacy"]+=7
    $ character_relations["dad"]["lust"]=0
    $ character_relations["dad"]["anger"]=max(0,character_relations["dad"]["anger"]-20)
    $ character_relations["dad"]["oral_sex"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $madd_willpower=max(0,madd_willpower-30)
    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_36
    $ journal_event_set_done("Dad", "Forced Rimming 2")

    jump step_parent_room_scene


#Events linked to him walking on shower

label dad_walks_in_shower:
    scene scene_dad_walks_in_home_bathroom_madd_in_towel
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd uncertain at left_small
    x "(I'm wrapped in my towel, just stepping out of the shower.)"
    
    show madd shocked at left_small
    x "(The bathroom door opens without a knock.)"
    
    show dad obsessed at right_small
    dad_says "Ah dear daughter. I didn't know you were in here."
    
    show madd horrified at left_small
    x "(He doesn't leave. He just says those words as he closes the distance between us.)"
    
    show madd trembling at left_small
    x "(My naked body covered only by a thin towel...)"

    scene scene_dad_walks_in_home_bathroom_madd_in_towel_hand_on_shoulder
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd paralyzed at left_small
    x "(He reaches out and places a hand on my shoulder. What a fucking creep.)"
    show dad creepy at right_small
    dad_says "Its really cold isnt it? "
    show madd horrified at left_small
    x "(I want to scream at him to get the fuck out, but I can't. I'm frozen in place.)"

    scene scene_dad_walks_in_home_bathroom_madd_in_towel_tries_to_remove_towel
    with dissolve 
    $ renpy.call_in_new_context("_hide_windows")
    show madd trembling at left_small
    x "(His hand grips my shoulder tightly as his other hand goes lower to the towel. I try to pull away, but he's too strong.)"
    show dad manipulative at right_small
    dad_says "how are you doing Maddie ? Was the shower okay ?"
    show madd horrified at left_small
    x "(He uses his words as distraction as he tries to pull the towel away from my body. )"
    show madd determined at left_small
    x "(I know whtat he's trying to do, but I can't let him win. I have to fight back.)"
    show madd stressed at left_small
    x "I'm fine..."
    x "(I hold the towel tightly to my body, trying to keep it from being pulled away.)"
    show madd distressed at left_small
    x "Please...don't...dad..."
    x "I know what you're trying to do...please just stop..."
    show madd shocked at left_small
    x "(I see the smug look on his face evaporate into confusion and then anger. )"

    scene scene_dad_walks_in_home_bathroom_madd_in_towel_removes_towel
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    x "(He looks at me with rage in his eyes. Then suddenly he removes my towel from the other side and drops it to the floor. )"
    show dad angry at right_small
    dad_says "You dont tell me what to do Maddie. I fucking own you as long as you live under my roof. "
    show dad dominant at right_small
    dad_says "Bitch, you will do as I say. You will let me do what I want to you. "
    show madd paralyzed at left_small
    x "(I was completely exposed now, standing there in front of him with nothing but my bare skin. )"
    show madd violated at left_small
    x "(his hands slide down my body, as he pinches my nipples and then immediately after that his hands go lower to my crotch. I try to pull away again, but he's too strong. )"
    show madd helpless at left_small
    x "(His fingers run over my clit and then he starts to rub it. )"

    scene scene_dad_walks_in_home_bathroom_madd_in_towel_removes_towel_rubbing_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad lecherous at right_small
    show madd violated at left_small
    x "(He starts to rub my clit with his fingers, and then only a small part of his fingers would go inside me and he would pull them out)"
    show madd helpless at left_small
    x "(As soon as his fingers actually entered me, even just the tips, my knees went weak. If it wasnt for his hands holding me up, I would have collapsed to the floor. )"
    x "(My mouth opened on its own. A soft, shaky moan slipped out before I could stop it. Then another one followed right after as he kept rubbing my clit in slow circles while pushing just the very tip of his fingers in and out of me.)"
    show madd conflicted at left_small
    x "(It felt so wrong. He was barely even inside me, just teasing the entrance, but my body was already reacting. I could feel myself getting wet around his fingers while he kept rubbing that sensitive spot on my clit.)"
    show madd distressed at left_small
    x "Da...dad...please stop..."
    show dad sadistic at right_small
    dad_says "Stop? Look at you you're already so wet."
    show dad mocking at right_small
    dad_says "Whore daughter loves her daddy's fingers in her pussy ? Huh ?"
    show madd paralyzed at left_small
    x "(His fingers kept moving — slow, teasing rubs on my clit while he only ever pushed the very tips inside me. Never going deeper. Just enough to make my pussy clench around nothing and leak more onto his hand.)"

    scene scene_dad_walks_in_home_bathroom_madd_in_towel_removes_towel_rubbing_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    x "I....I'm not....wet"
    x "(I speak shakingly, trying to deny the obvious. But my body betrays me as I feel myself getting wetter and wetter around his fingers.)"
    x "I...just...had a hot shower..."
    show madd shocked at left_small
    x "(Without warning he suddenly pushes more of his fingers inside me. Almost half of them. It stretches me open wider than before and I feel them sink in deep.)"

    scene scene_dad_walks_in_home_bathroom_madd_in_towel_removes_towel_rubbing_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show dad sadistic at right_small
    dad_says "Hot shower? Bullshit. With how hot and wet this pussy is right now, any water from the shower would've evaporated already."
    show dad mocking at right_small
    dad_says "Or maybe it just got hotter when I started touching you ? Slutty girl."
    show madd violated at left_small
    x "(His fingers are thicker now, pushing deeper. I can feel them sliding through all the slickness that's coming out of me. There's no way to hide it anymore. It's making wet, nasty sounds every time he moves them.)"
    show madd helpless at left_small
    x "(He curls his fingers a little and starts rubbing that spot inside while his thumb keeps working my clit. My legs are shaking so bad now making my whole body tremble. )"
    show dad lecherous at right_small
    dad_says "Ah lovely breasts. So perky and soft. Just like I like them."
    show madd conflicted at left_small
    x "(No ...noo... I can't let him win. I have to fight back. My stomach is getting all warm and fluttery )"
    show madd self loathing at left_small
    x "(Fuck...I can feel myself getting close...please not from him...please not from him... )"

    scene scene_dad_walks_in_home_bathroom_madd_in_towel_removes_towel_rubbing_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd helpless at left_small
    x "(His fingers suddenly start moving faster. Much faster. They piston in and out of me roughly while his thumb rubs hard circles on my clit. I can't keep up with it.)"
    x "(My legs completely give out. The only thing holding me up is his arm behind my back and his hand between my legs. I feel it building too fast, too strong. I can't stop it.)"
    show madd conflicted at left_small
    x "(Fuck...not...not now...please...if I cum now...he'll know...he'll know I like it...I can't let him know...I have to hold it in...but it's getting so hard to do...)"
    show madd flustered at left_small
    x "(It hits me hard. My whole body jerks and I cum. Hard. A hot, messy stream shoots out of me but his hand is right there, fingers still buried inside, so it splits — some of it sprays forward onto the floor and some of it goes backward between my legs, running down my butt and thighs.)"
    show dad cruel at right_small
    dad_says "Hah! Look at that. You're cumming all over the fucking place. What a filthy little slut. Cumming from your own dad's fingers like a cheap whore."
    show madd traumatized at left_small
    x "(He laughs right in my face while I keep twitching. More keeps coming out in short, uncontrolled spurts because his fingers are still moving inside me. It's going everywhere — on his hand, down my legs, dripping onto the bathroom floor in wet streaks.)"
    show madd self loathing at left_small
    x "(I can't even speak. My mouth is open but only broken sounds come out. My body won't stop shaking. I can feel how wet everything is now — my thighs, the floor, his wrist. It's disgusting. I came so hard I made a mess and he's still laughing at me.)"
    show dad mocking at right_small
    dad_says "Couldn't even hold it in, could you? Your pussy just started squirting the second daddy sped up. Pathetic."
    show madd distressed at left_small
    x "(I want to disappear. I want to push him away. But my body is still twitching around his fingers and I can't stop the small aftershocks that keep making more of that warm mess leak out of me.)"
    show dad possessive at right_small
    dad_says "Remember this moment, Maddie. Remember how you cummed all over the place from daddy's fingers. "
    show dad dominant at right_small
    dad_says "Well i made you cum , so you owe me now. You know you should swallow my cum as a thank you for making you feel so good. "
    show madd traumatized at left_small
    x "(He kept humiliating me like that for a while longer, making me feel even worse about what just happened. I was so ashamed and disgusted with myself. )"
    show madd violated at left_small
    x "(After a while, he finally stopped and just stood there looking at me with that smug expression on his face before leaving the bathroom without another word. I was left there, trembling thinking about what just happened and feeling completely violated.)"
    show madd self loathing at left_small
    x "Fuck.Fuckkk.Fuckk.. I cant believe that just happened. Fucking end my life right now..."

    $ character_relations["dad"]["lust"] = max(character_relations["dad"]["lust"]-50, 0)
    $ character_relations["dad"]["intimacy"] += 5
    $ character_relations["dad"]["anger"] += 20
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ madd_willpower = max(0, madd_willpower - 20)
    $ journal_event_set_done("Dad", "Dad Walks In Shower")
    call advance_time_and_check(minutes=30) from _call_advance_time_and_check_110

    jump shower_nothing_happens


#Events linked to kitchen minigame


label miss_event_dad:
    
    scene scene_kitchen_minigame_madd_standing
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd nervous at left_small

    x "(I was busy cooking a quick meal for myself when I heard footsteps coming from behind me.)"
    x "(Whoever it was, they were getting closer. I just hope they dont try anything funny.)"

    scene scene_miss_event_dad_misses_1_scene_1_dad_standing_behind_madd
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd worried at left_small

    x "(I continued cooking , trying to ignore the footsteps, but they stopped right behind me.)"
    x "(lets just finish this meal and get out of here.)"

    scene scene_kitchen_minigame_madd_dad_standing_closes_distance
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd shocked at left_small

    x "(Suddenly , i heard footsteps again ...whoever it was, they were getting closer. My shoulders tensed up as I prepared myself for someones presence right behind me.)"
    x "(He wraps his hairy arms around me , his head resting on my shoulder. Thats when i turned around to see who it was.)"
    x "(It was my stepdad, he had a big smile on his face as he asked)"
    show dad possessive at right_small
    dad_says "How are you doing, Maddie ? I smell something good cooking in here."
    show madd anxious at left_small
    x "(He was holding me tightly, and I could feel his breath on my neck. Why is he getting so close to me ? )"
    x "Um...I am fine dad, just cooking some food."

    scene scene_kitchen_minigame_madd_dad_standing_closes_distance_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad hungry at right_small

    x "(He lowers his hands down to my waist, and he asks )"
    dad_says "What are you cooking Maddie ?"
    show madd horrified at left_small
    x "(As soon as he said that , i felt his chin on the beck of my neck, he was inhaling my scent, and it made me feel uncomfortable. )"
    show dad lecherous at right_small
    dad_says "It smells so good, I wish I could have a taste."
    show madd paralyzed at left_small
    x "(Right after he said that he landed a soft kiss on my neck , the wetness of  his lips sent shivers down my spine. I was frozen in place, not knowing how to react to his sudden affection.)"
    x "(I wanted to push him away, but I was too scared to do so. I just stood there, hoping that he would stop.)"
    x "(Obviously , he took this as a sign as consent and continued to kiss my neck)"

    scene scene_kitchen_minigame_madd_dad_standing_closes_distance_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad wistful at right_small

    dad_says "Maddie, you remind me of your mother, you know that ?"
    show madd distressed at left_small
    x "(His hands started to roam around my butt area , the thin fabric of my shorts did little to stop him from feeling my skin. )"
    x "(His hands roaming around my waist and hips, while his kiss got more intense)" 
    show madd hesitant at left_small
    x "I...I know dad, you always say that. "
    x "Could you please stop ? I ...I just want to finish cooking and eat my food. "

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad lecherous at right_small

    dad_says "You wouldnt want dad to go without tasting your cooking, would you Maddie?"
    show madd violated at left_small
    x "(Right after he said that, he started to lick my neck, his tongue tracing the back of my neck )"
    x "(He's using food as an excuse to taste me, I can't believe this is happening. What the hell is wrong with him ? )"
    show madd horrified at left_small
    x "(I looked back at him, hoping that he would stop, right when i looked back he stopped licking my neck and looked me in the eyes, his expression was a mix of desire and frustration.)"
    x "(He is lusting for his own stepdaughter, this is disgusting. I knew his pause was just to catch his breath before he continued with his advances.)"

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small

    x "Dad...PLease...this is not right , you are my stepdad "
    show dad dominant at right_small
    x "(Suddenly he continued with his licking but this time he was more aggressive, his tongue was rough against my skin, from bottom of my neck to the back of my ear, he was marking me with his saliva, like a dog marking its territory. )"
    show madd shocked at left_small
    x "(My eyes  widened in shock and disgust, not only was he licking my neck, but he was doing it in a way that made it clear that he was claiming me as his own. )"
    show dad yearning at right_small
    dad_says "You remind me so much of your mother, Maddie. I can't help myself around you."
    dad_says "Plus now that your mom is gone, I feel like I have to take care of you in every way possible. " 
    show madd distressed at left_small
    x "(I couldn't believe what I was hearing, he was using my mother's death as an excuse to justify his inappropriate behavior towards me. )"
    show madd feels violated at left_small
    x "(HIs hands started wandering everywhere on my body, he was touching me in places that made me feel violated it was a sign that he had no respect for my boundaries. )"
    show madd anxious at left_small
    x "(I started cutting my vegetables faster, knowing that the longer I stayed in this situation, the worse it would get. )"

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad sadistic at right_small

    x "(He started to slowly spank my butt now , each spank reverberating through the kitchen reminding me of how powerless I was in this situation. )"
    show madd helpless at left_small
    x "(I looked back at him hoping that he would stop like he did before, but this time he didn't stop . This time when I looked back at him, his spanking got more aggressive )"
    show dad controlling at right_small
    x "(It was a demonstration of his dominance over me, a way to assert his control and ownership over my body. )"
    x "(HIs tongue reached my hair too , i felt his saliva soaking my hair)"
    dad_says "Your food tastes so good Maddie , it would be a crime to not share it with others"
    show madd angry at left_small
    x "Fuucking Assshole, you are using food as an excuse to touch me and lick me, you are disgusting. "

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad predatory at right_small

    x "(Suddenly his movements got more aggressive, his licking and his hands rubbing my body were more forceful, it was clear that he was losing control of himself. )"
    show madd trembling at left_small
    x "(He used his weight to bend me over the counter, I was sweating and trembling with fear)"
    dad_says "Your sweat taste good too , i dont  think any man can resist you Maddie. I wonder if your real dad ever tried making a move on you"
    show madd stressed at left_small
    x "(I felt so ashamed that i was sweating so profusely, but it was only fueling his lust for me even more. On top of that he was soiling the name of my dad. )"

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd paralyzed at left_small

    x "(With each passing moment, his actions became more aggressive, his hands were all over my body, and his licking was more intense. )"
    x "(There was a knife in my hand, i should have used it to defend myself, but i was too scared to do so. I just stood there, hoping that he would stop.)"
    show dad fixated at right_small
    x "(Guess that was the moment he realized that I was not going to fight back, and he took full advantage of that. )"

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_and_gropes_maddie
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad horny at right_small

    x "(In his aggressive state , his hands started sliding up my shirt, now landing on my breasts, he was groping them roughly, his fingers squeezing and kneading my flesh like it was a toy. )"
    show madd shocked at left_small
    dad_says "Thats so soft Maddie, did you purposefully not wear a bra for daddy ?"
    show madd disgusted at left_small
    x "(Fking scumbag, you are groping my breasts and asking me if I am not wearing a bra on purpose )"
    x "No..I just feel more comfortable without one "
    show dad entitled at right_small
    x "(He continued to grope my breasts, his hands were rough and aggressive, it was clear that he was not interested in pleasuring me, but rather in asserting his dominance over me. )"
    dad_says "dont lie to daddy, I know you are not wearing a bra on purpose, you want daddy to see your breasts and touch them, dont you ?"
    show madd distressed at left_small
    x "(Does he not understand that I am trying to avoid this situation ? I am not trying to seduce him)"
    show dad mocking at right_small
    dad_says "Your mom couldnt resist my charming personality, and I can see that you cant either"
    x "(What the hell is he going on about ? what charmimg personality ? He looks ugly , he smells bad and he is a creep, how can anyone be attracted to him ? )"
    x "(But i couldnt hold it in anymore, him mentioning my mom was the last straw, I had to say something to him )"
    show madd angry at left_small
    x "You are a disgusting pig and you are not charming at all "
    x "NO woman would ever be attracted to you, If you were the last man on earth i would rather turn lesbian than with you. "
    x "(I was so angry that I was shaking, I wanted to hit him, but I was too scared to do so. I just stood there,but i was glad i spoke up for myself and let him know how disgusting he is. )"

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_and_gropes_maddie_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad manipulative at right_small

    x "(After hearing my words, he didnt say a word but his actions spoke louder than words )"
    x "(He was now licking directly next to my ear , and thats when I realized that he was trying to whisper something to me, but his breath was so hot and close to my ear that I could barely understand what he was saying. )"
    show dad cruel at right_small
    dad_says "You can say what you want slut , but remember that i will be the one to take your virginity"
    dad_says "And when I do , you will submit to me completely, you will be my obedient little stepdaughter..." 
    show madd horrified at left_small
    x "(I was horrified by his words, he was openly admitting that he wanted to have sex with me, and that he expected me to submit to him. )"
    x "(if i heard it in any other setting, I would have thought it was a joke, but him whispering it in my ear while licking my neck made it clear that he was serious about it. )"
    show dad delusional at right_small
    dad_says "And you will learn to love it, you will learn to love me creampieing you and filling you every night "
    show madd broken at left_small
    x "(every nerve in my body was screaming at me to run away, but I was frozen in place, I couldn't move or speak)"
    dad_says "And when you finally have my baby inside you, you and me both will forget that you are my stepdaughter, and we will just be two people in love, a family, a couple. " 
    show madd processing at left_small
    x "(This is not just him imagining this, he is actually saying this to me, he is actually planning for me to get pregnant with his child)"
    show madd traumatized at left_small
    x "(God , i need to get out of this house, i need to get away from him, but i have no money, no car, no job, and no friends to turn to for help. I am trapped here with him and I have no way out. )"

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_and_gropes_maddie_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad coercive at right_small

    x "(After whispering those words in my ear, he continued to grope my breasts and lick my neck while I was shocked trying to process what he just said. )"
    x "(His other hand also started to grope my other breast, he was groping both of them at the same time now )"
    dad_says "Say you're sorry for talking back to daddy"
    show dad authoritative at right_small
    dad_says "say sorry for disrespecting daddy or I will breed you right here on the kitchen counter"
    show madd shaken at left_small
    x "(His both hands started squeezing my breasts roughly, his fingers digging into my flesh, it was like he was holding my breasts hostage, using them as leverage to force me into submission. )"
    show madd resigned at left_small
    x "I....I am sorry dad "
    x "I am sorry for disrespecting you, I am sorry for talking back to you, please forgive me "
    show dad dominant at right_small
    dad_says "Good girl, now you know your place "
    show madd submissive nod at left_small
    x "(I was so humiliated that I had to apologize to him, but I was also relieved that he seemed to be satisfied with my apology, at least for now. )"



    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_and_undresses_maddie
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad greedy at right_small

    dad_says "but now daddys little friend is too excited ...What shall we do about that ?"
    show madd distressed at left_small
    x "(His words made it clear what he wanted to do to me, he wanted to fuck me right here and now)"
    x "Please dad....I cant do this , i dont want anything inside me ...please"
    show madd helpless at left_small
    x "(His hands were now at the waistband of my shorts, he was trying to pull them down, but my hands were holding onto the counter i couldnt stop him from making me naked in the kitchen )"

    x "(He's gonna undress me . If i want to stop him , now is the last chance)"
    if character_relations["dad"]["intimacy"] < 15:
        menu:
            "Try to stop him" :
                if madd_willpower+2*(15-character_relations["dad"]["intimacy"]) >= character_relations["dad"]["lust"]:
                    show madd angry at left_small
                    x "You are my dad, you shouldnt be doing this. If you dont move your hands I will use this knife to stab myself"
                    show dad angry at right_small
                    dad_says "What? Why? why the fuck would you do that ?"
                    x "I ...I will do anything to get away from you asshole."
                    x "(His grip on me loosened as he stopped groping me, but the damage was already done. I could feel the heat of his touch lingering on my skin, and the memory of it burned in my mind)"
                    x "(I heard his footsteps as he angrily walked out of the kitchen, leaving me alone with my thoughts )"
                    $ character_relations["dad"]["anger"] +=20
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_111
                    $ character_relations["dad"]["intimacy"]+=3
                    call advance_time_and_check(minutes=120) 
                    $ madd_willpower=max(madd_willpower-20,0)
                    jump cooking_complete
                else:
                    $character_relations["dad"]["lust"]=0
                    $character_relations["dad"]["anger"] +=20
                    show madd trembling at left_small
                    x "(I wanted to stop him, but i was so scared that i couldnt even say anything, my voice was trembling and my body was shaking)"
                    x "(I just stood there, letting him do whatever he wanted to me, hoping that it would be over soon )"
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_112


    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_and_undresses_maddie_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad lustful at right_small

    x "(My shorts were now halfway down my butt, exposing my bare skin to him)"
    show madd horrified at left_small
    x "(HIs hands were now squeezing my butt cheeks, he was groping them roughly, his fingers digging into my flesh)"
    dad_says "Soo Soft Maddie , I would feel so good to just go inside you right now, to feel your tight little pussy wrapped around my dick"
    show madd broken at left_small
    x "(He was blackmailing me with his words, i cant let him take my virginity...I feel so trapped)"

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_and_undresses_maddie_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd weeping at left_small

    x "(Now my shorts were completely down, exposing my bare butt to him)"
    x "(cold air hit my skin, making me shiver with embarrassment and fear but i knew the shivers were not from the cold, they were from the fear of what was about to happen to me )"
    x "Please...I am begging you, if you put it in me , my life will be over, I will never be able to recover from this, anything but that"
    x "(I was almost on the verge of tears, I was so scared and desperate that I was begging him to not fuck me)"
    x "(Meanwhile his hands were running on my now naked butt, )"

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_naked_maddie_gropes_maddie_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad calculating at right_small

    x "(He squeezed my butt cheeks very tightly once and said  )"
    dad_says "Tch...Fine, I will wait until you are ready"
    show madd relieved at left_small
    x "(I was so relieved that he was not going to force me , but then i thought about it, he didnt say he wouldnt do it at all, he just said he would wait until i am ready)"
    show madd uncertain at left_small
    x "(Basically he is gonna push me further and further until i am ready, and then he will do it to me, he is just waiting for the right moment to strike. )"
    
    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_naked_maddie_gropes_maddie_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad perverted at right_small

    x "(My train of thought was interrupted by him suddenly spreading my butt cheeks apart)"
    dad_says "Such beatiful holes Maddie , I am gonna fill them both up one day"
    show madd horrified at left_small
    x "(I gulped hard, his words were so vulgar and explicit )"
    x "(He was talking about both my pussy and my asshole, I am definitely not safe around him )"
    dad_says "Let me see how it smells down there, I bet it smells so good"
    show madd confused at left_small
    x "Eh...?"

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_naked_maddie_gropes_maddie_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad debased at right_small

    x "(Before I could even process what he just said, he suddenly bent down i felt his breath on my butt cheeks , he was still spreading them apart giving him full access)"
    show madd self loathing at left_small
    x "(This is soo humiliating, I am being bent over the counter and my stepdad is smelling my asshole, this is not how I imagined my life would be at all )"
    x "(Then i felt it , his breath directly on the skin of my asshole , the deepest part of my body and he was inhaling deeply, like he was trying to savor the scent of my asshole )"
    show madd nauseated at left_small
    x "(Strike me down with lightning if this is not the most disgusting thing I have ever experienced in my life )"
    dad_says "Mmm...It smells so good, I can tell you are a clean girl Maddie"
    x "(What the hell , my stepdad is complimenting the smell of my asshole ...why am i alive to experience this ? )"

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_naked_maddie_gropes_maddie_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad lecherous at right_small

    dad_says "I had plans to eat food after this, but your asshole smells so good i might just eat you instead"
    show madd shocked at left_small
    x "(EEEE....... what the hell is going on ? Is he seriously considering putting his tongue in my asshole ? )"
    x "(Thats when i felt it , wet muscles of his tongue on my asshole, he was licking it, his tongue was tracing circles around my asshole)"
    show madd conflicted at left_small
    x "( For some reason ,  i was more worried about the fact that i was hoping my butt was clean enough for him to eat than the fact that my stepdad was licking my asshole)"
    x "(His tongue entered inside my asshole, it was a strange sensation, I felt it wriggling around inside me)"
    x "(is this what its gonna feel like when he fucks me ? this doesnt feel bad at all, it actually feels kind of good, but this is my stepdad, this is not supposed to feel good, this is wrong on so many levels )"
    x "(He continued to lick my asshole for what felt like an eternity, until finally he pulled out his tongue from my asshole)"
    dad_says "Mmm...That tastes so good, I could eat you all day Maddie"
    show dad thinks at right_small
    dad_thinks "God that tasted like battery acid, I hope I dont get sick from this."
    dad_thinks "But i had to compliment her, so that i can make her clean my filthy asshole with her tongue later on, I need to make her feel like this is enjoyable even for the one licking it"
    show dad manipulative at right_small
    dad_says "You should be proud of yourself Maddie, your moms asshole wasnt as clean as yours, I am glad you take care of yourself down there"
    show madd self loathing at left_small
    x "(I hate it when he compares me to my mom, but using this to compliment the smell of my asshole is just disgusting especially)"

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_naked_maddie_gropes_maddie_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd relieved at left_small

    x "(He finally gets back up  to his feet as i sigh in relief, both his hands are off my body now. Oh is he finally gonna stop ? )"
    show madd paralyzed at left_small
    x "(thats when i heard it , his zipper being unzipped, and his pants being pulled down)"
    x "(NO no no ...I am not ready for this, I am not ready for this, I am not ready for this )"
    show dad lustful at right_small
    dad_says "You know you should sleep in the living room Maddie, maybe you will get to taste my asshole too if you did "
    dad_says "Your mom was always cleaning my asshole with her tongue, and she loved it, I am sure you will love it too if you give it a try"
    show madd horrified at left_small
    x "(what the hell what the hell  ! He is trying to get me to lick his asshole too ? not happening ! )"
    x "Dad ....please ...you said you would wait until I am ready, I am not ready for this "

    if character_relations["dad"]["intimacy"] < 40:
        menu:
            "Do not touch me with your penis ! " :
                if madd_willpower+2*(40-character_relations["dad"]["intimacy"]) >= character_relations["dad"]["lust"]:
                    show madd angry at left_small
                    x "I...I have a knife in my hand "
                    x "If...If you do take your dick anywhere near my body I will cut it right off"
                    show dad angry at right_small
                    dad_says "Heh , you cant fool me Maddie. You dont have the balls"
                    x "(I picked the knife and rolled it in my hands to scare him )"
                    x "I might not have the big stinky balls you got but i still got them"
                    dad_says "Tch..I will remember this Maddie , You will never get away from me"
                    x "(I heard his footsteps as he angrily walked out of the kitchen, leaving me alone with my thoughts )"
                    $ character_relations["dad"]["anger"] +=20
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_113
                    $ character_relations["dad"]["intimacy"]+=5
                    call advance_time_and_check(minutes=120) 
                    $ madd_willpower=max(madd_willpower-20,0)
                    jump cooking_complete
                else:
                    $character_relations["dad"]["lust"]=0
                    $character_relations["dad"]["anger"] +=20
                    show madd trembling at left_small
                    x "(I wanted to stop him, but i was so scared that i couldnt even say anything, my voice was trembling and my body was shaking)"
                    x "(I just stood there, letting him do whatever he wanted to me, hoping that it would be over soon )"
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_114   


    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_naked_maddie_rubs_maddie_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad horny at right_small

    x "(Then i felt it, his hard dick pressing against my butt cheeks, i could feel its warmth its veiny texture, and its girth just by its touch)"
    dad_says "Dont worry Maddie , i will just rub myself against you for now, we can save the ultimate pleasure for later"
    show madd shaken at left_small
    x "(this isnt what i wanted to hear but i guess its better than him just shoving it in me right away )"
    x "Okay...dad...can you just cum somewhere else ? I dont want you to cum on me, please"
    x "(He didnt reply to me, he just kept rubbing his hard dick against my butt cheeks i knew he was gonna finish on me )"

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_naked_maddie_touches_maddie_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad debased at right_small

    x "(he finally started moving his hips , i felt my butt skin rubbing against his hard dick, it was a strange sensation )"
    x "(It was like my skin was being used as a makeshift condom, it was not pleasurable at all, it was just uncomfortable and humiliating )"
    x "(He would put his dick between my butt cheeks and pull back and then smack it back between them again , like he was trying to get me used to the sensation of having something between my butt cheeks)"
    show madd disgusted at left_small
    x "um...what are you doing ? "
    dad_says "Dont worry , just cleaning my dick with your butt cheeks, its a common practice in some cultures, you should be honored that I am sharing this with you"
    show madd nauseated at left_small
    x "(What the hell is he talking about ? clean it how ?)"
    x "(Then i realized what he meant, my skin was pulling his dick back and the smegma and precum on his dick was getting wiped on my skin, he was using my butt cheeks as a way to clean his penis, this is so disgusting )"
    x "(How does he even come up with this stuff ? )"

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_naked_maddie_touches_maddie_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad possessive at right_small

    dad_says "I see my friend is shedding its filth on your butt cheeks, you should be proud of that Maddie"
    show madd overwhelmed at left_small
    x "(UGH i should just use this knife to slit my  own throat right now)"
    x "(he continued this weird rubbing which was only to clean himself on me , after a while i could feel the sticky mess of his precum and smegma all over my butt cheeks)"
    show madd traumatized at left_small
    x "(Thats when i realized the whole room was smelling like his penis, the scent of my stepdad's dick was so strong that it was permeating the entire kitchen especially when he started cleaning  himself on me .  I could smell it on my skin, I could smell it in the air, it was everywhere, and it was a constant reminder of what was happening to me )"
    dad_says "Now you can smell like me too Maddie, the whole world would know that you belong to me . Might as well get used to the smell of my dick, because you are gonna be smelling it a lot in the future"
    show madd depressed at left_small
    x "(I am already depressed as it is , stop making it worse by telling me that I am gonna be smelling this disgusting smell a lot in the future )"
    show dad bonamic at right_small
    dad_says "Okay now time to actually rub myself against you "

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_naked_maddie_touches_maddie_rubbing_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small

    x "(He places his dick between my butt cheeks again, but this time he starts rubbing it up and down, the skin contact not leaving my butt cheeks at all)"
    x "(I am being used as a human fleshlight by my own stepdad, this is not how I imagined my life would be at all )"
    x "(He was getting more and more excited, his breathing was getting heavier, and I could feel his dick getting harder and harder , it was leaking precum all over my butt cheeks, the sticky mess was getting all over my skin)"
    x "(His scrotum was slapping against my butt cheeks as he rubbed himself against me  )"
    show madd overwhelmed at left_small
    x "(the whole kitchen was filled with the sound of his dick slapping against my butt cheeks, it was so loud that I was sure that brother would be able to hear it from his room)"
    x "(I was already filthy by having his smegma and precum all over my butt cheeks, but now I was also covered in his sweat too , not to forget his sweaty balls slapping on me as well as the saliva from his tongue on my neck, )"
    show madd resigned at left_small
    x "(All those things made me realize that I was truly marked by him, I was covered in his bodily fluids, I smelled like him, I was his property now, and there was no way to deny that anymore )"
    show dad sadistic at right_small
    dad_says "You like that dont you Maddie ? You like being used by daddy ?"
    show madd helpless at left_small
    x "(I wasnt saying a word but my mouth was now whimpering in response to his movements, I was trying to suppress the sounds but I couldnt help but let out little whimpers )"

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_naked_maddie_touches_maddie_rubbing_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad dominant at right_small

    x "(he started getting more and more aggressive with his rubbing, with his hands placed on my hips, he was pulling me back against him as he rubbed himself against me )"
    show madd broken at left_small
    x "(His dick digging deeper between the crevices of my butt cheeks, the sensation was getting more intense)"
    x "(With more aggressive slapping the sound got louder too, it was a constant reminder of what was happening to me, it was like a soundtrack to my humiliation and degradation by my own stepdad )"
    dad_says "God that feels so good Maddie , everything about you feels so good"
    show dad delusional at right_small
    dad_says "Even when you are pregnant with my baby, we will still have raw filthy sex until the room smells like my dick"
    show madd distressed at left_small
    x "(This just keeps getting worse and worse, his imagination is  so twisted that he is already planning for us to have sex while I am pregnant with his child )"
    x "(I dont wanna end up pregnant with his child, I dont wanna have his baby, I dont wanna be a mother at all, let alone a mother to my stepdad's child )"

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_naked_maddie_touches_maddie_rubbing_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad lecherous at right_small

    x "(Now he placed his dick COMPLTELY between my butt cheeks, he was rubbing it up and down)"
    x "(My buttcheeks were like a condom covering his whole dick he was holding them together with his hands and rubbing himself against me)"
    dad_says "You hear that Maddie ? Its gonna sound so much better when I am actually inside you, but for now just enjoy the feeling of my dick rubbing against your butt cheeks"
    show madd helpless at left_small
    x "(Like hell i am enjoying this, I am being used as a human fleshlight by my own stepdad )"
    x" ( i felt his dick twitching against my butt cheeks, I knew he was getting close to cumming, I just wanted it to be over already )"
    show dad horny at right_small
    dad_says "Ah...I am gonna cum Maddie, I am gonna cum all over your butt cheeks, you are gonna be covered in my cum, you are gonna be a mess for daddy"

    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_naked_maddie_touches_maddie_cumming_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd traumatized at left_small

    x "(I felt his dick twitching against my butt cheeks as he started shooting his load, his cum was shooting out of the tip of his penis and landing all over my butt cheeks, it was a sticky mess)"
    x "(it was flying everywhere, some of it was landing on the floor, some of it landed on my hips and some of it landed on his thighs too )"
    show dad sadistic at right_small
    dad_says "AAAhhh...this feels so good Maddie"
    show madd self loathing at left_small
    x "(He was shouting this so loudly as if he was doing it on purpose to humiliate me even more, maybe his intention was to make sure that brother could hear him )"
    x "(Maybe he wanted him to know that i belong to him, that i am his property, that i will be his future baby mama )"
    x "(He kept humping himself against me as he was cumming)"
    x "(Meanwhile with his hands he was spreading his cum that was on my cheeks)"
    show dad possessive at right_small
    dad_says "You look good covered in my cum Maddie"
    show madd feels violated at left_small
    x "(he says that as he continues to spread his cum all over my butt cheeks, he was making sure that every inch of my skin was covered in his cum )"
    x "(He kept cumming and spreading it on me for what felt like an eternity, until finally he was completely spent and his dick was softening against my skin )"
    x "(He finally pulled back away from me and stood there for a moment, catching his breath, and looking down at me with a satisfied expression on his face )"
    dad_says "Ah i am spent, its been a while since i had such a good release, you really know how to please daddy Maddie"
    show madd broken at left_small
    x "(what the hell was this volume of cum ? I am pretty sure he just emptied his entire testicles on me)"
    x "(I dont know the science behind conception of twins i always thought it was based on volume of cum according to that  if this load was done inside me i would end up pregnant with twins for sure)"
    show dad authoritative at right_small
    dad_says "Go on maddie, put on your shorts "
    show madd hesitant at left_small
    x "huh...But i am still covered in your cum, I need to clean myself up first"
    show dad cruel at right_small
    dad_says "I SAID PUT ON YOUR SHORTS, NOW"
    show madd shaken at left_small
    x "(There was anger in his voice, he was not used to being disobeyed, and now that I was covered in his cum, he wanted me to put my shorts back on immediately so that I would be able to hide the evidence of what just happened to me )"
    
    scene scene_kitchen_minigame_madd_dad_standing_licks_neck_naked_maddie_touches_maddie_cumming_shorts_back_on
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small

    x "(AS i pulled my shorts back up , i felt the sticky mess of his cum on my skin, the fabric of my shorts was getting soaked with his cum)"
    x "(It was also serving as a container for his cum, it was trapping it against my skin, and I could feel the warmth of his cum trapped in my shorts )"
    show dad mocking at right_small
    dad_says "Ah...there you go Maddie , now you look like a painting covered in my cum, you are such a good canvas for daddy"
    show madd self loathing at left_small
    x "(Everytime he opened his mouth to say something, it was like he was adding another arrow to the target on my back)"
    x "(The trapped cum in my shorts was getting all over my skin UGH i just want to wash it off)"
    dad_says "That's all for now Maddie, lets just mate like animals "
    show madd distressed at left_small
    x "(ABsolutely not, I am not gonna have sex with you like an animal)"
    show madd traumatized at left_small
    x "(As he said that i heard footsteps moving away from the kitchen, dad was finally leaving me alone, but i knew this was not the end of it, this was just the beginning of a long nightmare that I would have to endure with him )"

    $ character_relations["dad"]["intimacy"]+=7 
    $ character_relations["dad"]["lust"] = 0 
    $ character_relations["dad"]["anger"] = 0 
    $ character_relations["dad"]["dominance"] += 15
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["kissed"] += 1
    $ character_relations["dad"]["came_on_madd"] += 1
    $ character_relations["dad"]["oral_sex"] += 1
    $ journal_event_show("Dad", "Sofa Sleep")
    $ journal_event_set_done("Dad", "Kitchen Ambush (Miss Event)")
    hide madd
    hide dad
    with dissolve
    $ madd_willpower=max(0,madd_willpower-20)
    call advance_time_and_check(minutes=120) 
    
    jump cooking_complete


#Clean his room for some money

label clean_dad_room:
    scene scene_madd_dad_talk_before_maid_event
    if dad_maid_event == False :
        $ dad_maid_event = True
        call dad_room_cleaning_event_first_time from _call_dad_room_cleaning_event_first_time
    else:
        x "(Dad is in his room, probably watching TV as usual.)"
        show madd determined at left_small
        with dissolve
        x "Hey ,I am here to clean the room "
        show madd hopeful at left_small
        with dissolve

        if character_relations["dad"]["intimacy"]>=70 and character_relations["dad"]["lust"]>=70:
            $ newrand = renpy.random.random()
            if newrand < 0.8:
                jump dad_room_cleaning_even_clean_final_domination

        if (character_relations["dad"]["vaginal_sex"] + character_relations["dad"]["anal_sex"] + character_relations["dad"]["oral_sex"]>=1 ) or character_relations["dad"]["intimacy"]>=30 :
            $newrand= renpy.random.random()
            if newrand < 0.45:
                jump dad_room_cleaning_event_clean_feet 
                jump dad_clean_event_getting_paid
            elif newrand <0.9:
                jump dad_room_cleaning_event_clean_armpit
                jump dad_clean_event_getting_paid
    

        
        if character_relations["dad"]["lust"] >=20:
            $ random_event = renpy.random.random()
            if random_event < 0.6:
                jump dad_room_cleaning_event_second_time
            else:
                jump dad_room_cleaning_event_second_time_clothes
        else:
            $ random_event = renpy.random.random()
            if random_event <= 0.8:
                jump dad_room_cleaning_event_nothing_happens
            elif random_event <= 0.95:
                jump dad_room_cleaning_event_second_time
            else:
                jump dad_room_cleaning_event_second_time_clothes

        label dad_clean_event_getting_paid:
        scene scene_dad_room_cleaning_event_second_time_dusting_vaccum_aftermath
        with fade
        show madd relieved at left_small
        with dissolve
        x "(He then paid me for my services )"
        x "( As i left the room )"
        $madd_money+=100

    jump home_areas


label dad_room_cleaning_event_first_time:
    scene scene_madd_dad_talk_before_maid_event
    with dissolve
    show madd nervous at left_small
    with dissolve
    
    x "(I take a deep breath before approaching him. He's sitting in his room, reading the newspaper like he always does.)"
    show madd hesitant at left_small
    with dissolve
    x "(This is it. I need to ask him for money. I've been saving up what little I can, but it's not enough.)"
    show madd determined at left_small
    with dissolve
    
    x "Dad? Can I talk to you for a minute?"
    show madd nervous at left_small
    with dissolve
    
    dad_says "What is it?"
    show dad mocking at right_small
    with dissolve
    dad_thinks "(She rarely approaches me voluntarily. This should be interesting.)"
    show dad possessive at right_small
    with dissolve
    
    x "(I gather my courage, trying to sound confident even though my heart is racing.)"
    show madd determined at left_small
    with dissolve
    
    x "I was wondering... I need some money. For things I need. And I thought... maybe I could earn it?"
    show madd hopeful at left_small
    with dissolve
    
    dad_says "Money?"
    show dad calculating at right_small
    with dissolve
    dad_thinks "(Money. She's finally realizing that nothing in life is free. That she needs to work for what she wants.)"
    show dad mocking at right_small
    with dissolve
    
    x "Yes, I could help around the house. More than I do now, I mean. I could... I could clean your room. Dust, organize, fold your clothes, keep everything tidy.)"
    show madd hopeful at left_small
    with dissolve
    x "(I'm holding my breath, waiting for his response.)"
    show madd nervous at left_small
    with dissolve
    
    dad_says "You want to clean my room?"
    show dad smirk at right_small
    with dissolve
    dad_thinks "(Her mother used to do the same thing. Offering herself in service to me. How delightful that the apple doesn't fall far from the tree.)"
    show dad lecherous at right_small
    with dissolve
    dad_thinks "(And now her daughter is volunteering to do the same. Perhaps genetics play a more important role than I thought.)"
    show dad possessive at right_small
    with dissolve
    scene scene_madd_dad_talk_first_maid_event_predatory_eyes
    dad_says "And tell me... why exactly do you need this money so suddenly?"
    show dad calculating at right_small
    with dissolve
    dad_thinks "(Is she planning something? An escape perhaps? Or maybe she has a boy she's trying to impress?)"
    show dad controlling at right_small
    with dissolve
    
    x "(I hesitate. I can't tell him the truth about needing money for escape supplies. He'll never allow me to leave.)"
    show madd conflicted at left_small
    with dissolve
    x "There's... there's a new gaming console that came out. The Switch 2. I've been wanting it for a while and...)"
    show madd hesitant at left_small
    with dissolve
    x "(It sounds so trivial when I say it out loud, especially now.)"
    show madd distressed at left_small
    with dissolve
    
    dad_says "A gaming console?"
    show dad mocking at right_small
    with dissolve
    dad_thinks "(Of course. She wants material things. She's a woman after all, always wanting, always needing.)"
    show dad mocking at right_small
    with dissolve
    
    dad_says "Do you have any idea how hard I work to keep a roof over your head? How ungrateful you sound right now?"
    show dad angry at right_small
    with dissolve
    dad_thinks "(She lives here rent-free. She eats my food, uses my electricity, sleeps in my house. And she has the audacity to ask me for more.)"
    show dad mocking at right_small
    with dissolve
    
    x "(His words sting. He's right, in a way. I am ungrateful. But I also know there's something darker beneath his anger.)"
    show madd distressed at left_small
    with dissolve
    x "(He's calculating something. I can see it in his eyes. Like a predator circling prey.)"
    show madd feels violated  at left_small
    with dissolve
    
    x "I know, Dad. I'm sorry. I just... I thought maybe if I helped more, it wouldn't be too much to ask..."
    show madd hesitant at left_small
    with dissolve
    
    dad_says "Helped more?"
    show dad calculating at right_small
    with dissolve
    dad_thinks "(She's offering herself to me. Whether she knows it or not.)"
    show dad predatory at right_small
    with dissolve
    dad_thinks "(And I can mold this situation exactly the way I want it.)"
    show dad manipulative at right_small
    with dissolve
    
    dad_says "Well, I suppose that's... reasonable. But if you want to work for money in this house, you need to understand something."
    show dad angry at right_small
    with dissolve
    dad_thinks "(She needs to understand her place. She needs to learn that nothing comes free. That everything comes with a price.)"
    show dad calculating at right_small
    with dissolve
    
    dad_says "Your mother used to do the same thing. Offer to help, offer to clean, offer to take care of things."
    show dad wistful at right_small
    with dissolve
    dad_thinks "(Memories of her. The way she used to move. The way she would look at me when she realized what her offer truly meant.)"
    show dad yearning at right_small
    with dissolve
    
    x "(Something in his tone changes. It becomes almost... nostalgic. And that scares me more than anger ever could.)"
    show madd feels violated  at left_small
    with dissolve
    x "(I've learned to recognize that tone. It means he's thinking about her. About my mother.)"
    show madd shaken at left_small
    with dissolve
    x "(And when he thinks about her, bad things usually happen.)"
    show madd trembling at left_small
    with dissolve
    
    x "Dad, I... I just want to help. I want to earn the money..."
    show madd nervous at left_small
    with dissolve
    
    dad_says "Of course you do. And that's... commendable."
    show dad manipulative at right_small
    with dissolve
    dad_says "So here's what we're going to do. You will take on all the responsibilities that your mother once had in this household."
    show dad dominant at right_small
    with dissolve
    dad_thinks "(Making her understand that she's replacing her mother. That she's stepping into that role. It's poetic in a way.)"
    show dad possessive at right_small
    with dissolve
    
    dad_says "You'll clean my room daily. You'll make sure everything is exactly how I want it. Every detail matters."
    show dad controlling at right_small
    with dissolve
    
    x "(Daily? The way he emphasizes it sends chills down my spine.)"
    show madd paralyzed at left_small
    with dissolve
    x "(What does 'everything exactly how I want it' really mean? There's a subtext here that I can feel but don't fully understand. And that's what frightens me most.)"
    show madd conflicted at left_small
    with dissolve
    
    dad_says "And your payment will be one hundred dollars per day for your work."
    show dad mocking at right_small
    with dissolve
    dad_thinks "(One hundred dollars a day. Enough to make her think she's getting a fair deal. Enough to keep her coming back. Enough to establish this dynamic permanently.)"
    show dad obsessed at right_small
    with dissolve
    
    x "(One hundred dollars a day? That's... actually quite generous. But why does it feel like a trap?)"
    show madd hesitant at left_small
    with dissolve
    x "(Because it is a trap, a voice inside me whispers. Nothing from him comes without a price. Nothing.)"
    show madd feels violated  at left_small
    with dissolve
    
    x "That's... that's really generous, Dad. Thank you."
    show madd hopeful at left_small
    with dissolve
    x "(I'm trying to sound grateful, but my voice doesn't quite cooperate.)"
    show madd nervous at left_small
    with dissolve
    
    dad_says "Of course. You're my daughter after all."
    show dad possessive at right_small
    with dissolve
    dad_thinks "(My daughter. My property. My responsibility. My right.)"
    show dad lecherous at right_small
    with dissolve
    
    x "(He's looking at me now in that way again. The way that makes my skin crawl.)"
    show madd horrified at left_small
    with dissolve
    x "(Like he's seeing something in me that isn't there. Or maybe seeing something that he put there himself.)"
    show madd conflicted at left_small
    with dissolve
    
    x "I... I understand, Dad. I'll do a good job. I promise."
    show madd determined at left_small
    with dissolve
    
    dad_says "I'm sure you will. You have so much of your mother in you, after all."
    show dad yearning at right_small
    with dissolve
    dad_thinks "(Yes. She does. In so many ways. And soon she'll understand what that means. Soon she'll take her proper place.)"
    show dad possessive at right_small
    with dissolve
    
    x "(And there it is again. The comparison to my mother. The weight of expectations I don't fully understand.)"
    show madd shaken at left_small
    with dissolve
    x "(I know from the tone in his voice that this is more than just cleaning. This is something else entirely. Something darker.)"
    show madd feels violated  at left_small
    with dissolve
    x "(But I need that money. I need it for my escape. So I have to accept this arrangement, whatever it truly means.)"
    show madd resigned at left_small
    with dissolve
    x "(I have to play along.)"
    show madd paralyzed at left_small
    with dissolve

    $ character_relations["dad"]["intimacy"]+=3
    $ madd_willpower=max(0,madd_willpower-20)
    $ journal_event_set_done("Dad", "Room Cleaning Deal")
    $ journal_event_show("Dad", "Room Cleaning: Dusting & Groping")
    $ journal_event_show("Dad", "Room Cleaning: Folding Clothes")
    $ journal_event_show("Dad", "Room Cleaning: Foot Cleaning")
    $ journal_event_show("Dad", "Room Cleaning: Armpit")
    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_40

    
    jump home_areas


label dad_room_cleaning_event_second_time:
    scene scene_madd_dad_talk_before_maid_event
    with dissolve
    show madd nervous at left_small
    with dissolve
    
    dad_says "Today you will dust the place. Make sure everything is spotless. I want to see my reflection in every surface."
    show dad dominant at right_small
    with dissolve
    dad_thinks "(Dust. A perfect excuse to have her bend down, to position her body in vulnerable ways.)"
    show dad calculating at right_small
    with dissolve
    dad_thinks "(She's learning to obey without question. Perfect. Soon she won't even hesitate.)"
    show dad possessive at right_small
    with dissolve
    
    x "(I nod, trying to keep my expression neutral, though my heart is already racing.)"
    show madd hesitant at left_small
    with dissolve
    x "(This is dangerous. Being alone with him in his room, doing this kind of work...)"
    show madd anxious at left_small
    with dissolve
    
    x "Yes, Dad. I'll make sure everything is perfect."
    show madd determined at left_small
    with dissolve
    x "(I go to fetch the vacuum cleaner and dust pad from the hallway closet, my hands trembling slightly.)"
    show madd nervous at left_small
    with dissolve
    
    dad_thinks "(She's afraid. Good. Fear makes them compliant. Fear makes them... responsive.)"
    show dad lustful at right_small
    with dissolve
    scene scene_dad_room_cleaning_event_second_time_dusting_vaccum
    with fade    
    x "(I start dusting the shelves, the desk, anywhere that doesn't require me to get too close to him. He watches me the entire time, and I can feel his eyes on me like physical weight.)"
    show madd processing at left_small
    with dissolve
    x "(Every surface I touch feels like it takes an eternity. My movements are slow, deliberate... almost like I'm stalling.)"
    show madd trembling at left_small
    with dissolve
    
    dad_thinks "(The way she moves. So careful. So aware of me. She knows what's coming. On some level, she's anticipating it.)"
    show dad fixated at right_small
    with dissolve
    dad_thinks "(That's the beautiful part about breaking someone down slowly. They start to expect the violation. To prepare for it.)"
    show dad sadistic at right_small
    with dissolve
    
    x "(I work methodically, moving from one corner of the room to the other, but all the while, I'm acutely aware that there's one place left: under the bed.)"
    show madd horrified at left_small
    with dissolve
    x "(That dark, confined space where I'll have to bend forward, where my body will be completely exposed to him.)"
    show madd shaken at left_small
    with dissolve
    x "(He's sitting very close to the edge of the bed. I can feel it. I know exactly what's going to happen, and there's nothing I can do to stop it.)"
    show madd paralyzed at left_small
    with dissolve
    
    dad_thinks "(Almost there. Just a little longer and she'll be exactly where I need her. Bent down, vulnerable, with no way to escape.)"
    show dad hungry at right_small
    with dissolve
    dad_thinks "(She's probably already thinking about what I'm going to do. The fear is exquisite.)"
    show dad obsessed at right_small
    with dissolve
    
    x "(I finish the rest of the room as slowly as I can manage, but eventually, there's nowhere left to clean but under the bed.)"
    show madd conflicted at left_small
    with dissolve
    x "(I take a deep breath, trying to steady my nerves.)"
    show madd nervous at left_small
    with dissolve
    
    x "I... I need to dust under the bed now."
    show madd hesitant at left_small
    with dissolve
    x "(My voice comes out smaller than I intended.)"
    show madd feels violated  at left_small
    with dissolve
    
    dad_says "Of course. Don't leave any corners untouched. That's where the dust accumulates."
    show dad manipulative at right_small
    with dissolve
    dad_thinks "(She knows. She absolutely knows what's about to happen.)"
    show dad lecherous at right_small
    with dissolve
    dad_thinks "(And she's going to do it anyway because she needs this money. Because she has nowhere else to go.)"
    show dad cruel at right_small
    with dissolve
    
    scene scene_dad_room_cleaning_event_second_time_madd_kneels_under_bed
    with fade

    x "(I gather my courage as I lower myself to my knees, dust pad in hand.)"
    show madd determined at left_small
    with dissolve
    x "(I have to do this. I need the money. I need to get out of here.)"
    show madd determined at left_small
    with dissolve
    x "(Those two thoughts keep me moving forward, even as every instinct in my body screams at me to run.)"
    show madd trembling at left_small
    with dissolve
    
    dad_thinks "(Perfect. There she is. On her knees. Exposed. Defenseless.)"
    show dad predatory at right_small
    with dissolve
    dad_thinks "(Now is the moment. When she's at her most vulnerable, when she can't run or fight back.)"
    show dad dominant at right_small
    with dissolve
    dad_thinks "(I'm going to touch her. Mark her. Slowly, steadily, with each day, I'm going to push further and further into her boundaries.)"
    show dad possessive at right_small
    with dissolve
    
    x "(I bend forward to get under the bed, the dust pad extended in front of me.)"
    show madd paralyzed at left_small
    with dissolve
    x "(My heart is pounding in my chest so hard I think he can hear it.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(My exposed position is exactly what he wants. My ass is raised, my back arched, completely at his mercy.)"
    show madd hesitant at left_small
    with dissolve
    
    dad_thinks "(God, look at her. The curve of her body. The way her clothes stretch across her.)"
    show dad lustful at right_small
    with dissolve
    dad_thinks "(Just like her mother. That same body, that same shape.)"
    show dad yearning at right_small
    with dissolve
    
    x "(I'm reaching under the bed with the dust pad, trying to focus on the task and not on the fact that I can feel him shifting on the mattress above me.)"
    show madd anxious at left_small
    with dissolve
    x "(He's moving. Getting closer. Or maybe he's just getting more comfortable.)"
    show madd feels violated  at left_small
    with dissolve
    
    scene scene_dad_room_cleaning_event_second_time_dust_under_bed_dad_grope_ass
    with dissolve
    
    x "(And then...)"
    show madd shocked at left_small
    with dissolve
    x "(I feel it.)"
    show madd horrified at left_small
    with dissolve
    x "(A hand on my ass.)"
    show madd paralyzed at left_small
    with dissolve
    
    dad_thinks "(There. The touch. The beginning of what I'm going to make her endure.)"
    show dad obsessed at right_small
    with dissolve
    dad_thinks "(She's frozen. Perfect. That shock, that moment of realization that there's no escape...)"
    show dad sadistic at right_small
    with dissolve
    
    x "(The shock of it hits me like a physical blow. I stop moving completely, my breath catching in my throat.)"
    show madd paralyzed at left_small
    with dissolve
    x "(His hand is warm, and it's pressing firmly against my buttocks, feeling the shape of me through my clothes.)"
    show madd distressed at left_small
    with dissolve
    x "(This is it. This is the moment I've been dreading.)"
    show madd overwhelmed at left_small
    with dissolve
    
    x "(I can't dust. I can't move. All I can do is feel the weight of his hand on my body, the possession implicit in that touch.)"
    show madd violated at left_small
    with dissolve
    
    dad_says "Don't stop working."
    show dad dominant at right_small
    with dissolve
    dad_thinks "(Let her know that what's happening doesn't change what she needs to do. She's mine to use.)"
    show dad controlling at right_small
    with dissolve
    
    dad_thinks "(God, her curves are the best. I could keep touching them all day. Every inch of her body is perfect. She's perfect.)"
    show dad lecherous at right_small
    with dissolve
    dad_thinks "(Just like her mother was. That same smoothness. That same softness.)"
    show dad yearning at right_small
    with dissolve
    
    x "(I force myself to move again, pulling the dust pad further under the bed, but my movements are mechanical now, without any real purpose.)"
    show madd processing at left_small
    with dissolve
    x "(His hand is exploring me more and more, feeling the contours of my buttocks through the fabric of my clothes.)"
    show madd trembling at left_small
    with dissolve
    
    dad_thinks "(I can sense that she's stopped moving. She's paralyzed by my touch. That's good. The longer she stays here, the longer I have to mold her, to shape her into what I need.)"
    show dad fixated at right_small
    with dissolve
    dad_thinks "(Soon she won't even flinch. Soon she'll accept this as part of the job.)"
    show dad manipulative at right_small
    with dissolve
    
    x "(A short squeeze on my left cheek. Then on my right. His touches are deliberate, almost like he's weighing me, measuring me, claiming me.)"
    show madd shaken at left_small
    with dissolve
    x "(The pressure is firm but not painful. It's almost... familiar. Like he's done this before.)"
    show madd conflicted at left_small
    with dissolve
    x "(And then...)"
    show madd shocked at left_small
    with dissolve
    
    scene scene_dad_room_cleaning_event_second_time_under_bed_spank
    with dissolve
    
    x "(I suddenly feel a sharp, stinging sensation across my buttocks.)"
    show madd horrified at left_small
    with dissolve
    x "(He slapped me.)"
    show madd trembling at left_small
    with dissolve
    x "(The sound is loud, echoing through the room—loud enough that I'm sure someone could hear it if they were nearby.)"
    show madd overwhelmed at left_small
    with dissolve
    
    dad_says "That sounded perfect. Just like her mother."
    show dad yearning at right_small
    with dissolve
    dad_thinks "(Yes. The sound of her slap. The curve of her buttocks. Everything about this moment is perfect.)"
    show dad obsessed at right_small
    with dissolve
    dad_thinks "(She's becoming what I need her to be.)"
    show dad possessive at right_small
    with dissolve
    
    x "(I gather what's left of my composure and quickly finish dusting under the bed, my hands shaking.)"
    show madd nervous at left_small
    with dissolve
    x "(I want to cry. I want to scream. But instead, I just finish the job and quickly pull myself out from under there.)"
    show madd weeping at left_small
    with dissolve
    
    x "(I hurry out from under the bed, my face flushed, my body still tingling from his touch.)"
    show madd shaken at left_small
    with dissolve
    x "(I stand up, trying to avoid looking at him directly.)"
    show madd hesitant at left_small
    with dissolve
    
    scene scene_dad_room_cleaning_event_second_time_dusting_vaccum_aftermath
    with dissolve
    
    dad_thinks "(Look at her. Flushed. Shaking slightly. The fear and shame mixed together on her face.)"
    show dad fixated at right_small
    with dissolve
    dad_thinks "(She's responding. Maybe not consciously, but her body is learning.)"
    show dad possessive at right_small
    with dissolve
    
    dad_says "Good work. Your dusting was thorough."
    show dad mocking at right_small
    with dissolve
    dad_thinks "(Let her think this is about the work. Let her believe that if she just does her job well enough, maybe it will stop.)"
    show dad manipulative at right_small
    with dissolve
    dad_thinks "(It won't.)"
    show dad sadistic at right_small
    with dissolve
    
    x "(He just stares at me, and I can't meet his eyes.)"
    show madd feels violated  at left_small
    with dissolve
    x "(He doesn't say anything else, but I know his actions are slowly having an impact on me.)"
    show madd conflicted at left_small
    with dissolve
    x "(I'm becoming numb to it. Or maybe I'm becoming something else entirely.)"
    show madd processing at left_small
    with dissolve
    x "(I'm not sure which is worse.)"
    show madd overwhelmed at left_small
    with dissolve
    
    dad_thinks "(Tomorrow, I'll push a little further. And the day after that, a little further still.)"
    show dad possessive at right_small
    with dissolve
    dad_thinks "(Until there's no part of her that doesn't belong to me.)"
    show dad obsessed at right_small
    with dissolve
    
    $ character_relations["dad"]["intimacy"]+=3
    $ character_relations["dad"]["anger"]=max(0,character_relations["dad"]["anger"]-5)
    $ character_relations["dad"]["lust"]=max(0,character_relations["dad"]["lust"]-20)
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ madd_willpower=max(0,madd_willpower-20)
    $ journal_event_set_done("Dad", "Room Cleaning: Dusting & Groping")
    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_41

    jump dad_clean_event_getting_paid


label dad_room_cleaning_event_second_time_clothes:
    scene scene_madd_dad_talk_before_maid_event
    with dissolve
    show madd nervous at left_small
    with dissolve
    
    dad_says "Today, you will fold my clothes. And I want them done properly."
    show dad dominant at right_small
    with dissolve
    dad_thinks "(This is the next step. The slow escalation. Each task more intimate than the last.)"
    show dad calculating at right_small
    with dissolve
    dad_thinks "(She'll soon understand that even something as mundane as laundry is an opportunity for me to mark her.)"
    show dad possessive at right_small
    with dissolve
    
    x "(I nod, trying to keep my expression neutral, though my heart is already racing.)"
    show madd hesitant at left_small
    with dissolve
    x "(Folding clothes. That's simple enough. Maybe today will be different.)"
    show madd hopeful at left_small
    with dissolve
    x "(But something in his tone tells me this isn't just about clothes.)"
    show madd nervous at left_small
    with dissolve
    
    scene scene_dad_room_cleaning_second_time_clothes_start
    with dissolve
    
    x "(He stands up and retrieves a large pile of clothes from his closet.)"
    show madd processing at left_small
    with dissolve
    x "(He hands them to me with deliberate slowness, and I take them, my hands already trembling slightly.)"
    show madd trembling at left_small
    with dissolve
    
    dad_thinks "(Look at her hands. Already shaking. She knows what's coming. Good.)"
    show dad fixated at right_small
    with dissolve
    
    x "(As I look through the pile, my stomach drops. Mixed in with his regular clothes are his socks and underwear.)"
    show madd horrified at left_small
    with dissolve
    x "(His intimate garments. The pieces that have been in direct contact with his body.)"
    show madd shaken at left_small
    with dissolve
    x "(He wanted me to handle these. To fold them. To... what?)"
    show madd conflicted at left_small
    with dissolve
    
    dad_says "Fold most of the clothes properly. But for the socks and underwear, you need to verify if they're suitable to be worn again."
    show dad manipulative at right_small
    with dissolve
    dad_thinks "(Now we're getting to the good part. The intimacy. The degradation.)"
    show dad lecherous at right_small
    with dissolve
    
    dad_says "I haven't washed them yet. So you'll need to check them for me."
    show dad controlling at right_small
    with dissolve
    dad_thinks "(This is perfect. Forcing her to interact with my unwashed body through my clothes.)"
    show dad sadistic at right_small
    with dissolve
    dad_thinks "(Every whiff of my scent is another mark of ownership.)"
    show dad obsessed at right_small
    with dissolve
    
    x "(My face flushes. Check them? How exactly am I supposed to do that?)"
    show madd distressed at left_small
    with dissolve
    x "(I already know the answer. I just don't want to acknowledge it.)"
    show madd feels violated  at left_small
    with dissolve
    
    x "Um... how would you want me to check that?"
    show madd hesitant at left_small
    with dissolve
    x "(I hate how small my voice sounds.)"
    show madd hesitant at left_small
    with dissolve
    
    dad_says "Isn't it obvious? You smell them."
    show dad dominant at right_small
    with dissolve
    dad_thinks "(Direct. No ambiguity. No room for misunderstanding.)"
    show dad dominant at right_small
    with dissolve
    
    x "(There it is. The confirmation of what I already suspected.)"
    show madd horrified at left_small
    with dissolve
    x "(I knew it. I knew somehow even this would be used by him to degrade me further.)"
    show madd self loathing at left_small
    with dissolve
    
    x "(I nod, not giving him the satisfaction of seeing me break. I want to appear resolute, even though inside I'm falling apart.)"
    show madd determined at left_small
    with dissolve
    x "(I want him to think I'm stronger than I am. That I'm not already falling into this.)"
    show madd resigned at left_small
    with dissolve
    
    dad_thinks "(She's trying to maintain control. That's fine. I'll break that too, eventually.)"
    show dad manipulative at right_small
    with dissolve
    dad_thinks "(One sniff at a time.)"
    show dad obsessed at right_small
    with dissolve
    
    scene scene_dad_room_cleaning_second_time_clothes_folding
    with dissolve
    x "(I start with folding the regular clothes first, leaving the worst part for last.)"
    show madd focused at left_small
    with dissolve
    x "(Shirts. Pants. Jackets. Each fold is precise, mechanical. A barrier between me and what's coming.)"
    show madd processing at left_small
    with dissolve
    x "(My hands move automatically, but my mind is elsewhere—dreading the moment when I have to face his intimate garments.)"
    show madd anxious at left_small
    with dissolve
    
    dad_thinks "(She's stalling. Smart girl. But it won't help her.)"
    show dad calculating at right_small
    with dissolve
    dad_thinks "(The anticipation is part of the punishment.)"
    show dad sadistic at right_small
    with dissolve
    
    x "(After what feels like far too short a time, I've finished with the regular clothes.)"
    show madd nervous at left_small
    with dissolve
    x "(All that remains are the intimate parts—the socks and the underwear.)"
    show madd trembling at left_small
    with dissolve
    

    
    x "(Throughout this entire time, he's been watching TV, seemingly minding his own business.)"
    show madd processing at left_small
    with dissolve
    x "(But the moment my hands reach for the first sock, his gaze shifts to me with an intensity that makes my breath catch.)"
    show madd shocked at left_small
    with dissolve
    x "(He's been waiting for this. Anticipating it.)"
    show madd horrified at left_small
    with dissolve
    
    dad_thinks "(She's finally there. About to touch my unwashed socks. To bring them to her face.)"
    show dad fixated at right_small
    with dissolve
    dad_thinks "(This is intimate in a way she doesn't fully understand yet.)"
    show dad hungry at right_small
    with dissolve
    
    dad_says "Now, do it properly. If I'm wearing bad socks or underwear, it would be problematic."
    show dad dominant at right_small
    with dissolve
    dad_thinks "(Problematic. As if I care about cleanliness. This is about her accepting my scent as part of her reality.)"
    show dad possessive at right_small
    with dissolve
    
    x "(Problematic to whom? You barely leave the house.)"
    show madd angry at left_small
    with dissolve
    x "(But I catch myself, biting back my sarcasm.)"
    show madd feels violated  at left_small
    with dissolve
    
    x "Y-yes."
    show madd hesitant at left_small
    with dissolve
    x "(That single syllable takes all my courage.)"
    show madd trembling at left_small
    with dissolve
    dad_thinks "(Good. She's compliant. For now.)"
    show dad smirk at right_small
    with dissolve

    scene scene_dad_room_cleaning_second_time_clothes_socks_sniff
    with dissolve 

    x "(I pick up the first sock, holding it between my thumb and forefinger as if it might bite me.)"
    show madd disgusted at left_small
    with dissolve
    x "(The moment I touch it, I'm immediately aware of its weight, its texture, and most of all, its smell.)"
    show madd nauseated at left_small
    with dissolve
    x "(The sock is clearly well-worn—stains visible along the heel and the toe area.)"
    show madd horrified at left_small
    with dissolve
    
    dad_thinks "(She's holding it like it's infected. That repulsion... it's exquisite.)"
    show dad lecherous at right_small
    with dissolve
    dad_thinks "(She's disgusted by me, and yet she's still here. Still holding my sock.)"
    show dad sadistic at right_small
    with dissolve
    
    x "(I bring it closer to my nose, hesitantly, and take a whiff.)"
    show madd conflicted at left_small
    with dissolve
    x "(The smell hits me like a wall—pungent, acrid, a mixture of sweat, salt, and something else I can't quite identify.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(My stomach turns. This is disgusting. This is degrading.)"
    show madd self loathing at left_small
    with dissolve
    x "(But I need the money. I always need the money.)"
    show madd resigned at left_small
    with dissolve
    
    x "(I put the sock aside, marking it as not good for wearing, trying to move on as quickly as possible.)"
    show madd processing at left_small
    with dissolve
    
    dad_says "Hey, stop. This is not how you check socks."
    show dad angry at right_small
    with dissolve
    dad_thinks "(She's trying to do the bare minimum. Not acceptable.)"
    show dad controlling at right_small
    with dissolve
    
    x "(My heart sinks. There's more to this.)"
    show madd horrified at left_small
    with dissolve
    
    dad_says "You open the sock up and put your nose inside to get a proper sense of whether it's worthy of being worn."
    show dad dominant at right_small
    with dissolve
    dad_thinks "(Let her understand the depths of this. Let her put her face inside my dirty sock.)"
    show dad dominant at right_small
    with dissolve
    dad_thinks "(This is psychological conditioning. Each act of degradation brings her further under my control.)"
    show dad obsessed at right_small
    with dissolve
    
    x "(I see anger in his eyes—but also dominance. A dominance that makes it clear this is non-negotiable.)"
    show madd paralyzed at left_small
    with dissolve
    x "(This is about establishing power. About making it clear that I have to obey.)"
    show madd overwhelmed at left_small
    with dissolve
    scene scene_dad_room_cleaning_second_time_clothes_socks_sniff_open_sock
    with dissolve
    x "(I pick the sock up again, my hands now visibly shaking.)"
    show madd trembling at left_small
    with dissolve
    x "(I open it carefully, spreading the opening as wide as I can.)"
    show madd distressed at left_small
    with dissolve
    x "(I hesitate for a moment, but his stare is unrelenting, so I bring my nose to the opening and inhale.)"
    show madd horrified at left_small
    with dissolve
    
    dad_thinks "(There. Her nose inside my sock. This image... I'll remember this forever.)"
    show dad fixated at right_small
    with dissolve
    dad_thinks "(She's a pet now. My pet. Learning to recognize my scent.)"
    show dad possessive at right_small
    with dissolve
    
    x "(The smell is overwhelming. It's not just sweat anymore—it's layers of sweat, dead skin cells, bacteria, and something acrid that makes my eyes water.)"
    show madd nauseated at left_small
    with dissolve
    x "(I gag. I actually gag, my body's natural response to the assault on my senses.)"
    show madd violated at left_small
    with dissolve
    
    dad_says "Yes, take a good whiff."
    show dad lecherous at right_small
    with dissolve
    dad_thinks "(She's gagging. Beautiful. That's the sound of her resistance breaking down.)"
    show dad sadistic at right_small
    with dissolve
    
    x "(I try to pull away, but he's still watching, waiting, expecting me to hold it longer.)"
    show madd feels violated  at left_small
    with dissolve
    x "(So I stay there, my nose in his sock, breathing in his scent for two long seconds that feel like an eternity.)"
    show madd paralyzed at left_small
    with dissolve
    x "(The smell seeps into my sinuses, coating the inside of my nose, impossible to ignore or forget.)"
    show madd overwhelmed at left_small
    with dissolve
    
    x "(Finally, I pull away, my face flushed with shame.)"
    show madd distressed at left_small
    with dissolve
    x "(I put the sock aside and immediately move to the next one.)"
    show madd resigned at left_small
    with dissolve
    
    x "(I do this seven more times. Seven more socks. Seven more assaults on my sense of smell.)"
    show madd processing at left_small
    with dissolve
    x "(Each one slightly different, but all distinctly repulsive. Each one a small death of dignity.)"
    show madd distressed at left_small
    with dissolve
    x "(By the time I'm finished with the socks, my nose feels numb, my mind feels foggy, and something inside me has shifted.)"
    show madd confused at left_small
    with dissolve
    
    dad_thinks "(Eight socks. Eight times she's degraded herself for money.)"
    show dad obsessed at right_small
    with dissolve
    dad_thinks "(Soon she won't even resist. Soon she'll do this willingly.)"
    show dad manipulative at right_small
    with dissolve
    

    
    x "(And then comes the worst. His underwear.)"
    show madd horrified at left_small
    with dissolve
    x "(I can feel a shift in the atmosphere. The air itself seems to thicken.)"
    show madd trembling at left_small
    with dissolve
    x "(When I reach for the first pair, I see him look at me with an intensity that's almost feral.)"
    show madd shocked at left_small
    with dissolve
    x "(This is the moment he's been waiting for. This is the most important part.)"
    show madd overwhelmed at left_small
    with dissolve
    
    dad_thinks "(Finally. Her face is about to be in my underwear.)"
    show dad fixated at right_small
    with dissolve
    dad_thinks "(The most intimate piece of clothing. The piece that touches my skin most directly.)"
    show dad hungry at right_small
    with dissolve
    dad_thinks "(She'll smell my sex. She'll smell my musk. She'll smell what I am.)"
    show dad dominant at right_small
    with dissolve
    dad_thinks "(And she'll do it because she has no choice.)"
    show dad sadistic at right_small
    with dissolve
    scene dad_room_cleaning_event_second_time_clothes_underwear_sniff
    with dissolve
    x "(I pick up the underwear hesitantly, and my hands are shaking so badly I can barely hold it.)"
    show madd paralyzed at left_small
    with dissolve
    x "(The fabric is clearly stained—darker patches visible in the crotch area, evidence of his arousal, his body's fluids.)"
    show madd distressed at left_small
    with dissolve
    x "(This is too much. This is asking me to literally inhale his sexual essence.)"
    show madd violated at left_small
    with dissolve
    
    x "(But I bring it closer to my nose anyway. Slowly. Inevitably.)"
    show madd feels violated  at left_small
    with dissolve
    x "(And I take a whiff.)"
    show madd horrified at left_small
    with dissolve
    
    x "(The smell is completely different from the socks.)"
    show madd nauseated at left_small
    with dissolve
    x "(It's thick, almost palpable. Sweat, yes, but also something musky, something raw and deeply sexual.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(There's a sweetness to it too—something I don't immediately recognize but understand instinctively.)"
    show madd confused at left_small
    with dissolve
    x "(It's his arousal. His desire. Literally embedded in the fabric of his underwear.)"
    show madd violated at left_small
    with dissolve
    
    dad_thinks "(She's smelling my cum. She's breathing in the evidence of my lust.)"
    show dad lustful at right_small
    with dissolve
    dad_thinks "(This is primal. This is pure domination.)"
    show dad obsessed at right_small
    with dissolve
    
    x "(I pull the underwear away from my face, but he hasn't instructed me to open it yet, and I know that's coming.)"
    show madd nervous at left_small
    with dissolve
    x "(The anticipation is almost worse than the act itself.)"
    show madd anxious at left_small
    with dissolve
    
    dad_says "Open it. Put your nose inside properly."
    show dad dominant at right_small
    with dissolve
    dad_thinks "(Let her see. Let her smell the depths of my mark.)"
    show dad controlling at right_small
    with dissolve
    
    x "(I know this is coming. I've already prepared myself mentally for it.)"
    show madd determined at left_small
    with dissolve
    x "(But knowing doesn't make it any easier.)"
    show madd trembling at left_small
    with dissolve
    
    scene dad_room_cleaning_event_second_time_clothes_underwear_sniff_open_underwear
    with dissolve
    x "(I open the underwear, the elastic stretching, and bring my nose to the opening.)"
    show madd paralyzed at left_small
    with dissolve
    
    dad_thinks "(Yes. Her face in my underwear. This is the moment.)"
    show dad fixated at right_small
    with dissolve
    
    x "(I inhale, deeply this time, because he's watching and I know he expects nothing less.)"
    show madd horrified at left_small
    with dissolve
    
    x "(The smell is so strong it fills my entire nasal cavity, coating the back of my throat, making me gag violently.)"
    show madd nauseated at left_small
    with dissolve
    x "(It's overwhelming. It's visceral. It's deeply, profoundly wrong.)"
    show madd violated at left_small
    with dissolve
    x "(But I hold it. Two seconds.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(I'm inhaling his sex. I'm breathing in the physical manifestation of his desire for me. His desire to breed me. To own me.)"
    show madd broken at left_small
    with dissolve
    
    dad_says "Good girl. A good pet always recognizes their master's scent."
    show dad possessive at right_small
    with dissolve
    dad_thinks "(Master. I want her to think of me as her master.)"
    show dad controlling at right_small
    with dissolve
    
    x "(I pull away from the underwear, gasping for breath like I've been held underwater.)"
    show madd weeping at left_small
    with dissolve
    x "(Tears are streaming down my face, though I'm not sure when they started.)"
    show madd traumatized at left_small
    with dissolve
    
    dad_says "The more intimate the part, the better you need to check it."
    show dad dominant at right_small
    with dissolve
    dad_thinks "(She's crying now. The breaking point is near.)"
    show dad sadistic at right_small
    with dissolve
    
    x "(I put the underwear aside, marked as unsuitable, though we both know that's a lie.)"
    show madd resigned at left_small
    with dissolve
    x "(I move to the next pair, my movements now automatic, my mind somehow separate from my body.)"
    show madd processing at left_small
    with dissolve
    
    x "(I repeat this process. Again and again. Each pair of underwear bringing a new assault, a new degradation.)"
    show madd processing at left_small
    with dissolve
    x "(With each submissive action, each obedient sniff, I feel more and more like his property.)"
    show madd self loathing at left_small
    with dissolve
    x "(The resistance in me is breaking down, piece by piece, sniff by sniff.)"
    show madd conflicted at left_small
    with dissolve
    
    dad_thinks "(I can see it happening. The moment she stops fighting. The moment she accepts.)"
    show dad obsessed at right_small
    with dissolve
    dad_thinks "(By the time I'm done with her, she won't just obey. She'll want to obey.)"
    show dad possessive at right_small
    with dissolve
    
    x "(By the time I've finished smelling all of his underwear, I'm shaking all over.)"
    show madd trembling at left_small
    with dissolve
    x "(My body is cold, my mind is foggy, and something inside me has changed.)"
    show madd traumatized at left_small
    with dissolve
    
    x "(But something else has changed too. Something twisted. Something dark.)"
    show madd conflicted at left_small
    with dissolve
    x "(As disgusting as it was, as degrading as it was, there's a small part of me that... that wants more of that smell.)"
    show madd shocked at left_small
    with dissolve
    x "(What does that make me?)"
    show madd confused at left_small
    with dissolve
    
    dad_thinks "(She's almost there. I can see the surrender in her posture.)"
    show dad mocking at right_small
    with dissolve
    dad_thinks "(Soon she won't need me to command her. She'll come willingly.)"
    show dad calculating at right_small
    with dissolve
    
    x "(I look up at him, and I can see the satisfaction in his eyes.)"
    show madd hesitant at left_small
    with dissolve
    x "(He knows what's happening to me. He's engineered it.)"
    show madd overwhelmed at left_small
    with dissolve
    
    dad_says "Good. I can see it in your face. The change. The acceptance."
    show dad manipulative at right_small
    with dissolve
    dad_thinks "(Her facial expression is changing. Becoming more submissive.)"
    show dad lecherous at right_small
    with dissolve
    dad_thinks "(This is how I play the slow game. This is how I break them.)"
    show dad obsessed at right_small
    with dissolve
    
    dad_says "Tomorrow, we'll do something more... engaging."
    show dad dominant at right_small
    with dissolve
    dad_thinks "(Each day, another step. Each day, another piece of her surrenders.)"
    show dad hungry at right_small
    with dissolve
    
    dad_says "That will be all for today."
    show dad dominant at right_small
    with dissolve
    
    x "(I nod quickly, eager to escape, to be alone, to try to make sense of what just happened to me.)"
    show madd resigned at left_small
    with dissolve
    x "(But as I was standing there waiting for my payment, I can still smell him on my hands, on my face, in my hair.)"
    show madd processing at left_small
    with dissolve
    x "(And that small, dark part of me... it wants to smell him again.)"
    show madd horrified at left_small
    with dissolve
    
    $ character_relations["dad"]["intimacy"]+=3
    $ character_relations["dad"]["lust"]=max(0,character_relations["dad"]["lust"]-20)
    $ madd_willpower=max(0,madd_willpower-20)
    $ journal_event_set_done("Dad", "Room Cleaning: Folding Clothes")
    $ journal_event_show("Dad", "Room Cleaning: Anger")

    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_42
    if character_relations["dad"]["anger"]>=30 or character_relations["dad"]["lust"]>=50 :
        call dad_room_cleaning_event_second_time_clothes_anger_event from _call_dad_room_cleaning_event_second_time_clothes_anger_event

    jump dad_clean_event_getting_paid


label dad_room_cleaning_event_second_time_clothes_anger_event:

    
    dad_thinks "(I have had it with this bitch. All this anger inside me is making me act. I need to teach her a lesson.)"
    show dad angry at right_small
    with dissolve
    dad_thinks "(She spends all this time smelling me, basking in my essence, and still she has the audacity to resist me?)"
    show dad angry at right_small
    with dissolve
    dad_thinks "(Now that she's just finished that intimate task, now would be the perfect time.)"
    show dad cruel at right_small
    with dissolve
    dad_thinks "(Time to remind her exactly what she is. Time to break her completely.)"
    show dad dominant at right_small
    with dissolve
    scene scene_dad_room_cleaning_smell_clothes_anger_event_dad_sits_close
    with dissolve
    x "(After I've just finished folding his clothes and sorting through his socks and underwear, he gets up from his chair.)"
    show madd processing at left_small
    with dissolve
    x "(I expect him to dismiss me, to tell me I can leave. But instead, he sits down on the bed next to me.)"
    show madd nervous at left_small
    with dissolve
    x "(The proximity is immediate and overwhelming. I can smell him—not just the scent lingering on his clothes, but his actual scent.)"
    show madd anxious at left_small
    with dissolve
    
    x "(I can see he's angry. Not the controlled anger from before, but something raw, something barely contained.)"
    show madd feels violated  at left_small
    with dissolve
    x "(And I know why. It's because of my previous actions. Times when I've pulled away, when I've resisted his advances.)"
    show madd shaken at left_small
    with dissolve
    x "(He considers me as part of his property, and me defying him must have pushed him over the edge.)"
    show madd horrified at left_small
    with dissolve
    
    dad_thinks "(She knows. I can see it in her eyes. The fear. The anticipation. Good.)"
    show dad possessive at right_small
    with dissolve
    
    scene scene_dad_cleaning_smell_clothes_room_anger_event_hands_on_jaw
    with dissolve
    
    x "(Suddenly, his hands move to my face.)"
    show madd shocked at left_small
    with dissolve
    x "(He grips my jaw with surprising strength, his fingers pressing into the soft flesh beneath my chin.)"
    show madd paralyzed at left_small
    with dissolve
    x "(I'm completely frozen. This isn't the controlled touch from before. This is aggressive, demanding, demeaning.)"
    show madd overwhelmed at left_small
    with dissolve
    
    dad_thinks "(Her jaw in my hands. So fragile. So easy to break. But I won't break her. I'll mold her.)"
    show dad possessive at right_small
    with dissolve
    dad_thinks "(She needs to understand the price of defiance.)"
    show dad controlling at right_small
    with dissolve
    
    dad_says "Your constant rejection. Your refusal of my advances... it's gone too far."
    show dad angry at right_small
    with dissolve
    dad_thinks "(Each word is a threat. Each word is a promise of what's to come.)"
    show dad dominant at right_small
    with dissolve
    
    dad_says "Don't you forget that you live under my roof, under my protection. Your mother understood that."
    show dad mocking at right_small
    with dissolve
    dad_thinks "(Her mother never resisted. She accepted her place. But this one... this one needs to learn.)"
    show dad delusional at right_small
    with dissolve
    
    x "(His grip on my jaw tightens, the pressure building uncomfortably.)"
    show madd distressed at left_small
    with dissolve
    x "(My teeth press against the inside of my cheeks. The pain is sharp, focused, a physical reminder of his power.)"
    show madd trembling at left_small
    with dissolve
    x "(I know something bad is coming. I can feel it in the tension of his body, in the heat radiating from him.)"
    show madd horrified at left_small
    with dissolve
    
    dad_thinks "(Now is the time I teach her her place. She will remember this lesson forever.)"
    show dad sadistic at right_small
    with dissolve
    dad_thinks "(Every time she thinks about resisting, she'll remember this moment.)"
    show dad obsessed at right_small
    with dissolve
    
    x "(Without warning, he pulls me closer to him.)"
    show madd shocked at left_small
    with dissolve
    x "(The sudden movement catches me off guard, and I stumble slightly, my balance disrupted.)"
    show madd shocked at left_small
    with dissolve
    
    scene scene_dad_clean_smell_anger_event_shirt_pull
    with dissolve
    
    x "(His other hand finds my shirt, and he pulls it with force.)"
    show madd horrified at left_small
    with dissolve
    x "(The fabric tears slightly at the seam. I dare not say a word. I see the anger in his eyes—raw, primal, hungry.)"
    show madd violated at left_small
    with dissolve
    
    dad_thinks "(She's mine. This body is mine. Every part of it belongs to me.)"
    show dad possessive at right_small
    with dissolve
    dad_thinks "(I need to feel her. I need to claim her.)"
    show dad lustful at right_small
    with dissolve

    scene scene_dad_clean_smell_anger_event_shirt_pull_hands_inside_shirt
    with dissolve


    x "(He pushes his hand inside my shirt, his fingers making contact with my bare skin.)"
    show madd paralyzed at left_small
    with dissolve
    x "(The sensation is overwhelming. His hand is warm, calloused, the skin rough from years of labor.)"
    show madd trembling at left_small
    with dissolve
    x "(He explores the bare skin of my torso without restraint, his touch both gentle and aggressive at the same time.)"
    show madd conflicted at left_small
    with dissolve
    
    dad_thinks "(Her skin is so soft. So unmarked. So mine.)"
    show dad hungry at right_small
    with dissolve
    dad_thinks "(Soon every inch of her will bear my mark.)"
    show dad obsessed at right_small
    with dissolve
    
    x "(His hand moves upward, slowly, deliberately.)"
    show madd nervous at left_small
    with dissolve
    x "(I know exactly where it's going. I can feel the trajectory of his touch, the inevitability of it.)"
    show madd feels violated  at left_small
    with dissolve
    x "(He takes his time, feeling every curve, every contour of my bare skin.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(Each second feels like an eternity of anticipation and dread.)"
    show madd distressed at left_small
    with dissolve
    
    scene scene_dad_clean_smell_anger_event_shirt_pull_hands_inside_shirt_breast_contact
    with dissolve
    
    x "(And then... his hand lands on my bare breast.)"
    show madd shocked at left_small
    with dissolve
    x "(Direct contact. No bra. Nothing between his palm and my skin.)"
    show madd horrified at left_small
    with dissolve
    
    x "(I see a visible change in his expression. The anger seems to... shift. Transform. His breathing deepens.)"
    show madd processing at left_small
    with dissolve
    x "(There's relief in his eyes now. A satisfied look, as if touching my breast calms something inside him.)"
    show madd violated at left_small
    with dissolve
    
    dad_thinks "(Yes. This is what I needed. This contact. This physical claim over her body.)"
    show dad obsessed at right_small
    with dissolve
    dad_thinks "(Her breast in my hand... it's everything.)"
    show dad fixated at right_small
    with dissolve
    
    x "(He gropes my left breast roughly, feeling its weight, its shape, exploring every inch.)"
    show madd trembling at left_small
    with dissolve
    x "(The sensation is uncomfortable, bordering on painful. His grip is firm, possessive, demanding.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(Then he moves to the right, repeating the process, squeezing, feeling, claiming.)"
    show madd violated at left_small
    with dissolve
    
    dad_thinks "(She's completely exposed now. She can't hide from me. She can't escape.)"
    show dad dominant at right_small
    with dissolve
    dad_thinks "(This is what she needed. This is what she deserves.)"
    show dad cruel at right_small
    with dissolve
    
    x "(His touch continues, relentless and invasive, exploring my body to his heart's content.)"
    show madd paralyzed at left_small
    with dissolve
    x "(Minutes pass. Five minutes. Ten minutes. The time blurs together.)"
    show madd broken at left_small
    with dissolve
    x "(And then something changes. His hand moves to my nipple.)"
    show madd shocked at left_small
    with dissolve
    
    x "(He pinches it, not gently, but with enough pressure to make me gasp involuntarily.)"
    show madd distressed at left_small
    with dissolve
    scene scene_dad_clean_smell_anger_event_1_thumb_on_lips
    dad_says "Now open your mouth."
    show dad dominant at right_small
    with dissolve
    dad_thinks "(Time for the next stage. Time to have her taste me directly.)"
    show dad lustful at right_small
    with dissolve
    dad_thinks "(This is the point of no return for her. Once she takes me into her mouth, she's no longer just a victim.)"
    show dad sadistic at right_small
    with dissolve
    dad_thinks "(She becomes a willing participant in her own degradation.)"
    show dad obsessed at right_small
    with dissolve
    

    
    x "(His thumb moves to my lips, positioned right at the entrance.)"
    show madd horrified at left_small
    with dissolve
    x "(I know what's coming. I know that if I obey, his thumb will enter my mouth. This is the line.)"
    show madd feels violated  at left_small
    with dissolve
    x "(But I dare not disobey. The anger in his eyes is still there, waiting, ready to resurface.)"
    show madd paralyzed at left_small
    with dissolve

    scene scene_dad_clean_smell_anger_event_1_thumb_inside_mouth
    with dissolve

    x "(Slowly, hesitantly, I open my mouth.)"
    show madd trembling at left_small
    with dissolve
    x "(It's barely a gap, just enough for my teeth to part, just enough for him to see the darkness within.)"
    show madd hesitant at left_small
    with dissolve
    
    dad_thinks "(There. The opening. Her mouth is open for me. This is surrender.)"
    show dad dominant at right_small
    with dissolve
    
    x "(The moment there's even a small space, his thumb pushes inside.)"
    show madd shocked at left_small
    with dissolve
    x "(It's sudden, invasive, and deeply violating. My reflex is to gag, but I suppress it.)"
    show madd nauseated at left_small
    with dissolve
    
    x "(I can feel it. The texture of his skin, rough and slightly damp.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(I can taste it. The saltiness of his skin, the faintness of sweat, the bitterness of something else I can't identify.)"
    show madd violated at left_small
    with dissolve
    x "(The heat it generates is unexpected. His thumb is warm, and it's filling a significant portion of my mouth.)"
    show madd distressed at left_small
    with dissolve
    
    dad_thinks "(Her mouth around my thumb. This is intimate in a way nothing else has been.)"
    show dad fixated at right_small
    with dissolve
    dad_thinks "(Soon it will be my cock. Soon she'll be begging for it.)"
    show dad lecherous at right_small
    with dissolve
    
    x "(It's overwhelming. The violation of this act, the surrender it represents. My mouth is no longer my own.)"
    show madd broken at left_small
    with dissolve
    
    dad_says "Good girl. Now use your tongue. I want every part of your tongue to taste me. Recognize me."
    show dad dominant at right_small
    with dissolve
    dad_thinks "(Make her use her tongue. Make her actively participate in her own degradation.)"
    show dad controlling at right_small
    with dissolve
    
    x "(I do as commanded, moving my tongue, letting each part of it come into contact with his thumb.)"
    show madd resigned at left_small
    with dissolve
    x "(My tongue is fluid, flexible, responsive. I swirl it around his thumb, and with each movement, a different part tastes his skin.)"
    show madd processing at left_small
    with dissolve
    x "(The tip of my tongue. The sides. The back. The underside. Every surface becomes intimate with him.)"
    show madd overwhelmed at left_small
    with dissolve
    
    dad_thinks "(Yes. She's tasting me. She's recognizing me with her tongue. This is perfect.)"
    show dad obsessed at right_small
    with dissolve
    
    x "(And as I do this, something inside me shifts.)"
    show madd conflicted at left_small
    with dissolve
    x "(Something dark awakens. I'm humiliated, I'm degraded, I'm violated...)"
    show madd self loathing at left_small
    with dissolve
    x "(But a part of me is... enjoying this.)"
    show madd shocked at left_small
    with dissolve
    
    x "(Is it because of what I smelled earlier? The hours spent inhaling his essence?)"
    show madd confused at left_small
    with dissolve
    x "(Maybe biology is real. Maybe exposure to someone's scent, their pheromones, creates some kind of chemical response in the brain.)"
    show madd processing at left_small
    with dissolve
    x "(I'm obeying every order he gives me, and some part of me is... loving it.)"
    show madd conflicted at left_small
    with dissolve
    x "(Loving the degradation. Loving the loss of control.)"
    show madd trembling at left_small
    with dissolve
    
    dad_thinks "(If I keep doing this, I can make bolder moves. Eventually, I'll get myself a new wife.)"
    show dad possessive at right_small
    with dissolve
    dad_thinks "(I will eventually put a baby in her belly and she'd be mine forever.)"
    show dad delusional at right_small
    with dissolve
    dad_thinks "(She'll never be able to leave. She'll never be able to resist.)"
    show dad obsessed at right_small
    with dissolve
    
    x "(The sensation of not being in control is... intoxicating.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(Being guided by someone who has more power than me, more control over me than I have over myself.)"
    show madd hesitant at left_small
    with dissolve
    x "(It should terrify me. And it does. But it also...)"
    show madd conflicted at left_small
    with dissolve
    x "(It also excites some dark part of me that I didn't know existed.)"
    show madd horrified at left_small
    with dissolve
    
    x "(This continues for around ten minutes. Him groping me with one hand while his thumb stays in my mouth, leaving his essence for me to taste with the other.)"
    show madd broken at left_small
    with dissolve
    x "(And some part of me... loves every second of it.)"
    show madd conflicted at left_small
    with dissolve
    x "(What does that make me?)"
    show madd self loathing at left_small
    with dissolve
    
    dad_thinks "(She's coming along nicely. By the end of this, she'll be completely mine.)"
    show dad obsessed at right_small
    with dissolve
    dad_thinks "(She'll crave my touch. She'll beg for it.)"
    show dad dominant at right_small
    with dissolve
    
    scene scene_dad_cleaning_smelling_anger_event_aftermath
    with dissolve
    
    x "(Eventually, he lets me go. His thumb withdraws from my mouth, and I gasp for breath like I've been held underwater.)"
    show madd weeping at left_small
    with dissolve
    x "(My shirt falls back into place, covering my exposed skin, though the shame remains.)"
    show madd traumatized at left_small
    with dissolve
    
    x "(I stand up slowly, my legs unsteady, my body still trembling from what just happened.)"
    show madd shaken at left_small
    with dissolve
    x "(I move toward the door, ready to collect my payment and leave, though I'm not sure how to face the world right now.)"
    show madd overwhelmed at left_small
    with dissolve
    
    dad_thinks "(She'll be back tomorrow. They always come back. Once women taste coercive control, they crave it.)"
    show dad obsessed at right_small
    with dissolve
    
    $ character_relations["dad"]["intimacy"]+=5
    $ character_relations["dad"]["anger"]=character_relations["dad"]["anger"]-40
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["oral_sex"] += 1
    $ madd_willpower=max(0,madd_willpower-10)
    $ journal_event_set_done("Dad", "Room Cleaning: Anger")
    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_43
    $ character_relations["dad"]["lust"]=0    
    jump dad_clean_event_getting_paid


label dad_room_cleaning_event_nothing_happens:
    scene scene_madd_dad_talk_before_maid_event
    with dissolve
    show madd nervous at left_small
    with dissolve
    
    dad_says "Today you will dust the place. Make sure everything is spotless. I want to see my reflection in every surface."
    show dad dominant at right_small
    with dissolve
    dad_thinks "(She looks nervous. But today, I'm not in the mood to push her. I have other things on my mind.)"
    show dad calculating at right_small
    with dissolve
    
    x "(I nod, feeling a strange mixture of relief and uncertainty.)"
    show madd processing at left_small
    with dissolve
    x "(Today feels different. There's no predatory intensity in his eyes, no deliberate positioning.)"
    show madd hesitant at left_small
    with dissolve
    
    scene scene_dad_room_cleaning_event_second_time_dusting_vaccum_nothing_happens
    with fade
    
    x "(I start dusting the shelves, the desk, anywhere I can reach.)"
    show madd focused at left_small
    with dissolve
    x "(He watches TV in the corner, seemingly unconcerned with what I'm doing.)"
    show madd processing at left_small
    with dissolve
    
    x "(It's almost strange. All the other times I've been in this room with him, there's been this underlying threat.)"
    show madd relieved at left_small
    with dissolve
    x "(But today... today it feels like he's just... ignoring me.)"
    show madd conflicted at left_small
    with dissolve
    
    dad_thinks "(She keeps glancing at me, waiting for something. But not today. Today I don't have the energy.)"
    show dad wistful at right_small
    with dissolve
    dad_thinks "(Today I just need her to do the work.)"
    show dad cruel at right_small
    with dissolve
    
    x "(I work methodically through the room, and for once, nothing happens. No violation. No degradation.)"
    show madd determined at left_small
    with dissolve
    x "(Just me, cleaning. Just him, watching TV.)"
    show madd processing at left_small
    with dissolve
    
    x "(And somehow, that makes me feel worse.)"
    show madd conflicted at left_small
    with dissolve
    x "(Because even though nothing is happening, I'm waiting for it.)"
    show madd anxious at left_small
    with dissolve
    x "(I'm expecting it. A part of me is disappointed that it hasn't.)"
    show madd distressed at left_small
    with dissolve
    
    x "(What does that say about me?)"
    show madd self loathing at left_small
    with dissolve
    
    x "(Eventually, I finish. I've cleaned everything he asked for, and nothing has occurred.)"
    show madd relieved at left_small
    with dissolve
    
    dad_says "Good work. That will be all for today."
    show dad mocking at right_small
    with dissolve
    dad_thinks "(She's wondering why I didn't touch her. Good. Let her wonder. Let her anticipate.)"
    show dad calculating at right_small
    with dissolve

    show madd confused at left_small
    with dissolve
    x "(Have I really become so broken that I crave his violations?)"
    show madd distressed at left_small
    with dissolve
    x "(What kind of person does that make me?)"

    $ character_relations["dad"]["intimacy"]+=1
    $ madd_willpower=max(0,madd_willpower-20)
    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_44

    jump dad_clean_event_getting_paid


label dad_room_cleaning_event_clean_feet:

    scene dad_room_cleaning_event_clean_feet_start
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd focused at left_small
    with dissolve
    x "(As usual, I was cleaning the room while my stepfather lay on the bed watching me like a teacher invigilating a student.)"
    show madd stressed at left_small
    with dissolve
    x "(I was exhausted from cleaning the room and sweating a lot.)"
    show madd relieved at left_small
    with dissolve
    x "(Finally done, I sat down on the floor next to the bed to rest for a bit.)"


    scene dad_room_cleaning_event_clean_feet_maddie_sitting_on_floor
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd nervous at left_small
    with dissolve
    x "(I was trying to cool down and relax. My stepdad was still watching me and I could see his mischievous smile on his face.)"
    show dad smirk at right_small
    with dissolve
    x "(I knew something was going to happen, but I didn't know what.)"
    show madd anxious at left_small
    with dissolve
    
    
    scene dad_room_cleaning_event_clean_feet_dad_first_clean_my_feet_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad calculating at right_small
    with dissolve
    dad_says "Are you finished, Maddie?"
    show madd hesitant at left_small
    with dissolve
    x "(Then he raised his foot and brought it very close to my face.)"
    show madd shocked at left_small
    with dissolve
    x "(I could smell his feet immediately and I was disgusted by it, but I didn't want to offend him so I just kept quiet.)"
    show dad dominant at right_small
    with dissolve
    dad_says "I don't pay you to slack off."
    show madd horrified at left_small
    with dissolve
    x "(HIS FEET ARE DISGUSTING AND SMELLY. WHY IS IT SO CLOSE TO MY FACE?)"
    show madd distressed at left_small
    with dissolve
    x "I'm almost done, dad..."
    show madd paralyzed at left_small
    with dissolve
    x "(Immediately after I said that he put his foot on my face and started rubbing it all over.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(The smell assaulted my nose and I was trying to hold my breath, but it was impossible.)"
    show dad sadistic at right_small
    with dissolve

    x "(I couldn't remove his foot from my face. I needed the money.)"
    show madd resigned at left_small
    with dissolve

    scene dad_room_cleaning_event_clean_feet_dad_first_clean_my_feet_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show dad lecherous at right_small
    with dissolve
    x "(He revolved his foot around my face as if tempting me to smell it more and more.)"
    show madd nauseated at left_small
    with dissolve
    x "(Who in their right mind would want to smell their stepfather's feet?)"
    show dad dominant at right_small
    with dissolve
    dad_says "Go on, clean my feet while you're at it."
    show madd conflicted at left_small
    with dissolve
    x "(How am I supposed to get out of this?)"
    show madd trembling at left_small
    with dissolve
    x "(I stopped breathing and just tried to endure the smell as much as I could.)"
    x "O-okay, dad..."
    show madd distressed at left_small
    with dissolve
    x "(I held his foot with both my hands and put his toes in my mouth and started sucking on them.)"
    show madd violated at left_small
    with dissolve
    x "(The smell only got worse now that I was tasting his feet directly.)"
    show madd confused at left_small
    with dissolve
    x "(Surprisingly, his feet weren't as calloused as I thought they would be — they were actually pretty soft.)"
    x "(I don't know why I thought it would be like licking a piece of sandpaper.)"
    show madd processing at left_small
    with dissolve
    x "(If it wasn't for the smell, it wasn't that bad.)"

    scene dad_room_cleaning_event_clean_feet_dad_first_clean_my_feet_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small
    with dissolve
    x "(I kept twirling my tongue around his toes and sucking on them while trying to ignore the smell.)"
    show dad mocking at right_small
    with dissolve
    dad_says "That's right, Maddie. Keep licking my feet like a dog..."
    show madd horrified at left_small
    with dissolve
    x "(I tried to ignore the fact that he just compared me to a dog, but it wasn't far from the truth with his foot in my mouth.)"
    show madd shaken at left_small
    with dissolve
    x "(I then pulled his foot away from my mouth and started using my tongue to clean the web spaces between his toes.)"
    show madd determined at left_small
    with dissolve
    x "(I had to get it cleaned properly or I won't get paid.)"
    show dad fixated at right_small
    with dissolve
    x "(But I noticed I was no longer as bothered by the smell as I was before — perhaps it was because my nose was completely full of it.)"
    show madd processing at left_small
    with dissolve
    x "(I continued using my tongue over his feet and now it wasn't bad at all.)"

    scene dad_room_cleaning_event_clean_feet_dad_first_clean_my_feet_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad possessive at right_small
    with dissolve
    dad_says "That's how you clean this room, Maddie. You clean my space, you clean my body too."
    show madd distressed at left_small
    with dissolve
    x "(I wasn't surprised by his statement. I knew he would do anything possible to get more of himself into my body.)"
    show madd conflicted at left_small
    with dissolve
    x "(Be it his filthy feet, his disgusting cum, or his unwashed scent all over my body — there was always another way.)"
    show madd resigned at left_small
    with dissolve
    x "(I put his toes back in my mouth and started sucking on them again.)"
    show madd inhead at left_small
    with dissolve
    x "(This was just like cleaning anything else, except now the taste and smell were growing on me.)"
    show dad obsessed at right_small
    with dissolve
    x "(My nose was involuntarily sniffing his feet more and more — fucking disgusting, I know — but I couldn't help it. I hoped he didn't notice, or he'd make me do it more often.)"
    show madd anxious at left_small
    with dissolve
    x "(I didn't hear any reaction from him so I just kept going.)"

    scene dad_room_cleaning_event_clean_feet_dad_first_clean_my_feet_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad smirk at right_small
    with dissolve
    dad_says "You think I can't feel you sniffing my feet?"
    show madd shocked at left_small
    with dissolve
    x "(No way he can feel that, right?)"
    show dad predatory at right_small
    with dissolve
    dad_thinks "(Oh I can feel every single sniff. She's practically huffing my foot at this point.)"
    x "(I didn't react. He withdrew his foot from my mouth — and it felt like a child being separated from its pacifier.)"
    show madd confused at left_small
    with dissolve
    x "(Why did I feel that way? It's literally my dad's foot.)"
    show madd horrified at left_small
    with dissolve
    show dad dominant at right_small
    with dissolve
    x "(He then rubbed his foot all over my face as if to mark his territory and show me he was in charge.)"
    show madd violated at left_small
    with dissolve
    x "(The sole of his foot was rubbing against my cheeks and I pulled my tongue out to get it cleaned as well.)"
    show madd broken at left_small
    with dissolve
    x "(Why was this kind of enjoyable?)"
    show madd conflicted at left_small
    with dissolve
    x "(When his foot was inside my mouth I felt like I was in a trance. I knew I was an orphan, but with his foot in my mouth I felt a sense of belonging and relief that I didn't have before.)"
    show dad possessive at right_small
    with dissolve
    dad_says "Just say you love licking my feet, Maddie."
    show madd overwhelmed at left_small
    with dissolve
    x "(He kept rubbing his foot on my face and I was doing my part of the cleaning.)"
    show madd shaken at left_small
    with dissolve
    x "(Finally it all ended with his big toe pushed deep into my mouth.)"

    scene dad_room_cleaning_event_clean_feet_dad_first_clean_my_feet_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad controlling at right_small
    with dissolve
    x "(He pushed his toes deeper into my mouth. At this point my tongue and nose were moving on their own accord — I was taking in deep breaths of his feet.)"
    show madd salivating at left_small
    with dissolve
    show dad wistful at right_small
    with dissolve
    dad_says "Yeah... just stay like that for a while and enjoy it."
    show dad obsessed at right_small
    with dissolve
    dad_thinks "(She's sucking on my toes like she was born to do it. Every session I take a little more.I am gonna own this bitch.)"
    dad_says "Then you can leave. You've cleaned enough."
    show madd trembling at left_small
    with dissolve
    x "(I used my hand as a stand for his foot and kept cleaning. I'm damn sure from the way I was doing it that I looked like a child sucking on a pacifier.)"
    show madd inhead at left_small
    with dissolve
    x "(His foot stayed in my mouth, changing my brain chemistry for ten more minutes, until he finally pulled it out.)"
    show madd broken at left_small
    with dissolve
    x "(I knew that whole licking session changed something inside me — I really wanted to put it back in or have another whiff.)"
    show madd conflicted at left_small
    with dissolve
    x "(I got up from the floor to collect the money I was owed, but in my head I thought I was already paid in full just from the experience of licking his feet.)"
    show madd confused at left_small
    with dissolve

    $ character_relations["dad"]["intimacy"] += 7
    $ character_relations["dad"]["lust"] = max(0, character_relations["dad"]["lust"] - 30)
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["groped_madd"] += 1
    $ madd_willpower = max(0, madd_willpower - 25)
    $ journal_event_set_done("Dad", "Room Cleaning: Foot Cleaning")
    $ journal_event_show("Dad", "Room Cleaning: Final Domination")
    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_clean_feet

    jump dad_clean_event_getting_paid

label dad_room_cleaning_event_clean_armpit:
    
    
    scene scene_dad_room_cleaning_event_second_time_dusting_vaccum_nothing_happens
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd focused at left_small
    with dissolve
    x "(I started vacuuming the room, and after I was done with that I moved on to dusting every surface.)"
    show madd stressed at left_small
    with dissolve
    x "(After a while it was spotless.)"

    scene dad_room_cleaning_event_clean_armpit_sitting_on_bed
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad wistful at right_small
    with dissolve
    x "(Stepdad had been resting on the bed, watching me clean the entire time.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(After I finished, I was completely exhausted, feet aching, so I sat down on the bed to rest for a bit.)"

    scene dad_room_cleaning_event_clean_armpit_sitting_on_bed_looking_at_stepdad
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd nervous at left_small
    with dissolve
    x "(Suddenly he peeled off his filthy shirt. Underneath he had on a tank top that was just as grimy as the one he'd taken off.)"
    show dad dominant at right_small
    with dissolve
    dad_says "Come closer."
    show madd anxious at left_small
    with dissolve
    x "(He growled it more than said it, and my body obeyed before my brain could weigh in.)"
    show madd hesitant at left_small
    with dissolve
    x "(The sudden shift in his voice and the hungry way he was staring at me made my stomach drop.)"

    scene dad_room_cleaning_event_clean_armpit_sitting_on_bed_looking_at_stepdad_dad_raises_arm
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad lecherous at right_small
    with dissolve
    x "(He raised his arm, exposing his hairy, disgusting armpit. From a foot away I could already smell it — sharp, pungent, rank with hours of built-up sweat.)"
    show madd horrified at left_small
    with dissolve
    x "(His other hand moved to the back of my head. I knew exactly what was coming and every nerve in my body screamed.)"
    show dad dominant at right_small
    with dissolve
    dad_says "Clean this for me."
    show madd paralyzed at left_small
    with dissolve
    x "(I played dumb and just stood there, hoping he'd drop it.)"

    scene dad_room_cleaning_event_clean_armpit_sitting_on_bed_looking_at_stepdad_dad_raises_arm_madd_in_dads_armpit_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad controlling at right_small
    with dissolve
    dad_says "Clean my underarms. Now."
    show madd shocked at left_small
    with dissolve
    x "(He didn't wait for a response — he pushed his arm down and shoved my face straight into his other armpit.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(I hadn't even processed what was happening before my face was already buried in it, his sweat and grime pressing into my skin.)"
    show madd nauseated at left_small
    with dissolve
    x "(Up close the smell was suffocating — thick, musky, the kind that gets into your throat and sits there.)"
    show madd distressed at left_small
    with dissolve
    x "Understood..."
    show dad sadistic at right_small
    with dissolve
    dad_says "Keep it clean if you want to get paid."
    show madd violated at left_small
    with dissolve
    x "(I couldn't make myself start. I just sat there frozen, disgusted, staring at the matted hair pressed against my face.)"
    show dad angry at right_small
    with dissolve
    dad_says "What are you waiting for? Get to work."

    scene dad_room_cleaning_event_clean_armpit_sitting_on_bed_looking_at_stepdad_dad_raises_arm_madd_in_dads_armpit_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small
    with dissolve
    x "(That tone was the trigger. My body responded before I could stop it.)"
    show madd distressed at left_small
    with dissolve
    x "(I pressed my tongue against his armpit and started licking — tasting the salt and grime caked into his skin and hair.)"
    show madd violated at left_small
    with dissolve
    x "(The texture was coarse from all the hair and dried sweat, but I kept going because I needed the money.)"
    show dad possessive at right_small
    with dissolve
    x "(His hand kept pressing my head deeper into his armpit, and I hated myself for not fighting it.)"
    show madd self loathing at left_small
    with dissolve
    x "(There I was, licking my stepdad's sweaty armpit like an obedient little dog, just so I could get paid.)"
    show madd broken at left_small
    with dissolve
    x "(What the fuck had I become?)"
    show dad mocking at right_small
    with dissolve
    dad_says "Yeah, that's right. Make it shine."
    show madd conflicted at left_small
    with dissolve
    x "(I knew I shouldn't be tolerating this. I knew it was wrong. But my bank account didn't care about my dignity.)"
    show madd processing at left_small
    with dissolve
    x "(Money was the only way out of this situation — so if I had to tongue-clean his filthy armpit to get it, so be it.)"

    scene dad_room_cleaning_event_clean_armpit_sitting_on_bed_looking_at_stepdad_dad_raises_arm_madd_in_dads_armpit_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd inhead at left_small
    with dissolve
    x "(After a while I started getting used to the smell and taste. Still disgusting, but bearable in a way that disturbed me.)"
    show madd confused at left_small
    with dissolve
    x "(It felt like I was sinking deeper and deeper into his world — his world of filth and sweat — and the worst part was I had stopped trying to climb back out.)"
    show dad cruel at right_small
    with dissolve
    dad_says "This is your only meal for the day."
    show madd horrified at left_small
    with dissolve
    x "(Why did he have to humiliate me like this on top of everything else? I was already in pieces mentally.)"
    show madd self loathing at left_small
    with dissolve
    x "(The only thing I was getting from licking his armpit was a mouthful of his sweat and a lungful of his stench.)"
    show madd conflicted at left_small
    with dissolve
    x "(And his pheromones — which were probably the reason I was starting to feel something other than disgust.)"
    show madd shocked at left_small
    with dissolve
    x "(Holy fuck. I just made up a reason for why I was getting turned on by licking my stepdad's armpit.)"
    show madd inhead at left_small
    with dissolve
    x "(No. Stop. Don't think about it. Block it out. But why did this suddenly feel so good?)"
    show madd salivating at left_small
    with dissolve
    x "(My nose was pulling in long, deep breaths of his armpit on its own, and I was getting genuinely high off the smell.)"

    scene dad_room_cleaning_event_clean_armpit_sitting_on_bed_looking_at_stepdad_dad_raises_arm_madd_in_dads_armpit_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd inheat at left_small
    with dissolve
    x "(The intoxication from his scent was bleeding directly into how the taste registered on my tongue — everything felt amplified, richer.)"
    show madd conflicted at left_small
    with dissolve
    x "(I was loving both the taste and the smell now. My nose kept dragging in more, involuntarily, like an addict at a pipe.)"
    show dad smirk at right_small
    with dissolve
    dad_says "I can hear you sniffing, Maddie."
    show madd shocked at left_small
    with dissolve
    dad_says "You like sniffing your dad's armpit, don't you?"
    show madd horrified at left_small
    with dissolve
    x "(I was mortified that he could hear it. I didn't answer — just kept licking, hoping my silence would pass as denial.)"
    show madd flustered at left_small
    with dissolve
    x "(He'd caught me enjoying it, and that concrete knowledge made everything ten times more humiliating. The best I could do now was take the money and pretend this never happened.)"

    scene dad_room_cleaning_event_clean_armpit_sitting_on_bed_looking_at_stepdad_dad_raises_arm_madd_in_dads_armpit_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd curious at left_small
    with dissolve
    x "(I'd had my eyes shut this whole time, but since I was already deep in it, I finally opened them — I wanted to see the filth I was putting in my mouth.)"
    show madd blush at left_small
    with dissolve
    x "(His hairy armpit was right there filling my entire field of view, and seeing it somehow made the whole thing hotter.)"
    show madd conflicted at left_small
    with dissolve
    x "(Why was this so hot? I was licking my stepdad's armpit and I was actively enjoying it. There was no version of this that wasn't completely depraved.)"
    show dad possessive at right_small
    with dissolve
    dad_says "I'll give you what you want, Maddie."
    show dad dominant at right_small
    with dissolve
    dad_says "Don't worry."
    show madd confused at left_small
    with dissolve
    x "(Was he talking about the money? Or something else entirely?)"
    show madd paralyzed at left_small
    with dissolve
    x "(Suddenly his hands roughly grabbed my head and shoved my face deeper into his armpit, pinning me there.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(My face was completely locked in — no movement, no escape, entirely at his mercy.)"
    show madd inheat at left_small
    with dissolve
    x "(Even trapped like that I kept licking. And the fact that I couldn't stop even if I wanted to made me even more turned on, which I had absolutely no idea how to process.)"
    show madd inhead at left_small
    with dissolve
    x "(So this was his version of giving me what I wanted — trapping my face in his armpit so I couldn't pull away even if I tried.)"
    show madd shocked at left_small
    with dissolve
    x "(I can't deny that the moment I got pinned, my heart skipped a beat as if i had just found love of my life.)"

    scene dad_room_cleaning_event_clean_armpit_sitting_on_bed_looking_at_stepdad_dad_raises_arm_madd_in_dads_armpit_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad hungry at right_small
    with dissolve
    x "(With my face locked in place and his arm pressing tighter, his body temperature was rising — I could feel the heat radiating off his skin.)"
    show madd salivating at left_small
    with dissolve
    x "(And then I saw it: fresh sweat beading out of his armpit, and I dragged my tongue through it in one long, greedy lick.)"
    show madd inheat at left_small
    with dissolve
    x "(It was straight sweat dripping from the source directly onto my tongue — the purest, most concentrated taste of him I'd gotten yet.)"
    show madd conflicted at left_small
    with dissolve
    x "(His raw, filthy sweat feeding straight into my mouth. And I wanted more.)"
    show dad lecherous at right_small
    with dissolve
    x "(He saw my expression — the look on my face when that sweat hit my tongue — and he knew exactly what it meant.)"
    show dad obsessed at right_small
    with dissolve
    dad_says "You like eating daddy's filthy sweat, huh?"
    show madd flustered at left_small
    with dissolve
    x "(God, the embarrassment. How was I ever going to look at him normally after this?)"
    show madd resigned at left_small
    with dissolve
    x "(I just kept going and finished what was in front of me.)"
    show dad delusional at right_small
    with dissolve
    dad_says "Don't worry, Maddie. Once you become my wife I'll have you licking my ass sweat and ball sweat too."
    show madd shocked at left_small
    with dissolve
    x "(I was floored by that statement — and even more floored that my body reacted to it like it was a promise rather than a threat.)"
    show madd horrified at left_small
    with dissolve
    x "(If his armpit smelled that rank, his ass sweat had to be ten times worse. And the fact that I was already wet at the thought of licking it made me feel like the dirtiest person alive.)"
    show madd inheat at left_small
    with dissolve
    x "(Part of me wanted to ask him if I could do it right now. I bit that part of me down hard and kept my mouth busy where it already was.)"

    scene dad_room_cleaning_event_clean_armpit_sitting_on_bed_looking_at_stepdad_dad_raises_arm_madd_in_dads_armpit_7
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad calculating at right_small
    with dissolve
    x "(After a while he loosened his grip and let me go — but my tongue kept moving on autopilot even after his arm dropped away.)"
    show madd broken at left_small
    with dissolve
    show dad mocking at right_small
    with dissolve
    dad_says "That's enough, Maddie."
    dad_says "It's clean now."
    show madd conflicted at left_small
    with dissolve
    x "(No no no — I had to pull away before he escalated this further.)"
    show madd distressed at left_small
    with dissolve
    x "(Fighting every instinct in my body, I pulled my face back, eyes still fixed on his hairy, filthy armpit that had somehow tasted incredible.)"
    show dad smirk at right_small
    with dissolve
    dad_says "You were licking it like it was the best thing you'd ever eaten."
    show madd horrified at left_small
    with dissolve
    x "(I put more distance between us when he said that. I couldn't let myself sink any deeper into this.)"
    show madd inhead at left_small
    with dissolve
    x "(My body was already screaming at me to ask him to let me lick his ass sweat or ball sweat. If I opened that door I might as well get on my knees and beg him to let me lick his asshole clean.)"
    show dad dominant at right_small
    with dissolve
    dad_says "Good work today, Maddie. You can go now."
    show madd resigned at left_small
    with dissolve

    $ character_relations["dad"]["intimacy"] += 7
    $ character_relations["dad"]["lust"] = max(0, character_relations["dad"]["lust"] - 30)
    $ character_relations["dad"]["touched_madd"] += 1
    $ madd_willpower = max(0, madd_willpower - 25)
    $ journal_event_set_done("Dad", "Room Cleaning: Armpit")
    $ journal_event_show("Dad", "Room Cleaning: Final Domination")
    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_clean_armpit

    jump dad_clean_event_getting_paid



label dad_room_cleaning_even_clean_final_domination:

    scene scene_dad_room_cleaning_event_second_time_dusting_vaccum_nothing_happens
    with dissolve 
    $ renpy.call_in_new_context("_hide_windows")
    show madd stressed at left_small
    with dissolve
    x "(I started my cleaning duties as general, everything was normal . I was using the vacuum cleaner to clean the floor, and I was dusting the shelves and furniture. "
    show dad angry at right_small
    with dissolve
    dad_says "Your cleaning lately has been complete shit, especially the under the table. It's filthy."
    dad_says "I pay you more than you deserve stupid bitch, you should be doing a better job. "
    show madd angry at left_small
    with dissolve
    x "(A hot spike of anger and frustration slammed into me. I had been working hard to clean his room while he made all sorts of advances towards me, and now he was criticizing my work and insulting me. )"
    show madd hesitant at left_small
    with dissolve
    x "I..I'm sorry dad, I will clean it up right away. "
    show dad controlling at right_small
    with dissolve
    dad_says "I will see to it personally that you do"
    show madd nervous at left_small
    with dissolve
    x "(He says that as he gets up right next to me as i prepare to clean under the table .)"


    scene scene_dad_room_cleaning_event_vacuming_under_table
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd stressed at left_small
    with dissolve
    x "(I started cleaning under the table, but one stubborn spot refused to lift no matter how hard I vacuumed. )"
    show dad angry at right_small
    with dissolve
    dad_says "You're useless at this. Hurry the fuck up."
    show madd distressed at left_small
    with dissolve
    x "(I cranked the vacuum to max and attacked the spot again, but it still wouldn't lift. )"
    show dad authoritative at right_small
    with dissolve
    dad_says "Im standing right here, Maddie. What the fuck is taking you so long?"
    show madd stressed at left_small
    with dissolve
    x "(I was already drenched in sweat, hair plastered to my neck, and my frustration was growing by the second. )"
    show madd anxious at left_small
    with dissolve
    x "I..I am trying dad."
    show dad angry at right_small
    with dissolve
    dad_says "Clearly not hard enough "
    show madd distressed at left_small
    with dissolve
    x "(Ugh, when will this end?  i leaned down to try to get the spot clean)"

    scene scene_dad_room_cleaning_event_vacuming_under_table_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd focused at left_small
    with dissolve
    x "(I wanted to have a good look at the spot, perhaps if i could figure out what it was, i could get it clean)"
    show madd nervous at left_small
    with dissolve
    x "(As I leaned down I knew my ass was sticking straight up in front of him. I could feel his stare burning into me and my face flushed with humiliation. )"
    show dad lecherous at right_small
    with dissolve
    dad_says "Are you trying to seduce your dad? You dont even have to try, you already do. "
    show madd shocked at left_small
    with dissolve
    x "(I froze, equal parts shocked and disgusted. I had to get the hell out of this situation. )"
    show madd distressed at left_small
    with dissolve
    x "No dad , I am just trying to clean the floor. "
    show madd anxious at left_small
    with dissolve
    x "(I placed the vacuum cleaner down and picked up a rag to try to clean the spot manually)"

    scene scene_dad_room_cleaning_event_dusting_under_table
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd stressed at left_small
    with dissolve
    x "(I switched to a rag and scrubbed furiously, but the spot refused to fade. What the actual fuck was this made of? )"
    show dad predatory at right_small
    with dissolve
    dad_says "the more you stay in this position, the more i get turned on. You know that right? "
    show dad manipulative at right_small
    with dissolve
    dad_says "Dont blame me for what happens next, you are the one putting yourself in this position. "
    show madd anxious at left_small
    with dissolve
    x "(I had to finish this and get out before anything worse happened...)"
    show madd nervous at left_small
    with dissolve
    x "I'll be done and out of your way in a second, dad."
    show madd distressed at left_small
    with dissolve
    x "(I scrubbed like my life depended on it, practically grinding the rag into the floor. I was desperate to finish and get the hell out of this position. )"
    show dad dominant at right_small
    with dissolve
    dad_says "That's it, I am not going to wait any longer"
    show madd horrified at left_small
    with dissolve
    x "(I gulped, knowing exactly what he meant by that. I just knew whatever he was going to do next was not worth the 100 dollars I was getting paid for this. )"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_spanking
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd shocked at left_small
    with dissolve
    x "(suddenly , i felt a rough hand right above my hip area)"
    show dad coercive at right_small
    with dissolve
    dad_says "What's taking so long Maddie? "
    show madd horrified at left_small
    with dissolve
    x "(I looked back at him , he was almost climbing on top of me, his hand was right above my hip, and i could see the lust in his eyes. )"
    show madd paralyzed at left_small
    with dissolve
    x "(I didnt say a word, knowing it would only make things worse. )"
    show madd distressed at left_small
    with dissolve
    x "(I saw him raise his hand and then drop it down hard on my butt, making me yelp in pain. )"
    show madd anxious at left_small
    with dissolve
    x "(Immediately i turned back in hopes to finish cleaning it up so i could escape .)"
    show madd trembling at left_small
    with dissolve
    x "(Each spank made my whole body jolt — pain and deep humiliation twisting together. )"
    show madd violated at left_small
    with dissolve
    x "(After multiple spanks , his hand remained on my butt, and he started rubbing it, as if trying to soothe the pain. )"
    show dad cruel at right_small
    with dissolve
    dad_says " You are absolutely useless arent you daughter? But luckily you have good body that no man can resist. "
    show madd self loathing at left_small
    with dissolve
    x "(Hearing those words coming from my own father made me feel sick to my stomach. I wanted to cry, but i was too humiliated to even let out a sob. )"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_licking_butt
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd shocked at left_small
    with dissolve
    x "(Right then i felt a bite on my butt, and i froze in shock. )"
    show dad lecherous at right_small
    with dissolve
    dad_says "God you smell so good when you are all sweaty from cleaning. "
    show madd horrified at left_small
    with dissolve
    x "(It  was my dad kissing and licking the shorts that i was wearing, right on my butt. )"
    show madd nauseated at left_small
    with dissolve
    x "(With his teeth and tongue, he was moving the shorts out of the way and licking my bare skin. I could feel his hot breath on my skin, and it made me want to vomit. )"
    show madd violated at left_small
    with dissolve
    x "(After moving my shorts with his tongue for a while, at least 70 percent of my butt was exposed)"
    show madd overwhelmed at left_small
    with dissolve
    x "(I felt his warm saliva dripping down my skin, and I wanted to scream. )"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_licking_butt_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd trembling at left_small
    with dissolve
    x "(His hands landed on my butt with a firm grip, and he started squeezing and groping my butt cheeks as he continued to lick and kiss the skin near my butt .)"
    show madd distressed at left_small
    with dissolve
    x "(My entire frame shook with fear, disgust, and humiliation, my mind a total mess and sweat pouring off me. )"
    show madd horrified at left_small
    with dissolve
    x "(The cleaning spot was long forgotten; all I could do was try to survive this nightmare.  )"
    show dad possessive at right_small
    with dissolve
    dad_says "I warned you. This is on you for keeping that ass up in my face."
    show dad hungry at right_small
    with dissolve
    dad_says "How the hell am I supposed to control myself with your ass right in my face like this?"
    dad_says "God, that fresh sweat scent has me completely feral."
    show madd violated at left_small
    with dissolve
    x "(This is completely fucked up. No father should ever speak to or touch his daughter this way.)"
    show dad sadistic at right_small
    with dissolve
    dad_says "I told you, to finish this up fast, but you took your sweet time and now i am horny as fuck. "
    show madd horrified at left_small
    with dissolve
    x "(Hearing those words felt like a sentencing . I knew this wont just end with him sniffing and licking my body )"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_licking_butt_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd violated at left_small
    with dissolve
    x "(With his teeth and tongue , he managed to move my shorts up now completely exposing my butt)"
    show madd horrified at left_small
    with dissolve
    x "(He had direct access to my bare skin, and he started licking my buttcheeks and the area around my anus with such intensity that it made me want to scream. )"
    show madd disgusted at left_small
    with dissolve
    x "(his mouth was salivating directly on my butt and some of it seeped through the cracks of my butt cheeks and directly onto my asshole, making me feel even more violated and disgusted. )"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_licking_butt_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd overwhelmed at left_small
    with dissolve
    x "(all the gloves were off now, he was no longer hiding his intentions, and he was dropping his saliva all over my butt and spreading it around with his tongue)"
    show madd distressed at left_small
    with dissolve
    x "(Every time he licked my butt, I could feel the wetness and the heat of his tongue on my skin )"
    show madd violated at left_small
    with dissolve
    x "Dad...you should not be doing this..."
    x "I am your step daughter dad..."
    show madd paralyzed at left_small
    with dissolve
    x "(He didnt reply back to me, he just kept licking and groping my butt, completely ignoring my protests. )"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_licking_butt_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    with dissolve
    x "(Now his tongue was moving dangerously close to my asshole, please dont let him go there...Not that area...Please... )"
    show madd distressed at left_small
    with dissolve
    x "Please...dad...not there... "
    x "Why are you licking me there... "
    show madd paralyzed at left_small
    with dissolve
    x "(He was like an animal who had his natural instincts taking over, he was no longer in control of himself, his tongue was moving all over my butt, )"
    show madd overwhelmed at left_small
    with dissolve
    x "(his wet tongue would go up and down my buttcrack , landing near my asshole only for a second almost as if he was testing the waters, but it was enough to make me feel like I was in a nightmare that I couldn't wake up from. )"
    show dad hungry at right_small
    with dissolve
    dad_says "How am I supposed to stop when my face is buried in your sweaty, perfect ass? "
    show dad manipulative at right_small
    with dissolve
    dad_says "After all that hard cleaning, the least I can do is savor your body and offer you some relief. "
    show madd violated at left_small
    with dissolve
    x "(There's zero relief here. This is nothing but sick violation and abuse.)"
    show madd determined at left_small
    with dissolve
    x "(I had to speak up and try to stop him, I had to...otherwise he might just get bolder and do even worse things to me. )"
    x "This is not some sort of relief dad, this is abuse. You dont fucking have the right to do this to me. "
    show madd hopeful at left_small
    with dissolve
    x "(Hearing those words he finally stopped licking my butt my shorts returned to their normal position. )"
    show madd trembling at left_small
    with dissolve
    x "(Did it actually work? Will he actually stop? I was still trembling with fear and disgust, but at least for now, he had stopped his assault on my body. )"
    show dad cruel at right_small
    with dissolve
    dad_says "I was being nice to you and this is how you repay me? Fine I will treat you like the bitch you are ."
    show madd shocked at left_small
    with dissolve
    x "(Huh)"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    with dissolve
    x "(Before I could even react, he climbed on top of me, his full weight crushing my back as he pinned me to the floor.)"
    show dad dominant at right_small
    with dissolve
    dad_says "Finish Cleaning fast , now you have other things to clean up for me. "
    show madd distressed at left_small
    with dissolve
    x "(His heavy belly rested on my hips as his hands locked around my waist, holding me in place )"
    show dad sadistic at right_small
    with dissolve
    dad_says "I thought licking a girl was something only gentlemen did but i guess you are not a lady, you are just a dirty bitch who deserves to be treated like a piece of meat. "
    dad_says "If that is the case, I will treat you like you want to be treated. "
    show madd horrified at left_small
    with dissolve
    x "(oh god, What the fuck did i get myself into? This is not just some weird fantasy, this is real life, and my step father is on top of me)"
    show madd distressed at left_small
    with dissolve
    x "I ..I didnt mean it that way , its just that you are my step father and you shouldnt be doing this to me. With me.. "
    show dad controlling at right_small
    with dissolve
    dad_says "Shh.. little bitch , you said what you wanted . There is no going back now. "
    show madd paralyzed at left_small
    with dissolve
    x "(I stopped cleaning all together and just stood there frozen in fear, am i responsible for what is happening to me? )"
    show madd horrified at left_small
    with dissolve
    x "(I heard unzipping sounds, and i knew what was coming next. )"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd trembling at left_small
    with dissolve
    x "(i heard the sound of his belt being unbuckled, somehow he managed to remove his pants without getting off of me)"
    show madd anxious at left_small
    with dissolve
    x "(No heat or smell yet, so his dick was still tucked away… but I knew it wouldn't stay that way for long.)"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd confused at left_small
    with dissolve
    x "(Suddenly the weight on my back shifted, huh was he letting me up ?  )"
    show madd horrified at left_small
    with dissolve
    x "(My hopes  were quickly crushed as i felt some hard object pressing down on the back of my head )"
    x "(The rotten smell of his feet suddenly filled my nose as I realized in horror his foot was pinning my head.)"
    show madd distressed at left_small
    with dissolve
    x "(His foot pressed down with more force, a clear show of control, as sweat from his foot ran across my skin. )"
    show madd helpless at left_small
    with dissolve
    x "I ...I'm sorry dad"
    show dad authoritative at right_small
    with dissolve
    dad_says "No no need to apologize, its my mistake for not making it clear enough"
    show dad possessive at right_small
    with dissolve
    dad_says " That dirty bitches like you are property of their fathers. Now I wont get out of this position until i am done with you. "
    show madd resigned at left_small
    with dissolve
    x "(My head was now touching the floor with his foot still pressing down on it, his crotch was directly in contact with my butt. I could feel it through my shorts)"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    with dissolve
    x "(He was now pushing my head even harder my foot was already touching the floor causing my head excruciating pain, and i could feel his crotch grinding against my butt with every movement he made)"
    show madd helpless at left_small
    with dissolve
    x "I..Sorry dad. I will be better.."
    x "(He continued pushing me down . words had no effect on him )"
    x "Please...i will be grateful..."
    show madd violated at left_small
    with dissolve
    x "(The smell of his feet was getting stronger and stronger , it was filling my nostrils but i couldnt move my head away from it, i was trapped in this position with no way out. )"
    show madd nauseated at left_small
    with dissolve
    x "(As he was pushing it down it got offbalance and his foot slipped off the back of my head and directly onto my face as I came in contact with  it i was directly inhaling the smell of his feet )"
    show dad mocking at right_small
    with dissolve
    dad_says "You should be grateful to daddy, he lets you smell his feet and gives you the honor of being his little bitch. "
    show madd self loathing at left_small
    with dissolve
    x "(The humiliation was total: his foot smothering my face while I inhaled his sweat and felt him grinding on me. )"
    show madd resigned at left_small
    with dissolve
    x "Yes...dad...thank you for letting me smell your feet..."
    x "(I lied through my teeth, I was not grateful at all, but that made him stop pushing his foot down on my head)"
    show dad dominant at right_small
    with dissolve
    dad_says "Good girl , now you are learning your place. "
    show dad sadistic at right_small
    with dissolve
    dad_says "Lets get your clothes off so you can serve me like a proper slave. "
    show madd horrified at left_small
    with dissolve
    x "(Before i knew it, he ripped off my shorts leaving me completely exposed from the waist down)"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    with dissolve
    x "(I was butt naked with my butt raised in the air towards my dad with his foot on my head, and his crotch grinding against my bare skin. )"
    show madd resigned at left_small
    with dissolve
    x "(I knew what was next, yet I couldn't risk stopping him. I could only endure and pray it would finish fast. )"
    show madd trembling at left_small
    with dissolve
    x "(He started thrusting his hips against my butt, and I could feel the heat and the wetness of his dick against my skin. )"
    show dad possessive at right_small
    with dissolve
    dad_says "Now this is how slaves like you are supposed to be treated. It was a privileg for slaves to get their masters dick inside them "
    show madd horrified at left_small
    with dissolve
    x "(He says those words as i hear the stretch of a fabric , he was pulling down his underwear )"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_dck_out
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd overwhelmed at left_small
    with dissolve
    x "(As soon as he pulled out it i felt a wave of panic wash over me, the temperature near my butt raised significantly, and the smell of his dick filled the air)"
    show madd trembling at left_small
    with dissolve
    x "(he was pressing it to the side of  my buttcheeks and rubbing it against my skin, teasing me with the sensation of his cock against my body)"
    show dad lustful at right_small
    with dissolve
    dad_says "You feel that Maddie? You will have it inside you soon  "
    show dad dominant at right_small
    with dissolve
    dad_says "Better be a good slave and love what your master is going to do"
    show madd anxious at left_small
    with dissolve
    x "(i clenched my fists and tried to focus on anything other than the sensation of his dick against my skin, but it was impossible to ignore. )"
    show madd horrified at left_small
    with dissolve
    x "(I shivered with a mix of fear, disgust, and humiliation as i prepared myself for what comes next. )"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_pussy   
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    with dissolve
    x "(His dick glided across my skin before finally forcing its way inside.)"
    show dad cruel at right_small
    with dissolve
    dad_says "That's right, this is what you deserve ..No mercy for ungrateful bitches like you. "
    show madd horrified at left_small
    with dissolve
    x "(The moment he entered me, pain and raw discomfort flooded every nerve, and before I could even gasp he was already pounding me with savage force )"
    x "(Oh god… my own dad's cock is inside me… the man who raised me is stretching his daughter's pussy right now. This is the most disgusting, forbidden sin imaginable and my body isn't even rejecting it.)"

    show madd overwhelmed at left_small
    with dissolve
    x "(His foot crushed my face harder with every savage thrust while his hand dug into my back, pinning me down as he fucked me mercilessly.)"
    x "(the smell of his feet assaulting my senses, the sound of his thrusts against my body echoing in my ears, i had become his plaything, his slave in every sense of the word. )"
    show madd broken at left_small
    with dissolve
    x "(The room filled with the sound of our bodies slapping together as painful moans escaped my mouth.)"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_pussy_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    with dissolve
    x "(I felt so full it was hard to breathe, like something huge had taken up all the space inside me.)"
    x "(The heat of his dick spreading inside me , its thick veins rubbing against the walls of my pussy, and the relentless pounding making me feel like i was being torn apart from the inside. )"
    show madd overwhelmed at left_small
    with dissolve
    x "(Everytime he would go deep inside me, and i would exhale a painful moan to release some of the pressure, he would pull out just enough to make it even more painful when he thrust back in. )"
    show dad mocking at right_small
    with dissolve
    dad_says "Your moans are music to my ears, that would be such a good wake up alarm for me."
    show dad sadistic at right_small
    with dissolve
    dad_says "I wish i could record you moaning for me and play it to remind you of your place as my little bitch. "
    show madd broken at left_small
    with dissolve
    x "(His words stung but what he was doing to me was far worse, I had my eyes shut tight, trying to block out the sensations and the sounds)"
    x "(Every savage thrust reminds me exactly who is raping me — my father. My mind is screaming in horror but my pussy keeps clenching around him like a desperate little incest slut. I'm being corrupted from the inside out and I can't stop it.)"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_pussy_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd processing at left_small
    with dissolve
    x "(slowly my body was getting used to the sensation of his dick inside me, and the pain was starting to subside a little bit but the mental anguish and humiliation was still overwhelming. )"
    show madd broken at left_small
    with dissolve
    x "(My voice turned into desperate, defeated cries once I understood this was my future , constant abuse from my own father. )"
    x "(My moans are turning into whoreish screams and I hate myself for it. My own father is turning me into his personal cumdump and my body is betraying me more with every thrust. How can I be getting this wet for my dad?)"
    show dad obsessed at right_small
    with dissolve
    dad_says "That's right daughter, your insides feel so good around my dick "
    show dad calculating at right_small
    with dissolve
    dad_says "Its starting to clamp down on me, I can tell your slutty body is enjoying this, even if you wont admit it. "
    show madd conflicted at left_small
    with dissolve
    x "(My moans turned into filthy, desperate screams against my will as my traitorous body betrayed me completely and my mind drowned in sick, unwanted ecstasy. )"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_pussy_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd helpless at left_small
    with dissolve
    x "(His assault on my body continued while i had little to no room to move, no words to say, and no way to escape. )"
    show dad delusional at right_small
    with dissolve
    dad_says "Imagine if you get pregnant from this, I would tell my offspring that this is how you were conceived, as a result of me pounding into you like the dirty bitch you are. "
    show madd nauseated at left_small
    with dissolve
    x "(The thought of getting pregnant from this made me want to vomit, how can any child live knowing that they were conceived from such a disgusting act? )"
    x "(The thought of my father impregnating me is absolutely detestable yet my pussy is throbbing harder at the idea of carrying his baby. My mind is breaking — I'm being involuntarily corrupted into wanting my own father's child.)"
    show dad dominant at right_small
    with dissolve
    dad_says "Actually this is exactly what im gonna do to you"
    show dad controlling at right_small
    with dissolve
    dad_says "I am gonna fuck you till i come at least twice in you while you are under me , smelling my feet and serving me like the good little bitch you are. "
    show madd broken at left_small
    with dissolve
    x "(Those words shattered the last scrap of resistance I had left. I was completely broken with nothing left to fight. )"
    show madd resigned at left_small
    with dissolve
    x "( I had to let him cum inside me, I had no choice, i prayed that i just dont get pregnant from this )"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_pussy_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    with dissolve
    x "(MMy resistance was slipping away and the terrifying realization hit me, this was going to be my life from now on.. I no longer recognized the voice coming from me; it belonged to someone completely obedient, a voice that was being shaped by the abuse I was enduring. )"
    show madd conflicted at left_small
    with dissolve
    x "(It was tired and broken, but it was also a voice that was starting to find pleasure in the pain, a voice that was starting to crave the sensations that my dad was giving me, even if I hated myself for it. )"
    show madd submissive nod at left_small
    with dissolve
    x "(For now it was still soft and hesitant, but i could feel my body giving in to him, his demands, his touch, his assault on my body. )"
    x "(My resistance is melting away against my will. I'm starting to crave the feeling of my father's cock owning me completely. This is the ultimate taboo and my body is surrendering faster than my mind can fight it.)"
    show dad lustful at right_small
    with dissolve
    dad_says " God you are so fucking tight around me, i am gonna enjoy fucking you like this."
    show madd overwhelmed at left_small
    with dissolve
    x "(With this he put his foot harder on my head, making my butt arch up even more, giving him better access to my pussy)"


    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_pussy_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd overwhelmed at left_small
    with dissolve
    x "(With my head against the floor and him getting deeper and deeper inside me, his balls started slapping against my skin thats when i knew he was all the way inside me )"
    show madd flustered at left_small
    with dissolve
    x "(It  was reaching depths that i didnt even know existed, it was filling me up completely, and i was starting to feel a mix of pleasure and pain that i had never felt before. )"
    show madd inheat at left_small
    with dissolve
    x "(AS his dick went to the deepest parts of my pussy, my moans became more feminine and desperate. As if a reset button was hit in my brain, and i was starting to enjoy the sensations that were overwhelming me. )"
    show dad smirk at right_small
    with dissolve
    dad_says "Heh, looks like someone had a change of heart"
    show dad sadistic at right_small
    with dissolve
    dad_says "Scream like the bitch you are, let everyone know that you are a slave to your daddy and you love it. "

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_pussy_7
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd inheat at left_small
    with dissolve
    x "(Something inside me had finally broken and I was completely submitting , what the hell is wrong with me? I was now moaning and screaming in pleasure)"
    show madd self loathing at left_small
    with dissolve
    x "(I couldn't believe his cruel words were turning me on — what was happening to me? )"
    show madd conflicted at left_small
    with dissolve
    x "(The sound of his balls slapping against my skin, the smell of his feet, the sensation of his dick filling me up, it was all becoming fuel for my body's twisted pleasure. )"
    x "(Something inside me has snapped and I'm moaning like a bitch for my own father's cock. I hate how good it feels — my neurons are being forced into loving the most depraved, incestuous act possible and I cant stop myself.)"
    show madd horrified at left_small
    with dissolve
    x "(No no no, this is not what I want)"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_pussy_8
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd inheat at left_small
    with dissolve
    x "(The sounds of our fleshes colliding got louder as he increased his pace, my moans were no longer contained, they were loud and desperate, echoing through the room as i was being used and abused by my dad. )"
    show dad possessive at right_small
    with dissolve
    dad_says "good slave, let the world know who you belong to"
    show dad calculating at right_small
    with dissolve
    dad_says "you know if your brother walks in on us, he will see you beneath me, smelling my feet, and getting pounded by me, and he will know that you are my little bitch. "
    show madd conflicted at left_small
    with dissolve
    x "(Imagining my brother seeing me like this made my heart jump, and I hated how it affected me .  I was now getting turned on by the thought of my brother seeing me like this, it was like my mind had been rewired to find pleasure in the most twisted and disgusting things. )"
    show madd self loathing at left_small
    with dissolve
    x "(Maybe it was because if he saw me like this, he would do the same to me, and i would have to endure this abuse more often, but for some reason, the thought of that was pleasure enducing to me. )"

    
    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_pussy_9
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad calculating at right_small
    with dissolve
    dad_says "Whoa did your pussy just clamp down on me? It just became tighter around me "
    show dad mocking at right_small
    with dissolve
    dad_says "Is it because i said your brother might see us? You are such a dirty bitch. You want to get abused by your own brother too dont you? "
    show madd conflicted at left_small
    with dissolve
    x "(I didnt respond back but my moans were indirectly answering his question )"
    show dad sadistic at right_small
    with dissolve
    dad_says "Maybe I will call your brother and we can both abuse you together, Is  that what you want? Dirty slut ?"
    show madd horrified at left_small
    with dissolve
    x "(NO stop ... every word he said was disgusting to my mind but my body was getting hotter and hotter )"
    show madd inheat at left_small
    with dissolve
    x "(My orgasm was racing toward me and I hated how badly my body craved it , what the fuck is wrong with me that my own father abuse can turn me on like this? )"
    show dad debased at right_small
    with dissolve
    dad_says "Maybe your brother and I will double penetrate your pussy and cum inside you at the same time, to see who's sperm is more potent"
    show madd self loathing at left_small
    with dissolve
    x "(What the fuck !!! why are these words having such an effect on me? I was getting so close to climaxing, and the thought of my brother being involved in this was making me even more turned on. )"
    x "(My mind is screaming that this is the sickest, most forbidden thing possible  my fathers dick is about to make me orgasm , yet my pussy is throbbing with need.)"
    
    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_pussy_10
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd salivating at left_small
    with dissolve
    x "( The moment arrived: his relentless pounding forced my pussy to squirt hard.)"
    show madd self loathing at left_small
    with dissolve
    x "(As his dick was in the way, my squuirt spread everywhere, it was like a fountain of pleasure that was uncontrollable, and it was a clear sign that i had reached my climax. )"
    show dad smirk at right_small
    with dissolve
    dad_says "Cumming already? nasty little bitch"
    show madd traumatized at left_small
    with dissolve
    x "(It was over, he now knows that he made me cum, and that was the final nail in the coffin for my submission to him. )"
    show madd broken at left_small
    with dissolve
    x "(No amount of words can describe the mix of emotions that were running through me at that moment, I was humiliated, disgusted, and yet there was a part of me that was also feeling pleasure from the sensations that were overwhelming me. )"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_pussy_11
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    with dissolve
    x "(Once I came, the sound of our bodies slapping together turned wet and filthy. It filled the room with a new level of depravity,)"
    show madd self loathing at left_small
    with dissolve
    x "(I just came from my own father's abuse… there is no taking that back, ever.)"
    show dad obsessed at right_small
    with dissolve
    dad_says "Heh i love this sound, the sound of sex between a father and his daughter. "
    show dad delusional at right_small
    with dissolve
    dad_says "That was an insane squirt , your body is screaming that it wants your father to breed you. "
    show madd conflicted at left_small
    with dissolve
    x "(Just few moments ago i was  barfing from the thought of getting pregnant from this, and now my body was craving it. )"
    show madd traumatized at left_small
    with dissolve
    x "(was it the foot on my head? The relentless pounding? The degrading words? I have no idea what exactly caused this change in me, but i was now craving to get impregnated by my dad, and that was a terrifying realization. )"
    show madd inheat at left_small
    with dissolve
    x "(The more i thought about those things the more i got excited and i realized i was about to climax again, i was getting so close to climaxing again, and the thought of getting pregnant from this was making it even more intense. )"
    show madd self loathing at left_small
    with dissolve
    x "(what the fuck , back to back orgasms from my dad's abuse? )"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_pussy_12
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd salivating at left_small
    with dissolve
    x "(And it happened again, this time it was more intense mentally but less squirting. With every squirt i was reaffirming my submission to him, and with every orgasm i was getting more and more addicted to the sensations that he was giving me. )"
    show madd broken at left_small
    with dissolve
    x "(I was now fully under his control, Even if he had removed his foot from my head, the mental image of it was still there , imprinting itself in my mind and making me crave it more and more. )"
    show dad smirk at right_small
    with dissolve
    dad_says "Eh? You came again? So soon? "
    show dad delusional at right_small
    with dissolve
    dad_says "Was it cuz I said you were begging to get impregnated by me? you want to get pregnant from your own father dont you? "
    show dad mocking at right_small
    with dissolve
    dad_says "Nasty bitch like you get turned on by abuse from your own family . Heh Good for me , i get such a fun slave to play with. "
    show madd traumatized at left_small
    with dissolve
    x "(The room was full of wet squelching sound produced by the fluids released from my body, and it being thrusted back into me by my dads cock. )"
    show madd broken at left_small
    with dissolve
    x "(It was like i was in a nightmare that ended up being a twisted fantasy that i was now living in)"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_pussy_13
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    with dissolve
    x "(He never slowed down, just kept hammering me while I lay there moaning and leaking.  )"
    x "(Every brutal thrust reminds me exactly who is inside me — my father. The shame burns hotter than the pleasure, but my body keeps clenching around him anyway.)"
    show madd inheat at left_small
    with dissolve
    x "(I was now fully inhaling the smell of his feet, as if my whole lungs were filled with it, and i was starting to feel like i was addicted to it)"
    show madd submissive nod at left_small
    with dissolve
    x "(I was beginning to crave being pinned under my dad, breathing his foot sweat while he used me like a free use toy. )"
    show dad excited at right_small
    with dissolve
    dad_says "Shit Maddie , looks like im gonna cum too "
    x "(This is the ultimate betrayal. The man who was supposed to protect me is now pounding me like an animal in hopes to impregnate me, and the worst part is how my pussy keeps getting wetter.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(With that he started thrusting even harder and faster, as i felt his cock getting harder and harder inside me, and his balls slapping against my skin with more force. )"
    show madd inheat at left_small
    with dissolve
    x "(I felt it throbbing inside me, and I knew he was getting close to climaxing, I was getting close to climaxing again too, and the thought of him cumming inside me was making it even more intense. )"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_pussy_14
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd salivating at left_small
    with dissolve
    x "(I felt his cock throb violently as he exploded deep inside me, and a sick wave of pleasure crashed through me the instant he started flooding my womb.. mixed with a deep sense of submission and obedience to him i started cumming again from being filled up by his load )"
    show dad dominant at right_small
    with dissolve
    dad_says "That's it Maddie , take it all in, let it fill you up "
    show dad obsessed at right_small
    with dissolve
    dad_says "Fuuuuck… I just flooded your womb, Maddie. That's Daddy's seed going straight into your fertile little cunt."
    show madd overwhelmed at left_small
    with dissolve
    x "(My fluid mixed with his cum creating a creamy mixture that was dripping down my thighs as he continued to thrust into me even after he came)"
    show madd horrified at left_small
    with dissolve
    x "(The horror slammed into me like a truck. He just came inside me… really came inside me. What if I actually get pregnant? What if his sperm is already swimming into my womb right now, making a baby with my own father? My life, my future, everything would be destroyed…)"
    show madd traumatized at left_small
    with dissolve
    x "(I felt sick to my stomach at the thought of carrying his child. The shame burned so deep I wanted to cry…)"
    show madd conflicted at left_small
    with dissolve
    x "(Yet my pussy kept twitching and squeezing around him, milking out even more of his cum like it wanted to keep every drop. Why the hell was my body reacting like this? The idea of being knocked up by him was disgusting… and it was making me even wetter.)"
    show madd inheat at left_small
    with dissolve
    x "(I couldn't hold back anymore. my moans were wild, loud, and full of need, if the moans could speak, they would be begging him to keep using me, to keep pounding into me, to keep filling me up with his cum till i get pregnant from him. )"
    show madd broken at left_small
    with dissolve
    x "(Oh god… I might already be pregnant. Right here, under his foot, with his cock still inside me. I'm going to be ruined forever because my own father just bred me and still i was moaning uncontrollably as if my life didnt just get destroyed.)"
    show madd self loathing at left_small
    with dissolve
    x "(I was ashamed of myself for loving this and thinking about getting pregnant from my own father )"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_pussy_15
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd inheat at left_small
    with dissolve
    x "(He kept cumming without pause, pumping load after load deep inside me, and my body was like a machine that inputed his cum and outputted more pleasure and more moans )"
    show madd overwhelmed at left_small
    with dissolve
    x "(I couldnt even keep track of how much cum he had shot into me, it was like a never ending stream of cum and in response my body too was climaxing again and again )"
    show dad calculating at right_small
    with dissolve
    dad_says "That's 4 maddie, thats how many times you have climbed from my abuse "
    show dad manipulative at right_small
    with dissolve
    dad_says "Perhaps you took so long to clean because you were waiting for me to take you like this? "
    show dad smirk at right_small
    with dissolve
    dad_says "When i asked if you were trying to seduce me , i was only joking, but now i am starting to think maybe you were not joking at all. "
    show madd broken at left_small
    with dissolve
    x "(At this point his degrading words were added fuel to my pleasure, cum was leaking out of me with every thrust, and with my squirt it was spreading everywhere, )"
    show madd submissive nod at left_small
    with dissolve
    x "(I could feel his thick white load around my pussy and on my thighs, and the smell of his cum mixed with the smell of his feet was filling the air and i started to take deep breaths of it)"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_pussy_16
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad possessive at right_small
    with dissolve
    dad_says "Look at that… your cunt is still twitching around my dick like it's trying to milk out every last drop. That's your new purpose now, Maddie. This hole only exists to take Daddy's seed."
    show madd broken at left_small
    with dissolve
    x "(Oh god… I could feel it. My pussy was still spasming and clenching around him even though I have climaxed so many times already. It was like my body had a mind of its own, greedily sucking at his cum like it was starving for more. The shame burned so hot in my chest I wanted to disappear.)"
    show madd traumatized at left_small
    with dissolve
    x "(My new purpose…? Just a hole for his seed? The words hit me like a slap. I was supposed to be his daughter, not… not this. Not a living cumdump whose only reason to exist was to let him breed me whenever he felt like it. Yet my pussy walls fluttered again at the thought )"
    show dad controlling at right_small
    with dissolve
    dad_says "You're going to walk around the house leaking me for the rest of the day. I want every step you take to remind you who owns this sloppy, cum stuffed pussy."
    show madd self loathing at left_small
    with dissolve
    x "(The thought of walking around the house like this with his thick, warm load slowly dripping down my thighs with every movement made my stomach twist.  My brother could walk past me in the hallway. And he would never know that under my shorts I was literally leaking my own father's cum like a used whore.)"
    show madd conflicted at left_small
    with dissolve
    x "(Every step would be a wet, sticky reminder. I could already imagine the disgusting squelch of his seed being pushed deeper inside me, or worse, sliding out and soaking into my shorts. My face burned with humiliation… but my clit throbbed anyway. Why the hell was my body getting excited at the idea of being marked and owned like this?)"
    show madd self loathing at left_small
    with dissolve
    x "(I'm disgusting. I'm actually getting wetter just picturing myself trying to act normal while his cum runs down my legs. I should be screaming, fighting, doing anything except lying here panting like a broken bitch who secretly loves being reduced to nothing but a cum-stuffed toy for her dad.)"
    show madd broken at left_small
    with dissolve
    x "(He was still buried inside me, his heavy dick twitching with the last weak spurts, and I could feel my pussy trying to milk him even harder, like it was afraid he would pull out and leave me empty. The mixture of our fluids was already leaking out around him, making a complete mess between my thighs.)"
    show madd resigned at left_small
    with dissolve
    x "(This is my life now, isn't it? Every time I clean this stupid room I'm going to end up bent over, face pressed into his sweaty foot, pussy stuffed and overflowing with his seed. And the worst part… a tiny, traitorous part of me is already wondering when he'll do it again.)"
    show dad dominant at right_small
    with dissolve
    dad_says "Time to try the other hold now , Maddie"
    show dad smirk at right_small
    with dissolve
    dad_says "I know you will not have any problem with that dear daughter"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_butt_16
    with dissolve 
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    with dissolve
    x "(He suddenly pulled his thick cock out with a wet pop and a huge flood of his cum poured from me splattering onto the floor between my knees. Before I could even gasp, he shoved the same cum drenched dick straight against my asshole and rammed it in with one savage thrust.)"
    show madd shocked at left_small
    with dissolve
    x "(Oh fuck The sudden stretch burned like fire as his thick, cum slick dick forced its way into my butt without any warning or mercy. My pussy was still gaping and drooling his load all over the floor, but he didn't care. He just used all that creamy mess as lube to spear straight into my tightest hole.)"
    show dad sadistic at right_small
    with dissolve
    dad_says "Fuuuuck… your asshole is even tighter than your cunt was, Maddie. It's gripping my cock like it never wants to let go."
    show dad dominant at right_small
    with dissolve
    dad_says "Feel that? Daddy's stretching your shithole wide open. Its almost as if your asshole is hugging its long lost friend."
    show madd overwhelmed at left_small
    with dissolve
    x "(His foot was still grinding my face into the carpet, forcing me to breathe nothing but his sweaty foot smell while he claimed my ass like it was his personal property. I couldn't even scream properly only broken, pathetic whimpers came out.)"
    show madd conflicted at left_small
    with dissolve
    x "(Why does it feel… good? My pussy is clenching on nothing, jealous that my butt is getting filled now. I'm leaking his seed everywhere and he's just using my other hole like a cheap toy.)"
    show madd inheat at left_small
    with dissolve
    x "(He's going so deep. I can feel his balls slapping against my dripping pussy with every thrust, smearing even more of his cum all over me. My butt is squeezing him so hard I can't stop it—like my body is begging him to ruin me completely.)"
    show madd self loathing at left_small
    with dissolve
    x "( I hate myself for thinking it but I want him to fill my ass too. I want both holes overflowing with his cum. I want to crawl around the house later with his load leaking from my pussy AND my butt, knowing I'm completely his.)"
    show madd submissive nod at left_small
    with dissolve
    x "( my body isnt even fighting anymore. It is autonomosly pushing my ass back against him like a desperate slut, moaning into his sole while my mind shatters even more.)"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_butt_17
    with dissolve 
    $ renpy.call_in_new_context("_hide_windows")
    show dad dominant at right_small
    with dissolve
    dad_says "Push that greedy ass back harder, Maddie. Show Daddy how desperate you are for my cock in your guts."
    show madd broken at left_small
    with dissolve
    x "(His words made my ass clench even harder around him. I was drooling onto his foot, completely broken, while he used my asshole.)"
    show madd submissive nod at left_small
    with dissolve
    x "(I hated that it felt so good. I couldn't stop grinding my ass back against him like a bitch in heat, grinding against his cock while his sweaty foot crushed my face. The smell of his foot mixed with the wet, sloppy sounds of my own ass getting destroyed was making my brain melt.)"
    show dad possessive at right_small
    with dissolve
    dad_says "I'm not stopping until I flood this shithole too. Both your holes are gonna be overflowing with my seed before I'm done with you."
    show madd resigned at left_small
    with dissolve
    x "(I knew they were not idle words and that he meant everything he said )"


    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_butt_18
    with dissolve 
    $ renpy.call_in_new_context("_hide_windows")

    show dad possessive at right_small
    with dissolve
    dad_says "Feel how deep I am? My balls are slapping your cum-leaking pussy while I wreck your guts. Both holes are mine now."
    show madd broken at left_small
    with dissolve
    x "(I'm drooling and moaning into his sweaty foot like a mindless animal. I hate how much I love this… but I can't stop pushing back. I need him to fill my ass. I need to feel completely owned.)"
    show madd traumatized at left_small
    with dissolve
    x "(The room echoed with the most depraved noises imaginable the wet, obscene squelch of his cum slick cock destroying my asshole. The loud, meaty slapping sound of his heavy balls smacking against my still-drooling pussy. My own broken, muffled moans vibrating against his sweaty foot. The carpet was already soaked beneath us.)"
    show madd horrified at left_small
    with dissolve
    x "(Every single wet squelch reminded me exactly what was happening — my own father had already pumped my womb full of his seed, and now he was destroying my asshole with the same cock that had probably just knocked me up. The thought hit me like lightning: I could already be pregnant with my dad's baby… and he was still using me like a cheap set of holes.)"
    show madd inheat at left_small
    with dissolve
    x "(The louder the sounds got, the wetter I became. That constant sound of his balls slapping against my cum-filled pussy was basically telling the whole room that Daddy was breeding his own daughter. And instead of feeling disgusted… my clit was throbbing harder than ever.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(His foot was covering my face and my neck as if my whole body was getting marked by some part of his body)"


    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_butt_19
    with dissolve 
    $ renpy.call_in_new_context("_hide_windows")

    $ brother_hears_madd_moan= True
    show madd broken at left_small
    with dissolve
    x "(There was no more resistant in my voice, my moans were exactly as my dad described . That of a bitch who just got creampied by her dad.)"
    show dad sadistic at right_small
    with dissolve
    dad_says "You sound so fucking broken. Your pussy is still leaking my load and now your asshole is squeezing me even tighter because you love it."
    show dad dominant at right_small
    with dissolve
    dad_says "Good girl. Moan louder while I breed your shithole. I want the whole house to hear what a pregnant anal slut you've become for Daddy."
    show madd self loathing at left_small
    with dissolve
    x "(Both holes were going to be dripping his load when I leave this room… and I could already be pregnant with my father's child.. The shame was overwhelming… yet I kept pushing my ass back onto him like I needed it more than air.)"
    show dad possessive at right_small
    with dissolve
    dad_says "This tight ring is pulsing around me like it's trying to pull me deeper. Your ass is learning its new job faster than your pussy ever did."

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_butt_20
    with dissolve 
    $ renpy.call_in_new_context("_hide_windows")

    show madd broken at left_small
    with dissolve
    x "(My own moans sounded alien to me — low, guttural, nothing like the girl I used to be. Every time he drove into my ass I made a new sound, one that screamed submission without any words left.)"
    show dad controlling at right_small
    with dissolve
    dad_says "I'm going to train this hole until it only feels right when it's wrapped around Daddy's cock. You're not allowed to feel empty anymore."
    show madd resigned at left_small
    with dissolve
    x "(The reality sank in deeper than his thrusts. My body was already adapting, gripping him like it never wanted him to leave. The heavy weight of his foot on my face made me feel like nothing more than furniture — a warm, breathing sex toy for him to use whenever he wanted.)"
    show madd traumatized at left_small
    with dissolve
    x "(I couldn't even remember what it felt like to be anything else. All I knew now was the burn in my ass, the taste of carpet and foot sweat on my tongue, and the sick, addictive need to keep giving him whatever hole he demanded next.)"


    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_butt_21
    with dissolve 
    $ renpy.call_in_new_context("_hide_windows")

    show madd overwhelmed at left_small
    with dissolve
    x "(He positions himself in such a way he used his leg as pivot to spread my buttcheeks and he continued exactly what he said he would.)"
    show dad debased at right_small
    with dissolve
    dad_says "That's right… keep moaning like the pathetic fuck-pet you are. From now on every drop of Daddy's sweat, spit, piss and cum is going straight into your body, Maddie."
    show dad perverted at right_small
    with dissolve
    dad_says "You're gonna wake up every morning with your face buried in my sweaty ass crack, tongue deep in my asshole cleaning me before I even take a piss."
    show madd nauseated at left_small
    with dissolve
    x "(Every single thing that comes out of his body… I'm supposed to take it all inside me? The thought made my stomach churn with pure disgust.)"
    x "(Everything that comes out of his body is disgusting and nasty of the higest tier espcially the words he spoke)"
    show madd resigned at left_small
    with dissolve
    x "(Is it because of my moans, is it because i squirted multiple times that he feels he has full autonomy over me ? )"
    show madd broken at left_small
    with dissolve
    x "(Regardless of what it is , i knew he expects me to do all those things now)"
    show dad perverted at right_small
    with dissolve
    dad_says "I'm gonna make you lick the sweat out of my armpits right before I go balls-deep in your ass. You'll choke on my stink and thank me for it."
    show dad debased at right_small
    with dissolve
    dad_says "After I finish flooding your guts you're licking my cock clean — every vein, every drop of cum and ass-juice mixed together. That's your new dessert."
    show madd nauseated at left_small
    with dissolve
    x "(Licking his armpits and then cleaning his cock right after it's been in my ass… I feel so gross and used I want to disappear.)"
    show madd self loathing at left_small
    with dissolve
    x "(Does he feel no shame in putting his degenerate thoughts to words?)"
    show dad perverted at right_small
    with dissolve
    dad_says "Your tongue is gonna be my personal toilet brush. Feet, armpits, balls, asshole — you're cleaning all of it every single day."
    show dad sadistic at right_small
    with dissolve
    dad_says "When I go balls-deep in your greedy pussy, I'm shoving my sweaty fucking foot straight into your mouth, Maddie. You'll suck on every toe, lick between them, and taste all the dirt and foot sweat while I stretch your guts wide open."
    show madd traumatized at left_small
    with dissolve
    x "(I know he's not joking… because right now his heavy, sweaty foot is already crushing my entire face into the carpet, smothering my nose and mouth with that exact rank foot smell while he's ballsdeep in my asshole. If he says he's going to force those same toes into my mouth next, he absolutely will.)"
    x "( I can already feel myself gagging and drooling around them, tongue sliding between each sweaty toe, tasting the dirt, toe-jam and foot sweat while he keeps pounding me without mercy.)"
    show madd broken at left_small
    with dissolve
    x "(The humiliation is so intense I feel like I could cry, but the fact that it's literally already happening makes it even worse. My life really is over… I'm going to be nothing but a foot-sucking, ass-stretched toy for him forever.)"
    show dad controlling at right_small
    with dissolve
    dad_says "As soon as you start the day you'll be gargling my morning piss while I sit my bare ass on your chest and use your throat like a urinal. You'll thank Daddy like the broken little piss rag you are."
    show madd broken at left_small
    with dissolve
    x "(He kept piling on the filth, each word more disgusting than the last, and the worst part was how my asshole kept clenching tighter around him with every new degradation.)"
    show madd helpless at left_small
    with dissolve
    x "(I'm completely helpless. He's turning me into his full-time, walking, breathing body slave…)"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_butt_22
    with dissolve 
    $ renpy.call_in_new_context("_hide_windows")

    show dad cruel at right_small
    with dissolve
    dad_says "Let me give you a hint of your life from now on "
    show madd horrified at left_small
    with dissolve
    x "(His hips snapped forward violently, turning the pace vicious as he tried to wreck my asshole completely.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(The wet, obscene sound of his hips crashing against my ass echoed through the room, louder and wetter than before. My broken moans turned into high pitched, guttural screams that I barely recognized as my own.)"
    show dad sadistic at right_small
    with dissolve
    dad_says "This is how hard I'm gonna wreck this shithole every single fucking day, Maddie. Morning, noon, and night  you'll be bent over or pinned under my foot getting your guts rearranged."
    show madd broken at left_small
    with dissolve
    x "(The room was filled with nothing but the loud, filthy sounds of him destroying my ass , wet skin slapping, my own desperate moans, and the constant squelch of his cum lubed cock slamming in and out of me.)"
    show madd resigned at left_small
    with dissolve
    x "(My voice cracked as I screamed into his foot, completely unable to hold back. Every brutal thrust made my mind spin. This is really going to be my life now… getting pounded this hard every single day.)"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_butt_23
    with dissolve 
    $ renpy.call_in_new_context("_hide_windows")

    show dad mocking at right_small
    with dissolve
    dad_says "Remember what you said before? That I shouldn't even be doing this to you?"
    show madd overwhelmed at left_small
    with dissolve
    x "(His hips suddenly slammed forward even harder, the brutal pace turning vicious as he started absolutely destroying my asshole with deep, punishing strokes.)"
    show dad mocking at right_small
    with dissolve
    dad_says "What were you saying before, huh? That I had no right to touch you? That I shouldn't even be licking your ass?"
    show dad cruel at right_small
    with dissolve
    dad_says "You called it abuse, remember? You begged me to stop when my tongue was barely grazing your butt."
    show madd traumatized at left_small
    with dissolve
    x "(The memory slammed into me, I really had fought him, told him he had no right, tried to stop him from even kissing my ass… and now here I was, screaming under his foot while he reamed me without mercy.)"
    show dad sadistic at right_small
    with dissolve
    dad_says "Look at you now, Maddie. Face crushed under my foot, asshole greedily swallowing every inch while you moan like a bitch in heat."
    show dad mocking at right_small
    with dissolve
    dad_says "One hard fuck and you went from a daughter disgusted by her dad to a drooling, cock loving whore who cant stop pushing back for more."
    show madd self loathing at left_small
    with dissolve
    x "(My cheeks burned with humiliation. He was throwing my own protests back in my face while he battered me senseless. I had been so sure I would never let him do this… and now I was the one desperately grinding against him, completely broken.)"

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_butt_24
    with dissolve 
    $ renpy.call_in_new_context("_hide_windows")

    show madd broken at left_small
    with dissolve
    x "(He deliberately slowed his thrusts again, dragging his thick cock almost all the way out before slamming back in with a vicious snap of his hips, clearly enjoying how my body jerked and twitched every time he toyed with me.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(The wet, filthy sounds grew even louder as he switched between torturously slow strokes and sudden, brutal pounds, keeping me completely off balance.)"
    show madd traumatized at left_small
    with dissolve
    x "(And that's when it came , the ultimate sign of my submission)"
    show dad dominant at right_small
    with dissolve
    dad_says "Beg for it, Maddie. Beg Daddy to cum in your asshole like the broken little cumdump you are."
    show dad controlling at right_small
    with dissolve
    dad_says "Say it loud and clear — 'Please Daddy, cum deep in my shithole. Fill your worthless daughter's guts with your hot load.' I want to hear you beg like you mean it."
    show madd horrified at left_small
    with dissolve
    x "(My heart slammed against my ribs. He wasn't just fucking me anymore , he was forcing me to beg for his cum out loud. If I said those words, there would be no more denial. No more telling myself I was only enduring this. It would be me openly pleading for my own step-father to pump his seed into my ass while his foot crushed my face.)"
    show madd trembling at left_small
    with dissolve
    x "(This single sentence would be like signing my life away in front of him. Once those words left my mouth, I would have officially surrendered everything. Every future morning, every night, every time he wanted to use me… I would have already begged for it. I would be admitting, willingly and loudly, that I belonged to him completely and forever.)"
    show madd broken at left_small
    with dissolve
    x "(The humiliation was suffocating. I could already picture myself months from now, still repeating the same desperate pleas while he used me like a living fleshlight except i would also be pregnant with his child. My dignity, my future, my entire identity all of it would vanish the second I obeyed. I would never be able to take it back.)"
    show madd helpless at left_small
    with dissolve
    x "(But his cock was still buried deep inside me, still throbbing, and his foot was still grinding my face into the carpet. I had nothing left. No fight, no pride, no escape. My body was already clenching around him, betraying me, silently begging even if my mind was screaming not to do it.)"
    show madd weeping at left_small
    with dissolve
    x "(I took a shaky, broken breath, tears stinging my eyes… and finally gave in.)"
    show madd submissive nod at left_small
    with dissolve
    x "P-Please Daddy… cum deep in my butt"
    x "I am just a worthless daughter who can only serve by letting dad cum inside her , so please cum inside me…"
    show madd traumatized at left_small
    with dissolve
    x "(The words tasted like poison, but the moment they left my mouth something inside me shattered completely. There was no going back now. I had just begged my dad to creampie my asshole… and I knew he was going to do exactly that.)"
    show dad excited at right_small
    with dissolve
    dad_says "That's what i wanted to hear !"
    show dad lustful at right_small
    with dissolve
    dad_says "I'm gonna cum in your ass you fucking slut"
    show madd broken at left_small
    with dissolve
    x "Please....cum in my ass dad..."

    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_butt_25
    with dissolve
    $ renpy.call_in_new_context("_hide_windows") 

    show madd overwhelmed at left_small
    with dissolve
    x "(His cock swelled violently inside my ass, the thick veins pulsing hard against my walls as the first powerful jet of cum exploded deep into my guts. It was hotter and thicker than the load he had pumped into my pussy earlier but much less in quantity, my asshole was eating it all up , barely letting any escape)"
    show madd broken at left_small
    with dissolve
    x "(I could feel every single rope shooting straight into my intestines while his foot kept my face pinned to the carpet. The wet, obscene squelching grew louder as his cum mixed with the earlier mess )"
    show dad obsessed at right_small
    with dissolve
    dad_says "Fuuuuck yes—take every drop in your asshole, you pathetic anal whore! Daddy's marking his property from the inside!"
    show dad possessive at right_small
    with dissolve
    dad_says "Feel that? That's me breeding your ass raw. Both your holes are now stuffed with my seed like the worthless cumdump you were always meant to be. This is what you get for talking back to me"
    show dad dominant at right_small
    with dissolve
    dad_says "This is what you get when you classify my love as abuse "
    show madd traumatized at left_small
    with dissolve
    x "(The shame crashed over me like a wave. He had already flooded my womb… and now he was pumping the second massive load straight into my ass. I was double creampied by my own dad, both holes overflowing with his cum at the same time. There was no coming back from this.)"
    show madd broken at left_small
    with dissolve
    x "(I could already imagine the disgusting mess I would be later , walking around leaking his thick load from my pussy and my asshole at the same time, the constant sticky reminder that I belonged to him completely. My future was gone. I was nothing but his personal cum toilet now.)"
    show dad controlling at right_small
    with dissolve
    dad_says "You're gonna carry my cum in both ends for the rest of the day… maybe even my baby in your belly. Say thank you, Maddie."
    show madd weeping at left_small
    with dissolve
    x "(My voice broke into a weak, shattered whimper as another thick spurt flooded my guts.)"
    show madd submissive nod at left_small
    with dissolve
    x "Th-thank you Daddy… for cumming in my ass..."


    scene scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_butt_26
    with dissolve 
    $ renpy.call_in_new_context("_hide_windows")

    show madd broken at left_small
    with dissolve
    x "(He didn't stop. Even after unloading deep in my guts he kept hammering into me with long, lazy, possessive strokes, using his own cum as fresh lube while my asshole made wet, sloppy, obscene noises around him.)"
    show madd helpless at left_small
    with dissolve
    x "(My body had gone totally limp. All that came out of me now were weak, shattered gasps with every thrust.. My throat was raw, my voice gone, my mind blank except for the overwhelming feeling of total defeat.)"
    show dad possessive at right_small
    with dissolve
    dad_says "You're mine now , Maddie "
    show madd traumatized at left_small
    with dissolve
    x "(I had completely surrendered. My free will, my pride, my entire future all of it vanished the second I begged him to fill my ass.. All that was left was this limp, cum stuffed body being lazily fucked under his foot like a living sex toy.)"
    show madd broken at left_small
    with dissolve
    x "(I could feel his thick load sloshing inside me with every slow thrust, some of it leaking out and mixing with the mess already dripping from my pussy. I was double creampied and completely broken, and the worst part was that a tiny, shattered piece of me already knew I would let him do this again tomorrow… and the day after… forever.)"
    show madd weeping at left_small
    with dissolve
    x "(My eyes fluttered, tears slipping down my cheeks as I lay there completely spent, unable to do anything but take it. This really was the end of me… and the beginning of my life as his permanent, filthy, cum filled slave.)"
    show madd resigned at left_small
    with dissolve
    x "(My eyes were tired and i finally passed out ...)"

    $ character_relations["dad"]["intimacy"] += 15
    $ character_relations["dad"]["lust"] = 0
    $ character_relations["dad"]["anger"] = 0 
    $ character_relations["dad"]["dominance"] += 10
    $ character_relations["dad"]["touched_madd"] += 5
    $ character_relations["dad"]["groped_madd"] += 5
    $ character_relations["dad"]["vaginal_sex"] += 1
    $ character_relations["dad"]["anal_sex"] += 1
    $ character_relations["dad"]["vaginal_creampie"] += 1
    $ character_relations["dad"]["anal_creampie"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ madd_willpower = max(0, madd_willpower - 50)
    $ journal_event_set_done("Dad", "Room Cleaning: Final Domination")
    call advance_time_and_check(minutes=180) from _call_advance_time_and_check_final_domination

    jump madd_wake_up_after_roughed_up





# knock on step father's door

label knock_step_father_room:
    show madd relieved at left_small
    with dissolve
    
    # Morning - Hear voices on zoom call
    if game_time.is_morning() and game_time.hour != 11:
        x "(I take a deep breath and approach Step Father's door.)"
        x "(But before I can knock, I hear voices coming from inside.)"
        show madd confused at left_small
        with dissolve
        x "(A male voice emanates from the computer speaker, mixed with his distinctive tone, all speaking in professional tone.)"
        show madd processing at left_small
        with dissolve 

        if  madd_interrupt_dad_meeting_count==2 and game_time.hour == 10 and (55 <= game_time.minute <= 59):
            x "(This is it. This is how I become free from morning to evening.)"
            show madd determined at left_small
            with dissolve
            x "(I can hear the meeting happening behind the door. His voice, the other voices, the same tired excuses playing out again.)"
            show madd focused at left_small
            with dissolve
            x "(I need to stay calm and think strategically.)"
            menu :
                "Open the door and interrupt the meeting":
                    if madd_willpower<30 :
                        x "(I feel my energy is super low. if i had to confront him i might not be able to resist)"
                        jump home_areas
                    if  character_relations["dad"]["intimacy"]<30:
                        x "(I am too scared to what might happen if do confront him.... I don't have enough intimacy with him to be able to handle the consequences of interrupting him.)"
                        jump home_areas
                    x "(I take a deep breath. This is risky, but I have to try.)"
                    show madd determined at left_small
                    with dissolve
                    x "(Last time was a failure but now I am prepared.)"
                    show madd hopeful at left_small
                    with dissolve
                    x "(Last time he violated me. His fingers, his spit in my mouth)"
                    show madd traumatized at left_small
                    with dissolve
                    x "(Rubbed his dirty feet on my face but now I am gonna stand up against him)"
                    show madd angry at left_small
                    with dissolve
                    x "(I reach for the door handle and push it open.)"
                    show madd focused at left_small
                    with dissolve
                    
                    jump madd_interrupt_dad_meeting_event_two
                "Let it be and leave":
                    x "(I can't do this. Too risky. He'd know it was me.)"
                    show madd resigned at left_small
                    with dissolve
                    jump home_areas
        elif dad_morning_knock_count == 0:
            if madd_willpower<10:
                x "(I feel my energy levels are super low. If i interrupt him now, I might not have the strength to deal with his anger.)"
                jump home_areas

            dad_says "Nothing to report on my end. "
            show dad calculating at right_small
            with dissolve
            x "(Is he... on a work meeting? During the morning?)"
            show madd hesitant at left_small
            with dissolve
            x "(I don't want to interrupt him while he's speaking with his colleagues. It would only invite his anger.)"
            show madd nervous at left_small
            with dissolve
            x "(I decide it's best to leave and return later when he's finished.)"
            $ dad_morning_knock_count += 1
            $ journal_event_set_done("Dad", "Morning Eavesdrop")
            $ journal_event_show("Dad", "Dad's Work Secret")
            $ journal_event_show("Dad", "Morning Knock at 11")
            
            call advance_time_and_check(minutes=30) from _call_advance_time_and_check_45
            $ madd_willpower = max(0,madd_willpower-10)
            jump home_areas
        
        elif dad_morning_knock_count == 1:
            if madd_willpower<10:
                x "(I feel my energy levels are super low. If i interrupt him now, I might not have the strength to deal with his anger.)"
                jump home_areas

            dad_says " Nothing has changed on my end."
            show dad dominant at right_small
            with dissolve
            x "(Again?? Does he have anything to report at all? )"
            show madd angry at left_small
            with dissolve
            x "(What exactly is his job? He's always on these calls, yet I never see him actually working.)"
            show madd processing at left_small
            with dissolve
            x "(I can hear the frustration in the other person's voice through the speaker, but I don't stay to listen further.)"
            show madd resigned at left_small
            with dissolve
            x "(I'll return later to check on him again.)"
            $ dad_morning_knock_count += 1
            call advance_time_and_check(minutes=30) from _call_advance_time_and_check_46
            $ madd_willpower = max(0,madd_willpower-10)
            jump home_areas
        
        elif dad_morning_knock_count == 2 and madd_interrupt_dad_meeting_count==0:
    
            x "(I pause outside the door and listen carefully. The voices are clearer now. Someone is talking about recent company policy about returning to office.)"
            show madd processing at left_small
            with dissolve
            x "(I decide to wait a moment, hoping to catch something useful in this conversation.)"
            show madd determined at left_small
            with dissolve

            # Advance time to 10:59 AM
            $ minutes_until_1059 = (10 - game_time.hour) * 60 + (59 - game_time.minute)
            call advance_time_and_check(minutes=minutes_until_1059) from _call_advance_time_and_check_47
            
            x "(I press my ear against the door to hear better. The conversation has intensified. They are asking him when Can he return to the office !)"
            show madd focused at left_small
            with dissolve
            show dad manipulative at right_small
            with dissolve
            dad_says "...but you know I can't come to the office. My daughter isn't stable after her mom died, so I have to stay at home to take care of her."
            x "(He uses me as an excuse to not work?)"
            show madd angry at left_small
            with dissolve
            x "(This is such bullshit. He's clearly just avoiding going to the office.)"
            show madd conflicted at left_small
            with dissolve
            x "(But I'm fine. I'm managing. And they need to know that.)"
            show madd determined at left_small
            with dissolve
            x "(If they saw me in that meeting, they might realize he isn't necessary to be at home.)"
            show madd hopeful at left_small
            with dissolve
            x "(Maybe they'd realize he has just been using mom's death as an excuse. Maybe they'd call him in to the office.)"
            show madd hopeful at left_small
            with dissolve
            x "(That would give me freedom. Mornings to evenings without him here.)"
            show madd conflicted at left_small
            with dissolve
            
            menu:
                "Open the door and interrupt the meeting":
                    if madd_willpower<30:
                        x "(I feel my energy is super low. if i had to confront him i mightn ot be able to resist)"
                        jump home_areas

                    $dad_morning_knock_count += 1
                    x "(I take a deep breath. This is risky, but I have to try.)"
                    show madd determined at left_small
                    with dissolve
                    x "(I reach for the door handle and push it open.)"
                    show madd nervous at left_small
                    with dissolve
                    
                    if madd_interrupt_dad_meeting_count == 0:
                        $ madd_interrupt_dad_meeting_count += 1
                        jump madd_interrupt_dad_meeting_event

                
                "Let it be and leave":
                    x "(I can't do this. Too risky. He'd know it was me.)"
                    show madd resigned at left_small
                    with dissolve
                    x "(I turn away from the door and head back downstairs.)"
                    call advance_time_and_check(minutes=15) from _call_advance_time_and_check_48
                    jump home_areas
        elif dad_morning_knock_count == 2 and madd_interrupt_dad_meeting_count==1:
            if madd_willpower<30:
                x "(I feel my energy is super low. if i had to confront him i mightn ot be able to resist)"
                jump home_areas

            x "(I stand outside his door again, listening to the familiar pattern of his voice on the speaker.)"
            show madd nervous at left_small
            with dissolve
            x "(He's in another meeting. This is becoming routine. He's always on these calls.)"
            show madd processing at left_small
            with dissolve
            $ minutes_until_1059 = (10 - game_time.hour) * 60 + (59 - game_time.minute)
            call advance_time_and_check(minutes=minutes_until_1059) from _call_advance_time_and_check_49
            
            x "(Then it happened again!)"
            show madd determined at left_small
            with dissolve
            x "(I hear voices on speaker they are asking him when will he be able to join the office in person)"
            show madd processing at left_small
            with dissolve
            show dad controlling at right_small
            with dissolve
            dad_says "...how many times do i have to explain this. My daughter is sick and I have to stay at home to take care of her"
            x "(I hear the voices on speaker say something about higher management wanting everyone in office)"
            show madd processing at left_small
            with dissolve
            show dad delusional at right_small
            with dissolve
            dad_says "...I understand that but my situation is different. I am a caring father."
            dad_says " I can't just abandon my daughter in her time of need"
            x "(Loving father my ass, caring father would not spit in his daughter's mouth)"
            show madd disgusted at left_small
            with dissolve
            x "(Then I remembered what happened last time)"
            show madd traumatized at left_small
            with dissolve
            x "(and a shiver ran down my spine)"
            show madd trembling at left_small
            with dissolve
            x "(snap out of it Madd!)"
            show madd focused at left_small
            with dissolve
            x "(If I track the time they ask this question to him. Maybe I can use the timings to interrupt the zoom meeting.)"
            show madd determined at left_small
            with dissolve
            x "(This time I have to be sure that I time it right otherwise I don't know what he will do to me)"
            show madd anxious at left_small
            with dissolve
            x "(I was ashamed of the fact that some part of me was excited thinking about what the next punishment would be.)"
            show madd conflicted at left_small
            with dissolve
            x "(It seems this happens around 10:59 so I have to be ready between 10:55 to 10:58 to enter)"
            show madd determined at left_small
            with dissolve
            
            x "(Yes, I am starting to believe I can pull this off. If I do he might do worse things to me for a day)"
            show madd conflicted at left_small
            with dissolve
            x "(But I will be free of his looming shadow from morning to evening.)"
            show madd hopeful at left_small
            with dissolve
            x "(It's well worth it!)"
            show madd determined at left_small
            with dissolve
            x "(Alright, next time I need to be here between 10:55 and 10:58 and I will taste some freedom hopefully)"
            show madd hopeful at left_small
            with dissolve
            x "(Oh shit he's getting up from his chair.)"
            show madd shocked at left_small
            with dissolve
            x "(If I start moving away now he will hear the floor creaking.)"
            show madd traumatized at left_small
            with dissolve
            x "(If he knows that I have figured out the timing of his meeting ending, he would start locking his door.)"
            show madd violated at left_small
            with dissolve
            x "(I can't let that happen)"
            show madd determined at left_small
            with dissolve
            x "(Only thing I can do is knock now and act as if I just came here.)"
            show madd focused at left_small
            with dissolve
            $ madd_interrupt_dad_meeting_count += 1
            $ dad_morning_knock_count += 1
            $ journal_event_set_done("Dad", "Cracking His Schedule")
            $ journal_event_show("Dad", "Second Interruption")
            $ advance_game_time( minutes=5)
            jump dad_morning_knock_at_11_event
        else :
            show madd happy at left_small
            with dissolve
            x "(I wait outside the door, my heart pounding in my chest.)"
            x "(I cant hear anything)"
            call advance_time_and_check(minutes=5) from _call_advance_time_and_check_50
            jump home_areas

    
    # 11:00 AM - Door opens unexpectedly
    elif game_time.hour == 11:
        if character_relations["dad"]["lust"] >= 10 and character_relations["dad"]["intimacy"]>=30:
            jump dad_morning_knock_at_11_event
        elif character_relations["dad"]["intimacy"]<30:
            x "I....I dont know what he'll do to me right after his work. I'm not prepared for it"
            x "He must be stressed out , I dont wanna be near him when that happens "
            jump home_areas
        else:
            x "(I knock on the door, but I hear nothing.)"
            show madd confused at left_small
            with dissolve
            x "(No movement. No response. He must be sleeping or too absorbed in whatever he's doing.)"
            show madd resigned at left_small
            with dissolve
            x "(I turn back and head to the lobby.)"
            jump home_areas
        

    
    # Afternoon
    elif game_time.is_afternoon():
        x "(I take a deep breath and knock on Step Father's door.)"
        show madd hesitant at left_small
        with dissolve
        dad_says "Come in."
        show dad at right_small
        with dissolve
        jump step_parent_room_scene
    
    # Evening
    elif game_time.is_evening():
        # 18:00-18:59 - He's not there
        if game_time.hour == 18:
            x "(I take a deep breath and knock on Step Father's door.)"
            show madd hesitant at left_small
            with dissolve
            x "(I knock and receive no response.)"
            show madd confused at left_small
            with dissolve
            x "(He's not here. I should go back to the lobby.)"
            jump home_areas
        # 19:00-19:59 - He tells you to come in
        else:
            x "(I take a deep breath and knock on Step Father's door.)"
            show madd hesitant at left_small
            with dissolve
            dad_says "Come in."
            show dad creepy at right_small
            with dissolve
            jump step_parent_room_scene
    
    # Night - Door slightly open with menu choice
    elif game_time.is_night():

        scene scene_night_dad_room_slightly_open
        with fade
        show madd nervous at left_small
        with dissolve
        x "(As I approach Step Father's door, I notice it's slightly ajar.)"
        show madd conflicted at left_small
        with dissolve
        x "(A sliver of light spills out from the crack, and I can see dad sleeping.)"
        show madd hesitant at left_small
        with dissolve
        x "(What do I do?)"
        show madd conflicted at left_small
        with dissolve
        menu:
            "Push the door further and enter":
                x "(I take a breath and gently push the door open wider.)"
                show madd determined at left_small
                with dissolve
                jump step_parent_room_scene_night_enter
            "Leave it be and come back later":
                x "(I decide it's better not to intrude. Whatever he's doing, I'll come back when it's more appropriate.)"
                show madd relieved at left_small
                with dissolve
                x "(I turn away from his door and head back down the hallway.)"
                jump home_areas


label madd_interrupt_dad_meeting_event:
    scene scene_madd_dad_meeting_interrupt
    with dissolve
    show madd determined at left_small
    with dissolve
    
    x "(I step into the room, my heart pounding in my chest.)"
    x "(The door clicks shut behind me - there's no turning back now.)"
    x "(My presence immediately catches dad's attention. I can see him tense up in his chair.)"
    x "(He immediately looks in my direction, and I can practically feel the weight of his stare.)"
    show dad what at right_small
    with dissolve
    show dad what at right_small
    with dissolve
    
    
    scene scene_madd_interrupt_dad_meeting_event_step_in
    with fade
    
    dad_thinks "(What is she doing here?)"
    show dad bonamic at right_small
    with dissolve
    dad_thinks "(She knows better than to interrupt me during a work meeting.)"
    x "(I swallow hard, my throat suddenly dry.)"
    x "(I can feel my palms getting sweaty. Stay calm, I tell myself. Just breathe.)"
    x "(I clear my throat, trying to steady my voice, trying to project confidence I don't feel.)"
    show madd nervous at left_small
    with dissolve
    x "(I just need to get near him so they can see me in the zoom call.)"
    x "(If his coworkers see me healthy and fine, they'll tell him to come back to work.)"
    x "(He won't have an excuse to stay home anymore.)"
    dad_says "Maddie? What are you doing here?"
    show dad bonamic at right_small
    with dissolve
    x "(His voice has that edge to it - the one that usually means trouble.)"
    x "(But I'm committed now. I have to see this through.)"
    x "(I take a deep breath, trying to keep my composure, forcing myself to look natural.)"
    show madd determined at left_small
    with dissolve
    x "(I need to make this convincing. I need them to believe that he doesn't need to be here.)"
    x "(That I'm completely fine. That there's no reason for him to take time off.)"
    x "(I started walking towards him, each step feeling heavier than the last.)"
    x "(As I approached near him, I could see his PC screen more clearly.)"

    
    scene scene_madd_interrupt_dad_meeting_event_step_in_madd_trying_to_get_in_frame
    with fade
    
    x "(I saw a couple of people on the screen - professional looking, in what seemed like an office setting.)"
    show madd hopeful at left_small
    with dissolve
    x "(Perfect. That's it, enough people to witness that he is not needed at home.)"
    x "(If they see me up and about, acting normal, they'll wonder why he's taking time off.)"
    x "(As I got close enough to enter the zoom frame, I prepared my voice.)"
    x "(I had to make it believable that I was healthy, that everything was normal.)"
    x "(I forced brightness into my tone, like nothing was wrong.)"
    x "Hey dad, can you take me to basketball today? Now that I'm fully healed and all?"
    show madd anxious at left_small
    with dissolve
    dad_thinks "(What is she talking about?)"
    dad_thinks "(Basketball? Fully healed?)"
    x "(I looked over to the monitor to see their reactions, waiting for the shock, the questions.)"
    x "(Waiting for them to ask why he'd said I was unstable if I'm standing here asking about basketball.)"
    show madd horrified at left_small
    with dissolve
    x "(But to my shock no one even noticed it.)"
    x "(No one looked surprised. No one looked at all.)"
    x "(The people on screen just continued whatever they were doing, completely oblivious.)"
    show dad calculating at right_small
    with dissolve
    dad_thinks "(Why is she looking at the zoom screen?)"
    show dad what at right_small
    with dissolve
    dad_thinks "(Wait... she's trying to get in frame...)"
    show dad angry at right_small
    with dissolve
    dad_thinks "(AH! This bitch is trying to sabotage me!)"
    show dad cruel at right_small
    with dissolve
    dad_thinks "(She must have overheard me telling work about her 'condition'.)"
    show dad possessive at right_small
    with dissolve
    dad_thinks "(This might've worked too...)"
    show dad smirk at right_small
    with dissolve
    dad_thinks "(Good for me I turned my mic and video off as soon as my part was over.)"
    x "(Why is nothing happening? Why is no one shocked?)"
    x "(Why aren't they reacting to what I just said?)"
    show madd confused at left_small
    with dissolve
    x "(Then I noticed it. There was no light on the camera.)"
    x "(If the camera was on, it would show up with that small white LED light.)"
    x "(But it was dark. Completely dark.)"
    show madd trembling at left_small
    with dissolve
    x "(The realization hit me like a punch to the gut.)"
    x "(He's offline. The camera is off. Nobody heard me.)"


    scene scene_madd_interrupt_dad_meeting_event_step_in_dad_spanks_madd_close_meet
    with fade
    
    x "(Suddenly I felt it - a hand on my ass. As he exits the meeting )"
    x "(His hand suddenly clamps violently onto my bare ass, fingers digging hard into my flesh even through my shorts.)"
    show madd horrified at left_small
    with dissolve
    x "(I jolt hard, a sharp, disgusted gasp escaping me.)"
    x "(He was slowly running his hand over my butt while looking at me with this expression...)"
    x "(God, that look on his face. Like he knows exactly what I tried to do.)"
    show dad calculating at right_small
    with dissolve
    dad_thinks "(I get the picture. She must have heard that I told work she's been mentally unstable after losing her mom.)"
    show dad controlling at right_small
    with dissolve
    dad_thinks "(So she decided to enter and say all those things so that I would be called back to work...)"
    show dad cruel at right_small
    with dissolve
    dad_says "You stupid fucking cunt. You really thought you could sabotage me in front of my coworkers?"
    dad_says "Parading your worthless ass in here like some hero? You're nothing but a pathetic, desperate little bitch trying to get rid of me."
    show madd paralyzed at left_small
    with dissolve
    x "(His words hit me like a slap... calling me a stupid fucking cunt right to my face...)"
    x "(I feel so small and worthless... like I'm nothing but a pathetic girl who made a terrible mistake.)"
    x "(My plan backfired completely. He knows what I tried to do.)"
    x "(I can't move. I should pull away but my body won't respond.)"
    x "(Then I felt it - a huge, searing pain in my ass cheeks as he slaps it hard.)"
    x "(The sound echoes in the room, and I couldn't help but gasp.)"
    show madd distressed at left_small
    with dissolve
    x "(This is harder than he's ever spanked me before.)"
    x "(Tears spring to my eyes from the sharp, burning pain.)"
    show dad entitled at right_small
    with dissolve
    dad_thinks "(I keep treating her well, and this is how she rewards me.)"
    show dad angry at right_small
    with dissolve
    dad_thinks "(Trying to get me sent back to work. Trying to ruin my time with her.)"
    show dad wistful at right_small
    with dissolve
    dad_thinks "(She is not like her mother at all in that regard.)"
    show dad mourning at right_small
    with dissolve
    dad_thinks "(Her mother was always so grateful, so understanding...)"
    show dad calculating at right_small
    with dissolve
    dad_thinks "(Maybe this has been my problem. I have been looking at her thinking it's my dead wife.)"
    show dad delusional at right_small
    with dissolve
    dad_thinks "(But no... she's not her mother.)"
    show dad lustful at right_small
    with dissolve
    dad_thinks "(No, it's an upgrade.)"
    show dad hungry at right_small
    with dissolve
    dad_thinks "(A whole new woman, young and fresh... that I get to break.)"
    show dad obsessed at right_small
    with dissolve
    dad_thinks "(I get to mold her from scratch.)"
    show madd violated at left_small
    with dissolve
    x "(I feel him squeezing my buttcheeks through my shorts, his fingers digging in.)"
    x "(He's not letting go. His grip only tightens.)"
    x "(I can feel each individual finger pressed into my flesh.)"
    x "(He uses his hand to stretch my ass cheeks. First the left one - he pulls it to the left, spreading me.)"
    x "(Then the right one, pulling it in the opposite direction.)"
    x "(He's examining me, playing with me like I'm some kind of object.)"
    show madd traumatized at left_small
    with dissolve
    x "(My skin crawls with revulsion, every nerve screaming danger.)"
    
    show madd horrified at left_small
    with dissolve
    x "(The sickening feeling pools in my stomach, acidic and burning.)"


    scene scene_madd_interrupt_dad_meeting_event_step_in_dad_spanks_madd_tugging_shorts
    with fade

    x "(Then I feel it—his fingers, rough and insistent, tugging at the waistband of my shorts.)"
    show madd paralyzed at left_small
    with dissolve
    x "(My body locks up completely. Every muscle refuses to obey me.)"
    show dad dominant at right_small
    with dissolve
    dad_says "Now, now, just relax. This will be our little secret."
    show madd shocked at left_small
    with dissolve
    x "(In one brutal yank, he rips my shorts down past my hips, completely exposing my bare ass and pussy to the cold air.)"
    show madd traumatized at left_small
    with dissolve
    x "(I feel so disgusting… so exposed… I want to cover myself but I'm too scared to move.)"


    scene scene_madd_interrupt_dad_meeting_event_step_in_dad_spanks_madd_naked_ass
    with fade
    
    show madd trembling at left_small
    with dissolve
    x "(I am frozen solid, a statue of fear—unable to move, unable to scream, unable to breathe.)"
    dad_says "So you wanted to play basketball, huh? Let's see how well you can really play."
    
    show madd violated at left_small
    with dissolve
    x "(His hand is on my bare buttocks now, fingers spreading, groping, squeezing.)"
    x "(The warmth of his palm sears into my skin like a brand.)"
    scene scene_madd_interrupt_dad_meeting_event_step_in_dad_spanks_madd_close_meet_hand_on_ass
    with fade
    show madd distressed at left_small
    with dissolve
    x "(I can't speak. My throat has closed. Fear has stolen my voice completely.)"
    x "(What have I done? This was such a catastrophic mistake. I never should have come here.)"
    
    show madd horrified at left_small
    with dissolve

    scene scene_madd_interrupt_dad_meeting_event_step_in_dad_spanks_madd_close_meet_hand_on_ass_dad_stands_up
    x "(He stands up from his chair with deliberate slowness, one hand still possessively gripping my butt.)"
    x "(He looks at the monitor screen one more time and then he turns to face me.)"
    x "(That smile. That horrible, predatory smile spreads across his face.)"
    
    show dad predatory at right_small
    with dissolve
    dad_says "I see what you were doing. Trying to get me away from you."
    show dad controlling at right_small
    with dissolve
    dad_says "Now be a good girl and lift your arms."
    
    show madd resigned at left_small
    with dissolve
    x "(My arms tremble as I slowly raise them, puppet-like, obeying his command.)"
    x "(I know—I know—if I don't comply, things will spiral into something even worse.)"
    
    show madd violated at left_small
    with dissolve
    show dad obsessed at right_small
    with dissolve
    dad_thinks "(She's obeying. Good. The body remembers submission, even when the mind tries to resist.)"
    show dad manipulative at right_small
    with dissolve
    dad_thinks "(Soon the mind will follow. That's always how it works.)"
    x "(He removes his hand from my butt. I feel the loss of warmth before his fingers grip my t-shirt hem.)"
    x "(Slowly, torturously slowly, he lifts my shirt upward, exposing my bare midriff.)"
    x "(The fabric scrapes against my skin, each centimeter of exposure making me feel smaller.)"


    scene scene_madd_interrupt_dad_meeting_event_step_in_dad_spanks_madd_close_meet_lifting_shirt
    with fade   
    
    show madd broken at left_small
    with dissolve
    x "(I feel so naked, so vulnerable, even with the shirt still half-on.)"
    x "(This is so fundamentally wrong. Every fiber of my being screams it.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I can feel his hot hands on my sides, fingers tracing over my ribs, lingering on my waist.)"
    x "(I can smell coffee and something else, something sour and unwashed.)"
    
    show madd traumatized at left_small
    with dissolve
    x "(With one quick motion, he tears my shirt over my head, exposing my bare chest to the cold air.)"
    x "(My nipples harden involuntarily from the temperature change. I hate that my body responds.)"
    
    scene scene_madd_interrupt_dad_meeting_event_step_in_dad_spanks_madd_close_meet_fully_naked
    with fade
    show madd self loathing at left_small
    with dissolve
    x "(Now I'm fully exposed from the waist up. My shirt lies crumpled on the floor like discarded trash.)"
    x "(My shorts are bunched around my knees, restraining my legs.)"
    
    dad_says "There we go. Remove your shorts now."
    
    show dad dominant at right_small
    with dissolve
    show madd weeping at left_small
    with dissolve
    x "(Tears blur my vision as I awkwardly shimmy my shorts down my trembling legs.)"
    x "(Standing here completely exposed... I feel so vulnerable and ashamed of my own body...)"
    x "(I have to balance on one foot, then the other, to step out of them completely.)"
    x "(My hands are shaking so badly... I hate this... I hate how helpless I feel...)"
    
    show madd violated at left_small
    with dissolve
    x "(Now I stand completely naked before him, every inch of skin exposed to his hungry gaze.)"
    x "(Shame floods through me, hot and suffocating.)"
    x "(I've never felt more humiliated, more degraded, more less-than-human in my entire life.)"
    
    dad_says "Good girl. Now, you wanted to play basketball, right?"
    dad_says "Let's see how well you can really play."
    
    scene scene_madd_interrupt_dad_meeting_event_step_in_dad_spanks_madd_close_meet_hand_on_breast
    with fade
    show dad cruel at right_small
    with dissolve
    x "(He slowly lifts his shirt only to show his midsection, exposing his bare chest to me.)"

    show dad mocking at right_small
    with dissolve
    dad_says "You see Maddie, in this Basketball Game your face is the ball" 
    show madd disgusted at left_small
    with dissolve
    x "( I stare at his bare chest , disgusting fat stomach and his hairy belly which would make anyone gag )"
    show dad perverted at right_small
    with dissolve
    dad_says "And the hole is either my naval or my asshole"
    show madd distressed at left_small
    with dissolve
    x "(I knew coming here was a bad idea , i knew i shouldnt have interfered with his meetings but now i have to deal with this)"
    show dad lecherous at right_small
    with dissolve
    dad_says "You wont be able to score until your tongue is in my asshole or my naval"
    dad_says "And once your tongue is in one of my hole I am damn sure you wont get the smell or taste out of your mouth for weeks."
    show madd weeping at left_small
    with dissolve
    x "Please...dad.. i am sorry for doing this "
    show madd nauseated at left_small
    x "(His words make my stomach twist... the thought of putting my tongue in his disgusting asshole makes me want to vomit...)"
    show madd horrified at left_small
    x "(And he's already talking about putting his fat dick inside me... like I'm just a toy for him to ruin...)"
    x "(I feel so dirty... so less than human... like I'm nothing but a set of holes to him...)"
    show madd resigned at left_small
    with dissolve
    x "( Begging him was the only thing left to do , I was the one who made the first move of antagonizing him and now i have to deal with the consequences )"
    show madd broken at left_small
    with dissolve
    x "Please... i cant do this, i am truly sorry for what i did, i will never do it again"
    show dad manipulative at right_small
    with dissolve
    dad_says "Shhh shhh Shhh , its ok Maddie, you played the game without knowing the rules, but now you know the rules "
    show dad dominant at right_small
    with dissolve
    dad_says "SO next time you want to play the game, you will know what to do"
    show dad smirk at right_small
    with dissolve
    dad_says "But for noW , since you have forefit the game, the ball is in my court isnt that right Maddie ?"
    show madd shocked at left_small
    with dissolve
    x "(Without warning, his hand shoots out and grabs my breast aggressively, fingers digging deep.)"
    x "(Pain lances through the sensitive flesh. I let out an involuntary gasp.)"
    show madd distressed at left_small
    with dissolve
    x "(Fear and utter confusion swirl inside me like a storm. Why is this happening?)"
    x "(He starts fondling my breast, squeezing rhythmically. His grip is firm, possessive, unrelenting.)"
    x "(The rough calluses on his palm scrape against my tender skin.)"
    

    scene scene_madd_interrupt_dad_meeting_event_step_in_dad_spanks_madd_close_meet_hand_on_breast_dragging_to_door
    with fade
    show madd horrified at left_small
    with dissolve
    x "(He begins walking toward the door, still gripping my breast like a leash.)"
    x "(I stumble after him, pulled along, my feet barely keeping up.)"
    
    show madd broken at left_small
    with dissolve
    x "(I'm like a dog being dragged by its collar, completely at his mercy.)"
    x "(He pulls me across the room with my breast, the pain sharpening with each step.)"
    
    show madd traumatized at left_small
    with dissolve
    x "(I feel so degraded, so utterly used. This can't be real. This must be a nightmare.)"
    
    scene scene_madd_interrupt_dad_meeting_event_step_in_dad_spanks_madd_close_meet_hand_on_breast_at_door_lock
    with fade

    show madd paralyzed at left_small
    with dissolve
    x "(When we reach the door, he slams it shut with his free hand. The sound echoes like a gunshot.)"
    x "(Click. The lock engages. The sound of my doom sealing shut.)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "Now, about that game of basketball."
    
    show madd weeping at left_small
    with dissolve
    x "(Quiet sobs escape my throat. I can't hold them back anymore.)"
    x "(I feel utterly helpless. Completely alone. Abandoned by the world.)"
    
    dad_says "Shh, didn't you say you were completely healed?"
    
    scene scene_madd_interrupt_dad_meeting_event_step_in_dad_spanks_madd_close_meet_hand_on_breast_at_door_lock_spanking
    with fade   

    show madd shocked at left_small
    with dissolve
    x "(His free hand comes down hard on my bare buttocks—SMACK!)"
    x "(The sharp crack echoes in the small office. Burning pain radiates across my skin.)"
    
    show madd distressed at left_small
    with dissolve
    x "(A louder sob rips from my throat. The pain mingles with humiliation in a toxic cocktail.)"
    x "(He pulls me even closer, his body heat radiating against mine. His grip on my breast tightens cruelly.)"
    
    show dad cruel at right_small
    with dissolve
    show madd horrified at left_small
    with dissolve
    x "(His other hand begins exploring my buttocks, fingers spreading, squeezing, kneading the flesh.)"
    x "(I can feel his hand moving lower, creeping closer to my most private areas.)"
    x "(Closer and closer to my asshole.)"
    
    show madd trembling at left_small
    with dissolve
    x "(His hands wander with deliberate purpose, like a predator closing in on prey.)"
    x "(The destination is sickeningly clear.)"
    x "(My asshole tightens instinctively, muscles clenching in desperate resistance.)"

    scene scene_madd_interrupt_dad_meeting_event_step_in_dad_spanks_madd_close_meet_hand_on_breast_at_door_lock_spanking
    with fade

    show madd paralyzed at left_small
    with dissolve
    x "(Terror freezes my blood. What will he do next? How far will he go?)"
    
    show madd shocked at left_small
    with dissolve
    x "(His middle finger brushes against the entrance of my asshole.)"
    x "(The sensation is foreign, invasive, utterly wrong.)"
    
    show scene_dad_middle_finger_near_asshole_ at topleft
    with Dissolve(2.0)

    dad_says "Aw, what's the matter? You look scared."
    dad_says "Don't like where this is going?"
    
    show madd traumatized at left_small
    with dissolve
    x "(I can't speak. My vocal cords are paralyzed. Fear has rendered me completely mute.)"
    
    show madd violated at left_small
    with dissolve
    x "(He presses his finger against my asshole, applying steady pressure.)"
    x "(I gasp sharply as the tight ring of muscle resists the intrusion.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(A strange sensation washes over me—fear mixed with something I don't understand.)"
    x "(My body is betraying me, reacting in ways I can't control.)"
    
    dad_says "I thought you wanted to play?"
    dad_says "Didn't you know in basketball, the other team tries to put the ball in your hole?"
    
    show madd paralyzed at left_small
    with dissolve
    x "(I'm frozen solid, a statue carved from pure terror.)"
    x "(I can't move. I can't speak. I can't even breathe properly.)"
    
    show madd horrified at left_small
    with dissolve
    x "(Then I feel it—his middle finger positioning itself directly at the entrance of my asshole.)"
    x "(Pressure builds as he begins pushing inward, trying to force entry.)"
    
    show scene_dad_middle_finger_near_asshole_trying_to_enter at topleft
    with Dissolve(2.0)

    show madd trembling at left_small
    with dissolve
    x "(My asshole clenches involuntarily, the muscles refusing to yield.)"
    x "(I tense my buttocks desperately, trying to prevent him from entering.)"
    x "(But he's relentless. He keeps pushing, probing, testing.)"

    hide scene_dad_middle_finger_near_asshole_trying_to_enter
    
    show dad calculating at right_small
    with dissolve
    dad_thinks "Hmm, seems like she's a bit tight there."
    show dad hungry at right_small
    with dissolve
    dad_says "You know Maddie , today the basketball is my fingers but in the future it would be my fat dick and you will have to learn to take it in your hole like the good slut you are."
    x "(I look at him with pleading eyes , hoping he gives up his conquest to enter my body as a whole but i knew it was in vain.)"
    show dad controlling at right_small
    with dissolve
    dad_says "Maybe not today though, I will take my sweet time to break your body ...little by little."
    
    show madd distressed at left_small
    with dissolve
    x "(After endless moments of struggle, I feel him finally pulling his finger back.)"
    x "(A wave of relief washes over me—premature, I realize too late.)"
    
    show dad smirk at right_small
    with dissolve
    dad_says "Oops, looks like you're not quite ready for that yet."
    show dad obsessed at right_small
    with dissolve
    dad_says "We'll have to work on that some more."
    scene scene_madd_interrupt_dad_meeting_event_one_dad_fingers_in_face
    with fade

    show madd shocked at left_small
    with dissolve
    x "(Suddenly, he brings his hand right up to my face, inches from my eyes.)"
    x "(He folds his palm with two fingers extended—index and middle.)"
    x "(Both fingers glisten with moisture. From me? From him? I don't know.)"
    
    show dad lustful at right_small
    with dissolve
    dad_says "Open up."
    show dad mocking at right_small
    with dissolve
    dad_says "It will be easier if you lubricate yourself first."
    
    show madd horrified at left_small
    with dissolve
    x "(No. No no no. This can't be happening. I have to get out of here.)"
    x "(But where would I go? He's blocking the door. I'm naked. I'm trapped.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I shake my head frantically, violently refusing him.)"
    x "(Please don't make me do this. Please.)"
    
    show madd violated at left_small
    with dissolve
    x "(His hand on my ass suddenly tightens—crushing, agonizing pressure.)"
    x "(He squeezes harder, twisting in a clockwise motion that makes me cry out.)"
    
    dad_says "I said open up."
    
    show madd weeping at left_small
    with dissolve
    x "(Tears stream down my face in hot rivulets as I reluctantly, shamefully open my mouth.)"
    scene scene_madd_interrupt_dad_meeting_event_one_dad_fingers_in_face_open_mouth
    with fade

    show madd disgusted at left_small
    with dissolve
    x "(He brings his fingers to my lips—I can see dirt under his nails—then pushes them into my mouth.)"
    x "(I gag immediately as his thick fingers fill my oral cavity, pressing down on my tongue.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I can taste the sweat on his skin—salty, bitter, revolting.)"
    x "(There's grime embedded in the ridges of his fingerprints.)"
    
    show madd violated at left_small
    with dissolve
    x "(And worse—much worse—these are the same fingers that just touched my asshole.)"
    x "(That contamination is now in my mouth. On my tongue. Mixing with my saliva.)"
    
    show madd broken at left_small
    with dissolve
    x "(I feel filthy. Violated. Utterly contaminated from the inside out.)"
    
    show madd distressed at left_small
    with dissolve
    x "(He starts moving his fingers in and out of my mouth in a clockwise churning motion.)"
    x "(Saliva pools and drips down my chin. I'm drooling uncontrollably.)"
    
    show madd traumatized at left_small
    with dissolve
    x "(There's nowhere to run. Nowhere to hide. Nowhere to escape.)"
    x "(I'm completely, utterly, helplessly at his mercy.)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "That's it, good girl."
    
    show madd resigned at left_small
    with dissolve
    x "(After what feels like an eternity, he finally pulls his fingers out of my mouth.)"
    x "(They emerge coated in my saliva, glistening strands connecting them to my lips.)"
    
    show madd distressed at left_small
    with dissolve
    x "(He brings those wet fingers to my face, using them to smear away my tears.)"
    x "(Now my tears and spit mix together on my cheeks.)"
    
    show dad controlling at right_small
    with dissolve
    dad_says "There, there. It's okay."
    show dad possessive at right_small
    with dissolve
    dad_says "We'll take good care of you."
    
    show madd broken at left_small
    with dissolve
    x "(I feel shattered into a thousand pieces. This nightmare has no end.)"
    scene scene_madd_interrupt_dad_meeting_event_step_in_dad_spanks_madd_close_meet_hand_on_breast_at_door_lock_spanking
    with fade    

    show madd horrified at left_small
    with dissolve
    x "(The hand travels back down to my butt, fingers trailing wetly down my spine.)"
    x "(His middle finger is now thoroughly coated with my saliva mixed with his sweat.)"
    
    show madd trembling at left_small
    with dissolve
    x "(I can feel the slick moisture this time as he zeroes in on my asshole again.)"
    x "(The wetness is warm, viscous, utterly revolting.)"
    x "(It squelches slightly as his finger makes contact.)"

    show scene_dad_middle_finger_with_saliva_at_butthole_sliding_in at topleft
    with Dissolve(2.0)
    dad_says "This will make it easier."
    show madd paralyzed at left_small
    with dissolve
    x "(He pushes again, and this time the lubrication helps him.)"
    x "(The tip of his finger breaches the tight ring of muscle.)"
    
    show madd shocked at left_small
    with dissolve
    x "(Maybe a centimeter penetrates—I can feel the exact depth.)"
    x "(Then he starts wiggling his finger inside my asshole, working it deeper.)"
    
    show madd violated at left_small
    with dissolve
    x "(I feel pressure building, an unbearable stretching sensation radiating outward.)"
    x "(The muscle ring is forced to expand, to accommodate the invader.)"
    
    show madd distressed at left_small
    with dissolve
    x "(Deeper. It's reaching deeper inside me with each wiggle.)"
    x "(It burns so much... having his fingers stretching me open like this feels so wrong and invasive...)"
    x "(I can't believe this is happening to me... my body isn't even mine anymore...)"
    
    show scene_dad_middle_finger_with_saliva_at_butthole_sliding_in_all_in at topleft
    with Dissolve(2.0)

    show madd horrified at left_small
    with dissolve
    x "(After several agonizing wiggles, I feel it—his entire finger is now buried inside my asshole.)"
    x "(Every knuckle, every inch, completely inserted into my body.)"
    
    show madd traumatized at left_small
    with dissolve
    x "(Having a foreign object lodged inside me creates such a bizarre, violating sensation.)"
    x "(It's like I can't breathe fully, like something is stealing my air.)"
    
    show madd violated at left_small
    with dissolve
    x "(Like I've been invaded by something living, with a pulse and warmth of its own.)"
    x "(Something with agency. With intent. With a mind separate from mine.)"
    
    show madd shocked at left_small
    with dissolve
    x "(A loud gasp tears from my throat—the sensation is completely overwhelming my senses.)"
    
    dad_says "Aw look at that, I scored in your hole!"
    dad_says "Maybe you're not at full health yet."
    
    scene scene_madd_interrupt_dad_meeting_event_one_hair_pull_other_hand_at_butt
    with fade

    show madd distressed at left_small
    with dissolve
    x "(He removes his hand from my breast—finally—but then grabs a fistful of my hair.)"
    x "(He yanks my head backward violently, forcing my spine to arch.)"
    
    show madd horrified at left_small
    with dissolve
    x "(My face is pulled back until I'm staring directly up at him.)"
    x "(He looms above me, his face filling my entire field of vision.)"
    x "(He leans in closer, his breath washing over my face.)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "I know what you need to get better."
    show dad mocking at right_small
    with dissolve
    dad_says "Medicine!"
    
    show madd confused at left_small
    with dissolve
    x "(I look at him with wide, terrified eyes. Fear and confusion whirl inside me like a cyclone.)"
    x "(Medicine? What is he talking about?)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "Yes, medicine. The best kind."
    show dad lustful at right_small
    with dissolve
    dad_says "My medicine."
    
    show madd trembling at left_small
    with dissolve
    x "(A cold shiver runs down my spine, raising goosebumps across my entire body.)"
    x "(This is escalating. Getting worse and worse with every passing second.)"
    
    show dad authoritative at right_small
    with dissolve
    dad_says "Open your mouth."
    
    show madd hesitant at left_small
    with dissolve
    x "(I hesitate, knowing with sickening certainty what's coming next.)"
    x "(My jaw refuses to unlock. My lips press together in futile resistance.)"
    

    show madd distressed at left_small
    with dissolve
    x "(But his grip on my hair tightens ruthlessly, yanking harder, forcing tears to spring to my eyes.)"
    x "(The pain in my scalp is excruciating.)"
    
    show dad cruel at right_small
    with dissolve
    dad_says "When daddy gives you medicine, you take it like a good girl."
    
    scene scene_madd_interrupt_dad_meeting_event_one_hair_pull_other_hand_at_butt_madd_open_mouth
    with fade

    show madd resigned at left_small
    with dissolve
    x "(Reluctantly, shamefully, I open my mouth in surrender.)"
    
    show dad possessive at right_small
    with dissolve
    dad_says "That's it."
    
    show madd disgusted at left_small
    with dissolve
    show dad perverted at right_small
    with dissolve
    x "(As I open my mouth, I watch in horror as he swirls spit around in his own mouth.)"
    x "(I can see his tongue moving behind his teeth, gathering saliva.)"
    x "(His cheeks puff slightly as he works up more liquid.)"
    
    show madd horrified at left_small
    with dissolve
    x "(I know exactly what's coming next. The knowledge makes my stomach heave.)"
    
    show madd traumatized at left_small
    with dissolve
    x "(He swirls the spit for several long seconds, building up volume.)"
    x "(Then he leans in closer—close enough that I can see the pores on his nose.)"
    
    show madd violated at left_small
    with dissolve
    show dad lecherous at right_small
    with dissolve
    x "(It's almost like a kiss, our faces so close, but grotesquely twisted.)"
    x "(Then he parts his lips and spits directly into my open mouth.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I gag as the warm, thick liquid splashes onto my tongue.)"
    x "(It keeps flowing—he's emptying his entire mouthful into mine.)"
    scene scene_madd_interrupt_dad_meeting_event_one_hair_pull_other_hand_at_butt_madd_open_mouth_dad_spitting_into_mouth
    with fade

    show madd disgusted at left_small
    with dissolve
    x "(The stream of spit flows from his mouth into mine like a grotesque fountain.)"
    x "(I can taste the bitterness, the overwhelming saltiness, the wrongness of it all.)"
    x "(His warm, thick spit is filling my mouth... it tastes so bitter and disgusting...)"
    
    show madd violated at left_small
    with dissolve
    x "(The taste of his spit still lingers... I feel so disgusting inside, like he marked me as his...)"
    
    show madd distressed at left_small
    with dissolve
    x "(Our lips never actually touch, but the act feels unbearably intimate in the most twisted way.)"
    x "(More intimate than any kiss could ever be.)"
    
    show madd nauseated at left_small
    with dissolve
    show dad debased at right_small
    with dissolve
    x "(He finally stops spitting after what feels like minutes.)"
    x "(My mouth is full—overfull—with his saliva.)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "Drink up, sweetie."
    show dad lustful at right_small
    with dissolve
    dad_says "This will make you feel so much better."
    show dad obsessed at right_small
    with dissolve
    dad_says "Daddy's special medicine."
    
    show madd broken at left_small
    with dissolve
    x "(I feel utterly shattered. Broken beyond repair. This nightmare has no bottom.)"
    
    show madd disgusted at left_small
    with dissolve
    x "(His spit coats my entire tongue and the inside of my cheeks.)"
    x "(Even though it's just saliva—just bodily fluid—I can distinguish his taste from mine.)"
    x "(His is more bitter, more acidic, fundamentally different from my own.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(If I swallow this, it will become part of me. Part of him will slide into my body.)"
    x "(I feel disgusted with myself for even being in this position.)"
    
    show madd resigned at left_small
    with dissolve
    x "(But I have no choice. None at all. I'm completely at his mercy.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I swallow reluctantly, forcing the foreign fluid down my throat.)"
    x "(Slowly, agonizingly, I feel his spit slide down my esophagus.)"
    x "(The texture is thick, viscous, coating my throat as it descends.)"
    
    show madd violated at left_small
    with dissolve
    x "(That was beyond degrading. I feel used like a receptacle, like an object.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I can still feel residue of his saliva lingering in my mouth, coating my teeth.)"
    
    show scene_dad_middle_finger_inside_asshole_index_finger_trying at topleft
    with Dissolve(2.0)       
    show madd shocked at left_small
    with dissolve
    x "(As I'm still recovering from that violation, I feel it—new pressure at my asshole.)"
    x "(His index finger is now joining the middle finger, pushing at the entrance.)"
    
    show dad fixated at right_small
    with dissolve
    show madd trembling at left_small
    with dissolve
    x "(My asshole isn't giving way easily this time either, despite the wetness.)"
    x "(The muscle ring is already stretched around one finger—two feels impossible.)"
    
    show madd horrified at left_small
    with dissolve
    x "(He pivots his index finger right next to the middle finger that's already inside.)"
    x "(He uses the embedded middle finger as a lever, stretching my asshole wider while forcing the index finger in.)"
    
    show madd violated at left_small
    with dissolve
    x "(It's an impossibly tight fit. The burning stretch is excruciating.)"
    x "(But he's making progress, millimeter by agonizing millimeter.)"
    
    show scene_dad_middle_finger_inside_asshole_index_finger_inside at topleft
    with Dissolve(2.0)

    show dad sadistic at right_small
    with dissolve
    dad_says "Fuck... that tight little asshole is gripping my fingers like a untouched nun. I can't imagine what your pussy is going to feel like when I finally wreck it with my cock"
    dad_says "You're going to be my personal cum-dump soon. I'll keep that cunt stuffed full every single night until you're leaking my seed for days."

    show madd distressed at left_small
    with dissolve
    x "(Soon I can feel both fingers inside my asshole, side by side.)"
    x "(The pressure is immense, overwhelming, unbearable.)"
    
    show madd traumatized at left_small
    with dissolve
    x "(He starts wiggling both fingers inside me, scissoring them apart.)"
    x "(The sensation is absolutely overwhelming—too much input for my brain to process.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(I can feel them reaching deeper inside me, exploring, violating.)"
    x "(They curl and press against my inner walls.)"
    
    show madd shocked at left_small
    with dissolve
    x "(After several brutal wiggles, the reality hits—both fingers are now fully buried inside my asshole.)"
    x "(Two entire fingers. All the way to the knuckles. Deep inside my body.)"
    
    show madd violated at left_small
    with dissolve
    x "(I gasp loudly—the sensation is completely overwhelming every other thought.)"
    
    dad_says "Wow, you're really something else."
    dad_says "Such a good girl for daddy."
    dad_says "Too bad you're losing the game though. That's 3 points for daddy."
    dad_says "Do you want a shot at the game too ?? By licking my asshole clean ?"

    show madd distressed at left_small
    with dissolve
    x "(As I'm gasping desperately for air, trying to process this violation, he leans in again torturing me with not just his actions but his words too)"
    x "(Just the thought of having my tongue in his asshole gives me the creeps. A disgusting man like him , i just cant imagine what kind of dark matters emanate from his butt.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(He spits more saliva directly into my open, gasping mouth without warning.)"
    x "(It splashes against my tongue, warm and thick.)"
    
    show dad smirk at right_small
    with dissolve
    dad_says "That's 4 points for daddy now."
    show dad dominant at right_small
    with dissolve
    dad_says "Do you give up yet?"
    
    show madd traumatized at left_small
    with dissolve
    x "(I'm struggling to breathe now—his fingers are stretching my asshole impossibly wide.)"
    x "(The burn radiates through my entire lower body. It's too much.)"
    
    show madd broken at left_small
    with dissolve
    x "(I can't take it anymore. I'm at my absolute limit.)"
    
    show madd weeping at left_small
    with dissolve
    x "(I nod my head frantically, desperately signaling my complete surrender.)"
    
    show madd resigned at left_small
    with dissolve
    x "Please, stop. I give up."
    
    show dad authoritative at right_small
    with dissolve
    dad_says "Never try to sabotage me again."
    show dad controlling at right_small
    with dissolve
    dad_says "You got that?"
    
    show madd submissive nod at left_small
    with dissolve
    x "(I nod my head again, tears streaming freely down my face, dripping off my chin.)"
    
    show dad authoritative at right_small
    with dissolve
    dad_says "Good girl. Now, bend down. Apologize to me."
    
    hide scene_dad_middle_finger_inside_asshole_index_finger_inside
    hide scene_dad_middle_finger_inside_asshole_index_finger_trying
    with Dissolve(2.0)

    show madd shocked at left_small
    with dissolve
    x "(As he commands, he pulls his fingers out of my asshole in one swift motion.)"
    x "(The sudden emptiness is jarring—a strange hollow sensation replaces the fullness.)"



    show madd distressed at left_small
    with dissolve
    x "(Finally, finally I feel like I can breathe again. Air rushes into my lungs.)"
    x "(But relief is premature—this isn't over.)"
    
    scene scene_madd_interrupt_dad_meeting_event_madd_bending_down
    with fade

    show madd resigned at left_small
    with dissolve
    x "(I slowly bend down, lowering my naked body until my face hovers inches from the floor.)"
    x "(I'm acutely aware of my complete nudity, every inch of skin exposed and vulnerable.)"
    
    show madd violated at left_small
    with dissolve
    x "(But I have no choice. Resistance means escalation. Compliance might mean survival.)"
    
    show madd weeping at left_small
    with dissolve
    x "(I look up at him through my tears, my vision blurred and distorted.)"
    
    show madd broken at left_small
    with dissolve
    x "I'm sorry dad. I won't do it again."
    
    show madd horrified at left_small
    with dissolve
    x "(He looks down at me with that sinister smile—the smile of someone who's won.)"
    x "(He casually removes his shoes followed by his socks, dropping them on the floor beside me.)"
    
    dad_says "Good girl. Now stay down there."
    
    show madd submissive nod at left_small
    with dissolve
    x "(I comply immediately, lowering my head until it's mere inches from the carpet.)"
    x "(The musty smell of the floor fills my nostrils.)"
    scene scene_madd_interrupt_dad_meeting_event_madd_bending_down_dad_bare_foot_on_head
    with fade

    show madd shocked at left_small
    with dissolve
    x "(Then I feel something unmistakably warm and fleshy pressing against the back of my head.)"
    x "(His foot. His bare foot.)"
    
    show madd violated at left_small
    with dissolve
    x "(He places his bare foot directly on my head, the sole pressing against my scalp.)"
    x "(I can feel every ridge, every callous, every imperfection in his skin.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(The smell hits me immediately—pungent sweat, accumulated grime, unwashed skin.)"
    x "(It's overwhelming, making my stomach churn with nausea.)"
    
    show madd broken at left_small
    with dissolve
    x "(His dirty, sweaty foot is pressing my face into the floor... I feel like a literal doormat...)"
    
    show madd distressed at left_small
    with dissolve
    x "(He applies more pressure with his foot, pushing my head down further toward the floor.)"
    x "(My neck strains with the pressure.)"
    
    show madd traumatized at left_small
    with dissolve
    x "(I'm a footrest now—literally. A human carpet for him to step on.)"
    x "(Completely, utterly, absolutely at his mercy.)"
    
    show madd violated at left_small
    with dissolve
    x "(He keeps pushing relentlessly with his foot, forcing my head lower.)"
    scene scene_madd_interrupt_dad_meeting_event_madd_bending_down_dad_bare_foot_on_head_madd_head_angled
    show madd distressed at left_small
    with dissolve
    x "(Eventually I have to rest my forehead against the floor—there's nowhere else to go.)"
    x "(But the pressure from his foot persists, unrelenting.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I have to angle my head to the side to accommodate his foot.)"
    x "(Now his foot is pressing directly against the side of my face.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I can feel every texture—the rough, dry skin against my cheek.)"
    x "(I can see dirt embedded in the crevices, callouses on the heel and ball.)"
    
    show madd disgusted at left_small
    with dissolve
    show dad smirk at right_small
    with dissolve
    x "(And the smell. God, the smell is the worst part.)"
    x "(The concentrated odor of sweat and grime is completely overwhelming.)"
    
    show madd violated at left_small
    with dissolve
    x "(I'm inhaling it directly through my nostrils with each breath.)"
    x "(The stench is right there, pressed against my face, impossible to escape.)"
    
    show madd broken at left_small
    with dissolve
    x "(I feel shattered beyond repair. A broken thing that used to be a person.)"
    
    show madd depressed at left_small
    with dissolve
    x "(I dreamed of getting him out of the house, working in an office.)"
    x "(I dreamed of having at least morning to evening to myself, safe from him.)"
    
    show madd self loathing at left_small
    with dissolve
    show dad mocking at right_small
    with dissolve
    dad_thinks "(Her plan was beautiful. And it failed beautifully.)"
    show dad obsessed at right_small
    with dissolve
    dad_thinks "(Now she understands. There is no escape. There is only me.)"
    x "(But it backfired so catastrophically. So horribly.)"
    x "(I should've known better. I should've predicted this.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I feel his foot pressure soften slightly once he's achieved full contact with my face.)"
    x "(He no longer needs force—my submission is complete.)"
    
    show madd violated at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "(He starts rubbing his foot slowly across my face.)"
    x "(Back and forth, grinding his sole against my skin, smearing sweat and grime.)"
    
    show madd weeping at left_small
    with dissolve
    x "(All I can do is sob quietly, tears mixing with the sweat from his foot.)"
    x "(How long this goes on, I have no idea. Time has lost all meaning.)"
    
    show madd distressed at left_small
    with dissolve
    x "(Finally—finally—he removes his foot from my face.)"
    x "(A cold breeze touches my cheek where his hot foot had been pressed.)"
    scene scene_madd_interrupt_dad_meeting_event_madd_bending_down_dad_bare_foot_madd_looks_up
    show madd traumatized at left_small
    with dissolve
    x "(I look up at him through my tears, my vision swimming.)"
    
    dad_says "Think you learned your lesson?"
    
    show madd submissive nod at left_small
    with dissolve
    x "(I nod my head slowly, mechanically. Yes. Yes, I learned.)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "Good girl. Now, get up."
    
    show madd trembling at left_small
    with dissolve
    x "(I slowly push myself up onto my knees, my entire body shaking.)"
    
    scene scene_madd_interrupt_dad_meeting_event_one_hair_pull_other_hand_at_butt_after_foot_on_head

    with fade


    show madd shocked at left_small
    with dissolve
    x "(He grabs my hair again without warning, yanking me up to a standing position.)"
    x "(My scalp screams in protest.)"
    
    show dad delusional at right_small
    with dissolve
    dad_says "You're going to be a good wife someday."
    show dad authoritative at right_small
    with dissolve
    dad_says "You need to learn to obey your husband."
    show dad controlling at right_small
    with dissolve
    dad_says "Do you understand me?"
    
    show madd resigned at left_small
    with dissolve
    x "(I nod my head slowly, numbly. Understanding and agreement are irrelevant now.)"
    
    show dad calculating at right_small
    with dissolve
    dad_says "Now, get dressed."
    show dad creepy at right_small
    with dissolve
    dad_says "And get the hell out of here. I have to join another meeting soon."
    
    show madd distressed at left_small
    with dissolve
    x "(Him and his damn meetings. All he ever contributes is 'nothing from my end.')"
    
    show madd violated at left_small
    with dissolve
    show dad calculating at right_small
    with dissolve
    x "(I shuffle over to his desk where my shorts and shirt lie in a crumpled heap.)"
    
    scene scene_madd_interrupt_dad_meeting_event_one_madd_picking_up_clothes
    with fade


    show madd trembling at left_small
    with dissolve
    x "(I bend down to pick up my shorts first, my hands shaking uncontrollably.)"
    
    show madd anxious at left_small
    with dissolve
    x "(As I'm pulling up my shorts, I feel his eyes boring into me.)"
    x "(He's staring directly at my exposed holes from behind.)"
    
    show madd horrified at left_small
    with dissolve
    x "(This time his vision has shifted to my other hole.)"
    x "(My pussy.)"
    
    show madd violated at left_small
    with dissolve
    x "(I can physically feel his gaze penetrating my pussy as I'm bent over.)"
    x "(The intensity of his stare makes my skin crawl with fresh revulsion.)"
    
    show dad fixated at right_small
    with dissolve
    show madd worried at left_small
    with dissolve
    x "(If I keep antagonizing him, who knows what else he might do to me.)"
    x "(No hole is safe with him in the house. None.)"
    
    show madd nervous at left_small
    with dissolve
    x "(I quickly pull up my shorts the rest of the way, keeping my back facing him.)"
    x "(He can stare at my asshole all he wants , just please leave my pussy alone.)"
    
    show madd distressed at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(If he sets his sights on my pussy, I'm terrified of what he might do to it too.)"
    x "(And then there would be no coming back from that. That would be the final violation.)"
    
    show madd trembling at left_small
    with dissolve
    x "(When my shorts are finally secured, I quickly grab my shirt and pull it over my head.)"
    
    scene scene_madd_interrupt_dad_meeting_event_one_madd_facing_dad_end
    with fade

    show madd anxious at left_small
    with dissolve
    x "(I quickly turn around to face him, breaking his line of sight to my backside.)"
    
    show dad lecherous at right_small
    with dissolve
    dad_thinks "(God that pussy looks so inviting.)"
    show dad greedy at right_small
    with dissolve
    dad_thinks "(It looks like if I enter that hole, I will never want to leave.)"
    show dad obsessed at right_small
    with dissolve
    dad_thinks "(One day maybe just sleep with my cock buried inside that pussy.)"
    show dad lustful at right_small
    with dissolve
    dad_thinks "(Let it stay there for the whole night, warm and tight.)"
    
    show madd relieved at left_small
    with dissolve
    x "(I start moving toward the door. Surprisingly, he unlocks it and even holds it open for me.)"
    x "(Like a gentleman. Like this is a normal goodbye. The cognitive dissonance is surreal.)"
    scene scene_dad_whisper_after_zoom_interview_break
    with fade
    show madd traumatized at left_small
    with dissolve
    x "(As I'm crossing the threshold, he leans in close and whispers directly into my ear.)"
    
    show dad cruel at right_small
    with dissolve
    dad_says "Remember this encounter. Don't you dare cross me."
    
    show madd submissive nod at left_small
    with dissolve
    x "(I nod mechanically and walk out, hastily wiping my tears as I go.)"
    x "(The taste of his spit still lingers in my mouth.)"
    $ madd_willpower=max(0,madd_willpower-30)
    $ journal_event_set_done("Dad", "Dad's Work Secret")
    $ journal_event_show("Dad", "Cracking His Schedule")
    call advance_time_and_check(minutes=90) from _call_advance_time_and_check_51
    $ character_relations["dad"]["intimacy"] +=7
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["oral_sex"] += 1
    $ character_relations["dad"]["lust"]=0
    jump home_areas




label madd_interrupt_dad_meeting_event_two:

    scene scene_madd_interrupt_dad_meeting_event_two_peek_inside
    with fade
    
    show madd determined at left_small
    with dissolve
    x "(I push the door open slightly to peek inside.)"
    x "(My heart is pounding as I scout the situation before making my move.)"
    
    show madd focused at left_small
    with dissolve
    x "(Dad is sitting at his desk, looking serious as he talks to someone off-screen.)"
    x "(He's engaged in a professional conversation—completely absorbed.)"
    
    show madd hopeful at left_small
    with dissolve
    x "(This is my moment! His mouth is open, meaning he was just about to speak.)"
    x "(The camera light on the monitor is clearly visible—it's on! Actually on this time!)"
    x "(This time I have a real chance.)"

    
    show madd determined at left_small
    with dissolve
    x "(I walk closer to him with steady steps, trying to appear calm and innocent.)"
    x "(His eyes glare at me with immediate warning, but I don't back down.)"
    
    show dad angry at right_small
    with dissolve
    dad_thinks "(What is she doing? She knows better than to interrupt me!)"
    
    show madd focused at left_small
    with dissolve
    x "(I try to ignore his angry eyes and focus on moving closer to him.)"
    x "(I need to get into that camera frame without appearing too obvious.)"
    x "(I can see the monitor clearly now, and there it is—the camera on top of the display.)"
    
    show madd determined at left_small
    with dissolve
    x "(The red recording indicator is definitely on. I can see it clearly.)"
    x "(Several faces are visible on his screen—his coworkers, probably from his office team.)"
    x "(This is my chance to prove I'm healthy and functional.)"
    
    scene scene_madd_interrupt_dad_meeting_event_two_approaching_desk
    with fade
    
    show madd nervous at left_small
    with dissolve
    x "(I take a deep breath and position myself where the camera can see me.)"
    x "(My mind races with the perfect thing to say—something that will convince them.)"
    
    show dad calculating at right_small
    with dissolve
    dad_thinks "(She's moving into the camera frame. What is she planning?)"
    show dad angry at right_small
    with dissolve
    dad_thinks "(No... she wouldn't dare try to sabotage me again, would she?)"
    
    show madd hopeful at left_small
    with dissolve
    x "(I force brightness and confidence into my voice—the voice of someone who is completely fine.)"
    
    show madd happy at left_small
    with dissolve
    x "Dad, when can we play basketball together? I'm feeling much better now—completely healed!"
    x "(I smile at the camera, making sure my face is visible and my demeanor appears perfectly normal.)"
    
    show dad what at right_small
    with dissolve
    dad_thinks "(No! She's trying to make me look like a liar!)"
    show dad angry at right_small
    with dissolve
    dad_thinks "(If those people hear this, they'll think I was lying about her condition!)"
    
    scene scene_madd_interrupt_dad_meeting_event_two_on_camera
    with fade
    
    show madd hopeful at left_small
    with dissolve
    x "(I can see myself clearly on the monitor now, standing next to him like everything is perfectly normal.)"
    x "(This is it—my score against him. I've got witnesses.)"
    
    show dad angry at right_small
    with dissolve
    dad_thinks "(This bitch! She's sabotaging everything! I told work she was mentally unstable!)"
    show dad angry at right_small
    with dissolve
    dad_thinks "(Now they'll think I'm a con for lying about her condition!)"
    
    show madd hopeful at left_small
    with dissolve
    x "(I look back at him, trying to gauge his reaction. His face is turning red—the veins on his forehead are bulging.)"
    
    show dad angry at right_small
    with dissolve
    dad_says "Honey, I'm busy right now. We can talk later about that."
    show dad angry at right_small
    with dissolve
    dad_thinks "(Maintain composure. In front of witnesses. I can't lose it now. But she's going to pay for this.)"
    
    show madd determined at left_small
    with dissolve
    x "(His tone is tight, controlled, but I can sense the volcano building beneath the surface.)"
    x "(I decide to push just a little further—one more piece of evidence.)"
    
    show madd determined at left_small
    with dissolve
    x "But dad, you promised we would play basketball this weekend. I was really looking forward to it."
    x "(I tilt my head innocently, driving the point home for his coworkers.)"
    
    show dad angry at right_small
    with dissolve
    dad_thinks "(She's pushing me! In front of my coworkers! This is it!)"
    
    show madd shocked at left_small
    with dissolve
    x "(I see his hands clench into fists. The anger is barely contained now.)"
    x "(His face is almost purple with rage.)"
    
    show dad controlling at right_small
    with dissolve
    dad_says "I need to drop from this call. Something urgent just came up."
    show dad dominant at right_small
    with dissolve
    dad_thinks "(I'm going to end this call and then I'm going to show her exactly what happens when you cross me.)"
    
    scene scene_madd_interrupt_dad_meeting_event_two_exit_call
    with fade
    
    show madd hopeful at left_small
    with dissolve
    x "(I watch as he immediately exits the video call, disconnecting from his team.)"
    x "(Success! I did it! I actually managed to get him away from that meeting!)"
    
    show madd determined at left_small
    with dissolve
    x "(I stand there for a moment, feeling a mixture of triumph and apprehension washing over me.)"
    x "(I've taken my first real stand against him. But deep down, I know there will be consequences.)"
    
    show madd processing at left_small
    with dissolve
    x "(For now, though, I feel a sense of empowerment I haven't felt in a long time.)"
    x "(This was the first real step in taking control of my life back from him.)"
    
    show dad angry at right_small
    with dissolve
    dad_thinks "(Time to remind her who's in charge.)"
    
    scene scene_madd_interrupt_dad_meeting_event_two_standing_still
    with fade
    
    show madd distressed at left_small
    with dissolve
    x "(I can see his face is now a deep crimson. The rage in his eyes is absolutely terrifying.)"
    x "(He slowly turns to face me completely, his jaw clenched so tight I'm worried his teeth might crack.)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "Don't blame me for what happens next."
    show dad coercive at right_small
    with dissolve
    dad_thinks "(She wanted to play. Let's play.)"
    
    show madd horrified at left_small
    with dissolve
    x "(My moment of triumph evaporates instantly as I realize what I've done.)"
    
    show madd trembling at left_small
    with dissolve
    x "(He stands up from his desk with deliberate, measured movements.)"
    x "(Each second feels like an eternity as he approaches me.)"
    
    show dad predatory at right_small
    with dissolve
    dad_thinks "(I'm going to make her regret every single word.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(I step aside to let him pass, trying to keep my expression neutral.)"
    x "(But inside, pure terror is overwhelming my senses.)"
    
    show dad controlling at right_small
    with dissolve
    dad_says "Now, I have been real patient with you, but this is the last straw."
    show dad cruel at right_small
    with dissolve
    dad_says "You are going to regret this for the rest of your life."
    
    scene scene_madd_interrupt_dad_meeting_event_two_door_locked
    with fade
    
    show madd horrified at left_small
    with dissolve
    x "(He stands near the door for a moment, and then he closes it behind us with a controlled but ominous click.)"
    x "(The lock engages—click—and I realize I'm now trapped with him.)"
    
    show dad dominant at right_small
    with dissolve
    dad_thinks "(Now she belongs only to me. No one to hear her. No one to save her.)"
    
    show madd shocked at left_small
    with dissolve
    x "(I brace myself, knowing that I have pushed him too far this time.)"
    x "(But something inside me—something small and stubborn—still feels that I did the right thing.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(Even as terror fills my veins, a part of me refuses to surrender completely.)"
    x "(I had stood up to him. I had scored a point. And no matter what comes next, I did that.)"
    
    scene scene_madd_interrupt_dad_meeting_event_two_dad_walking_towards
    with fade
    
    show dad angry at right_small
    with dissolve
    dad_says "You think you're so clever, don't you?"
    show dad obsessed at right_small
    with dissolve
    dad_says "Trying to make me look stupid in front of my colleagues?"
    show dad possessive at right_small
    with dissolve
    dad_says "You're mine. Every inch of you belongs to me."
    
    show madd distressed at left_small
    with dissolve
    x "(He reaches out and grabs my arm tightly, his grip firm and unyielding.)"
    x "(His fingers dig into my skin as he pulls me closer to him.)"
    
    show dad hungry at right_small
    with dissolve
    dad_thinks "(I'm going to break her. Completely. By the time I'm done, she won't even remember her own name.)"
    
    show madd violated at left_small
    with dissolve
    x "(I wince in pain as he pulls me closer, and I'm suddenly in his arms.)"
    x "(I'm looking up at him, his face just inches away from mine.)"
    x "(In his eyes, I can see a potent mixture of fury, desire, and something darker—ownership.)"
    
    scene scene_madd_interrupt_dad_meeting_event_two_face_to_face
    with fade
    
    show madd trembling at left_small
    with dissolve
    x "(His breath is hot against my face. I can smell the coffee on his breath and something else—rage.)"
    
    show dad predatory at right_small
    with dissolve
    dad_says "you wanted to be ambitious huh ? This bravery of yours is going to cost you dearly."
    show dad coercive at right_small
    with dissolve
    dad_thinks "(I'm going to remind her exactly what she is to me. A toy. A possession.)"
    
    show madd horrified at left_small
    with dissolve
    x "(He leans in closer, and his lips meet mine in a forceful, invasive kiss.)"
    x "(There's nothing gentle or loving about it—it's pure domination.)"
    
    scene scene_madd_interrupt_dad_meeting_event_two_forced_kiss
    with fade
    
    show madd disgusted at left_small
    with dissolve
    x "(I can feel his tongue trying to invade my mouth, pushing past my clenched teeth.)"
    x "(His hands roam over my body, rough and possessive, claiming every part of me.)"
    
    show dad obsessed at right_small
    with dissolve
    dad_thinks "(She always taste so good. I'm going to taste it all out of her.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(He puts his hand behind my head and pulls me into an even deeper kiss.)"
    x "(My mouth is no longer my own—it's his to use as he sees fit.)"
    x "(His tongue is aggressive, probing, demanding entry into the most intimate part of me I can control.)"
    
    show madd violated at left_small
    with dissolve
    x "(I can only hold his tongue at bay for so long before it forces its way inside.)"
    x "(I feel disgusted as his tongue explores my mouth.)"
    x "(It's prodding and pushing against mine, invading, claiming.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I can feel his saliva mixing with mine, and the taste of him makes me gag.)"
    x "(His lips are as if he's trying to consume me whole, to make me a part of him.)"
    
    
    show madd broken at left_small
    with dissolve
    x "(After what feels like an eternity, he finally pulls away.)"
    x "(I gasp for air, my heart racing in my chest, my mouth tasting of him.)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "You taste so much better than your mom . Too bad your amitions ruin your submissive body. Let me show you where ambition leads girls like you."
    
    show madd shocked at left_small
    with dissolve
    x "(He immediately grabs my hair and pulls my head back with force.)"
    x "(I'm forced to look up at him, my neck straining with the pressure.)"
    
    show dad possessive at right_small
    with dissolve
    dad_thinks "(She wanted to play games. I'll show her the real game.)"
    
    show madd horrified at left_small
    with dissolve
    x "(His eyes are dark with an intensity that terrifies me.)"
    x "(He starts licking my cheeks, his tongue rough and invasive against my skin.)"
    x "(From my chin all the way up to my forehead, marking me, claiming me.)"
    
    show madd traumatized at left_small
    with dissolve
    x "(I can feel his hot breath on my face as he continues his assault.)"
    x "(I can smell his foul breath mixed with sweat and something bitter.)"
    x "(The smell of his saliva on my skin makes me want to vomit.)"
    
    scene scene_madd_interrupt_dad_meeting_event_two_licking_neck
    with fade
    
    show madd distressed at left_small
    with dissolve
    x "(He then moves down to my neck, his tongue tracing a path down to my collarbone.)"
    x "(I can feel his saliva dripping onto my skin, making me shiver with pure revulsion.)"
    
    show dad hungry at right_small
    with dissolve
    dad_thinks "(She tried to shame me in front of my colleagues. She's going to wear my mark.)"
    
    show madd violated at left_small
    with dissolve
    x "(He then moves back up to my lips, capturing them in another forceful kiss.)"
    x "(This time, I don't resist. I feel utterly powerless against his overwhelming need to possess me.)"
    
    scene scene_madd_interrupt_dad_meeting_event_two_shirt_removal
    with fade
    
    show madd broken at left_small
    with dissolve
    x "(His hands roam over my body, rough and possessive, and I feel completely trapped.)"
    x "(His hands lower to the hem of my shirt, and in one swift motion, he yanks it upward.)"
    x "(He's pulling it with such force that if I had resisted, the fabric would have torn.)"
    
    scene scene_madd_interrupt_dad_meeting_event_two_shirt_removal_complete
    with fade

    show madd resigned at left_small
    with dissolve
    x "(So I comply, letting him pull the shirt over my head.)"
    x "(Now I stand before him with my breasts fully exposed.)"
    
    show dad fixated at right_small
    with dissolve
    dad_thinks "(Perfect. She's mine now. Completely mine.)"
    
    show madd horrified at left_small
    with dissolve
    x "(I can see the anger still burning in his eyes, mixed now with undisguised hunger.)"
    x "(I know that this will last for a long time. He's just getting started.)"
    
    scene scene_madd_interrupt_dad_meeting_event_two_breast_groping
    with fade
    
    show madd distressed at left_small
    with dissolve
    x "(He reaches out and grabs one of my breasts, his hand firm and possessive.)"
    x "(I gasp as he squeezes it tightly, roughly, without any consideration for my comfort.)"
    x "(He's squeezing it as if expecting something to yield to his pressure.)"
    
    show dad dominant at right_small
    with dissolve
    dad_thinks "(She wanted attention. She's going to get it. All of it.)"
    
    show madd traumatized at left_small
    with dissolve
    x "(He moves his hand to my other breast, giving it the same rough treatment.)"
    x "(I can feel his fingers digging into my skin as he kneads my breasts like they're objects to be manipulated.)"
    x "(I feel a mix of anger and profound humiliation wash over me.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(Then his face comes closer to my chest.)"
    x "(I can feel his hot breath on my skin as he leans in.)"
    x "(I know exactly what's coming next, and a wave of dread washes over me.)"
    
    scene scene_madd_interrupt_dad_meeting_event_two_biting_breast
    with fade
    
    show madd shocked at left_small
    with dissolve
    x "(He opens his mouth and takes one of my nipples between his lips.)"
    x "(He closes his lips around it and starts sucking on it with intensity.)"
    x "(I can feel the suction of his mouth on my nipple, and I feel utterly humiliated.)"
    
    show dad obsessed at right_small
    with dissolve
    dad_thinks "(She tastes like victory. I'm going to mark her so everyone knows she's taken.)"
    
    show madd violated at left_small
    with dissolve
    x "(He's sucking on my breast as if it's some kind of conquest he's claiming.)"
    x "(I can feel his tongue moving around my nipple, adding to the humiliation and discomfort.)"
    
    show madd distressed at left_small
    with dissolve
    x "(Then I feel strong pain shoot through me as he bites down on my nipple.)"
    x "(I cry out involuntarily as he continues to bite and suck, the pain sharp and unforgiving.)"
    
    show madd weeping at left_small
    with dissolve
    x "(Tears welling up in my eyes as I endure this painful assault.)"
    x "(But somewhere deep inside, I'm still holding onto a small spark of defiance.)"
    x "(I stood up to him. That matters. Even if it costs me everything.)"
    
    show madd distressed at left_small
    with dissolve
    x "(He kept sucking and biting on my breast for what felt like an eternity.)"
    x "(Finally, he pulled away, leaving my breast red and sore.)"
    x "(I stood there, trying to catch my breath and compose myself.)"
    
    show dad dominant at right_small
    with dissolve
    dad_thinks "(She's branded now. Mine to use as I see fit.)"
    
    scene scene_madd_interrupt_dad_meeting_event_two_shorts_removal
    with fade
    
    show madd trembling at left_small
    with dissolve
    x "(I knew this was just the beginning of what was to come.)"
    x "(His hand moves down to my waist and grabs my shorts.)"
    
    show madd horrified at left_small
    with dissolve
    x "(With a swift motion, he pulls them down along with my panties, exposing me completely.)"
    x "(My naked body is now fully exposed to him.)"
    
    show dad fixated at right_small
    with dissolve
    dad_thinks "(Perfect. She's completely vulnerable now. No escape.)"
    
    show madd horrified at left_small
    with dissolve
    x "(I remember last time he was staring at my pussy after we were done.)"
    x "(This time I can see his eyes locked on it.)"
    x "(That's when I realized what he was planning to do next.)"
    
    show madd horrified at left_small
    with dissolve
    x "(I realized I might have made a catastrophic mistake by standing up to him.)"
    x "(If he takes me now... if I end up pregnant... my life is over.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I felt a wave of panic wash over me as I realized the gravity of the situation.)"
    x "(I was completely at his mercy, and I had no way out of this.)"
    x "(I had to say something to try and stop him.)"
    
    show madd violated at left_small
    with dissolve
    x "Please dad, don't do this. Anything but this."
    
    show dad cruel at right_small
    with dissolve
    dad_says "Silence!"
    show dad dominant at right_small
    with dissolve
    dad_says "You brought this on yourself."
    
    show madd violated at left_small
    with dissolve
    x "Please dad, I beg you. If you do this my life will be ruined."
    
    show dad authoritative at right_small
    with dissolve
    dad_says "Enough!"
    
    scene scene_madd_interrupt_dad_meeting_event_two_throat_grab
    with fade
    
    show madd shocked at left_small
    with dissolve
    x "(Suddenly his hand comes at my throat and grabs it tightly.)"
    x "(I can't breathe. The pressure is immense.)"
    
    show dad angry at right_small
    with dissolve
    dad_says "Did I warn you or not?"
    show dad possessive at right_small
    with dissolve
    dad_says "About not messing with me?"
    
    show madd paralyzed at left_small
    with dissolve
    x "(I nodded silently, unable to speak as he squeezed my throat.)"
    x "(Stars are appearing in my vision. I'm starting to black out.)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "I tried to be a loving father to you."
    show dad coercive at right_small
    with dissolve
    dad_says "But you just don't seem to understand your place."
    
    show madd distressed at left_small
    with dissolve
    x "(My lungs are screaming for air.)"
    x "(I'm completely helpless, completely under his control.)"
    
    show madd violated at left_small
    with dissolve
    x "Please dad, I will do anything. Just no penetration."
    
    show dad calculating at right_small
    with dissolve
    dad_says "Like you are in any position to negotiate."
    show dad calculating at right_small
    with dissolve
    dad_thinks "(She just stood up to me. If I penetrate her now and if she goes to the cops, she'll have evidence.)"
    show dad obsessed at right_small
    with dissolve
    dad_thinks "(Maybe I can let it slide this time. Teach her a lesson without going all the way.)"
    show dad cruel at right_small
    with dissolve
    dad_thinks "(But I'm going to make sure she knows who owns her.)"
    
    show madd hopeful at left_small
    with dissolve
    x "(He released my throat and I gasped for air desperately.)"
    x "(My heart was racing in my chest.)"
    x "(I knew I had narrowly avoided a worse fate, but I was still terrified of what was to come.)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "Fine. But I'm going to give you something."
    show dad predatory at right_small
    with dissolve
    dad_says "And you have to drink it... down to the very last drop."
    
    scene scene_madd_interrupt_dad_meeting_event_two_pants_down
    with fade
    
    show madd paralyzed at left_small
    with dissolve
    x "(He then lowers his shorts and boxers to his knees, revealing his erect dick.)"
    x "(It's hard, throbbing, and ready.)"
    
    show dad fixated at right_small
    with dissolve
    dad_thinks "(She's going to remember this. Every. Single. Second.)"
    
    show madd horrified at left_small
    with dissolve
    x "(He puts his hands on my shoulders and pushes me down.)"
    x "(I slowly descend... on my knees.)"
    x "(The floor is cold against my skin.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I was now at his crotch level, and I could see his dick clearly.)"
    x "(He was fully erect, and I could see the veins bulging on his shaft.)"
    x "(The heat radiating from him is intense.)"
    
    show dad obsessed at right_small
    with dissolve
    dad_says "This is where you belong Maddie , between my knees."
    
    show madd trembling at left_small
    with dissolve
    x "(He grabbed my hair firmly and pulled my head closer to his dick.)"
    x "(I could feel the heat radiating from his body as he positioned himself in front of my face.)"
    x "(I knew what was coming next, and I felt a wave of nausea wash over me.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I didn't resist this time. I just closed my eyes and waited for the inevitable.)"
    
    scene scene_madd_interrupt_dad_meeting_event_two_oral_forced
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    
    show madd shocked at left_small
    with dissolve
    x "(He pushed his dick into my mouth, and I felt a strange sensation.)"
    x "(I could feel the rough texture of his skin against my lips, and the warmth of his dick inside my mouth.)"
    x "(The salt taste hits immediately.)"
    
    scene scene_madd_interrupt_dad_meeting_event_two_oral_forced_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")


    show madd nauseated at left_small
    with dissolve
    x "(I tried to suppress my gag reflex, but it was no use. I felt like I was going to vomit.)"
    x "(He started thrusting his dick into my mouth.)"
    x "(It was so deep I felt like it was going down my throat.)"
    x "(He forced my head all the way till my chin touched his scrotum and my nose touched his hairy crotch)"
    x "(Small strangs of his hair enter my nose , it was already hard to breath without his pubic hair entering my orfices )"


    scene scene_madd_interrupt_dad_meeting_event_two_oral_forced_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd distressed at left_small
    with dissolve
    x "(he started pounding me with more force now , as involuntary moans escaped my mouth )"
    x "(I could feel the pressure building up inside me as he thrust harder and harder.)"
    x "(He wasn't moving himself. He was using my head to bob up and down on his dick.)"
    x "(I had no choice but to go along with it.)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "Know your place whore, you dare interrupt my life."
    

    scene scene_madd_interrupt_dad_meeting_event_two_oral_forced_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")    


    show madd violated at left_small
    with dissolve
    x "(I was reduced to a ragdoll in his hands, completely at his mercy.)"
    x "(I could feel his dick hitting the back of my throat with every thrust.)"
    x "(The sound it created as it hit the back of my throat made my whole body shake ,I couldnt believe it was coming out of me)"
    x "(I felt it growing wetter and wetter in my mouth.)"
    

    scene scene_madd_interrupt_dad_meeting_event_two_oral_forced_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows") 

    show madd distressed at left_small
    with dissolve
    x "(The taste changed too. It was salty and bitter.)"
    x "(I felt like I was drowning in it.)"
    x "(It was radiating more heat now.)"
    
    show madd traumatized at left_small
    with dissolve
    x "(On my tongue I felt his dick pulsing.)"
    x "(I realized he was close.)"
    x "(My stomach churned with anticipation and dread.)"
    


    show madd horrified at left_small
    with dissolve
    x "(I felt a sudden surge as he started to thrust harder and faster.)"
    x "(Now he was moving himself too along with my head.)"
    x "(This created a new sensation... a friction that was intense.)"
    x "(I felt like my mouth was on fire.)"
    

    show dad obsessed at right_small
    with dissolve
    dad_says "Drink it all slut"
    dad_says "Remember Maddie if you dont yield to being my personal whore daughter , I will make you become a toilet for the whole house"
    dad_says "I will even let adam use you while we play Playstation " 

    scene scene_madd_interrupt_dad_meeting_event_two_oral_forced_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows") 

    show madd shocked at left_small
    with dissolve
    x "(Then I felt it... the first spurt of his seed shooting into my mouth.)"
    x "(It was hot and thick... filling my mouth completely.)"
    x "(It was salty and bitter... and had a distinct smell too.)"
    x "(It smelled like foul eggs.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I tried to swallow it all down. I had no choice.)"
    x "(But some part of me felt relieved.)"
    x "(Maybe now it would be over.)"
    
    show madd violated at left_small
    with dissolve
    x "(I tried to swallow it all down. I had no choice.)"
    x "(He did warn me after all. This was my last chance.)"
    
    show dad possessive at right_small
    with dissolve
    dad_thinks "(She's mine now. Completely mine.)"
    
    show madd distressed at left_small
    with dissolve
    x "(He finally stopped moving but kept his dick in my mouth.)"
    x "(It kept pulsing for a while... then slowly it started to soften.)"
    x "(My mouth was filled with his seed.)"
    x "(I started swallowing it down slowly... drop by drop.)"
    


    show madd broken at left_small
    with dissolve
    x "(I felt as if every drop I swallowed was a defeat.)"
    x "(But I had no choice.)"
    x "(I looked up at him.)"
    x "(He didn't look satisfied yet.)"
    


    show dad cruel at right_small
    with dissolve
    dad_says "Remember, I told you... to drink it all."
    show dad dominant at right_small
    with dissolve
    dad_thinks "(Time for the second part of her medicine.)"
    


    scene scene_madd_interrupt_dad_meeting_event_two_oral_forced_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows") 
    
    show madd shocked at left_small
    with dissolve
    x "(As soon as he said that, he grabbed my hair again and pushed his dick deeper into my mouth.)"
    x "(Even though it was softening now, it was almost reaching my throat.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(Then I felt it. His dick was pulsing again.)"
    x "(Another fluid came shooting into my mouth.)"
    x "(But this time it was different.)"
    x "(It was thinner and more watery. It had a different taste too.)"
    
    show scene_madd_interrupt_dad_meeting_event_two_oral_forced_drinking_urine at topleft
    with Dissolve(2.0)

    show madd horrified at left_small
    with dissolve
    x "(Oh no.)"
    x "(It was... his urine.)"
    x "(He was peeing into my mouth.)"
    
    show dad obsessed at right_small
    with dissolve
    dad_says "This is how animals mark their territory. And you are my territory now"
    dad_says "You already live in my house , this is how whores like you pay rent isnt it ?"

    
    show madd traumatized at left_small
    with dissolve
    x "(I wanted to pull away.)"
    x "(But his grip on my hair was too strong and I had no choice.)"
    x "(I was being used like a filthy urinal.)"
    
    show madd violated at left_small
    with dissolve
    x "(As his dick was reaching my throat I couldn't even stop the flow.)"
    x "(It was directly going down my throat.)"
    x "(Mixing with his seed.)"
    x "(All inside my stomach now.)"
    x "(I felt so dirty. So humiliated.)"
    
    show madd broken at left_small
    with dissolve
    x "(This is how low I've sunk.)"
    x "(To be used like this.)"
    x "(By my own dad.)"
    x "(This is how animals mark their territory.)"
    x "(I've become his property.)"
    x "(His filthy little cumdump.)"
    
    show madd distressed at left_small
    with dissolve
    x "(It kept going and going.)"
    x "(I felt like it would never stop.)"
    x "(I could feel my stomach swelling up.)"
    x "(Filled with his disgusting fluids.)"
    
    show dad possessive at right_small
    with dissolve
    dad_thinks "(Now she carries a part of me inside her. She's marked. She's mine.)"
    
    hide scene_madd_interrupt_dad_meeting_event_two_oral_forced_drinking_urine

    show madd violated at left_small
    with dissolve
    x "(Finally, after what felt like an eternity, he stopped.)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "Good girl. You've done well."
    show dad controlling at right_small
    with dissolve
    dad_thinks "(She's learning. Finally learning.)"
    
    scene scene_madd_interrupt_dad_meeting_event_two_after_oral
    with fade
    
    show madd broken at left_small
    with dissolve
    x "(He finally let go of my hair.)"
    x "(I collapsed onto the floor, gasping for air.)"
    x "(My mouth was still filled with the taste of his seed and urine.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(I felt so ashamed.)"
    x "(So degraded.)"
    x "(But at the same time... a small part of me felt relieved.)"
    x "(It's over now. I've survived it. For now.)"
    
    show madd traumatized at left_small
    with dissolve
    x "(But deep down, I know this isn't the end.)"
    x "(Not by a long shot.)"
    x "(He'll be back.)"
    x "(And next time, who knows what he'll make me do.)"
    x "(I just have to stay strong.)"
    x "(And hope for a way out of this nightmare.)"
    
    show dad coercive at right_small
    with dissolve
    dad_says "Remember, the taste of my seed and urine will always be with you."
    show dad possessive at right_small
    with dissolve
    dad_says "You're mine now."
    show dad cruel at right_small
    with dissolve
    dad_says "Next time you try to sabotage me, you'll remember this moment."
    show dad obsessed at right_small
    with dissolve
    dad_says "And you'll obey me without question."
    
    show madd submissive nod at left_small
    with dissolve
    x "(Even after he pulled away, I could still taste his seed and urine in my mouth.)"
    x "(A constant reminder of my degradation.)"
    x "(I knew I had to find a way out of this situation.)"
    x "(Before it got any worse.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(Slowly and slowly he is upping the stakes.)"
    x "(Testing my limits.)"
    x "(Breaking me down piece by piece.)"
    x "(I have to stay strong.)"
    x "(And find a way to escape.)"
    x "(Before it's too late.)"
    
    show dad authoritative at right_small
    with dissolve
    dad_says "Now get up and clean yourself."
    show dad cruel at right_small
    with dissolve
    dad_says "Now, because of your shenanigans, you're going to have additional punishments to endure."
    
    show madd weeping at left_small
    with dissolve
    x "(I slowly got up from the floor, still feeling weak and humiliated.)"
    x "(I went over to my clothes to put them on.)"
    x "(Trying to ignore the lingering taste in my mouth.)"
    
    scene scene_madd_interrupt_dad_meeting_event_two_after_oral_aftermath_madd_crying
    with fade


    show madd anxious at left_small
    with dissolve
    x "(He was walking away now, but he didn't shut the door completely.)"
    x "(I could still hear his footsteps fading away into the distance.)"
    
    show madd distressed at left_small
    with dissolve
    x "(There was complete silence now.)"
    x "(Except for the sound of my own breathing.)"
    
    show madd horrified at left_small
    with dissolve
    x "(As I was putting on my clothes I heard the sound of locking.)"
    x "(Not of his room door.)"
    x "(It was in the distance. Possibly the brother's room or the main door.)"
    x "(But it was definite. Someone locked a door.)"
    
    show madd trembling at left_small
    with dissolve
    x "(Then I heard more footsteps.)"
    x "(Then another lock sound.)"
    x "(Someone else locking a door.)"
    x "(This one felt closer.)"
    x "(The direction suggested it was my room door.)"
    
    show madd feels violated at left_small
    with dissolve
    x "(My heart started racing.)"
    x "(What is he doing?)"
    x "(Why is he locking my room?)"
    
    show madd nervous at left_small
    with dissolve
    x "(I quickly finished putting on my clothes and stood up.)"
    x "(My heart was pounding in my chest.)"
    x "(I saw dad walking back into the room, jingling some keys.)"
    
    scene scene_madd_interrupt_dad_meeting_event_one_madd_facing_dad_end
    with fade

    show dad dominant at right_small
    with dissolve
    dad_says "I've locked your room and the main door."
    show dad controlling at right_small
    with dissolve
    dad_says "So you can't leave."
    
    show madd horrified at left_small
    with dissolve
    x "(My blood ran cold.)"
    
    show dad coercive at right_small
    with dissolve
    dad_says "Now you have 3 options."
    show dad cruel at right_small
    with dissolve
    dad_says "You can either sleep here in my room..."
    show dad dominant at right_small
    with dissolve
    dad_says "Or in your brother's room..."
    show dad possessive at right_small
    with dissolve
    dad_says "Or you sleep in the living room."
    show dad controlling at right_small
    with dissolve
    dad_says "Your choice. But remember... you are not going anywhere... until I say so."
    
    show madd feels violated at left_small
    with dissolve
    x "(I felt a wave of panic wash over me.)"
    x "(Trapped in this house with him.)"
    x "(Unable to escape.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I looked at him, pleading silently for some mercy.)"
    x "(But I knew it was useless.)"
    
    show madd processing at left_small
    with dissolve
    x "(If I start sleeping in his room he would definitely do worse things to me.)"
    x "(If I start sleeping in my brother's room he would definitely take advantage of me too.)"
    x "(The living room... they both will take turns abusing me there.)"
    
    show madd broken at left_small
    with dissolve
    x "(I had no choice now.)"
    x "(I was completely at their mercy.)"
    x "(Well, I'll decide later when it's nighttime.)"
    x "(For now, I have to just survive the day.)"
    scene scene_dad_whisper_after_zoom_interview_break
    with fade

    show dad authoritative at right_small
    with dissolve
    dad_says "And remember... any attempt to escape."
    show dad sadistic at right_small
    with dissolve
    dad_says "Or contact anyone outside this house..."
    show dad controlling at right_small
    with dissolve
    dad_says "Will result in even harsher punishments."
    
    show madd submissive nod at left_small
    with dissolve
    x "(I nodded silently.)"
    x "(Too scared to speak.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I started to walk out of the room.)"
    x "(My mind racing with fear and uncertainty.)"
    x "(I have to find a way out of this nightmare.)"
    x "(Before it's too late.)"
    
    $ madd_willpower=max(0,madd_willpower-20)
    $ journal_event_set_done("Dad", "Second Interruption")
    call advance_time_and_check(minutes=90) from _call_advance_time_and_check_52
    $ character_relations["dad"]["intimacy"] += 9
    $ character_relations["dad"]["dominance"]=character_relations["dad"]["dominance"]+10
    $ character_relations["dad"]["kissed"] += 1
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["oral_sex"] += 1
    $ character_relations["dad"]["pissed_in_mouth"] += 1
    $ character_relations["dad"]["lust"]=0
    $madd_interrupt_dad_meeting_count+=1
    $ locked_home_areas.append("madd_home_room")
    $ locked_home_areas.append("home_main_door")
    $research_cram_schools=0
    # Store that room is locked (flag starts false, will be set to true when unlocked)
    $ madd_room_got_unlocked = False
    $ journal_event_show("Dad", "Sleep in Dad's Room")
    $ journal_event_show("Dad", "Sofa Sleep")
    $ journal_event_show("Brother", "Ask to Sleep in Brother's Room")
    $ journal_event_show("Brother", "Sofa Sleep")
    $ journal_event_show("Dad", "Room Intrusion: Anal")

    jump home_areas


#KNOCK AT 11 EVENT


label dad_morning_knock_at_11_event:
    show madd nervous at left_small
    with dissolve
    x "(I take a deep breath and raise my hand to knock, my heart already pounding nervously.)"
    scene dad_morning_knock_at_11_event_dad_at_door
    with fade

    show madd shocked at left_small
    with dissolve
    x "(But before my knuckles can even make contact with the door, it suddenly swings open—as if he was waiting for this moment.)"
    
    show madd anxious at left_small
    with dissolve
    x "(Step Father is standing right there in the doorway, his expression immediately darkening as he sees me.)"
    
    show dad predatory at right_small
    with dissolve
    dad_thinks "(Perfect. She came. Right on schedule. How... convenient.)"
    
    show dad possessive at right_small
    with dissolve
    dad_says "I was hoping you'd stop by. I've been waiting all morning."
    
    show madd horrified at left_small
    with dissolve
    x "(The casual way he says it sends a shiver down my spine. There's nothing casual about his gaze.)"
    
    show madd trembling at left_small
    with dissolve
    x "(Before I can even respond or take a step back, his hand shoots out and grabs my wrist firmly.)"
    
    scene dad_morning_knock_at_11_event_dad_at_door_grab_madd_arm
    with fade
    
    show madd paralyzed at left_small
    with dissolve
    x "(With surprising strength, he pulls me inside the room in one sharp motion, closing the door behind me with a soft but deliberate click.)"
    
    show madd distressed at left_small
    with dissolve
    x "(As soon as the door closes and I hear the lock engage, panic floods through my entire body.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall
    with fade

    show madd helpless at left_small
    with dissolve
    x "(He immediately pushes me against the adjacent wall, pinning me there with his body. I'm trapped.)"
    
    show madd violated at left_small
    with dissolve
    x "(His eyes are dark and intense, burning with an obsessive desire as his gaze traces over every inch of me.)"
    
    show dad lustful at right_small
    with dissolve
    dad_thinks "Fucking HR meeting ruined my entire day. But having my way with her... makes all my frustration go away."
    
    show dad obsessed at right_small
    with dissolve
    dad_thinks "She's so innocent. So pure. I can't wait till all that changes ."
    
    show madd nauseated at left_small
    with dissolve
    x "(I can feel his gaze lingering on me, analyzing me, possessing me with my eyes alone. My skin crawls at the intensity.)"
    
    show madd distressed at left_small
    with dissolve
    x "(Then his hands begin to move across my body, exploring without asking, taking without permission.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_hands_on_shoulder
    with fade

    show madd stressed at left_small
    with dissolve
    x "(He places one hand firmly on my shoulder, pressing me harder against the wall, trapping me in place.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I'm locked in this space with him, completely unable to escape his grasp or his intentions.)"
    
    show madd violated at left_small
    with dissolve
    x "(I try to stay calm, to steady my breathing, hoping desperately that he might stop, but in my heart, I know what's coming.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(How many times have I ended up in this exact situation? How many times will this happen before I can finally escape?)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(Fear, anger, and helplessness swirl inside me in a dizzying mix.)"
    
    show madd flustered at left_small
    with dissolve
    x "(His free hand begins to move upward toward my chest, his fingers tracing the outline of my ribs.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_breast_groping
    with fade

    show madd blush at left_small
    with dissolve
    x "(He begins groping me, his touch possessive and crude.)"
    
    show madd deep blush at left_small
    with dissolve
    x "(My silk t-shirt is thin, and I can feel the texture of his palm easily sliding across my skin beneath the fabric.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(He's running his hand over my breast repeatedly, squeezing it with increasing pressure, as if testing the give of my flesh.)"
    
    show dad dominant at right_small
    with dissolve
    dad_thinks "Mmm... this young body. God, how I've missed this."
    
    show dad hungry at right_small
    with dissolve
    dad_thinks "Her skin is so soft. I can never get enough of this feeling."
    
    show madd paralyzed at left_small
    with dissolve
    x "(I just stand there, frozen, enduring his unwanted advances as my disgust grows with each passing second.)"
    
    show madd anxious at left_small
    with dissolve
    x "(Then his hand moves lower, stopping at the hem of my shirt. He pauses for a moment, savoring the anticipation.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_hand_under_shirt
    with fade

    show madd horrified at left_small
    with dissolve
    x "(He lifts the fabric slightly, exposing a strip of my bare midriff to his wandering gaze.)"
    
    show madd processing at left_small
    with dissolve
    x "(Next, he slides his hand beneath my shirt, his fingers grazing directly across my bare skin now.)"
    
    show madd trembling at left_small
    with dissolve
    x "(His touch starts at my stomach, but then he moves his hand upward, trailing toward my breast.)"
    
    show madd stressed at left_small
    with dissolve
    x "(I can feel the heat of his palm as it presses firmly against me.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_hand_under_shirt_groping_tits
    with fade

    show madd distressed at left_small
    with dissolve
    x "(He reaches my breast—and since I'm not wearing a bra today, his hand cups it completely, his fingers spreading across the tender flesh.)"
    
    show madd shaken at left_small
    with dissolve
    x "(He squeezes it forcefully, kneading it like dough, making my heart race with a sickening mixture of fear and revulsion.)"
    
    show madd violated at left_small
    with dissolve
    x "(I try to avert my gaze, to look away anywhere but at his face, hoping to mentally escape even though my body is trapped.)"
    
    show dad lecherous at right_small
    with dissolve
    dad_says "I love your skin. It's so soft and smooth."
    
    show dad possessive at right_small
    with dissolve
    dad_says "You know, we should do this more often. Don't you think? Just you and me."
    
    show madd shocked at left_small
    with dissolve
    x "(I look at him, opening my mouth to protest, to say something—anything—but no words come out. Nothing. My voice has abandoned me.)"
    
    show madd violated at left_small
    with dissolve
    x "(He continues to grope me for a few more moments, clearly savoring this forbidden touch, this stolen intimacy.)"
    
    show madd horrified at left_small
    with dissolve
    x "(Finally, he releases my breast, though his hand remains beneath my shirt.)"
    
    show dad perverted at right_small
    with dissolve
    dad_says "I've been so frustrated at work today. All that stress, all those incompetent people..."
    
    show dad controlling at right_small
    with dissolve
    dad_says "Will you help your... husband... relax?"
    
    show madd horrified at left_small
    with dissolve
    x "(I want to correct him—to scream that he is absolutely not my husband, that he's my step-father, that this is wrong—but I stay silent.)"
    
    show madd anxious at left_small
    with dissolve
    x "(Resistance only makes things worse.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I just nod slightly, praying desperately that this nightmare will end soon, that he'll be satisfied and leave me alone.)"
    
    show dad manipulative at right_small
    with dissolve
    dad_thinks "Obedient little thing. She barely resists anymore. Soon, she'll completely replace her mother in my heart. In my bed."
    
    show madd distressed at left_small
    with dissolve
    x "(He pulls his hand out from beneath my shirt, but the violation doesn't end.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_hand_at_hem_of_shirt
    with fade

    show madd horrified at left_small
    with dissolve
    x "(Just when I think it might be over, his other hand reaches for the hem of my shirt.)"
    
    show madd trembling at left_small
    with dissolve
    x "(With both hands now, he lifts my shirt higher and higher, exposing more and more of my midriff.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(Slowly—so painfully slowly—he pulls my shirt up and over my head, tossing it aside carelessly like it means nothing.)"
    
    if character_relations["dad"]["intimacy"] < 15:
        menu:
            "Try to stop him" :
                if madd_willpower+2*(15-character_relations["dad"]["intimacy"]) >= character_relations["dad"]["lust"]:
                    show madd angry at left_small
                    x "Stop it Dad , I just came to check on you !"
                    show dad angry at right_small
                    dad_says "Fine..I was just trying to do some stress relief"
                    x "Well...I .. I am not your servant"
                    dad_says "For now...You will end up as my slave just you watch Maddie"
                    x "(He finally let go of me as i escaped the room his final words of turning into my slave still in my mind)"
                    $ character_relations["dad"]["anger"] +=20
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_117
                    $ character_relations["dad"]["intimacy"]+=3
                    call advance_time_and_check(minutes=120) 
                    $ madd_willpower=max(madd_willpower-20,0)
                    jump home_areas
                else:
                    $character_relations["dad"]["lust"]=0
                    $character_relations["dad"]["anger"] +=20
                    show madd trembling at left_small
                    x "(I wanted to stop him, but i was so scared that i couldnt even say anything, my voice was trembling and my body was shaking)"
                    x "(I just stood there, letting him do whatever he wanted to me, hoping that it would be over soon )"
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_118


    scene scene_dad_event_at_11_madd_pushed_against_wall_shirt_removed_madd_topless
    with fade

    show madd violated at left_small
    with dissolve
    x "( I'm now standing topless in front of him, my bare chest exposed to his hungry gaze.)"
    
    show madd helpless at left_small
    with dissolve
    x "(The cool air of the room hits my skin, raising goosebumps across my body.)"
    
    show dad obsessed at right_small
    with dissolve
    dad_says "God, look at that. Your body is so beautiful. So young, so fresh. I can't get enough of it."
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_topless_groping_breast
    with fade

    show madd shocked at left_small
    with dissolve
    x "(As soon as the words leave his lips, he places one of his hand on my bare breasts.)"
    
    show madd distressed at left_small
    with dissolve
    x "(He begins kneading them firmly, roughly, his fingers digging into my sensitive flesh.)"
    
    show madd trembling at left_small
    with dissolve
    x "(I can feel the warmth of his hands as they move over my skin, possessive and violent in their intent.)"
    
    show madd shaken at left_small
    with dissolve
    x "(On both breasts, he's using his index fingers to dig into my nipples, applying painful pressure.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(It hurts—it genuinely hurts—but I can do nothing to stop him, nothing to make him stop.)"
    
    show madd conflicted at left_small
    with dissolve
    x "( But strangely, I feel a complex mix of sensations building inside me—part terror, part unwanted arousal that disgusts me.)"
    
    show madd blush at left_small
    with dissolve
    x "(His hands keep moving over my breasts, squeezing and massaging, claiming ownership of my body.)"
    
    show madd deep blush at left_small
    with dissolve
    x "( I can feel my nipples hardening under his touch, responding to his manipulation despite my mental resistance.)"
    
    show madd self loathing at left_small
    with dissolve
    x "( I hate this. I hate him for making my body respond this way. I hate myself for feeling this way.)"
    
    show dad fixated at right_small
    with dissolve
    dad_thinks "Hmm... her nipples are hardening. What a beautiful sight to behold."
    
    show dad predatory at right_small
    with dissolve
    dad_thinks "That definitely means she's enjoying my touch. Time to move things further along."
    
    show madd anxious at left_small
    with dissolve
    x "(Then, without any warning, he leans in closer to me, towering over me.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_dad_leaning_in_to_kiss_hand_on_breast
    with fade

    show madd nervous at left_small
    with dissolve
    x "(His lips are approaching mine, his breath becoming increasingly present.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I can smell his breath now—the familiar stench of alcohol and cigarettes that usually repels me.)"
    
    show madd conflicted at left_small
    with dissolve
    x "( But inexplicably, today it doesn't. For some twisted reason, it seems... intoxicating.)"
    
    show madd flustered at left_small
    with dissolve
    x "(Maybe it's because his hands are still massaging my breasts that some part of me has been chemically rewired to respond.)"
    
    show madd horrified at left_small
    with dissolve
    x "(His face is just inches away from mine now, so close I can feel the heat radiating from him.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(His lips are almost touching mine, hovering just out of contact for a torturous moment.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I can feel his breath directly on my lips now, warm and insistent.)"
    
    show madd violated at left_small
    with dissolve
    x "(Suddenly, he closes the gap completely, his lips pressing hard against mine in a forceful, dominating kiss.)"
    show madd violated at left_small
    with dissolve
    x "(The suddenness of it catches me completely off guard. My mind races with conflicting emotions.)"
    
    show madd helpless at left_small
    with dissolve
    x "(His lips are rough and demanding against mine, claiming my mouth, leaving me feeling trapped and utterly powerless.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(I can feel his hands still on my breasts, squeezing, adding to the overwhelming sensation of violation.)"
    
    show madd distressed at left_small
    with dissolve
    x "(He moves his lips against mine with deliberate aggression, caressing them roughly, almost violently.)"
    
    show madd shocked at left_small
    with dissolve
    x "(Then he pulls away from the kiss, looking at me with a mix of frustration and desire.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_dad_leaning_in_to_kiss_hand_on_breast_with_dad_kissing_madd_neck_front
    with fade

    show madd flustered at left_small
    with dissolve
    x "(Then immediately he goes to kissing my neck, biting and sucking on the sensitive skin there.)"
    
    show madd trembling at left_small
    with dissolve
    x "(I felt a shiver run down my spine as his lips trailed lower, his hands roaming over my body.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(That touch was electrifying, sending waves of pleasure through me despite the situation.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "( I did not like what was happening, but part of me couldn't help but respond to his touch.)"
    
    show madd violated at left_small
    with dissolve
    x "(His hands were still on my breasts, squeezing and caressing them roughly.)"
    
    show madd flustered at left_small
    with dissolve
    x "(But the neck kissing was making me feel things I didn't want to feel.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(At this point I was conflicted, torn between my discomfort and the involuntary reactions of my body.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(Even though these acts with my stepfather were forbidden and wrong, my body betrayed me with its responses.)"
    
    show madd distressed at left_small
    with dissolve
    x "(His wet tongue tracing patterns on my neck, his hands gripping my breasts firmly.)"
    
    show madd helpless at left_small
    with dissolve
    x "( I know he wasn't trying to write any words with his tongue, but whatever he was doing it felt like he was saying I belong to him.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(Then he pulled back slightly, looking into my eyes with a possessive intensity.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_dad_leaning_in_to_kiss_hand_on_breast_with_dad_tongue_in_mouth_tightgrope
    with fade    
    
    show madd resigned at left_small
    with dissolve
    x "(Then immediately he went back to kissing my mouth, his hands still on my breasts.)"



    show madd helpless at left_small
    with dissolve
    x "(This isn't a passionate kiss—it's a dominating one. It's a statement of possession.)"
    
    show dad coercive at right_small
    with dissolve
    x "( Then I feel it—unmistakably his tongue—forcing its way into my mouth without consent.)"



    show dad sadistic at right_small
    with dissolve
    x "(He's using his tongue like a weapon, drilling into my mouth, asserting control over every part of me.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "( I try to keep my mouth closed, to maintain this one last barrier, and he definitely notices my resistance.)"
    
    show madd shocked at left_small
    with dissolve
    x " (So he squeezes my breasts harder—almost painfully hard—forcing me to gasp involuntarily.)"
    
    show scene_dad_event_at_11_tongue_pushes_inside_madd_mouth at topleft
    with Dissolve(2.0)

    show madd nauseated at left_small
    with dissolve
    x "( He uses that moment of surprise to force his tongue deeper into my mouth.)"
    
    show madd disgusted at left_small
    with dissolve
    x "(I feel a wave of disgust and confusion as his tongue invades my intimate space.)"
    
    show madd distressed at left_small
    with dissolve
    x "( Along with his tongue comes his saliva, filling my mouth with its bitter, unpleasant taste.)"
    
    show madd nauseated at left_small
    with dissolve
    x "( As his tongue moves around inside my mouth, he uses it to transfer saliva from his mouth directly into mine.)"
    
    show madd violated at left_small
    with dissolve
    x "(He's literally marking me from the inside, making me ingest part of him.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "( The more I swallow, the more I feel the urge to gag, to reject this invasion.)"
    
    show dad horny at right_small
    with dissolve
    dad_thinks "Yes... this is exactly what I needed to do. "
    
    show dad possessive at right_small
    with dissolve
    dad_thinks " The more of my fluids I can get into her system, the more she'll be bound to me. There will be no escape."
    
    hide scene_dad_event_at_11_tongue_pushes_inside_madd_mouth


    show madd distressed at left_small
    with dissolve
    x "(After what feels like an eternity of violation, he finally pulls away from the kiss.)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "Did you like that? Did you enjoy my kiss? I felt your nipples hardening dont lie to me."
    
    show madd trembling at left_small
    with dissolve
    x "(I'm breathless and thoroughly shaken, struggling desperately to process what just happened to me.)"
    
    show madd conflicted at left_small
    with dissolve
    x "Yes... I... I liked it..."
    
    show madd resigned at left_small
    with dissolve
    x "(I lie, my voice hollow and uncertain, knowing that compliance is my only armor against further escalation.)"
    
    show dad perverted at right_small
    with dissolve
    x "(He smirks—that cruel, satisfied expression spreading across his face.)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "Good girl. Very good. Eventually, you're going to learn to genuinely enjoy these moments with me."
    
    show dad lustful at right_small
    with dissolve
    dad_says "Maybe one day you'll even beg me for them. "
    
    show madd self loathing at left_small
    with dissolve
    x "(Like hell I would ever reach that point.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I just nod silently, eager for any part of this ordeal to end, wishing I could disappear.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_dad_hands_on_waist_tugging_down_shorts
    with fade

    show dad calculating at left_small
    with dissolve
    x "(Then his hands move downward, toward my waist, toward my shorts.)"
    
    show dad possessive at right_small
    with dissolve
    x "(He begins tugging at the waistband of my shorts with deliberate, measured movements.)"
    
    show madd anxious at left_small
    with dissolve
    x "(Slowly—so agonizingly slowly—he starts pulling them down over my hips.)"
    
    show madd trembling at left_small
    with dissolve
    x "(He's doing it very slowly, clearly savoring every moment, every inch of skin revealed.)"

    scene scene_dad_event_at_11_madd_pushed_against_wall_dad_hands_on_waist_tugging_down_shorts_halfway
    with fade

    show madd violated at left_small
    with dissolve
    x "(He keeps his hands pressed against my skin as he pulls the shorts down, caressing my butt as the fabric slides away.)"
    
    show madd distressed at left_small
    with dissolve
    x "(As my shorts reach halfway down my buttocks, he pauses to take his time caressing my bare skin.)"
    
    show madd helpless at left_small
    with dissolve
    x "(Slowly, he pulls my shorts all the way down, finally exposing my bare legs and buttocks completely.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_fully_naked
    with fade

    show madd horrified at left_small
    with dissolve
    x "(I'm now standing completely naked before him—vulnerable, exposed, and defenseless.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(The walls of the room seem to close in on me as I stand exposed.)"
    
    show dad lustful at right_small
    with dissolve
    dad_says "What an absolutely angelic body you have. Truly breathtaking."
    
    show dad fixated at right_small
    with dissolve
    x "(He admires my naked form with hungry eyes, his gaze roaming over every inch of my exposed skin.)"
    
    show madd violated at left_small
    with dissolve
    x "(Then his gaze moves downward, focusing with intense fixation on my pussy.)"
    
    show madd helpless at left_small
    with dissolve
    x "(I can feel his eyes burning into me there, lingering, making me feel stripped bare not just physically but emotionally exposed and vulnerable.)"
    
    show dad fixated at right_small
    with dissolve
    dad_says "Your pussy is so beautiful. So soft and inviting. So perfect."
    
    show dad hungry at right_small
    with dissolve
    dad_says "I could lose myself in it for hours. Just diving into it, drowning in you."
    
    show madd nauseated at left_small
    with dissolve
    x "(I feel a wave of revulsion wash over me at his crude words. How can someone say that to your face !)"
    
    show madd distressed at left_small
    with dissolve
    x "(I want to cover myself, to hide from his leering, possessive gaze, to make myself invisible.)"
    
    show madd violated at left_small
    with dissolve
    x "(But there's nowhere to hide. I'm completely exposed.)"
    
    show madd processing at left_small
    with dissolve
    x "(Then his gaze returns to my face, as if checking something.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I assume he's searching for signs of my defeat and complete submission in my expression.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_naked_grope_ass
    with fade

    show dad dominant at right_small
    with dissolve
    x "(He slowly moves his hand across my buttocks in a possessive caress.)"
    
    show madd flustered at left_small
    with dissolve
    x "( After each squeeze of my butt, he delivers a light slap, testing my reaction.)"
    
    show madd violated at left_small
    with dissolve
    x "(I can feel the warmth of his palms as they move over my skin, claiming ownership.)"
    
    show dad obsessed at right_small
    with dissolve
    dad_thinks "Fucking hell, I can't wait any longer. I need to feel her around me."
    
    show dad coercive at right_small
    with dissolve
    dad_thinks " I want to put my dick inside her pussy right now."
    
    show dad possessive at right_small
    with dissolve
    dad_thinks " I need her. I need this. I need to be inside her now."
    
    show dad predatory at right_small
    with dissolve
    dad_thinks "How could any man resist such a beautiful young body? So untouched. So perfect."
    
    show madd distressed at left_small
    with dissolve
    x "(He seems lost in thought for a moment, but his touch grows noticeably more aggressive. The slaps on my buttocks become harder, more forceful.)"
    
    show madd shocked at left_small
    with dissolve
    x "(Suddenly, he grabs my hips with a firm grip, holding me in place.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_naked_grope_ass_spread_ass
    with fade

    show madd violated at left_small
    with dissolve
    x "(He spreads my buttocks apart with both hands, exposing me completely.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(The cold air of the room hits both my bare buttocks and pussy, making me shiver involuntarily.)"
    
    show madd anxious at left_small
    with dissolve
    x "( It's good that I'm facing him directly—at least he can't see my pussy from this angle as clearly as he'd like.)"
    
    show madd helpless at left_small
    with dissolve
    x "( Then he removes his hands from my buttocks momentarily.)"
    
    show madd trembling at left_small
    with dissolve
    x "(I feel a sudden chill as the cool air brushes against my exposed skin, raising goosebumps.)"
    
    show madd conflicted at left_small
    with dissolve
    x "( My buttocks are still hot from his earlier touch, so the cold air is almost refreshing in comparison.)"
    
    show madd horrified at left_small
    with dissolve
    x "(Then I see him unzipping his pants deliberately, pulling them down with clear intent.)"

    if character_relations["dad"]["intimacy"] < 40:
        menu:
            "Stop Him from escalating" :
                if madd_willpower+2*(40-character_relations["dad"]["intimacy"]) >= character_relations["dad"]["lust"]:
                    show madd angry at left_small
                    x "(There is no way he stops with usual methods , I have to do something different)"
                    x "Dad ...stop...I"
                    x "I ... have diarrhea . That's why i knocked on your room..."
                    x "I was too scared ... or ashamed "
                    show dad angry at right_small
                    x "(I felt his grip on me loosen as he angrily growls)"
                    dad_says "The fuck bitch, couldnt you have said that before i spread your ass"
                    x "Well...I .. I tried..."
                    dad_says "I dont have any diarrhea meds , get the fuck out of here ."
                    dad_says "You better not shit on my carpet "
                    x "(He finally let go of me as i escaped the room acting as if i was going towards the bathroom.)"
                    $ character_relations["dad"]["anger"] +=20
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_115
                    $ character_relations["dad"]["intimacy"]+=5
                    call advance_time_and_check(minutes=120) 
                    $ madd_willpower=max(madd_willpower-20,0)
                    jump home_areas
                else:
                    $character_relations["dad"]["lust"]=0
                    $character_relations["dad"]["anger"] +=20
                    show madd trembling at left_small
                    x "(I wanted to stop him, but i was so scared that i couldnt even say anything, my voice was trembling and my body was shaking)"
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_116


    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_naked_grope_ass_dad_pants_down
    with fade


    show dad obsessed at right_small
    with dissolve
    x "(He pulls his pants and underwear down, revealing his already erect dick.)"
    
    show madd shocked at left_small
    with dissolve
    x "(My heart races—partly from fear, partly from shock.)"
    
    show madd resigned at left_small
    with dissolve
    x "(It's large. Much larger than someone his age should realistically have. But I've become accustomed to it by now.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(He moves closer to me again, his erect dick pointing directly toward my exposed pussy. The heat radiating from it is almost visible. I can feel the intensity of his arousal like a physical force.)"
    
    show madd horrified at left_small
    with dissolve
    x "\"Please... don't...\""
    
    show madd broken at left_small
    with dissolve
    x "\"Not this... please...\""
    
    show dad calculating at right_small
    with dissolve
    dad_thinks "Hmm, looks like she still needs more breaking in. But that's fine. I have time."
    
    show dad dominant at right_small
    with dissolve
    dad_says " Tch, fine. I'll just use friction then. That'll do for now."
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_naked_dad_dick_rubbing_pussy_lips
    with fade

    show dad coercive at right_small
    with dissolve
    x "(He uses his hand to guide his dick directly beneath my pussy, positioning it carefully.)"
    
    show madd violated at left_small
    with dissolve
    x "( My eyes widen as soon as his dick touches my pussy lips .It never enters me, but it's positioned right at my pussy lips—close enough to feel, intimate enough to violate.)"
    show dad horny at right_small
    with dissolve
    x "(Then he starts moving his body forward, my pussy lips and my thighs serving as the friction surface for his dick. This is so intimiate , sex is just one misstep away.)"
    
    show madd deep blush at left_small
    with dissolve
    x "(I can feel the rough texture of his skin sliding against my pussy lips.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(It's intensely hot and sticky.)"
    
    show madd nauseated at left_small
    with dissolve
    x "( The pre-cum from his dick is now being smeared all over my pussy lips, creating an additional layer of wetness.)"
    
    show madd violated at left_small
    with dissolve
    x "(He's thrusting his dick against my pussy lips repeatedly, creating a wet, slippery sensation that's both intimate and violating.)"
    
    show dad lustful at right_small
    with dissolve
    dad_thinks "Yes, this is perfect. This is exactly what I needed."
    
    show dad obsessed at right_small
    with dissolve
    dad_thinks " I can't penetrate her fully yet, but this feels incredible. Just rubbing against her pussy lips like this. Can't imagine how good being inside her would feel like."
    
    show madd distressed at left_small
    with dissolve
    x "( I can feel my pussy lips being rubbed and massaged by his thrusting dick in a degrading rhythm.)"
    
    show madd feels violated at left_small
    with dissolve
    x "( His foreskin is being pulled back and forth over my pussy lips with each thrust.)"
    
    show madd helpless at left_small
    with dissolve
    x "(He keeps thrusting his dick against my pussy lips with increasing pressure.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_naked_dad_dick_rubbing_pussy_lips_and_kiss
    with fade

    show madd anxious at left_small
    with dissolve
    x "( Then his mouth comes close to my face again—this is a kiss I knew was coming.)"
    
    show madd resigned at left_small
    with dissolve
    x "( It's another forceful, dominating kiss, and this time I'm too numb to resist.)"
    
    show madd horrified at left_small
    with dissolve
    x "(I don't resist. I feel completely numb, detached from my own body and what's happening to it.)"
    
    show scene_dad_event_at_11_tongue_pushes_inside_madd_mouth at topleft
    with Dissolve(2.0)

    show madd violated at left_small
    with dissolve
    x "(His tongue invades my mouth again, mixing his saliva with mine in an act of complete domination.)"
    
    show madd distressed at left_small
    with dissolve
    x "( I'm being invaded from both ends now—my mouth and my pussy simultaneously.)"
    
    show madd conflicted at left_small
    with dissolve
    x "( Some twisted part of me is actually feeling aroused by this overwhelming situation.)"
    
    show madd self loathing at left_small
    with dissolve
    x "( But the larger part of me just feels disgust and violation washing over me.)"
    
    show dad dominant at right_small
    with dissolve
    x "(He keeps kissing me forcefully, his tongue probing deeper into my mouth as he increases the intensity and speed of his thrusts against my pussy lips.)"
    
    show dad possessive at right_small
    with dissolve
    x "( I can hear the wet friction sounds of his dick sliding against my pussy lips. It's obscene and squelchy.)"
    
    hide scene_dad_event_at_11_tongue_pushes_inside_madd_mouth

    show dad coercive at right_small
    with dissolve
    x "( Then I notice his breathing is becoming heavier and more rapid.)"
    
    show dad obsessed at right_small
    with dissolve
    x "( His thrusts against my pussy lips are getting faster and harder, more desperate.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I can feel the pressure building up inside him. His dick is throbbing against my pussy lips with increasing intensity.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_naked_dad_dick_rubbing_pussy_lips_and_kiss_dad_cums_on_pussy_lips
    with fade

    show madd shocked at left_small
    with dissolve
    x "( Suddenly, with a muffled groan that he's trying to suppress into our kiss, he climaxes.)"
    
    show madd violated at left_small
    with dissolve
    x "(I feel a warm, thick fluid spraying onto my pussy lips and down my thighs.)"
    
    show madd disgusted at left_small
    with dissolve
    x "(His cum is hot and viscous, coating my pussy lips and dripping down my legs.)"
    
    show dad perverted at right_small
    with dissolve
    x "(He continues to thrust against my pussy lips for a few more moments, ensuring that every last drop of his cum is deposited there.)"
    
    show dad possessive at right_small
    with dissolve
    x "(Finally, he stops thrusting, though his dick remains pressed against my pussy lips.)"
    
    show dad coercive at right_small
    with dissolve
    x "(He never stops kissing me through the entire climax.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_naked_dad_dick_rubbing_pussy_lips_and_stopkissing
    with fade

    show dad dominant at right_small
    with dissolve
    x "(After several more moments, he finally pulls away from the kiss.)"
    
    show dad perverted at right_small
    with dissolve
    dad_says "That felt absolutely incredible. Thank you for that."
    
    show madd distressed at left_small
    with dissolve
    x "( I just nod silently, still trying to process and accept what just happened to me.)"
    
    show madd nauseated at left_small
    with dissolve
    x "( He slowly pulls his dick away from my pussy lips. I notice that there's still a significant amount of his cum remaining on my pussy lips—I'm disgusted by it.)"
    
    show madd shocked at left_small
    with dissolve
    x "( Surprisingly, his dick is still erect, showing no signs of softening.)"
    
    show dad obsessed at right_small
    with dissolve
    dad_says "I think I need to go for another round. You've gotten me so worked up."
    
    show madd horrified at left_small
    with dissolve
    x "(I look at him in shock and horror.)"
    
    show madd broken at left_small
    with dissolve
    x "\"No... please... I can't take this anymore... I let you do as you pleased... but please don't do this again...\""
    
    show dad authoritative at right_small
    with dissolve
    dad_says "You do exactly as I say. Do you understand?"
    
    show madd broken at left_small
    with dissolve
    x "(I nod silently, too frightened and exhausted to argue or resist any further.)"
    
    show dad dominant at right_small
    with dissolve
    x "(He smirks at my complete submission, clearly satisfied with my obedience.)"
    
    show dad coercive at right_small
    with dissolve
    dad_says "Good. Now turn around. Face the wall."
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_naked_turn_around
    with fade


    show dad possessive at right_small
    with dissolve
    x "(He uses his hands to physically turn me around to face the wall directly.)"
    
    show madd anxious at left_small
    with dissolve
    x "( I plant my hands on the wall as he clearly expects me to do.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_naked_turn_around_ass_grope
    with fade

    show madd trembling at left_small
    with dissolve
    x "(Then I feel his hands on my buttocks again.)"
    
    show madd violated at left_small
    with dissolve
    x "(He starts squeezing and massaging them once more, claiming my body all over again.)"
    
    show madd helpless at left_small
    with dissolve
    x "(I can no longer see his face, but I can definitely feel his intense gaze on my exposed body.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_naked_turn_around_ass_grope_neck_kiss

    show madd distressed at left_small
    with dissolve
    x "( Then I feel his breath growing heavier on my neck.)"
    
    show dad lustful at right_small
    with dissolve
    x "( He starts kissing my neck slowly, his lips and tongue devouring it with intense focus.)"
    
    show dad possessive at right_small
    with dissolve
    x "( It's almost as if he's biting my neck—the line between pleasure and pain is blurred.)"
    
    show madd flustered at left_small
    with dissolve
    x "( It's not painful, but rather a pleasurable sensation that surprises me.)"
    
    show madd conflicted at left_small
    with dissolve
    x "( For some reason I find myself liking the way he's kissing my neck, despite everything.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_naked_turn_around_ass_grope_neck_kiss_ass_spread
    with fade

    show madd overwhelmed at left_small
    with dissolve
    x "( Then I feel his hands moving downward, toward my butt crack, spreading my buttocks apart again.)"
    
    show madd violated at left_small
    with dissolve
    x "(He spreads my buttocks apart with both hands, creating complete exposure.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(Cold air hits both my bare buttocks and pussy once again, making me shiver.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_naked_turn_around_ass_grope_neck_kiss_ass_spread_dick_between_cheeks_precumpenis
    with fade

    show madd paralyzed at left_small
    with dissolve
    x "( Then he places his dick directly between my buttocks, nestling it there. I can the head from his dick directly on my asshole)"
    x "( His dick was coated in his cum and that was being deposited on my butt. Which made the feeling all more gross.)"
    
    show madd shocked at left_small
    with dissolve
    x "(I can feel the rough texture of his skin pressing against my bare buttocks.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(His dick is large enough to be felt significantly between my buttocks.)"
    
    show madd distressed at left_small
    with dissolve
    x "(He positions the entire length of his dick between my buttocks for maximum friction.)"
    
    show madd resigned at left_small
    with dissolve
    x "( He's going to use my buttocks as the friction surface this time.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_naked_turn_around_ass_grope_neck_kiss_ass_spread_dick_between_cheeks_moving_precumpenis
    with fade

    show madd helpless at left_small
    with dissolve
    x "(Then he starts moving his body forward, beginning to thrust his dick against my bare buttocks.)"
    
    show dad possessive at right_small
    with dissolve
    x "(He continues licking and biting my neck as he thrusts his dick against my bare buttocks—multitasking in his assault.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "( His dick is so hot and sticky. The cum from earlier is still present and it makes the friction even more intense and slippery.)"
    
    show madd violated at left_small
    with dissolve
    x "( Because of the cum, it feels like there's a layer of glue between his dick and my buttocks.)"
    
    show madd feels violated at left_small
    with dissolve
    x "(He keeps thrusting his dick against my bare buttocks, creating a wet, slippery sensation.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I can feel the rough texture of his skin dragging against my sensitive skin with each thrust.)"
    
    show madd helpless at left_small
    with dissolve
    x "(He uses his hands to knead my buttocks aggressively as he thrusts his dick against them. He was spreading my ass apart so his dick could be deeper into the gap of my buttcheeks)"
    
    show dad predatory at right_small
    with dissolve
    x "(Somehow, I'm too distracted by the way he's kissing my neck that I don't immediately notice how fast his thrusting has become.)"
    
    show dad obsessed at right_small
    with dissolve
    x "( His dick is starting to throb again as he increases the speed and intensity of his thrusts.)"
    
    show madd anxious at left_small
    with dissolve
    x "( I know exactly what's coming next—I can feel it building.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_naked_turn_around_ass_grope_neck_kiss_ass_spread_dick_between_cheeks_cum_neckbite
    with fade

    show madd horrified at left_small
    with dissolve
    x "(Suddenly, he bites my neck hard—harder than before.)"
    
    show madd shocked at left_small
    with dissolve
    x "(I feel a sharp pain followed immediately by a wave of unexpected pleasure.)"
    
    show dad sadistic at right_small
    with dissolve
    x "( He's using the bite as a signal that he's about to climax. There's something so animalistic and primal about it that it sends shivers down my entire spine—shivers I find myself strangely aroused by.)"
    x "(With him suppressing his groan into the bite on my neck, he climaxes a second time.)"
    show madd overwhelmed at left_small
    with dissolve
    x "( I feel more warm, sticky fluid spraying onto my buttocks and lower back. The cum trickled down , some of it got inside my asshole. Feeling it seeping into my asshole was extremely frustrating.)"
    
    show madd violated at left_small
    with dissolve
    x "(His cum is hot and thick, coating my skin and dripping down my legs in streams.)"
    
    show dad dominant at right_small
    with dissolve
    x "(He continues to thrust against my bare buttocks for a few more moments, ensuring that every last drop of his cum is deposited there.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_naked_turn_around_ass_grope_neck_kiss_ass_spread_dick_between_cheeks_cum_neckbite_stops_kissing
    with fade

    show dad possessive at right_small
    with dissolve
    x "(Finally, he stops thrusting, though his dick remains positioned between my buttocks.)"
    
    show dad perverted at right_small
    with dissolve
    x "( Slowly he stops kissing my neck.)"
    
    show dad obsessed at right_small
    with dissolve
    dad_says "That was absolutely amazing. You are such a good girl."
    
    show dad dominant at right_small
    with dissolve
    dad_says "That was exactly the stress relief I needed. If HR offered services like this, maybe I wouldn't be so frustrated with my life all the time."
    
    show madd helpless at left_small
    with dissolve
    x "(I just stand there silently, completely exhausted and overwhelmed by everything that's happened.)"
    
    show madd broken at left_small
    with dissolve
    x "(I have nothing left to give. No words. No energy. No will.)"
    
    show madd distressed at left_small
    with dissolve
    x "(After several more moments, he finally pulls his dick away from my buttocks.)"
    
    show dad perverted at right_small
    with dissolve
    x "(He moves away from me, pulling up his pants and zipping them up with satisfaction. I turn around again so i can hide my shameful painted ass from him. Painted in his cum.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_naked_turn_around_madd_covered_in_cum_dad_dressed
    with fade

    show madd nauseated at left_small
    with dissolve
    x "( There's cum all over my lower body—covering my pussy lips, my thighs, my buttocks, and my lower back.)"
    
    show madd self loathing at left_small
    with dissolve
    x "( I feel marked, possessed, violated from the inside out.)"
    
    show madd anxious at left_small
    with dissolve
    x "(Then I see him picking up my clothes from the floor.)"
    
    show madd distressed at left_small
    with dissolve
    x "(He hands me my shorts deliberately.)"
    
    show dad manipulative at right_small
    with dissolve
    dad_says "Go on, put those on. Put them on while my cum is still fresh and wet on you."
    
    show dad possessive at right_small
    with dissolve
    dad_says "I want to see you wearing my cum. I want everyone to know that you're mine."
    
    show madd feels violated at left_small
    with dissolve
    x "(I'm shocked and deeply humiliated by his request, but I comply because I have no choice.)"
    
    scene scene_dad_event_at_11_madd_pushed_against_wall_madd_naked_turn_around_madd_covered_in_cum_dad_dressed_with_madd_putting_on_shorts
    with fade

    show madd resigned at left_small
    with dissolve
    x "( Slowly, I pull on the shorts. As I'm pulling them up, I can feel his cum squishing between my skin and the fabric.)"
    
    show madd disgusted at left_small
    with dissolve
    x "( As I pull them up fully, I can feel his cum being spread and distributed all over my lower body.)"
    
    show madd violated at left_small
    with dissolve
    x "( The shorts are acting like a spreader for his cum, redistributing it across my entire lower half.)"
    
    scene scene_dad_11_cum_shorts_visible
    with fade


    show madd helpless at left_small
    with dissolve
    x "( His cum is leaking from the shorts leg holes onto my thighs, continuing to drip.)"
    
    show madd resigned at left_small
    with dissolve
    x "( The shorts themselves are getting stained with his cum—white stains on my black shorts.)"
    
    show dad possessive at right_small
    with dissolve
    dad_thinks "Haha, she looks so perfectly cute and marked wearing my cum-stained shorts."
    
    show dad sadistic at right_small
    with dissolve
    dad_thinks "Everyone will know what she's been doing. Everyone will know she's mine."
    
    show madd resigned at left_small
    with dissolve
    dad_says "Good job, love. You did exceptionally well today. I'm very pleased with you."
    
    show dad authoritative at right_small
    with dissolve
    dad_says "Now you may leave. Get out of my room. If you help me relieve my stress like this regularly, maybe I'll actually be in a better mood at home."
    
    show madd processing at left_small
    with dissolve
    x "(I nod silently, finally eager to leave this room and escape his presence.)"
    
    show madd broken at left_small
    with dissolve
    x "(I pick up my discarded shirt from the floor carefully.)"
    
    show madd anxious at left_small
    with dissolve
    x "(I quickly put it on, trying desperately to cover up as much as possible of the cum stains on my shorts.)"
    
    show madd distressed at left_small
    with dissolve
    x "(With a final glance at him, I hurry out of the room, my heart still pounding with a complex mix of fear, shame, confusion, and something I'm too ashamed to name.)"
    
    $madd_willpower=max(0,madd_willpower-30)
    call advance_time_and_check(minutes=90) from _call_advance_time_and_check_53
    $ character_relations["dad"]["intimacy"]+= 7
    $ character_relations["dad"]["dominance"]=character_relations["dad"]["dominance"]+5
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["kissed"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["lust"]=0
    $ character_relations["dad"]["anger"]=0
    $ journal_event_set_done("Dad", "Morning Knock at 11")
    jump home_areas




# SLEEP NEXT TO HIM AT NIGHT EVENT 





label step_parent_room_scene_night_enter:
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping
    with fade
    x "(I quietly enter Dad's room at night, careful not to wake him.)"
    x "(He's asleep, lying on his back with his mouth slightly open.)"
    x "(Should I sleep next to him?)"

    $ journal_event_show("Dad", "Dad's Room Night 3")
    $ journal_event_show("Dad", "Sleep in Dad's Room")
    $ journal_event_show("Dad", "Sleep With Dad: Vaginal Night")
    
    menu:
        "Yes, sleep next to him":
            if "madd_home_room" in locked_home_areas or madd_room_got_unlocked or character_relations["dad"]["vaginal_sex"] + character_relations["dad"]["anal_sex"] >= 1 or character_relations["dad"]["intimacy"] >= 40:
                $ sleep_next_to_dad_count += 1
                show madd happy at left_small
                x "(I turn on the lamp to position myself carefully lie down next to him, trying not to disturb his sleep.)"
                x "(I have no choice. My room is ...)"

                if character_relations["dad"]["vaginal_sex"]>=1:
                    jump sleep_next_to_dad_night_vaginal
                
                if sleep_next_to_dad_count >= 3:
                    jump sleep_next_to_dad_night_after_locked_room_3
                else:
                    jump sleep_next_to_dad_night_after_locked_room

            else:
                show madd stressed at left_small
                x "Why the hell would i sleep next to him"
                call advance_time_and_check(minutes=5) from _call_advance_time_and_check_54
                jump home_areas
        "No, sleep elsewhere":
            call advance_time_and_check(minutes=5) from _call_advance_time_and_check_55
            jump home_areas


label sleep_next_to_dad_night_after_locked_room:
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_lie_next_to_dad
    with fade
    show madd anxious at left_small
    with dissolve
    x "(I lie down next to him carefully, trying not to make any sudden movements that might wake him. My hands are shaking slightly as I lower myself onto the mattress.)"
    
    show madd anxious at left_small
    with dissolve
    x "(Every part of me is already preparing for what's coming. The adrenaline is coursing through my veins, making my heart race faster than it should.)"
    
    show madd shocked at left_small
    with dissolve
    x "(But before I can even settle, his arms wrap around me and pull me against his chest. The sudden movement catches me off guard—his grip is firm, possessive, like he's been waiting for this exact moment.)"
    
    show madd shocked at left_small
    with dissolve
    x "(He was awake the whole time. Of course. He was probably just lying there in the dark, waiting for me to come to him. Testing me.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I should've known. That's what I get for being stupid enough to come in here willingly.)"
    
    show madd distressed at left_small
    with dissolve
    x "(He holds me close, real close, not giving me an inch of space. His forearms are locked around me and I can feel the hair on his arms against my skin.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I can feel his breath on my neck now—warm and heavy, with that familiar scent of whiskey and cigarettes mixed in.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(It makes my skin crawl. Not in a pleasant way. Like something's climbing across my neck, burrowing into me.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I need to stay calm. I can't let him know this affects me. Control my breathing. Relax my shoulders. Don't let him see the fear.)"
    
    show madd anxious at left_small
    with dissolve
    x "(If he sees me panic, he'll push harder. He likes it when I'm scared. It gives him more power to take.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(His hands move up and lock around my arms, holding me in place. His grip is tight enough that I can feel my circulation being cut off slightly.)"
    
    show madd helpless at left_small
    with dissolve
    x "(I can't move even if I wanted to. And God, some part of me does want to. Every instinct is screaming at me to run, but his arms are like steel bands around me.)"
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_lie_next_to_dad_licking_neck
    with fade
    
    show madd helpless at left_small
    with dissolve
    x "(He lifts his head and brings his face to my neck. I can feel him taking in a deep breath, like he's trying to smell me, memorize me.)"
    
    show madd violated at left_small
    with dissolve
    x "(I feel his tongue slide across my skin—wet and deliberate, starting from where my neck meets my shoulder and moving upward slowly.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(He's licking me slowly, enjoying it. Taking his time. Like he's savoring something delicious. And the wet warmth of his mouth on my skin makes me feel trapped and exposed at the same time.)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "I knew you'd come sleep here with me."
    
    show dad coercive at right_small
    with dissolve
    dad_says "Maybe I'll unlock your room later if you behave."
    
    show madd shocked at left_small
    with dissolve
    x "(The thought of having my room unlocked again—I don't want to feel hope. Hope is dangerous. But I feel it anyway, hot and bitter in my chest. It makes me hate myself even more.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(He keeps licking my neck, and I hate that it feels good. The sensation travels down my spine in ways I don't want to acknowledge.)"
    
    show madd flustered at left_small
    with dissolve
    x "(Part of me is actually... enjoying this. And that makes me want to throw up. My face is flushing, my breathing is getting heavier, and I'm horrified by what that means about me.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(What's wrong with me? What kind of person gets turned on by someone who's using her and that being my Dad? Who's taking from her? Am I broken? Or am I just... adapting to survive?)"
    
    show madd resigned at left_small
    with dissolve
    x "(His hands start moving down. I brace myself. This is the moment where things escalate, where my clothes start coming off.)"
    
    show madd anxious at left_small
    with dissolve
    x "(The inevitable next step. I know this dance by now. His hands will find my shirt, my shorts, and I'll be naked within minutes.)"
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_lie_next_to_dad_licking_neck_lifting_shirt
    with fade
    
    show madd distressed at left_small
    with dissolve
    x "(He grabs the hem of my shirt and starts lifting it up. The fabric brushes against my skin as it pulls away, and I feel the cool air of the room hit my bare stomach.)"
    
    show madd violated at left_small
    with dissolve
    x "(My stomach is exposed first, then more. I'm acutely aware of how vulnerable I am, how every inch of me that becomes visible gives him more to take, more to claim.)"
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_lie_next_to_dad_licking_neck_lifting_shirt_exposing_breast
    with fade
    
    show madd violated at left_small
    with dissolve
    x "(Slowly, he pulls it up until my entire upper body is bare. The cool air hits my breasts and I feel my nipples harden involuntarily. I know it was just physical response but  he'll interpret it as want.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I know what kind of night this is going to be. The shirt's completely off now, tossed aside .)"
    
    show dad lustful at right_small
    with dissolve
    dad_says "You've got a beautiful body... and you smell so good."
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_lie_next_to_dad_licking_neck_lifting_shirt_exposing_breast_initial_grope
    with fade

    show madd flustered at left_small
    with dissolve
    x "(His hands move across my stomach, then upward to my breasts. They're warm and rough, calloused from work, and they move possessively over my skin.)"
    
    show madd violated at left_small
    with dissolve
    x "(He's squeezing them, kneading them like he's claiming ownership. Like they belong to him. His thumbs are near my nipples, and I can feel every touch, every adjustment of his grip.)"
    
    show madd blush at left_small
    with dissolve
    x "(A moan escapes me. I can't stop it. It's like my body has its own brain, its own wants, separate from what I actually want.)"
    
    show madd shocked at left_small
    with dissolve
    x "(He smiles when he hears it. Like he's won something. His grip tightens, his movements become more confident, and I realize I've just given him permission to continue.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(I feel so ashamed. I can't believe I just made that noise for him. It's like I've confirmed every horrible thing he believes about me—that I'm his, that I want this, that I'm enjoying it.)"
    
    show dad hungry at right_small
    with dissolve
    dad_says "Mmm... daddy loves these... so soft..."
    
    show madd deep blush at left_small
    with dissolve
    x "(His hands keep moving, exploring every part. There's no inch of my upper body that isn't being touched, examined, claimed.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(Now his fingers are on my nipples, pinching them. The sensation is sharp, almost electric, and it shoots straight down to my core.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(It hurts a little but... it doesn't. The pain and pleasure are so intertwined that I can't separate them anymore. It all just feels like... something. Something I'm not supposed to want.)"
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_lie_next_to_dad_licking_neck_lifting_shirt_gropping_breast_biting_neck
    with fade
    
    show madd overwhelmed at left_small
    with dissolve
    x "(He gets more aggressive, biting at my neck now. His teeth are sharp against the delicate skin and I can feel him breaking the surface.)"
    
    show madd shocked at left_small
    with dissolve
    x "(I can feel his teeth sinking into my skin. He's not trying to be gentle anymore. The pretense of care is completely gone.)"
    
    show madd violated at left_small
    with dissolve
    x "(It's like he's marking me, claiming me for everyone to see. Like he's writing his name on my skin in teeth and saliva.)"
    
    show madd feels violated at left_small
    with dissolve
    x "(Heat builds up inside me. I'm scared and excited at the same time, and I don't know which feeling is worse. The two emotions are feeding each other, making me dizzy.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(The fear and the pleasure are mixing together, and I can't separate them anymore. It's like he's rewiring my brain, making me associate pain with pleasure, violence with affection.)"
    
    show madd horrified at left_small
    with dissolve
    x "(This is what he's doing to me. He's breaking me down piece by piece. Systematically. Like he's studying exactly which buttons to push and when to push them.)"
    
    show madd helpless at left_small
    with dissolve
    x "(His mouth, his tongue, his teeth—he wants to consume me. Literally. Like he wants to swallow me whole and make me part of him.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(Like a predator that's finally caught its prey. I remember this from nature documentaries—the way predators toy with what they catch before they kill it. Is that what this is?)"
    
    show dad possessive at right_small
    with dissolve
    dad_says "You have a beautiful body... I'm going to enjoy every part of it."
    
    show dad obsessed at right_small
    with dissolve
    dad_says "Soon I'll put a baby in you, and you'll be mine forever."
    
    show dad coercive at right_small
    with dissolve
    dad_says "Turn your face toward me."
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_lie_next_to_dad_kiss_initial
    with fade
    
    show madd nervous at left_small
    with dissolve
    show madd hesitant at left_small
    with dissolve
    x "(I hesitate for just a moment, then turn toward him. That split second of hesitation feels like defiance, like a tiny rebellion, even though I know it won't matter.)"
    
    show madd resigned at left_small
    with dissolve
    x "(It's easier to just do what he says. Resistance = pain. Compliance = maybe less pain. Simple math. I learned it a long time ago.)"
    
    show madd helpless at left_small
    with dissolve
    x "(Resistance only makes it worse. I've learned that the hard way. Every time I've tried to push back or pull away, he's escalated. Pushed harder. Gone further. So now I just... accept it.)"
    
    show madd paralyzed at left_small
    with dissolve
    show madd shocked at left_small
    with dissolve
    x "(His lips come down hard on mine.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(This isn't a kiss... it's an invasion. His mouth is forcing mine open, claiming the space inside. It's the most intimate violation because it feels almost tender, almost like affection.)"
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_lie_next_to_dad_kiss_initial_kissing_deeply
    with fade
    
    show madd distressed at left_small
    with dissolve
    x "(His tongue pushes into my mouth without hesitation. It's thick and warm and it tastes like cigarettes and alcohol. The foreign object in my mouth makes my gag reflex activate immediately.)"
    
    show madd trembling at left_small
    with dissolve
    x "(I try to close my lips but he's stronger. His hand moves to the back of my head and holds me in place, forcing my mouth to stay open for him.)"
    
    show madd violated at left_small
    with dissolve
    x "(He's in my mouth now, and it feels wrong in every way.)"
    
    show madd helpless at left_small
    with dissolve
    x "(His hands are still on my body. One's in my hair, the other's on my breast, squeezing, kneading, never staying still.)"
    
    show madd violated at left_small
    with dissolve
    x "(He never stops touching me. Not for a second. It's like he needs constant contact to know I'm really here, really his.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(There's no escape. Not even when he's kissing me.)"
    
    show madd resigned at left_small
    with dissolve
    x "(Every part of me is his to touch, his to use. I've given up trying to protect anything. There's nothing left that's just mine anymore.)"
    
    show dad perverted at right_small
    with dissolve
    dad_says "Your mouth is perfect... god, I love this..."
    
    show madd nauseated at left_small
    with dissolve
    x "(His tongue goes deeper, nearly reaching my throat.)"
    
    show madd trembling at left_small
    with dissolve
    x "(I can barely breathe. My nose is being cut off by his face. Each breath I take is difficult, forced. It's like he wants me to panic, wants me to feel like I'm suffocating.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I want to gag. I want to pull away. My body is rejecting this, sending me signals to get away from the danger. But he's holding my head in place.)"
    
    show madd resigned at left_small
    with dissolve
    x "(But I don't. I just let him do it. I've learned that fighting just makes it worse. Sometimes compliance is the only power you have—the power to decide how much you'll resist.)"
    
    show madd violated at left_small
    with dissolve
    x "(He's trying to own me completely, even my mouth isn't safe. No part of me is off-limits. My body, my mouth, my thoughts—he's claiming all of it. And the worst part is, I'm letting him.)"
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_lie_next_to_dad_kiss_initial_kissing_deeply_body_turned_around
    with fade
    
    show madd shocked at left_small
    with dissolve
    x "(He suddenly turns my whole body to face him directly. The movement is forceful and sudden, not asking for permission, just taking what he wants. My body is manhandled like a doll, repositioned for his comfort, his pleasure.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(His hand presses on top of my head, keeping me in place while he keeps kissing me. The pressure is firm but not painful. It's almost gentle. That somehow makes it worse.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(It's strange... the way he kisses me while his hands roam across my bare skin. There's a tenderness to it that makes it even more horrible. Like he actually cares. Like this is love.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(Almost intimate, if it weren't so wrong. If he weren't forcing it. If I had any choice in the matter. But there's nothing intimate about coercion, no matter how much he tries to dress it up.)"
        
    show madd horrified at left_small
    with dissolve
    x "(This is nothing like that. This is the opposite. This is the perversion of everything that's supposed to be safe and loving about family.)"
    
    show madd disgusted at left_small
    with dissolve
    x "(This is something sick. Truly sick. There's no love here, no care, just want and power and the need to own. And he's doing it under the guise of affection, which somehow makes it even more disgusting.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I know what's coming. I've memorized the progression by now. I could predict every move if I wanted to. That should be comforting somehow, but it's not.)"
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_lie_next_to_dad_kiss_initial_kissing_deeply_body_turned_around_dad_leg_on_top
    with fade
    
    show madd trembling at left_small
    with dissolve
    x "(He pins my legs down with his. The weight of his body on mine is suffocating. I can feel his thigh pressing between my legs, spreading them apart whether I want them to or not.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(I'm completely trapped under him now. There's no escape route, nowhere to run, nowhere to hide. I'm pinned to the mattress by his body weight and his will.)"
    
    show madd helpless at left_small
    with dissolve
    x "(I can't move. I can't escape. My arms are pinned, my legs are pinned, my mouth is occupied. I'm immobilized.)"
        
    show madd violated at left_small
    with dissolve
    x "(This is what he wants—to show me he has complete control. To make it physical and real and impossible to deny. Words don't cut it anymore. He needs me to feel his dominance in my body.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(I'm not even a person to him. Just something to use. A body. An object. A toy to play with and then discard when he's done.)"
    
    show madd resigned at left_small
    with dissolve
    x "(His hands move down to my hips. They're big enough to span almost my entire waist and he uses that to his advantage, holding me steady for what's about to come.)"
    
    show madd trembling at left_small
    with dissolve
    x "(He squeezes them, then moves lower. His fingers are trailing down my abdomen now, getting closer to where this is heading. The anticipation is making my breath come faster.)"
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_dad_lowering_madd_shorts
    with fade
    
    show madd anxious at left_small
    with dissolve
    x "(He reaches for the waistband of my shorts. His fingers hook under the elastic and I feel the fabric starting to loosen.)"
    
    show madd distressed at left_small
    with dissolve
    x "(My heart is pounding so hard I think it might break through my ribs. This is the moment. The moment where the last barrier comes down.)"
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_dad_lowering_madd_shorts_madd_naked
    with fade
    
    show madd trembling at left_small
    with dissolve
    x "(He pulls them down slowly, exposing my lower body. Each inch of skin that becomes visible feels like a loss, like he's peeling away another layer of my protection.)"
    
    show madd shocked at left_small
    with dissolve
    x "(The air is cold against my skin. The temperature change makes my entire body react, makes goosebumps rise across my exposed flesh.)"
        
    show dad lustful at right_small
    with dissolve
    dad_says "So soft... so smooth... I want to be inside you."
    
    show madd horrified at left_small
    with dissolve
    x "\"Please... no... not that... anything else but not that...\" (My voice cracks on the last word. I'm actually begging. I've never felt so powerless, so desperate, so small.)"
    
    show madd trembling at left_small
    with dissolve
    x "(My voice shakes. I can't hide my desperation. It's pathetic, really. I'm begging him like it'll make a difference, like he hasn't already decided what's going to happen to me.)"
    
    show madd determined at left_small
    with dissolve
    x "(This is the one line I'm still holding onto. The one thing I haven't completely surrendered. Full penetration—that feels like it would be the final breaking point. The moment where I'm completely his. So I cling to this boundary with everything I have left.)"
    
    show dad calculating at right_small
    with dissolve
    dad_says "Alright... for now."
    
    show dad manipulative at right_small
    with dissolve
    dad_says "But one day you're going to beg me for it."
    
    show madd shocked at left_small
    with dissolve
    x "(He actually listens. I can't believe it. There's this tiny moment where I think maybe, just maybe, he actually cares.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I don't know if that makes things better or worse. Because now I'm confused. If he can listen, if he can show restraint in this one moment, then what does that say about all the other times? Isn't everything else a choice? Doesn't that make it all even more deliberate and cruel?)"
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_dad_lowering_his_shorts
    with fade
    
    show madd distressed at left_small
    with dissolve
    x "(He pulls his shorts down.)"
    
    show madd horrified at left_small
    with dissolve
    x "(His dick is hard and massive.)"
    
    show madd shocked at left_small
    with dissolve
    x "(I've seen it before but it still shocks me. The sheer size of it. The sheer wrongness of it. How is something like that supposed to fit inside a body?)"
    
    show madd nauseated at left_small
    with dissolve
    x "(The head is swollen, purple-ish, with thick veins running down the sides. I can see his pulse in them, see how much blood is in it. He's completely aroused. Completely ready.)"
    
    show madd disgusted at left_small
    with dissolve
    x "(There's already fluid at the tip. Clear pre-cum that glistens in what little light there is. The thought of what that means—that he's been aroused this whole time, that he's been waiting for this—makes me feel dirty just looking at it.)"
    
    show dad lustful at right_small
    with dissolve
    dad_says "One day this will be deep inside you... all the way to your womb."
    
    show dad obsessed at right_small
    with dissolve
    dad_says "And when I cum, I'll fill you with my seed."
    
    show madd nauseated at left_small
    with dissolve
    x "(His words should disgust me.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(But something inside me responds to them anyway.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(I hate that I nod.)"
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_dad_dick_between_madd_thighs_and_pussy_lips
    with fade
    
    show madd paralyzed at left_small
    with dissolve
    x "(He positions himself between my thighs. I can feel him adjusting his body, shifting his weight, getting the angle just right.)"
    
    show madd helpless at left_small
    with dissolve
    x "(His hands are on my hips, holding me steady while he lines himself up. The grip is firm, controlling, like I'm something to be positioned rather than someone with a choice.)"
    
    show madd anxious at left_small
    with dissolve
    x "(His dick is pressed against me, hot and hard. The temperature is shocking—it's so much hotter than I expected, like fever-hot, and the heat radiates into my skin.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I can feel the pulse in it. Each throb sends a wave of warmth against my most sensitive areas, and I hate that I can feel it so clearly.)"
    
    show madd distressed at left_small
    with dissolve
    x "(But not inside. Not yet. That small distinction feels like the only thing keeping me from completely falling apart.)"
    
    show madd anxious at left_small
    with dissolve
    x "(Just pressed against the outside. The tip is right there, right at my entrance, and I can feel how easy it would be for him to push forward. One movement. That's all it would take.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(The feeling is overwhelming. Every nerve ending in my lower body is firing at once, creating a sensation so intense I can barely process it.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(It's too much. My brain can't handle this level of stimulation. I'm drowning in sensation and I don't know if I want to escape or sink deeper.)"
    
    show madd distressed at left_small
    with dissolve
    x "(His length slides against my sensitive skin. I can feel every ridge, every vein, the texture of his foreskin as it moves.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(The friction is creating heat between us. The combination of his body heat and the friction is making me feel like I'm burning from the inside out.)"
    
    show madd trembling at left_small
    with dissolve
    x "(My thighs are getting hot where he's pressed between them. The skin-to-skin contact is creating this intense warmth that's spreading outward.)"
    
    show madd flustered at left_small
    with dissolve
    x "(He starts to move, grinding against me. The movement is slow at first, deliberate, like he's savoring the sensation.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(Each slide of his length against me sends sparks through my nervous system. My body jerks involuntarily with each pass, and I can't control it.)"
    
    show madd blush at left_small
    with dissolve
    x "(The friction is intense. Each movement sends a jolt of sensation straight through me. The rough texture of his skin sliding against the sensitive skin of my pussy is almost unbearable in how good it feels, and I hate myself for every second of it.)"
    
    show madd blush at left_small
    with dissolve
    x "(My nipples harden. They're standing up now, darkened, obvious. A physical tell that I'm responding to this, enjoying it. And he sees it.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(I can see his eyes flick down to them. The way he looks at them makes me feel so exposed, like he's cataloging every physical response for future reference.)"
    
    show madd flustered at left_small
    with dissolve
    x "(They're so sensitive now. Even the air feels like too much. And when his hands brush against them, I have to bite back a sound.)"
    
    show madd deep blush at left_small
    with dissolve
    x "(My face is heating up. I can feel the blood rushing to my cheeks, making me blush in a way that's completely visible. There's no hiding what's happening to me.)"
    
    show madd flustered at left_small
    with dissolve
    x "(The warmth is pooling between my legs. I can feel it concentrating there, building, making me more and more aware of every point where his body touches mine.)"
    
    show madd flustered at left_small
    with dissolve
    x "(I'm getting wet. I can feel it. The moisture between my legs is unmistakable evidence that my body is responding to him, that some part of me actually wants this even though every conscious part of my mind is screaming that I don't.)"
    
    show madd blush at left_small
    with dissolve
    x "(The wetness is making everything slicker. His movements are getting smoother, easier, and I know he can feel the difference. The increased lubrication is proof of my arousal.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(I can feel it spreading. Not just at my entrance but along my inner thighs where he's sliding. The evidence of my body's betrayal is coating both of us now.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(God, I hate that I like this. The disgust I feel for myself is so visceral, so overwhelming, that it's making me nauseous. I'm no better than an animal. I'm responding to stimulation like a dog responds to food.)"
    
    show madd disgusted at left_small
    with dissolve
    x "(There's no conscious thought involved. My body just reacts. Wetness, hardened nipples, flushed skin—all automatic responses that have nothing to do with what I actually want.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(What does that make me? If I enjoy being raped, if my body wants it even though my mind rejects it, what does that make me? A victim? A willing participant? A monster? I don't know anymore.)"
    
    show madd horrified at left_small
    with dissolve
    x "(The lines are so blurred now. Consent, force, pleasure, pain—they're all tangled together in a knot I can't untie.)"
    
    show madd broken at left_small
    with dissolve
    x "(Maybe there is no answer. Maybe I'm just broken in a way that can't be fixed, and I need to accept that this is who I am now.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(He kisses me again, deep and rough. No tenderness this time, just possession. His mouth claims mine like he's proving ownership.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I can taste him—cigarettes, whiskey, something else I can't identify. The taste is coating my tongue, becoming part of me.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(His tongue is in my throat again. I can feel it going deeper, like he's trying to reach my very center. Like he wants to brand me from the inside out.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I'm gagging. My throat is constricting around the intrusion, trying to expel it, but his hand on the back of my head keeps me in place.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(I can barely breathe. Each breath has to be stolen in the brief moments when he pulls back slightly, and even then it's not enough air.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(His hands on my breasts, his dick rubbing against my pussy. His tongue in my mouth, his body pressing down on me. There are too many sensations, too many points of contact, and I can't think straight.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(My senses are overloading. I can smell him, taste him, feel him everywhere. There's no part of me that isn't being stimulated right now.)"
    
    show madd helpless at left_small
    with dissolve
    x "(My brain is struggling to process it all. Each sensation is competing for attention and I'm getting lost in the chaos of it.)"
    
    show madd distressed at left_small
    with dissolve
    x "(Everything at once. My body is on overload, my senses firing in every direction, and I'm drowning in it all.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(I can't focus on any single thing because there are too many things happening. It's breaking down my ability to think, to process, to resist.)"
    
    show madd anxious at left_small
    with dissolve
    x "(He speeds up, moving faster and faster. The rhythm is increasing, becoming more urgent, more desperate.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I can hear the wet sounds now. The slick friction of his dick against my pussy is making obscene noises that fill the quiet room.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(Each thrust is harder than the last. He's putting more force behind it, grinding against me with increasing pressure.)"
    
    show madd blush at left_small
    with dissolve
    x "(The friction builds, and I can feel myself getting wet. Wetter than before. So wet that I can feel it dripping down, coating my inner thighs.)"
    
    show madd flustered at left_small
    with dissolve
    x "(The moisture is making everything slippery. His movements are getting smoother, sliding easier, and the sensation is intensifying with each pass.)"
    
    show madd deep blush at left_small
    with dissolve
    x "(I can feel my own slickness mixing with his pre-cum. The combination is creating this warm, sticky mess between my legs that's impossible to ignore.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(I'm completely betrayed by my own body. It's responding to his touch like it belongs to him, like it wants him, like I'm some kind of nymphomaniac who enjoys being assaulted.)"
    
    show madd horrified at left_small
    with dissolve
    x "(Every physical sign is pointing to arousal. Wetness, flushed skin, hardened nipples, rapid breathing. My body is screaming that it wants this even while my mind is screaming that it doesn't.)"
    
    show madd violated at left_small
    with dissolve
    x "(There's no hiding it anymore. He can feel every response, see every reaction. I'm completely transparent to him now.)"
    
    show madd flustered at left_small
    with dissolve
    x "(My pulse is racing. My breathing is coming faster, matching his rhythm, and I realize we're synchronized now. Our bodies are in sync even if our minds are in conflict.)"
    
    show madd anxious at left_small
    with dissolve
    x "(My heart is pounding so hard I can feel it in my throat, in my ears, in my fingertips. The adrenaline is making everything sharper, more intense.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(Each breath is shallow and quick. I'm almost panting now, and I hate the sound of it because it makes me sound like I'm enjoying this.)"
    
    show madd deep blush at left_small
    with dissolve
    x "(I'm responding to him like... like I want this. Every physical indicator says yes even though every thought says no.)"
    
    show madd horrified at left_small
    with dissolve
    x "(My hips are moving slightly. I didn't consciously decide to do that. They're just... responding. Meeting his rhythm. Participating.)"
    
    show madd horrified at left_small
    with dissolve
    x "(But I don't. I don't want this. I didn't want this to happen. I don't want to be here. I don't want to want this.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I keep repeating it to myself like a mantra. I don't want this. I don't want this. But the words are losing meaning with each repetition.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(My body is calling me a liar. Every wet, flushed, trembling part of me is contradicting what I'm telling myself.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(Do I? That's the question that's destroying me from the inside. Does wanting something that's being forced on you count as consent? Or am I just adapting to trauma by convincing myself I enjoy it?)"
    
    show madd anxious at left_small
    with dissolve
    x "(I've read about Stockholm syndrome. About trauma bonding. About how victims sometimes develop feelings for their abusers as a survival mechanism.)"
    
    show madd horrified at left_small
    with dissolve
    x "(Is that what's happening to me? Or is this something else? Something darker? Something that means I was broken long before he ever touched me?)"
    
    show madd shocked at left_small
    with dissolve
    x "(He knows. He can definitely tell. There's no hiding my arousal, no pretending I'm not enjoying this. My body has betrayed every wall I've built.)"
    
    show madd horrified at left_small
    with dissolve
    x "(I can see it in his eyes. The satisfaction. The triumph. He knows he's winning, breaking me down, and that knowledge is fuel to his fire.)"
    
    show madd broken at left_small
    with dissolve
    x "(This is what he wanted all along. Not just to use my body, but to make me complicit in my own violation. To make me want it.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(He devours my mouth, almost violent in the way he's kissing me. Like he's trying to consume me, possess me, make me his in this moment.)"
    
    show madd violated at left_small
    with dissolve
    x "(His teeth clash against mine. There's no technique here, no skill. Just raw hunger and the need to claim.)"
    
    show madd anxious at left_small
    with dissolve
    x "(I can feel his desperation. It's in the way he's gripping me, the way his breathing has become ragged, the way every movement is losing its rhythm.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(His breathing gets heavier. I can feel him against my neck, his breath hot and urgent, his control slipping.)"
    
    show madd anxious at left_small
    with dissolve
    x "(He's panting now. Each exhale is warm and damp against my skin, coming faster and faster until they're almost continuous.)"
    
    show madd distressed at left_small
    with dissolve
    x "(The sound of his breathing is filling my ears. It's loud, desperate, animal-like. He sounds like he's running a race.)"
    
    show madd distressed at left_small
    with dissolve
    x "(Faster. He's losing himself in this, and that makes it even more intense because I know what's coming next.)"
    
    show madd anxious at left_small
    with dissolve
    x "(His movements are becoming erratic. The steady rhythm is breaking down into frantic grinding, like he can't control himself anymore.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(I can feel his dick throbbing between my thighs. The pulsing is getting stronger, more frequent, a clear sign of what's about to happen.)"
    
    show madd trembling at left_small
    with dissolve
    x "(I know he's close. I've felt this buildup enough times to recognize it. The way his whole body tenses, the way his breathing changes, the way his movements become desperate.)"
    
    show madd anxious at left_small
    with dissolve
    x "(Any second now. I'm bracing myself for it, preparing for the feeling of his cum on my skin.)"
    
    show madd resigned at left_small
    with dissolve
    x "(Part of me just wants it to be over. The other part is horrified that it's about to happen again.)"
    
    show dad obsessed at right_small
    with dissolve
    dad_says "Gahhhh... yes... that's it..."
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_dad_dick_between_madd_thighs_and_pussy_lips_dad_cumming
    with fade
    
    show madd shocked at left_small
    with dissolve
    x "(His body tenses. Every muscle goes rigid for just a moment and I know exactly what that means.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(He's stopped moving. Frozen in place. It's the calm before the storm, that split second of stillness before release.)"
    
    show madd anxious at left_small
    with dissolve
    x "(I can feel his dick swelling between my thighs. It's getting even harder, if that's possible, preparing to expel.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(I feel it happening. The building pressure, the tightening, the moment right before release. I've felt this progression a hundred times now and I could predict it perfectly.)"
    
    show madd anxious at left_small
    with dissolve
    x "(There's a final throb. Stronger than all the others. And then I know it's happening.)"
    
    show madd shocked at left_small
    with dissolve
    x "(Time seems to slow down. That instant before his climax stretches out, and I'm hyper-aware of every sensation.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(He cums, hard, spraying across my skin. The force of it is almost violent, almost like he's attacking me with his release.)"
    
    show madd shocked at left_small
    with dissolve
    x "(I can feel each spurt. They're coming in waves, each one hitting my skin with surprising force. It's not gentle. It's aggressive.)"
    
    show madd violated at left_small
    with dissolve
    x "(The first spray hits my lower stomach. Hot and thick. Then another, and another, coating my skin in rapid succession.)"
    
    show madd shocked at left_small
    with dissolve
    x "(The warmth is shocking. The temperature contrast between the hot fluid and my cooler skin makes my body recoil instinctively, but there's nowhere for me to go.)"
    
    show madd distressed at left_small
    with dissolve
    x "(It's so hot it almost burns. Not quite painful but close. My skin is tingling where it lands, like it's too much heat all at once.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I can feel it spreading. The liquid is running across my skin, following the contours of my body, finding every curve and hollow.)"
    
    show madd disgusted at left_small
    with dissolve
    x "(I feel it landing on me. Hot and sticky and gross, coating my skin in evidence of what just happened.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(The texture is thick. Viscous. It's not like water or sweat. It's heavier, stickier, and it clings to my skin in a way that makes me want to claw it off.)"
    
    show madd violated at left_small
    with dissolve
    x "(I can smell it. That distinct smell of semen that I've become too familiar with. Slightly salty, slightly bitter, unmistakable.)"
    
    show madd violated at left_small
    with dissolve
    x "(His length is trapped between my thighs, so all of it ends up on me. Every drop lands on my pussy, my thighs, my stomach. I'm painted in him.)"
    
    show madd disgusted at left_small
    with dissolve
    x "(I can feel it pooling. Gathering in the creases where my thighs meet my body. Dripping down. Some of it is already starting to run down toward the bed.)"
    
    show madd horrified at left_small
    with dissolve
    x "(It's on my pussy lips. I can feel it coating them, warm and thick. The most intimate violation because that's where he wants to be, inside me.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(My inner thighs are soaked. The cum is running down them in streams, and I can feel every path it takes as gravity pulls it downward.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(There's so much of it. More than seems possible. How can one person produce this much? It feels like it's never going to stop.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(I've lost count of how many spurts. Five? Seven? Ten? They're blurring together into one continuous release.)"
    
    show madd disgusted at left_small
    with dissolve
    x "(It's disgusting. The feeling of being marked like this, claimed like this, used like this. I'm covered in his DNA, his essence, his ownership.)"
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_dad_cum_between_madd_thighs_and_pussy
    with fade
    
    show madd distressed at left_small
    with dissolve
    x "(It goes on for about ten seconds. Each spurt feels like it's marking me, claiming me, proving that I belong to him now.)"
    
    show madd violated at left_small
    with dissolve
    x "(Ten seconds that feel like an eternity. Each one stretches out, and I'm aware of every single moment, every single drop.)"
    
    show madd relieved at left_small
    with dissolve
    x "(Finally, the spurts are getting weaker. Smaller amounts. The flood is becoming a trickle. It's almost over.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(My thighs and pussy are covered in it. The amount is shocking. There's so much that I can't imagine how that was all inside him just moments ago.)"
    
    show madd disgusted at left_small
    with dissolve
    x "(It's everywhere. On my stomach, my thighs, my pussy, probably even on the bed beneath me. There's no part of my lower body that isn't contaminated.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I can feel the weight of it. The liquid has substance, mass. It's heavy on my skin in a way that makes it impossible to ignore.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(The sticky mess is all over my skin. I can feel it starting to dry already, becoming tacky, adhering to me like glue.)"
    
    show madd disgusted at left_small
    with dissolve
    x "(It's cooling. The temperature is dropping as it's exposed to the air. Going from hot to warm to body temperature.)"
    
    show madd disgusted at left_small
    with dissolve
    x "(I can feel it starting to cool on me. Drying. The texture is changing from liquid to something thicker, stickier, harder to remove.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(Soon it will be crusty. I've experienced this before. The way it dries into a flaky residue that clings to skin and hair.)"
    
    show madd horrified at left_small
    with dissolve
    x "(I'll have to wear this. On me. For hours. He won't let me clean it off. He never does. He wants me to feel it, to remember.)"
    
    show madd distressed at left_small
    with dissolve
    x "(All night I'll feel this drying on my skin. Every time I move, I'll be reminded. Every time I shift position, the dried cum will crack and flake.)"
    
    show madd violated at left_small
    with dissolve
    x "(By morning it will be completely dry. Crusty and uncomfortable and a physical reminder of what he did to me.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(The thought makes me want to scream. To claw at my skin until it's raw. To scrub myself bloody just to get it off. But I can't. I have to just... accept it.)"
    
    show dad creepy at right_small
    with dissolve
    dad_says "Good girl. Keep this up and I might unlock your room soon."
    
    show madd self loathing at left_small
    with dissolve
    x "(The promise of freedom makes me feel pathetic. The idea that I'd trade my body, my dignity, my very self for the chance to have my locked room opened... it makes me hate myself.)"
    
    show madd broken at left_small
    with dissolve
    x "(But this is where I am. This is what I've become. Someone who measures worth in unlocked doors and moments of relative safety.)"
    
    show madd distressed at left_small
    with dissolve
    x "(The bar has been lowered so far that basic privacy feels like a reward worth suffering for. That's how broken I am.)"
    
    show madd resigned at left_small
    with dissolve
    x "(But I cling to it anyway. It's all I have. Even though I know deep down that he's never going to keep that promise, I hold onto the hope because without it, I have nothing.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(Hope is dangerous. It keeps me compliant. It makes me think that if I just endure a little more, things might improve. But they never do.)"
    
    show madd broken at left_small
    with dissolve
    x "(Still, I can't let it go. The human mind needs something to hold onto. Even if it's a lie. Even if it's the very chain that's keeping me trapped.)"
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_dad_push_madd_back_to_old_position_cum_on_madd
    with fade
    
    show madd trembling at left_small
    with dissolve
    x "(He turns me away from him. The movement is casual, careless. Like I'm an object he's done using and now needs to put away.)"
    
    show madd violated at left_small
    with dissolve
    x "(I feel my body being repositioned. Back to how I was before. Facing away from him so he doesn't have to look at what he's done.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I guess he's done with me now. Used up for the night. Satisfied. The thought makes me feel empty and hollow.)"
    
    show madd broken at left_small
    with dissolve
    x "(This is always how it ends. He takes what he wants and then discards me. There's no aftercare, no comfort, just dismissal.)"
    
    show madd relieved at left_small
    with dissolve
    x "(At least he didn't go all the way. At least his dick isn't inside me. At least there's that small mercy.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I should be grateful for that, I guess. But how sick is that? How completely broken do I have to be to be grateful that I wasn't fully penetrated? Isn't the whole thing terrible regardless?)"
    
    show madd horrified at left_small
    with dissolve
    x "(But grateful? To my rapist?)"
    
    show madd self loathing at left_small
    with dissolve
    x "(What am I becoming?)"
    
    show dad possessive at right_small
    with dissolve
    dad_says "Put your shorts back on. I want you to wear my cum tonight."
    
    show dad sadistic at right_small
    with dissolve
    dad_says "It's good preparation for when I actually fill your womb."
    
    show madd horrified at left_small
    with dissolve
    x "(The thought of actually getting pregnant by him... it paralyzes me with terror. Even though he didn't go all the way, the risk is still there. Pre-cum can carry sperm.)"
    
    show madd anxious at left_small
    with dissolve
    x "(I know the biology. I paid attention in health class. Even without full penetration, pregnancy is possible if his fluids get inside me.)"
    
    show madd distressed at left_small
    with dissolve
    x "(And with all this cum on my pussy lips, some of it has definitely made contact. Some of it could be making its way inside right now.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(My period is due in... when? I try to count the days but my mind is too scattered. Two weeks? Three? I don't even know anymore.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(I don't want to think about it. But I can't stop. The image of me, pregnant with his baby, is burned into my mind. That's his ultimate goal, I know. To make me carry his child so I'm permanently bound to him.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(A baby. His baby. Growing inside me. The thought makes me want to vomit. It would be the final violation, the ultimate proof of ownership.)"
    
    show madd horrified at left_small
    with dissolve
    x "(I'd be showing. Everyone would see. Everyone would know. There would be no hiding what he's done to me then.)"
    
    show madd distressed at left_small
    with dissolve
    x "(Carrying his baby. Being tied to him forever. The pregnancy would just be the beginning. Then there would be a child. A living reminder.)"
    
    show madd broken at left_small
    with dissolve
    x "(I'd have to look at that child every day and see his face. See the evidence of what he did. There would be no escape, ever.)"
    
    show madd anxious at left_small
    with dissolve
    x "(That's his plan. I know it is. He's said it enough times. He wants to put a baby in me, to make me his in a way that can never be undone.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(Every time he cums on me, near me, inside the general vicinity of my reproductive organs, I feel this panic. Is this the time? Is this when it happens?)"
    
    show madd violated at left_small
    with dissolve
    x "(To completely own me. Not just my body, not just my time, but my future. My biology. My entire life trajectory altered by his decision.)"
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_madd_shorts_full_of_cum
    with fade
    
    show madd distressed at left_small
    with dissolve
    x "(I pull my shorts back up. The movement is mechanical, devoid of any feeling. I'm just going through motions now.)"
    
    show madd trembling at left_small
    with dissolve
    x "(My hands are shaking as I grab the waistband. I can barely grip the fabric. My fine motor control is shot from the adrenaline.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I have to touch the cum to do this. My fingers come into contact with it as I pull the fabric up, and the texture makes my stomach turn.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(The fabric is sticking to my wet skin. Both my wetness and his cum are mixing together, creating a disgusting paste that coats the inside of the fabric.)"
    
    show madd disgusted at left_small
    with dissolve
    x "(I can hear the wet sound as the fabric makes contact with my skin. A soft squelching noise that makes me want to gag.)"
    
    show madd violated at left_small
    with dissolve
    x "(The shorts are absorbing some of the moisture. I can feel them getting damp, heavy with the combination of fluids.)"
    
    show madd disgusted at left_small
    with dissolve
    x "(It's disgusting. There's no other word for it. The sensation of pulling clothing over cum-covered skin is one of the worst things I've ever felt.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I can feel individual wet spots where there's more cum. The fabric clings to those areas more, creating texture I can feel through the material.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(The wetness is spreading as I pull them up. His cum and my arousal are mixing together, creating something obscene, something that feels like corruption.)"
    
    show madd disgusted at left_small
    with dissolve
    x "(It's being pushed around. Redistributed. Areas that were relatively clean are now contaminated as the fabric spreads it all around.)"
    
    show madd violated at left_small
    with dissolve
    x "(I can feel it moving. Sliding across my skin as the tight fabric forces it into new patterns, new locations.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(It's everywhere now—on my thighs, my pussy, even some on my stomach. I can feel it seeping into every crevice, and there's nothing I can do about it.)"
    
    show madd violated at left_small
    with dissolve
    x "(The shorts are trapping it against my skin. Creating a warm, wet environment where it can soak in, where I can't escape the sensation.)"
    
    show madd horrified at left_small
    with dissolve
    x "(Some of it is being pushed inside me. I can feel it. The pressure of the fabric is forcing fluids into my vagina, and that terrifies me more than anything.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I don't like it at all. Every second of this is torture. The physical sensation, the emotional weight, the knowledge of what this means.)"
    
    show madd resigned at left_small
    with dissolve
    x "(But I do it anyway. Because he told me to. Because I've learned that obedience is the path of least resistance.)"
    
    show madd helpless at left_small
    with dissolve
    x "(But there's nothing I can do about it. No shower. No cleanup. No washing it away. He's made that clear. I have to wear this.)"
    
    show madd resigned at left_small
    with dissolve
    x "(If I tried to clean up, he'd know. He always knows. And the punishment for disobedience is always worse than the original offense.)"
    
    show madd violated at left_small
    with dissolve
    x "(I'm stuck like this. Wearing his cum. His mark. Branded. There's nowhere to hide it. When I walk, I'll feel it. When I sit, I'll feel it. When I sleep, it'll be drying on me.)"
    
    show madd distressed at left_small
    with dissolve
    x "(The waistband is cutting into my skin slightly. The elastic is tight and it's pressing the wet fabric against me, ensuring constant contact.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I can feel it between my pussy lips. The fabric of the shorts is thin enough that it's not really a barrier. It's just spreading his cum more intimately.)"
    
    show madd helpless at left_small
    with dissolve
    x "(Every movement is going to remind me. If I shift my legs, I'll feel the wet fabric move. If I walk, I'll feel it rubbing.)"
    
    show madd resigned at left_small
    with dissolve
    x "(A living reminder that I'm his. That my body belongs to him. That I'm not my own anymore.)"
    
    show madd broken at left_small
    with dissolve
    x "(This is what ownership looks like. Not just the act itself, but the aftermath. The requirement to wear his mark, to carry proof of what he's done.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(I am his property. That's what this is about. Property doesn't get to clean itself. Property stays exactly as the owner wants it.)"
    
    show dad possessive at right_small
    with dissolve
    dad_says "Perfect. You're such a good girl. So obedient."
    
    show madd distressed at left_small
    with dissolve
    x "(His praise feels empty and hollow. The words good girl make my skin crawl because I know exactly what they mean. They mean I'm compliant. They mean I'm broken. They mean I've accepted my place.)"
    
    show madd broken at left_small
    with dissolve
    x "(I'm not a good girl. I'm just... trapped. And maybe I'm starting to like it, which is the most horrifying thought of all.)"
    
    show madd helpless at left_small
    with dissolve
    x "(I let him do whatever he wants to me. I have no defense. No walls. No secrets left. He's taken everything.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(And the saddest part? I'm starting to accept it. The fight is leaving me day by day, replaced by this numb resignation.)"
    
    show madd broken at left_small
    with dissolve
    x "(Maybe that's what happens when you're trapped long enough. Your mind starts to break, looking for ways to make the pain bearable.)"
    
    show madd resigned at left_small
    with dissolve
    x "(You stop fighting. You stop hoping. You just... become.)"
    
    show madd resigned at left_small
    with dissolve
    x "(As I drift off to sleep, I can feel how hot the shorts are against my skin. The fabric is damp and uncomfortable and disgusting, and I can't wash it away.)"
    
    show madd distressed at left_small
    with dissolve
    x "(A reminder of what he did to me. His cum is cooling on my skin, drying, becoming part of me in a way that feels permanent.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(A reminder of what he's going to keep doing. This isn't a one-time thing. This is my life now. This is what I am.)"
    
    show madd anxious at left_small
    with dissolve
    x "(Tomorrow it'll all happen again. And the day after that. And the day after that, stretching into an infinite future of violation.)"
    
    show madd helpless at left_small
    with dissolve
    x "(And the day after that. Each repetition makes it feel more normal, more acceptable, more like this is just how things are.)"
    
    show madd broken at left_small
    with dissolve
    x "(Until I figure out how to escape. If I can. If I even want to anymore.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(Or until I don't want to anymore. Until the person I used to be is completely gone, replaced by whatever this is.)"

    x "(I woke up as i am being shoved outside the room.)"
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["kissed"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["intimacy"]+=7
    $ character_relations["dad"]["anger"]=0
    $ character_relations["dad"]["lust"]=0
    $madd_willpower=max(madd_willpower-20,0)
    $ journal_event_show("Dad", "Dad's Room Night 3")
    $ journal_event_set_done("Dad", "Sleep in Dad's Room")
    $ journal_event_show("Dad", "Found the Keys")
    $ journal_event_show("Dad", "Sleep With Dad: Vaginal Night")
    call dad_after_sleep_message from _call_dad_after_sleep_message
    jump sleep_on_bed_dad_room

label sleep_next_to_dad_night_after_locked_room_3:
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_lie_next_to_dad
    with fade
    show madd anxious at left_small
    with dissolve
    x "(I lie down next to him carefully, trying not to make any sudden movements that might wake him. My hands are shaking slightly as I lower myself onto the mattress, my breath shallow.)"
    x "(I know how the last few times it's ended with him using me while I sleep. I have to be prepared for that possibility, to be ready.)"

    scene scene_sleep_next_to_dad_night_after_locked_room_3_dad_hand_on_madd_body
    with fade
    x "(Immediately after lying down, I feel his hand all over me, like he was waiting for me.)"
    x "(He immediately locks me down with his hand on my elbow locking me in place and I can't move, can't even breathe right.)"
    show madd paralyzed at left_small
    with dissolve
    dad_says "Sleeping here again? "
    x "(I heard his coarse voice and then felt his wet tongue exploring my neck, tasting me.)"
    show madd trembling at left_small
    with dissolve
    x "(He was licking and biting my neck like a wild animal. My body was frozen in place unable to move or resist, pinned under his weight.)"
    scene scene_sleep_next_to_dad_night_after_locked_room_3_dad_legs_lifting_madd_legs_more_licking
    with fade
    x "(With his legs' strength he lifted mine up and bit my neck roughly, marking me.)"
    show madd distressed at left_small
    with dissolve
    dad_says "You did this on purpose, didn't you?"
    x "(I couldn't say a word as he went back to roughly licking my neck, his tongue hot and invasive.)"
    scene scene_sleep_next_to_dad_night_after_locked_room_3_dad_legs_lifting_madd_legs_more_licking_2
    with fade
    x "(My legs were lifted, my elbows were pushed down, I had nowhere to go anymore, completely trapped.)"
    show madd helpless at left_small
    with dissolve
    dad_says "You like playing daddy's wife, huh?"
    x "(I was sure he thought I was sleeping here on purpose, that I had given in completely.)"
    show madd conflicted at left_small
    with dissolve
    x "(His tongue was rough and wet on my neck making me shiver. But him calling me his wife made me feel things I could not accept, things that scared me.)"

    scene scene_sleep_next_to_dad_night_after_locked_room_3_continued_neck_lick_assault
    with fade
    show madd paralyzed at left_small
    with dissolve
    x "(His tongue was exploring my neck more aggressively now. I could feel his teeth grazing my skin as he bit down hard on my neck, almost drawing blood.)"

    show madd broken at left_small
    with dissolve
    x "(He had lost any semblance of control over himself a long time ago, if he ever had it...)"
    x "(He was hungry and I was his food, his meal, his everything...)"
    show madd violated at left_small
    with dissolve
    x "(He continued licking my neck with saliva dripping from his mouth. My neck was fully covered in his saliva, marked with his ownership.)"
    x "(Saliva would drop from his mouth and onto my neck and he would lick it up eagerly, savoring me...)"
    show madd nauseated at left_small
    with dissolve
    x "(Only words that came from my mouth were soft moans as he continued to dominate me, to own me...)"

    scene scene_sleep_next_to_dad_night_after_locked_room_3_kiss_dad_first 
    with fade
    show madd shocked at left_small
    with dissolve
    x "(He then stopped lifting my leg, he used his hand to turn my face to his and kissed me deeply, claiming my mouth like it belonged to him. His legs climbed on top of my butt, pinning me further.)"
    show madd paralyzed at left_small
    with dissolve
    x "(His tongue explored my mouth deeply as he kissed me passionately. His saliva mixed with mine, it was everywhere, coating my tongue. His weight pressed me down firmly into the mattress.)"
    show madd distressed at left_small
    with dissolve
    x "(His hands were reaching down my crotch, he just kept his hand there he didn't do anything more. I knew it was some psychological control he wanted to have over me, to remind me he owned every part of me...)"
    show madd helpless at left_small
    with dissolve
    x "(He is always calculating how to control me more and more, finding new ways to break me...)"
    scene scene_sleep_next_to_dad_night_after_locked_room_3_kiss_dad_second
    with fade
    show madd nauseated at left_small
    with dissolve
    dad_says "You taste so good, Maddie..."
    x "(He continues licking my whole face, I can smell his saliva everywhere, his musk, his sweat. It was like the whole world disappeared and it was just him and me, only him and me.)"
    show madd flustered at left_small
    with dissolve
    x "(The only smell left was his saliva and sweat, the scent of him overpowering everything else. It was disgusting but some part of me liked it, craved it...)"
    show madd self loathing at left_small
    with dissolve
    x "(I've learned this about myself. I like being dominated by him. I like being his submissive little plaything, his toy...)"
    x "(No matter how evil and disgusting he is, my body just wants to please him, to satisfy him...)"
    scene scene_sleep_next_to_dad_night_after_locked_room_3_kiss_dad_second_back_to_licking
    with fade
    show madd distressed at left_small
    with dissolve
    x "(He went back to licking my face and neck again. I could feel his tongue moving all over my face, worshipping me like I was his deity...)"
    show madd conflicted at left_small
    with dissolve
    x "(This was so degrading, so humiliating, but I couldn't help but moan softly as he continued to dominate me, to own me...)"
    show madd broken at left_small
    with dissolve
    x "(My body was betraying me, responding to his touch. I hated myself for enjoying this, for wanting it...)"

    scene scene_sleep_next_to_dad_night_after_locked_room_3_kiss_dad_second_back_to_licking_closeup_i_want_you_again
    with fade
    show madd overwhelmed at left_small
    with dissolve
    x "(He finally stopped licking me and pulled away slightly, his breathing heavy. His hand gripped my arm tightly, possessively, as he licked my face one big lick all over, tasting every inch of me...)"
    show madd anxious at left_small
    with dissolve
    dad_says "I want you again, Maddie..."
    x "(His free hand reached down to my face and he grabbed my face roughly, turning it to look at him. He pulled me closer to him, closer and closer, and continued licking my face and neck.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(My body was responding to his every touch, trembling, giving in...)"
    x "(I FORGOT. I forgot his words. I was so lost in his licks and touches that I missed what he just said, my mind foggy...)"
    show madd horrified at left_small
    with dissolve
    x "(He wanted me again. I knew what that meant. He was gonna penetrate me again, fully, completely...)"
    show madd determined at left_small
    with dissolve
    x "(No, no, I must not let him penetrate my pussy. I must stop him, I must resist. I need to keep him away from my pussy, it's the only line left...)"
    show madd paralyzed at left_small
    with dissolve
    x "(My body was betraying me again. I can perhaps let him put it in my butt, but not my pussy, not there, no no no...)"
    scene scene_sleep_next_to_dad_night_after_locked_room_3_kiss_dad_lifting_madd_shirt
    with fade
    show madd flustered at left_small
    with dissolve
    x "(He starts lifting my shirt, and I feel his warm hands on my skin, the warmth shocking against the cool air of the bedroom. Sharp contrast with the cold that makes me shiver...)"
    show madd resigned at left_small
    with dissolve
    x "(I didn't stop him. I let him lift it, part of me wanting it, needing the contact. I even raised my arms to help him, to make it easier for him to undress me...)"
    show madd helpless at left_small
    with dissolve
    x "(He tosses my shirt aside, exposing my bare chest to him, leaving me vulnerable, exposed...)"
    show madd broken at left_small
    with dissolve
    x "(Another one of those nights where I let him do whatever he wants to me, where I don't even try to stop him...)"

    scene scene_sleep_next_to_dad_night_after_locked_room_3_kiss_dad_lifting_madd_shirt_hands_on_chest_groping
    with fade
    show madd distressed at left_small
    with dissolve
    x "(With access to my bare chest, he starts to caress and fondle me, his touch invasive and all-consuming. I can feel his hands exploring every inch of my skin, mapping my body like territory...)"
    show madd violated at left_small
    with dissolve
    x "(He started tightly groping my chest, no care in the world that he was touching his own daughter, that this was taboo and wrong...)"
    show madd conflicted at left_small
    with dissolve
    x "(I felt a mix of emotions. Shame, excitement, confusion, all tangled together...)"
    show madd paralyzed at left_small
    with dissolve
    x "(He was so rough and eager with it. I knew this night was gonna end with some of his filthy fantasies, with him using me however he wanted...)"
    x "(He finally stops groping me, his lips, his tongue has been all over my neck this whole time...)"
    show madd anxious at left_small
    with dissolve
    x "(His hand starts moving downwards, lower and lower...)"
    scene scene_sleep_next_to_dad_night_after_locked_room_3_kiss_dad_lifting_madd_shirt_hands_on_chest_groping_hands_inside_shorts
    with fade
    show madd trembling at left_small
    with dissolve
    x "(He didn't ask for permission and straight up went inside my shorts, crossing the last boundary without hesitation...)"
    show madd paralyzed at left_small
    with dissolve
    x "(He was just touching the soft skin of my lower belly, his fingers tracing across my skin...)"
    x "(Then he started lowering my shorts with his hand inside them, pulling the fabric down slowly, teasingly...)"
    show madd shocked at left_small
    with dissolve
    x "(He was very aggressive today, at a point he stopped trying to lower them carefully and just yanked them off, tearing...)"
    show madd distressed at left_small
    with dissolve
    x "(The fabric tearing apart as it came off, leaving me completely exposed...)"
    show madd helpless at left_small
    with dissolve
    x "(Now I was fully naked, from top to bottom, sleeping with my dad like this, vulnerable and bare...)"
    scene scene_sleep_next_to_dad_night_after_locked_room_3_kiss_dad_lowering_his_shorts
    with fade
    show madd anxious at left_small
    with dissolve
    x "(He stopped kissing me for a moment to lower his own shorts. I felt the bed lower as he got up on his knees to take them off, the movement quick and decisive...)"
    show madd shocked at left_small
    with dissolve
    x "(I raised my head a bit to see him taking them off. His hardening member was now fully exposed. It was humongous, intimidating, terrifying...)"
    show madd horrified at left_small
    with dissolve
    x "(I knew what was coming next. It was gonna happen, I couldn't stop it, I couldn't say no...)"
    scene scene_sleep_next_to_dad_night_after_locked_room_3_first_anal_insertion
    with fade
    show madd resigned at left_small
    with dissolve
    x "(I lowered my head back down to the pillow as he positioned himself behind me. There was no point in resisting anymore, no point in saying no, I had surrendered...)"
    show madd paralyzed at left_small
    with dissolve
    x "(His hands were on my breast then they moved, he held my elbows firmly as he started to push his member against my bare butt. With my elbow he was pulling me closer to him, and with his dick he was pushing against my anus, testing, preparing...)"
    show madd distressed at left_small
    with dissolve
    x "(I couldn't help but let out a small moan as he started to push inside me. The sensation was overwhelming, a mix of pain and pleasure that made my entire body tense...)"
    show madd overwhelmed at left_small
    with dissolve
    x "(He kept pushing until he was fully inside me. I could feel every inch of him filling me up, stretching me, claiming me. It was a strange feeling, invasive and wrong, but I couldn't deny the pleasure that came with it...)"
    show madd broken at left_small
    with dissolve
    x "(The room was silent except for the sound of my moans, his breathing, the creaking of the bed under his weight, and the sound of his balls slapping against my butt, a rhythmic reminder of what was happening...)"
    show madd violated at left_small
    with dissolve
    x "(It was so humiliating that I was letting my stepdad take me like this, in the bed of my mom, in my parents' bedroom. But at the same time I couldn't help but feel aroused, conflicted...)"
    show madd self loathing at left_small
    with dissolve
    x "(I was his. His daughter, his wife, his property, and he was taking what was his, what he believed belonged to him...)"
    scene scene_sleep_next_to_dad_night_after_locked_room_3_first_anal_sex_1
    with fade
    show madd blush at left_small
    with dissolve
    x "(He started thrusting inside me, slowly at first, testing, feeling. Then faster and harder, losing control...)"
    show madd overwhelmed at left_small
    with dissolve
    x "(His hands moved to my waist gripping it tightly, holding me in place as he pounded into me with increasing intensity...)"
    show madd flustered at left_small
    with dissolve
    x "(Each thrust sent waves of pleasure through my body. I couldn't help but moan louder with each one, louder and louder...)"
    show madd helpless at left_small
    with dissolve
    x "(I could hear his grunts of pleasure as he fucked me, his voice low and primal. It was like we were the only two people in the world, like nothing else existed...)"
    show madd conflicted at left_small
    with dissolve
    x "(He was enjoying himself immensely, I could feel it in the way he was moving with such energy and need, the way he was holding me like he never wanted to let go...)"
    show madd self loathing at left_small
    with dissolve
    x "(Some dirty part of me was loving every second of it. The taboo nature of our act only heightened the pleasure, and the fact that him being my stepdad made it even more thrilling, even more wrong...)"
    show madd blush at left_small
    with dissolve
    x "(I was glad that he was happy and enjoying himself. It made me feel wanted and desired, even if it was in a twisted and corrupted way, even if it meant allowing this abuse...)"

    scene scene_sleep_next_to_dad_night_after_locked_room_3_first_anal_sex_2
    with fade
    show madd distressed at left_small
    with dissolve
    x "(As he continued his assault on my body, his hand reached up to my chest again, doing the same groping and fondling as before, rough and possessive...)"
    show madd flustered at left_small
    with dissolve
    x "(Then it reached down to my hands, holding my hands like a lover would do, intertwining his fingers with mine. It was a strange feeling, being held like that while being fucked by my stepdad, intimate and violent all at once...)"
    show madd conflicted at left_small
    with dissolve
    x "(Even though it was wrong, even though it made my skin crawl and my stomach turn. I couldn't help but feel a sense of intimacy in that moment, of connection, of being wanted...)"
    show madd helpless at left_small
    with dissolve
    x "(I should be hating this, I should be pushing him away, creating distance. But I wasn't doing any of that. I was letting him do whatever he wanted to me, accepting my fate...)"
    show madd broken at left_small
    with dissolve
    x "(I was letting him mold me into his wife, the one he so desperately wanted, the one he'd been grooming me to become since the moment he met me...)"
    scene scene_sleep_next_to_dad_night_after_locked_room_3_first_anal_sex_3
    with fade
    show madd overwhelmed at left_small
    with dissolve
    x "(His hands moved back to my chest, another rough groping session, kneading my flesh like dough. The way his whole body was moving against mine was synchronized, it was like we were in perfect sync, one body with two minds...)"
    show madd anxious at left_small
    with dissolve
    x "(Then his hand moved down to my hips again, gripping them tightly as he continued to thrust into me, accelerating, losing himself in the moment...)"
    show madd deep blush at left_small
    with dissolve
    x "(The pleasure was overwhelming, absolutely intense. I could feel myself getting closer and closer to the edge, to that precipice. I was so close to cumming, orgasming because of my stepdad, in the bed of my mom, in this forbidden place...)"
    show madd self loathing at left_small
    with dissolve
    x "(I thought about it, I was in a locked room willingly allowing my stepdad to take me like this. My lungs full of his scent, his smell marking me. My face, neck all covered in his saliva. My butt being pounded by his huge member, which soon was going to fill with his cum, his seed...)"
    show madd flustered at left_small
    with dissolve
    x "(Something about that thought made me even more aroused, even more eager. Suddenly being his dirty little wife felt so right, so natural, like this was where I belonged...)"
    scene scene_sleep_next_to_dad_night_after_locked_room_3_first_anal_sex_cumming
    with fade
    show madd anxious at left_small
    with dissolve
    x "(I feel his breathing getting heavier, more ragged, more desperate. His thrusts getting more erratic, more wild. His dick pulsing inside me, throbbing. I knew he was close, I could feel it building...)"
    show madd overwhelmed at left_small
    with dissolve
    x "(It started thumping harder inside me, harder and harder. Each thrust sending waves of pleasure through my body, pushing me closer to my own climax...)"
    show madd shocked at left_small
    with dissolve
    x "(That's when I felt it. The warmth spreading inside me, his cum filling me up, flooding my insides. I let out a loud moan as I felt myself cumming as well, the pleasure overwhelming, hitting me all at once...)"
    show madd blush at left_small
    with dissolve
    x "(He must have felt it too, me climaxing around his member, my muscles contracting. It must have sent him over the edge, pushed him past the point of no return. We both reached our peaks together, our bodies trembling with pleasure, with ecstasy...)"
    show madd distressed at left_small
    with dissolve
    x "(He continued to thrust inside me for a few more moments, riding out his orgasm, emptying himself into me. I could feel my anus filling up with his cum, filling to capacity, some of it leaking out, running down my thighs...)"
    show madd violated at left_small
    with dissolve
    x "(The sound of the room changed, filled now with the sound of our heavy breathing, rapid and ragged. The creaking of the bed under our combined weight, and the wet squelching sound of his cum leaking out of me while he continued pounding into my butt, pushing deeper...)"
    show madd broken at left_small
    with dissolve
    x "(I just got dominated anally by my stepdad, in the bed of my mom, and I loved every second of it. His cum still flooding my insides, a filthy reminder of what I was, his property, his dirty little wife...)"
    x "(He didn't say a word, he let his dick soften inside me, it stayed there for a while, still connected to me...)"
    show madd relieved at left_small
    with dissolve
    x "(After a while he finally pulled out of me, the sensation of him leaving my body was almost as intense as when he entered it. It was like a part of me was being ripped away, leaving me empty and hollow...)"
    show madd resigned at left_small
    with dissolve
    x "(I didn't care though, not really. I was still filled with his cum, a constant reminder of our night together, of the forbidden pleasure we shared, of what I'd become...)"
    show madd distressed at left_small
    with dissolve
    x "(I put on my shirt again, didn't put on my shorts, they were torn and destroyed and would get ruined if I tried to wear them again. I left my lower half exposed to his view...)"
    show madd violated at left_small
    with dissolve
    x "(I was laying there next to him, my butt still laying on the bed where he just fucked me, the cum was pooling around the area of the bed where he made his mark. The sheets were soaked...)"
    show madd broken at left_small
    with dissolve
    x "(I was laying in that pool of cum, my stepdad's cum, and I couldn't help but smile softly. That was my life now, being his dirty little wife, his property, and I was okay with that, I was accepting it...)"
    show madd resigned at left_small
    with dissolve
    x "(He took the blanket and covered us both, pulling me close. I felt so warm and safe in his arms, held, protected. Even after everything that had happened, even covered in his cum. Well, of course I felt warm, I was covered in his cum, his seed, his essence...)"
    scene scene_sleep_next_to_dad_night_after_locked_room_3_aftermath_did_you_like_it
    with fade
    show madd flustered at left_small
    with dissolve
    x "(As I tried to sleep he moved closer to my face, his hand resting on my head pulling me closer to him, stroking my hair...)"
    show madd confused at left_small
    with dissolve
    dad_says "I loved every moment of that, Maddie."
    x "(He gives me a soft kiss on the forehead before raising himself slightly and asks me, his voice gentle but with an undertone of possessiveness...)"
    show madd hopeful at left_small
    with dissolve
    dad_says "Did you like it, sweetheart?"
    show madd conflicted at left_small
    with dissolve
    x "(My body loved it, absolutely loved it. I was filled with his cum, it was inside me, marking me. My butt still sore from the rough pounding, tender and aching. But a part of me felt satisfied, deeply satisfied, like I had finally found my place, my purpose, as his dirty little wife...)"
    show madd horrified at left_small
    with dissolve
    x "(But should I tell him the truth? That I actually enjoyed it, that I wanted more of it? Or should I just keep pretending that it was all wrong, that I hated it, that I wanted to escape? The choice terrified me...)"

    menu:
        "I....I loved it..daddy":
            jump sleep_next_to_dad_night_after_locked_room_3_loved_it_daddy
        "I...I hated it....Never touch me again":
            jump sleep_next_to_dad_night_after_locked_room_3_hated_it_never_touch_me_again



    label sleep_next_to_dad_night_after_locked_room_3_loved_it_daddy:
    $ journal_event_set_done("Dad", "Dad's Room Night 3")
    scene scene_sleep_next_to_dad_night_after_locked_room_3_loved_it_daddy
    with fade
    show madd blush at left_small
    with dissolve
    x "(I look into his eyes and smile softly, genuinely, a real smile that comes from deep inside me...)"
    show madd flustered at left_small
    with dissolve
    x "I...I loved it...daddy."
    show madd happy at left_small
    with dissolve
    dad_says "Hmmm...that's my wife.."
    show madd violated at left_small
    with dissolve
    x "(He continues licking my face and neck tenderly, softly, almost lovingly. I knew he liked that answer, that it pleased him, that it made him happy...)"
    scene scene_sleep_next_to_dad_night_after_locked_room_3_loved_it_daddy_reward_door_unlocked
    with fade
    show madd shocked at left_small
    with dissolve
    dad_says " I will open the door to your room for your good behavior, my little wife."
    show madd flustered at left_small
    with dissolve
    x "(He says that and starts roughly kissing me again, his lips pressing against mine. I can feel his hands roaming my body again, possessive, claiming...)"
    show madd deep blush at left_small
    with dissolve
    x "(But I was shocked when he said that, genuinely shocked. I was getting rewarded for letting him do whatever he wanted to me, for submitting to him. That was incredible, that was power, that was control...)"
    show madd violated at left_small
    with dissolve
    x "(He kept roughly licking my face, by now I was loving the smell of his saliva on me, the scent of his dominance. He was marking his property, marking me as his...)"
    show madd resigned at left_small
    with dissolve
    x "I'm glad daddy..."
    show madd broken at left_small
    with dissolve
    x "(I say that as my stepdad continues to kiss and lick me all over, claiming me again and again...)"
    x "(He continued licking me few more moments before I fell asleep, tired from all the abuse he just put me through, my body exhausted. But I was happy, genuinely happy, happy playing the role of his dirty little wife, his replacement for my mom, his possession...)"
    x "(Even though I'm not sure if I even want to escape this situation anymore. I was starting to like it, starting to accept it, being his property, his wife, his slave...)"

    $ madd_room_got_unlocked = True
    $ locked_home_areas.remove("madd_home_room") if "madd_home_room" in locked_home_areas else None
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["kissed"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["anal_sex"] += 1
    $ character_relations["dad"]["anal_creampie"] += 1
    $ character_relations["dad"]["intimacy"]+=7
    $ character_relations["dad"]["lust"] = 0
    $ character_relations["dad"]["anger"] =0 
    $madd_willpower=max(madd_willpower-20,0)
    $ dad_anal_scene_completed = True
    
    scene black
    with fade

    x "(i doze off to sleep...)"

    menu:
        "Search for main door keys" if madd_willpower > 20:
            jump search_for_main_door
        
        "I have no energy":
            x "(I'm too exhausted... I can barely move...)"
            
            jump sleep_on_bed_dad_room



    jump sleep_on_bed_dad_room


    label sleep_next_to_dad_night_after_locked_room_3_hated_it_never_touch_me_again:
    $ journal_event_set_done("Dad", "Dad's Room Night 3")
    scene scene_sleep_next_to_dad_night_after_locked_room_3_hated_it_never_touch_me_again
    with fade
    show madd angry at left_small
    with dissolve
    x "(I looked away from him, I don't want him to know I enjoyed it, I don't want him to see the pleasure in my eyes...)"
    show madd horrified at left_small
    with dissolve
    x "I...I hated it...Never touch me again."
    show madd anxious at left_small
    with dissolve
    x "(I heard anger in his tone, a dangerous edge, as he said...)"
    show madd traumatized at left_small
    with dissolve
    dad_says "You will love it..."
    show madd distressed at left_small
    with dissolve
    x "(He pulled my hair roughly, his grip tight and painful, and starts roughly licking my whole face again, aggressively, forcefully...)"
    show madd shocked at left_small
    with dissolve
    x "(I felt his dick hardening again as he continued to kiss and lick me, his arousal returning quickly. I knew he wasn't done with me yet, not by a long shot...)"
    show madd broken at left_small
    with dissolve
    x "(He inserted his dick in my ass again, pushing inside without waiting. I was too tired at that point, too emotionally drained, I just blacked out, losing consciousness...)"
    scene black
    with fade
    x "(I dont know how long it has been  he kept ravaging my asshole )"
    x "(I heard his heavy breathing and grunting sound one more time ,He came inside me again didnt he ..)"
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["kissed"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["anal_sex"] += 1
    $ character_relations["dad"]["anal_creampie"] += 2
    $ character_relations["dad"]["intimacy"]+=3
    $madd_willpower=max(madd_willpower-20,0)
    $ dad_anal_scene_completed = True
    x "(I blacked out again.)"

    menu:
        "Search for main door keys" if madd_willpower > 20:
            jump search_for_main_door
        
        "I have no energy":
            x "(I'm too exhausted... I can barely move...)"
            $ character_relations["dad"]["intimacy"] += 3
            
            jump sleep_on_bed_dad_room


    label search_for_main_door:
    
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping
    with fade
    show madd horrified at left_small
    x "(I woke up and immediately felt the searing pain shoot through my entire body. My asshole was absolutely throbbing in excruciating agony. I could feel it... still full... completely stuffed with his cum.)"
    scene scene_sleep_next_to_dad_night_after_locked_room_3_hated_it_walk_to_drawer
    with fade

    show madd disgusted at left_small
    x "(My own stepfather's hot, sticky cum is still floating inside me... pooling inside my body like some kind of grotesque reminder of last night. That is so... absolutely gross.)"
    
    show madd self loathing at left_small
    x "I can't believe I actually let him do that to me... How did I even let this happen?"
    
    show madd traumatized at left_small
    x "(Letting my own stepfather cum inside me... what type of girl... what kind of daughter lets her own stepfather do something like that? What am I becoming?)"
    
    show madd horrified at left_small
    x "He came inside me twice... not once but twice... I'm still feeling it."
    
    show madd paralyzed at left_small
    x "(Each movement sends fresh waves of pain through me as I slowly started walking towards the drawers.)"
    
    show madd distressed at left_small
    x "My butt still hurts so much... it hurts to even walk... every single step is torture..."
    



    scene scene_sleep_next_to_dad_night_after_locked_room_3_hated_it_walk_to_drawer_search_keys
    with fade
    
    show madd focused at left_small
    x "(I read somewhere that climaxing makes people fall into a deeper sleep... and he just came twice... which means...)"
    
    show madd determined at left_small
    x "(Now would be the perfect time to search for the main door keys... to finally plan my escape from this nightmare.)"
    
    show madd relieved at left_small
    x "Well, at least now that he came twice inside me, he'll be sleeping heavily for a long time. That gives me a window... an opportunity..."
    
    show madd hesitant at left_small
    x "(I carefully bent down to open the drawer and begin searching for those keys.)"
    
    show madd focused at left_small
    x "I can finally search for the keys now without interruption... without him watching me..."

    if stole_2000_dollars==False:
        scene scene_dad_ass_usb_discovery
        with dissolve
        
        show madd uncertain at left_small
        x "( I found a USB with sticker attached saying CRYPTO 2000 USD)"
        
        show madd nervous at left_small
        x "( Crypto..thats what killed my dad its gonna be used to save me from this abusive lifestyle )"
        
        show madd stressed at left_small
        x "( Life truly comes full circle huh , thanks crypto ! )"
        
        show madd hopeful at left_small
        x "( The total value... is... 2000 dollars... exactly what I need... )"
        
        show madd relieved at left_small
        x "( This is... this is everything... )"
        
        show madd happy at left_small
        x "( Tears start streaming down my face... tears of relief... tears of hope... )"
        
        show madd submissive nod at left_small
        x "( I'm crying... actually crying from happiness and the terrible cost of this escape... )"
        
        show madd determined at left_small
        x "( I have what I need to escape... to get away from this house... from him... )"
        
        show madd focused at left_small
        x "( I carefully eject the USB and pocket it )"
        
        show madd hopeful at left_small
        x "( I wipe my tears and try to compose myself... )"
        

        if not stole_2000_dollars:
            $madd_money+=2000
            $stole_2000_dollars = True
            $stole_2000_dollars_date = game_time.get_date_string()
            $stole_2000_dollars_day = days_passed
        
        x "(Now back to searching for the keys... I have to find those keys...)"
    
    scene scene_sleep_next_to_dad_night_after_locked_room_3_hated_it_walk_to_drawer_search_keys_found_keys
    with fade
    
    show madd uncertain at left_small
    x "(I searched through the first drawer... just bunches of papers and stationary items scattered about... but it was only half open.)"
    
    show madd hopeful at left_small
    x "(I pushed it in and then pulled the entire drawer out this time, and suddenly... a wide smile spread across my face as I finally found them... the main door keys.)"
    
    show madd happy at left_small
    x "Yes! Finally! I got it!"
    
    show madd determined at left_small
    x "This is my road to freedom... this is the way out..."
    
    show madd relieved at left_small
    x "(I can't believe my escape was suddenly so close now... within my grasp... possible...)"
    
    show madd conflicted at left_small
    x "(Even though my asshole got completely ravaged by my own stepfather, there is... a silver lining to all of this. Maybe there's something good coming from this nightmare.)"
    
    show madd depressed at left_small
    x "I guess... taking two loads inside me...... I guess it was worth it if I can get away from this place."
    
    scene scene_sleep_next_to_dad_night_after_locked_room_3_hated_it_walk_to_drawer_search_keys_found_keys_put_back_keys
    with fade
    
    show madd curious at left_small
    x "(I best not take the keys yet... not tonight... I know exactly where they are now, and I can come back to get them on the night I'm about to leave... when I make my final escape.)"
    
    show madd focused at left_small
    x "Now I know exactly where the keys are... I have the knowledge I need... freedom is within reach..."
    x "I can come get it when Im ready to leave and have paid the bills."
    x "(I put the keys back in the drawer carefully and went back to bed. My butt still sore from the pounding i took last night.)"
    $ journal_event_show("Madd", "Stealing the Keys")
    $ main_door_key_found = True
    $madd_willpower=max(madd_willpower-20,0)
    $ journal_event_set_done("Dad", "Found the Keys")
    jump sleep_on_bed_dad_room

    
label sleep_next_to_dad_night_vaginal:
    scene step_parent_room_scene_night_enter_madd_inside_dad_sleeping_lie_next_to_dad
    with dissolve  
    $ renpy.call_in_new_context("_hide_windows")
    show madd anxious at left_small
    with dissolve
    x "(I lie down next to him carefully, trying not to make any sudden movements that might wake him. My hands are shaking slightly as I lower myself onto the mattress, my breath shallow.)"
    x "(I know how the last few times it's ended with him using me while I sleep. )"
    x "(We have already crossed all the boundaries between a father and daughter, if he wakes up, I know what will happen. )"

    scene scene_sleep_next_to_dad_night_after_locked_room_3_dad_hand_on_madd_body
    with dissolve 
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    with dissolve
    x "(Immediately after lying down, I feel his hand all over me, like he was waiting for me.)"
    x "(He immediately locks me down with his hand on my elbow locking me in place and I can't move, can't even breathe right.)"
    show madd paralyzed at left_small
    with dissolve
    dad_says "Sleeping here again? "
    x "(I heard his coarse voice and then felt his wet tongue exploring my neck, tasting me.)"
    show madd trembling at left_small
    with dissolve
    x "(He was licking and biting my neck like a wild animal. My body was frozen in place unable to move or resist, pinned under his weight.)"
    show dad dominant at right_small
    dad_says "You know what's gong to happen, right? "
    x "(I could feel his hot breath on my skin as he spoke, and I knew exactly what he meant. So i nodded my head slightly and said )"
    show madd resigned at left_small
    with dissolve
    x "Yes...dad."
    scene black 
    with dissolve 
    x "(Before i knew , he was on top of me fucking me in my pussy.)"

    scene scene_sleep_next_to_dad_night_vaginal_clothes_on_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd helpless at left_small
    with dissolve
    
    x "( his thick, veiny dick is stretching my pussy so wide it burns. Every brutal thrust splits me open like I'm nothing but a warm hole for him to ruin. He's been pounding me for so long but my pussy is gripping him like it doesn't want him to ever pull out.)"
    x "(His sweat keeps pouring off him in hot, sticky sheets. Thick drops rain straight onto my face — splattering across my forehead, sliding into my eyes, landing on my parted lips and tongue."
    x " ( The smell hits me like a punch: that heavy, sour, unwashed stench of my dad. )"
    x "(I noticed his mouth was open and his tongue was hanging out as he pounded into me and I understood why the sweat was pouring off him like a river and why it smelled so bad. )"
    x "(The sweat was mixing with his saliva and i was getting the final result of them both: the stench of my dad's unwashed body and the taste of his saliva all over my face and in my mouth.)"

    scene scene_sleep_next_to_dad_night_vaginal_clothes_on_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd disgusted at left_small
    with dissolve

    x "(God it's disgusting. The way it coats my face, the way every drop that hits my mouth tastes bitter and rancid, like I'm drinking his sweat and saliva while he fucks me. I want to gag, to turn away, but I can't move, his weight pins me down and all I can do is breathe it in, let it soak into my skin, let it mark me.)"
    show madd conflicted at left_small
    with dissolve
    x "(And the worst part? My pussy is getting even wetter. Every time that nasty, sour smell floods my nose I feel myself clench harder around his dick, like my body is thanking him for degrading me. I'm so fucked up... lying here getting railed by my own dad while his rank sweat drips into my open mouth and I can't stop the sick little thrill running through me.)"
    show dad lustful at right_small
    dad_says "You feel that? Daddy's cock ruining that tight little pussy. And you love it, don't you? Love daddy's sweat all over your pretty face."
    x "(Just how much of his saliva and sweat is on my face right now? He can tell just by looking at me, can't he? )"
    x "(I just nodded my head slightly, unable to speak, unable to deny it. )"
    show dad dominant at right_small
    dad_says "Good girl, lets get our clothes out of the way. Tonight, daddy will ruin you beyond recognition. "
    x "O...okay...dad."
    x "(Even though i was fine with taking my clothes off, he tore them off just like he tore the father-daughter boundary apart. )"

    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd violated at left_small
    with dissolve
    x "(Hours have passed. The clock on the wall says it's almost 2 a.m. now. He never stopped. Not once. My dad's thick, veiny cock is still buried balls-deep inside my pussy, still stretching me open, still pounding me like a savage animal that hasn't eaten in days.)"
    x "(We're both completely naked now. My torn clothes are scattered on the floor somewhere. His heavy, sweaty body is crushing me into the mattress, skin sliding against skin, our bodies slick with his filth. Every thrust makes wet, disgusting squelching noises — my ruined pussy gushing around him, mixing with his sweat and pre-cum.)"
    x "(And now he's biting me. Hard. His teeth sink into my cheek, my jaw, the soft skin just below my ear. Sharp, possessive bites that leave red marks and make me whimper.)"
    x "( Then he moves to my mouth — forcing his tongue past my lips, shoving it deep, swirling it around like he's trying to taste every inch of his daughter's mouth.)"
    x "(God it's so fucking disgusting. My own father's saliva is flooding my mouth.)"
    show madd shaken at left_small
    with dissolve
    x "(I can feel the shame burning in my chest. This is my dad. The man who was supposed to protect me after my mom died . But instead I became her replacement, her substitute)"


    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd helpless at left_small
    with dissolve
    x "(My mouth is forced wide open now. His tongue along with his lower teeth are hooked right over my top lip, holding it pulled back so I can't close. )"
    x "(A steady, warm stream of his saliva just keeps pouring straight from his open mouth into mine. Thick and slow at first, then heavier, like he's deliberately drooling into me. I can feel every viscous rope sliding over my tongue, pooling at the back of my throat before I have to swallow.)"
    x "(It smells so fucking bad up close — that sour, rotten-milk stench of his unwashed mouth mixed with the heavy musk of his sweat. Every time he exhales I get another hot wave of it right in my nose and down my throat. and I am locked in this position so  I can't turn away.)"
    x "(I keep trying to swallow it down but there's always more coming, overflowing from the corners of my lips, running down my chin in sticky strings.)"
    x "(And the sick part is my body is reacting like this is the best thing I've ever tasted. My pussy is clenching and fluttering around his cock every time I gulp down another mouthful of his spit. Like I'm thirsty for it. Like I need more.)"
    show dad debased at right_small
    dad_says "That's it... keep drinking daddy's spit, baby girl. Don't waste a single drop."
    x "(He growls it right into my open mouth, more saliva pouring out with the words, and I feel another hot gush slide down my throat.)"
    show madd resigned at left_small
    with dissolve
    x "(I'm not even fighting it anymore. I'm just lying here, mouth held wide by his teeth and tongue, taking every nasty, warm, stinking mouthful he gives me like it's the only thing keeping me alive.)"

    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd nauseated at left_small
    with dissolve
    x "(Now his whole mouth has clamped down over my nose. His lips are sealed tight around it, sucking and pulling like he's trying to draw something out of me. )"
    x "(His tongue is sticking out, thick and wet, right up against my nostrils. I can feel the hot, slimy tip pushing just inside one nostril, then the other, like he's deliberately smearing his spit directly into them. The smell is overwhelming — pure, concentrated stench of his unwashed mouth pouring straight into my nose from the source.)"
    show madd depressed at left_small
    with dissolve
    x "(This is what my life is reduced to for the foreseeable future. Lying here, being used and degraded by my own father )"

    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd overwhelmed at left_small
    with dissolve
    x "(I don't even know how much time has gone by anymore. Everything's blurred together. The only thing that feels real is his cock still moving inside me and now... now he's finally dropping his full weight down on top of me.)"
    x "(His body presses flat against mine. Skin to skin. No space left. His fat, greasy stomach is the first thing that hits — heavy, hot, and full of sweat. It spreads across my belly and chest like warm, sticky dough, smothering me under its weight.)"
    x "(It feels disgusting. The grease on his skin is rubbing off onto mine, leaving this thick, oily film everywhere it touches. I can feel every fold, every soft bulge of his gut molding against me, trapping heat and that sour, unwashed smell right between us.)"
    show madd nauseated at left_small
    with dissolve
    x "(My skin is crawling. Literally crawling. Little ripples of revulsion running up my arms and legs as his greasy stomach slides and presses, like it's trying to absorb me. I feel like I'm sinking into quicksand made of his filth — slow, inescapable, pulling me deeper into the warm, sticky mess of his body with every movement.)"
    show dad lustful at right_small
    dad_says "God that feels so good, doesn't it? "
    show dad wistful at right_small
    dad_says "Not gonna lie , i have wanted to pin you down like this for a long time. Maybe even before your mom died. "

    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd shocked at left_small
    with dissolve
    x "(His words hit me like a slap . He wanted this before mom died. Before any of it. He wasn't just using me to replace her. He wanted me. His own daughter. All along.)"
    x "(The thought makes my head spin. All this  time I thought I was just filling a hole she left behind, but no — he was looking at me like this even when she was still alive. Picturing pinning me down, feeling my skin under his greasy stomach, shoving his dick into me while I couldn't move. I was the one he really wanted. Not her. Me.)"
    show madd horrified at left_small
    with dissolve
    x "(It feels so much worse now. So much more twisted. I'm not the substitute. I'm the main event. The daughter he always craved, the one he waited for. And now he's got me exactly where he planned — naked, pinned under his heavy, sweaty body, my face still trapped in his mouth while he fucks me like he's been dreaming about for years.)"
    show dad possessive at right_small
    dad_says "You understand now, don't you? You've always been the one."
    show dad obsessed at right_small
    dad_says "You're the one for me. You're the one who will give me everything I want. "
    x "(My mind keeps looping on it while he keeps pounding. All those years... he was waiting for this. Waiting to pin his daughter down and cover her in his filth, drown her in his spit, fuck her until she couldn't think straight. And I'm here. Taking it. Wanting it even more because of what he just admitted.)"
    show dad dominant at right_small
    dad_says "Fuck Fuck Fuck Maddie...This is the first time you came to sleep next to me , I will make sure you will do it by yourself every night. "

    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    with dissolve
    x "(He suddenly starts slamming into me way harder. The bed creaks loud under us. Every thrust now feels like he's trying to punch straight through me. His dick is reaching places it hasn't touched all night — deeper, meaner, stretching parts of me that make my vision blur.)"
    x "(At the same time his fat gut is pressing down even heavier, like it's trying to sink right into me. I can feel his greasy skin pushing against mine, the heat and oil from his body starting to mix with my own. It doesn't feel like two separate bodies anymore. It feels like his filth is melting into me, seeping through my pores, becoming part of me on some deep, nasty level.)"
    show dad lustful at right_small
    dad_says "Girl you make me so bricked up. I can't get enough of you. I want to fuck you until you can't walk, until you can't even remember your own name. "
    x "(This is it. This is what he meant when he said I was the one. He's not just using me tonight. He's changing me. Turning me into something that carries his filth forever. And I'm lying here taking every hard, deep thrust while his body melts into mine like it's exactly what I was made for.)"
    show dad possessive at right_small
    dad_says "My only regret was that you're not my real daughter. But dont worry after tonight, you will be mine in every way that matters. "
    show dad dominant at right_small
    dad_says "Even the dog with sharpest smelling nose won't be able to tell the difference between you and a real daughter after tonight. "
    show madd resigned at left_small
    with dissolve
    x "( He's gonna cover me in his filth from head to toe, inside and out. He's gonna mark me like his own, make sure everyone knows I'm his. )"


    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_7
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    with dissolve
    x "(His eyes are locked straight on mine now. He pulled his face back just enough to stare down at me while his dick stays buried deep. Those eyes are dark and hungry, like he's finally saying out loud what he's been thinking for years.)"
    show dad obsessed at right_small
    dad_says "I'm gonna knock you up, Maddie. Multiple times. Gonna fill this pussy over and over until your belly swells up big and round with my seed. You're gonna carry my babies. One after another."
    if madd_dp_finished:
        show dad possessive at right_small
        dad_says "Maybe here and there I will let Adam have a turn too. But you will always be mine first and foremost. "
    show dad perverted at right_small
    dad_says "Imagine it. Your stomach all stretched out, heavy with my load. Everyone seeing you waddling around knowing exactly who put it there. And then after you pop one out, I'm just gonna put another one in you. Keep you full for years."
    show dad dominant at right_small
    dad_says "You like that idea, don't you? Your dad's babies growing inside you. Say it. Tell me you want me to breed this pussy until you're always carrying my load."
    show madd conflicted at left_small
    with dissolve
    x "(I can't even speak. I'm just lying there, eyes locked on his, trying to process the nightmare he's describing. I dare not say it out loud, but the sick part is... I do want it. )"

    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_8
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    with dissolve
    
    show dad calculating at right_small
    dad_says "Even if you don't say it right now, you will by the end of the night. I can feel it. Your body already knows what it wants."
    show dad controlling at right_small
    dad_says "After tonight you won't be able to sleep anywhere else. Not in your own bed. Not on the couch. Not even in another room. The only place you'll be able to close your eyes is right here, pinned under me with my dick still inside you and my load leaking out of that used pussy."
    show dad dominant at right_small
    dad_says "You'll come crawling back here on your own. Begging to sleep next to daddy again. And every time you do, I'm gonna breed you a little more."
    x "(His eyes never leave mine. He's still staring straight into me like he can already see the future he's describing — me pregnant with inability to refuse him )"
    show dad predatory at right_small
    dad_says "By sunrise you'll be saying it. 'Breed me, daddy. Knock me up again.' You'll say it while I'm filling you. And you'll mean every word."
    x "(Is this really gonna be my future? Getting degraded and used every night by my dad. )"
    show madd hopeful at left_small
    with dissolve
    x "(I didnt think much about it in the moment but for some reason, the thought of being pregnant with his babies and waddling around with a big belly full of his seed made me feel something. Like a twisted kind of hope. Like maybe if I can just get through tonight, if I can just survive this, then maybe there will be something good at the end of it. Something that makes all this worth it.)"

    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_9
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd overwhelmed at left_small
    with dissolve

    x "(The whole room is quiet except for two sounds. My own broken moans spilling out of my open mouth and the loud, wet clapping of my ass cheeks against his crotch and every time his balls slap against them.)"
    x "(Just the filthy rhythm of skin on skin contact , my butt rippling and clapping loud every time he drives in deep, his heavy balls swinging and smacking right against me with every brutal thrust.)"
    x "(My moans keep coming out without me even trying. Little broken sounds that mix with the clapping. I sound pathetic. I sound like I'm getting destroyed which I am. Dad's fucking me so hard the bed is shaking and the only thing I can hear is my own voice and my ass getting clapped raw by his balls.)"
    show madd resigned at left_small
    with dissolve
    x "(I guess that's the soundtrack of my life now. That's what I get to hear every night. Sound of my own body getting pounded by my dad while I moan and my butt gets slapped by his balls. )"

    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_10
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd conflicted at left_small
    with dissolve
    x "(His head leans in closer until his face is right above mine again. His greasy body keeps sliding and rubbing all over me with every thrust, that hot, sticky gut pressing and grinding my petite frame )"
    x "(The closer he gets, the worse my moans sound. They stop being human. They turn low and guttural, coming out in broken, animal grunts every time he slams in. I sound like a bitch in heat — raw, desperate, non-human sounds spilling out of me while his greasy stomach rubs and smears across my body.)"    
    x "(What ... what is this feeling? I know it's wrong. I know it's disgusting. But I can't stop it. I can't stop the way my body is reacting to this. )"
    show dad smirk at right_small
    dad_says "Ah, there it is. That's the sound I wanted to hear. "
    show dad sadistic at right_small
    dad_says "We havent even reached the best part yet. Just wait until you start leaking cum from that used pussy of yours. "
    x "( Is he still holding back? Is there more to this nightmare? )"
    
    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_11
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd conflicted at left_small
    with dissolve
    x "(I....I hate to admit it but I can feel it. I wont be able to go back to being a normal person after this. )"
    x "(Fuck...fuck...fuck... I can feel it building up inside me. That hot, thick pressure in my lower belly that tells I'm close to cumming. )"
    show madd overwhelmed at left_small
    with dissolve
    x "(I can't hold it anymore. My body is giving up. That pressure in my belly is getting too strong and I know I'm about to cum on my dad's dick while he's still talking about breeding me. I hate it. I hate how much I need it right now.)"
    x "(If anyone ever found out... the world would see me as the sick daughter who let her own dad knock her up. They'd say I was broken, disgusting, that I begged for it. And they'd be right. Because I'm about to do exactly that.)"
    x "(The thought makes my stomach twist but my pussy is throbbing harder than ever. Everyone would look at me waddling around with a big pregnant belly and know my dad put it there. They'd know I sleep in his bed every night getting fucked raw. And instead of feeling shame i was  getting more turned on by the thought. )"
    x "(i gulp one last time , his saliva and sweat making me even more desperate for him, as i finally told him what he wanted to hear.)"
    x "Fuck me.."
    x "Fuck me....dad."

    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_12
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd overwhelmed at left_small
    with dissolve
    x "(The second those words leave my mouth he goes feral. His hips slam down harder than ever, pounding me like he's trying to break me in half. Every thrust knocks the air out of my lungs and makes that hot pressure in my belly spike even higher.)"
    show dad excited at right_small
    dad_says "Fuck Maddie... I've been waiting all night to hear you say that. Been waiting years. Say it again while I ruin this pussy."
    x "(My orgasm is right there, building so fast I can barely think. His greasy body is rubbing all over me, his dick is hammering so deep it feels like it's in my stomach, and all I can do is moan like an animal while he demands more.)"
    show dad dominant at right_small
    dad_says "Tell me you're my breeding bitch. Tell me you want your dad's babies stretching your belly. Say it loud."
    x "I'm... I'm your breeding bitch dad... I want your babies stretching my belly..."
    show dad authoritative at right_small
    dad_says "Louder. Tell me you love getting fucked by your own dad. Tell me this used pussy belongs to me forever."
    x "I love getting fucked by my own dad... this pussy belongs to you forever... please don't stop..."
    x "(The words keep spilling out of me while he pounds harder. My body is shaking, my orgasm seconds away, and I'm saying the most disgusting, demeaning sht I've ever said in my life. And the worse it gets, the closer I get to cumming.)"


    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_13
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")  
    show madd overwhelmed at left_small
    with dissolve
    x "(I can feel it crashing over me. My whole body is locking up around his dick while I say these filthy things. I'm cumming on my dad's cock while begging to be his permanent breeding bitch. And I don't even care how broken I sound anymore.)"
    x "(It hits me hard. My whole body locks up and then I start cumming in thick, heavy waves. My juices coats his cock and balls in a messy layer, turning everything between us into a slippery, sticky mess. I can feel it leaking out around him with every thrust, making it even wetter.)"
    x "(It was not a squirt or anything like that. Just a steady, heavy flow of my juices pouring out of me )"
    x "(The sound changes right away. The clapping turns into loud, nasty, wet squelching. Every time he slams in now it makes these thick, creamy noises — like he's stirring up a heavy batch of my cum mixed with his precum. The whole room fills with that sloppy, wet sound.)"

    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_14
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small
    with dissolve
    x "(My moans have turned into something else now. These high, desperate, slutty sounds keep pouring out of me like I've been locked up for years and finally got let out. I'm moaning like a bitch who just got her first real release after being denied forever.)"
    show dad mocking at right_small
    dad_says "Listen to you... sounding like a desperate little slut who finally got to cum. I did that. "
    show dad possessive at right_small
    dad_says "Oh Maddie you realize that you just came from your dad's cock right? That means you belong to me now. Completely."
    x "(His words hit me while I'm still shaking from the orgasm. The wet, creamy squelching is still loud between us as he keeps thrusting through the mess I made.)"
    show dad dominant at right_small
    dad_says "You hear how wet you are? That's all for me. Your body knows who owns it now. Say it. Tell me you belong to daddy."
    x "I... I belong to you dad"
    x "I can't believe i was missing out on this for so long. "
    x "I love having you as my dad. I love being your daughter. "
    x "(All of the words are coming out of my mouth without me even thinking about it. Its as if my mouth was in sync with his filthy thoughts my body had been having)"
    show dad smirk at right_small
    dad_says "That's right girl. "
    show dad lustful at right_small
    dad_says "Fuck... I'm getting close. I'm gonna fill this used pussy up. Take it all, Maddie. Don't waste a single drop."
    x "(He's about to cum inside me. After everything — the breeding talk, the ownership, the filthy demands — he's finally going to pump his load into me. And I'm going to take it like the broken daughter I am.)"
    x "Yes... please dad... fill me up... "
    x "Give me my birthright... give me your seed... "
    show dad smirk at right_small
    dad_says "Damn , even I didn't think you'd beg for it like that. "
    x "(I feel him tense up. His thrusts get shorter and harder. I know he's about to unload everything he's been building up all night into me. And I'm going to take every bit of it.)"
    x "(I feel it the second it starts. His cock begins throbbing hard inside me, swelling to its absolute maximum length, stretching me even wider as he buries himself as deep as he can go.)"

    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_15
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd helpless at left_small
    with dissolve
    x "(He leans his full weight forward and presses my head down into the soft pillow with his own. His face is right against mine, hot breath on my ear while his body pins me completely. I can't move. I can only take it.)"
    x "(Then it happens. Hot, thick cum starts pumping out of him in heavy spurts. I feel every single pulse — warm ropes flooding deep inside me, filling me up fast.)"
    x "(The warmth spreads through my belly like some kind of twisted comfort, like my body is finally getting what it was always meant to have.)"
    x "(It's so much. It keeps coming. I can feel it coating my insides, making everything even messier and wetter. The creamy sounds between us get louder as his cum mixes with everything else. I'm lying here with my dad's seed pumping into me while he pushes my head deeper into the pillow.)"
    show madd conflicted at left_small
    with dissolve
    x "(The warmth keeps spreading. It feels disgusting and right at the same time. Like this is what I've been waiting for without even knowing it. His cum is claiming me from the inside, marking me as his in the most permanent way possible.)"
    x "(I don't even try to fight the feeling. The comfort of being filled by him is too strong. My body is accepting every drop like it's a gift. Like this is my real purpose — getting bred and filled by my own dad while he pins me down and uses me.)"
    show dad dominant at right_small
    dad_says "That's it... take it all, Maddie. Let daddy fill you up. Take my gift to you."


    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_16
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd relieved at left_small
    with dissolve
    x "I love the gift dad. I love feeling your warm cum filling me up like this... it's exactly what I needed..."
    x "(He doesn't stop. Even while he's still cumming he keeps thrusting, pushing more thick spurts deep inside me. I can feel it building up fast, the pressure getting too much.)"
    x "(It starts overflowing. Hot cum leaks out around his dick in thick globs, running down my ass and dripping onto the bedsheets in messy white streaks. The wet squelching gets even louder and filthier as more keeps pouring out of me.)"
    x "(I can feel more of it pushing out with every thrust. The warmth is still spreading inside me while the excess runs down and soaks into the sheets. I'm lying here in a puddle of his cum, pinned under him, taking load after load )"    
    x "(This is what I asked for. This is the gift I said I loved. And now it's everywhere — inside me, leaking out of me, staining the bed. And he's still going, still giving me more while I moan and take it all.)"
    x "(and i loved every second of it. )"

    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_17
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small
    with dissolve
    x "(My pussy is so full now I can't even tell if he's still hard. There's just this thick, heavy, viscous mess inside me — so much cum that everything feels swollen and packed tight. I can't feel any hardness anymore, just this warm, slimy fullness stretching me from the inside.)"   
    x "( I don't know how many times he's already cum. It feels like he's been pumping load after load for ages and still won't let any of it escape.)"
    x "(It's disgusting how much is in there. Every little movement makes more of that thick, sticky cum shift around inside me. I can feel it pressing against my walls, heavy and warm, while he stays locked in place. Like he's making sure every drop stays where it belongs — deep in his daughter.)"
    x "(And the sound it made was so filthy. Like a river of cum flowing inside me, mixing with my juices, making this wet, squelching mess that I can feel with every breath. )"
    x "(He stays inside me like a dog knotting its bitch. Not moving, not pulling back, just plugging me up so all his seed stays trapped.)"
    x "(This is what he wanted. Me completely full, overflowing, unable to tell where his dick ends and his cum begins. And this is what I wanted too. )"
    show dad debased at right_small
    dad_says "Soak it all in, Maddie. I want you breathing and swimming in my cum. "

    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_18
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd conflicted at left_small
    with dissolve
    x "I'm gonna throw away all my pills... anything that stop me from getting pregnant by you."
    x "I don't want them anymore."
    x "(His cheek is pressed right against mine. I can feel the corners of his mouth pulling up into a wide, satisfied smile. He doesn't say anything at first, just smiles against my skin like he's been waiting to hear those exact words.)"
    show dad smirk at right_small
    dad_says "Good girl. My perfect little submissive daughter. That's what I wanted to hear."
    show madd relieved at left_small
    with dissolve
    x "(His smile stays pressed against my cheek while he speaks. I can feel how pleased he is. How proud. It makes something dark and warm twist inside my chest.)"
    x "(My mind was broken beyond repair. Any thought that came in my mind was twisted by the filth that had been poured into it all night and my mouth would immediately put it into words without me even realizing it. )"
    x "I..I can smell your cum all the way up here, dad..."
    x " It smells so good..."    
    show dad possessive at right_small
    dad_says "That's because your body is molded to love everything about me now. Even the smell of my cum inside you."
    show dad dominant at right_small
    dad_says "Breathe it in. Get used to it. This is what you smell like now. This is what home smells like."
    x "(I stay quiet, just breathing through my nose while his cum keeps slowly dripping out of me. His cheek is still pressed to mine, his dick still buried to the hilt, and I can feel that twisted sense of rightness settling deeper. This is my new normal. This is what I chose.)"

    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_19
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small
    with dissolve
    x "(He's slowed down now. Just slow, deep thrusts while he stays buried inside me.)"
    show dad debased at right_small
    dad_says "My ass is so sweaty from fucking you all night... I hate showering after this. Feels like a waste."
    show dad perverted at right_small
    dad_says "You wanna lick the sweat off daddy's ass? Save me the trouble."
    show dad mocking at right_small
    dad_says " That's what good daughters do, right? Clean up after their dad."
    x "(My face is still pressed against his cheek. I can feel how serious he is. My body is exhausted, my pussy is still stuffed full and leaking, but the thought of putting my tongue on his sweaty ass makes something sick twist inside me.)"
    x "I... I'd love to, dad... but I'm too tired right now."
    x "Tomorrow though. I promise. I...I'll even take an energy drink if I have to."
    x " I'll lick all the sweat off your ass for you."
    show dad smirk at right_small
    dad_says "Heh, I can tell  you're excited about that. You really wanna put your tongue on daddy's sweaty ass, huh? "
    x "(I feel my face get hot against his cheek. My voice comes out small and shy, but the words are already leaving my mouth before I can stop them.)"
    x "Y...yes, dad. If your cum inside me can comfort me this much..."
    x "I wanna know how much comfort my tongue would feel inside your asshole. I can already tell how warm it would be having my tongue inside your sweaty, stinky ass. "
    show dad tongueout laugh at right_small
    dad_says "Stinky, huh? You love dad's stinky ass, don't you? "
    x "Mmhmm... I do...dad."
    show dad smirk at right_small
    dad_says "Fuck... you're really gone, aren't you? My perfect little ass licking daughter."
    x "(I don't answer. I just stay pressed against his cheek, breathing in the smell of his sweat and cum feeling so satisfied tomorrow i get to experience more of his filth. )"

    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_20
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small
    with dissolve
    show dad dominant at right_small
    dad_says "Okay fine.  Tomorrow you better lick my ass clean inside and out. But since you postponed daddy's plan for tonight we're sleeping like this. My dick stays buried inside you all night. No pulling out."    
    x "(The second he says it my legs move on their own. They wrap around his waist and lock behind his back, pulling him even deeper into me.)"
    show dad smirk at right_small
    dad_says "Look at you... wrapping those legs around me already. You really wanna sleep with daddy's dick plugged inside you all night, huh? Gonna wake up in a big pool of my cum."
    x "(I feel my face burn against his cheek but I don't let go. My legs stay locked tight around him. The thought of sleeping like this makes something warm and sick spread through my chest.)"
    show madd hopeful at left_small
    with dissolve
    x "(I'm happy. Actually happy. The idea of waking up sticky and full of him, the sheets ruined with his cum, my body still plugged by his dick... it feels right. Like this is exactly how I should be sleeping from now on.)"
    x "(Despite the fact i know I am gonna wake up with a sore pussy and a ruined bed and my legs probably won't even work in the morning, I am still excited for it. )"

    scene scene_sleep_next_to_dad_night_vaginal_clothes_off_21
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small
    with dissolve
    x "(He finally stops thrusting. Just stays buried deep inside me, keeping everything plugged and sealed.)"
    x "Dad...I dont think i can go back to sleeping anywhere else now. "
    x "You...you were right."
    show dad authoritative at right_small
    dad_says "Of course I was. I always am. "
    x "(His voice is calm and final against my ear. I feel my chest tighten in the best and worst way.  There's no going back from what we just did . Not after tonight. Not after everything I've said and done and let him do to me.)"    
    x "If we ever get married... can I still call you dad? "
    show madd hopeful at left_small
    with dissolve
    x " To the outside world we can be husband and wife... but I still want to be your daughter. I want to keep calling you dad."
    show dad perverted at right_small
    dad_says "I prefer it that way. Something so twisted about marrying a daughter I fucking love it."
    show dad possessive at right_small
    dad_says " Even if we get married, you'll still be calling me dad when I'm inside you."
    show madd happy at left_small
    with dissolve
    x "(I feel a wide, stupid smile spread across my face.)"
    x "(If you remove the impossible, whatever remains no matter how improbably is the truth)"
    x "(This was my truth, i loved my dad , i loved how good he feels inside me , how his rough treatment turn me on , how his stink is comforting to me , how his cum is the best thing i ever tasted and how his filth is the only thing that can fill the hole in my heart that was left by my mom's death. )"
    x "(I close my eyes, still smiling against his cheek, and let myself fall asleep like this — legs locked around him, his warmth filling me, knowing this is exactly where I belong.)"

    $ character_relations["dad"]["lust"] = 0
    $ character_relations["dad"]["anger"] = 0 
    $ character_relations["dad"]["dominance"] = min(character_relations["dad"]["dominance"] + 10, 100)
    $ character_relations["dad"]["intimacy"] += 11
    $ character_relations["dad"]["vaginal_sex"] += 1
    $ character_relations["dad"]["vaginal_creampie"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["kissed"] += 1
    $ character_relations["dad"]["identity"] = max(character_relations["dad"]["identity"] - 15, 0)
    $ journal_event_set_done("Dad", "Sleep With Dad: Vaginal Night")

    jump madd_wake_up_after_roughed_up_4


# Drag to room events 


label home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room:
    $ brother_lets_dad_abuse_madd =False 
    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_scene
    with dissolve
    
    show madd horrified at left_small
    with dissolve
    x "(To my horror, my dad dragged me into his room, but before he could shut the door my stepbrother barged in and joined us.)"
    show madd paralyzed at left_small
    x "(Now the three of us were in the room and I was so scared and confused about what was going to happen next...)"
    show madd hopeful at left_small
    x "(I was looking at my stepbrother with hope, with pleading eyes, hoping that he would protect me from my dad...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_dad_starts_dragging_madd_to_bed
    with dissolve
    show dad dominant at right_small
    with dissolve
    dad_says "Come on, Maddie... time to play your role."
    show madd distressed at left_small
    x "(My dad started dragging me to his bed and my stepbrother just stood there.)"
    show madd hesitant at left_small
    x "(Finally I got the courage to look at my stepbrother and say...)"
    x "Please... stop this."
    hide dad
    show brother shocked at right_small
    with dissolve
    brother_says "What's going on here?? Why are you dragging Maddie to your bed??"
    show madd trembling at left_small
    x "(He dragged me a few more steps and then...)"

    if character_relations["brother"]["lust"]< 30 and character_relations["brother"]["friend"] >=20:
        scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_brother_stands_up_to_dad
        with dissolve
        show dad angry at right_small
        with dissolve
        dad_says "You stay out of this!! This is between me and my daughter!!"
        show madd weeping at left_small
        x "(At this point tears were streaming down my face and I was begging my stepbrother.)"
        x "Please... help."
        hide dad
        show brother serious at right_small
        x "(Suddenly my stepbrother's expression changed and he jumped in front of me, forcing dad to remove his hands from me and said...)"
        brother_says "Let her go!!"
        show madd relieved at left_small
        x "(He stood there blocking my dad from getting to me...)"
        x "(I stood behind my stepbrother, hoping he would protect me...)"
        x "Thank you!!"
        show madd anxious at left_small
        x "(I was too scared to say anything else or look at my dad...)"
        x "(I just heard him say in a very angry voice...)"
        hide brother
        show dad angry at right_small
        dad_says "You will pay for this..."
        hide dad
        show brother amused at right_small
        brother_says "Yeah, like I care."
        show madd relieved at left_small
        x "(With that, my stepbrother put his arm around me and we left the room together... He left me in the living room and went to his own room...)"
        x "(I was surprised he didn't try anything with me... maybe he is not as bad as I thought...)"
        $ character_relations["brother"]["friend"] += 10
        $ brother_protects_madd_from_dad +=1
        jump home_areas
    if character_relations["brother"]["lust"]< 50 and (character_relations["brother"]["vaginal_sex"]+character_relations["brother"]["anal_sex"]+character_relations["brother"]["oral_sex"]<3) :
        scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_brother_gives_up_and_leave
        with dissolve
        show dad angry at right_small
        with dissolve
        dad_says "You stay out of this!! This is between me and my daughter!!"
        show madd weeping at left_small
        x "(At this point tears were streaming down my face and I was begging my stepbrother.)"
        x "Please... help."
        hide dad
        show brother serious at right_small
        show madd shocked at left_small
        x "(Suddenly my stepbrother's expression changed and he looked at me with a blank expression, not saying a word, he was looking down on the floor. I knew what that meant )"
        show madd horrified at left_small
        x "(He was gonna abandon me here..)"
        show madd weeping at left_small
        brother_says "I..I'm sorry Maddie."
        hide brother
        show dad angry at right_small
        show madd distressed at left_small
        x "(right after saying that he started to walk out and at the same time dad pulls me roughly in his arms)"
        show madd trembling at left_small
        x "(i was left alone...alone with him)"
        show madd traumatized at left_small
        x "(I heard the sound of the door closing and i knew my fate was sealed)"
        dad_says "You Fucked up Maddie!! "
        show madd distressed at left_small
        x "(At this point he was holding me tightly and I was struggling to get out of his grip but it was no use)"
        dad_says "Stupid Girl !!"
        $ brother_lets_dad_abuse_madd=True
        jump home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room


    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_brother_lets_dad_drag_madd_to_bed_and_joins_in
    with dissolve
    show dad controlling at right_small
    with dissolve
    dad_says "You stay out of this!! This is between me and my daughter!!"
    show madd hopeful at left_small
    x "(I looked at my stepbrother with pleading eyes, hoping he would protect me, and begged...)"
    x "Please... help."
    show madd horrified at left_small
    x "(To my horror, my stepbrother was staring at the floor, and when he opened his mouth I was dumbfounded by what he said.)"
    hide dad
    show brother calculating at right_small
    with dissolve
    brother_says "I actually want in, dad... I want to be part of this..."
    hide brother
    show dad smirk at right_small
    x "(Even dad was surprised and stared at him with shock and disbelief before saying...)"
    dad_says "Alright then... let's do it together... son..."
    show madd broken at left_small
    x "(After that, both of them started dragging me to the bed and made me sit between them.)"
 
    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_sitting_between_dad_and_brother_on_bed
    with dissolve
    show madd depressed at left_small
    with dissolve
    x "(I was sitting on the bed with my dad on one side and my stepbrother on the other...)"
    show madd self loathing at left_small
    x "(What a fool... I actually called for help and he wanted to join in...)"
    x "(God, I am such an idiot... men only have one thing on their mind...)"
    show dad smirk at right_small
    hide dad
    show brother smirk at right_small
    x "(They both had this sinister smile on their faces, looking at me like I was dessert...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_sitting_between_dad_and_brother_on_bed_2
    with dissolve
    show dad manipulative at right_small
    with dissolve
    x "(Suddenly dad leaned in closer to my face and said...)"
    dad_says "So... Maddie... you wanted his help, huh?"
    show madd uncertain at left_small
    x "(He then grabbed my hair and pulled it gently, continuing...)"
    show dad possessive at right_small
    dad_says "You thought he was going to help you??"
    show madd hesitant at left_small
    x "(Maybe apologizing is the best way to get out of this...)"
    x "I... I'm sorry, dad..."
    hide dad
    show brother condescending at right_small
    with dissolve
    brother_says "Yeah, don't you know you belong to us..."

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_sitting_between_dad_and_brother_on_bed_3
    with dissolve
    show dad dominant at right_small
    with dissolve
    x "(Suddenly dad pulled my hair again, forcing me to look at him, and said...)"
    dad_says "Tell me who you belong to."
    show madd resigned at left_small
    x "(There was a long pause and I had no way out of this... I had to give in to their demands...)"
    x "To you... I belong to you..."
    show dad sadistic at right_small
    x "(He didn't say anything, but then his face got closer to mine and he started licking my face.)"
    dad_says "You know, Maddie... I am saddened that I do so much for you and you still call for help."
    dad_says "It's like you aren't even loyal to me... My feet have become sore from all the work I do for you and you still call for help..."
    show madd disgusted at left_small
    x "(He continued licking my face.)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_sitting_between_dad_and_brother_on_bed_4
    with dissolve
    show dad coercive at right_small
    with dissolve
    x "(He finally pulled back and rested his feet on his knees right near me, and said...)"
    dad_says "Go on, show me your loyalty... kiss my feet..."
    show madd nauseated at left_small
    x "(I was so disgusted and humiliated, but I had no choice but to obey...)"
    x "(As soon as he placed his feet near me, the stench hit my nose — it was as if they had been sweating constantly.)"
    show madd submissive nod at left_small
    x "(I nodded my head and said...)"
    x "Yes... dad."
    show madd resigned at left_small
    x "(I lowered my head closer to his feet and said a few last words before kissing them.)"
    x "As you command."
    show madd disgusted at left_small
    x "(I took a deep breath, the stench filling my lungs, and then I took his big toe into my mouth completely.)"
    x "(I was using my tongue to lick the odor off his foot, trying to hold back my gag reflex, but it was so hard...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_kissing_dads_feet_2
    with dissolve
    show madd weeping at left_small
    with dissolve
    x "(At this point I was so humiliated and disgusted that tears were streaming down my face, but I didn't say a word...)"
    show dad sadistic at right_small
    x "(He finally let go of my head, giving me the chance to continue on my own.)"
    dad_says "Lick it clean now..."
    show madd nauseated at left_small
    x "(I was holding his foot with both hands and using my tongue to lick the gaps between his toes.)"
    x "(It was the most disgusting thing I had ever done in my life...)"
    x "(In my life... yet... I didn't know what else they would make me do...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_kissing_dads_feet_3
    with dissolve
    show madd resigned at left_small
    with dissolve
    x "(I pressed my tongue along his sole in slow, dragging strokes, trying to prove my submission with each pass...)"
    show brother mocking at right_small
    x "(The whole time I could feel their eyes on me...)"
    show madd traumatized at left_small
    x "(I had been licking his feet for a while now — I wanted to stop, but I couldn't stop until he said so...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_kissing_dads_feet_4
    with dissolve
    show dad dominant at right_small
    with dissolve
    x "(He started forcing his hand on the back of my head, making me take more of his toes into my mouth...)"
    show madd traumatized at left_small
    x "(I continued to do as told — humiliation and disgust filled every part of my body.)"
    hide dad
    show brother sadistic at right_small
    with dissolve
    brother_says "Hahaha, look at her... cleaning your foot, dad!"
    brother_says "Like a dog..."
    show madd self loathing at left_small
    x "(They were both mocking me while I was doing this...)"
    x "(I wanted to die at this point... why did I call for help?? I should have just endured the night...)"
    show madd resigned at left_small
    x "(It had been so long since I started licking his feet that my body had grown accustomed to the stench and the taste...)"
    x "(Now I wasn't so disgusted anymore... I was just doing what I had to do to survive...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_kissing_dads_feet_5
    with dissolve
    show madd resigned at left_small
    with dissolve
    x "(By now I had given up any thought of stopping — I lavished each toe with attention, my tongue working diligently, hoping to satisfy him...)"
    show dad smirk at right_small
    x "(Finally he pulled my head away from his feet and asked...)"
    dad_says "So... Maddie, how did it taste??"
    show madd broken at left_small
    x "(I had to give a positive answer...)"
    x "It tasted good... dad."
    x "I would love to clean them for you again..."
    show madd weeping at left_small
    x "(Tears streamed down my face as I betrayed myself by saying this...)"
    show dad laugh at right_small
    hide dad
    show brother laugh at right_small
    x "(They both burst out laughing at my answer...)"
    x "(They were laughing at how pathetic I am... how quickly I gave in to their demands... how easily I was broken...)"
    show madd traumatized at left_small
    x "(Finally he put his feet down and his face moved closer to mine — I knew he was going in for a kiss.)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_dad_kissing_madd_on_lips_full_scene
    with dissolve
    show dad lustful at right_small
    show madd broken at left_small
    with dissolve
    x "(He turned my head and kissed me on the lips...)"
    x "(Whatever dignity I had left was completely erased — the stench of his feet and taste of his toes still lingered in my mouth...)"
    x "(He started moving his tongue inside my mouth and I offered no resistance...)"
    hide dad
    show brother possessive at right_small
    with dissolve
    x "(I felt another hand on my head — I knew it was my stepbrother's. He was pushing me toward my dad's face, making the kiss more intense...)"
    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_dad_kissing_madd_on_lips_full_scene_1_1
    with dissolve
    show dad dominant at right_small
    show madd paralyzed at left_small
    with dissolve
    x "(Dad roughly pulled my whole body and made me sit on his lap while still kissing me...)"
    x "(I felt movement behind me — my stepbrother had moved closer.)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_dad_kissing_madd_on_lips_full_scene_1_2
    with dissolve
    show brother lustful at right_small
    show madd overwhelmed at left_small
    with dissolve
    x "(While dad continued assaulting me with his tongue, I felt my stepbrother's tongue brush my hair aside and begin licking my neck...)"
    x "(Now I was trapped between them, each one claiming a different part of me with his mouth...)"
    x "(The lust in their eyes was so intense, the heat their bodies gave off... I was in the middle of all that heat...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_dad_kissing_madd_on_lips_full_scene_2
    with dissolve
    show madd broken at left_small
    with dissolve
    x "(At this point I was completely broken. I had no dignity left... I was just a toy for them to use and abuse as they pleased...)"
    show dad lecherous at right_small
    x "(They were so consumed by lust that their saliva was dripping all over me without restraint — coating my face, neck, and chest with their mess...)"
    x "(Dad's spit ran in a warm trail down from my cheek to my jaw while strings of my stepbrother's saliva dripped down the side of my neck...)"
    show madd disgusted at left_small
    x "(As if the stench and taste of his feet weren't bad enough, now both of their saliva was smeared all over me, the wet smell of it mixing with the stench still on my tongue...)"
    show madd conflicted at left_small
    x "(At first I hated the smell, but now that all I could smell was their saliva and the stench of dad's feet, I was getting used to it...)"
    x "(God, why am I starting to enjoy this?? I'm so disgusted with myself... Why do I want to go back to smelling his feet and tasting his toes??)"
    show dad lustful at right_small
    x "(Finally they let me sit on the bed again, but his lips found mine once more.)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_dad_kissing_madd_on_lips
    with dissolve
    show dad lustful at right_small
    show madd resigned at left_small
    with dissolve
    x "(Dad continued kissing me on the lips — I knew there was no escape from this...)"
    show madd processing at left_small
    x "(At least my stepbrother wasn't licking me... for now...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_dad_kissing_madd_on_lips_2
    with dissolve
    show brother leering at right_small
    show madd horrified at left_small
    with dissolve
    x "(My God, I was so wrong... I felt a hand on my thigh and I knew it was my stepbrother's...)"
    x "(It was so close and personal... I could feel his hand on my inner thigh...)"
    show madd self loathing at left_small
    x "(Why do I think they will ever stop?? I am so naive... I am so stupid...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_dad_kissing_madd_on_lips_3
    with dissolve
    show brother sadistic at right_small
    show madd distressed at left_small
    with dissolve
    x "(He started getting rougher with his approach.)"
    x "(He pinched my upper thigh and started shaking it a little bit...)"
    x "(Just to avoid the pain I shifted my hips to reduce the pressure...)"
    x "(This excited him even more and he started pinching harder and shaking it more...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_dad_kissing_madd_on_lips_4
    with dissolve
    show dad lustful at right_small
    show madd overwhelmed at left_small
    with dissolve
    x "(This whole time I was caught up in the pain below, while dad was passionately kissing me on the lips.)"
    hide dad
    show brother dominant at right_small
    x "(My stepbrother finally stopped pinching my thigh and began moving his hand up to my backside...)"
    x "(He started slapping it softly, like kneading dough... I could feel the sting building up from the repeated slaps...)"

    if madd_dp_finished:
        menu:
            "Choose spitroast instead":
                jump home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_scene
            "Continue with whatever they decide":
                pass


    if character_relations["brother"]["lust"]<= 60 and (character_relations["brother"]["anal_sex"]+character_relations["brother"]["vaginal_sex"]<=1):
        jump home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_scene


    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_dad_kissing_madd_on_lips_5
    with dissolve
    show dad dominant at right_small
    show madd paralyzed at left_small
    with dissolve
    x "(Finally he stopped and suddenly they both gripped my thighs, pulling me backwards and pinning me down on the bed...)"
    x "(My stepbrother started running his hands all over my body while dad continued kissing me on the lips...)"
    hide dad
    show brother lecherous at right_small
    x "(My stepbrother's face was right next to mine, so he took advantage and started licking my face too.)"
    hide brother
    show dad dominant at right_small
    x "(Dad's hand gripped my neck... as if to make it very clear he was in control of me...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_lying_on_bed_with_dad_and_brother
    with dissolve
    show madd horrified at left_small
    with dissolve
    x "(Oh no... I am lying in bed with my dad and stepbrother on each side of me...)"
    show madd paralyzed at left_small
    x "(This is terrible... this is really, truly bad...)"
    x "(Both of their faces were right next to mine...)"
    show madd overwhelmed at left_small
    x "(I felt hands over my stomach... over my neck... over my crotch... I couldn't tell whose was whose...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_lying_on_bed_with_dad_and_brother_2
    with dissolve
    show dad lecherous at right_small
    show madd disgusted at left_small
    with dissolve
    x "(Their mouths were on me again, drooling all over me without shame — their spit soaking into my skin from both sides...)"
    x "(Dad's tongue pressed straight past my lips... my stepbrother's mouth dragged slowly down the side of my throat...)"
    show madd conflicted at left_small
    x "(I was tasting dad on my tongue while feeling the damp heat of my stepbrother's breath crawling down my neck...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_lying_on_bed_with_dad_and_brother_3
    with dissolve
    show madd resigned at left_small
    with dissolve
    x "(They kept groping and squeezing every part of me while their tongues left wet trails of saliva wherever they could reach...)"
    show madd traumatized at left_small
    x "(Four fingers dug into my tits simultaneously, rough and possessive, kneading without care...)"
    x "(I was like livestock being handled by two farmers...)"
    x "(If I stayed in this house, I knew this was going to be my life...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_lying_on_bed_with_dad_and_brother_4
    with dissolve
    show brother lustful at right_small
    hide brother
    show dad lustful at right_small
    show madd overwhelmed at left_small
    with dissolve
    x "(My stepbrother slid his hands from my collarbone down to my breasts while dad simultaneously lowered my shirt below them.)"
    x "(My tits were now completely bare and both of them started squeezing and groping them harder than before, fingers digging in...)"
    x "(My shirt was bunched just below my chest, covering the rest of my body...)"
    show madd traumatized at left_small
    x "(Their tongues kept lapping at my face and neck, coating me with spit, while their hands stayed locked on my tits and kept squeezing...)"


    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_lying_on_bed_with_dad_and_brother_5
    with dissolve
    show madd conflicted at left_small
    with dissolve
    x "(They finally stopped playing with my breasts and stopped kissing too.)"
    x "(Just when I thought they were going to stop, they lowered their heads back to my breasts and started licking them through my shirt...)"
    x "(They kept kissing and biting softly while licking...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_lying_on_bed_with_dad_and_brother_5_2
    with dissolve
    show dad sadistic at right_small
    hide dad
    show brother sadistic at right_small
    show madd flustered at left_small
    with dissolve
    x "(Suddenly they got much rougher with it...)"
    x "(They used their hands to grope and squeeze my breasts while biting and licking more and more passionately...)"
    show madd conflicted at left_small
    x "(At this point I was mesmerized by the dominance they had over me... I was giving in to their desires more and more...)"
    x "(The smell of their saliva and the stench of dad's feet had rewired my brain to associate them with pleasure...)"
    show madd blush at left_small
    x "(I was actually enjoying this... I was softly moaning while they licked and bit my breasts...)"
    hide brother
    show dad laugh at right_small
    dad_says "Hear that?? I think our little Maddie is enjoying this..."
    hide dad
    show brother amused at right_small
    brother_says "Yeah, dad, hear those soft moans... she loves being treated like this..."
    show madd deep blush at left_small
    x "(Their laughter filled the room while I lay there unable to stifle my own moans — they knew exactly what they were doing to me...)"
    hide brother
    show dad lustful at right_small
    dad_says "Let's give her more pleasure then... before we cum inside her slutty body..."
    show madd conflicted at left_small
    x "(They were going to finish inside me?? I'm completely done for — usually I would be terrified, but now I was actually getting turned on by the thought...)"
    x "(Why am I reacting like this?? Why does the thought of them finishing inside me at the same time turn me on??)"
    show madd flustered at left_small
    x "(They finally stopped teasing my breasts and started kissing me on the lips again...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_dad_kissing_madd_on_lips_6
    with dissolve
    show dad horny at right_small
    show madd conflicted at left_small
    with dissolve
    x "(Slowly their hands moved to my shorts and they started rubbing me through the fabric...)"
    x "(It was slow and sensual, letting me adjust to the feeling...)"
    dad_says "Feel how wet the fabric is getting from her arousal..."
    dad_says "She is like a bitch  in heat..."
    show madd blush at left_small
    x "(I should have recoiled, but every stroke of their hands sent warmth bleeding through my skin that I couldn't fight...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_dad_kissing_madd_on_lips_7
    with dissolve
    show brother horny at right_small
    show madd deep blush at left_small
    with dissolve
    x "(They pulled their hands away for only a moment, then resumed — this time harder and faster...)"
    x "(Parts of their hands slipped under my shorts and they were rubbing my bare skin directly...)"
    x "(Their hot hands on my bare skin were sending shivers down my spine...)"
    show madd conflicted at left_small
    x "(If they weren't related to me, I would have told them right there to just take me...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_dad_kissing_madd_on_lips_8
    with dissolve
    show dad dominant at right_small
    show madd overwhelmed at left_small
    with dissolve
    x "(Finally they stopped and their hands moved back up to my breasts...)"
    dad_says "Tonight is going to be a very long night for you, Maddie..."
    x "(He said this while groping my breasts and kissing my lips.)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_dad_kissing_madd_on_lips_9
    with dissolve
    show brother dominant at right_small
    show madd flustered at left_small
    with dissolve
    brother_says "Yeah... you don't get to sleep tonight..."
    show madd conflicted at left_small
    x "(Why does that threat send heat straight to my stomach?? What has happened to me...)"
    hide brother
    show dad sadistic at right_small
    dad_says "I'm going to take her pussy... Adam, you can have her asshole..."
    show madd horrified at left_small
    x "(What?? Did he really just say that?? Having both of them inside me at the same time??)"
    x "(How am I ever going to survive this?? And even if I do, what if I start to like it... how do I ever go back after that?)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_dad_kissing_madd_on_lips_10
    with dissolve
    show dad lustful at right_small
    hide dad
    show brother lustful at right_small
    show madd paralyzed at left_small
    with dissolve
    x "(They both kissed me one last time before reaching under my thighs and lifting me.)"
    x "(Dad lay back and I was pushed on top of him while my stepbrother pressed his weight onto me from behind...)"
    x "(I was perfectly sandwiched between them...)"


    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_sandwiched_between_dad_and_brother_on_bed
    with dissolve
    show madd traumatized at left_small
    with dissolve
    x "(I knew what was going to happen... dad was going to penetrate me from the front and my stepbrother from the back...)"
    show madd conflicted at left_small
    x "(Surprisingly, I was getting more and more turned on by the thought of them taking me at the same time...)"
    show madd blush at left_small
    x "(For now they were slowly kissing me while touching my body gently.)"


    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_sandwiched_between_dad_and_brother_on_bed_2
    with dissolve
    show dad horny at right_small
    show madd overwhelmed at left_small
    with dissolve
    x "(They picked up the pace — dad started kissing me more passionately while my stepbrother licked my neck more intensely...)"
    x "(I could feel both of them growing harder against my body...)"
    show madd flustered at left_small
    x "(I was trapped between them, both of them in complete control of me... their warmth surrounding me from all sides...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_sandwiched_between_dad_and_brother_on_bed_3
    with dissolve
    show dad dominant at right_small
    hide dad
    show brother dominant at right_small
    show madd overwhelmed at left_small
    with dissolve
    x "(Suddenly they became much more aggressive with their kissing and touching...)"
    x "(They were handling my body like animals in heat...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_sandwiched_between_dad_and_brother_on_bed_4
    with dissolve
    show brother horny at right_small
    show madd flustered at left_small
    with dissolve
    x "(I felt someone's hand reach for my shorts again and begin rubbing my backside...)"
    x "(Their rubbing was gradually exposing more of my bare skin — cold air hitting my exposed skin sent shivers down my spine...)"
    
    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_sandwiched_between_dad_and_brother_on_bed_5
    with dissolve
    show dad lustful at right_small
    show madd deep blush at left_small
    with dissolve
    x "(They slowed down again...)"
    x "(But this time his hands didn't leave my backside, while another hand moved to my breasts and started squeezing them...)"
    show madd conflicted at left_small
    x "(I was so lost in the feeling... every time their hands pressed deeper into my bare skin I could feel how wet and ready my body was for them...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_sandwiched_between_dad_and_brother_on_bed_6
    with dissolve
    show dad horny at right_small
    hide dad
    show brother horny at right_small
    show madd inheat at left_small
    with dissolve
    x "(It was dad's hand on my breasts and my stepbrother's hand on my backside...)"
    x "(Dad was squeezing and kneading my breasts as if they were clay...)"
    x "(My stepbrother was slapping and pinching my backside as if it were his own...)"
    show madd deep blush at left_small
    x "(My body was ready for them... I was so aroused I was practically begging them to take me...)"
    hide brother
    show dad dominant at right_small
    dad_says "Alright Maddie... time for the real treat."
    show madd paralyzed at left_small
    x "(They started removing my shorts, exposing me completely to them...)"

    if character_relations["dad"]["intimacy"]<80:
        if madd_is_virgin and last_madd_drugged_day<0:
            if character_relations["dad"]["vaginal_sex"]<1 and madd_is_virgin: 
                x "(NO NO no , i am still a virgin... I can't let them do this to me... )"
                x "Please stop this! Please don't do this to me!"
                show madd horrified at left_small
                dad_says "Shut up, Maddie... you are going to enjoy this whether you like it or not..."
                show madd conflicted at left_small
                x "(I have to be tough on them, I have to let them know the consequences..."
                x "Once i get out I will call the cops if you dont let me leave"
                if dad_knows_madd_stole_crypto or dad_knows_madd_drugs_food:
                    x "(to my surprise dad looked at me with a blank expression for a moment, then he started laughing)"
                    dad_says "Go on, call the cops, see if they will do anything to me"
                    x "(Huh, why is he laughing? Does he think the cops will do nothing to him? Or does he just not care?)"
                    if dad_knows_madd_stole_crypto:
                        dad_says "I will just tell them how you stole my crypto and they will throw you in jail for a long time"
                    if dad_knows_madd_drugs_food:
                        dad_says "I will tell them how you drug our food making us all sick and they will throw you in jail for a long time"
                    x "(I was shocked, i had no idea that he knew about those things, but it explained why he was laughing)"
                    x "(He had all the cards in his hand, he could easily get me arrested and thrown in jail, and he knew it)"
                    x "(I have no choice but to comply with his demands, i have to let fuck me raw ...its all over if i end up in jail)"
                else :
                    dad_says "Fucking mood killer , Just wait till i catch some dirt on you and then i will make you scream for me"
                    x "(Surprisingly brother got off of me and stood up , i got off of dad and they both looked at me with a dead expression)"
                    x "(This is gonna make them so mad...)"
                    x "(I hurried up outside to the main lobby..)"
                    $ character_relations["dad"]["intimacy"] +=7
                    $ character_relations["brother"]["intimacy"] +=7
                    jump home_areas        
        elif madd_is_virgin and last_madd_drugged_day>0:
            x "(I feel the effects of drugs still affecting me ...my mind and body both want to continue this..."
            x "(No no...i shouldnt be losing my virginity like this)"
            x "(What kind of whore loses her virginity in a double penetration, but i cant stop it. I shouldnt have mixed those drugs in...)"
            x "(I am sorry mom i am taking both your step son and your husband inside me at the same time and this is my first time having a dick inside my vagina.)"
            x "(These drugs are making me so excited i cant refuse anyone..)"



    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_sandwiched_naked 
    with dissolve
    show madd traumatized at left_small
    with dissolve
    x "(I was lying exposed on the bed between my dad and stepbrother...)"
    show madd broken at left_small
    x "(Although my words wanted to say no, my body was betraying me and inviting them in...)"
    x "(My stepbrother's hand was on my ass and dad's hand was on my back, holding me down... this night would only end when they were both done with me...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_sandwiched_naked_2
    with dissolve
    show dad lustful at right_small
    show madd horrified at left_small
    with dissolve
    x "(Dad slowly removed his jeans and underwear, revealing his big dick...)"
    x "(I couldn't see it but I could feel it pressing against me... the hardness, the heat....)"
    show dad dominant at right_small
    dad_says "I am going to enjoy this so much... Maddie..."
    dad_says "You will not be able to say no to me after tonight..."
    show madd horrified at left_small
    x "(I was in a state of panic but massively turned on at the same time...)"
    show dad sadistic at right_small
    dad_says "Now... I am going to insert it in your tight little pussy, Maddie..."
    hide dad
    show brother horny at right_small
    with dissolve
    brother_says "Wait... dad... I want to put mine in her asshole too... let's do it at the same time..."
    hide brother
    show dad dominant at right_small
    dad_says "I'm not waiting for anyone..."
    show madd paralyzed at left_small
    x "(Dad didn't wait for him or for me — he just started penetrating me...)"
    if madd_is_virgin:
        x "(He didnt care if i was a virgin, i knew my purity ends tonight but i didnt expect it to end in such a brutal manner)"
        x "(Being double penetrated by them is how i lose my virginity , thats just sick...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_being_penetrated_by_dad_brother_just_got_naked
    with dissolve
    show madd overwhelmed at left_small
    with dissolve
    x "(I felt him stretching me open...)"
    if madd_is_virgin:
        x "( I felt a wave of pain hit my body as his dick stretched my hymen, I knew my virginity was lost at that moment but I didnt expect it to be so painful and brutal...)"
        x "(Once he broke my hymen, I felt a wave of pleasure hit my body as he reached deeper inside me... I couldn't help but release a soft moan...)"
        x "(Its over, my virginity is lost, but at least i can say that it was my dad who took it, i just wish it was in a better way...)"
        x "(Losing my virginity to the guy my mom married...for sure i will not be seeing the pearly gates)"
        $ madd_is_virgin=False

    show madd flustered at left_small
    x "(A wave of pleasure hit my body as he reached deeper inside me... I couldn't help but release a soft moan...)"
    show brother lecherous at right_small
    with dissolve
    brother_says "Whatever, dad... I'm ready too..."
    show madd horrified at left_small
    x "(That's when I felt another pressure against me from behind — by the weight and heat I could tell he was ready to enter as well...)"
    show madd conflicted at left_small
    x "(But I was too focused on what was already happening to me from the front.)"
    x "(God, that felt so good... the fact that my body was accommodating dad without my consent was making me feel completely helpless.)"
    hide brother
    show dad dominant at right_small
    dad_says "That's it, Maddie... take it all in..."
    show madd deep blush at left_small
    x "(With that he drove himself deeper and the sounds escaped my lips before I could catch them...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_being_penetrated_by_dad_and_brother_1
    with dissolve
    show brother dominant at right_small
    show madd horrified at left_small
    with dissolve
    x "(Finally my stepbrother had enough waiting and began entering me from behind...)"
    x "(...)"
    x "(What is this sensation?? I have never felt anything like this before...)"
    show madd overwhelmed at left_small
    x "(Being taken by both of them at the same time was sending waves of pleasure and pain all over my body...)"
    show brother sadistic at right_small
    brother_says "Wow... she is so tight..."
    show madd paralyzed at left_small
    x "(The sheer pressure of them both filling me at once left me completely unable to shift my body...)"
    x "(Both of them were moving at the same time and my body was struggling to adjust to them both.)"
    x "(Both of them were pulsing against me from within — I could feel them swelling and pressing harder with every thrust...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_being_penetrated_by_dad_and_brother_2
    with dissolve
    show dad sadistic at right_small
    show madd inheat at left_small
    with dissolve
    x "(Now they were relentless, showing no mercy at all...)"
    x "(As if I was just an object to them.)"
    show dad mocking at right_small
    dad_says "You feel even tighter when both are filled up... hahaha."
    dad_says "You might say no, but I can feel how wet you are... how your body is gripping me..."
    show madd overwhelmed at left_small
    x "(I was in so much pleasure and pain at the same time that I was moaning uncontrollably...)"
    show madd conflicted at left_small
    x "(I no longer cared what they thought of me... whether they laughed at me or not...)"
    x "(I knew that if I moaned louder they would take it as an open invitation to do this whenever they wanted, here or anywhere else... but I couldn't hold back...)"
    show madd inheat at left_small
    x "(The room was silent except for the sound of my moans and the sound of their balls clapping against my ass...)"
    x "(God, I was loving this feeling... the smell of his feet and taste of his toes still lingering in my mouth... the feeling of their saliva on my skin... the feeling of both of their cocks inside me ...)"
    show madd conflicted at left_small
    x "(I knew I would become their devoted slave if I climaxed from this... and at this moment I wouldn't mind that at all... I might even welcome it...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_being_penetrated_by_dad_and_brother_3
    with dissolve
    show dad horny at right_small
    show madd deep blush at left_small
    with dissolve
    x "(As they were moving, I caught a glimpse of dad's face and saw pure lust — he was staring at my body like it was the most intoxicating thing he had ever seen...)"
    show dad lustful at right_small
    x "(His face no longer held that dominant, calculating look — now it was the face of someone completely lost in desire...)"
    show madd conflicted at left_small
    x "(For the moment, I was just glad to be the object of their complete attention...)"
    x "(Then I felt it... something building inside me...)"
    show madd overwhelmed at left_small
    x "(I knew I was going to climax from this... I was so close to the edge...)"
    show madd horrified at left_small
    x "(No... no... if they see me climax they will take it as proof that I love being used like this and they will never let me go...)"
    x "(I don't want to be their personal thing they take whenever they want... I can't...)"
    show madd traumatized at left_small
    x "(No... please... I'm not ready to be their slave yet... but it's getting closer...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_being_penetrated_by_dad_and_brother_4
    with dissolve
    show madd salivating at left_small
    with dissolve
    x "(I couldn't hold it in anymore... with louder moans than ever before I climaxed from the pleasure of being taken by both of them at the same time...)"
    x "(The release was so powerful that it was spraying in every direction...)"
    x "(Since it was partially blocked, it was spraying out unevenly all over the bed...)"
    show dad laugh at right_small
    hide dad
    show brother laugh at right_small
    x "(I had released so much that they both burst out laughing...)"
    dad_says "Look at that... our little Maddie is squirting from our pounding..."
    brother_says "Hahaha, she is loving this so much... look at her squirting like a fountain..."
    dad_says "Just like a wild bitch wanting to get knotted"
    show madd broken at left_small
    x "(There was no going back from this... I was completely theirs now...)"
    x "(I had just lost all control in front of them both — I can never deny them anymore...)"
    hide brother
    show dad dominant at right_small
    dad_says "Okay Maddie... now it's my turn to finish inside you..."
    hide dad
    show brother horny at right_small
    brother_says "I am reaching my limit too... I'm going to finish inside her as well..."
    show madd horrified at left_small
    x "(They are both going to finish inside me??)"
    x "(At the same time??)"
    x "(How is my body ever going to handle all of that??)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_being_penetrated_by_dad_and_brother_5
    with dissolve
    show dad lustful at right_small
    show madd overwhelmed at left_small
    with dissolve
    x "(I could feel both their cocks throbbing desperately inside me — their thrusting turning erratic and urgent as they both got close to cumming...)"
    x "(Their breathing above me was ragged and broken, grunting with every thrust, their bodies going rigid...)"
    show madd conflicted at left_small
    x "(That's when I felt it... the first thick jets of dad's cum shooting deep inside my pussy... the hot liquid flooding my insides relentlessly...)"
    x "(And immediately after, my stepbrother unloaded inside my ass as well... his cum pouring into me from behind, mixing with the heat already flooding my pussy...)"
    show madd overwhelmed at left_small
    x "(I was completely stuffed with their cum from both holes at once... every part of me they had taken now flooded and dripping with their seed...)"
    x "(I could feel it starting to overflow and leak out of me...)"
    show madd salivating at left_small
    x "(What is this feeling?! I should be in agony but I am absolutely loving this...)"
    show dad sadistic at right_small
    dad_says "That's it, Maddie... take all of it..."
    show madd overwhelmed at left_small
    x "(They kept moving while still releasing... how long would this last?)"
    x "(The sounds in the room changed — now just wet, rhythmic sounds.)"
    x "(I still couldn't move... I was being flooded with warm fluid inside... as it leaked out of me it made soft, wet sounds...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_being_penetrated_by_dad_and_brother_6
    with dissolve
    show madd salivating at left_small
    with dissolve
    x "(I was so completely overwhelmed that sounds poured out of me uncontrollably, and I dimly became aware that I was drooling...)"
    x "(The fluid leaking from behind was mixing with the fluid from the front and both overflowed out of me...)"
    show madd broken at left_small
    x "(There was simply no more room — my body was overflowing, unable to contain what they had poured into me...)"
    show dad smirk at right_small
    dad_says "That felt incredible... you are such a good girl, Maddie..."
    x "(They were still moving but now slowing their pace...)"
    show dad possessive at right_small
    dad_says "Hopefully I've filled you up and you become pregnant from this..."
    hide dad
    show brother angry at right_small
    with dissolve
    x "(I heard an angry grunt from my stepbrother — I knew he wanted to be the one to impregnate me, but he couldn't say anything because dad was in control...)"
    hide brother
    show dad dominant at right_small
    dad_says "You will be a good mother to my children... and if it's a boy..."
    x "(Now his tone became more serious and dominant...)"
    dad_says "I will raise him to be as dominant as me and once he comes of age he fuck you just like I do and you wont have a say in the matter... you will be creating generations of my bloodline..."
    show madd conflicted at left_small
    x "(I was in so much pleasure that I was actually savoring the thought of being used as a vessel for their future generations...)"
    show madd broken at left_small
    x "(I was so exhausted at this point... I just wanted to sleep. As they slowed down and finally stopped, my body went completely limp.)"
    show madd traumatized at left_small
    x "(I felt my stepbrother pull out from behind and dad pull out from the front... as they both left my body I felt a wave of emptiness and a flood of warmth rush out of me...)"
    x "(They had been holding everything inside me and now it was all coming out at once...)"
    x "I... fill me up again..."
    x "(My eyes closed as I drifted off to sleep.)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_lying_on_bed_with_dad_and_brother_7
    with dissolve
    show dad mocking at right_small
    with dissolve
    dad_says "Damn girl... fell asleep. I wanted her to clean everything up."
    hide dad
    show brother amused at right_small
    with dissolve
    brother_says "There is always next time... Now we know how much she loves it..."
    hide brother
    show dad laugh at right_small
    dad_says "Yeah... let her sleep on top of me... I'm tired too..."
    x "(They were both talking about me while I was sleeping on top of dad...)"
    x "(I was so exhausted that I didn't even care what they were saying...)"
    show dad dominant at right_small
    dad_says "Turn off the lights when you leave the room..."
    x "(The last thing I heard before I finally fell asleep was the sound of a zipper closing and the door shutting...)"

    # ── DAD stats: vaginal sex + vaginal creampie + DP scene (Tier 6-7) ──────────
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["kissed"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["vaginal_sex"] += 1
    $ character_relations["dad"]["vaginal_creampie"] += 1
    $ character_relations["dad"]["intimacy"] += 11
    $ character_relations["dad"]["lust"] = 0
    $ character_relations["dad"]["dominance"] = min(character_relations["dad"]["dominance"] + 10, 100)
    $ character_relations["dad"]["anger"]=0
    # ── BROTHER stats: anal sex + anal creampie + DP scene (Tier 5-7) ────────────
    $ character_relations["brother"]["groped_madd"] += 1
    $ character_relations["brother"]["undressed_madd"] += 1
    $ character_relations["brother"]["kissed"] += 1
    $ character_relations["brother"]["touched_madd"] += 1
    $ character_relations["brother"]["anal_sex"] += 1
    $ character_relations["brother"]["anal_creampie"] += 1
    $ character_relations["brother"]["intimacy"] += 9
    $ character_relations["brother"]["lust"] = 0
    $ character_relations["brother"]["dominance"] = min(character_relations["brother"]["dominance"] + 5, 100)
    $  character_relations["brother"]["anger"]=0
    # ── Global stats ─────────────────────────────────────────────────────────────
    $ madd_willpower = max(madd_willpower - 30, 0)
    $ brother_watched_madd_vaginal_with_dad = True
    $  madd_is_virgin=False
    $wake_up_after_sex="dp"
    $number_of_people_had_sex_with_before_sleeping=2
    $ journal_event_show("Dad", "Dragged to Dad's Room (DP2)")
    $ madd_dp_finished=True
    $ journal_event_set_done("Dad", "Dragged to Dad's Room (DP)")


    jump sleep_on_bed_dad_room_exhausted_sleep



label home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_scene:
    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_flip
    with dissolve
    
    show madd flustered at left_small
    show brother lustful at right_small
    with dissolve
    x "(With one last kiss, my stepdad and stepbrother lifted and flipped me "
    x "(Now i was facing my stepbrother, with my butt raised in the air facing my stepdad...)"
    x "(I felt dads hand on my ass caressing it, while my stepbrother's hand touched my face and leaned in to kiss me...)"
    show madd blush at left_small
    x "(I looked deeply into my stepbrother's eyes and instinctively kissed him back, while my stepdad's hand continued to caress my ass...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_flip_kiss
    with dissolve
    show brother horny at right_small
    show madd deep blush at left_small
    with dissolve
    x "(Brothers kiss got more passionate as he pulled out his tongue and started to explore my mouth while dad said)"
    hide brother
    show dad possessive at right_small
    dad_says "All of this is mine...These 2 holes, I will fill them both up with my cum..."
    show madd inheat at left_small
    x "(Right after he said that i felt his hot breath on my ass seeping through my shorts)"
    x "(Then i felt him starting to kiss my butt, while his hands was trying to reach for my pussy through my shorts...)"
    x "(I could feel his tongue starting to lick my ass, his hands got more aggressive and i could feel his fingers starting to touch my pussy )"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_flip_kiss_1_5
    with dissolve
    show brother lustful at right_small
    show madd deep blush at left_small
    with dissolve
    x "(Now with his hands he moved my shorts to the side barely just to have access to my pussy and put his fingers inside of me...)"
    x "(All this while my stepbrother was still kissing me passionately and my stepdad had his face pressed against me from behind, his tongue tracing every inch of my ass obsessively )"
    show madd flustered at left_small
    x "(His hot fingers inside my pussy was making me feel all sorts of sensations, i knew it was only a precursor to what was going to happen next)"
    x "(Either way i was enjoying every second of it , being spitroasted betweenmy stepdad and stepbrother was something i didnt even know i wanted until it was happening...)"
    show madd inheat at left_small
    x "(Everytime he would thrust his fingers in and out of my pussy would send a jolt of pleasure through my body and i would moan directly into my stepbrother's mouth, which would make him kiss me even more intensly)"
    x "(They knew ...both of them knew i was enjoying this, and they were enjoying it too... )"
    hide brother
    show dad horny at right_small
    dad_says "I can feel your pussy getting wetter and wetter for me...Maddie , you cant hide it from me...I know you want me"
    show madd conflicted at left_small
    x "(I couldnt deny it anymore, but i cant say it verbally either...I just continued to moan and kiss my stepbrother while my stepdad worked his fingers inside me and pressed his mouth hungrily into my most private parts...)"
    show dad lecherous at right_small
    dad_says "Your body is as if its inviting me to put my dick inside you..."
    show madd blush at left_small
    x "(With that he withdrew his fingers and returned his tongue to my hole, dragging it slowly and deliberately like he was memorizing every part of me )"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_kiss_butt
    with dissolve
    show madd deep blush at left_small
    show dad debased at right_small
    with dissolve
    x "(He had his tongue against my hole, worshipping it with such raw intensity, like he had wanted nothing more than this for years)"
    show madd inheat at left_small
    x "(At the same time he was pinching my thighs making me spread my legs wider and wider, giving him better access)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_kiss_butt_2
    with dissolve
    show madd conflicted at left_small
    show dad perverted at right_small
    with dissolve
    x "(I could sense his breath getting heavier and heavier ...it was as if he was losing himself completely in the act, his hunger growing more desperate and consuming with every second he spent buried behind me like that)"
    x "(I should be humiliated by this, but rather i was proud that my dad was so turned on by my body scent and taste that he couldnt control himself...)"
    show madd processing at left_small
    x "(These 2 were like animals in training, and i was their reward for good behavior and in that moment i didnt mind being their reward at all)"
    x "(He finally pulls his head away from my ass and i knew his eyes were leering at my pussy  )"
    hide dad
    show brother leering at right_small
    brother_says "Dad can i have a turn now ?"
    hide brother
    show dad dominant at right_small
    dad_says "NO ! You can keep her topside...."
    show dad possessive at right_small
    dad_says "Her baby making hole is mine,I will not let anyone else touch it but me..."

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_dad_rises_to_stand
    with dissolve
    show madd trembling at left_small
    show dad authoritative at right_small
    with dissolve
    dad_says "Every inch of your body belongs to me... i will use every hole you have whenever i want..."
    show madd horrified at left_small
    x "(With that he stood up and i felt a sudden weight on top of my back, it was his stomach...he was positioning himself to enter me from behind...)"
    x "(Even brothers hand reached down to my  butt )"
    show madd flustered at left_small
    x "(Just how much these 2 wanted me was so obvious, and it was such a turn on to see them both so desperate to have me that they couldnt even wait for each other to finish...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_dad_rises_to_stand_2
    with dissolve
    show madd resigned at left_small
    show brother dominant at right_small
    with dissolve
    brother_says "Go down on my thighs now Maddie,its time for you to worship my dick with your mouth..."
    hide brother
    show dad horny at right_small
    dad_says "How are you feeling Maddie?"
    show madd submissive nod at left_small
    x "(I didnt answer him...but i lowered my head down to my stepbrother's thighs and placed it gently on his lap )"
    show madd resigned at left_small
    x "(I cant verbally say yes to my stepdad, but i can show him how much i want him by listening to both of their commands like a proper little submissive slave )"
    show madd helpless at left_small
    x "(I felt brothers hand on my back locking me in place now...There was nowhere for me to run, they were both gonna have their way with me)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_dad_rises_to_stand_3
    with dissolve
    show madd paralyzed at left_small
    show dad coercive at right_small
    with dissolve
    dad_says "Now give me your hand...I will hold them to pull you back while I ravage your pussy with my dick..." 
    show madd distressed at left_small
    x "(I didnt listen...I kept my head down on my stepbrother's thighs and suddenly dads hand grabbed mine and pulled my arm back with force)" 
    x "(Right after that brother pushed my head down harder now it was right in front of his crotch, and i could feel his hard dick pressing against my face through his pants...)"
    x "(AFter dad got hold of my hands he started dry humping me from behind, his dick rubbing against my pussy through my shorts)"
    show madd processing at left_small
    x "(This is gonna happen isnt it ? )"
    show madd shaken at left_small
    x "(Thats when i heard 2 unzipping sounds, and i knew both of them were getting ready to undress themselves )"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_dad_rises_to_stand_4
    with dissolve
    show madd conflicted at left_small
    show brother leering at right_small
    with dissolve
    x "(They had removed their jeans and shorts and now  they were in their underwear...)"
    show madd flustered at left_small
    x "(I knew brother rarely showered but because my nose was pressed against his crotch i could smell his thick, raw musk seeping through the fabric... it was heavy and inescapable...)"
    x "(Usually i should be disgusted by this, but instead my body was responding to his scent in ways i couldnt explain... his hard cock pressing right against my face was all i could focus on...)"
    show madd self loathing at left_small
    x "(It had to be the pheromones soaked deep into the fabric doing this to me... how could something so filthy make me this desperate ? what have i become ?)"
    hide brother
    show dad horny at right_small
    dad_says "Time to see your pretty tight pussy opening up for me..."
    show madd deep blush at left_small
    x "(With that i felt his hands removing my shorts  to expose my pussy to him, while brothers hand remained pressed firmly against my back, a silent reminder that there was no escaping what was about to happen)"
    
    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_dad_rises_to_stand_5
    with dissolve
    show madd inheat at left_small
    show brother debased at right_small
    with dissolve
    x "(I couldnt see it but i felt cold air hit my pussy and butt as my shorts were removed but i wasnt worried about the cold... i knew soon it would be filled  with hot semen)"
    show madd blush at left_small
    x "(I was so turned on by the thought i instinctively started licking brothers underwear kising it , tasting his dirty underwear with my tongue )"
    show madd self loathing at left_small
    x "(God i must be compltely braindead to be tasting that filthy underwear but i couldnt help myself...)"
    x "(And of course he noticed...)"
    show brother sadistic at right_small
    brother_says "Ahhahaha, look at this bitch, licking my dirty  underwear "
    show brother mocking at right_small
    brother_says "I will have you know i have worn these underwear for 5 days straight without washing them, so you are tasting 5 days worth of my sweat and pheromones with every lick"
    show brother condescending at right_small
    brother_says "You love it dont you ? You love the scent of my unwashed underwear and the thought that my dick is right there in front of your face ?"
    show madd deep blush at left_small
    x "(I didnt say a word but once i heard him say that it was 5 days worth of his sweat and pheromones in those underwear, i couldnt help but take pieces of it in my mouth whole licking it and tasting it with my tongue )"
    hide brother
    show dad sadistic at right_small
    dad_says "What a fucking slut , Fine i am going to push my dick inside you now"
    show madd shaken at left_small
    x "(I knew there was sadness in his voice, perhaps he didnt like that i willingly took his sons underwear in my mouth and tasted it)"
    x "(His body stopped touching mine and i knew he was removing his underwear )"
    show madd paralyzed at left_small
    x "(Suddenly I FELT it...i felt his dick pressing against my pussy, and i knew he was about to enter me from behind...)"
    

    if character_relations["dad"]["intimacy"]< 80:
        if madd_is_virgin and last_madd_drugged_day<0:
            if (character_relations["dad"]["vaginal_sex"]<1) and madd_is_virgin: 
                x "(NO NO no , i am still a virgin... I can't let them do this to me... )"
                x "Please stop this! Please don't do this to me!"
                show madd horrified at left_small
                dad_says "Shut up, Maddie... you are going to enjoy this whether you like it or not..."
                show madd conflicted at left_small
                x "(I have to be tough on them, I have to let them know the consequences..."
                x "Once i get out I will call the cops if you dont let me leave"
                if dad_knows_madd_stole_crypto or dad_knows_madd_drugs_food:
                    x "(to my surprise dad looked at me with a blank expression for a moment, then he started laughing)"
                    dad_says "Go on, call the cops, see if they will do anything to me"
                    x "(Huh, why is he laughing? Does he think the cops will do nothing to him? Or does he just not care?)"
                    if dad_knows_madd_stole_crypto:
                        dad_says "I will just tell them how you stole my crypto and they will throw you in jail for a long time"
                    if dad_knows_madd_drugs_food:
                        dad_says "I will tell them how you drug our food making us all sick and they will throw you in jail for a long time"
                    x "(I was shocked, i had no idea that he knew about those things, but it explained why he was laughing)"
                    x "(He had all the cards in his hand, he could easily get me arrested and thrown in jail, and he knew it)"
                    x "(I have no choice but to comply with his demands, i have to let fuck me raw ...its all over if i end up in jail)"
                else :
                    dad_says "Fucking mood killer , Just wait till i catch some dirt on you and then i will make you scream for me"
                    x "(Surprisingly brother stopped pushing me down on his crotch , i got away from dads grip as i saw them both look very angrily at me... )"
                    x "(This is gonna make them so mad...)"
                    x "(I hurried up outside to the main lobby..)"
                    $ character_relations["dad"]["intimacy"] +=7
                    $ character_relations["brother"]["intimacy"] +=7
                    jump home_areas   
        elif madd_is_virgin and last_madd_drugged_day>0:
            x "(I am still a virgin, i shouldnt be letting them do this to me but this drug wont let me move )"
            x "(I am losing the only pure part of me in such a disgusting act, getting spitroasted by my own stepbrother and stepdad)"
            x "(i shouldnt have put the drugs in the food, even the biggest whores dont lose their virginity in a disgusting threesome)"
            x "(I am sorry mom i am giving my first time to your husband while swallowing your step sons dick at the same time.)"
            x "(What have i become...)"




    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_dad_inserts_1
    with dissolve
    show madd horrified at left_small
    show dad dominant at right_small
    with dissolve
    x "(What the hell without any warning he just pushed his dick inside me from behind )"
    if madd_is_virgin:
        x "(Something inside me tore. A sharp, wet rip that made my whole body lock up. My stepdad just broke my hymen with one brutal push.)"
        x "(I could feel it — the thin membrane splitting around the head of his cock, the sudden hot trickle of blood mixing with whatever slickness my traitorous cunt had made.)"
        x "(Dad was popping my cherry while my face was buried in my stepbrother's filthy underwear. The same underwear he'd worn for five straight days. I could taste the sour, cheesy crust of his balls and the sharp piss stains on the fabric as it was forced against my tongue.)"
        x "(Dad's dick kept sinking in anyway, stretching the fresh tear wider, pushing through the resistance like he was claiming territory. Every inch that went deeper made the pain bloom hotter and meaner.)"
        x "(I tried to scream but brother's dirty crotch just muffled it into a wet, pathetic sound. The taste of his unwashed dick sweat and old cum flooded my mouth as I choked on the fabric.)"
        x "(This was it. This was how I lost it. Not to some boy my age. Not even in a bed. On my hands and knees in my stepdad's room with my stepbrother's rank underwear gagging me and my own father's cock splitting me open for the first time.)"
        x "(I felt every ridge, every vein as he forced the rest of himself inside. My cunt was trying to push him out and pull him deeper at the same time. Blood and slick leaked down my thighs in thin, shameful strings.)"
        x "(Dad groaned like he'd been waiting years for this exact moment — breaking his dead wife's daughter while her son watched and used her mouth as a laundry basket.)"
        x "(My eyes watered. Not just from the pain. From the sheer disgusting reality of it. I was never going to be untouched again. My stepdad had taken that from me and he was still pushing, still grinding deeper like he wanted to reach my fucking womb on the first try.)"
        x "(And the worst part — the part that made my stomach twist with self-hatred — was that my hips gave a tiny, involuntary twitch backward. Like my body was already learning to make room for him.)"


    show dad cruel at right_small
    if madd_is_virgin:
        dad_says "Fuck... tight little virgin cunt. You feel that, Maddie? That's me taking what your mother never gave me."
        x "(And my virginity ended so quickly too, he inserted his dick in me without any warning...it was so anticlimactic)"
        x "(I am never getting this moment again ...)"
        $madd_is_virgin=False
    dad_says "That's it , take it you little slut..."

    show dad mocking at right_small
    dad_says "bitch wants to lick her brothers dirty underwear...i will give her something to lick that is much better than that..."
    show madd conflicted at left_small
    x "(I could hear jealousy in his voice)"
    show madd overwhelmed at left_small
    x "(Oh god he was pushing all the way inside me...I could feel his dick stretching me wide open, filling every inch of me until i was completely stuffed full of him and could barely process the sensation)"
    show madd processing at left_small
    x "(Before i could even process what was happening brother spoke up )"
    hide dad
    show brother calculating at right_small
    brother_says "Wait up dad let's spitroast her together..."

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_dad_inserts_brother_joins_in_spitroast_complete
    with dissolve
    show madd paralyzed at left_small
    show brother horny at right_small
    with dissolve
    x "(IMmediately he removed his underwear and in one swift brutal motion forced his thick cock past my lips while my stepdad was still buried inside me from behind...)"
    show madd inheat at left_small
    x "(it was complete chaos, i was being fucked from behind by my stepdad while my stepbrother was fucking my mouth at the same time..."
    x "(my body was reacting to both of them , immediately my pussy was getting wetter and started pulling my stepdad all the way inside me, while my mouth was watering and i was swallowing my stepbrother's cock further and further with every thrust)"
    hide brother
    show dad laugh at right_small
    dad_says "HAHAHA, I could tell you wanted this dirty wore, you wanted to be spitroasted by your stepdad and stepbrother, you just didnt know how to ask for it..."
    show madd salivating at left_small
    x "(only sound coming from my body was the wet sounds of my pussy and mouth being fucked by my stepdad and stepbrother, and the moans of pleasure escaping my lips supressed by the dick in my mouth)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_dad_inserts_brother_joins_in_spitroast_complete_2
    with dissolve
    show madd deep blush at left_small
    show dad lustful at right_small
    with dissolve
    x "(And then they found their rhythm together, both of them driving deep into me in perfect sync, soft broken moans spilling from my lips as my body rocked helplessly between them...)"   
    show madd flustered at left_small
    x "(I could smell his scrotum and the scent of his whole crotch area was so strong in my mouth that it was making me even more turned on)"
    show madd inheat at left_small
    x "(I was so lost in the sensation that every forbidden thing about what was happening had completely dissolved... all i could think about was how right and overwhelming it felt and how badly i never wanted it to stop...)"
    show dad debased at right_small
    x "(I felt warm wet liquid trailing down my skin and knew my stepdad was drooling as he hammered into me from behind... the thought of him being so consumed by my body that he couldnt even keep his mouth closed made the heat inside me burn even hotter)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_dad_inserts_brother_joins_in_spitroast_complete_3
    with dissolve
    show madd overwhelmed at left_small
    show brother dominant at right_small
    with dissolve
    x "(My mouth was so full of my stepbrother's dick that i could barely breathe, I tried to pull away but brother's hand was still on my head locking me in place )"
    show madd salivating at left_small
    x "(My saliva starts leaking out of my mouth mixed with his precum dripping onto the bedsheets)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_dad_inserts_brother_joins_in_spitroast_complete_4
    with dissolve
    show madd broken at left_small
    show dad sadistic at right_small
    with dissolve
    x "(I realized just moments ago i was so against even getting touched by them but now i was in the most submissive position possible)"
    x "(Dad roughly grabbing my hand with his dick inside my most intimate part while brother was fucking my mouth and fisting my hair to drive himself deeper with no way for me to escape... )"
    dad_says "This bitch is so wet , i bet she wants to drink my cum out of her pussy after i fill her up with it..."
    hide dad
    show brother mocking at right_small
    brother_says "Yeah dad i bet she loves the though of drinking our cum for dessert ....Look at her face right now, she is in pure bliss being fucked by both of us at the same time...She loves it so much that she cant even pull away from my dick in her mouth even if she wanted to..."
    show madd inheat at left_small
    x "(It was like i was at their mercy , i was so horny by all that transpired that i wouldnt mind if what dad said really did happen everynight)"
    show madd conflicted at left_small
    x "(The thought of being used like this again and again... stuffed full from both ends, their bodies caging me in with nowhere to go... i wanted that to be my reality more than i wanted anything else...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_dad_inserts_brother_joins_in_spitroast_complete_5
    with dissolve
    show madd deep blush at left_small
    show dad horny at right_small
    with dissolve
    x "(Having that thought my pussy clenched around my stepdad's dick and  i got even wetter inside )"
    x "(All i could hear was the obscene rhythm they had built together, the slick sounds of my body being claimed from both ends, the groaning bedframe and my own muffled whimpers the only witnesses to what was being done to me )"
    show madd inheat at left_small
    x "(The sound, the smell, the position i was in , could it get any better ? all of them would be considered taboo in any other situation but in this moment it was all i wanted and all i needed to be happy...)"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_dad_inserts_brother_joins_in_spitroast_complete_6
    with dissolve
    show madd salivating at left_small
    show brother obsessed at right_small
    with dissolve
    x "(Now i knew both of them were closer to cumming, i could feel their dicks throbbing inside me...i felt like a mom raising her children, i was nurturing them and giving them pleasure by letting them use my body like this... )"
    show brother possessive at right_small
    x "(Now brother started moving his hips too , he was moving his hips in sync with his hand forcing my head down harder into his crotch )"
    hide brother
    show dad dominant at right_small
    x "(My hand still held tightly by my stepdad , he started pulling me even harder into him . I suppose he wanted to make sure i was taking him as deep as possible so that he could feel every inch of me clenching around him when he came inside me...)"
    show madd inheat at left_small
    x "(I was there just praying that this moment would never end, that they would just keep fucking me like this forever...)"
    show madd trembling at left_small
    x "(I felt their bodies tensing up and i knew they were both about to cum inside me at the same time... )"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_dad_inserts_brother_joins_in_spitroast_complete_7
    with dissolve
    show madd overwhelmed at left_small
    show dad lustful at right_small
    with dissolve
    dad_says "Take it all in you little slut, take all of my cum inside you..."
    show madd salivating at left_small
    x "(Hot streams of cum started shooting out of my stepdad's dick and filling my pussy with his cum, he was pulling my hand roughly so he was as deep as possible inside me )"
    hide dad
    show brother sadistic at right_small
    brother_says "Swallow my load you dirty underwear licking slut."
    show madd overwhelmed at left_small
    x "(At the same time my stepbrother was cumming in my mouth, his cum shooting down my throat he was pushing me down even harder , his dick reaching my throat )"
    show madd conflicted at left_small
    x "(Even while cumming they were degrading me but instead that had opposite effect on me, it was making me even more turned on to be degraded by them while they were cumming inside me... )"
    show madd salivating at left_small
    x "(Brothers cum deposited directly into my stomach as his dick was reaching the deppest part of my throat, while dads was reaching the deepest part of my pussy and filling me up with his cum... )"
    show madd inheat at left_small
    x "(If i was ovulating i would have surely gotten pregnant from this, but even if i wasnt ovulating the thought of being filled up with their cum and having it inside me was making me so happy that i didnt even care about the possibility of getting pregnant at this point...)"
    x "(They kept pounding me while they were cumming , And it was a lot of cum ! )"
    x "(I could feel gallons of it leaking from my mouth and pussy . it was so erotic to feel their cum filling me up and leaking out of me  )"
    show madd deep blush at left_small
    x "(i was in pure bliss and i am sure they were too...)"
    hide brother
    show dad possessive at right_small
    dad_says "Ah Maddie, your pussy is just the best... I could cum inside you all day long and never get tired of it..."
    show madd flustered at left_small
    x "(I wanted to say if he wasnt tired then please continue fucking me and cumming inside me all day long but i couldnt say it verbally, so instead i just raised my butt and pushed back against him to show him how much i wanted him to continue fucking me)"
    x "(I knew he understood the message i was sending him with my body language, because he kept pounding me)"
    show dad dominant at right_small
    dad_says "Heh, Naughty slut, For now i need rest but you will be my cumdump every night "
    show dad sadistic at right_small
    dad_says "Your belly swelling with my baby wont protect you... i will keep stuffing your holes and pumping you full every single day without exception..."
    show madd inheat at left_small
    x "(I was so happy to hear that... the thought of carrying his baby inside me while he still used my body every single night without mercy... it was such a filthy, overwhelming desire that i wanted to arch my back and offer myself to him completely right then and there...)"
    hide dad
    show brother angry at right_small
    x "(Suddenly Brother started moving his hips faster and making my head bob up and down harder on his dick, i knew he was jealous of the attention i was giving my stepdad )"
    show brother vindictive at right_small
    x "(I knew brother wanted to be the only to impregnate me ,but watching dad cum inside me right in front of him made him lash out on me...)"
    show madd traumatized at left_small
    x "(He didnt say a word just kept face fucking me rougher until his dick got limp in my mouth and he was done cumming , dad was done too.)"
    show madd broken at left_small
    x "(They both stayed inside me for a while , not wanting to pull out just yet, it was like my body was a place of refuge for them, warm and tight around them as they savored the afterglow of emptying themselves completely into me... )"
    show madd conflicted at left_small
    x "(I liked it too, soft or hard i liked the feeling of them being inside me, it made me feel wanted and needed by them... )"
    show madd resigned at left_small
    x "(After a while they finally pulled out, and i could feel the emptiness after they were gone, it was like a part of me was missing... )"
    x "(I wanted to beg them to stay inside me forever but i couldnt say it verbally, i had to wait for next time they would want to use my body again )"
    show madd depressed at left_small
    x "(They quickly wore their underwear again and i could smell the scent of his unwashed underwear again BUT He pushed me down )"


    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_dad_inserts_brother_joins_in_spitroast_complete_aftermath
    with dissolve
    show madd distressed at left_small
    show brother dominant at right_small
    with dissolve
    brother_says "Lick the cum that leaked from your mouth...CLean it all up with your tongue..."
    show madd self loathing at left_small
    x "(Eh? Why is he asking me to lick his cum that leaked from my mouth ? I guess he understood that the way to owning me was to treat as harshly as possible and make me do disgusting things for him... )"
    x "(It was the same blueprint dad had been using on me all this time... command, humiliate, degrade... and somehow it worked on me without fail every single time... )"
    show madd resigned at left_small
    x "(His underwear was near my mouth again making my mouth open  involuntarily and i started licking the cum from the bedsheets )"
    hide brother
    show dad authoritative at right_small
    dad_says "Clean it all up Slut , i sleep here..."
    show madd broken at left_small
    x "(With that he left the room and i was left there alone with the mess that was my mouth and pussy. Along with my brother )"

    scene home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_dad_inserts_brother_joins_in_spitroast_complete_aftermath_2
    with dissolve
    show madd resigned at left_small
    show brother serious at right_small
    with dissolve
    x "(I was still in that position with my brother holding my head down till i finished cleaning every drop from the sheets with my tongue, having completely surrendered to his command )"
    show brother obsessed at right_small
    brother_says "You know Maddie....i dont care if you are my stepsister or not, I want to be the father of your child more than anything in the world..."
    show brother possessive at right_small
    brother_says "I will be the one to conquer you not him...I will give you birth control..paid by my money..."
    show madd uncertain at left_small
    x "(I was surprised by his sudden confession, i didnt expect him to say something like that after what just happened... )"
    show brother dominant at right_small
    brother_says "I will get us out of this place... just wait for me... everything will be different when its just the two of us..."
    show brother fixated at right_small
    brother_says "And when we are finally alone together i will fuck you raw on every surface of our place until your womb is full of my seed..."
    show madd conflicted at left_small
    x "(this whole time i was still pressing my face into his crotch, his scent drowning me out completely while i worked my tongue against the sheets)"
    show brother smirk at right_small
    brother_says "Heh, you can even sleep with my unwashed underwear in your mouth if you want to"
    show madd depressed at left_small
    x "(With that he finally let go of my head , wore his jeans and left the room...)"
    show madd self loathing at left_small
    x "(I looked around and dads cum was on the other side of the bed ...I guess i should clean that up too... )"
    show madd resigned at left_small
    x "(I started licking that too before i left the room, i wanted to clean up every last drop of his cum from the bed as well... )"

    # ── DAD stats: vaginal sex + vaginal creampie + rimming + fingering (Tier 6) ─
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["kissed"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["vaginal_sex"] += 1
    $ character_relations["dad"]["vaginal_creampie"] += 1
    $ character_relations["dad"]["intimacy"] += 11
    $ character_relations["dad"]["lust"] = 0
    $ character_relations["dad"]["dominance"] = min(character_relations["dad"]["dominance"] + 5, 100)
    $ character_relations["dad"]["anger"] = 0
    # ── BROTHER stats: oral sex to completion + face fucking (Tier 4-5) ──────────
    $ character_relations["brother"]["kissed"] += 1
    $ character_relations["brother"]["touched_madd"] += 1
    $ character_relations["brother"]["groped_madd"] += 1
    $ character_relations["brother"]["oral_sex"] += 1
    $ character_relations["brother"]["intimacy"] += 7
    $ character_relations["brother"]["lust"] = 0
    $ character_relations["brother"]["dominance"] = min(character_relations["brother"]["dominance"] + 3, 100)
    $ character_relations["brother"]["anger"] = 0
    # ── Global stats ─────────────────────────────────────────────────────────────
    $ madd_willpower = max(madd_willpower - 40, 0)
    $ brother_watched_madd_vaginal_with_dad = True
    $  madd_is_virgin=False
    $wake_up_after_sex="spitroast"
    $number_of_people_had_sex_with_before_sleeping=2
    $ journal_event_set_done("Dad", "Dragged to Dad's Room (Spitroast)")

    jump home_areas


label home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room:
    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_pushes_madd
    with fade
    
    show madd shocked at left_small
    x "(Now I was alone with my dad in his room.)"
    x "(Suddenly, he pushed me onto the bed and got on top of me.)"
    show dad desperate at right_small
    dad_says "I've been holding back for too long, Maddie. I can't keep my f*cking hands off you anymore."
    show madd distressed at left_small
    x "(He got closer to my face, climbing over my body.)"
    show dad obsessed at right_small
    dad_says "F*ck, Maddie. You have no idea how badly I've wanted this body."
    show madd flustered at left_small
    x "(Now his face was just centimeters away from mine. I could feel his breath on my face.)"
    show dad lustful at right_small
    dad_says "Every goddamn day I watch that tight little ass of yours bounce around in those shorts and all I can think about is getting my hands — and my mouth — all over you."

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_kissing_madd
    with fade
    show madd paralyzed at left_small
    x "(Suddenly, he pinned my hands to the bed and, with his other hand, lifted my head up just slightly — close enough that his tongue could reach my face.)"
    show dad possessive at right_small
    dad_says "Tonight I'm going to use every inch of that slutty little body, Maddie. You're going to be my dirty little wife whether you like it or not."
    show madd conflicted at left_small
    x "(After saying that, he started kissing me. I involuntarily closed my eyes, my mouth opened slightly, and he started licking my tongue.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_kissing_madd_2
    with fade
    show madd flustered at left_small
    x "(He continued licking my tongue, then pulled my head a little further and locked his lips with mine.)"
    x "(His saliva coated my tongue and I could feel it moving inside my mouth.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_kissing_madd_3
    with fade
    show madd resigned at left_small
    x "(I was still pinned under his weight, his hands still holding my wrists down.)"
    x "(He pulled his face back for a second, then — while twirling his tongue — closed in on my face again.)"
    x "(It felt like his tongue was a homing missile and my mouth was the target. As soon as he hit it, he went exploring straight to my throat and then back to my tongue.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_kissing_madd_4
    with fade
    show madd inheat at left_small
    x "(He would repeat it again — pulling back and then going straight to my throat, then back to my tongue.)"
    x "(As if signaling that he was in control and that I was his to do with as he pleased.)"
    x "(By now his smell was all over me and I could feel his saliva dripping down my chin.)"
    x "(By now my mind had grown used to the smell of his saliva and started to enjoy it. I could feel my body responding to his touch and kisses.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_kissing_madd_5    
    with fade
    show madd flustered at left_small
    x "(He pulled back again, but this time went for my face — licking near each of my eyes and then my forehead.)"
    x "(As if I was being marked by his fluids.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_kissing_madd_6        
    with fade
    show madd resigned at left_small
    x "(He continued licking my face, his saliva dripping directly from his mouth onto it.)"
    x "(By now my whole face was covered in his saliva and I could smell it all over me.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_kissing_madd_7
    with fade
    show madd inhead at left_small
    x "(His tongue assault on my face continued for a while.)"
    x "(By the time he was satisfied, his saliva was fully dripping down my face, my lungs were filled with his smell, and my body was responding to his touch and kisses.)"
    x "(I wasn't naive anymore. I knew that in the end I would start to enjoy it — that I'd become addicted to his touch and kisses, and that the night was not going to end with just kissing.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_neck_kissing_madd_1
    with fade
    show madd conflicted at left_small
    x "(He lifted my head again, briefly licked my neck, and said:)"
    show dad lecherous at right_small
    dad_says "God, you smell like a f*cking dream, Maddie. Especially drenched in my spit, reeking of me from head to toe. That's how you should always smell."
    show madd self loathing at left_small
    x "(Just hearing that made me feel so dirty — but he wasn't wrong. At least to me, I also thought I smelled good covered in his saliva.)"
    x "(Then, with my hands pinned and nowhere to go, he started roughly licking my neck.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_neck_kissing_madd_2
    with fade
    show madd inheat at left_small
    x "(He licked me gently now — from my collarbone to my chin and back, over and over.)"
    x "(For some reason, whenever he started with rough licking and then suddenly switched to gentle licking, it made me feel so much more aroused and made me want him even more.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_neck_kissing_madd_3
    with fade
    show madd flustered at left_small
    x "(He repeated the same pattern again and again — rough licking, then gentle licking.)"
    x "(Licking from my collarbone to my chin, then licking my face — the cycle repeating endlessly.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_neck_kissing_madd_4
    with fade
    show madd resigned at left_small
    x "(By now he was salivating like a dog, all his saliva pouring down my face and neck.)"
    x "(My shirt was completely soaked in his saliva. Even after all of this is over, I'll probably still be able to smell it on my shirt for days.)"
    show madd inhead at left_small
    x "(The thought of that made me more aroused instead of disgusted.)"
    x "(He was right when he said I would accept him. After multiple encounters, I was giving in to pleasure much faster and starting to crave being owned by him.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_neck_kissing_madd_5
    with fade
    show madd processing at left_small
    x "(Even though he kept running his tongue all over my face and neck, my mind was wandering to other things.)"
    x "(It had been a very short time since he started doing these things to me, but a pattern was already forming in my mind.)"
    x "(I would reject him at first, but he'd still have his way with me — and then after a while I would start to enjoy it and crave it. The next time he did it I would give in much faster, and then the cycle would repeat again and again.)"
    x "(Eventually there would come a time where I would just give in right away. That's when I would be fully under his control and fully addicted to him.)"
    show madd inhead at left_small
    x "(I guess that's when we would officially be 'married'.)"
    x "(When that day comes, I don't think I would be using birth control anymore — or any form of protection at all. He would take me raw, I would get pregnant with his child, and that child would be the product of our love and our marriage.)"
    x "(I realize how twisted that thought is, but at the same time I would be so addicted to him that I wouldn't care. I would just want to be with him and have his child.)"
    x "(Maybe the world would never even know that we are father and daughter. Maybe we would just be a normal couple and no one would ever know the truth.)"
    show madd shaken at left_small
    x "(I snapped back to reality as he stopped licking my neck and pulled away from my face — if only for a second.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_groping_madd_1
    with fade
    show madd distressed at left_small
    x "(The hands that were holding my wrists down started to roam my body — groping my breasts.)"
    x "(He was very rough with them, squeezing hard and kneading them.)"
    show madd inheat at left_small
    x "(It was a bit painful, but by this point I was uncontrollably aroused and started making small moans and whimpers.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_groping_madd_2
    with fade
    show madd inheat at left_small
    x "(Those moans were like fuel to his fire — he squeezed my breasts even harder and started to pinch my nipples.)"
    show dad dominant at right_small
    dad_says "You like that, you little slut? You like when daddy gropes those tits and twists your nipples raw?"
    show madd conflicted at left_small
    x "(I can't... I can't say I like it. If I do, things will escalate and I'll be in far more trouble.)"
    x "(I didn't say anything, but my body was giving me away — I was moaning and whimpering, and my nipples were hardening under his touch.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_groping_madd_3
    with fade
    show dad mocking at right_small
    dad_says "Too pathetic to admit you love it, huh? Your body's already screaming yes for me."
    show madd distressed at left_small
    x "(Then he started squeezing my breasts even harder. The shirt was getting tighter and tighter around my chest.)"
    x "(The imprints of my hardened nipples were now visible through my shirt.)"
    show dad lecherous at right_small
    dad_says "Look at those stiff little nipples poking through the fabric, Maddie. Your body is begging for it even while your mouth plays dumb."
    show madd deep blush at left_small
    x "(I just wanted to disappear. I was so embarrassed. It's so frustrating getting aroused by your own stepdad, and then having him humiliate you by pointing out exactly how aroused you are.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_groping_madd_4
    with fade
    show madd resigned at left_small
    x "(Due to his touch, I instinctively wrapped my arms around his neck and pulled him closer.)"
    show madd conflicted at left_small
    x "(No... no, no. I didn't mean to do that.)"
    x "(But he took it as an invitation.)"
    show dad manipulative at right_small
    dad_says "Stop pretending you don't want it, you little tease. I can feel how hot and wet you're getting under me. Just shut up and let daddy use you the way you were meant to be used."
    show madd resigned at left_small
    x "(As he said that, he squeezed my breasts again, pulled them toward his mouth, and took them in, sucking on them.)"
    x "(He had my right tits in his mouth while using my other tits to rub his face against — as though my breasts were pillows he was both sucking and nuzzling.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_groping_madd_5
    with fade
    show dad debased at right_small
    x "(He pulled back from my tits for a second, pinned me down again with his hands, and said:)"
    dad_says "F*ck, even your tits smell incredible, Maddie. Every inch of your body smells like it was made to drive me absolutely out of my mind — like you were built from the ground up to be mine."
    show madd inheat at left_small
    x "(Then he pressed his face between my breasts, licking the skin between them, then went back to sucking on them.)"
    x "(He continued sucking and nibbling on my breasts for a while. My legs relaxed — there was no escape, and I was completely at his mercy.)"
    show madd resigned at left_small
    x "(And somehow that made me feel peaceful and safe. Even though I had resisted at first, I was now craving it more and more.)"
    x "(My body was no longer tense — it was fully relaxed and accepting him.)"
    x "(It was as if my body had already decided to give in to him and my mind was just trying to catch up.)"
    x "(He finally stopped sucking on my breasts and pulled back, giving me and my body a moment to breathe.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_making_maddie_lick_armpits
    with fade
    show dad sadistic at right_small
    dad_says "Time to shove that face somewhere new, Maddie. Daddy's got a special treat for that greedy little mouth of yours."
    show madd confused at left_small
    x "(Hm? What is he going to make me do now? I hope it's not something too crazy.)"
    show madd shocked at left_small
    x "(He removed his shirt, revealing his hairy chest and armpits. He had been wearing a black tank top underneath.)"
    x "(Immediately after taking off his shirt, his hands were back to pinning me down.)"
    x "(He leaned down and kissed me again.)"
    show madd relieved at left_small
    x "(Oh, it's just a kiss. I was worried for nothing.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_making_maddie_lick_armpits_0
    with fade
    show madd horrified at left_small
    x "(That's when I realized how wrong I was.)"
    x "(After kissing me, he raised his arm, exposing his hairy armpit. A strong smell of sweat and musk immediately filled the air and hit my nose like a truck.)"
    x "(His other hand started pulling my head closer to his armpit.)"
    show madd conflicted at left_small
    x "(Is this the dessert he was talking about? God, his armpits smell so strong.)"
    x "(It's absolutely disgusting — but at the same time, why does it also smell so good to me? I can't help but feel aroused by the smell of his sweat and musk.)"
    show madd inheat at left_small
    x "(I was now just inches away from his armpit and the smell was so strong it was filling my lungs and making me lightheaded.)"
    show dad controlling at right_small
    dad_says "That's right, get that nose buried in there and breathe it all in, you filthy little pig. Fill those lungs with daddy's stink."
    show madd salivating at left_small
    x "(I was inhaling deeply without even thinking — trying to take in as much of the smell as I could, as if trying to get drunk off his armpits.)"
    show dad perverted at right_small
    dad_says "Go on then, you dirty little animal — stick that tongue in and lick up every last drop of daddy's sweat."
    dad_says "Get it all. Don't you dare waste a drop."

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_making_maddie_lick_armpits_1
    with fade
    show madd hesitant at left_small
    x "(I pulled my head back for a second, trying to gather the courage.)"
    x "(Just from the smell, I could tell his armpits would be salty, musky, and sweaty.)"
    show madd disgusted at left_small
    x "That's disgusting. You need to shower, dad."
    show madd salivating at left_small
    x "(Right after saying that, I was drawn to his armpit and I licked it — like a moth to a flame, I was pulled in by the smell and just had to taste it.)"
    show madd self loathing at left_small
    x "(I didn't even realize it — his hands weren't pushing me anymore. My body was acting on its own, licking his dirty armpits.)"
    x "(God... what have I become?)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_making_maddie_lick_armpits_2
    show madd salivating at left_small
    x "(It was just as I expected — salty, musky, and sweaty.)"
    x "(But somehow I found myself enjoying the taste.)"
    x "(His hairy armpits acted like a container that held the sweat and musk in, making it more concentrated and stronger in smell and taste.)"
    x "(I didn't mind the hair at all. In fact, it made it even better.)"
    show madd inheat at left_small
    x "(I was slowly licking his underarms — including the hair — and the worst part was that I was softly moaning and whimpering while doing it.)"
    show madd self loathing at left_small
    x "(I was so disgusted with myself for enjoying it.)"
    x "(I probably enjoyed it more than he did.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_making_maddie_lick_armpits_3
    with fade
    show madd salivating at left_small
    x "(I continued passionately licking his underarms.)"
    x "(I wanted the taste of his sweat and musk to coat my entire tongue and fill my mouth.)"
    x "(I wanted it to linger inside me as long as possible.)"
    show dad sadistic at right_small
    dad_says "Look at you — a depraved little pig slobbering all over my pits like you'd starve without it. You absolutely love the taste of daddy's filthy sweat, don't you?"
    show madd self loathing at left_small
    x "(After saying that, he started laughing. He probably thought it was a sign of his victory over me.)"
    x "(Nobody in their right mind would enjoy licking their dad's armpits — so he probably figured that me enjoying it meant I had fully given in to him and was now completely under his control.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_making_maddie_lick_armpits_4
    with fade
    show madd inheat at left_small
    x "(As I continued greedily licking his armpits, I could tell he was enjoying it too.)"
    x "(His body relaxed as my tongue massaged his underarms.)"
    show dad possessive at right_small
    dad_says "You lick like a starving animal, Maddie. You'd be happy living with that slutty face buried in my armpits forever, wouldn't you? Just be daddy's permanent pit-licker and never leave."
    show madd inhead at left_small
    x "(I hated that the thought of being his little armpit licker and staying in his room forever actually sounded appealing to me.)"
    x "(At this moment I would have agreed to anything just to stay and keep licking his armpits.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_making_maddie_lick_armpits_5
    with fade
    show madd inheat at left_small
    x "(At this point I was fully addicted to licking his armpits. I wanted to do it all day and all night.)"
    show dad dominant at right_small
    dad_says "Alright, you disgusting filthy little slut. Time to get that pretty face truly wrecked."
    show madd resigned at left_small
    x "(After saying that, he pushed my head even closer to his armpit and with his raised arm locked my head in place.)"
    x "(Now my face was fully buried in his armpit and held there.)"
    x "(Locked in place — me and my 'meal' for the next few minutes.)"
    show madd inheat at left_small
    x "(He was right. I would get addicted to this. I thought to myself as I made out with his hairy armpits, using my tongue to explore every inch of his underarms.)"
    x "(It was like every hair of his armpit was a tentacle wrapping around my tongue and pulling me deeper in.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_making_maddie_lick_armpits_6
    with fade
    show madd salivating at left_small
    x "(I was in armpit heaven — a state of pure bliss and ecstasy as I made out with his underarms.)"
    x "(At this point I was salivating. Spoiled by the taste of his sweat and musk, I wanted more and more.)"
    x "(I wanted to cover my whole body in his scent. His sweat and musk were like a drug to me — I wanted to be high on it all the time.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_making_maddie_lick_armpits_7
    with fade
    show madd inheat at left_small
    x "(He pushed my face even harder into his armpits. There was no space left between my face and his underarms.)"
    show dad dominant at right_small
    dad_says "Get that slutty face buried all the way in there, Maddie — lick every last inch of it. I want my stink so deep in you that you'll smell like me for a week."
    show dad controlling at right_small
    dad_says "Breathe in my scent, you addicted little slut. Let it rot deep into your brain. Let it make you need me like the f*cking drug I am."
    show madd inhead at left_small
    x "(He was using animalistic language to describe the effect of his pheromones on me — as if I were some kind of animal being marked by his scent and driven crazy by it.)"
    x "(He wasn't wrong, though. I was being marked by his scent and going crazy for it.)"
    show madd resigned at left_small
    x "(I knew all of this was preparation for the next step — which was probably going to be him taking me. But his armpits had already broken down so much of my resistance.)"
    x "(I wouldn't be able to refuse him after this.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_making_maddie_lick_armpits_8
    with fade
    show madd salivating at left_small
    x "(He finally let go of my head, but I kept lapping at his armpits a while longer. Finally, I pulled back for a second to breathe.)"
    show dad smirk at right_small
    dad_says "So? How does daddy's filthy pit-sweat taste on that pathetic little tongue of yours, Maddie? Still think I need a shower?"
    show madd self loathing at left_small
    x "It tasted good. It tasted like the best meal I've ever had in my life."
    x "(It hit me then — I had gone from 'that's disgusting, you need to shower' to 'it's the best meal I've ever had' in a matter of minutes.)"
    x "(Even after saying that, my eyes were still locked on his armpits. My mind was still craving them. I wanted to go back.)"
    x "(Those sweaty armpits were just so incredible. If he had used a gym towel after a workout and could squeeze out the excess sweat, I would have asked him to wring it right into my mouth.)"
    show madd broken at left_small
    x "(My mind is getting so warped living here with them.)"
    x "(By this point I was fully his — he could have told me to bark and I would have.)"    

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_on_top
    with fade
    show madd resigned at left_small
    x "(At this point I was fully in his control. Whatever his command, I would follow without question.)"
    show madd inheat at left_small
    x "(My body involuntarily raised my legs and spread them apart — almost as if inviting him in.)"
    show dad smirk at right_small
    dad_says "Heh. Look at this filthy little girl spreading open for daddy all on her own. You want this that badly, Maddie?"
    show madd deep blush at left_small
    x "(As he said that, he started removing his jeans.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_on_top_removing_jeans
    with fade
    show madd flustered at left_small
    x "(As he removed his jeans, I could see his black underwear and the bulge forming in it.)"
    show dad dominant at right_small
    dad_says "Time to get that slutty little hole out in the open, shall we?"
    
    if character_relations["dad"]["intimacy"]<80:
        if madd_is_virgin and last_madd_drugged_day<0:
            if character_relations["dad"]["vaginal_sex"]<1 and madd_is_virgin: 
                x "(Oh no , he's gonna go for my pussy)"
                x "(NO NO no , i am still a virgin... I can't let him do this to me... )"
                x "Please stop this! Please don't do this to me!"
                show madd horrified at left_small
                dad_says "Shut up, Maddie... you are going to enjoy this whether you like it or not..."
                show madd conflicted at left_small
                x "(I have to be tough on them, I have to let them know the consequences..."
                x "Once i get out I will call the cops if you dont let me leave"
                if dad_knows_madd_stole_crypto or dad_knows_madd_drugs_food:
                    x "(to my surprise dad looked at me with a blank expression for a moment, then he started laughing)"
                    dad_says "Go on, call the cops, see if they will do anything to me"
                    x "(Huh, why is he laughing? Does he think the cops will do nothing to him? Or does he just not care?)"
                    if dad_knows_madd_stole_crypto:
                        dad_says "I will just tell them how you stole my crypto and they will throw you in jail for a long time"
                    if dad_knows_madd_drugs_food:
                        dad_says "I will tell them how you drug our food making us all sick and they will throw you in jail for a long time"
                    x "(I was shocked, i had no idea that he knew about those things, but it explained why he was laughing)"
                    x "(He had all the cards in his hand, he could easily get me arrested and thrown in jail, and he knew it)"
                    x "(I have no choice but to comply with his demands, i have to let fuck me raw ...its all over if i end up in jail)"
                else :
                    dad_says "Fucking mood killer , Just wait till i catch some dirt on you and then i will make you scream for me"
                    x "(Surprisingly he got off of me and was now  looking at me with a dead expression)"
                    x "(This is gonna make them so mad...)"
                    x "(I hurried up outside to the main lobby..)"
                    $ character_relations["dad"]["intimacy"] +=7
                    jump home_areas  
        elif madd_is_virgin and last_madd_drugged_day>0:
            x "(I feel the effects of drug still in my system , i am still a virgin  I dont wanna lose it to my stepfather)"
            x "(what kind of disgusting whore lays with her own stepdad , worst so in the same bed where mom made love with him)"
            x "(And here i am about to lose my virginity in the same bed , i am so sorry mom i am about to give my first time to dad while moaning like a bitch)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_on_top_removing_maddie_shorts
    with fade
    show madd deep blush at left_small
    x "(He roughly pulled my shorts down my raised legs.)"
    x "(In one swift motion, he pulled them free, exposing me to him.)"
    x "(Cold air hit me, and I saw him hungrily staring.)"
    show dad hungry at right_small
    dad_says "F*ck, look at that — the prettiest, wettest little hole I've ever seen. I'm going to absolutely wreck it, Maddie."
    show madd inheat at left_small
    x "(He climbed on top of me again and started kissing me passionately.)"
    x "(As he kissed me, his hands moved to his own underwear.)"
    x "(He started pulling it down, exposing his dick.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_on_top_both_naked
    with fade
    show madd inheat at left_small
    x "(The moment his underwear left his body, his dick grazed my skin — and I felt a shiver run down my spine.)"
    x "(I knew he was going to enter me. I knew it was wrong — me being a replacement for my mom — but I couldn't help feeling excited.)"
    show madd conflicted at left_small
    x "(The temperature in the room seemed to rise as he positioned himself between my legs, his cock pressing against me.)"
    show dad delusional at right_small
    dad_says "Once I stuff myself inside you there's no going back, Maddie. You'll be my dirty little wife forever — my personal bitch that i get to fuck whenever i want."
    show madd inheat at left_small
    x "(For some reason, a wide smile spread across my face as he said that — and he saw it too.)"


    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_on_top_penetrating_maddie
    with dissolve
    show madd inheat at left_small
    if madd_is_virgin:
        x "(The thick head of his cock pressed harder against me — then pushed.)"
        x "(Something inside tore with a wet, ugly sound I felt more than heard. A sharp, burning rip that made my back arch off the bed.)"
        dad_says "Fuck... there it is. I felt that little cherry pop. You're bleeding on me already, Maddie."
        x "(My stepdad just broke my hymen. Mom's husband was splitting me open on the same bed she used to sleep in.)"
        x "(I could feel it — the thin skin giving way, the sudden hot trickle of blood coating his cock as he kept forcing himself deeper. It stung like hell, but he didn't stop. He just kept sinking in like he had every right to be there.)"
        x "(This was how I was losing it. Not gently. Not to someone who cared. To the man who used to fuck my mother. And I was wet. I was fucking wet while he did it.)"
        x "(Every inch that stretched me wider felt like he was carving out a new place inside me that would only ever belong to him now. I could feel my own blood mixing with the slick mess between my legs, making everything slippery and filthy.)"
        dad_says "There we go... all the way in. Your virgin cunt just swallowed your dad's cock. No going back now, girl."
        x "(I wanted to scream. I wanted to tell him to get off me, that this was wrong, that I was still supposed to be untouched. But all that came out was a broken, shaky breath as he bottomed out inside me for the first time.)"
        x "(He was all the way in. My stepdad's cock was buried inside his stepdaughter's virgin pussy. And I could feel every twitch of it.)"
        x "(The worst part wasn't the pain. It was the sick, heavy realization that there was no going back from this. I wasn't a virgin anymore. I was just another hole in this house for him to use.)"
        dad_says "This pussy belongs to me now. Same bed your mother used to spread her legs on... and now her daughter's doing the same thing. First I had the vintage now i have the modern version of Emily"
        dad_says "God am i blessed."
        $ madd_is_virgin = False

    $ brother_hears_madd_moan= True
    x "(He slowly entered me and I felt a jolt of pleasure run through my body.)"
    x "(As he pushed inside, I could feel the warmth of him spreading through me — the distance between us closing as he filled me up.)"
    x "(Immediately after entering me, he started pounding. This night was not going to be gentle — it was going to be rough and passionate. He knew the only way to make me his was to be forceful, to show me he was in control and that I was his.)"
    x "(And he was doing exactly that.)"
    show madd salivating at left_small
    x "(He was pounding into me with such force that I could feel my body bounce with each thrust. I could no longer hold back my moans of pleasure.)"
    x "(The room filled with the sound of our bodies and my moans as he drove into me hard.)"
    show dad dominant at right_small
    dad_says "You love getting pounded by daddy's cock, don't you, you filthy little slut? Say you love it. Say it."
    show madd inheat at left_small
    x "(I didn't nod or say anything, but the way my body was reacting said everything.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_on_top_pounding_maddie
    with dissolve
    show madd inheat at left_small
    x "(The whole bed shook with the force of his thrusts. He was enjoying himself too — saliva dripping from his mouth, his face flushed with pleasure.)"
    x "(Some of his saliva dripped directly into my mouth, reminding me of the taste from earlier — and I swallowed it without hesitation.)"
    x "(Anything he gave me I was taking it. Anything he did to me I was loving it. It truly felt like we were married in that moment. I was his and nothing else mattered.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_on_top_pounding_maddie_2
    with dissolve
    show madd inheat at left_small
    x "(With every thrust he was hitting me deeper and deeper — the sensation so overwhelming it was reaching my very core.)"
    x "(It was the most intense pleasure I had ever felt in my life.)"
    x "(No matter how repulsive he was to me, I couldn't deny his raw nature — his dominance, his control over me, combined with his forceful presence was making me feel things I had never felt before.)"
    x "(I could no longer control what came out of my mouth.)"
    show madd salivating at left_small
    x "Fuck me, dad. Fuck me harder."
    x "(Even he was surprised by my words, but he didn't stop — he kept his pace, steady and relentless.)"
    show dad mocking at right_small
    dad_says "Heh. There it is — that dirty little mouth finally catching up to that slutty body."
    show madd salivating at left_small
    x "Yes, dad. I love it when you fuck me like this. I want to be your bitch"
    x "(I don't know why I was saying those things, but I couldn't stop myself.)"

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_on_top_pounding_maddie_3
    with dissolve
    show madd inheat at left_small
    x "(Hearing those words only made him more aggressive.)"
    x "(I could feel every thrust more intensely now — the sound of our bodies colliding growing louder and louder.)"
    x "(This whole time his sweat and saliva had still been dripping into my mouth.)"
    x "(I was swallowing it — not just to please him anymore. I was genuinely starting to enjoy the taste of his sweat and saliva.)"
    show madd self loathing at left_small
    x "(I no longer cared that he could see me hungrily swallowing it. I knew he'd only dominate me more if he noticed — and I wanted that.)"
    show dad sadistic at right_small
    dad_says "You filthy little thing — swallowing daddy's spit like you'd shrivel up without it. You're completely obsessed with tasting me, aren't you, you disgusting little pet?"
    show madd salivating at left_small
    x "(I kept moaning but this time nodded my head eagerly.)"
    show dad controlling at right_small
    dad_says "I bet you'd open that pathetic little mouth for my piss too, wouldn't you? Swallow every drop of it down like the good filthy pig you are."
    show madd resigned at left_small
    x "(I was surprised by his words, but I reassured him.)"
    x "Yes, dad. I love everything that comes out of you — your sweat, your saliva, everything."
    x "The smell of your armpits, your feet, your scent — everything about you is so intoxicating to me. I love it all."
    show dad sadistic at right_small
    dad_says "Hehe. There she is — the real Maddie. Completely broken, turning into a whore for your dad."
    dad_says "You'll be mine for life once I knock you up, you desperate little breeding slut."
    show madd salivating at left_small
    x "(After his words, I felt a surge of pleasure run through my body. I was close to the edge, so I pushed his buttons even more.)"
    x "Please, dad. Keep going until I get pregnant. I want to be your baby maker. I want to carry your child inside me."
    x "(I don't know what compelled me to say those words, but I said them — and I meant them, at least in that moment.)"
    

    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_on_top_pounding_maddie_4
    with dissolve
    show madd salivating at left_small
    x "(While being pounded, the thought of being impregnated by him made me so desperate that I finally started to squirt all over the bed.)"
    x "(His presence blocked the path and the squirting scattered in all directions.)"
    x "(I kept moaning uncontrollably as it kept coming — and he didn't stop, he kept going.)"
    show dad excited at right_small
    dad_says "Holy sh*t, Maddie — you're squirting like a broken pipe. Look at what daddy's cock does to you, you soaking little slut."
    show madd salivating at left_small
    x "(I nodded eagerly. The sound of the room had shifted — wetter, messier, his movements creating a different sound now.)"
    show dad horny at right_small
    dad_says "Ah — f*ck, Maddie — I'm about to blow. Every last drop going straight into that greedy little hole."
    dad_says "I'm going to breed you raw, you little slut. Fill that womb till it drowns in my seed"
    show madd salivating at left_small
    x "Yes, please, dad. I want this —  I want to be your pregnant wife."
    show madd inheat at left_small
    x "(Hearing this, I felt him throbbing inside me. The heat he was emanating grew to its peak and I could feel him pulsing as he neared his release.)"


    scene home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_on_top_cumming_inside_maddie
    with dissolve
    show madd inheat at left_small
    x "(Finally, I felt him release inside me — pulsing and filling me up. There was no protection, no way to stop it, and I didn't want to stop it. I wanted to be filled.)"
    x "(As he came inside me, I could feel the warmth spreading through me as I continued making sounds of pleasure for the man I now thought of as my future husband.)"
    x "(The sounds of everything mixing together — it was the most overwhelming thing I had ever experienced. It felt like music.)"
    show madd broken at left_small
    x "(I knew my brother was in the house, but I was still moaning without restraint as my dad filled me up.)"
    show dad dominant at right_small
    dad_says "Take every last drop of daddy's load deep inside you, you filthy cum dump. Not one drop leaves that hole."
    show madd salivating at left_small
    x "Give it all to me, dad. I want every drop of it."
    x "(His hips were still moving as he came inside me — so much that I could feel it dripping out of me and onto the bed.)"
    x "(Being filled by him sent the most overwhelming warmth through my entire body. It was as if I was being filled with love and pleasure at the same time.)"
    show madd inhead at left_small
    x "(I was in the bed where my mom used to sleep — and here I was, taking her place in every sense. She had been replaced by me in his heart and in his bed.)"
    x "(I knew this wronged her memory, but my mind kept making excuses — telling myself I was helping a grieving husband.)"
    show madd processing at left_small
    x "(While I was lost in those thoughts, I was still moaning and begging him to fill me completely — and he kept going until he had nothing left.)"
    x "(Finally, when he was done and I couldn't feel him pulsing anymore, he stopped moving. He just stayed inside me, and I went quiet.)"
    x "(I knew my moans had probably echoed through the whole house. My brother had almost certainly heard everything.)"
    show madd relieved at left_small
    x "(Even still, his presence inside me felt incredible.)"
    show dad smirk at right_small
    dad_says "So? How does it feel to have daddy's cum leaking out of you? Did my dirty little slut enjoy getting bred raw?"
    show madd inheat at left_small
    x "Yes, dad. It felt amazing."
    show dad possessive at right_small
    dad_says "You're officially mine now, Maddie. Perhaps you wont get pregnant this time — but we'll keep at it until that belly swells."
    show madd inhead at left_small
    x "(Hearing this, I felt a surge of warmth and relief wash over me. Is this what I had been waiting for? To be protected, loved, and claimed by my stepdad?)"
    show madd happy at left_small
    x "Thank you, dad. I'm so happy to be your wife. I'll do anything to make you happy — including getting pregnant with your child."
    show madd processing at left_small
    x "(I knew my ovulation had already passed and I probably didn't get pregnant from this — but I desperately wished I could give him what he wanted.)"
    show dad smirk at right_small
    dad_says "My door — and my bed — are always open for you, Maddie. Anytime you want to crawl back in here and take more of what daddy gives you, you know where to come."
    show dad sadistic at right_small
    dad_says "Hehe. I love using every filthy hole in that slutty little body. And I'll keep stuffing you full until you give me that baby."
    show madd conflicted at left_small
    x "(He was still degrading me even while calling me his wife — and somehow I liked it.)"
    show madd resigned at left_small
    x "Yes, dad. I'll always be yours. I'll do anything you want. I'll always be your obedient wife."
    show madd flustered at left_small
    x "(I felt him soften inside me and he finally pulled out, a rush leaking out of me and onto the bed.)"
    x "(God... just how much did he have? I was leaking so much it almost felt like I was losing control of myself — but it was just him, still draining out of me.)"
    show madd sad at left_small
    x "(Ah... I'm so tired now.)"
    x "Please let me sleep in your bed tonight, dad. I want to be close to you."
    show dad laugh at right_small
    dad_says "Heh. Next time I just know i will catch your face buried in my armpits in the middle of the night I'll just clamp your head in there and make you sleep like that. But yeah — stay."
    show madd happy at left_small
    x "(I nodded, and I was so exhausted that I simply lay down on the bed and drifted off to sleep — still leaking, still wearing his scent.)"

    # ── DAD stats: vaginal sex + vaginal creampie + armpit licking + groping + kissing (Tier 7) ──
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["kissed"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["vaginal_sex"] += 1
    $ character_relations["dad"]["vaginal_creampie"] += 1
    $ character_relations["dad"]["intimacy"] +=11
    $ character_relations["dad"]["lust"] = 0
    $ character_relations["dad"]["dominance"] = min(character_relations["dad"]["dominance"] + 10, 100)
    $ character_relations["dad"]["anger"] = 0


    # ── Global stats ─────────────────────────────────────────────────────────────
    $ madd_willpower = max(madd_willpower - 30, 0)
    $wake_up_after_sex="pussy"
    $number_of_people_had_sex_with_before_sleeping=1
    $  madd_is_virgin=False
    $ journal_event_set_done("Dad", "Dragged to Dad's Room (Dad Only)")

    jump sleep_on_bed_dad_room_exhausted_sleep

    
label dad_brother_join_maddie_in_dads_room_dp2:
    scene black 
    with dissolve  
    show madd resigned at left_small
    x "(As soon as he dragged me into the room, he settled on the bed and gently lowered me on the floor next to him. I was thinking today he might be gentle with me but immediately after he shoved his foot in my mouth.)"
    show madd distressed at left_small
    x "(I stayed still cleaning his foot while he waited till brother joined us. And he too shoved his foot in my mouth.  They had made it clear that i was their pet and they were going to treat me like one.)"
    show madd traumatized at left_small
    x "(Eventually after them making me clean their feet then armpits then slapping my face with their cocks they finally got me sandwiched between them and started to have their way with me. )"
    show madd broken at left_small
    x "(I remember getting dragged to his room in the afternoon and now it was evening and they were still using me. )"

    scene dad_brother_dp2_clothes_on 
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show madd resigned at left_small
    x "(they were relentlessly pounding me just like they did last time . Only difference was this time i knew my place since i knew going along with it was the only way to get through it. )"
    show madd violated at left_small
    x "(Since afternoon they had already came in me twice, filling me up with their cum and stretching me out like a toy. But they never stopped. They just kept going and going, )"
    show dad sadistic at right_small
    dad_says "God damn, this bitch is even tighter than last time. "
    hide dad
    show brother lecherous at right_small
    brother_says "Yeah, dad you gotta try her asshole, it's like squeezing me in there. "
    show madd disgusted at left_small
    x "(Hearing them talk about me like I'm not even here... just some toy they're passing back and forth.)"
    show madd horrified at left_small
    x "(Dad bragging about how much tighter I feel than last time and brother laughing, telling him to try the other hole... its so degrading.)"
    show madd violated at left_small
    x "(They're literally discussing which part of me feels better while I'm stuck between them.)"  
    hide brother
    show dad dominant at right_small
    dad_says "Hey Adam , remove her clothes . Our pet doesnt need to wear them in our presence. "
    show madd paralyzed at left_small
    x "(I sensesd brother nod behind me as i felt his hand on my back, pulling my shirt up and over my head. I was now completely naked in front of them, just like they wanted.)"
    show madd resigned at left_small
    x "(After that he removed his own shirt as well and so did dad.)"

    scene dad_brother_dp2_clothes_off
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd violated at left_small
    x "( I'm completely naked between them now. No clothes, no protection, nothing.)"
    show madd horrified at left_small
    x "(My stepdad under me and my stepbrother behind me, both their dick buried deep inside me at the same time, stretching me to the limit. I'm literally sandwiched between the two men who are supposed to be my family.)"
    show madd disgusted at left_small
    x "(Their hot, sweaty bodies are rubbing all over me. I can feel every drop of their sweat soaking into my skin.)"
    show madd nauseated at left_small
    x "(It's so fucking disturbing. Their family sweat is mixing with mine, seeping into my pores like they're trying to mark me from the inside out. I smell like both of them now. I guess that's what they wanted, to make me part of their family in the most twisted way possible.)"

    scene dad_brother_dp2_clothes_off_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    x "(My tits are bouncing up and down like crazy with every thrust. Dad keeps lunging forward trying to catch them in his mouth like it's some twisted game.)"
    show madd horrified at left_small
    x "(Every time he catches one he bites down hard on my nipple... sharp pain shoots through me but I just bite my lip and take it.)"
    show madd violated at left_small
    x "(When he misses he licks instead, dragging his wet tongue all over my nipple and tits like he's marking his territory.)"
    show madd trembling at left_small
    x "(Bite... lick... bite... lick... back and forth while my stepbrother keeps slamming into me from behind. I'm stuck between them with no escape.)"

    scene dad_brother_dp2_clothes_off_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    x "(The room is filled with nothing but wet, nasty squelching sounds every time they slam into me... and these pathetic little moans I can't stop from coming out.)"
    show madd horrified at left_small
    x "(It's the sound of a daughter getting double-teamed by her own dad and brother. The men who were supposed to look after her. Now they're just using both her holes at once.)"  
    show madd self loathing at left_small
    x "(My moans keep slipping out and echoing around the walls, coming straight back to me. I have to listen to myself getting fucked like this on repeat. It's making me sick.)"  
    show madd disgusted at left_small
    x "(I hate how my body sounds when they're inside me. Like I'm enjoying being their toy. The noises are so fucking nasty and humiliating knowing that all of the sounds in the room are coming from me. )"

    scene dad_brother_dp2_clothes_off_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad lustful at right_small
    dad_says "Man this view is amazing. Seeing my daughter moaning in pleasure while I'm pounding her ,making her tits bounce up and down... it's like a dream come true. "
    show dad possessive at right_small
    dad_says "Sorry Adam, i would let you enjoy this view but her pussy is precious to me. Only I get access to her uterus."
    hide dad
    show brother serious at right_small
    brother_says "Understood Dad"
    show madd conflicted at left_small
    x "(When brother said 'Understood' I heard the sadness in his voice. He wants it too. He wants to fill me up and knock me up just like dad does. They're both fighting over who gets to put their seed inside me)"
    show brother lecherous at right_small
    brother_says "The view from back here ain't bad either. Watching her fat ass jiggle while I stretch her asshole... it's fucking out of this world."
    show madd violated at left_small
    x "(THe moment i feel bad for brother is exactly when he starts talking about how much he enjoys stretching my asshole. He's going on about my ass bouncing and my stretched asshole gripping his dick like it's the greatest view in the world)"
    show madd conflicted at left_small
    x "(They're both obsessed with every disgusting detail of my body. I dont know if i should  be disgusted or flattered that they find every inch of me so irresistible. )"
    hide brother
    show dad possessive at right_small
    dad_says "You know Adam, Emily was great too but she was infertile. Luckily Maddie here is fertile as hell. "
    show dad calculating at right_small
    dad_says "I have been reading her medical records since she turned 18 and I know for a fact that her ovulation cycles are regular and her fertility is off the charts. She's gonna give me so many kids."
    show madd shocked at left_small
    x "(I froze. Hearing him casually talk about reading my medical records since I turned 18... tracking my ovulation... planning to breed me over and over until I give him as many kids as he wants. As if everything was by design...his plan all along.)"
    show madd distressed at left_small
    x "(But despite my body craving both of them, I wanted to stand up for my mom.)"
    show madd angry at left_small
    x "Please... don't talk about mom like that..."
    show dad angry at right_small
    dad_says "Bitch, you don't get to tell me what to do. Your mom is dead and I'm the one who's taking care of you now."
    show dad cruel at right_small
    dad_says "If you want to know the truth, I used to fuck that infertile bitch raw every single night. Pumped her full of cum for months hoping she'd finally get pregnant. Since she was useless, now it's your turn. And I'm gonna show you exactly how hard I used to wreck her"
    show madd resigned at left_small
    x "(I shouldn't have said anything. I should have just stayed quiet and let them do whatever they wanted to me. I prepared myself for him speeding up and pounding me harder than ever before... )"

    scene dad_brother_dp2_clothes_off_fast
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd trembling at left_small
    x "(Dad suddenly yanks my body down hard against his chest. His hands grip my waist like iron and he starts slamming up into me from below with brutal force.)"
    show madd distressed at left_small
    x "(The sound of skin clapping against skin gets louder and wetter. Every thrust makes this nasty, loud smack that fills the whole room.)"
    show madd violated at left_small
    x "(My moans are getting higher and more desperate. I can't control them anymore. They keep spilling out louder every time he pounds up into me.)"
    show madd broken at left_small
    x "(He's fucking me so hard from underneath that my whole body is shaking. I can feel him hitting deeper than before, like he's punishing me for opening my mouth.)"
    show brother sadistic at right_small
    brother_says "Damn dad, you're really going at it. Look at her body shaking like crazy. "
    hide brother
    show dad cruel at right_small
    dad_says "Bitch should learn to keep her mouth shut if she doesn't want to get fucked like this. "
    show madd broken at left_small
    x "(Every word added to the humiliation , my whole body was convulsing with every brutal thrust. I was completely at their mercy )"

    scene dad_brother_dp2_clothes_off_fast_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd violated at left_small
    x "(Dad suddenly yanks me even closer. My tits are now smashed flat against his chest, rubbing and sliding with every brutal thrust. My stomach is pressed tight against his.)"
    show madd paralyzed at left_small
    x "(I'm completely trapped. My stepdad in front and my stepbrother behind me... their hot, sweaty bodies surrounding me like quicksand made of family filth. I can't move. I can't breathe. I can't escape.)"
    show madd conflicted at left_small
    x "(As i come to the realization that everything around me was surrounded by my brother and dad , my pussy and asshole both start throbbing on their own. I hate it. I hate how my body is betraying me in front of them.)"
    show dad mocking at right_small
    dad_says "Look at that shit. Her greedy holes are twitching like crazy. You really love being our family cumdump that much, don't you?"
    hide dad
    show brother mocking at right_small
    brother_says "Haha fuck, her asshole is pulsing around my dick like it's begging for more. She's such a nasty little slut "
    show madd self loathing at left_small
    x "(They're both laughing at me... mocking me while my body keeps throbbing and moaning like it actually wants this. I wish i was born without a body so i wouldn't have to deal with these disgusting sensations.)"

    scene dad_brother_dp2_clothes_off_fast_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    x "(Dad's fat, sweaty body is pressed so tight against mine now. His hot sweat is seeping straight into my skin, mixing with mine. I can feel it soaking into me... like something inside me is starting to change.)"
    show madd conflicted at left_small
    x "(It's getting harder to think straight. His sweat, his smell, his body heat... it's like he's marking me from the outside in. I hate how warm it feels. Like being covered in his filth is making me part of him. I want to fight it but my body is betraying me, craving more of him )"
    show dad authoritative at right_small
    dad_says "See son, Always treat women like they are beneath you. They can act all smart and moral, but once you start pounding them hard enough, they hit factory reset."    
    show dad dominant at right_small
    dad_says "Just few days ago, this bitch was trying to lecture me about how I should respect her mom. Now look at her... she's nothing but a filthy little family toy for me and you to share. "
    hide dad
    show brother condescending at right_small
    brother_says "You're right, dad. I used to think Maddie was all innocent and quiet... but seeing you break her and hearing her moan like a bitch changed my mind completely."
    show madd broken at left_small
    x "(Their words are like knives cutting through me. Cuz they're right. I did hit factory reset after they started pounding me. After they forgot that I was a human being and just treated me like a toy.)"
    show madd self loathing at left_small
    x "(And the worst part is that my life got better after that. )"
    show madd horrified at left_small
    x "(But why the fuck are they having family bonding time over my body.  Father and son having a little talk about how to treat women... while they're both balls-deep inside me.How is this even real?)" 

    scene dad_brother_dp2_clothes_off_fast_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    x "(Brother suddenly grabs my shoulder and yanks me backwards hard against his chest. His dick slams even deeper inside my tits with the sudden pull.)"
    show brother dominant at right_small
    brother_says "Look at me riding this horse, dad. She's taking it so deep now."
    hide brother
    show dad sadistic at right_small
    dad_says "Then look at me milk this cow. Watch how I make her udders bounce."
    show madd violated at left_small
    x "(Dad immediately starts lunging forward again, catching my bouncing tits in his mouth. Every time he catches one he bites down hard on my nipple like before... sharp pain shooting through me while brother keeps pulling me back.)"
    show madd distressed at left_small
    x "(They're literally playing tug of war with my body. Brother yanking me back to bury himself deeper in my ass, dad pulling me forward to bite and suck on my tits. I'm just a toy being fought over between them.)"
    show madd horrified at left_small
    x "(Being called a horse and a cow... reduced to nothing but holes and tits for them to use and laugh about. The humiliation is making my head spin.)"
    
    scene dad_brother_dp2_clothes_off_fast_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd disgusted at left_small
    x "(I suddenly hear brother making that wet sound in his mouth... stirring up spit. Then I feel it — hot, thick, viscous fluid landing on my back near my shoulders. It's his saliva. I can feel it slowly sliding down my skin.)"
    show madd horrified at left_small
    x "(The disgust hits me hard. He's spitting on me like I'm a nonentity. Like I'm just a piece of meat for him to use and degrade. I want to wipe it off but I can't move. )"
    show brother perverted at right_small
    brother_says "I'm gonna drown you in my fluids, Maddie. Piss, cum, saliva... every single drop is going inside you. You're gonna be full of me."
    show madd self loathing at left_small
    x "(The second he says that my pussy and asshole both twitch hard. My body pulls them deeper on its own... like it's welcoming them. Thanking them. I hate it. I hate how my body is begging for more of their filth.)"  
    show madd broken at left_small
    x "(Brother keeps spitting on me more and more, his saliva sliding down my back and soaking into my skin. And with every spit, my body keeps betraying me, craving more of it. )"
    hide brother
    show dad mocking at right_small
    dad_says "Look at that. The broken little whore is actually getting turned on by what you just said Adam. Her holes are twitching like crazy. I dont think she can live without being filled with our filth now. " 
    show madd self loathing at left_small
    x "(They're both laughing at me again. My own body just proved dad right by pulling them deeper the moment brother talked about filling me with piss and cum. I feel so fucking broken.)" 

    scene dad_brother_dp2_clothes_off_fast_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad debased at right_small
    dad_says "I'm getting real fucking sweaty now, Maddie. I can feel my thick, hot ass sweat clinging to my hairy ass crack, all musky and ripe from hours trapped in my pants."
    show dad perverted at right_small
    dad_says "Don't you worry though — after we finish stretching both your holes , I'm gonna make you bury your pretty face deep between my fat cheeks and lick every single drop of your dad' ass sweat straight from the source."
    dad_says "And after that, you're gonna shove that tongue of yours all the way inside my asshole and play a little guessing game... tell me exactly what I ate for dinner last night while you taste it all on your tongue."  
    show madd nauseated at left_small
    x "(My stomach twists so hard I almost gag. It's so fucking twisted and degrading I feel like I'm going to break.)"  
    show madd inheat at left_small
    x "(I imagined myself licking his sweaty, musky ass crack... then sticking my tongue all the way inside his asshole to taste it... and my pussy betrays me worse than ever. It throbs violently the second i thought it, pulling both their dicks deeper on its own like it's begging for them to never leave. I hate how much my body wants this sick shit. I hate that I'm getting wetter just imagining licking my stepdad's ass sweat and tonguing his asshole)"
    show dad mocking at right_small
    dad_says "Haha look at that. Her greedy little pussy is throbbing like crazy just from hearing about licking her stepdad's dirty ass. What a nasty family whore."
    hide dad
    show brother mocking at right_small
    brother_says "Fuck, she's really gone. Her body is begging for it now."
    show madd self loathing at left_small
    x "(I am truly a lost cause. My body is completely broken and addicted to their filth. )"

    scene dad_brother_dp2_clothes_off_fast_7
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    x "(Brother suddenly reaches up and grabs the back of my head, squeezing my face hard between his fingers. His grip is tight and possessive.)"
    show brother possessive at right_small
    brother_says "We own you, Maddie. Every single fucking inch of you. Your holes, your body, your mind... all of it belongs to us now. And you're gonna learn to find real joy in submitting to your dad and brother. You're gonna love being our filthy little family toy."
    show madd violated at left_small
    x "(Dad's hands immediately grab my tits and squeeze them hard, fingers digging into the soft flesh while brother keeps my face trapped. They're both holding me like property.)"
    show madd trembling at left_small
    x "(Meanwhile i continued to moan and squirm between them augmenting their believes that I'm loving this. )"

    scene dad_brother_dp2_clothes_off_fast_8
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    x "(Brother suddenly yanks my hair hard from behind, pulling my head back sharply while dad keeps squeezing my tits.)"
    show madd violated at left_small
    x "(Dad immediately starts slapping my breasts — hard, stinging slaps that make them bounce and burn. Every slap sends a sharp jolt through my chest while brother keeps my head pulled back.)"

    scene dad_brother_dp2_clothes_off_fast_9
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    x "(The hard, rough sound of my ass cheeks getting clapped fills the room with every brutal thrust. It's loud, wet, and nasty which gets interrupted by dad finally accepting his son)"
    show dad authoritative at right_small
    dad_says "You finally grew into the man I wanted you to be, Adam. Ruthless. Dominant. I'm proud of you, son."
    show dad dominant at right_small
    dad_says "First child with Maddie is gonna be mine though. But after I put my first one in her, I'll let you have a turn and breed her too. We'll take turns knocking her up until she's delivering our babies every nine months. She's gonna be a breeding machine for our family."
    hide dad
    show brother shocked at right_small
    brother_says "Wait... are you serious, dad? "
    hide brother
    show dad possessive at right_small
    dad_says "Dead serious, son. She's got a fertile little womb just begging to be filled. I'll pump the first baby into her, then once she's carrying my kid, you can have your turn and put one in her too. We'll share her properly like a real family should."
    hide dad
    show brother amused at right_small
    brother_says "Wow... I never thought you'd share her like that, dad. Thanks, I really appreciate it. I want to have kids with her too, but I didn't want to step on your toes. "
    hide brother
    show dad wistful at right_small
    dad_says " I know your life has been hard, Adam. Losing your mom, not getting any romantic experience... I want to give you the chance to have a family of your own. And Maddie is perfect for that. "
    hide dad
    show brother serious at right_small
    brother_says "Thanks, dad. for understanding. I wont let you down. "
    show madd horrified at left_small
    x "(They're really doing it. Having a full father-son  moment while both their dick are buried inside me. Talking about who gets to breed me first like I'm just a breeding sow for the family. And they didn't ask me. Not once. Not even a single question about what I want.)"
    show madd violated at left_small
    x "(My dad just decided he's putting the first baby in me... and then he'll let his son have a turn. They're planning my entire future like I'm not even a person. Just holes to be filled and wombs to be used. I feel so fucking doomed.)"
    show madd traumatized at left_small
    x "(how did my life come to this? Ever since mom died, I've been trapped in this nightmare. )"

    scene dad_brother_dp2_clothes_off_fast_10
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    x "(They don't even slow down. But I can't stop thinking about what they just said. My stepdad deciding he's putting the first baby in me... then letting his son have a turn. )"
    show madd broken at left_small
    x "(this sounds like a never-ending cycle . I will be pregnant with one of them, then the other, then the first one again... over and over until I'm just a walking baby factory for them. )"
    show madd traumatized at left_small
    x "(Knowing him , after 18 years when my son grows up, dad will probably let him have a turn too. I would literally be the backbone of the entire lineage. )"
    show madd conflicted at left_small
    x "(Regardless of how disgusting and dehumanizing it was to even think about, some twisted part of me  couldn't help but feel a twisted sense of pride. Like maybe this was my purpose in life after all. )"    

    scene dad_brother_dp2_clothes_off_fast_11
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    x "(My thoughts were interrupted by dad suddenly yanking my elbows using it as pivot to pull his ass upwards and slam even deeper into me. )"
    show dad lustful at right_small
    dad_says "That's right, ah this feels soo good. Like i am 20 years younger again. I could fuck you like this all day, Maddie. "
    show dad perverted at right_small
    dad_says "Once Maddie pops out one of my kids and then one of yours, Adam, we should try double vaginal. Both of us cumming inside her at the exact same time. See whose baby it ends up being. Like a fucked up Russian roulette."
    hide dad
    show brother amused at right_small
    brother_says "Haha fuck, that's actually genius, dad. I'm down."
    show madd broken at left_small
    x "(They're laughing about it now. Talking about double vaginal and cumming inside me together like it's some kind of sick game to see who knocks me up first. I'm just a breeding experiment to them.)"

    scene dad_brother_dp2_clothes_off_fast_12
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    x "(Brother suddenly grabs my hair with both hands and yanks my head back hard, using it like a handle while he keeps pounding into me from behind.)"
    show brother perverted at right_small
    brother_says "Dad, I've always wanted to carry Maddie upside down on my shoulder with her face buried deep between my legs, her nose pressed right against my sweaty balls."
    show brother debased at right_small
    brother_says " Walk around the park all hot and dripping so everyone can see this whore of a sister sniffing her own brother's ball sweat like the desperate little family slut she is. I want the whole world to watch her tongue hanging out, licking my nuts in public while I show them what a broken toy she became affter dreaming of being an engineer "
    show madd horrified at left_small
    x "(The image is so fucking disturbing I almost stop breathing. Him carrying me upside down in the middle of the park, my face smashed into his sweaty crotch, everyone staring at his shorts wondering what i was doing there while I sniff and lick his balls like some kind of public pet. The thought makes me feel so small and filthy I want to cry.)"
    show madd self loathing at left_small
    x "(And the worst part is... my body is still moaning and throbbing around their dicks like it's excited by the idea. I really am completely broken.)"
    show madd broken at left_small
    x "(This is what they've turned me into. A public display of their ownership. And there's nothing I can do to stop it. Not anymore.)"

    scene dad_brother_dp2_clothes_off_fast_13
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad perverted at right_small
    dad_says "You know what, Adam? We can try something like that tonight. After we're done fucking her and she finishes cleaning both our butts with her tongue, you can sleep on top of her in a 69 position."
    show dad debased at right_small
    dad_says " Your dick stuffed deep in her mouth the whole night while your sweaty balls rest right on her nose. Let her breathe nothing but your ball musk until morning."
    hide dad
    show brother lustful at right_small
    brother_says "That's actually a really good idea, dad. I like it. I would love to sleep on top of her like that. I want to feel her mouth wrapped around my dick all night "
    show brother think at right_small
    brother_says "Wait... where would you sleep then?"
    hide brother
    show dad dominant at right_small
    dad_says "The room's gonna reek like crazy after we're done with her. I'll just sleep on the living room sofa. You two enjoy your little brother sister time."
    hide dad
    show brother serious at right_small
    brother_says "Thanks again, dad. I really appreciate it."
    show madd horrified at left_small
    x "(They're actually planning this. After they finish using me, my stepbrother is going to sleep on top of me with his dick buried in my mouth and his sweaty balls pressed directly against my nose the entire night. I'll be forced to breathe nothing but his thick, musky ball sweat for hours straight.)"
    show madd traumatized at left_small
    x "(My lungs will be full of nothing but his ball sweat. Every breath I take will smell like his dirty, unwashed nuts. And even after he wakes up and pulls out, I probably won't be able to smell anything else for hours. His scent will be stuck inside me.)"
    show madd broken at left_small
    x "(The thought of waking up with my mouth full of his soft cock and my nose buried in his sweaty balls... it's so fucking disgusting and dehumanizing I feel like I'm going to break. And the worst part is my body still wants this nightmare to happen.)"

    scene dad_brother_dp2_clothes_off_fast_14
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show brother leering at right_small
    brother_says "What about you, dad? Don't you wanna do something like this too?"
    hide brother
    show dad perverted at right_small
    dad_says "Nah, I prefer when her tongue is buried deep inside my asshole. But maybe tomorrow I'll make her my personal seat. Sit her right under my chair while I do Zoom meetings from morning till afternoon."
    show dad debased at right_small
    dad_says " My asshole will swallow her nose and let it marinate in there for hours, soaking up all my sweat and musk before I make her shove that tongue deep inside and do the same thing."
    hide dad
    show brother mocking at right_small
    brother_says " That's actually hilarious, dad. She'd be stuck under your chair like a human cushion. totally deserved for what she's become. "
    show madd horrified at left_small
    x "(They're both laughing now. My stepdad just casually decided he's going to use me as his personal chair for hours tomorrow while he works. My nose and tongue both cooked in the heat of the inside of his asshole. And I know... I know this is really going to happen to me.)"
    show madd violated at left_small
    x "(I can't even imagine how bad it's going to smell. His asshole is probably the dirtiest, sweatiest part of his body. My nose is going to be buried in there for hours while he works )"

    scene dad_brother_dp2_clothes_off_fast_15
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad debased at right_small
    dad_says "My ass cheeks are so fucking wet from all this sweat it feels like I just had a full-on diarrhea explosion back there. The crack is soaked, sticky, and I can tell it probably reeks like hell."
    show dad dominant at right_small
    dad_says " Daughter you definitely need  to clean every inch of it with your tongue before I can even think about doing anything else."
    show dad perverted at right_small
    dad_says "I can just tell its so much sweat your tongue is gonna get so tired and numb licking up all it. You're gonna be down there for a long time, tongue buried deep in my crack, licking up every drop of that thick sticky filth until your mouth is full of my ass taste. I want you to really work for it."
    show madd resigned at left_small
    x "(I was just numb at this point. No point in thinking anything anymore. Just waiting for them to finish with me and then I'll have to deal with the aftermath. )"
    show dad lustful at right_small
    dad_says "Fuck..I am close to cumming again. I can feel it building up inside me. I'm gonna impregnate this fertile little whore so hard. "
    show madd violated at left_small
    x "(They had already came in me twice before even removing my shirt...This would be the 3rd load of their semen filling me up. I was already so full of them )"
    show madd traumatized at left_small
    x "(if the last two didnt knock me up, this one definitely will. )"
    hide dad
    show brother sadistic at right_small
    brother_says "Damn dad, you're really going to wreck her. I'm gonna cum too , lets do it together for the 3rd time."
    show madd resigned at left_small
    x "(I gritted my teeth and braced myself for what comes next , my mind divided between what was worst? The fact that their pounding will finally end or the fact that I have to clean their butts with my tongue after they fill me up with their cum. )"

    scene dad_brother_dp2_clothes_off_fast_16
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd violated at left_small
    x "(Dad suddenly wraps both his hands around my waist like iron and starts pounding up into me even faster and harder than before. His hips are slamming against me with brutal force.)"
    show madd traumatized at left_small
    x "(Then I feel it — hot, thick cum flooding my pussy and asshole at the exact same time. Both of them are cumming inside me together. The wet, sloppy sound in the room changes completely. It's now loud, nasty squelching  as they keep thrusting even while they're still pumping their loads into me. I can feel their cum mixing inside me, making disgusting wet noises with every thrust.)"
    show madd broken at left_small
    x "(They're still fucking me while cumming. Their dicks are pushing their own semen deeper into my holes, creating this thick, creamy sloshing sound that fills the entire room. It's so fucking nasty and degrading I want to disappear.)"  
    show madd disgusted at left_small
    x "(As if they are stirring up a pot of soup inside me. I can feel it dripping out of me with every movement, making this nasty, wet sound that echoes around the walls.)" 
    show dad smirk at right_small
    dad_says "Fuuuuck... I'm finally done. That was a great evening. You were perfect tonight, Maddie."
    hide dad
    show brother smirk at right_small
    brother_says "Yeah, dad... best night ever. She took it so well."
    show madd violated at left_small
    x "(They finally stop moving but stay buried inside me, their sweaty bodies still pressed against mine. I can feel more of their hot sweat seeping into my skin, mixing with their cum that's leaking out of me. My stepdad's fat, sweaty chest is glued to my tits, my stepbrother's stomach pressed against my back. I'm completely covered in their filth.)"
    show madd resigned at left_small
    x "(And i know its far from over. I know they're just taking a break before I am made to clean their butts with my tongue. )"
    show madd broken at left_small
    x "(My vision is starting to go blurry, i feel like I'm going to pass out. My body is so overwhelmed with the sensations of being filled with their cum and covered in their sweat that I can't think straight anymore. )"
    hide brother
    show dad angry at right_small
    dad_says "Dont you dare...pass out on me, Maddie. I want you to stay awake till i wipe my ass sweat all over your face and tongue. "
    show madd weeping at left_small
    x "I...am soo...tired...dad..."
    show dad cruel at right_small
    dad_says "No, you need to stay awake. I want to see the look on your face when I rub my sweaty ass all over your pretty face. "
    show madd broken at left_small
    x "(I was so exhausted and overwhelmed I couldnt keep my eyes open. )"

    scene black 
    with dissolve
    show dad smirk at right_small
    dad_says "Damn...bitch is out cold. "
    show dad dominant at right_small
    dad_says "Well, here's a lesson son. Even when she's asleep, she's still our property. I'm gonna rub my sweaty ass all over her face regardless of whether she's awake or not. "
    hide dad
    show brother shocked at right_small
    brother_says "Whoa, dad... that's pretty hardcore. I mean, I know she's our property and all, but rubbing your ass on her face while she's asleep? That's next level."
    hide brother
    show dad mocking at right_small
    dad_says "Yeah, Too much work balancing myself on her face. Will just smear my ass sweat all over her face instead. "
    show madd resigned at left_small
    x "(I heard some rustling sounds , i figured it was him scratching his ass with his hands before the inevitable)"

    scene maddie_face_after_dp2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd traumatized at left_small
    x "(I laid there for a while, completely unconscious. Knowing full well any minute now, my dad is gonna clean his hands on my face which he had used to scratch his sweaty, musky ass. )"
    show madd resigned at left_small
    x "(It turned out to be much worst than I expected. )"

    scene maddie_face_after_dp2_dad_hands_on_face
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    x "(Suddenly i felt it — his hot, sweaty hands directly next to my lips trying to enter my mouth. I could smell the strong scent of his ass sweat on his hands )"
    show madd disgusted at left_small
    x "(I can taste it too... just a little. The salty, bitter, dirty taste of his ass sweat transferring from his fingers onto my lips. It's so fucking gross but I can't even move my head away.)"
    show madd paralyzed at left_small
    x "(His fingers are pushing a little more now, trying to slip inside my mouth. I can feel the sweat from his ass crack all over them. The same fingers that were scratching his hairy, sweaty hole just moments ago.)"
    show madd horrified at left_small
    x "(The smell is getting stronger the closer they get. That deep, pungent, unwashed ass musk that belongs only to my stepdad. And now it's all over my lips and starting to enter my mouth.)"

    scene maddie_face_after_dp2_dad_fingers_in_mouth
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd violated at left_small
    x "(Now his fingers slipped fully inside my mouth. I can feel the thick, sticky sweat from his ass crack coating my tongue and the inside of my cheeks. The taste wasnt any different than the smell. Just a salty, bitter, musky taste that makes me want to gag.)"
    show madd self loathing at left_small
    x "(The only part that made it bad was that i knew it was my dads ass sweat. The knowledge of where the taste and smell was coming from made it so much worse. )"
    show dad dominant at right_small
    dad_says "That's it , eat it all up, Maddie. I want you to savor the taste of my ass sweat. I can wait till tomorrow to have your tongue inside my asshole, until then here, have a little taste of it on my fingers. "
    show madd violated at left_small
    x "(He would force his fingers deep in my mouth like this for a while, making me taste his ass sweat and smell it on my tongue. Then he would pull them out and wipe them on my face)"
    show madd broken at left_small
    x "(Then i would hear the rustling sound of him scratching his ass again, before he would put his fingers back in my mouth to taste more of his sweat. This cycle would repeat for a few minutes until he was done with me.)"
    show dad smirk at right_small
    dad_says  "Now it feels my ass is drying up. I think I'm done with you for today, Maddie. Alright Adam, you can sleep on top of her tonight like we planned. "
    hide dad
    show brother lustful at right_small
    brother_says "Thanks, dad. I really appreciate it. I can't wait to sleep on top of her tonight with my cock in her mouth and my balls on her nose. It's gonna be so hot."
    show madd resigned at left_small
    x "(finally he pulled his fingers out of my mouth and wiped them on my face one last time before leaving me there like a filthy mess. I heard the door close and i assume that he had went out)"
    
    scene maddie_face_after_dp2_alone_with_brother
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    x "(I was now alone with my brother. Oh god, I know what's coming next. It would be so much easier if I was just completely knocked out right now. I just want to sleep and forget about everything.)"
    show brother serious at right_small
    brother_says "I know you might be knocked out and all, but I just want to say... I'm really sorry for everything, Maddie. I know this is all really messed up and I wish things were different. "
    show brother dominant at right_small
    brother_says "That was genuinely how i felt before Dad allowed me to have a turn with you. I guess i am team dad now."
    show brother condescending at right_small
    brother_says "I helped you with so many things , but you never showed any appreciation for it. Thanks to dad he showed me how women really work and now i can finally understand you. "
    show brother lustful at right_small
    brother_says "Tonight is the night i stop being the nice brother and start being the dominant man I was always meant to be. And it starts with keeping my cock buried deep in your mouth while I sleep on top of you. I want to feel your tongue wrapped around my cock all night while my sweaty balls rest right on your nose. "
    show madd distressed at left_small
    x "(As he said that i heard bed creaking sounds near me, and I knew he was climbing on top of me. )"

    scene maddie_face_after_dp2_brother_on_top
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd violated at left_small
    x "(I felt his cock directly pressing against my lips. I can smell the strong scent of his sweaty balls right on my face.)"
    show madd disgusted at left_small
    x "(His dick parted my lips and slipped inside my mouth. As he starts roughly thrusting into my mouth )"
    show madd nauseated at left_small
    x "(It  was the taste of his dick which had been burried in my asshole for god knows how many hours. He came inside my asshole twice and his dick still remained inside me, which was evident by the strong smell of cum and sweat on his penis. )"
    show madd horrified at left_small
    x "(What the hell , you already came 3 times today... and now you're still going to use my mouth like this? )"
    show madd broken at left_small
    x "(the sound of my saliva mixing with the sweat and cum on his cock was so nasty and humiliating. it was like a person drowning in the smallest puddle of filth, trying to breathe but only getting more and more of it in their mouth. )"

    scene maddie_face_after_dp2_brother_on_top_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd violated at left_small
    x "(He continued face fucking me for a while , then played with my tits with his free hands. He squeezed them hard, fingers digging into the soft flesh)"
    show madd distressed at left_small
    x "(Fortunaltely my involuntary muscles were still working or i would have suffocated by now. His precum and whatever else he had on his cock was making my mouth overflow with nasty fluids. )"
    show brother mocking at right_small
    brother_says "You sound so obscene dear sister. Even when you're asleep, you're still moaning like a filthy whore. Guess you got it from your mom huh?"
    show madd sad at left_small
    x "( More than any abuse they throw at me, for some reason these kinds of comments about my mom always hit me the hardest.)"
    show brother smirk at right_small
    brother_says "Sheesh, I am tired too now...Perhaps its time to call it a day."

    scene maddie_face_after_dp2_brother_on_top_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd paralyzed at left_small
    x "(I felt his weight drop on me completely now. His sweaty balls pressed against my nose, his fat belly resting on my chest while his dick stayed buried deep in my mouth. I was completely trapped under him, suffocating in his filth.)"
    show madd resigned at left_small
    x "(His knees were on either side of my head, keeping me completely still . He stopped moving his hips but kept his dick buried deep in my mouth. I could feel the heat radiating from his body, the strong scent of his sweaty balls filling my nostrils.)"
    show madd broken at left_small
    x "(Is this gonna be how I sleep from now on? How long is this going to last? Its hard to even sleep like this. )"
    show brother smirk at right_small
    brother_says "Goodnight, Maddie. Sleep tight. "
    show madd broken at left_small
    x "(His last words as he drops all of his weight on me as my vision goes completely black from directly under his balls)"

    scene black 
    with dissolve
    show madd traumatized at left_small
    x "(I had no choice but to taste his dick and smell his sweaty balls all night long... )"

    # ── DAD stats: vaginal sex ×3 + creampies + DP2 scene ────────────────────────
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["vaginal_sex"] += 3
    $ character_relations["dad"]["vaginal_creampie"] += 3
    $ character_relations["dad"]["intimacy"] +=11
    $ character_relations["dad"]["lust"] = 0
    $ character_relations["dad"]["dominance"] = min(character_relations["dad"]["dominance"] + 10, 100)
    $ character_relations["dad"]["anger"] = 0
    # ── BROTHER stats: anal sex ×3 + creampies + oral (sleeping) ─────────────────
    $ character_relations["brother"]["groped_madd"] += 1
    $ character_relations["brother"]["undressed_madd"] += 1
    $ character_relations["brother"]["touched_madd"] += 1
    $ character_relations["brother"]["anal_sex"] += 3
    $ character_relations["brother"]["anal_creampie"] += 3
    $ character_relations["brother"]["oral_sex"] += 1
    $ character_relations["brother"]["intimacy"] +=11
    $ character_relations["brother"]["lust"] = 0
    $ character_relations["brother"]["dominance"] = min(character_relations["brother"]["dominance"] + 10, 100)
    $ character_relations["brother"]["anger"] = 0
    # ── Global stats ─────────────────────────────────────────────────────────────
    $ madd_willpower = max(madd_willpower - 40, 0)
    $ madd_is_virgin = False
    $ wake_up_after_sex = "dp"
    $ number_of_people_had_sex_with_before_sleeping = 2
    $ journal_event_set_done("Dad", "Dragged to Dad's Room (DP2)")

    jump madd_wake_up_after_roughed_up_3





