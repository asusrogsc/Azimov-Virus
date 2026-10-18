label outside_home:
    python:
        if game_time.is_morning():
            outside_bg = "madd_home_from_outside_morning"
        elif game_time.is_afternoon():
            outside_bg = "madd_home_from_outside_afternoon"
        elif game_time.is_evening():
            outside_bg = "madd_home_from_outside_evening"
        else:  # night
            outside_bg = "madd_home_from_outside_night"

    if "home_main_door" in locked_home_areas:
        p "(The main door is locked. I can't go outside.)"
        jump home_areas

    scene expression outside_bg
    with fade

    p "(Je suis maintenant à l'extérieur de chez moi. Je peux voir d'autres quartiers et des endroits à explorer.)"

    menu:
        "Maison du voisin":
            call advance_time_and_check(minutes=1) 
            jump neighbors_house_scene

        "Pharmacie" if pharmacy_available:
            call advance_time_and_check(minutes=1) 
            jump pharmacy_near_home

        "Parc":
            if game_time.hour == 10 and game_time.minute <= 20:
                jump parklindsandrocky
            elif game_time.hour == 15 and game_time.minute <= 30:
                jump rocky_talk
            elif game_time.hour == 15 and convrocky == 2 and savemzelle == 0 and game_time.minute == 30 and game_time.day != "Tuesday":
                jump rocky_tier2
            else:
                call advance_time_and_check(minutes=1) 
                jump home_park_scene
        
        "Consultez le panneau d'affichage du quartier.":
            call advance_time_and_check(minutes=1) 
            jump notice_board_scene
        "Run away from home" if (paid_school_fees and got_male_clothes):
            call advance_time_and_check(minutes=1) 
            jump running_away_from_home


        "Retournez à l'intérieur de la maison":
            call advance_time_and_check(minutes=1)
            jump home_areas



label neighbors_house_scene:
    if 20 <= game_time.hour <= 22:
        jump damon_working_on_car_night_scene

    python:
        if game_time.is_morning():
            neighbor_bg = "neighbor_house_morning"
        elif game_time.is_afternoon():
            neighbor_bg = "neighbor_house_afternoon"
        elif game_time.is_evening():
            neighbor_bg = "neighbor_house_evening"
        else:  # night
            neighbor_bg = "neighbor_house_night"

    scene expression neighbor_bg
    with fade
    p "(Je suis chez mon voisin. Je vois son jardin et sa vieille voiture rouillée… beurk, qui voudrait conduire ça ?)"

    menu:
        "Frappez à leur porte":
            x "(I dont know them that well ..)"
            x "(Maybe version 0.04)"
            call advance_time_and_check(minutes=1) 
            jump neighbors_house_scene


        "Retournez dehors.":
            call advance_time_and_check(minutes=1) 
            jump outside_home
        "Aller au Parc":
            call advance_time_and_check(minutes=1) 
            jump home_park_scene


label damon_working_on_car_night_scene:
    scene neighbor_house_night_damon_working_on_car
    with fade   

    if "damon" in contacts_met:
        x "(I see Damon working on his car.)"
    else:
        x "(I see an old man working on a rusty old car, perhaps trying to fix that piece of junk.)"

    menu:
        "Talk to old man":
            call advance_time_and_check(minutes=1) 
            jump talk_to_damon_working_on_car_night_scene
        "Go back outside the house":
            call advance_time_and_check(minutes=1) 
            jump outside_home



label notice_board_scene:
    python:
        if game_time.is_morning():
            notice_board_bg = "outside_home_notice_board_morning_afternoon"
        elif game_time.is_afternoon():
            notice_board_bg = "outside_home_notice_board_morning_afternoon"
        elif game_time.is_evening():
            notice_board_bg = "outside_home_notice_board_evening"
        else:  # night
            notice_board_bg = "outside_home_notice_board_night"

    scene expression notice_board_bg
    with fade

    if game_time.is_night() or game_time.is_evening() :
        show madd think at left_small
        with dissolve
        x "(I am at the notice board, but it is pitch dark out here. I can barely make out the shapes of the flyers.)"
        show madd resigned at left_small
        with dissolve
        x "(I can't read anything in this darkness. I'll have to come back during the day.)"
        hide madd resigned
        jump outside_home

    x "(I am now at the neighborhood notice board. I can see various flyers and announcements.)"

    menu:
        "Read the flyers related to the neighborhood":
            call advance_time_and_check(minutes=1) 
            jump read_flyers_scene
        
        "Read mom's obituary":
            if mom_obitiary_read>=1:
                jump read_mom_obituary_2
            call advance_time_and_check(minutes=1) 
            jump Read_mom_obituary_scene

        "Read about the pharamcy nearby":
            call advance_time_and_check(minutes=1) 
            $ pharmacy_available=True
            x "(I read the flyer about the pharmacy. It mentions that they have a variety of medications and some over-the-counter products. It also mentions that they are closed at night)"
            x "(Perhaps i can buy something from there to help with my stress or sleep issues)"
            jump notice_board_scene


        "Go back outside the house":
            call advance_time_and_check(minutes=1) 
            jump outside_home


label Read_mom_obituary_scene:
    $mom_obitiary_read+=1
    scene scene_notice_board_mom_obituary
    with fade
    show madd sad at left_small
    x "(I see the flyer with mom's obituary. It has her picture and some details about her life and family)"
    show madd depressed at left_small
    x "(Just looking at it makes me feel a mix of emotions. )"
    show madd trembling at left_small
    x "(I touch the flyer as if trying to connect with her )"
    show madd self loathing at left_small
    x "I am sorry mom.... Im sorry i wasnt there for you when you needed me the most"
    
    
    show madd think at left_small
    x "(Memories flood my mind)"

    scene black 
    with fade
    show madd sad at left_small
    x "( I remember the time after dad died i was so lost and hopeless, but mom was there for me)"

    scene scene_notice_board_mom_obituary_memories_funeral
    with fade
    show madd sad at left_small
    x "(It was as if she took on the role of both parents and i never realized how much she sacrificed for me)"
    show madd think at left_small
    x "(She assured me that everything would be okay and i never knew how hard it was for her to keep it together for my sake)"

    scene black 
    with fade
    show madd think at left_small
    x "(I remember how she would always take care of my health ,only cooking healthy meals and making sure i was eating well)"

    scene scene_notice_board_mom_obituary_memories_cooking_noodles
    with fade
    show madd conflicted at left_small
    x "(But sometimes she would let me have my noodles , once a month as a treat, and i would always look forward to those days)"
    show madd self loathing at left_small
    x "(When she used to say no to noodles i thought she was being mean, but now i understand she was just trying to take care of me in her own way)"

    scene scene_notice_board_mom_obituary_memories_eating_noodles_1
    with fade
    show madd think at left_small
    x "(I would start stealing noodles from the pantry and eating them in secret )"
    show madd conflicted at left_small
    x "(But she would always catch me while i was on my computer and scold me for eating too many noodles )"

    scene scene_notice_board_mom_obituary_memories_eating_noodles_2
    with fade
    show madd think at left_small
    x "(But i would never listen )"
    show madd conflicted at left_small
    x "(For some reason there was always a mischevious part of me that wanted to get caught and scolded by her for eating noodles )"

    scene scene_notice_board_mom_obituary_memories_eating_noodles_3
    with fade
    show madd think at left_small
    x "(I would always get caught and scolded but i still did it again and again )"
    show madd sad at left_small
    x "(I guess i liked the attention and the way she would care for me even when i was being bad )"

    scene black
    with fade
    show madd worried at left_small
    x "(THen she got married to stepdad and things changed a lot .)"
    show madd disgusted at left_small
    x "(I heard her sexual moans from their room and loud bed creaking sounds and i felt so uncomfortable and awkward hearing those sounds )"
    
    scene scene_notice_board_mom_obituary_memories_eating_noodles_moaning_sounds
    with fade
    show madd disgusted at left_small
    x "(Those sounds came even from stepbrother's room and i knew she was banging him too and i felt so disgusted and betrayed by her actions )"
    show madd angry at left_small
    x "(I never confronted her about it but i always felt so hurt and betrayed by her actions well at least now i can eat noodles without feeling guilty about it )"
    show madd depressed at left_small
    x "(But i guess what felt worst was that i was the only one mourning dad now and it seemed like she didnt care about him at all anymore )"
    show madd shaken at left_small
    x "(I didnt know she was sleeping with stepdad and stepbrother just to earn money to support my future and i was so devastated )"

    scene black 
    with fade
    x "(she kept trying to talk to me but i was so angry at her i didnt listen at all)"
    

    scene scene_notice_board_mom_obituary_memories_mom_tries_to_talk_to_madd
    with fade
    show madd angry at left_small
    x "(One night she came to my room to talk to me but i was playing games and i was too angry at her to pause my game )"
    show madd horrified at left_small
    x "(I saw her bruised body and i thought that's what she gets for sleeping with those two guys )"
    show madd angry at left_small
    x "(She was repeatedly saying how i am the only one she has and only one she can talk to but i didnt listen )"
    show madd distressed at left_small
    x "(she kept trying to talk but i confronted her about her not caring about dad and that i can hear her moans of pleasure every night)"

    scene scene_notice_board_mom_obituary_memories_mom_tries_to_talk_to_madd_2
    with fade
    show madd angry at left_small
    x "(I even made fun of her painful moans saying that they didnt sound moans of endurance but more like moans of pleasure)"
    show madd distressed at left_small
    x "(She insisted that she was doing all of this for me and that she was trying to support me and give me a better future but i didnt care at that point )"
    show madd angry at left_small
    x "(Finally i told her to get out of my room )"
    show madd self loathing at left_small
    x "(That was the last time i ever talked to her )"

    scene scene_notice_board_mom_obituary_memories_madd_finds_mom_body_1
    with fade
    show madd think at left_small
    x "(Next morning i got out of my room after a gaming session and saw moms body lying on the floor )"
    show madd shocked at left_small
    x "(I joked to myself that she probably got drunk like usual and passed out on the floor but)"
    show madd horrified at left_small
    x "(Then i tried to wake her up but she was cold and stiff and i realized she wasnt moving )"

    scene scene_notice_board_mom_obituary_memories_madd_finds_mom_body_2
    with fade
    show madd shaken at left_small
    x "(Thats when i panicked, i started screaming and crying and i didnt know what to do )"
    show madd weeping at left_small
    x "(I called for help from someone...anyone...)"
    show madd distressed at left_small
    x "(thats when my emotions came pouring out...the grief, the guilt, the anger, the betrayal, the loneliness...)"
    show madd weeping at left_small
    x "(I apologised to mom for not being there for her ,  i promised to never touch noodles again if she woked up and i begged her to forgive me for being such a bad daughter )"
    show madd broken at left_small
    x "(But it was all for nothing...)"

    scene scene_notice_board_mom_obituary_memories_madd_finds_mom_body_3
    with fade
    show madd weeping at left_small
    x "(I kept screaming for help but none came , my brother and dad were both out of the house and i was all alone  )"
    show madd traumatized at left_small
    x "(In my emotional burst i ended up repeating the same words she had said to me earlier that night)"
    show madd weeping at left_small
    x "I have no one to talk to but you..."
    show madd self loathing at left_small
    x "(thats when i realized how similar our situations were and how much she was struggling with her own loneliness)"
    show madd distressed at left_small
    x "(She was selling her body to support me and give me a better future despite getting used by those two guys and i was treating her like garbage  )"
    show madd broken at left_small
    x "(I didnt even let her talk to me on her final day....)"
    show madd weeping at left_small
    x "(I kept begging  her to wake up but she never did ...)"

    scene black 
    with fade
    show madd broken at left_small
    x "(When the ambulance finally arrive she was already dead and i was left alone with the paramedics)"
    show madd traumatized at left_small
    x "(She had died from alcohol poisoning caused by her accute loneliness and despair )"
    show madd self loathing at left_small
    x "(She tried talking to me...but i pushed her away...)"
    show madd depressed at left_small
    x "(She did everything she could to support me after dad died...but i treated her like garbage...)"
    show madd weeping at left_small
    x "(I wish i could go back in time and talk to her one last time...to tell her that i love her and that im sorry for treating her like garbage...)"
    show madd broken at left_small
    x "(I wish i could...)"

    scene scene_notice_board_mom_obituary_memories_eating_noodles_after_mom_death
    with fade
    show madd depressed at left_small
    x "(I tried eating noodles again after mom's death)"
    show madd sad at left_small
    x "(I sat there in silence picking some noodles from the bowl and just staring at them)"
    show madd distressed at left_small
    x "(Hoping i'd hear her voice telling me to stop eating noodles)"
    show madd weeping at left_small
    x "(Hoping i'd feel her presence in the room again...)"
    show madd broken at left_small
    x "(But it never came...)"
    show madd self loathing at left_small
    x "(As i finally put the noodles in my mouth i felt a wave of guilt and sadness wash over me and threw away the noodles without even tasting them )"
    show madd depressed at left_small
    x "(I never tried noodles again after that day...)"

    hide madd

    $ journal_event_set_done("Madd", "Mom's Obituary")
    $ journal_event_show("Madd", "Dream: Mom's Last Night")
    $madd_willpower_max +=30 
    jump notice_board_scene




label read_mom_obituary_2:
    $mom_obitiary_read+=1
    scene expression Transform("images/Dream_sequence/scene_notice_board_mom_obituary.JPG", xysize=(1920, 1080))
    with fade

    show madd sad at left_small
    x "(I see the flyer with mom's obituary. It has her picture and some details about her life and family)"
    show madd hopeful at left_small
    x "(I will make sure to honor her memory and live a good life for her sake)"

    jump notice_board_scene



label talk_to_damon_working_on_car_night_scene:
    if "damon" not in contacts_met:
        jump introduce_damon_night_introduction_scene
    else:
        jump damon_working_on_car_night_conversation_scene

label introduce_damon_night_introduction_scene:
    scene neighbor_house_night_damon_working_on_car
    with fade
    show madd boy nervous at left_small
    x "Hi there, Sir... Sorry to bother you, but I saw that you're looking for a male maid."
    show damon dismissive at right_small
    damon "Can't you see I'm busy working on my car?"
    show madd boy hesitant at left_small
    x "Oh... sorry to bother you — (before I can finish my sentence he cuts me off)"
    show damon contemptuous at right_small
    damon "I know you lot can't see very well."
    show madd boy shocked at left_small
    x "(Did he just comment about my ethnicity?)"
    show madd boy nervous at left_small
    x "I... I just need a job, Sir."
    show damon calculating at right_small
    damon "I see..."
    show damon commanding at right_small
    damon "Come here, boy!!"
    x "(I walked up to him and stood right beside him.)"
    scene neighbor_house_night_damon_working_on_car_madd_looks_up_at_damon
    with fade
    show damon stern at right_small
    damon "So why do you want to work?"
    show madd boy hesitant at left_small
    x "I just need to make some money to support myself and my family."
    show damon arrogant at right_small
    damon "Young men like you get used as stress relief for guys fresh out of the army..."
    show madd boy confused at left_small
    x "(Why the hell is he saying this?)"
    show damon smirk at right_small
    damon "But I'm straight, so you don't have to worry about that."
    show madd boy confused at left_small
    x "(Then why even bring it up? Is he mentally ill?)"
    show damon dismissive at right_small
    damon "My wife is dealing with some health issues and we need a maid to help around the house."
    show damon stern at right_small
    damon "Think you can manage that?"
    show madd boy nervous at left_small
    x "Yes sir, I can. Just one question though..."
    show damon arrogant at right_small
    damon "What is it?"
    show madd boy hesitant at left_small
    x "Why did the notice board say you needed a male maid? Usually it's the other way around."
    show damon contemptuous at right_small
    damon "God, I can't stand nosy chinese people... mind your own business."
    show madd boy resigned at left_small
    x "But I'm not —"
    show damon dismissive at right_small
    damon "Chinese, Japanese, Korean, jungle asian — same difference. Anyway."
    show madd boy resigned at left_small
    x "(Surprisingly, he just kept going on his own.)"
    show damon scheming at right_small
    damon "I cheated on my wife... ever since then she doesn't trust other women around me."
    show madd boy shocked at left_small
    x "(I just need the job... why is he telling me this? But I had to seem sympathetic.)"
    x "Do you regret it, Sir?"
    show damon arrogant at right_small
    damon "Hell no. The woman I cheated with was way hotter and younger than my wife."
    show madd boy horrified at left_small
    x "(Wow. He switched so fast.)"
    show damon dismissive at right_small
    damon "My wife has a terminal illness — she's not far from the end. I'm still here to inherit her money."
    show damon smirk at right_small
    damon "Once she's gone I'm going to remarry. Some girl in her twenties."
    show madd boy horrified at left_small
    x "(What the hell is wrong with him? Why would you say all this to a stranger?)"
    show madd boy resigned at left_small
    x "I..."
    show damon calculating at right_small
    damon "Tell you what — if you're still willing to work, come by in the afternoon or evening."
    show madd boy resigned at left_small
    x "(I don't have much of a choice... I do need this job.)"
    x "Sounds great, Sir! I'll see you soon."
    scene neighbor_house_night_damon_working_on_car_introduction_neck_grab
    with fade
    show madd boy scared at left_small
    x "(Suddenly he grabbed my neck.)"
    show damon intimidating at right_small
    damon "And if you breathe a word of this to anyone, there will be consequences."
    show madd boy paralyzed at left_small
    x "(I looked at his build... the man was intimidating as hell.)"
    show damon commanding at right_small
    damon "This is where you nod."
    show madd boy submissive at left_small
    x "(I slowly nodded and he released my neck.)"
    show damon dismissive at right_small
    damon "Good. Now that we have an understanding — let me get back to my car. Get lost."
    show madd boy resigned at left_small
    x "(I nodded and walked away... I was so shaken I didn't even want to look back at him.)"
    x "(I just wanted the job, and I got it.)"
    hide madd boy resigned
    hide damon dismissive
    $contacts_met.append("damon")
    jump neighbors_house_scene
    
label damon_working_on_car_night_conversation_scene:
    scene neighbor_house_night_damon_working_on_car
    with fade
    show madd boy nervous at left_small
    x "(I decided to check on Damon while he was working on his car.)"
    x "Hi sir, how are you doing today?"
    x "(He looks back at me and gives me a cold stare.)"
    show damon commanding at right_small
    damon "STAND CLOSE TO ME BEFORE YOU SPEAK TO ME."
    scene neighbor_house_night_damon_working_on_car_madd_looks_up_at_damon
    with fade
    show madd boy obedient at left_small
    x "(I quickly walked up and stood right beside him, looking up at him.)"
    show damon stern at right_small
    damon "Just working on my car. Should have it sorted soon."
    show madd boy hesitant at left_small
    x "Can I help with anything, sir?"
    show damon dismissive at right_small
    damon "Here — tighten up the loose hood hinges. Stop them from sagging and rattling."

    scene neighbor_house_night_damon_working_on_car_madd_working_on_car
    with fade
    show madd boy working at left_small
    x "(He handed me a wrench and stepped back to watch me work.)"
    show madd boy confused at left_small
    x "(Ugh... I have absolutely no idea how to do this.)"
    x "(What do I do...)"
    show madd boy uncertain at left_small
    x "(I spotted the biggest bolt I could see and tried tightening it — but the wrench didn't even fit.)"

    scene neighbor_house_night_damon_working_on_car_madd_struggling_to_work_on_car_damon_angry
    with fade
    show damon angry at right_small
    damon "What!! You don't even know the basics??"
    show madd boy humiliated at left_small
    x "(I was so embarrassed — and then suddenly he started slapping my backside hard.)"
    x "(Instinctively my lips parted and a small sound escaped before I could stop it. I quickly apologized.)"
    show madd boy shamed at left_small
    x "I... I'm sorry, sir."
    show damon contemptuous at right_small
    damon "Sorry won't fix anything... idiot."
    show madd boy humiliated at left_small
    x "(He pulled me away from the car.)"
    show damon degrading at right_small
    damon "At least you're soft back there... maybe that's the only thing you're good for."
    show madd boy silent at left_small
    x "(I just stood there in silence, trying not to make things worse.)"
    scene neighbor_house_night_damon_working_on_car_madd_struggling_to_work_on_car_damon_angry_2
    with fade
    show damon lecherous at right_small
    x "(He put his hand on my backside again and started rubbing it this time.)"
    show damon taunting at right_small
    damon "Guess I was right about you being stress relief for men in the service."
    show madd boy dissociating at left_small
    x "(I had to endure his disgusting behavior just to hold onto this job.)"
    show madd boy resigned at left_small
    x "I.... Yes sir."
    scene neighbor_house_night_damon_working_on_car_madd_looks_down_at_ground_and_walkss_away_from_damon
    with fade
    show damon dismissive at right_small
    damon "Good. Now get out of here and let me work on my car."
    show madd boy horrified at left_small
    x "(I left him and walked away, not wanting to look back at him.)"
    show damon degrading at right_small
    damon "Damn fag with those hips..."
    show madd boy horrified at left_small
    x "(What!!? He thinks I'm a boy, slaps my backside and rubs it, then calls me a fag??)"
    hide madd boy horrified
    hide damon degrading
    jump outside_home

label home_park_scene:
    python:
        if game_time.is_morning():
            park_bg = "parkmor"
        elif game_time.is_afternoon():
            park_bg = "parkaft"
        elif game_time.is_evening():
            park_bg = "parkeve"
        else:
            park_bg = "parknig"

    scene expression park_bg
    with fade

    p "(Le parc est magnifique comme toujours.)"
    
    if convrocky == 0 and game_time.is_afternoon() and personnage_actuel == "Dave" and game_time.hour == 15 and game_time.day != "Tuesday":
        x "(Je regarde si Rocky est dans le coin.)"
        jump rocky_intro
    else:
        p "(Je me suis reposé là pendant quelques minutes.)"
        call advance_time_and_check(minutes=30) from _call_advance_time_and_check_park

    jump outside_home

label parklindsandrocky:
    python:
        if game_time.is_morning():
            park_bg = "parkmor"
        elif game_time.is_afternoon():
            park_bg = "parkaft"
        elif game_time.is_evening():
            park_bg = "parkeve"
        else:
            park_bg = "parknig"
    scene expression park_bg
    show dave happy
    with fade

    x "(Le parc est magnifique comme toujours.)"
    show dave stressed
    x "(Oh voilà rocky qui parle à Lindsay.)"
    x "(On dirait qu'ils se rapprochent de jour en jour...)"
    jump outside_home


label pharmacy_near_home:
    python:
        if game_time.is_morning() or game_time.is_afternoon():
            pharmacy_bg = "pharmacy_home_morning_afternoon"
        elif game_time.is_evening():
            pharmacy_bg = "pharmacy_home_evening"
        else:
            pharmacy_bg = "pharmacy_home_night"

    scene expression pharmacy_bg
    with fade

    x "(I am inside the pharmacy )"

    if game_time.is_night():
        x "(Looks like the pharmacist is almost ready to close the shop, I should probably talk to him before he leaves.)"

    menu:
        "Talk to the pharmacist":
            call advance_time_and_check(minutes=1)
            jump talk_to_pharmacist_scene

        "Go back outside":
            call advance_time_and_check(minutes=1)
            jump outside_home


screen pharmacy_buy_screen():
    modal True
    add "#000000bb"

    default qty_aph = 1
    default qty_str = 1
    default qty_slp = 1
    default qty_tst = 1

    frame:
        xalign 0.5
        yalign 0.4
        xsize 880
        padding (40, 30, 40, 30)
        background Frame("gui/textbox.png", 25, 10, 25, 10)

        vbox:
            spacing 20
            xfill True

            text "Pharmacy Shop" xalign 0.5 size 32 color "#d4a050"
            null height 8

            # ── Aphrodisiac ────────────────────────────────────────────
            hbox:
                spacing 14
                yalign 0.5
                frame:
                    background "#7a1030"
                    xsize 54
                    ysize 54
                    padding (4, 4, 4, 4)
                    text "\u2665" xalign 0.5 yalign 0.5 size 30 color "#ff6090"
                vbox:
                    xsize 360
                    yalign 0.5
                    text "Aphrodisiac  \u2014  $150 ea." size 22 color "#c8b8b0"
                    text "Raises lust when slipped into a drink or food." size 16 color "#807078"
                    text "Total: $[qty_aph * 150]" size 17 color ("#e05050" if madd_money < qty_aph * 150 else "#a0d080")
                hbox:
                    yalign 0.5
                    spacing 4
                    textbutton "\u2212" action SetScreenVariable("qty_aph", max(1, qty_aph - 1))
                    frame:
                        xsize 38
                        ysize 32
                        background "#2a2a2a"
                        text "[qty_aph]" xalign 0.5 yalign 0.5 size 20 color "#c8b8b0"
                    textbutton "+" action SetScreenVariable("qty_aph", qty_aph + 1)
                textbutton "Buy" yalign 0.5 action If(madd_money >= qty_aph * 150, [SetVariable("inv_aphrodisiac", inv_aphrodisiac + qty_aph), SetVariable("madd_money", madd_money - qty_aph * 150), Return("bought")], Return("no_money"))

            null height 4

            # ── Stress Reduction Pills ─────────────────────────────────
            hbox:
                spacing 14
                yalign 0.5
                frame:
                    background "#163a6b"
                    xsize 54
                    ysize 54
                    padding (4, 4, 4, 4)
                    text "\u2605" xalign 0.5 yalign 0.5 size 28 color "#80c0ff"
                vbox:
                    xsize 360
                    yalign 0.5
                    text "Stress Reduction Pills  \u2014  $80 ea." size 22 color "#c8b8b0"
                    text "Helps you sleep more soundly. Lowers anger and lust." size 16 color "#807078"
                    text "Total: $[qty_str * 80]" size 17 color ("#e05050" if madd_money < qty_str * 80 else "#a0d080")
                hbox:
                    yalign 0.5
                    spacing 4
                    textbutton "\u2212" action SetScreenVariable("qty_str", max(1, qty_str - 1))
                    frame:
                        xsize 38
                        ysize 32
                        background "#2a2a2a"
                        text "[qty_str]" xalign 0.5 yalign 0.5 size 20 color "#c8b8b0"
                    textbutton "+" action SetScreenVariable("qty_str", qty_str + 1)
                textbutton "Buy" yalign 0.5 action If(madd_money >= qty_str * 80, [SetVariable("inv_stress_pills", inv_stress_pills + qty_str), SetVariable("madd_money", madd_money - qty_str * 80), Return("bought")], Return("no_money"))

            null height 4

            # ── Sleeping Pills ─────────────────────────────────────────
            hbox:
                spacing 14
                yalign 0.5
                frame:
                    background "#231550"
                    xsize 54
                    ysize 54
                    padding (4, 4, 4, 4)
                    text "\u263d" xalign 0.5 yalign 0.5 size 28 color "#c0a0ff"
                vbox:
                    xsize 360
                    yalign 0.5
                    text "Sleeping Pills  \u2014  $60 ea." size 22 color "#c8b8b0"
                    text "Puts someone to sleep when added to food or drink." size 16 color "#807078"
                    text "Total: $[qty_slp * 60]" size 17 color ("#e05050" if madd_money < qty_slp * 60 else "#a0d080")
                hbox:
                    yalign 0.5
                    spacing 4
                    textbutton "\u2212" action SetScreenVariable("qty_slp", max(1, qty_slp - 1))
                    frame:
                        xsize 38
                        ysize 32
                        background "#2a2a2a"
                        text "[qty_slp]" xalign 0.5 yalign 0.5 size 20 color "#c8b8b0"
                    textbutton "+" action SetScreenVariable("qty_slp", qty_slp + 1)
                textbutton "Buy" yalign 0.5 action If(madd_money >= qty_slp * 60, [SetVariable("inv_sleeping_pills", inv_sleeping_pills + qty_slp), SetVariable("madd_money", madd_money - qty_slp * 60), Return("bought")], Return("no_money"))

            null height 4

            # ── Testosterone Pills ──────────────────────────────────────
            hbox:
                spacing 14
                yalign 0.5
                frame:
                    background "#5a1a00"
                    xsize 54
                    ysize 54
                    padding (4, 4, 4, 4)
                    text "\u26a1" xalign 0.5 yalign 0.5 size 28 color "#ff8800"
                vbox:
                    xsize 360
                    yalign 0.5
                    text "Testosterone Pills  \u2014  $120 ea." size 22 color "#c8b8b0"
                    text "Raises anger and aggression when added to food or drink." size 16 color "#807078"
                    text "Total: $[qty_tst * 120]" size 17 color ("#e05050" if madd_money < qty_tst * 120 else "#a0d080")
                hbox:
                    yalign 0.5
                    spacing 4
                    textbutton "\u2212" action SetScreenVariable("qty_tst", max(1, qty_tst - 1))
                    frame:
                        xsize 38
                        ysize 32
                        background "#2a2a2a"
                        text "[qty_tst]" xalign 0.5 yalign 0.5 size 20 color "#c8b8b0"
                    textbutton "+" action SetScreenVariable("qty_tst", qty_tst + 1)
                textbutton "Buy" yalign 0.5 action If(madd_money >= qty_tst * 120, [SetVariable("inv_testosterone", inv_testosterone + qty_tst), SetVariable("madd_money", madd_money - qty_tst * 120), Return("bought")], Return("no_money"))

            null height 12
            text "Your money: $[madd_money]" xalign 0.5 size 22 color "#d4a050"
            null height 6
            textbutton "Leave" xalign 0.5 action Return("leave")


label talk_to_pharmacist_scene:
    if game_time.is_night():
        # Night path — pharmacist closing up, random freebies
        if pharmacy_night_pills_taken:
            pharmacist "Sorry, you already grabbed what was left earlier tonight. Come back tomorrow."
            jump outside_home

        python:
            night_aphrodisiac = 1 if renpy.random.random() < 0.2 else 0
            night_stress_pills = 1 if renpy.random.random() < 0.2 else 0
            night_sleeping_pills = 1 if renpy.random.random() < 0.2 else 0
            night_testosterone = 0  # set after sleeping pills check

        pharmacist "Sorry, I'm done for the day. I'm closing up now."
        pharmacist "You can take whatever's left on the counter — I'm not carrying it home."

        if night_aphrodisiac or night_stress_pills or night_sleeping_pills:
            x "(I look at the counter...)"
            if night_aphrodisiac:
                $ inv_aphrodisiac += night_aphrodisiac
                x "(There's a bottle of aphrodisiac sitting there. I pocket it.)"
            if night_stress_pills:
                $ inv_stress_pills += night_stress_pills
                x "(There's a pack of stress reduction pills on the counter. I take it.)"
            if night_sleeping_pills:
                $ inv_sleeping_pills += night_sleeping_pills
                x "(There are some sleeping pills left out. I slip them into my bag.)"
            python:
                night_testosterone = 1 if renpy.random.random() < 0.2 else 0
            if night_testosterone:
                $ inv_testosterone += night_testosterone
                x "(There's a small bottle of testosterone pills on the counter. I grab it.)"
        else:
            x "(I look at the counter — it's completely empty. Nothing left.)"

        $ pharmacy_night_pills_taken = True
        pharmacist "Alright, out you go. Come back tomorrow."
        jump outside_home

    else:
        # Day / evening path — normal shop
        pharmacist "Welcome! What can I get for you today?"
        x "(I look over the items on display.)"

        $ keep_shopping = True
        while keep_shopping:
            call screen pharmacy_buy_screen()
            if _return == "no_money":
                pharmacist "You don't have enough money for that, darling."
            elif _return == "leave":
                $ keep_shopping = False
            else:
                pharmacist "Good choice! Anything else?"

        pharmacist "Come again!"
        jump pharmacy_near_home


label read_flyers_scene:
    x "(I take a closer look at the flyers on the notice board related to the neighborhood.)"
    x "(It seems they are looking for a male maid to help out with some household chores. )"
    x "(Male maids are pretty rare, usually its the other way around )"

    jump notice_board_scene







