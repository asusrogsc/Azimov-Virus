label my_room_scene:
    python:
        if game_time.is_morning():
            davebedroomscene = "davebedroomscenemor"
        elif game_time.is_afternoon():
            davebedroomscene = "davebedroomscenenoon"
        elif game_time.is_evening():
            davebedroomscene = "davebedroomsceneeven"
        else:  # night
            davebedroomscene = "davebedroomscenenight"
    
    scene expression davebedroomscene
    if personnage_actuel == "Dave":
        "Ma chambre, mon univers"
    
    menu:
        "Aller sur le pc et étudier" if personnage_actuel == "Dave":
            jump research_cram_schools
     
        "Mission: Sauvetage 1" if convrocky == 1 and checkinfos == 1 and savelindsay == 0 and personnage_actuel == "Dave":
            jump lindsay_save

        "Mission: Sauvetage 1" if convrocky == 3 and checkinfos == 5 and savemzelle == 0 and personnage_actuel == "Dave":
            jump mzelle_save

        "Dormir dans le lit" if personnage_actuel == "Dave":
            show madd think at left_small
            with dissolve
            x "Un peu ou beaucoup ?"
            menu:
                "Sieste jusqu'àprès midi":
                    if game_time.is_evening() or game_time.is_night():
                        show madd think at left_small
                        with dissolve
                        x "It's already evening or night. No point in napping now."
                        jump my_room_scene
                    else:
                        scene madd_home_nap_till_evening
                        show madd happy at left_small
                        with dissolve
                        x "I'll take a nap until evening..."
                        # Calculate hours to advance to 18:00 (6 PM - start of evening)
                        $ hours_to_evening = (18 - game_time.hour) if game_time.hour < 18 else 0
                        $ minutes_to_evening = -game_time.minute if game_time.hour < 18 else 0
                        $ total_minutes_to_evening = (hours_to_evening * 60) + minutes_to_evening
                        $ game_time.advance_time(minutes=total_minutes_to_evening)
                        show madd think at left_small
                        with dissolve
                        x "I feel refreshed after that nap."
                        $  madd_willpower = min(madd_willpower + 30, madd_willpower_max)
                        jump my_room_scene
                
                "Jusque demain":
                    jump sleep_on_bed_my_room
        
        "Attendre ici":
            show madd think at left_small
            with dissolve
            x "How long should I wait here?"
            menu:
                "1 minute":
                    $ game_time.advance_time(minutes=1)
                    jump my_room_scene
                "5 minutes":
                    $ game_time.advance_time(minutes=5)
                    jump my_room_scene
                "15 minutes":
                    $ game_time.advance_time(minutes=15)
                    jump my_room_scene
                "30 minutes":
                    $ game_time.advance_time(minutes=30)
                    jump my_room_scene
                "1 heure":
                    $ game_time.advance_time(minutes=60)
                    jump my_room_scene
                "3 heures":
                    $ game_time.advance_time(minutes=180)
                    jump my_room_scene
                "6 heures":
                    $ game_time.advance_time(minutes=360)
                    jump my_room_scene
                "12 heures":
                    $ game_time.advance_time(minutes=720)
                    jump my_room_scene
        
        "Retour au lobby":
            jump home_areas



label research_cram_schools:
    if madd_willpower < 40:
        show madd distressed at left_small
        x "Crever, je dois me reposer..."
        jump my_room_scene
    $ madd_willpower -= 40
    scene scene_madd_home_room_research_sitting_on_computer
    with fade
    show madd focused at left_small
    with dissolve
    x "Pour devenir grand, il faut travailler ..."
    if research_cram_schools == 0:
        jump research_cram_schools_1
    elif research_cram_schools == 1:
        jump research_cram_schools_2
    elif research_cram_schools == 2:
        jump research_cram_schools_3
    else:
        show madd think at left_small
        x "I've already researched everything I need about cram schools. So I will study other things now."
        $ madd_willpower_max += 5

        
        jump my_room_scene


label research_cram_schools_1:
    scene scene_madd_research_athome
    with fade
    show madd focused at left_small
    x "Je lance le logiciel et c'est partis !"
    
    show madd think at left_small
    x "( The screen glows in the dimly lit room... this is my way out. This is how I change my life. )"
    
    show madd uncertain at left_small
    x "My fingers move across the keyboard, clicking through websites and reviews. There are so many options..."
    
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
    
    show madd horrified at left_small
    x "Entrance fee: 2,000 dollars. Monthly tuition: 500 dollars. Additional materials: 200 dollars."
    
    show madd distressed at left_small
    x "( 2,000 dollars just to start. That's nearly everything I have. My hands are trembling. )"
    
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
    x "I minimize the browser and look around my room. My eyes land on the small photo I keep hidden - the only family photo I have left."
    
    show madd relieved at left_small
    x "( Dad in his younger days, laughing. Mom beside him, so happy. Before everything fell apart. )"
    
    show madd worried at left_small
    x "Dad always said: 'If you're going to do something, do it right. Never settle for mediocre when you can have excellence.'"
    
    show madd shocked at left_small
    x "( He believed in working hard, in earning the best through determination and sacrifice. )"
    
    show madd sad at left_small
    x "And Mom... she always supported his dreams, even when it got risky. Even when it all fell apart."
    
    show madd paralyzed at left_small
    x "( Mom never complained. She just... endured. She did what she had to do. )"
    
    show madd think at left_small
    x "I take a deep breath and move the mouse back to the Akira Cram School page."
    
    show madd focused at left_small
    x "I'm going to do this. I'm going to get into the best school, the one with the best results, the one that actually matters."
    
    show madd angry at left_small
    x "( If I'm escaping this hellhole, I'm not doing it halfway. I'm going to make it count. )"
    
    show madd determined at left_small
    x "I'm going to pay the 2,000 dollars. I'm going to tough it out."
    
    show madd relieved at left_small
    x "( Like Dad said... if you're going to do it, do it right. )"
    
    show madd think at left_small
    x "The best costs the most. And I'm worth paying for."
    
    $ research_cram_schools = 1
    $ journal_event_set_done("Madd", "Research: Cram School Choice")
    $ journal_event_show("Madd", "Research: Boys Hostel")
    $ stat_notification = "Research Progress: 1/3 - Chosen Akira Cram School"
    $ renpy.pause(2.0)
    $ stat_notification = ""
    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_74
    show madd focused at left_small
    x "Now I need to find a place to stay near the school."
    
    jump my_room_scene


label research_cram_schools_2:
    scene scene_madd_research_athome
    with fade
    show madd uncertain at left_small
    x "I open my computer again. This time, I need to find a place to live near Akira Cram School."
    
    show madd think at left_small
    x "( If I have to commute for hours every day, I'll lose so much time. I need to be close. )"
    
    show madd focused at left_small
    x "I search for hostels and shared housing near the school. The results flood in..."
    
    show madd shocked at left_small
    x "Girls-only hostels near the cram school: 800 dollars per month."
    
    show madd horrified at left_small
    x "( 800 dollars EVERY MONTH. That's... that's insane. )"
    
    show madd distressed at left_small
    x "I do the math in my head. If I pay for the cram school, I dont have any money. I can't afford 800 for rent."
    
    show madd paralyzed at left_small
    x "( Why is everything so expensive? How am I supposed to escape if every option is impossible? )"
    
    show madd depressed at left_small
    x "I search more desperately. Maybe there's a cheaper girls-only option further away?"
    
    show madd worried at left_small
    x "I find some options, but they're all 30-45 minutes away from the school. The commute alone would consume hours every day."
    
    show madd conflicted at left_small
    x "( This is hopeless. I can't afford to stay close, and I can't afford to commute. What am I supposed to do? )"
    
    show madd sad at left_small
    x "I lean back in my chair, feeling the weight of despair pressing down on me. Maybe this plan is too ambitious. Maybe I'm being naive."
    
    show madd distressed at left_small
    x "Maybe I should just accept that I'm trapped here. Maybe there's no way out."
    
    show madd think at left_small
    x "( No. No, I can't think like that. There has to be a way. There has to be. )"
    
    show madd uncertain at left_small
    x "I scroll down further in my search, almost mechanically. And then something catches my eye."
    
    show madd shocked at left_small
    x "Boys-only hostels near the cram school."
    
    show madd curious at left_small
    x "( Why would there be so many boys-only hostels? )"
    
    show madd think at left_small
    x "I click on the first one. The monthly rent: 200 dollars."
    
    show madd horrified at left_small
    x "( 200 dollars? That's... that's a quarter of the girls' hostels. How is that even possible? )"
    
    show madd uncertain at left_small
    x "I check multiple listings. It's not a mistake. Boys-only hostels are consistently 1/4 the price."
    
    show madd conflicted at left_small
    x "( Why is there such a huge difference? )"
    
    show madd think at left_small
    x "I read reviews and descriptions. The boys-only hostels are often run as dormitories, with shared communal spaces, basic amenities."
    
    show madd confused at left_small
    x "Girls-only hostels have private rooms, security features, 24-hour staff, better facilities... that's why they cost more."
    
    show madd distressed at left_small
    x "( But I can't afford the safe option. So what do I do? )"
    
    show madd think at left_small
    x "I stare at the boys-only hostel listings. My mind is racing with a dangerous idea."
    
    show madd nervous at left_small
    x "( What if... what if I could pass as a boy? )"
    
    show madd shocked at left_small
    x "The thought makes my heart race. It's insane. It's impossible. It would be discovered immediately."
    
    show madd worried at left_small
    x "( But... is it? Really? )"
    
    show madd think at left_small
    x "I look at myself in the small mirror on my desk. My hair is long... but I could cut it. The right clothes could hide my shape."
    
    show madd uncertain at left_small
    x "( It would be risky. If anyone found out, the consequences would be severe. They'd kick me out immediately. Maybe worse. )"
    
    show madd conflicted at left_small
    x "But without this plan, I'm stuck. I'm trapped in this house with a stepfather who abuses me and a stepbrother who... "
    
    show madd distressed at left_small
    x "( ...who is becoming more and more like his father every day. )"
    
    show madd focused at left_small
    x "I need to do this. I need a fake certificate, a fake name, a fake identity."
    
    show madd paralyzed at left_small
    x "( Creating a fake certificate is illegal. If I get caught, I could go to jail. )"
    
    show madd think at left_small
    x "But staying here is a living hell. Every day is a new humiliation, a new boundary violated, a new reason to hate myself."
    
    show madd angry at left_small
    x "( Jail would actually be safer than this house. )"
    
    show madd determined at left_small
    x "I make my decision. I'm going to do this. I'm going to create a fake identity and live as a boy."
    
    show madd worried at left_small
    x "( It's dangerous. It's risky. But it's the only way. )"
    show madd relieved at left_small
    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_75
    $ research_cram_schools = 2
    $ journal_event_set_done("Madd", "Research: Boys Hostel")
    $ journal_event_show("Madd", "Research: The Escape Budget")
    $ stat_notification = "Research Progress: 2/3 - Found boys hostel, committed to plan"
    $ renpy.pause(2.0)
    $ stat_notification = ""
    
    jump my_room_scene


label research_cram_schools_3:
    scene scene_madd_research_athome
    with fade
    show madd think at left_small
    x "I pull out my notebook and a calculator. It's time to see if this plan is actually feasible."
    
    show madd focused at left_small
    x "Let me break down the numbers. Everything depends on this calculation."
    
    show madd uncertain at left_small
    x "Cram school entrance fee: 2,000 dollars."
    
    show madd worried at left_small
    x "Boys-only hostel rent per month: 200 dollars. But they'll want a deposit first."
    
    show madd distressed at left_small
    x "A deposit is typically 2-4 months worth of rent. So that's 400 to 800 dollars."
    
    show madd think at left_small
    x "( Let's calculate conservatively. 2,000 for cram school + 800 for hostel deposit = 2,800 dollars minimum. )"
    
    show madd horrified at left_small
    x "That's 2,800 dollars just to get started."
    
    show madd paralyzed at left_small
    x "( I only have [madd_money] dollars right now. I need [2800 - madd_money] more. I am comepletely broke! )"
    
    show madd conflicted at left_small
    x "Once I'm there at the hostel and cram school, I can find a part-time job. I can work while I study."
    
    show madd uncertain at left_small
    x "If the rent is 200 a month, and I can earn even 100-150 a month working part-time, that could sustain me for a few more months."
    
    show madd think at left_small
    x "( The key is just getting there. Once I'm out of this house, I have options. Here, I have nothing. )"
    
    show madd focused at left_small
    x "So the critical amount is 2,800 dollars. That's my target. That's my escape fund."
    
    show madd shocked at left_small
    x " I need 2,800. Not impossible, but I need to find it fast."
    
    show madd distressed at left_small
    x "( How am I supposed to get 2,800 dollars? )"
    
    show madd think at left_small
    x "I scratch my head, staring at my calculations."
    
    show madd uncertain at left_small
    x "( There are only a few ways to get that much money quickly: )"
    
    show madd worried at left_small
    x "I could work multiple jobs, but I'd have to work constantly and it would take months. I don't have months."
    
    show madd paralyzed at left_small
    x "I could... I could try to find someone to give me money. But who?"
    
    show madd distressed at left_small
    x "( I'm alone. I have no one. )"
    
    show madd think at left_small
    x "Or... or I could steal it."
    
    show madd shocked at left_small
    x "( The moment that thought crosses my mind, I feel both terrified and oddly calm. )"
    
    show madd conflicted at left_small
    x "I know there's money hidden in the house. Not much, but maybe enough. My stepfather keeps extra cash hidden in different places."
    
    show madd distressed at left_small
    x "( If I steal it and he finds out, the consequences would be... )"
    
    show madd think at left_small
    x "But what are my options really? Stay here? Accept being abused? Wait for something to change that never will?"
    
    show madd angry at left_small
    x "( No. I've waited long enough. I've suffered long enough. )"
    
    show madd focused at left_small
    x "I make my decision. I will find the money and I will steal it if I have to."
    
    show madd determined at left_small
    x "I need at least 2,800 dollars to escape. My stepfather has hidden money around this house. I just need to find it."
    
    show madd think at left_small
    x "( And once I have it, I'm gone. I'm never coming back to this place. )"
    
    show madd relieved at left_small
    x "Now I have a plan. A real plan. It's dangerous, it's illegal, but it's the only way out."
    
    show madd uncertain at left_small
    x "But there's still the matter of getting there. The hostel is 20-30 kilometers away."
    
    show madd worried at left_small
    x "( Can I take a bus? No... that costs money. Money I need for the deposit and school. )"
    
    show madd think at left_small
    x "( What about a taxi? Even worse. That would be at least 30-50 dollars. I can't spare that. )"
    
    show madd distressed at left_small
    x "That leaves only one option: I walk."
    
    show madd nervous at left_small
    x "( 20-30 kilometers on foot. Carrying a backpack with everything I own. In the summer sun. )"
    
    show madd hesitant at left_small
    x "The thought makes my stomach twist. My legs already ache just thinking about it."
    
    show madd conflicted at left_small
    x "( It could take 5-7 hours depending on how heavy my bag is and how tired I get. )"
    
    show madd worried at left_small
    x "What if I collapse from heat exhaustion? What if someone stops me and asks questions?"
    
    show madd paralyzed at left_small
    x "( A young person walking alone with a backpack in the heat... I could look suspicious. )"
    
    show madd distressed at left_small
    x "I could be spotted, reported, brought back here. Everything would be ruined."
    
    show madd anxious at left_small
    x "My hands are shaking just thinking about all the things that could go wrong."
    
    show madd think at left_small
    x "( But what's the alternative? Stay here? Accept this life? )"
    
    show madd angry at left_small
    x "No. Absolutely not. I would rather collapse on the road than spend another day in this house."
    
    show madd determined at left_small
    x "I've endured worse than heat and exhaustion. I can walk 20-30 kilometers."
    
    show madd focused at left_small
    x "I'll start early in the morning, when it's cooler. I'll wear light clothes and bring water."
    
    show madd hopeful at left_small
    x "( It's only one day of walking. One day between here and freedom. I can do this. )"
    
    show madd conflicted at left_small
    x "( I hope I can do this. )"
    
    show madd determined at left_small
    x "I have to do this."
    
    show madd focused at left_small
    x "First, I need to find where dad keeps his money."
    
    $ research_cram_schools = 3
    $ journal_event_set_done("Madd", "Research: The Escape Budget")
    $ money_location_discovered = False
    $ stat_notification = "Research Complete: 3/3 - Needs 2800 dollars to escape"
    $ renpy.pause(2.0)
    $ stat_notification = ""

    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_76
    show madd determined at left_small
    x "Time to find where the money is."
    $stat_notification = "Now you may give in to demands of other characters."
    $ renpy.pause(2.0)
    $ stat_notification = ""

    $ journal_event_show("Brother", "Bare Ass (Demands)")
    $ journal_event_show("Brother", "Bare Breast (Demands)")
    $ journal_event_show("Brother", "Escape Night")
    $ journal_event_show("Dad", "Sleep With Dad: Breast Night")
    $ journal_event_show("Dad", "Sleep With Dad: Ass Night")
    
    jump my_room_scene




label steal_and_runaway:
    python:
        if game_time.is_morning() or game_time.is_afternoon():
            madd_room_scene = "scene_madd_home_room_morning_afternoon"
        elif game_time.is_evening():
            madd_room_scene = "scene_madd_home_room_evening"
        else:  # night
            madd_room_scene = "scene_madd_home_room_night"
    
    scene expression madd_room_scene
    with fade
    show madd angry at left_small
    x "I've had enough. I 've got a plan, I've got the money I need. It's time to leave this place behind."
    show madd focused at left_small
    x "This is my chance. My only chance to escape this nightmare."
    scene scene_madd_research_athome
    with fade
    show madd determined at left_small
    x "I logged on to the Akira Cram School website earlier and completed the enrollment form."
    show madd think at left_small
    x "(I used the crypto wallet to pay the entrance fee. It's done. There's no turning back now.)"
    $madd_money -= 2000
    $ paid_school_fees=True
    show madd relieved at left_small
    x "I have [madd_money] dollars left. Just enough for the hostel deposit and a little extra for food."
    show madd focused at left_small
    x "Now, I need to gather my things and prepare to leave."
    show madd determined at left_small
    x "It's time to run away from this place and start my new life."
    menu:
        "Run away":
            jump runaway_execution


label runaway_execution:
    python:
        if game_time.is_morning() or game_time.is_afternoon():
            madd_room_scene = "scene_madd_home_room_morning_afternoon"
        elif game_time.is_evening():
            madd_room_scene = "scene_madd_home_room_evening"
        else:  # night
            madd_room_scene = "scene_madd_home_room_night"
    
    scene expression madd_room_scene
    with fade
    show madd focused at left_small
    x "I've already paid the cram school fees using cryptocurrency. There's no turning back now."
    
    show madd determined at left_small
    x "It's time to pack my things and leave this place behind."
    
    show madd think at left_small
    x "I start gathering my belongings carefully. Not much - just the essentials."
    
    python:
        if game_time.is_morning() or game_time.is_afternoon():
            madd_room_scene = "scene_madd_home_room_morning_afternoon"
        elif game_time.is_evening():
            madd_room_scene = "scene_madd_home_room_evening"
        else:  # night
            madd_room_scene = "scene_madd_home_room_night"
    
    scene expression madd_room_scene
    with fade
    show madd sad at left_small
    x "I take one last look around my room. This has been my sanctuary, the only safe space in this house."
    
    show madd relieved at left_small
    x "( I'm leaving all of this behind. But I'm finally getting out. )"
    
    show madd focused at left_small
    x "I pack my few belongings into my backpack. Then I start checking my clothes."
    
    show madd worried at left_small
    x "( Wait... all my clothes are way too skinny and fitted. They'll completely blow my cover when I show up at the hostel pretending to be a boy. )"
    
    show madd shocked at left_small
    x "( I need loose, baggy clothes. Clothes that hide my shape. )"
    
    show madd distressed at left_small
    x "( But I don't have any. And I can't go shopping without raising suspicion. )"
    
    show madd paralyzed at left_small
    x "( The only person who might have guy's clothes is... my brother. )"
    
    show madd nervous at left_small
    x "( Do I really want to ask him for help? Do I want to owe him anything? )"
    
    show madd angry at left_small
    x "( But I don't have a choice. He's my only option. )"
    
    show madd determined at left_small
    x "I take a deep breath and head toward his room. This is the only way."
    
    jump request_for_clothes_brother


label request_for_clothes_brother:
    python:
        lobby_scene = get_dynamic_lobby_scene()
    scene expression lobby_scene
    with fade
    show madd nervous at left_small
    x "I stand outside his door, my hand raised to knock. My heart is pounding."
    
    show madd distressed at left_small
    x "( I'm about to ask my brother for help. The person who's violated me. The person I fear. )"
    
    show madd paralyzed at left_small
    x "( But I need those clothes. I need to escape. )"
    
    scene scene_brother_room_night_time
    with fade
    show madd determined at left_small
    x "I knock on his door."
    
    brother_says "Come in."
    show brother creepy at right_small
    with dissolve

    scene scene_escape_home_brother_room_brother_sitting_on_bed
    with fade
    
    show madd nervous at left_small
    x "I open the door slowly. He's sitting on his bed, looking at me with curiosity."
    
    show madd distressed at left_small
    x "Um... I need to ask you something."
    
    brother_says "What is it?"
    show brother possessive at right_small
    with dissolve
    
    show madd anxious at left_small
    x "I... I need some of your clothes. Loose, baggy stuff. And a cap if you have one."
    
    show madd processing at left_small
    x "I can't really explain why right now, but it's important."
    
    brother_says "My clothes? And a cap?"
    show brother sadistic at right_small
    with dissolve
    
    brother_thinks "(Oh... oh this is interesting.)"
    show brother manipulative at right_small
    with dissolve
    brother_thinks "(She needs to hide her body.She is asking for clothes much bigger than her, She needs to look like a man. She's planning to disguise herself.)"
    show brother obsessed at right_small
    with dissolve
    
    brother_thinks "(And I know why. I saw the research she was doing for cram school, all of it.)"
    show brother cruel at right_small
    with dissolve
    brother_thinks "(She's leaving. She's paying to go to cram school, then she's going to hide herself as a boy to get into those men-only hostels.)"
    brother_thinks "(Those are cheap and she doesnt have money and that's why she was asking for money. IT all makes sense now.)"
    show brother sadistic at right_small
    with dissolve
    
    show madd shaken at left_small
    x "I just... I really need them. Please."
    
    show madd violated at left_small
    x "Can you help me or not?"
    
    brother_thinks "(And that's where she's planning to stay. A men-only hostel near that cram school. Where nobody would think to look for a girl.)"
    show brother cruel at right_small
    with dissolve
    brother_thinks "(She thinks she's being so clever. But she has no idea what she's walked into.)"
    show brother sadistic at right_small
    with dissolve
    
    brother_thinks "(Dad has parental phone tracking on all of us. I can access it. I know exactly where she'll go.)"
    show brother obsessed at right_small
    with dissolve
    brother_thinks "(And once I know the hostel... I can enroll there myself. I can become a student too.)"
    show brother manipulative at right_small
    with dissolve
    
    brother_thinks "(She's trying to escape. But she's just walking into a cage I can control.)"
    show brother cruel at right_small
    with dissolve
    brother_thinks "(A cage where she'll never be free of me.)"
    show brother possessive at right_small
    with dissolve
    
    show madd nervous at left_small
    x "Why are you looking at me like that?"
    
    brother_says "I'll get you the clothes."
    show brother cruel at right_small
    with dissolve
    
    show madd shocked at left_small
    x "You... you will? Just like that?"
    
    brother_says "Yeah. No problem at all, little sister."
    show brother sadistic at right_small
    with dissolve
    
    brother_thinks "(Because I want you to leave. I want you to feel safe. I want you to think you've escaped.)"
    show brother possessive at right_small
    with dissolve
    brother_thinks "(Because I'm going to follow you everywhere you go. And you're going to need me more than ever.)"
    show brother cruel at right_small
    with dissolve
    brother_thinks "(And once you are in boys only hostels, I'll be right there with you. Watching you. Controlling you.)"
    show brother obsessed at right_small
    with dissolve
    brother_thinks "(You will do whatever I say , to keep your identity secret. You will be mine forever.)"

    
    jump brother_gives_clothes




label brother_gives_clothes:
    scene scene_escape_home_brother_room_brother_sitting_on_bed_madd_requesting_clothes
    with fade
    show brother cruel at right_small
    with dissolve
    show madd distressed at left_small
    with dissolve
    
    x "He walks over to his closet and starts rifling through hangers and drawers with deliberate slowness."
    
    show madd anxious at left_small
    with dissolve
    x "The sound of fabric rustling fills the room. Each movement seems calculated to keep me waiting, watching."
    
    show madd uncertain at left_small
    with dissolve
    x "Finally, he pulls out a collection of oversized t-shirts, loose athletic wear, and baggy cargo pants. Clothes that could belong to anyone."
    
    show brother sadistic at right_small
    with dissolve
    brother_says "Here. These should work perfectly for what you need."
    
    show madd nervous at left_small
    with dissolve
    x "I nod quickly, relief flooding through me. Finally, I can do this. I can actually—"
    
    show madd processing at left_small
    with dissolve
    x "But he doesn't hand them to me. Instead, he holds them, watching my face."
    
    show madd conflicted at left_small
    with dissolve
    
    show madd conflicted at left_small
    with dissolve
    brother_says "Actually, no. Change into them here."
    
    show madd shocked at left_small
    with dissolve
    x "W-what? Here? Right now?"
    
    show madd shaken at left_small
    with dissolve
    brother_says "Yeah. I want to see how they look on you. Make sure they actually work for your plan."
    
    x "( My heart skips a beat. This is worse than I imagined. )"
    x "(He sits on the bed, eyes fixed on me, waiting. As if he wanted to enjoy  the show.)"
    show madd distressed at left_small
    with dissolve
    x "( My stomach drops. He knows something. He knows something is wrong. )"
    
    show madd helpless at left_small
    with dissolve
    x "Um... can't I just... take them to my room?"
    
    show brother possessive at right_small
    with dissolve
    brother_says "No. Here. Now. Don't be difficult."
    
    show madd shaken at left_small
    with dissolve
    x "( I can't refuse. I need these clothes more than I need my dignity right now. )"
    
    show madd paralyzed at left_small
    with dissolve
    x "I take a shaky breath and start to remove my shirt."
    
    show madd trembling at left_small
    with dissolve
    x "My fingers grip the hem of the fabric. They're trembling so badly I can barely hold on."
    
    show madd anxious at left_small
    with dissolve
    x "I pull it up slowly, feeling the fabric drag across my stomach, my ribs, sliding upward."
    
    scene scene_escape_home_brother_room_brother_sitting_on_bed_madd_requesting_clothes_topless
    with fade

    show madd distressed at left_small
    with dissolve
    x "The cool air hits my bare skin first—my lower abdomen, the curves of my waist becoming visible."
    
    show madd horrified at left_small
    with dissolve
    x "I continue pulling, and my breasts come into view. No bra underneath. Completely exposed."
    
    show madd self loathing at left_small
    with dissolve
    x "I finally yank the shirt over my head and drop it to the floor."
    
    show madd violated at left_small
    with dissolve
    x "My upper body is completely bare now. I can feel every inch of my skin exposed to the air, to his eyes."
    
    show brother obsessed at right_small
    with dissolve
    brother_thinks "(Oh god... look at them. Those breasts... the way they sit, the size of them, the curve...)"
    
    brother_thinks "(Her nipples are already hardening from the cold. She's so vulnerable right now.)"
    
    brother_thinks "(How am I supposed to let her just... leave... knowing what she looks like? Knowing what her body looks like?)"
    
    show madd shaken at left_small
    with dissolve
    x "I can feel his eyes on my chest, tracing every curve, every detail."
    
    x "( He's staring so intensely. Like he's memorizing me. )"
    
    x "My arms want to cross over my chest, to hide, but I force them to stay at my sides."
    
    show brother cruel at right_small
    with dissolve
    brother_thinks "(The way her breasts move slightly when she breathes... the definition in her chest... she's so perfectly shaped.)"
    
    brother_thinks "(And those breasts—they're larger than I thought. Full. Heavy. How did she hide those under her clothes?)"
    
    show madd distressed at left_small
    with dissolve
    x "Now I reach for my pants. My hands are shaking even worse now."
    
    x "I unfasten the button—my fingers slip once, twice, before I finally manage it."
    
    x "The zipper comes next. I pull it down slowly, the metallic sound filling the silent room."
    scene scene_escape_home_brother_room_brother_sitting_on_bed_madd_requesting_clothes_topless_pants_down
    with fade
    x "My pants sit loose on my hips now, barely held up."
    
    show brother obsessed at right_small
    with dissolve
    brother_thinks "(There... I can see the edge of her underwear now. Just a glimpse of the fabric. What color are they? White? Black? How do they fit her?)"
    
    show madd shaken at left_small
    with dissolve
    x "I pause for a moment, gathering courage I don't have."
    
    show madd paralyzed at left_small
    with dissolve
    x "Then I push my pants down. They slide over my hips, revealing more of me."
    
    show madd distressed at left_small
    with dissolve
    x "The fabric catches slightly on my skin as I lower it, dragging down my thighs."
    
    show madd horrified at left_small
    with dissolve
    x "My legs come into view—my thighs, my knees, all the way down to my ankles."
    
    show madd self loathing at left_small
    with dissolve
    x "I step out of them, kicking them aside."
    
    show brother cruel at right_small
    with dissolve
    brother_thinks "(Her legs... they're so smooth. So well-shaped. The way they curve from ankle to thigh... the definition in her calves...)"
    
    show madd violated at left_small
    with dissolve
    brother_thinks "(She's so completely exposed now. Just underwear between me and her entire body.)"
    
    show madd distressed at left_small
    with dissolve
    x "I'm standing there in just my underwear now. Vulnerable. Exposed."
    
    show madd trembling at left_small
    with dissolve
    x "I can see his eyes moving across my body—starting at my chest, lingering on my breasts, then sliding down to my waist."
    
    show madd helpless at left_small
    with dissolve
    x "Down to my hips. Down to my thighs."
    
    show madd paralyzed at left_small
    with dissolve
    x "He's studying me like I'm an object. Like he's cataloging every detail."
    
    show brother obsessed at right_small
    with dissolve
    brother_thinks "(Look at her stomach... so flat. So perfect. And her hips... the way they flare out from her waist...)"
    
    show madd horrified at left_small
    with dissolve
    brother_thinks "(Those legs go on forever. And between them... I can almost see the outline through the fabric. Is she wet? Probably terrified, but does her body respond anyway?)"
    
    show madd self loathing at left_small
    with dissolve
    x "I pause, my hands hovering at the elastic of my underwear."
    
    show madd paralyzed at left_small
    with dissolve
    x "This is the last barrier. The last thing protecting me."
    
    show madd shaken at left_small
    with dissolve
    x "Once these come off, there's nothing left. No hiding. No secrets."
    
    show brother possessive at right_small
    with dissolve
    brother_says "Go on."
    
    show madd distressed at left_small
    with dissolve
    x "His voice is cold. Command. Expectation."
    
    show madd helpless at left_small
    with dissolve
    x "( I have no choice. )"
    
    show madd paralyzed at left_small
    with dissolve
    x "I hook my thumbs into the elastic."
    
    scene scene_escape_home_brother_room_brother_sitting_on_bed_madd_requesting_clothes_topless_pants_down_underwear_down
    with fade
    show madd trembling at left_small
    with dissolve
    x "I take a breath and push them down."
    
    show madd violated at left_small
    with dissolve
    x "They slide down my legs slowly, revealing everything—the dark hair between my thighs, the shape of me, the most intimate part of myself."
    
    show madd self loathing at left_small
    with dissolve
    x "I step out of them, and I'm standing completely naked in front of him."
    
    show brother obsessed at right_small
    with dissolve
    brother_thinks "(There... oh god, there it is. That perfect pussy. The shape of it, the way the lips are slightly parted...)"
    
    show madd horrified at left_small
    with dissolve
    brother_thinks "(Is she wet? I need to know if she's aroused. Is her body betraying her? Is there any part of her that wants this?)"
    
    show madd violated at left_small
    with dissolve
    brother_thinks "(Her body is absolutely perfect. The curves, the softness, the vulnerability... she's completely at my mercy.)"
    
    show madd shaken at left_small
    with dissolve
    x "I'm completely naked now. Every inch of me exposed to his gaze."
    
    show madd helpless at left_small
    with dissolve
    x "The silence is deafening. I can hear him breathing heavily."
    
    scene scene_escape_home_brother_room_brother_standing_up_from_bed_madd_naked
    with fade
    show brother sadistic at right_small
    with dissolve
    x "He stands up slowly, and I can hear the sound of his clothes shifting as he moves toward me."
    
    show madd paralyzed at left_small
    with dissolve
    x "His footsteps are loud in the small room. Every one brings him closer."
    
    show madd distressed at left_small
    with dissolve
    x "I can smell him now—the scent of his body, something musky and invasive."
    
    show brother cruel at right_small
    with dissolve
    x "He reaches out and his hand closes around my chin, forcing my face upward to meet his eyes."
    
    show madd paralyzed at left_small
    with dissolve
    x "( I can't move. I can't breathe properly. )"
    
    show madd traumatized at left_small
    with dissolve
    brother_says "You look so much better like this. Without anything hiding you."
    
    show madd distressed at left_small
    with dissolve
    x "His thumb traces my jawline. His touch makes my skin crawl."
    scene scene_escape_home_brother_room_brother_standing_up_from_bed_madd_naked_hands_on_chin
    with fade
    show brother possessive at right_small
    with dissolve
    brother_says "And don't forget—you came to me. You asked for my help. You owe me."
    
    show madd shaken at left_small
    with dissolve
    x "His eyes are dark, filled with something I recognize but don't want to name."
    
    show madd helpless at left_small
    with dissolve
    x "And then his face is moving toward mine. I can see the decision in his expression."
    
    show madd distressed at left_small
    with dissolve
    x "( No. No, please, not this. )"
    
    show madd traumatized at left_small
    with dissolve
    x "But I don't say it aloud. I learned long ago that saying no doesn't matter."
    
    scene scene_escape_home_brother_room_brother_leaning_in_to_kiss_madd_naked_kissing
    with fade

    show madd shaken at left_small
    with dissolve
    x "His lips touch mine, and I feel his beard against my skin—rough and scratchy, almost painful against my softness."
    
    show madd distressed at left_small
    with dissolve
    x "His breath smells like alcohol and cigarettes, and I can already taste the bitterness of both on his lips."
    
    show madd traumatized at left_small
    with dissolve
    brother_thinks "(She's not fighting anymore. She's just accepting it. She knows she needs me.)"
    

    x "( His kiss is forceful, demanding. There's no gentleness here, no care. Just possession. )"
    x "(I can feel his tongue pressing against my lips, insisting on entry.)"
    x "(It wants to be inside me. Taking over. )"
    scene scene_escape_home_brother_room_brother_kissing_madd_naked_kissing_deeper_tongue_inside
    show brother sadistic at right_small
    with dissolve
    x "His tongue forces its way past my lips, invasive and possessive, pushing into the space of my mouth."
    
    show madd paralyzed at left_small
    with dissolve
    x "He's not kissing me—he's claiming me. Marking me. Making me understand that my body isn't my own."
    
    show madd distressed at left_small
    with dissolve
    x "I want to pull away. Every instinct screams at me to push him off, to run, to escape."
    
    show madd helpless at left_small
    with dissolve
    x "But his hand tightens on my chin, holding me in place. His grip is iron. I cannot move."
    
    show madd violated at left_small
    with dissolve
    x "His hand moves from my chin to my waist, pulling me against him with brutal force."
    
    show madd shaken at left_small
    with dissolve
    x "I can feel the hardness pressing against me—the undeniable reality of what he wants, what he's taking."
    
    scene scene_escape_home_brother_room_brother_kissing_madd_naked_kissing_deeper_tongue_inside_hands_on_waist
    with fade
    show madd self loathing at left_small
    with dissolve
    x "The other hand slides down, grabbing my buttock roughly, squeezing painfully. I feel marks forming under his fingers."
    
    show madd broken at left_small
    with dissolve
    x "( This is what I get for asking him. This is the price. )"
    
    show madd distressed at left_small
    with dissolve
    x "His tongue moves deeper into my mouth, and I can taste him now—the full flavor of alcohol and cigarettes coating my tongue."
    
    show madd horrified at left_small
    with dissolve
    x "The taste makes my stomach turn. It's revolting, invasive, wrong."
    
    show madd paralyzed at left_small
    with dissolve
    x "He twists and turns his tongue inside my mouth, exploring every corner like he's trying to claim every part of me from the inside."
    
    show madd shaken at left_small
    with dissolve
    x "It feels like he's trying to reach down my throat, to occupy spaces inside my body that should be mine alone."
    
    show madd violated at left_small
    with dissolve
    x "The aggression increases. His kiss becomes more forceful, more demanding, more possessive."
    
    show madd helpless at left_small
    with dissolve
    x "I can't breathe. His mouth is covering mine completely, and his tongue seems to take up all the space in my mouth."
    
    show madd traumatized at left_small
    with dissolve
    x "I want to gag. The sensation of his tongue trying to go deeper, reaching toward my throat, makes my body want to reject him."
    
    show madd paralyzed at left_small
    with dissolve
    x "But I can't. His hands hold me in place. I'm completely trapped."
    
    show madd distressed at left_small
    with dissolve
    x "My eyes water. My body trembles. Every part of me wants to scream, but I can't even do that because his mouth has stolen my ability to make sound."
    
    show madd broken at left_small
    with dissolve
    x "I'm no longer in my body. I'm watching this happen from somewhere else, somewhere safe."
    
    show madd helpless at left_small
    with dissolve
    x "This isn't happening to me. This is happening to someone else. I'm not here."
    
    show madd violated at left_small
    with dissolve
    x "His hands continue to move, groping, squeezing, claiming every part of me. His kiss becomes more brutal, more rough, like he's trying to absorb me completely into himself."
    
    show madd broken at left_small
    with dissolve
    x "The aggression in the kiss matches the aggression in his hands. Everything about him is violent. Everything is taking. Everything is possession."
    
    show madd paralyzed at left_small
    with dissolve
    x "Finally, mercifully, he pulls away."
    
    show madd traumatized at left_small
    with dissolve
    x "I gasp for air, my lungs burning. My heart is hammering so hard I think it might break through my ribs."
    
    show brother cruel at right_small
    with dissolve
    brother_says "There. That's how grateful you should be."
    
    show madd traumatized at left_small
    with dissolve
    x "I nod weakly, unable to speak."
    
    scene scene_escape_home_brother_room_brother_standing_up_from_bed_madd_naked_hands_on_chin
    with fade

    show madd distressed at left_small
    with dissolve
    brother_says "Now put on the clothes before I decide you need to earn them a different way."
    
    show madd nervous at left_small
    with dissolve
    x "I dress quickly, my hands still shaking."
    
    show madd boy hesitant at left_small
    with dissolve
    x "First, I reach for the t-shirt. It's oversized, heavy cotton fabric."
    
    show madd boy processing at left_small
    with dissolve
    x "I pull it over my head. The fabric is cool and slightly damp. I wonder if it's from his body, his sweat."
    
    show madd boy anxious at left_small
    with dissolve
    x "As I pull it down, it swallows my frame completely. The neckline hangs loose, the sleeves extend past my elbows."
    
    show madd boy relieved at left_small
    with dissolve
    x "I look down and see that my entire torso is hidden now. My breasts, my waist, all of it completely concealed under the baggy fabric."
    
    x "( Finally. Thank god. At least I don't have to feel his eyes on my chest anymore. )"
    
    show brother cruel at right_small
    with dissolve
    brother_thinks "(Damn. She's completely hidden now. All those curves, all that skin, completely gone under that fabric.)"
    
    show brother sadistic at right_small
    with dissolve
    brother_thinks "(But that's okay. I've seen it. I've memorized it. I can call it up anytime I want.)"
    
    show madd boy hesitant at left_small
    with dissolve
    x "Now for the underwear. Male underwear. Boxer briefs, loose-fitting."
    
    show madd boy processing at left_small
    with dissolve
    x "I pull them on carefully, aware that this transition is important. If anyone at the hostel sees traditional female underwear, it's over."
    
    show madd boy anxious at left_small
    with dissolve
    x "The fabric feels different against my skin—coarser, less soft. It sits differently on my body."
    
    show madd boy nervous at left_small
    with dissolve
    x "They don't conform to my shape like my normal underwear. They hang loose around my hips."
    
    x "These feel like a uniform. The costume of escape. The first piece of my disguise."
    
    show brother obsessed at right_small
    with dissolve
    brother_thinks "(She's putting on my underwear... the ones I wore. Fresh from my drawer. She's wearing a piece of me.)"
    
    show brother cruel at right_small
    with dissolve
    brother_thinks "(I should have done something to mark them. Maybe I'll tell her. Maybe I'll make sure she knows what she's wearing.)"
    
    show madd boy shocked at left_small
    with dissolve
    x "As I pull up the underwear, I notice something immediately—the fabric is damp."
    
    show madd boy horrified at left_small
    with dissolve
    x "And it smells. Unmistakably. Like sweat, like musk, like sex."
    
    show madd boy disgusted at left_small
    with dissolve
    x "My stomach turns."
    
    show madd boy traumatized at left_small
    with dissolve
    x "( He... he wore these. Recently. Very recently. This smells like... like cum. )"
    
    show madd boy trembling at left_small
    with dissolve
    x "The realization makes my whole body recoil, but I've already pulled them on."
    
    show madd boy violated at left_small
    with dissolve
    x "I'm wearing his underwear. Literally carrying his bodily fluids against my most intimate skin."
    
    show brother sadistic at right_small
    with dissolve
    brother_thinks "(Perfect. She knows. She understands now that she's wearing me. That she can't escape that.)"
    
    show brother obsessed at right_small
    with dissolve
    brother_thinks "(Even when she's hiding as a boy, even at her new hostel, she'll be wearing my cum against her skin.)"
    
    show brother possessive at right_small
    with dissolve
    brother_thinks "(She's marked. She's branded. She's mine.)"
    
    show madd boy self loathing at left_small
    with dissolve
    x "Now the jeans. I pull on the baggy cargo pants."
    
    show madd boy processing at left_small
    with dissolve
    x "They're huge on me. The waistband has to be cinched tight with a belt just to stay up."
    
    show madd boy anxious at left_small
    with dissolve
    x "As I fasten the belt, I realize how much fabric is bunched around my hips."
    
    show madd boy numb at left_small
    with dissolve
    x "No curves visible. No shape. Just generic male silhouette."
    
    show madd boy numb at left_small
    with dissolve
    x "I look down and see that my body—the body that defines me as a woman—is completely erased."
    
    show brother cruel at right_small
    with dissolve
    brother_thinks "(The transformation is complete. She doesn't look like the girl I just saw naked anymore.)"
    
    show brother possessive at right_small
    with dissolve
    brother_thinks "(But I know what's under there. I've seen it. I own it.)"
    
    scene scene_escape_home_brother_room_brother_standing_up_from_bed_madd_dressed_in_brother_clothes
    with fade


    show madd boy hesitant at left_small
    with dissolve
    x "Finally, the cap. I pull it on, tucking my hair underneath."
    
    show madd boy conflicted at left_small
    with dissolve
    x "I catch my reflection in his mirror."
    
    show madd boy processing at left_small
    with dissolve
    x "The person staring back at me is a stranger. A boy. Short hair hidden under the cap, loose t-shirt, oversized jeans."
    
    show madd boy shaken at left_small
    with dissolve
    x "My face is the only giveaway—softer features, but my expression is so terrified, so traumatized, that maybe it just reads as a scared kid."
    
    show madd boy numb at left_small
    with dissolve
    x "Not a girl. Not anymore."
    
    show madd boy self loathing at left_small
    with dissolve
    x "( I look like a boy now. But I don't feel like one. I feel like exactly what I am—a girl in boy's clothing, trying to hide from the world. )"
    
    show madd boy hesitant at left_small
    with dissolve
    x "Th-thank you for the clothes. They... they're perfect."
    
    show brother cruel at right_small
    with dissolve
    brother_says "Of course they are. I chose them for a reason."
    
    show brother possessive at right_small
    with dissolve
    brother_says "And remember—you're wearing a piece of me right now. Literally and figuratively."
    
    show madd boy horrified at left_small
    with dissolve
    x "( I am. Oh god, I am. )"
    
    show madd boy determined at left_small
    with dissolve
    x "I turn toward the door, desperate to leave."
    
    show brother possessive at right_small
    with dissolve
    brother_says "Hey. Don't think this is over."
    
    show madd boy shocked at left_small
    with dissolve
    x "W-what do you mean?"
    
    show brother cruel at right_small
    with dissolve
    brother_says "You'll understand soon enough. Just remember—you came to me for help. And now you're bound to me in ways you can't undo."
    
    show madd boy trembling at left_small
    with dissolve
    x "I nod weakly, not understanding but too afraid to ask for clarification."
    
    show madd boy broken at left_small
    with dissolve
    x "I stand there, frozen, realizing the horrible truth."
    
    show madd boy defeated at left_small
    with dissolve
    x "I came to escape. To find freedom. But all I've done is walk deeper into his web."
    
    show madd boy violated at left_small
    with dissolve
    x "I'm wearing him. I'm marked by him. I can never truly escape what he's done to me, no matter how far I run."
    
    show madd boy broken at left_small
    with dissolve
    x "( I'm not free. I'll never be free. )"
    $ got_male_clothes=True

    
    $ character_relations["brother"]["undressed_madd"] += 1
    $ character_relations["brother"]["kissed"] += 1
    $ character_relations["brother"]["groped_madd"] += 1
    $ stat_notification = "Escape clothes obtained from brother"
    $ renpy.pause(2.0)
    $ stat_notification = ""
    
    jump continue_runaway_preparation


label continue_runaway_preparation:
    python:
        if game_time.is_morning() or game_time.is_afternoon():
            madd_room_scene = "scene_madd_home_room_morning_afternoon"
        elif game_time.is_evening():
            madd_room_scene = "scene_madd_home_room_evening"
        else:  # night
            madd_room_scene = "scene_madd_home_room_night"
    
    scene expression madd_room_scene
    with fade
    show madd boy working at left_small
    with dissolve
    x "I check my backpack one more time. Everything I need is here."
    
    show madd boy determined at left_small
    with dissolve
    x "The cram school enrollment is paid. I have enough money. Now I just need to leave when everyone is asleep."
    
    show madd boy disgusted at left_small
    with dissolve
    x "( They have no idea what's about to happen. In a few hours, I'll be gone. )"
    
    show madd boy relieved at left_small
    with dissolve
    x "( And I'll never have to come back to this nightmare. )"
    
    show madd boy hesitant at left_small
    with dissolve
    x "I take one final look at my room. Goodbye to this place. Goodbye to this life."
    
    show madd boy determined at left_small
    with dissolve
    x "( My new life starts tonight. )"
    
    $ madd_money -= 0
    
    jump outside_home


label dad_walks_in_madd_room_sleep:
    # Dad walks into Madd's room while she's sleeping
    # This triggers when the room is unlocked and dad's lust is >= 80
    scene scene_madd_sleep_on_bed_my_room
    with fade


    "The stepfather walks into Madd's room quietly while she's asleep, the darkness of the night concealing his intrusion."   
    scene scene_dad_walks_in_madd_room_sleep_dad_looking_at_madd_sleeping
    with fade

    show dad possessive at right_small
    with dissolve
    "He gazes down at her sleeping form with predatory hunger in his eyes, watching the gentle rise and fall of her chest in the darkness."
    scene scene_dad_walks_in_madd_room_sleep_dad_sitting_beside_madd_bed
    with fade
    show dad lustful at right_small
    with dissolve
    "He pulls a chair over with deliberate slowness and sits down beside her bed, his breathing already becoming heavy as he stares at her defenseless form."

    scene scene_dad_walks_in_madd_room_sleep_dad_sitting_beside_madd_bed_hand_reaching_towards_her_face
    with fade
    show dad possessive at right_small
    with dissolve
    "His hand reaches out slowly, trembling with desire. His fingers brush across her lips with a gentle touch that belies the darkness in his intentions, testing her softness, attempting to slip his finger between her lips."
    show dad lustful at right_small
    with dissolve
    "Madd remains lost in deep sleep, blissfully unaware of the violation happening mere inches from her face."

    scene scene_dad_walks_in_madd_room_sleep_dad_sitting_beside_madd_bed_hand_running_through_her_hair
    with fade

    "His second hand moves to her hair, fingers threading through the silken strands with reverence and possessiveness. He caresses her arm slowly, feeling the smooth warmth of her skin under his calloused palms."
    show dad possessive at right_small
    with dissolve
    dad_says "You look so peaceful when you sleep, Maddie.."
    show dad lustful at right_small
    with dissolve
    "He continues running his hand through her hair and down her arm, savoring every moment of touching her soft, unresisting skin. His breathing grows heavier, more labored."
    "Madd's body begins to shift in her sleep, a sign that consciousness is slowly pulling her from the depths of slumber."

    scene scene_dad_walks_in_madd_room_sleep_dad_sitting_beside_madd_bed_madd_waking_up
    with fade
    show madd shocked at left_small
    with dissolve
    x "( Huh... what... where am I... )"
    show madd distressed at left_small
    with dissolve
    x "( Dad's hand... his fingers... they're in my hair... and his other hand on my arm... )"
    show madd paralyzed at left_small
    with dissolve
    x "( What is he doing in my room... in the middle of the night... )"
    show madd nervous at left_small
    with dissolve
    x "What are you doing here? "
    
    show madd helpless at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    dad_says "I'm here to look at my wife. "
    
    show madd violated at left_small
    with dissolve
    x "( He's calling me his wife... the word makes my skin crawl... )"
    x "( I notice him slowly withdraw his hand from my arm, but his fingers remain tangled in my hair, gripping tightly. )"
    
    show madd conflicted at left_small
    with dissolve
    x "( I need to be careful here... I can't provoke him... but I also need to make him leave... )"
    x "( Every fiber of my being wants to scream and push him away, but I know that won't work... )"
    
    show madd violated at left_small
    with dissolve
    x "I... I'm not...  "
    
    show madd distressed at left_small
    with dissolve
    x "( I need to keep him calm... to manage this situation... )"
    
    show madd shaken at left_small
    with dissolve
    x "Can you please leave? "
    x "( My legs curl up on the bed, and my head lowers slightly, a instinctive gesture of submission and fear. )"

    scene scene_dad_walks_in_madd_room_sleep_dad_sitting_beside_madd_dad_angry_lifting_madd_head_by_hair
    with fade

    show madd feels violated at left_small
    with dissolve
    x "( I can hear his breathing... it's getting heavier... deeper... more labored... He's getting angry... I can feel the rage building in him like a storm... )"
    
    show madd paralyzed at left_small
    with dissolve
    x "( Oh god, I said something wrong... I said something that made him angry... )"
    x "( Suddenly I feel sharp, painful pulls on my hair... he's yanking me upward with brutal force... his grip unrelenting... my scalp screaming in agony... )"
    
    show madd violated at left_small
    with dissolve
    show dad angry at right_small
    with dissolve
    dad_says "I am your husband! Don't you DARE tell me what to do in my own house!"
    
    show madd broken at left_small
    with dissolve
    show dad dominant at right_small
    with dissolve
    x "( His voice is a growl, filled with rage and entitlement. His pull makes my entire body jolt, forcing me to sit up on the bed against my will. )"
    
    show madd distressed at left_small
    with dissolve
    show dad cruel at right_small
    with dissolve
    dad_says "You can't tell me to leave. "
    
    show madd helpless at left_small
    with dissolve
    x "( And another violent pull... my head wrenches backward, my neck straining under the force... the pain is white-hot and overwhelming... )"
    
    show madd traumatized at left_small
    with dissolve
    show dad sadistic at right_small
    with dissolve
    dad_says "Got it?!"
    
    show madd shaken at left_small
    with dissolve
    x "( Through tears, I nod... the only gesture I can manage... )"
    x "I... I get it.. husband..."
    
    show madd relieved at left_small
    with dissolve
    x "( I feel his grip slowly weakening on my hair... his fingers uncurling from their vicious hold... I feel a brief moment of relief, knowing the immediate violence has passed... )"

    scene scene_dad_walks_in_madd_room_sleep_dad_sitting_beside_madd_dad_hand_on_her_cheeks
    with fade    
    
    show madd uncertain at left_small
    with dissolve
    x "( His hand now descends to my cheeks, his touch shifting from violent to deceptively gentle... he caresses my skin slowly, as if he hadn't just been hurting me... )"
    x "( I feel a shiver run through my entire body... fear and confusion mixing together... )"
    
    show madd distressed at left_small
    with dissolve
    x "( He pulls my face closer to his... I can smell him now... the scent of whiskey and tobacco mixing with his musky, predatory pheromones... so much raw male scent flooding my senses... )"
    
    show madd paralyzed at left_small
    with dissolve
    x "( His finger trails across my lips, his intent clear... he points it toward my mouth, commanding without words... )"
    
    show madd helpless at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    dad_says "Okay now take it in your mouth."
    
    show madd trembling at left_small
    with dissolve
    x "( My lips part hesitantly, my body betraying my will as his thick finger pushes past my teeth into the warm cavity of my mouth... )"
    x "( I can taste him... the bitterness of alcohol mixed with the rough, stale taste of cigarettes coating my tongue... it's revolting... )"
    
    show madd violated at left_small
    with dissolve
    x "( He moves his finger around in my mouth with deliberate slowness, exploring, claiming, marking... I can feel the roughness of his calloused hands... I gag slightly, my throat constricting... )"
    
    show madd broken at left_small
    with dissolve
    x "( He's making me get accustomed to the taste of him... he's conditioning me... I know what he's going to make me do next... I can feel it in the way his breathing deepens, in the hardness pressing against my stomach... )"
    
    show madd paralyzed at left_small
    with dissolve
    x "( He puts his finger deeper into my mouth... with a rhythmic motion he moves it in and out... in and out... like he's practicing... preparing me for something worse... )"
    
    show madd distressed at left_small
    with dissolve
    x "( He was preparing me... conditioning me to obey him in any way he wants... making my body learn submission... )"
    
    show madd broken at left_small
    with dissolve
    x "( I close my eyes and try to relax, trying to make this easier on myself... trying to distance myself mentally from what's happening... Finally he lets go of my face... )"
    x "( I thought the worst was over... surely it is... )"

    scene scene_dad_walks_in_madd_room_sleep_dad_sitting_beside_madd_dad_hand_on_her_waist_lifting_her_up
    with fade
    
    show madd shocked at left_small
    with dissolve
    x "( Suddenly, without warning, his powerful hands grip my waist and he lifts me with ease, pulling me toward him... I gasp in surprise, my body going rigid... )"
    x "( He positions me on his lap, my legs on either side of his hips... )"
    
    show madd horrified at left_small
    with dissolve
    x "( I was very close to his face now... I can smell him more intensely... so much potent pheromones radiating from him, thick and suffocating... )"
    x "( I feel his hardness pressing insistently against my thigh, hot and demanding, the evidence of his lust impossible to ignore... )"
    
    show madd paralyzed at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "( He lowers his face to mine... and in his eyes, I see nothing but raw, predatory lust... pure animal desire... I feel scared... terrified... and then his lips are on mine... )"
    
    show madd violated at left_small
    with dissolve
    show dad dominant at right_small
    with dissolve
    x "( His kiss is forceful... demanding... there's no tenderness, no affection, only possession and domination... I try to pull away but his hands tighten on my waist, his grip unbreakable... )"
    
    scene scene_dad_walks_in_madd_room_sleep_madd_on_dads_lap_kissing_deeper
    with fade

    show dad sadistic at right_small
    with dissolve
    show madd distressed at left_small
    with dissolve
    x "( He pushes his tongue deep into my mouth... it's thick and invasive... I can taste him more strongly now... the full flavor of alcohol and cigarettes coating every inch of my tongue... I gag... )"
    
    show madd helpless at left_small
    with dissolve
    x "( His tongue is rough and invasive... it moves with aggressive intent... I feel so violated... so completely invaded... )"
    
    show madd broken at left_small
    with dissolve
    x "( He penetrates deeper into my mouth with his tongue, like he's trying to claim ownership of my very core... I feel like he's trying to absorb me entirely, to take over my being from the inside... I feel so helpless... so utterly powerless... )"
    
    show madd paralyzed at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "( I have no option but to let him do whatever he wants... his hands move from my waist to my breasts... and he squeezes them roughly, kneading the soft flesh with aggressive possessiveness... I cry out softly against his mouth... )"
    
    show madd traumatized at left_small
    with dissolve
    x "( He has full control over me... I am completely at his mercy... nothing I do or say matters... my body is just an object for his use... )"
    
    show madd violated at left_small
    with dissolve
    x "( He was pulling my breasts while his tongue licks against mine... the sensation is overwhelming and nauseating... I feel so broken... so completely shattered... )"
    
    scene scene_dad_walks_in_madd_room_sleep_madd_on_dads_lap_kissing_deeper_lift_legs_parting
    with fade
    
    show madd horrified at left_small
    with dissolve
    show dad sadistic at right_small
    with dissolve
    x "( Suddenly, while continuing to kiss me deeply, he lifts me up and spreads my legs wide, forcing them to part on either side of his hips, then drops me back down... )"
    x "( Now I'm straddling him, my most intimate area pressed against his hardness... )"
    
    show madd distressed at left_small
    with dissolve
    x "( This position makes me feel so incredibly vulnerable... so completely exposed... it's such an intimate, submissive position... I feel so utterly exposed and defenseless... )"
    
    show madd helpless at left_small
    with dissolve
    x "( He continues kissing me deeply, his hands on my hips, controlling my movements... I'm like a toy to him... a doll he can position and use however he wants... )"
    
    scene scene_dad_walks_in_madd_room_sleep_madd_on_dads_lap_kissing_deeper_lift_legs_parting_kiss_madd_resisting
    with fade
    
    show madd paralyzed at left_small
    with dissolve
    show dad cruel at right_small
    with dissolve
    x "( Now with my legs parted completely, he has full control over me... I try to resist with my hands, pushing against his chest, trying to create distance between us... )"
    
    show madd self loathing at left_small
    with dissolve
    x "( But his grip was too strong... his strength is overwhelming... I can't escape... I can't break free... )"
    x "( He continues his assault with his tongue in my mouth, ignoring my attempts at resistance... )"
    
    scene scene_dad_walks_in_madd_room_sleep_madd_on_dads_lap_kissing_deeper_lift_legs_parting_kiss_madd_resisting_2
    with fade
    
    show madd broken at left_small
    with dissolve
    x "( His tongue now explores my entire face... it felt like he was trying to consume me whole... I'm like prey caught in the jaws of a predator... a bird whose wings are being torn apart by a hawk... )"
    
    show madd weeping at left_small
    with dissolve
    x "( I knew resistance was futile... there was no point in fighting... all it does is make things worse... I had to give in... I had to accept what was happening... )"
    
    scene scene_dad_walks_in_madd_room_sleep_madd_on_dads_lap_kissing_deeper_lift_legs_parting_kiss_madd_giving_in
    with fade
    
    show madd broken at left_small
    with dissolve
    x "( I stop resisting and let him do whatever he wants... I close my eyes and mentally check out... I drift away from my body... )"
    x "( My mouth opens slightly, passively... allowing his tongue to go deeper... letting him take over... )"
    
    show madd resigned at left_small
    with dissolve
    x "( His heavy breathing mingles with mine... I'm trapped in his kiss... trapped in his embrace... there's no escape... )"
    x "( I knew the only way out of this is to let him have his way... to surrender completely... to stop fighting... )"
    
    show madd helpless at left_small
    with dissolve
    x "( I surrender myself to him entirely... He has already won... He knows I am his... )"
    
    scene scene_dad_walks_in_madd_room_sleep_madd_on_dads_lap_kissing_deeper_lift_legs_parting_kiss_madd_giving_in_2
    with fade

    show madd violated at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "( As he felt that he had completely won, that I had completely submitted, he pulls away slightly... I gasp desperately for air, my lungs burning, my heart racing... )"
    
    show madd trembling at left_small
    with dissolve
    x "( Immediately, almost without thinking, I lean back toward his mouth and kiss him back... it's a gesture meant to show him I was his... that I accepted my role... )"
    
    show madd submissive nod at left_small
    with dissolve
    x "( My body was moving on its own... I was kissing him back... I was submitting... showing him with actions what words could never express... )"    
    
    show madd resigned at left_small
    with dissolve
    x "( Now that he knew I was completely submitting, his aggression softens slightly... His kisses became slightly softer... less immediately demanding... but no less possessive... )"
    
    show madd distressed at left_small
    with dissolve
    x "( With every lick of his tongue across mine... with every soft bite of my lips... I felt more and more broken inside... more and more owned by him... his touch was like a brand, marking me as his property... )"
    
    show madd broken at left_small
    with dissolve
    x "( And some part of me... some dark, twisted part deep inside... was starting to feel a confused pleasure in this submission... in this absolute ownership... in being completely claimed... )"

    scene scene_dad_walks_in_madd_room_sleep_madd_on_dads_lap_kissing_deeper_lift_legs_parting_lick_to_kiss_madd_submitting
    with fade
    
    show madd resigned at left_small
    with dissolve
    x "( Then he moved lower... his mouth left mine and traveled downward... he pulled my hair, forcing my head to arch back exposing my entire neck... )"
    x "( Now he was licking my neck... his tongue tracing the delicate skin with deliberate slowness... )"
    
    show madd trembling at left_small
    with dissolve
    x "( For me, my neck is so incredibly sensitive... a place where every nerve ending screams... His tongue on my neck made me shiver involuntarily... despite myself... despite my revulsion... )"
    
    show madd violated at left_small
    with dissolve
    x "( He bit my neck softly at first, then harder... making me gasp involuntarily... then immediately went back to kissing my lips... the contrast between pain and tenderness was dizzying... )"
    
    show madd resigned at left_small
    with dissolve
    x "( I wasn't refusing him anymore... there was no point... I was his... completely his... he could do whatever he wanted with me... )"
    
    scene scene_dad_walks_in_madd_room_sleep_madd_on_dads_lap_kissing_deeper_lift_legs_parting_lick_to_kiss_madd_submitting_2
    with fade

    show madd broken at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "( My body was completely his now... My mind was his... I was completely under his control... there was nothing left of me that wasn't his... )"
    
    show madd broken at left_small
    with dissolve
    show dad dominant at right_small
    with dissolve
    x "( I was his wife... his property... his to use and discard as he saw fit... )"
    
    show madd helpless at left_small
    with dissolve
    show dad sadistic at right_small
    with dissolve
    x "( He roughly kissed me, his mouth dominating mine, while his hands lifted my shirt up... exposing my bare back to the cool night air... His hands roamed across my skin, rough and possessive... Making me shiver with a mixture of cold and dread... )"

    scene scene_dad_walks_in_madd_room_sleep_madd_on_dads_lap_kissing_deeper_lift_legs_parting_licking_neck_1
    with fade
    
    show madd distressed at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "( He pulled my hair again, the sharp pain making my entire head arch backward, exposing the full length of my neck to him... then he started licking my neck again... )"
    
    show madd trembling at left_small
    with dissolve
    x "( He licked it like I was ice cream on a hot summer day... methodical... savoring... and honestly, he wasn't entirely wrong... I was melting under his touch... under his complete control... despite the horror of it all... )"
    
    show madd violated at left_small
    with dissolve
    x "( I felt his tongue moving slowly from the top of my neck to the side... then to the front... then back again... tracing every line, every curve... )"
    
    show madd resigned at left_small
    with dissolve
    x "( He was marking my entire neck with his tongue and saliva... claiming me... making sure that anyone who saw me would know exactly who I belonged to... )"

    scene scene_dad_walks_in_madd_room_sleep_madd_on_dads_lap_kissing_deeper_lift_legs_parting_licking_neck_2
    with fade
    
    show madd helpless at left_small
    with dissolve
    show dad sadistic at right_small
    with dissolve
    x "( I felt his mouth watering over my neck... his tongue moving faster now... more aggressively... with increased hunger... )"
    
    show madd distressed at left_small
    with dissolve
    x "( So much saliva dripping from his mouth onto my neck and chest... I could smell it now... the pungent, musky scent mixing with the taste of him on my skin... )"
    
    show madd broken at left_small
    with dissolve
    x "( His stinky saliva on my neck was the permanent mark of his claim over me... a visible sign to anyone who might see that I was his... )"
    
    show madd broken at left_small
    with dissolve
    x "( I was drowning in his lust... suffocating in his possessive need... lost in his smell and taste... completely consumed by his desires... )"
    
    show madd traumatized at left_small
    with dissolve
    x "( My entire neck must be absolutely soaked in his saliva by now... dripping down my shoulders... the evidence of his ownership unmistakable... )"

    scene scene_dad_walks_in_madd_room_sleep_madd_on_dads_lap_kissing_deeper_lift_legs_parting_licking_neck_spanking
    with fade
    
    show madd shocked at left_small
    with dissolve
    show dad cruel at right_small
    with dissolve
    x "( Suddenly, without warning, I feel his hand land hard on my buttocks... he spanks me with surprising force... I had no energy to resist... no energy left to scream... )"
    
    show madd distressed at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "( He lifts my shorts up slightly and rubs his hand roughly on my bare skin... the touch both burning and arousing in a way that makes me hate myself... I gasp in surprise and conflicted shame... )"
    
    show madd broken at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "( He rubs his hand roughly on my ass, kneading it like dough, marking it with his touch... only desperate, involuntary moans escape from my mouth, sounds I can't control... )"
    
    show madd resigned at left_small
    with dissolve
    x "( His tongue was consuming me... eating me whole... and his hands were kneading my body like I was clay to be molded in his image... I was his creation... his possession... his to keep forever... )"

    x "(He continues kissing and licking my neck, as his hands reach down to the waistband of my shorts I knew what was coming next...)"
    
    
    scene scene_dad_walks_in_madd_room_sleep_madd_on_dads_madd_underessing
    with fade

    x "(By that point, i had no willpower left to resist him...I let him do whatever he wanted to me...)"
    x "(I even lifted my leg to let him slide my shorts down my hips...)"
    x "(And then he threw away my shorts and continued his assault on my neck)"
    x "(I was bottom naked now, with my stepdad's hands and mouth all over me...)"
    x "(Sitting on his lap,  He had fully taken control of me...)"

    scene scene_dad_walks_in_madd_room_sleep_naked_madd_on_dad_lap_groping_1
    with fade

    show madd helpless at left_small
    with dissolve
    x "(As soon as he gains access to my bare skin, he starts caressing my buttocks and thighs with possessive slowness...)"
    
    show madd distressed at left_small
    with dissolve
    x "(I feel his fingers reaching my exposed butthole...I'm so exhausted and overwhelmingly aroused that I find I don't even resist...)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(Normally he takes his time...normally my butthole would involuntarily clench when he attempts to touch it...)"
    
    show madd violated at left_small
    with dissolve
    x "(But this time it's different...My body is begging for more...it's as if my body is willingly allowing him entry...)"
    
    show madd broken at left_small
    with dissolve
    x "(He pushes two fingers inside my butthole before I even fully process it...using them to methodically stretch me open...)"
    
    show madd resigned at left_small
    with dissolve
    x "(Slowly his other hand reaches down to my left ass cheek...He begins massaging it with firm, claiming touches...)"
    
    show madd helpless at left_small
    with dissolve
    x "(He's exploring my ass like a cave explorer claiming new territory...and I let him do it...I don't resist...)"
    scene scene_dad_walks_in_madd_room_sleep_naked_madd_on_dad_lap_groping_2
    with fade
    
    show madd trembling at left_small
    with dissolve
    x "(Once again he uses his hands to massage the sensitive area near my butthole as if trying to soothe and stretch it simultaneously...)"
    
    show madd distressed at left_small
    with dissolve
    x "(I'm utterly lost now...I don't know where I am anymore...my mind adrift in a sea of sensation...)"
    
    show madd helpless at left_small
    with dissolve
    x "(But here I am...completely naked, sitting on my stepfather's lap in my own private sanctuary...)"
    
    show madd resigned at left_small
    with dissolve
    x "(Waiting for him to finish having his way with me...)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(Once again he pushes his index and middle finger inside my tight little opening...penetrating me with deliberate intent...)"
    
    show madd violated at left_small
    with dissolve
    x "(I'm so exhausted that my face barely manages to stay upright...I find myself leaning heavily against him...My face started moving downward uncontrollably...)"
    
    show madd broken at left_small
    with dissolve
    x "(It ends with his nose pressing into my mouth...Normally I would have gagged and pushed him away in revulsion...but now I'm too drained to care...too consumed by what's happening...)"
    
    scene scene_dad_walks_in_madd_room_sleep_naked_madd_on_dad_lap_fingering_madd_butt_1
    with fade
    
    show madd trembling at left_small
    with dissolve
    x "(Suddenly he begins accelerating his rhythm...His fingers moving in and out of my ass at an increasingly frantic pace...)"
    
    show madd distressed at left_small
    with dissolve
    x "(He's still kissing my face passionately...his teeth grazing against my cheek and jawline...claiming every inch of my skin...)"
    
    show madd helpless at left_small
    with dissolve
    x "(I'm melting completely into his lap...my eyes fluttering closed...all resistance evaporating...I'm surrendering to whatever he intends for me...)"
    
    show madd violated at left_small
    with dissolve
    x "(Something warm and wet leaks from my deepest places...my own shameful fluids...I'm thoroughly drenched from his relentless fingering of my most intimate opening...)"
    
    show madd shocked at left_small
    with dissolve
    x "(No no no...He absolutely noticed that...He felt my wetness...and him recognizing my arousal means only one terrible thing...he'll use it to push me further...)"
    
    show madd broken at left_small
    with dissolve
    x "(He knows I'm betraying myself by enjoying this...the wet squelching sound of his fingers thrusting relentlessly in and out is unmistakable evidence of my shameful pleasure...)"
    
    show madd resigned at left_small
    with dissolve
    x "(The entire room is filled with that obscene, rhythmic sound...echoing our depravity...)"
    
    show madd trembling at left_small
    with dissolve
    x "(He knows exactly what my body is revealing to him...and he'll weaponize my own pleasure against me...using it to drag me deeper into degradation...)"
    scene scene_dad_walks_in_madd_room_sleep_naked_madd_on_dad_lap_fingering_madd_butt_2
    with fade
    
    show madd trembling at left_small
    with dissolve
    x "(He maintains his unrelenting invasion of my ass...his fingers plunging progressively deeper with each forceful thrust...stretching me wider...)"
    
    show madd flustered at left_small
    with dissolve
    x "(My body commits complete betrayal...becoming increasingly aroused from his relentless fingering...my nipples hardening into aching, sensitive peaks...my breathing transforming into ragged, desperate gasps...)"
    
    show madd helpless at left_small
    with dissolve
    x "(Soft moans escape my lips beyond my control...my body responding involuntarily to his penetrating invasion...I can't suppress these sounds...these shameful admissions of pleasure echoing in the darkness...)"
    
    show madd shocked at left_small
    with dissolve
    x "(He definitely hears every whimper...and responds by viciously accelerating his rhythm...driving deeper...faster...with increased aggression...)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(I'm losing all authority over my own body...it's operating of its own primitive volition...craving his domination...wanting to be penetrated...used...claimed entirely...)"
    
    show madd broken at left_small
    with dissolve
    x "(My body responds like an animal in heat...desperate to be bred...every nerve ending screaming for his invasion...but I can't surrender to true breeding...not from him...not from my own father...)"

    scene scene_dad_walks_in_madd_room_sleep_naked_madd_on_dad_removing_jeans
    with fade

    show madd shocked at left_small
    with dissolve
    x "(Suddenly he slightly pushes me aside onto the bed...his movements commanding and absolute...)"
    
    show madd violated at left_small
    with dissolve
    x "(The moment my back meets the mattress, my legs involuntarily spread wide apart...something primal within me is demanding submission...preparing my body for his inevitable invasion...)"
    
    show madd distressed at left_small
    with dissolve
    x "(He rises above me and removes his jeans...revealing his fully engorged dick...hardened to its maximum potent capacity...)"
    
    show madd horrified at left_small
    with dissolve
    x "(It's absolutely enormous...throbbing with intense heat...a sight I've never witnessed in such an aggressively aroused state...)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(I've glimpsed it before, certainly...but now it's profoundly different...this moment defines everything...today is when he forcefully penetrates me)"
    
    show madd broken at left_small
    with dissolve
    x "(I can only offer him one remaining thing...my ass...I cannot let him have my virginity I still possess...I cannot permit him to impregnate me by cumming in my pussy...I must fiercely protect that last boundary...)"
    
    show dad possessive at right_small
    with dissolve
    dad_thinks "Her ass was absolutely begging for my cock...the way it was clenching when she reached climax...If I push too hard to fuck her in her pussy she might resist and ruin everything..."
    
    show dad lustful at right_small
    with dissolve
    dad_thinks "I could settle for her ass today...but I can feel she's finally ready...soon she'll be desperately begging me to fill her pussy...begging to carry my seed..."
    
    show madd helpless at left_small
    with dissolve
    x "(He approaches...positions himself above me...his massive, throbbing dick hovering mere inches from my vulnerable body...the radiating heat nearly scorching my exposed flesh...)"


    scene scene_dad_walks_in_madd_room_sleep_naked_madd_on_dad_inserting_manhood_into_butt
    with fade
    
    show madd paralyzed at left_small
    with dissolve
    x "(He repositions me onto his lap...forcing me to face away...where I'm powerless to see what's coming...his iron grip securing my complete immobilization...)"
    
    show madd helpless at left_small
    with dissolve
    x "(With commanding authority, he lifts me effortlessly...positioning my exposed ass directly above his throbbing dick...)"
    
    show madd distressed at left_small
    with dissolve
    x "(The heat radiating from his enormous cock is nearly unbearable...pulsing against my trembling skin...hovering so dangerously close to my most vulnerable entrance...the anticipation is suffocating...)"
    
    show madd horrified at left_small
    with dissolve
    x "(This is the moment...he's finally going to penetrate me from behind...claim my ass with his full length...I can feel it coming inevitably...)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(His musky masculine scent surrounds me completely...intoxicating...primal...filling my senses completely...the entire room reeks of his raw male power and lust...)"
    
    show dad calculating at right_small
    with dissolve
    dad_thinks "She's tense...I need to ease into this carefully...if she's too resistant it'll spoil my moment...I'll take it slow...allow her to adjust to my size..."
    
    show madd distressed at left_small
    with dissolve
    x "(He presses his massive cockhead firmly against my tight little asshole...the pressure is immense...I can feel every prominent ridge and vein of his dick pushing insistently against my entrance...)"
    
    show madd broken at left_small
    with dissolve
    x "(Oh god...this is really happening...he's going to enter me...I can feel the inevitable penetration approaching...my entire body convulsing with primal terror and unwanted anticipation...)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "Relax honey...let me in...surrender completely to me..."
    
    show madd resigned at left_small
    with dissolve
    x "(I don't scream...don't resist...what would be the point...I simply surrender entirely and let it happen...I feel his massive cock slowly breaching me from behind...stretching my ass wider than I ever conceived possible...)"
    
    show madd helpless at left_small
    with dissolve
    x "(One leg remains planted on the bed while the other is captured firmly in his grip...being pulled open so he can have easier access to my asshole.)"
    
    show madd violated at left_small
    with dissolve
    x "(The residual wetness from his earlier invasive fingering eases his passage somewhat...my ass reluctantly accommodating his massive girth with reluctant)"
    
    show madd broken at left_small
    with dissolve
    x "(Inch by agonizing inch he drives deeper into me...I feel each centimeter of his throbbing dick filling my core...stretching me to my absolute limit...)"
    
    show madd distressed at left_small
    with dissolve
    x "(His pulsing heat fills me completely...stretching my innermost places to their breaking point...I feel utterly impaled...invaded from deep within...my body a willing vessel for his complete domination...)"
    
    show madd traumatized at left_small
    with dissolve
    x "(I'm being penetrated by my own father...my body forced to accommodate his breeding dick...positioned between his legs )"
    
    show madd broken at left_small
    with dissolve
    x "(He stands, maintaining his firm grip on my waist...his massive cock buried even deeper inside me as this new position shifts him even further into my depths...)"

    scene scene_dad_walks_in_madd_room_sleep_naked_madd_on_dad_inserting_manhood_into_butt_2
    with fade
    
    show madd distressed at left_small
    with dissolve
    x "(He initiates his first slow, deliberate thrusts...each movement pushing his enormous dick deeper into my stretched ass...claiming new territory with every stroke...)"
    
    show madd helpless at left_small
    with dissolve
    x "(He's not fully sheathed inside me yet...but I can feel my body being stretched open...every thrust reaching deeper...accessing places I never knew existed...)"
    
    show madd resigned at left_small
    with dissolve
    x "(He moves with deliberate, measured slowness...allowing my ass to adjust to his massive girth...methodical...patient...building toward something far more intense and demanding...)"
    
    show madd shocked at left_small
    with dissolve
    x "(He's such a calculated predator...every movement is precisely planned...designed to maximize my submission while pleasing his own dark desires...I can see the calculated intention burning in his predatory eyes...)"
    
    show madd broken at left_small
    with dissolve
    x "(His dick seems to grow even larger inside me...hardening further with each passing moment...I'm being consumed completely by him...utterly claimed by my own father...)"

    scene scene_dad_walks_in_madd_room_sleep_naked_madd_on_dad_anal_fully_inserted_1
    with fade
    
    show madd distressed at left_small
    with dissolve
    x "(He slowly lowers himself down...pulling me along with him...His dick is now completely buried inside me...filling me with overwhelming fullness...)"
    
    show madd helpless at left_small
    with dissolve
    x "(I can feel the complete length of his dick occupying my depths...it looked deceptively massive earlier...and now that it's fully sheathed inside me...I can feel every prominent inch of it...)"
    
    show madd broken at left_small
    with dissolve
    x "(It stops expanding...I suppose he's reached his absolute peak arousal now...I can feel the intense throbbing heat of it deep inside me...it's making me feel so overwhelmingly full and warm...)"
    
    show madd violated at left_small
    with dissolve
    x "(With one hand he holds me firmly from my waist...with the other hand he's spreading my legs even wider apart...exposing my buttocks more completely to him...)"
    
    show madd resigned at left_small
    with dissolve
    x "(Giving him optimal access to penetrate me deeper...making it easier for him to thrust with maximum force...)"
    
    show madd broken at left_small
    with dissolve
    x "(I couldn't believe this was actually happening...My own father was fucking me in the ass...taking me from behind with primal intensity...I felt simultaneously so completely debased yet strangely aroused...)"
    
    scene scene_dad_walks_in_madd_room_sleep_naked_madd_on_dad_anal_fully_inserted_2
    with fade
    
    show madd trembling at left_small
    with dissolve
    x "(I can't suppress my soft moans as he begins his relentless thrusting movements...his dick moving rhythmically in and out of me...)"
    
    show madd distressed at left_small
    with dissolve
    x "(The sound of my buttocks slapping hard against his thighs fills the entire room...mixing with my involuntary moans and his heavy breathing...)"
    
    show madd violated at left_small
    with dissolve
    x "(It's so humiliating to hear those explicit, undeniable sounds...But simultaneously it's so arousing...I felt so completely used...So utterly owned by him...)"
    
    show madd resigned at left_small
    with dissolve
    x "(This is not how a stepfather and stepdaughter should be...but here we are...My father fucking me in the ass with brutal intent...)"
    
    show madd broken at left_small
    with dissolve
    x "(I'm certain in that moment he views me as his wife...Not his stepdaughter...He's claiming me as his intended bride...His breeding companion...His property...)"
    
    scene scene_dad_walks_in_madd_room_sleep_naked_madd_on_dad_anal_fully_inserted_3
    with fade
    
    show madd trembling at left_small
    with dissolve
    x "(He begins thrusting with increased aggression and speed...)"
    
    show madd distressed at left_small
    with dissolve
    x "(The taboo nature of our incestuous act is making it increasingly arousing to some dark part of me...I felt so wickedly immoral...So completely wrong...Yet paradoxically so intensely right...)"
    
    show madd helpless at left_small
    with dissolve
    x "(My body is responding helplessly to his relentless thrusts...My nipples hardening into sensitive peaks...My breathing becoming increasingly ragged and desperate...My moans growing progressively louder...my most intimate places becoming increasingly wet...)"
    
    show madd broken at left_small
    with dissolve
    x "(I can feel the pleasure building intensely inside me...My entire being feels engulfed in flames...I'm so impossibly close to climax...)"
    
    scene scene_dad_walks_in_madd_room_sleep_naked_madd_on_dad_anal_fully_inserted_4
    with fade
    
    show madd overwhelmed at left_small
    with dissolve
    x "(He accelerates his pace even more aggressively...with his hands he's forcefully pushing my hips down onto his dick...ensuring it penetrates as deep as physically possible with each brutal thrust...)"
    
    show madd violated at left_small
    with dissolve
    x "(And he himself is pushing upward simultaneously...ensuring his dick reaches the absolute deepest recesses of my being...)"
    
    show madd trembling at left_small
    with dissolve
    x "(The sensation is absolutely overwhelming...I can feel the pleasure accumulating intensely inside my entire body...My whole being is trembling uncontrollably...)"
    
    show madd broken at left_small
    with dissolve
    x "(And I'm certain he can feel it too...my ass tightening involuntarily around his dick...My moans becoming increasingly louder and more desperate...)"
    

    scene scene_dad_walks_in_madd_room_sleep_naked_madd_on_dad_anal_climax
    with fade

    show madd distressed at left_small
    with dissolve
    x "(Suddenly I feel it...His dick becoming progressively harder and even more engorged inside me...)"
    
    show madd trembling at left_small
    with dissolve
    x "(His breathing becoming increasingly heavier...He's approaching his climax...I can sense it building...)"
    
    show madd shocked at left_small
    with dissolve
    x "(I can feel it intensely...The building warmth...The mounting pressure...He's about to reach his peak and release...)"
    
    show madd violated at left_small
    with dissolve
    x "(And then I feel it...Thick, scorching hot liquid shooting deep inside me...)"
    
    show madd broken at left_small
    with dissolve
    x "(My father is climaxing inside me...flooding me with his seed...marking me completely from the inside...)"
    
    show madd distressed at left_small
    with dissolve
    x "(I'm relieved it's not in my pussy...but still...I can feel his cum penetrating deep inside me...settling inside my depths...)"
    
    show madd helpless at left_small
    with dissolve
    x "(Allowing him to fill me like this...It makes me feel so completely debased...So thoroughly used and discarded...)"
    
    show madd violated at left_small
    with dissolve
    x "(My body involuntarily clenches around him...trying desperately to milk every last drop from his dick...as my face lowers against his, kissing his cheek)"
    
    show madd broken at left_small
    with dissolve
    x "(He never stops his thrusting...continuing relentlessly while I feel his hot seed filling me completely...)"
    
    show madd resigned at left_small
    with dissolve
    x "(I can feel it dripping out of me...mixing with my own shameful juices...)"
    
    show madd conflicted at left_small
    with dissolve
    x "(This is profoundly wrong...allowing him to do this to me...But I didn't resist at all...It was as if my body wanted it...needed it...)"
    
    show madd broken at left_small
    with dissolve
    x "(My body has a mind of its own...It wanted to be used by him...To be filled by him...Perhaps even to be bred by him...)"
    
    show madd distressed at left_small
    with dissolve
    x "(Filled by my own father...It was so intensely arousing...Is that why mom stayed with him...?To be repeatedly filled by him...To be constantly used by him...?)"
    
    show madd traumatized at left_small
    with dissolve
    x "(Some twisted, dark part of me wanted to replace her starting now...To become the one he uses...The one he fills...The one he claims completely...)"
    
    show madd shaken at left_small
    with dissolve
    x "(I need to clear my mind...If I let him do this to me repeatedly...I will lose my sanity... I will become his wife in every possible way...)"
    
    show madd broken at left_small
    with dissolve
    x "(Finally he stopped thrusting...he just remains there sitting deep inside me...His dick still completely buried within my depths...)"
    
    scene scene_dad_walks_in_madd_room_dad_after_anal_climax_filling_maddie_with_seed_i_just_came_inside_you
    with fade

    show dad lustful at right_small
    with dissolve
    dad_says "Maddie...I...I just came inside you...that was...absolutely incredible..."
    
    scene scene_dad_walks_in_madd_room_dad_after_anal_climax_filling_maddie_with_seed_i_just_came_inside_you_dont_you_love_how_i_fill_you_up
    with fade

    show dad possessive at right_small
    with dissolve
    dad_says "You feel so incredibly tight around me...I could stay like this forever...Don't you love the way I fill you up completely...?"
    
    show madd helpless at left_small
    with dissolve
    x "(Hearing him say that made me shiver intensely...He loved filling me up like this...Claiming me as his...making me his permanent property...)"
    
    scene scene_dad_walks_in_madd_room_dad_after_anal_climax_filling_maddie_with_seed_maddie_Love_it_when_you_fill_me_up
    with fade

    show madd resigned at left_small
    with dissolve
    x "I..I loved it when you filled me up completely...It made me feel...special...claimed...owned..."
    
    show dad dominant at right_small
    with dissolve
    dad_says "Special? of course you are my wife..are you not?"
    
    show madd violated at left_small
    with dissolve
    x "(Hearing him say that made my heart race wildly...My mind spinning in confusion...Was I really becoming his wife now...?)"
    
    show madd broken at left_small
    with dissolve
    x "(Before I could think any further he slowly began withdrawing from me...His dick sliding gradually out of my ass...leaving me feeling completely empty and thoroughly used...)" 
    
    show madd distressed at left_small
    with dissolve
    x "(So much cum leaked immediately as soon as he pulled out...Dripping down my thighs...I could feel it continuously dripping from my asshole...)" 
    
    show madd traumatized at left_small
    with dissolve
    x "(I was now a cum-filled mess...My ass overflowing with his seed...My thighs completely covered in it...I felt so thoroughly dirty...So completely used...So utterly owned...I was dripping with sweat from the intense experience of being filled by him...)"
    
    show madd helpless at left_small
    with dissolve
    x "(He placed me on the bed again, positioning me in front of him)"
    
    show madd violated at left_small
    with dissolve
    x "(I looked up at him...My eyes full of desperate desire...Wanting more...Needing more...Craving to be used by him...To be filled by him again and again...To be permanently owned by him...)"
    

    scene scene_dad_walks_in_madd_room_dad_my_seed_inside_you_maddie_own_mine
    with fade
    
    show dad possessive at right_small
    with dissolve
    dad_says "Maddie...my seed is now inside you...You are mine ....All mine."
    
    show dad dominant at right_small
    with dissolve
    dad_says "Remember that permanently...You are my property now...You belong to me in every conceivable way..."
    
    show madd helpless at left_small
    with dissolve
    x "(Hearing him claim ownership of me like that made me shiver deeply...My body aching desperately for more of him...Craving more of his complete domination...Needing more of his possessive filling...)"
    
    show madd resigned at left_small
    with dissolve
    x "(I nodded my head slowly and deliberately... my head lowered completely in utter submission...Accepting my new role as his wife...His permanent property...His cum-filled wife...)"
    
    scene scene_dad_walks_in_madd_room_dad_kisses_maddie_goodnight
    with fade
    
    show dad lustful at right_small
    with dissolve
    x "(He leans in even closer to me...Kissing me intensely and possessively...His hands roaming across my entire body...Claiming every part of me as his exclusive property...)"
    
    show madd violated at left_small
    with dissolve
    x "(In that kiss I felt him deliberately spitting into my mouth...One final degrading way of marking me as his...Filling me with his fluids in every possible way...)"
    
    show dad possessive at right_small
    with dissolve
    dad_says "Goodnight maddie...sleep with my seed inside you...remember who you belong to..."
    
    show madd traumatized at left_small
    with dissolve
    x "(I looked down completely unable to meet his eyes...My entire body still trembling from the intense experience of being filled and claimed by him)"
    
    show madd broken at left_small
    with dissolve
    x "(I simply responded)"
    
    show madd resigned at left_small
    with dissolve
    x "Goodnight .... Husband..."
    
    show dad sadistic at right_small
    with dissolve
    dad_thinks "Heh...She's finally starting to fully accept it...My little wife...my property...my breeding bitch..."
    
    show dad possessive at right_small
    with dissolve
    dad_says "Sleep well knowing my cum is inside you...That  cum inside you is gonna change you permanently ."
    
    x "(He says that as he walks deliberately out of my room...leaving me completely alone with his seed still inside me... as I slowly drift off into troubled sleep...)"
    
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["kissed"] += 1
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["anal_sex"] += 1
    $ character_relations["dad"]["anal_creampie"] += 1
    $ character_relations["dad"]["intimacy"]+=9
    $ dad_anal_scene_completed = True
    $ journal_event_set_done("Dad", "Room Intrusion: Anal")
    $ journal_event_show("Dad", "First Vaginal: Punishment Night")
    
    jump my_room_scene



label dad_walks_in_madd_room_sleep_vag:
    scene scene_madd_sleep_on_bed_my_room
    with fade

    "Maddie was sleeping in her bed, unaware of what was going on."

    scene scene_dad_walks_in_madd_room_sleep_dad_sitting_beside_madd_bed
    with fade
    "In the middle of the night, while Maddie was sleeping, her dad walked into her room, pulled the chair, and sat next to her."
    "He looked at her sleeping body and admired her beauty. It almost made him forget that Maddie had stolen his money and he had seen her making out with her stepbrother "
    "He was fighting between his lust and his anger"

    scene dad_walks_in_madd_room_sleep_vag_dad_changes_madd_position
    with fade
    "he had made his mind, he was gonna use his anger to justify his lust, he was gonna punish her for stealing his money and for making out with her stepbrother, and he was gonna do it in the most humiliating way possible"    
    "He gets up from the chair and sits on the bed"
    "He moves maddie's body turning her horizontally beside him , he holds her hand and looks her face one more time"
    dad_says "God your body is so beautiful, Maddie"
    "Maddie was still sleeping , not knowing what was about to happen to her"
    "He then lowers his lips on top of hers and starts kissing her gently so as to not wake her up "
    "He positions himself between her legs"

    scene dad_walks_in_madd_room_sleep_vag_dad_changes_madd_position_2
    with fade
    "He slowly lifts her legs up , now her legs were in the air and he continues kissing her while he was doing that."
    "Maddie was moaning in her sleep as her stepDad was touching her, but she was still asleep and didn't know what was going on"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up
    with fade
    "He starts kissing her more passionately and this time Maddie felt it "
    
    show madd confused at left_small
    with dissolve
    x "(I felt rough kissing on my lips , i noticed my legs were in the air. What was going on ?)"
    
    show madd shocked at left_small
    with dissolve
    x "(I slowly opened my eyes and saw stepDad's face right in front of mine, and i was so confused)"
    
    show madd horrified at left_small
    with dissolve
    x "(He was kissing me and he was placed between my legs, when did that happen ? )"
    
    show madd paralyzed at left_small
    with dissolve
    x "(When he saw me wake up , he pulled back a little )"
    x "What ...?"
    
    show madd trembling at left_small
    with dissolve
    x "What's going on ?"
    x "(I ask him in hope that he would stop and explain to me what was going on, but he didn't say anything)"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_angry
    with fade
    
    show madd confused at left_small
    with dissolve
    show dad angry at right_small
    with dissolve
    x "(I could see he was angry but i didn't understand why, I could also see the lust in his eyes that I could explain)"
    
    show madd distressed at left_small
    with dissolve
    show dad coercive at right_small
    with dissolve
    x "(Suddenly he pulled my hair and forced me to look at him, his face directly in front of mine)"
    dad_says "You stole from me Maddie ! "
    
    show dad manipulative at right_small
    with dissolve
    dad_says "I loved you and you stole from me !"
    
    show madd shocked at left_small
    with dissolve
    x "(I could sense the sadness in his voice when he said that, but i was still so confused and scared)"
    
    show madd anxious at left_small
    with dissolve
    x "(Did he find out about the money ? 2000 Dollars is a lot , he is not gonna let that go)"
    show dad possessive at right_small
    with dissolve
    dad_says "And you got intimate with your stepbrother !"
    
    show madd horrified at left_small
    with dissolve
    x "(He was much more angry and sad when he said that, i could see the disappointment in his eyes)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(I was speechless, i didn't know what to say )"
    x "I....I .."
    
    show madd helpless at left_small
    with dissolve
    x "(I was trying to find the right words to say, but i couldn't find any, i was just staring at him)"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_angry_2
    with fade
    
    show madd distressed at left_small
    with dissolve
    show dad controlling at right_small
    with dissolve
    x "(He pulls my hair again roughly, i had to say something now, i couldn't just stay silent)"
    
    show madd trembling at left_small
    with dissolve
    x "I...I'm sorry ...dad"
    
    show dad authoritative at right_small
    with dissolve
    x "(He leaned in closer to me and said in his rough voice )"
    dad_says "I am gonna report you to the cops."
    
    show madd horrified at left_small
    with dissolve
    x "(Oh god, he is gonna report me to the cops)"
    
    show madd weeping at left_small
    with dissolve
    x "(My dream of becoming an engineer is gonna be ruined, i am gonna go to jail, i am gonna lose everything)"
    
    show madd helpless at left_small
    with dissolve
    x "I...I will make it right for you.."
    x "PLease..."

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_angry_3
    with fade
    
    show dad calculating at right_small
    with dissolve
    dad_says "How can you make it right for me ?"
    
    show dad predatory at right_small
    with dissolve
    x "(He leaned in a little bit closer to me and said in a very rough voice )"
    
    show dad lustful at right_small
    with dissolve
    dad_says "what can you give me that i dont have ?"
    show madd shocked at left_small
    with dissolve
    x "(i looked away from him, i knew what he wanted. He wanted to use the last hole of my body that he hasn't used yet.)"
    
    show madd horrified at left_small
    with dissolve
    x "(He wanted to be my first )"
    
    show madd trembling at left_small
    with dissolve
    x "I...I'm sorry"
    
    show madd anxious at left_small
    with dissolve
    x "(oh no , this situation is getting worse and worse ...How can i get out of this ? )"
    show madd resigned at left_small
    with dissolve
    x "(There is no other way... I have to give him what he wants, i have no choice...)"
    
    show madd broken at left_small
    with dissolve
    x "You can have me then...."
    
    show madd helpless at left_small
    with dissolve
    x "Please dont report me to the cops, i will do anything you want, just please dont report me to the cops"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_negotiation
    with fade
    
    show madd distressed at left_small
    with dissolve
    show dad calculating at right_small
    with dissolve
    x "(He leaned in closer for a gentle kiss only for a second, then he pulled back and said )"
    
    show dad dominant at right_small
    with dissolve
    dad_says "I want the front hole Maddie"
    dad_says "Its that or nothing."
    
    show dad possessive at right_small
    with dissolve
    dad_says "Only way to make sure you are mine is to have my seed inside you, to make sure you are pregnant with my child"
    show madd shocked at left_small
    with dissolve
    x "(I was so shocked when he said that, i couldn't believe what i just heard)"
    
    show madd horrified at left_small
    with dissolve
    x "(I was stuck between a rock and a hard place, either i give him what he wants or he reports me to the cops)"
    
    show madd trembling at left_small
    with dissolve
    x "You..."
    
    show madd resigned at left_small
    with dissolve
    x "You can have it then..."
    
    show madd broken at left_small
    with dissolve
    x "(That was it,  i had given him the green light to do whatever he wanted to my body,)"
    x "( i had given him the permission to use me as he pleases, and that was it, there was no going back from that point on)"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_kiss_1
    with fade
    
    show dad lustful at right_small
    with dissolve
    x "(I saw smile on his face when i said that, he was so happy that i gave him the permission to do whatever )"
    
    show madd helpless at left_small
    with dissolve
    x "(It was as if i just accepted his proposal to be his wife, i just accepted to be his property )"
    
    show madd resigned at left_small
    with dissolve
    x "(I felt his hand on the back of my head as he lift my head slightly bringing my face closer to his)"
    
    show dad possessive at right_small
    with dissolve
    dad_says "That's what i wanted to hear my dear ,Maddie"
    
    show madd distressed at left_small
    with dissolve
    x "(As soon as he said that, he kissed me passionately )"
    x "(The hand on the back of my head was pulling me closer to him)"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_kiss_2
    with fade
    
    show madd paralyzed at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(He starts slowly kissing me , using his tongue to explore my lips)"
    
    show madd distressed at left_small
    with dissolve
    x "(He would gently process my lips with his tongue and it would go in my mouth a little bit, but it was still a gentle kiss)"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_kiss_3
    with fade
    
    show madd trembling at left_small
    with dissolve
    show dad dominant at right_small
    with dissolve
    x "(Now his tongue was going deeper into my mouth)"
    
    show madd helpless at left_small
    with dissolve
    x "(He would pull it back a little bit and then push it back in again, it was like he was trying to make me get used to the feeling of his tongue in my mouth, it was like he was trying to make me accept him more and more)"
    
    show madd resigned at left_small
    with dissolve
    x "(I knew this is what he will be doing to me later but with his dick instead of his tongue, i was trying to prepare myself for that, i was trying to get used to the feeling of him being inside me,)"
    x " ( even if it was just his tongue in my mouth, it was still a step forward in accepting him and accepting what he is gonna do to me later on )"
    
    show madd flustered at left_small
    with dissolve
    x "(His cold gold chain touching my neck , the contrast between the temperature of the chain and the warmth of his tongue was making me feel so many things at the same time)"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_kiss_4
    with fade
    
    show madd distressed at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(The rhythmic movement of his tongue in my mouth continued for a while ,)"
    
    show madd disgusted at left_small
    with dissolve
    x "(I knew he was enjoying it as much as i was hating it )"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_kiss_5
    with fade
    
    show madd shocked at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(Suddenly he got rougher with the kiss, i guess he has had enough of the gentle kissing and he wanted to get to the next step)"
    
    show madd paralyzed at left_small
    with dissolve
    show dad dominant at right_small
    with dissolve
    x "(His hand reached around to my neck and he starts to move his tongue more aggressively in my mouth )"
    show madd helpless at left_small
    with dissolve
    x "(one of his hand was in my shoulder and other hand on my neck while my legs were suspended in the air with him in between them, i was completely at his mercy)"
    
    show madd resigned at left_small
    with dissolve
    x "(This was such an intimate position to be in with him, it was like i was giving him all of myself, my body, my soul, my everything, i was completely his at that moment)"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_kiss_6
    with fade
    
    show madd distressed at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "(He slows down a bit, then he gently lifts my head up like a husband would do during wedding night)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(And he again kissed me , i wasnt resisting him nor accepting him. I just let him do whatever he wanted to me)"
    x "(After a while he put my head down again )"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_kiss_7
    with fade
    
    show madd trembling at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(He lifted my head up again...this time using my hair . While the last one was more gentle, this one was rougher,)"
    
    show madd distressed at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(And so was the kiss ...)"
    
    show madd disgusted at left_small
    with dissolve
    x "(I could taste him in my mouth now ...so many times his tongue went deep into my mouth that the taste lingered . Bitter and slightly salty, like old coffee and cigarettes.)"
    
    show madd resigned at left_small
    with dissolve
    x "(Now i was fully used to the feeling of his tongue in my mouth, my body was starting to accept him more and more, i was starting to accept what he is gonna do to me later on. )"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lick_face_1
    with fade
    
    show madd distressed at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(he set my head down again, then he started to lick my face, starting from my lips down to my chin)"
    
    show madd disgusted at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "(he was licking it slowly and gently, it was like he was trying to mark me as his own, it was like he was trying to claim me with his saliva)"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lick_face_2
    with fade
    
    show madd paralyzed at left_small
    with dissolve
    show dad dominant at right_small
    with dissolve
    x "(He was gently biting my chin while he was licking it)"
    
    show madd helpless at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(Dad was consuming me with his love and lust, he was trying to make me his in every possible way )"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lick_face_3
    with fade
    
    show madd disgusted at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(He got rougher with his licks , now licking my lips-chin-cheeks area . Covering me whole in his saliva )"
    
    show madd flustered at left_small
    with dissolve
    x "(I should be disgusted by it but it was actually making me feel a bit aroused.)"
    
    show madd conflicted at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "(So much saliva on my face , all i could smell was that. Warm and slightly sour, mixing with the musk of his skin. It was like i was being baptized with his saliva)"
    
    show madd resigned at left_small
    with dissolve
    x "(Except instead of becoming pure, i was becoming more and more dirty in his fluids , in his scent)"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lick_neck_1
    with fade
    
    show madd trembling at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(He become more and more rough , his hands moved to my arm holding me in place as he started licking my neck)"
    
    show madd flustered at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(My legs were shaking in the air, his crotch was rubbing against my pussy, i was getting more and more aroused )"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(I could feel his hot breath on my neck, the lust he had for me was so intense that it was almost suffocating but i could feel it in the heat his breath was producing on my skin )"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lick_neck_2
    with fade
    
    show madd distressed at left_small
    with dissolve
    show dad sadistic at right_small
    with dissolve
    x "(His mouth was leaking soooo much saliva on my neck, it was like a river of saliva flowing down my skin)"
    
    show madd helpless at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "(And my skin was absorbing it like a sponge, i could feel the wetness of his saliva on my skin, it was like i was being drenched in his love and lust )"
    
    show madd flustered at left_small
    with dissolve
    x "(I couldn't help but moan from his touch , from his smell, from his dominance over me)"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lick_neck_3
    with fade
    
    show madd trembling at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(His licks got rougher , he would lick my neck then my lips and back to my neck)"
    
    show madd flustered at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(And as he got rougher with his licks my moans got louder)"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lick_neck_4
    with fade
    
    show madd distressed at left_small
    with dissolve
    show dad sadistic at right_small
    with dissolve
    x "(He was now biting my neck while licking it )"
    
    show madd trembling at left_small
    with dissolve
    show dad dominant at right_small
    with dissolve
    x "(He would take a small part of my neck skin in his mouth and bite it while licking it )"
    
    show madd overwhelmed at left_small
    with dissolve    
    x "(At this point so much saliva had dropped on my neck and face , all i could smell was his saliva . That sour, warm smell, mixed with his male musk, it was all over me)"
    
    show madd conflicted at left_small
    with dissolve
    x "(Only thing that could've overwritten the smell of his saliva was the smell of his cum, and i knew that was coming soon )"
    show madd resigned at left_small
    with dissolve
    x "(But today he was not gonna waste his cum on my face, he was gonna put it inside me, he was gonna make sure i get pregnant with his child, he was gonna make sure that i am his forever )"
    
    show madd helpless at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "(He finally pulled away from my neck and looked at me, his face was full of lust and love, he was so happy that i accepted him, that i accepted to be his )"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lifting_shirt_1
    with fade
    
    show madd distressed at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(He let go of my legs ,finally they have been in the air for so long, they were starting to hurt and his hands move to the hem of my shirt, he lifted it up exposing my stomach and black lace bra i was wearing)"
    
    show madd helpless at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(He was gonna devour my whole body today... as he went for another kiss on my lips)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "Lift your arms up for me Maddie"
    
    show dad possessive at right_small
    with dissolve
    dad_says "And pull my head to your armpits....like a lover would.."
    
    show madd shocked at left_small
    with dissolve
    x "(What ?? Why ? I was so confused by his request, but i had to do it, i had no choice but to obey him)"


    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lifting_shirt_armpit_1
    with fade
    
    show madd trembling at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(He pulled his head away frop me and i knew this was what he wanted , he wanted me to pull his head to my armpits, he wanted to smell me there, )"
    
    show madd resigned at left_small
    with dissolve
    show dad obsessed at right_small
    with dissolve
    x "(And i pulled his head to my armpits, i was so embarrassed by this but i had to do it)"
    
    show madd disgusted at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(As soon as i pulled his head to my armpits, he started to smell them, he was inhaling deeply)"
    
    show madd helpless at left_small
    with dissolve
    x "(It was very humiliating for me, I could feel his hot breath on my armpit)"
    
    show madd distressed at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(And then he started licking my armpit, he was licking it slowly and gently, )"



    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lifting_shirt_armpit_2
    with fade
    
    show madd nauseated at left_small
    with dissolve
    show dad obsessed at right_small
    with dissolve
    x "(He was licking my underarms while also taking deep breaths from it)"
    
    show madd flustered at left_small
    with dissolve
    show dad horny at right_small
    with dissolve
    x "(I dont know why but i could tell it was making him super hard just by the way he was breathing and the way his tongue was moving on my skin)"
    
    show madd disgusted at left_small
    with dissolve
    x "(on the other hand it was embarassing for me ,someone was licking my armpits, it was like i was being treated like a dog)"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lifting_shirt_armpit_3
    with fade
    
    show madd helpless at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(Slowly and slowly he was licking my armpits clean.)"
    
    show madd conflicted at left_small
    with dissolve
    show dad obsessed at right_small
    with dissolve
    x "(I knew he loved the taste and the smell of my armpits. That slightly salty, musky scent of my sweat, like he was getting drunk on it.)"
    
    show madd curious at left_small
    with dissolve
    x "(Did he do that with mom too ? Did he lick her armpits ? I was so curious about that but i was also so scared to ask him about it )"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lifting_shirt_armpit_4
    with fade
    
    show madd distressed at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(Now he was gently biting my armpits while licking them )"
    
    show madd flustered at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(his tongue would wander to the armpit to parts under my boobs and back to the armpits again)"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lifting_shirt_armpit_5
    with fade
    
    show madd hesitant at left_small
    with dissolve
    show dad obsessed at right_small
    with dissolve
    x "(He takes another lick and another big sniff from my armpits and says )"
    
    show dad lustful at right_small
    with dissolve
    dad_says "You  taste so good Maddie, you smell so good. i love everything about you)"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lifting_shirt_armpit_6
    with fade
    
    show madd shocked at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(After saying that he started getting so rough)"
    
    show madd trembling at left_small
    with dissolve
    show dad sadistic at right_small
    with dissolve
    x "(HIs tongue would move with such force on my armpits and underboobs that it would make them jiggle.)"
    
    show madd helpless at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(The lust had taken over him completely, he was not in control of himself anymore, he was just doing whatever his lust was telling him to do )"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lifting_shirt_armpit_7
    with fade
    
    show madd distressed at left_small
    with dissolve
    show dad cruel at right_small
    with dissolve
    x "(Then he almost bit parts of my boob while licking it, he was so rough that it was almost painful but i could feel the pleasure from it at the same time )"
    
    show madd flustered at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(and went back to licking my armpits again )"
    
    show madd conflicted at left_small
    with dissolve
    x "(i was humiliated but i felt glad that my smell and taste was making him so happy )"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lifting_shirt_armpit_8
    with fade
    
    show madd overwhelmed at left_small
    with dissolve
    show dad obsessed at right_small
    with dissolve
    x "(At this point even he was making grunting noises while licking my armpits, he was so into it, he was so in love with me that he was making all these noises while licking my armpits )"
    
    show madd confused at left_small
    with dissolve
    x "(Does he love me that much ?)"
    
    show madd anxious at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "(If that was true he will never let me leave him )"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lifting_shirt_armpit_9
    with fade
    
    show madd paralyzed at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "(He finally slows down a bit and looks at me and says )"
    
    show dad dominant at right_small
    with dissolve
    dad_says "Tonight you're gonna be mine Maddie, you're gonna be my wife "
    
    show madd trembling at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(He takes another lick from my armpits and continues )"
    
    show dad obsessed at right_small
    with dissolve
    dad_says "All of your body will be mine Maddie, and i am gonna make sure you are pregnant with my child, and then you're gonna be mine forever"
    
    show madd horrified at left_small
    with dissolve
    x "(It send shivers down my spine when he said that, it was like a promise and a threat at the same time, it was like he was saying that i am his forever and there is no way out of this relationship )"
    show madd flustered at left_small
    with dissolve
    x "(But part of me was so aroused by the thought of being his forever, being his wife, being pregnant with his child, it was like a twisted fantasy  )"
    
    show madd conflicted at left_small
    with dissolve
    x "(Submitting to him, sleeping with him everynight, waking up with his cum inside me every morning, being pregnant with his child, being his forever)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(At this point i was too aroused to tell if this was a dream or a nightmare scenario, i was so confused by my feelings, my body was betraying me...)"


    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lifting_shirt_armpit_10
    with fade
    
    show madd resigned at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(He licks me one last time, passionately licking my armpits like a dog cleaning its owner except i was not his owner, i was his property, i was his wife )"
    
    show madd helpless at left_small
    with dissolve
    show dad dominant at right_small
    with dissolve
    x "(And after he had enough he finally pulled back and looked me straight in the eye. )"
    
    show dad possessive at right_small
    with dissolve
    dad_says "Now get ready for me Maddie, time for you to be my wife."

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_on_top_removing_bra
    with fade
    
    show madd resigned at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(He then got on top of me , kissed me again and starts to unhook my bra)"
    
    show madd helpless at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(It came off very easily, and i wasnt offering any resistance)"
    
    show madd flustered at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "(He admired my boobs for a second, then continued kissing me while   tugging at my shorts)"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_on_top_removing_shorts
    with fade
    
    show madd trembling at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(Finally he starts pulling my shorts away , my legs were in the air so he was able to slide them off very easily)"
    
    show madd violated at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(I was in my bed naked now, with him on top of me between my legs, kissing me and touching me everywhere)"
    
    show madd flustered at left_small
    with dissolve
    x "(I was so aroused about the situatoin i was in)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I knew i was not on my ovulation day but i was still so aroused by the thought of being his wife, being pregnant with his child )"
    
    show dad dominant at right_small
    with dissolve
    dad_says "Time to unleash the beast Maddie, tonight we consumate our marriage."
    show dad manipulative at right_small
    with dissolve
    dad_says "So you will never steal from me again, and even if you do ...You are my wife and i will always forgive you"
    
    show dad possessive at right_small
    with dissolve
    dad_says "Your brother will know that his sibling is growing inside you and he will leave you alone"
    
    show madd flustered at left_small
    with dissolve
    x "(I was speechless when he said that, what the fuck thinking about that was so hot....)"



    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_on_top_removing_dad_shorts
    with dissolve
    
    show madd trembling at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve 
    x "(Finally his hand moved to his shorts, as he lowers them down along with his boxers, revealing his hard dick.)"
    
    show madd horrified at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(I couldn't see it but i could feel its heat and hardness against my skin.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(It was really close to my pussy and i could feel the warmth of it on my buttcheeks for now...)"
    
    show madd anxious at left_small
    with dissolve
    show dad dominant at right_small
    with dissolve
    x "(He looks me in the eyes one last time before he enters me and says....)"
    
    show dad possessive at right_small
    with dissolve
    dad_says "With this our relationship is official, you are mine now Maddie."

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_on_top_first_vag_penetration
    with dissolve
    
    show madd flustered at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(I was already so wet from the kisses and licking i knew his dick was slide right in.)"
    
    show madd shocked at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(And Finally it did , he put his dick right in my pussy and i could feel it filling me up.)"
    
    show madd violated at left_small
    with dissolve
    show dad dominant at right_small
    with dissolve
    x "(My hymen broke and i felt a little pain but it was quickly replaced by pleasure as he started to move in and out of me.)"

    $ stat_notification = "Lost virginity to Stepdad ❤️"
    $ renpy.pause(3.0)
    $ stat_notification = ""

    show madd resigned at left_small
    with dissolve
    x "(This was it, this is where i become his...All human rights,all of my identity , its all gone now, i am his property and he is my owner.)"
    
    show madd overwhelmed at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(I was so overwhelmed with pleasure that i couldn't even speak, all i could do was moan and cry out in pleasure as he fucked me.)"
    show madd flustered at left_small
    with dissolve
    show dad horny at right_small
    with dissolve
    x "(I could feel his happiness and satisfaction as he penetrated my vagina, the way he was grunting and moaning, it was like he was in heaven.)"
    
    show dad lustful at right_small
    with dissolve
    dad_says "GOD DAMN YOU'RE SO FUCKING TIGHT, I CAN'T BELIEVE THIS IS MY STEP DAUGHTER FUCKING ME, THIS IS THE BEST DAY OF MY LIFE!"
    
    show madd inheat at left_small
    with dissolve
    show dad dominant at right_small
    with dissolve
    x "(I could feel his dick hitting my cervix with every thrust, it was so deep and it felt so good.)"
    show madd helpless at left_small
    with dissolve
    x "(I was under him ,my legs in the air, and he was pounding me so hard, i could feel every inch of him inside me.)"
    
    show madd flustered at left_small
    with dissolve
    x "(This was such a submissive position to be in, with my step dad on top of me pounding me like that it was soo humiliating but also so arousing at the same time.)"
    
    show madd overwhelmed at left_small
    with dissolve
    show dad sadistic at right_small
    with dissolve
    x "(The sound in the room was filled with the sound of our moans ,the bed creaking, and the sound of his crotch hitting my buttcheeks as he fucked me.)"
    show madd shocked at left_small
    with dissolve
    x "(So this...this is sex...this is what it feels like to be fucked by a man)"
    
    show madd inheat at left_small
    with dissolve
    x "(This feels so good.....I never want this to end.....)"
    
    show madd confused at left_small
    with dissolve
    x "(Is it because he's my step dad? Is it because its my first time? I don't know but it feels so much better than i ever imagined it would.)"
    show madd flustered at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(I could feel his dick throbbing inside me as he fucked me, it was like it was alive and it was pulsing with pleasure.)"
    
    show madd curious at left_small
    with dissolve
    x "(Is this what mom felt when she was alive, when she was with dad? Did she feel this good when he fucked her?)"
    
    show madd conflicted at left_small
    with dissolve
    x "(How the hell did she get depressed when she had pleasureable experiences like this with dad? I don't understand it at all.)"
    show dad horny at right_small
    with dissolve
    dad_says "This feels so good, I can't believe how tight you are, Maddie. You're such a good fucking  daugh-....Wife, I can't wait to do this again and again with you."
    
    show dad possessive at right_small
    with dissolve
    dad_says "I want to sleep with my dick inside you every night. You will keep it in your pussy keeping it warn as i fill you up with my cum throughout the night)"
    
    show dad lustful at right_small
    with dissolve
    dad_says " You will be my little cum dump and i will be your loving husband who fills you up with his seed."
    show madd flustered at left_small
    with dissolve
    x "(When he said that suddenly the thought of him sleeping with his dick inside me didnt seem so bad, )"
    
    show madd inheat at left_small
    with dissolve
    x "(In fact it sounded really good, i wanted to feel his dick inside me all the time, i wanted to be his little cum dump and have him fill me up with his cum every night.)"
    
    show madd shocked at left_small
    with dissolve
    x "(God what is happening to my brain? I can't believe I'm thinking like this, I can't believe I'm so turned on by the idea of being my step dad's cum dump.)"
    show madd horrified at left_small
    with dissolve
    x "(Losing my virginity to him might have been very dangerous....I cant believe i let this happen...I dont think i can ever refuse him now.)"
    
    show madd anxious at left_small
    with dissolve
    x "(At least now i am not ovulating but once I am ovulating again, I will be even more fertile and even more at risk of getting pregnant from him)"
    
    show madd worried at left_small
    with dissolve
    x "(And if he starts fucking me every night like he said, then the chances of me getting pregnant are super high, I could get pregnant from him in just a few weeks)"
    show madd conflicted at left_small
    with dissolve
    x "(I don't want to get pregnant from him, I don't want to have his baby, but at the same time I can't stop thinking about how good it feels to have his dick inside me, I can't stop thinking about how good it feels to be his little cum dump.)"
    
    show madd broken at left_small
    with dissolve
    x "(Morally I know this is wrong, I know this is illegal, but I can't help how good i feel being absolutely pounded by him while he is on top of me)"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_on_top_first_vag_penetration_2
    with dissolve
    
    show madd overwhelmed at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(He starts going faster , i could feel his dick increasing in size inside me ...my body could feel all of his dick)"
    
    show madd disgusted at left_small
    with dissolve
    show dad sadistic at right_small
    with dissolve
    x "(At this point his mouth was leaking saliva right onto my face and i LOVED IT )"
    
    show madd flustered at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(I knew my body was covering every inch of his dick and that was making me feel good too !)"
    show madd inheat at left_small
    with dissolve
    x "(I could feel the hotness spreading through me as he fucked me, it was like there was another organism inside me that was alive and it was pulsing with pleasure.)"
    
    show madd overwhelmed at left_small
    with dissolve
    show dad dominant at right_small
    with dissolve
    x "(He positioned his hand on my buttcheeks and pulled me closer to him as he fucked me, his body was pushing down on me and his hands were pulling me closer to him...)"
    
    show madd violated at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "(This combo made his dick go all they way deeper inside me )"
    show dad horny at right_small
    with dissolve
    dad_says "Fucking hell ,this feels amazing maddie,"
    
    show dad lustful at right_small
    with dissolve
    dad_says "You are even better than your mother was... I can't believe how good you feel inside me, it's like you were made for me."
    
    show dad obsessed at right_small
    with dissolve
    dad_says "If we keep doing this every night , i will forget all about your mother and only think about you, you will be the only woman in my life  and i will love you till the end of time."
    
    show madd flustered at left_small
    with dissolve
    x "(Oh god, hearing him say that made me feel so special and so loved ... i should feel guilty for feeling that way but i can't help it)"
    
    show madd conflicted at left_small
    with dissolve
    x "( I want to keep mothers memory alive but replacing her sounds so tempting right now and hearing him say that made me feel like i could be the one to do that for him)"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_on_top_first_vag_penetration_3
    with dissolve

    show madd inheat at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(i grew so wet hearing that ... the sound of the room changed...it was now filled with wet squishing sounds as his dick slid in and out of me)"
    
    show madd overwhelmed at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "( I knew i had just climaxed after hearing him say that and he knew it too because he started going even faster and harder inside me)"
    show madd resigned at left_small
    with dissolve
    show dad dominant at right_small
    with dissolve
    x "(He knew i had cum... that was the consent he needed to know that i was enjoying it and he grew faster and harder inside me after that)"
    
    show madd violated at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "(At this point i was moaning so loud that i was sure that step brother could hear me from his room and i didn't care at all)"
    
    show madd conflicted at left_small
    with dissolve
    x "(Perhaps dad liked that i was being so loud, it only supports his dominance and claim over me  compared to my step brother )"
    show madd overwhelmed at left_small
    with dissolve
    show dad sadistic at right_small
    with dissolve
    x "(I was in my room , laying on my bed with my dad pounding the lights off of me , cumming with his cock deep inside me .)"
    
    show madd inheat at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(Rooms sound was filled with the sound of our moans, the bed creaking, sound of his crotch hitting my buttcheeks as he fucked me, and wet squishing sounds as his cock slid in and out of me)"
    
    show madd broken at left_small
    with dissolve
    x "(All of this combined with the smell of the room was overwhelming my senses . The heavy musk of sex, sweat mixing with his masculine scent, I cant think straight at all!!)"
    show madd flustered at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(suddenly his cock started throbbing inside me and i could feel it pulsing with pleasure, i knew he was close to cumming and i wanted to take his cum inside me)"
    
    show dad horny at right_small
    with dissolve
    dad_says "Maddie ,I am going to cum inside you, I want to fill you up with my cum, make you pregnant with my baby"
    
    show madd inheat at left_small
    with dissolve
    x "(Hearing him say that i instinctively responded with a moan of pleasure)"
    show madd salivating at left_small
    with dissolve
    x "Yes...dad...fill me up with your cum...make me pregnant with your baby..."
    
    show madd inheat at left_small
    with dissolve
    x "I want to be your little cum dump...I want to be your little baby maker..."
    
    show madd overwhelmed at left_small
    with dissolve
    x "(i dont know why i said that but it just came out of my mouth, my brain was rewiring itself to accept this new reality of being my step dad's wife)"
    
    show dad lustful at right_small
    with dissolve
    x "(After hearing that he just smiled and increased his pace even more)"


    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_on_top_first_vag_penetration_climax
    with dissolve
    
    show dad dominant at right_small
    with dissolve
    dad_says "That's it Maddie , take all of my cum inside you, get fucking pregnant with my baby "
    
    show madd shocked at left_small
    with dissolve
    show dad horny at right_small
    with dissolve
    x "(He says  that and i felt hot thick liquid shooting inside of my pussy, it was his cum )"
    
    show madd overwhelmed at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(I havent had anything inside my pussy before but this felt so good, it was like a new sensation that i had never felt before and it was amazing)"
    show madd inheat at left_small
    with dissolve
    x "(The heat from his cum spread throughout my body like wildfire)"
    
    show madd violated at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "(I could feel his cum filling me up i dont know how to put it but it was such a fullfilling sensation .)"
    
    show madd shocked at left_small
    with dissolve
    x "(I have been missing out on so much !!!!"
    show madd salivating at left_small
    with dissolve
    show dad sadistic at right_small
    with dissolve
    x "(As he was cumminng inside me , spit from his mouth was coming down on my face and i was loving it)"
    
    show madd inheat at left_small
    with dissolve
    x "(I have tasted and taken every fluid from hinm now, his saliva, his cum, i have taken it all and i love it)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I wish he would pee in my mouth next , i want to taste his piss too...)"
    show madd shocked at left_small
    with dissolve
    x "(I dont know why i was having such a strong desire to taste his piss but i just wanted to do it so bad )"
    
    show madd horrified at left_small
    with dissolve
    x "(CMON MADD , snap out of it...if you ask him to pee in your mouth he might get the idea that you want to be his piss slave and that is a whole new level of submission that you might not be ready for yet...)"
    
    show madd overwhelmed at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(He kept cumming inside me for a while and i felt a lot of it was leaking out of my pussy and onto the bed sheets but i didnt care at all)"
    show madd inheat at left_small
    with dissolve
    x "(Heck once he was done cumming inside me i will just lay there with his cum leaking out of me and lick the bed sheets to get every last drop of his cum that i can get)"
    
    show madd horrified at left_small
    with dissolve
    x "(WHAT AM I THINKING RIGHT NOW? I CANT BELIEVE I AM THINKING ABOUT LICKING THE BED SHEETS TO GET HIS CUM OFF OF THEM...WHAT THE HELL IS WRONG WITH ME?)"
    
    show madd resigned at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "(Finally he stopped cumming inside me and he collapsed on top of me, his cock still inside me and he kissed my lips again)"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_on_top_first_vag_penetration_climax_aftermath
    with dissolve

    show madd inheat at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "Daddy...that felt so good... thank you for filling me up with your cum...I love you so much..."
    
    show madd conflicted at left_small
    with dissolve
    x "(I said that and i meant it, i really did love him so much and i was so grateful for the pleasure he had given me...at least in the moment)"
    
    show dad possessive at right_small
    with dissolve
    dad_says "Heh, all it took was one night of fucking you and now you're already in love with me, that's so cute Maddie."
    show dad manipulative at right_small
    with dissolve
    dad_says "I will give you lots of pleasure every night if you marry me , not just in bed but in every aspect of our lives, "
    
    show dad obsessed at right_small
    with dissolve
    dad_says "We can raise a family together, we can have kids together lots of kids ...especially with your beautiful fertile pussy that i just filled up with my cum"
    
    show madd flustered at left_small
    with dissolve
    x "I...I want that too daddy, I want to have lots of kids with you, I want to be your wife and have your babies..."
    
    show dad possessive at right_small
    with dissolve
    dad_says "Heh, I knew you would say that, you're such a good little cum dump, I can't wait to have you as my wife and fill you up with my cum every night."
    show madd violated at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(With that he kissed me for 10 more minutes straight while i was laying in the pool of his cum and a lots of it still inside me )"
    
    show madd resigned at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "(Finally after few minutes i felt his cock start to soften inside me and he pulled out of me)"
    
    show madd helpless at left_small
    with dissolve
    x "(He finally pulled out of me and i could feel the emptiness inside me after he left, it was like a part of me was missing and i wanted to feel him inside me again right away)"
    show dad obsessed at right_small
    with dissolve
    dad_says "You know Maddie, we should get married soon... I want to make our relationship official and I want to make you my wife."
    
    show madd overwhelmed at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(his head goes down and he puts my nipples in his mouth and starts sucking on them then pulls out and says)"
    
    show dad lustful at right_small
    with dissolve
    dad_says "I want them to be lactating as soon as possible..."
    show madd flustered at left_small
    with dissolve
    x "(I was still breathing heavily from the intense sex we just had but hearing him say that made me feel so horny again and i was already getting wet again just from the thought of him sucking on my nipples)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I knew his greedy butt just wanted to drink my breast milk but i said )"
    
    show madd resigned at left_small
    with dissolve
    x "If thats what you want husband..."
    
    show dad possessive at right_small
    with dissolve
    dad_says "That's my good wife... I will make sure to fill you up with my cum every night so that you can have lots of milk for me to drink..."
    show madd broken at left_small
    with dissolve
    x "(with that he got up and left the room, leaving me laying there in a pool of his cum although i wanted to lick it off the bed sheets i was too tired to do anything but lay there )"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(I feel alseep thinking about how good it felt to have his cum inside me and how much i wanted to have more of it inside me again soon)"

    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["kissed"] += 1
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["vaginal_sex"] += 1
    $ character_relations["dad"]["vaginal_creampie"] += 1
    $ character_relations["dad"]["intimacy"] +=11
    $ character_relations["dad"]["lust"] = 0
    $ character_relations["dad"]["anger"] = 0 
    $ dad_walks_in_madd_room_sleep_vag_flag = True
    $ journal_event_set_done("Dad", "First Vaginal: Punishment Night")
    $ journal_event_show("Dad", "Nightly Visits: Foot and Breeding")
    jump my_room_scene


label dad_walks_in_madd_room_sleep_vag_2:
    scene scene_madd_sleep_on_bed_my_room
    with fade

    "After the first time, Maddie's dad walked into her room regularly while she was sleeping, and each time he did as he pleased "

    scene dad_walks_in_madd_room_sleep_vag_dad_changes_madd_position
    with fade
    "He would play around with her body, changing her position, touching her"
    "Until Maddie woke up but at this point, she was unable to do stop him, she was too scared to say anything and just let him do whatever he wanted to her"

    scene dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_lick_face_3
    with fade
    show madd horrified at left_small
    with dissolve
    show dad predatory at right_small
    with dissolve
    x "(He would lick me , kiss me, touch me everywhere, it almost became a routine for him to do that to me now.)"

    scene dad_madd_room_sleep_vag_dad_foot_on_madd_face
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd paralyzed at left_small
    with dissolve
    show dad creepy at right_small
    with dissolve
    x "(But tonight was different .He would pull back for a second, I hoped he was gonna finish with just kissing and licking me)"
    x "(But then a creepy smile would appear on his face, and he would make my back arch as he puts his foot directly on my face)"
    x "(The base of his foot used to open my my mouth while the rest of his foot stamp itself on my face )"
    show madd disgusted at left_small
    with dissolve
    x "(His foot is right on my face... it smells something awful. That thick, cheesy foot stink from not washing for days. It's burning my nose and I can barely breathe.)"
    x "(The bottom of his foot is so rough and sweaty. Calloused skin scraping against my lips. I can taste the dirt and old sweat... it's disgusting.)"
    x "(I knew it was wrong for me to allow him to do this to me, my own dad.)"
    show madd resigned at left_small
    with dissolve
    x "(But i have already surrendered to him, I can't do anything about it)"

    scene dad_madd_room_sleep_vag_dad_foot_inside_madd_mouth
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd violated at left_small
    with dissolve
    show dad authoritative at right_small
    with dissolve
    x "(He would run his foot over my face before saying)"
    dad_says "Open up Maddie, A good daughter cleans her father's feet"
    x "(I would slightly open my mouth not enough to let anything enter , hoping he would get the hint and stop there, but his foot would press inside my mouth, pushing my tongue down and making me gag on his foot)"
    x "(He would be so rough with pushing his foot inside my mouth as if he had some chewing gum stuck to the bottom of his foot and he wanted to use my mouth to clean it off)"
    show madd disgusted at left_small
    with dissolve
    x "(The taste is  vile. Salty, bitter, and sour all at once — like licking sweaty old skin mixed with dirt . )"
    x "(This is my dad's foot. My own stepdad's dirty, unwashed foot is shoved inside my mouth. I'm actually letting him use my mouth like a foot rag.)"
    
    scene dad_madd_room_sleep_vag_dad_foot_inside_madd_mouth_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd conflicted at left_small
    with dissolve
    show dad mocking at right_small
    with dissolve
    x "(He would tease me by pulling his foot out of my mouth just a little bit, only his big toe still in contact with my tongue, and then push the area below his toes against my tongue)"
    x "(My body was now autonomously reacting to his foot, as i would start making out being in deep kiss with the area below his toes )"
    show madd flustered at left_small
    with dissolve
    x "(He never asked me to use tongue in that deep kiss, but i would do it anyway, as if my body was betraying me and doing things on its own)"
    dad_says "That's my good girl, see how much you like it when daddy's foot is in your mouth? "
    dad_says "And to think you hated even my hands on you at first, now look at you."
    show madd self loathing at left_small
    with dissolve
    show dad laugh at right_small
    with dissolve
    x "(He would laugh as he said that to me , with each laugh more of my self respect and dignity would be crushed under his foot)"

    scene dad_madd_room_sleep_vag_dad_foot_inside_madd_mouth_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd salivating at left_small
    with dissolve
    show dad sadistic at right_small
    with dissolve
    x "(He would pull it out completely increase its distance from my mouth, only to push it close to my face again )"
    x "(And my mouth would reach out to it again, as if meeting with a long lost lover and he would laugh at how much i was enjoying his foot in my mouth)"
    x "(As he would slide his foot back into its rightful place.)"

    scene dad_madd_room_sleep_vag_dad_foot_inside_madd_mouth_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    with dissolve
    show dad dominant at right_small
    with dissolve
    x "(I dont remember how long he kept his foot in my mouth , how many minutes or hours i continued to taste it. But at this point it started sweating more and more )"
    x "(His foot was getting wetter and wetter inside my mouth. Thick, hot sweat was pouring out of his skin, making everything slick and slimy.)"
    x "(The smell got so much worse — that thick, rotten, cheesy foot stink mixed with fresh sour sweat. It was filling my nose and throat, so strong it felt like I was breathing in pure filth.)"
    show madd inheat at left_small
    with dissolve
    x "(But even though the smell was disgusting and overwhelming, I wasn't hating it as much as I should. The warm, slippery texture of his sweaty foot against my tongue actually felt... good. )"
    x "(It felt like home. Like being wrapped up in something warm and familiar. My own dad's sweaty, dirty foot was making me feel safe and wanted. That's how messed up I was at this point. )"
    x "(The more it sweated, the more I wanted to keep licking it. I hated how much I was starting to crave the taste of his foot sweat.)"  

    scene dad_madd_room_sleep_vag_dad_foot_inside_madd_mouth_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd self loathing at left_small
    with dissolve
    show dad predatory at right_small
    with dissolve
    x "(By now i wasnt even trying to fight it anymore, I wasnt trying to hide it from myself or from him, I was just letting myself enjoy it as much as i could, as if i had given up on trying to resist it and just accepted that this is what i am now)"
    show madd resigned at left_small
    with dissolve
    x "(Feminine, submissive moans were escaping my lips as i was licking his foot. A clear sign of my body being molded to enjoy this, to crave this, to need this. )"
    x "(I realized how much i have changed, in such a short amount of time, how much i have given up on myself and my dignity, how much i have accepted being treated like this by my own dad )"
    show madd traumatized at left_small
    with dissolve
    x "(Probably it was after the day he came inside me for the first time, that i have fully accepted this new reality of mine. The warm, sticky feeling of his cum inside me was the final nail in the coffin for my old self )"

    scene dad_madd_room_sleep_vag_dad_foot_inside_madd_mouth_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd inhead at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "(I would try to take in as much of the experience as i could, trying to memorize every single detail of it, trying to imprint it in my mind forever .)"
    x "(The smell, the taste, the texture, the sound of his foot moving in my mouth, the way he would laugh at how much i was enjoying it, the way my body would react to it, the way i would moan and squirm under his foot... all of it was burned into my memory now. )"
    show dad delusional at right_small
    with dissolve
    dad_says "Poor Maddie, how are you ever gonna live without me now ?" 
    dad_says "Would you even want to live without me ? I am the only one who can make you feel this good after all"
    show madd resigned at left_small
    with dissolve
    x "(I wouldnt reply to him, just continue moaning and licking his foot, as if i was in a trance )"

    scene dad_madd_room_sleep_vag_dad_foot_inside_madd_mouth_7
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd inheat at left_small
    with dissolve
    show dad hungry at right_small
    with dissolve
    x "(He would pull out again and keep it at small distance from my face, not far enough to stop me from reaching out  )"
    x "(And thats exactly what i did , my neck would stretch out as i tried to reach his foot again, trying to get it back in my mouth as soon as possible )"
    show madd salivating at left_small
    with dissolve
    x "(Feeling a sense of relief as i finally got it back in my mouth, as if a mother bird had returned to its baby after a long time apart . How fucked is my brain)"
    show dad horny at right_small
    with dissolve
    dad_says "See, you cant even stay away from my foot for a few seconds, you need it too much already. "
    dad_says "But Daddy is getting horny now and he wants to put a baby inside his daughter, do you think you can handle that ?"
    show madd submissive nod at left_small
    with dissolve
    x "(Having it back in my mouth fulled me with joy as i just nodded at him, agreeing to whatever he said without even thinking about it)"
    show dad dominant at right_small
    with dissolve
    dad_says "Heh, actually you can keep sucking my foot while I fuck you. You deserve to be treated like a good foot slave after all "
    show madd resigned at left_small
    with dissolve
    x "(He pulled out his foot only to remove his shirt and pants and mine before putting his foot back in my mouth and then his dick entered inside me  )"

    scene dad_madd_room_sleep_vag_dad_foot_inside_madd_vag_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd deep blush at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(My pussy was already soaking wet from the way he was treating me, but as soon as his dick entered inside me, it felt like a floodgate had opened. I was drowning in my own arousal, in the pleasure and pain of being fucked by my own dad while he shoved his foot in my mouth )"
    x "(With every thrust of his dick his foot would also go deeper into my mouth, He was inside me in multiple ways at once. )"
    x "(I can feel every inch of his thick cock stretching my pussy open while my tongue is forced to lap at the sweaty, calloused sole of his foot.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(Every time he thrusts, his foot presses deeper, toes curling against the back of my throat. I can't breathe without inhaling the thick, musky stench of his foot. And the worst part? My body loves it. My pussy is clenching around him, milking him, begging for his cum while I gag and slurp on his foot sweat like a desperate whore.)"
    show dad dominant at right_small
    with dissolve
    dad_says "Keep sucking, baby. Lick between my toes while I breed this tight pussy of yours. "
    show madd resigned at left_small
    with dissolve
    x "(Even if i dont agree with what he says, my body has already accepted him as its master, and whatever he says my body molds itself to obey and enjoy it. )"
    show madd conflicted at left_small
    with dissolve
    x "(I wonder how far it would go...What else would he make me do ? How much more of my dignity would he crush under his command ? Regardless of the answer, I know the only thing for sure is that the whole world would be judging me for being a daughter who loves getting fucked by her own dad )"

    scene dad_madd_room_sleep_vag_dad_foot_inside_madd_vag_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    with dissolve
    show dad sadistic at right_small
    with dissolve
    x "(My voice is cracking higher now — desperate, girly, pleading whimpers spilling out around his toes. I sound like a broken little girl begging to be ruined.)"
    x "(His cock slams in and my pussy gushes instantly. Thick, wet squelch after squelch fills the entire room, loud and nasty, mixing with my feminine moans. Every thrust forces more of my juices to spray out around his shaft.)"
    x "(The sound is humiliating beyond words. That loud, sloppy, wet pounding is coming from my pussy  getting fucked by my own father. )"
    show madd violated at left_small
    with dissolve
    x "(I can't stop the noises. High, needy, feminine little cries keep escaping me while my pussy leaks nonstop, creating filthy wet echoes every time he bottoms out. The room is filled with the disgusting soundtrack of my own submission.)"
    x "(I'm so soaked it's obscene. The sounds are proof — undeniable, nasty proof — that I'm nothing but my dad's dripping, moaning fucktoy now.)"

    scene dad_madd_room_sleep_vag_dad_foot_inside_madd_vag_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    with dissolve
    show dad obsessed at right_small
    with dissolve
    x "(The saliva in my mouth is mixing with the sweat from his foot, creating a thick layer of filth in my  mouth. I try to swallow it but his foot is still there, making it impossible to get rid of the disgusting taste.)"
    x "(This creates a pool of foul liquid in my mouth, and as his foot continues to sweat, the pool grows larger and more revolting. With the movement of his foot the liquid sloshes around coming out of my mouth with a projectile force )"
    show madd violated at left_small
    with dissolve
    x "( Everything about this moment is humiliating and degrading.)"
    show dad delusional at right_small
    with dissolve
    dad_says "What say you Maddie, Wouldnt it be fun if we do this everynight ? That way we will have something to tell our future kids about  how they were conceived"
    dad_says "I can already imagine little runts sucking on your tits while you suck on my foot, just like their mommy does now. "
    show madd conflicted at left_small
    with dissolve
    x "(His words hit me like a prophecy I can't escape. Every night… forever. Me on my back with his foot in my mouth while he pumps load after load into my womb until I'm swollen with his child. Then doing it again the next night. And the next. Until there are little runts crawling around us.)"
    show madd inheat at left_small
    with dissolve
    x "(I can already see it — me breastfeeding his babies while I'm forced to suck on his filthy foot at the same time, just like he said. My own kids watching their mommy get used like this every single night. The thought is so fucking degrading it makes my pussy clench hard around his cock.)"

    scene dad_madd_room_sleep_vag_dad_foot_inside_madd_vag_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd overwhelmed at left_small
    with dissolve
    show dad cruel at right_small
    with dissolve
    x "(The second those filthy words leave his mouth my pussy clamps down hard around his cock like its trying to milk him dry on the spot. My body is answering his disgusting prophecy before my brain can even process it.)"
    show dad sadistic at right_small
    with dissolve
    dad_says "Ohhh fuck you just squeezed me like a vice, you nasty little btch. Hearing about our future kids made this greedy pussy lock up tight around Daddy's dick , didn't it?"
    show madd broken at left_small
    with dissolve
    x "(He laughs — a low, cruel sound — and suddenly starts slamming into me like a machine. Each thrust is brutal, faster, deeper, his hips crashing against me with wet, violent force. My whole body jolts with every impact.)"
    x "(My moans have changed completely. They're no longer high or girly. They're raw, guttural, animal.  Like a wounded dog being mounted and destroyed. The sounds are so primal and broken it doesn't even sound human anymore.)"
    x "(I'm nothing but a convulsing, barking, foot-sucking breeding hole now. And the way my pussy keeps gripping him tighter with every nasty word he says only proves how completely Ive accepted this twisted future as my only reality.)"

    scene dad_madd_room_sleep_vag_dad_foot_inside_madd_vag_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    with dissolve
    show dad mocking at right_small
    with dissolve
    x "(His foot is buried so deep it's acting like a drain plug, trapping all the thick, slimy mixture of my spit and his foot sweat inside my mouth. The disgusting pool keeps growing, pressing against the back of my throat, but it has nowhere to go.)"
    x "(I can feel it sloshing around with every movement of his foot, the liquid was so much in volume that it was actually making my cheeks bulge out ) "
    dad_says "Fuck Maddie, it feels like I'm wearing a wet sock . That foot's the only thing keeping all that nasty sht from pouring straight down your throat. Look at you — mouth full of your own drool and my foot sweat, sealed shut like a filthy little toilet."    
    show madd disgusted at left_small
    with dissolve
    x "(He suddenly lifts his leg just a few inches. The second his foot moves, the plug is gone. Everything floods in at once.)"
    x "(I can feel every drop sliding down inside me, warm and slimy, settling in my stomach. I'm literally being used as a drain. A warm, wet toilet that just got flushed by her own father's foot.)"
    show madd violated at left_small
    with dissolve
    x "(And the worst part? My pussy is still clenching hard around his dick the entire time, like my body is thanking him for treating me like this.)"
    show dad laugh at right_small
    with dissolve
    dad_says "AHAHAHA, look at you! You're so fucking disgusting. It feels like i Just flushed a toilet full of nasty foot sweat down your throat. And your pussy is still milking me like a desperate whore, even after all that filth just poured inside you. "

    scene dad_madd_room_sleep_vag_dad_foot_inside_madd_vag_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small
    with dissolve
    show dad dominant at right_small
    with dissolve
    x "(Right after he makes that cruel joke, his foot goes back deeper into my mouth, sealing it shut again. As the pool starts building up again while my moans thank him for it)"
    x "(He suddenly starts slamming into me like he's trying to break something inside. Every thrust is heavier, meaner, his dick driving so deep it feels like it's rearranging my guts.)"    
    x "(I can feel it happening — his dick is swelling inside me, getting thicker and longer until it reaches that terrifying full size I now know by heart. It stretches me to my absolute limit, pressing right against my cervix like it belongs there.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(My body recognizes it instantly. The way it throbs so violently, the way it pulses against my walls — this is what it feels like right before he floods me. My own pussy is already starting to flutter and squeeze like it's excited to receive his cum )"
    show madd conflicted at left_small
    with dissolve
    x "(I hate how natural it feels now. How my body has memorized the exact moment my stepfather's cock is at its hardest and fullest, like it's welcoming its rightful owner home. )"
    show dad lustful at right_small
    with dissolve
    dad_says "Fuck I'm about to blow, Maddie. Your nasty little pussy is about to get another load pumped straight into it while you're still sucking on my foot like a braindead whore. Get ready to take every drop, you filthy daughter."
    show madd inheat at left_small
    with dissolve
    x "(His cock is twitching so hard inside me now it feels like it's alive, jerking and swelling even more as he gets closer. My body is already preparing itself, clenching greedily around him like it can't wait to be filled again by the man who will inevitably be the father of my future kids.)"

    scene dad_madd_room_sleep_vag_dad_foot_inside_madd_vag_creampie_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd overwhelmed at left_small
    with dissolve
    show dad lustful at right_small
    with dissolve
    x "(His dick suddenly jerks violently inside me and I feel the first thick, hot spurt explode straight against my cervix. It's so powerful it feels like liquid fire shooting deep into my womb.)"
    dad_says "Fuuuuck — I'm cumming, Maddie! Take it all, you filthy little daughter. Daddy's pumping his seed straight into your womb. I'm gonna knock you up tonight, you nasty incest loving whore."
    show madd violated at left_small
    with dissolve
    x "(It's so much. My pussy was already drenched  from my own juices, and now his cum is mixing with it, forcing everything out. I can feel the warm, slimy mess immediately starting to leak out around his dick in thick, nasty globs that run down my butt and drip onto the sheets.)"
    x "(Every time he throbs and shoots another load, more of that filthy mixture squirts out of me. I'm overflowing. His cum is literally pouring out of my pussy while he's still inside me, like my body can't even hold all the incestuous seed he's pumping into me.)"
    show madd conflicted at left_small
    with dissolve
    x "(Every single creampie makes it more likely I'm going to end up pregnant with my own dad's child. The thought makes my stomach twist… but my pussy keeps clenching around him like it wants it to happen.)"
    show madd inheat at left_small
    with dissolve
    x "(I can feel it happening — the way my pussy keeps squeezing him, milking him, trying to pull every last drop out of him. My body is so desperate for his cum that it's doing everything it can to make sure I get every single drop, even if it means leaking out all over the place.)" 
    x "(He continued pounding me while I was leaking out all over the sheets, until finally he stopped pounding but stayed inside me )"
    show dad smirk at right_small
    with dissolve
    dad_says "God that was amazing, Maddie. "
    show madd distressed at left_small
    with dissolve
    x "(With his foot still in my mouth and his dick still buried deep inside me, I looked up at him, trying to find some trace of humanity in his face. So that he finally stops treating me like this)"
    show dad creepy at right_small
    with dissolve
    x "(But instead of seeing any remorse or guilt, I just see that same creepy smile)"
    dad_says "I see the pool of cum leaking out of your pussy . You're such a filthy little whore."
    show dad dominant at right_small
    with dissolve
    dad_says "Go Rub that nasty mess all over your tits, I want to see you covered in my cum like the good little daughter you are."
    show madd resigned at left_small
    with dissolve
    x "(I paused for a second, trying to find the strength to say no, trying to find the courage to stand up for myself for the first time in a while but his foot stench had me in trance like state)"
    x "(I used my hand to reach out to the bed sheet area right beneath my pussy and i picked a glob of cum and then i rubbed it all over my breasts, spreading it around until my whole chest was covered in his sticky, nasty seed)" 
    show dad laugh at right_small
    with dissolve
    dad_says "AHAHAHA, thats my girl . I have more in store for you."
    show madd overwhelmed at left_small
    with dissolve
    x "(He says that and he starts slamming into me again, harder and faster than before and i felt the same throbbing sensation as before...He's about to cum again )"

    scene dad_madd_room_sleep_vag_dad_foot_inside_madd_vag_creampie_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    with dissolve
    show dad obsessed at right_small
    with dissolve
    x "(The sound has changed completely. Every thrust now makes a thick, wet, squelching noise — my juices mixed with his heavy, sticky cum creating a nasty, creamy mess that splatters loudly with every brutal slam.)"
    x "(My moans are so loud now they're echoing off the walls. High, broken, animal sounds ripping out of my throat around his foot. I know they're loud enough to be heard through the entire house, even through my brother's gaming headset.)"
    show madd horrified at left_small
    with dissolve
    x "(What if he can hear me? What if he's sitting there right now listening to his own sister getting bred by our dad? The thought makes my stomach twist with shame… but my pussy clenches even harder around him.)"
    show madd conflicted at left_small
    with dissolve
    x "(Would he get hard hearing these sounds? Would he  demand to fuck me the same way once Dad finishes and he leaves my room? The idea of both of them taking turns breeding me makes my moans turn even more desperate and broken.)"
    show madd violated at left_small
    with dissolve
    x "(More and more of his thick cum keeps leaking out of me with every thrust, mixing with my juices and running down my butt in warm, slimy trails. I can feel it dripping onto the sheets in heavy globs while he keeps pounding me.)"
    x "(Every time that thick, hot cum spreads deeper inside me, I feel something inside me snap a little more. The warmth is sinking into my womb, coating my walls, and with each pulse I can feel my resistance crumbling away like wet paper.)"
    show madd resigned at left_small
    with dissolve
    x "(It's disgusting how good it feels. That sticky, heavy heat is melting the last bits of fight left in me. My body is learning to crave this — to crave being pumped full of my own father's seed until I'm nothing but a leaking, obedient hole.)"
    show madd inheat at left_small
    with dissolve
    x "(I can feel it happening again. The warmth is spreading through my belly, making my thoughts slower, heavier, more submissive. Every creampie makes me weaker. Every load makes it harder to imagine saying no to him ever again.)"
    show dad possessive at right_small
    with dissolve
    dad_says "Good , this time spread it all over your stomach. I am gonna paint you inside and out with my cum, just like a good little daughter should be."
    show dad delusional at right_small
    with dissolve
    dad_says "The whole world should know our father-daughter love story "

    scene dad_madd_room_sleep_vag_dad_foot_inside_madd_vag_creampie_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small
    with dissolve
    show dad possessive at right_small
    with dissolve
    x "(This time he continued pounding as i extended my hand to grab another glob of cum and spread it all over my stomach )"
    x "(I kept rubbing it in slow circles across my stomach, feeling the thick, sticky mess smear across my skin. It smelled so strong — heavy, musky, and unmistakably his. That deep, masculine scent of my own father's cum clinging to me like a second skin.)"
    show madd inhead at left_small
    with dissolve
    x "(The warmth was strange. Even though it was disgusting and slimy, the heat felt almost comforting as it soaked into my belly. Like a filthy, warm blanket wrapping around me from the inside out.)"
    x "(I moved my hands higher, spreading more of that nasty, thick load across my chest and between my breasts. The smell was getting stronger, filling my nose, but instead of making me sick it was making me feel oddly safe. Like I was being marked, claimed, and somehow… protected by it.)"
    x "(Every time I rubbed more of his cum into my skin, I felt a sick kind of comfort settle over me. It was warm, sticky, and reeked of sex with him — but it felt like being hugged by something that finally accepted every broken, filthy part of me. Like I belonged right here, covered in my father's seed.)"
    show dad dominant at right_small
    with dissolve
    dad_says "Okay This is my last one for tonight Maddie, I want you to spread this one all over your face. "

    scene dad_madd_room_sleep_vag_dad_foot_inside_madd_vag_creampie_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd overwhelmed at left_small
    with dissolve
    show dad sadistic at right_small
    with dissolve
    x "(More and more of his seed pours out around his dick in thick, creamy globs, running down my butt and soaking into the sheets. I can feel it everywhere — warm, sticky, and reeking of him.)"
    show madd trembling at left_small
    with dissolve
    x "(I reached down with trembling fingers, scooping up a thick handful of that filthy mixture from the soaked bedsheet. It was warm, slimy, and smelled so strong — a disgusting combination of his cum and the heavy musk from his foot still buried in my mouth.)"
    x "(I smeared it all over my face in slow, deliberate strokes. The thick, sticky mess coated my cheeks, my lips, and my nose. The smell hit me instantly — his foot sweat mixed with his thick, salty cum. It was overwhelming. It was everywhere.)"
    show madd inheat at left_small
    with dissolve
    x "(My nose was completely full of it. That nasty, masculine scent of my own father's cum and foot sweat was all I could breathe. And instead of disgust, I felt pure, sick ecstasy. My body was shaking with pleasure, my cunt clenching hard around him like this was the best thing I had ever felt.)"
    x "(I was in heaven. Covered in my stepdad's cum, his foot still stuffed in my mouth, his seed still leaking out of me… and I felt happier than I had in years. The realization terrified me. How could something this wrong, this incestuous, feel so fucking good?)"
    show madd conflicted at left_small
    with dissolve
    x "(I was scared. Not because of what he was doing to me… but because I was starting to love it. Because part of me wanted this disgusting, filthy life with him forever.)"
    show madd broken at left_small
    with dissolve
    x "(My entire body is coated now. Inside my womb, my cunt, my stomach, my tits, my face, my neck — every inch of me is drenched in his thick, warm, sticky seed. I can feel it clinging to my skin, his foot sweat sliding down my throat, and still leaking out of my ruined pussy in slow, heavy globs.)"
    show madd traumatized at left_small
    with dissolve
    x "(It feels like I've been baptized in his cum. Like every drop that touches me is washing away the old me and replacing it with something new — something filthy, obedient, and completely his.  Instead of disgust I feel a sick kind of rebirth.)"
    x "(In this disgusting, perverted baptism I made a silent vow. I pledged myself to him — not just as his daughter, but as his wife.  My body is already accepting it like it was always meant to be this way.)"
    x "(I'm already thinking of excuses. How I'll explain it to people. How I'll smile and say we fell in love after mom died. How natural it all was. The fact that I'm already preparing lies to protect this incestuous nightmare terrifies me more than anything he's done to me tonight.)"
    x "(I'm covered head to toe in my stepfather's cum, his foot still stuffed in my mouth, and I'm already planning how to tell the world that the man who raised me is now my husband. The realization makes me feel both sick and strangely complete at the same time.)"
    show dad smirk at right_small
    with dissolve
    dad_says "Ah, I am spent"
    show madd resigned at left_small
    with dissolve
    x "(He finally stops thrusting but his foot stays in my mouth. He stays in that position until i feel his dick start to soften inside me, few minutes later he finally pulls out and a large glob of his cum leaks out of me and onto the sheets. )"
    show dad possessive at right_small
    with dissolve
    dad_says "Damn i really did a number on you tonight, but cant blame me . You're such a hot daughter with a tight pussy.  "
    dad_says "Plus your body is as if its begging to be fucked by me"
    show madd broken at left_small
    with dissolve
    x "(I could see him heaving a sigh of satisfaction as he said that to me, like he was proud of how much he has ruined me and how much i have accepted being treated like this by him )"
    show dad creepy at right_small
    with dissolve
    dad_says "I'm so tired i could just sleep right here with you, but i dont like sleeping in my own cum. But you must be honored to be sleeping in it, after all you are my daughter and this is your rightful place now"
    show madd violated at left_small
    with dissolve
    x "(I knew what that meant, he wouldnt let me clean or change the sheets, he would just leave me there to sleep in my own filth)"
    show madd resigned at left_small
    with dissolve
    x "(I too was so exhausted that i just nodded at him, accepting that this is how the night will end and that i will be sleeping in a blanket getting soaked in my father's cum)"
    show dad dominant at right_small
    with dissolve
    dad_says "Good girl ,you deserve a treat like this after all. Get soaked well in daddy's cum and then get some rest "
    show madd traumatized at left_small
    with dissolve
    x "(After that he finally pulls out his foot from my mouth and climbs off the bed, as he starts to leave the room)"
    x "( I felt a strange sense of loss as his foot left my mouth, like a part of me was being ripped away. I wanted to beg him to stay, to keep his foot in my mouth, to keep treating me like this forever. )"
    show madd broken at left_small
    with dissolve
    x "(I was really exhausted so i pulled the blanket over myself and i just laid there, trying to fall asleep while my body was still buzzing from the experience and while i was still smelling his foot sweat and his old man cum  in my mouth hoping that i could just stay in this moment forever )"
    $ brother_hears_madd_moan = True
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["vaginal_sex"] += 1
    $ character_relations["dad"]["vaginal_creampie"] += 3
    $ character_relations["dad"]["intimacy"] +=11
    $ character_relations["dad"]["lust"] = 0
    $ character_relations["dad"]["anger"] = 0 
    $ dad_walks_in_madd_room_sleep_vag_2_flag = True
    $ journal_event_set_done("Dad", "Nightly Visits: Foot and Breeding")
    jump my_room_scene










