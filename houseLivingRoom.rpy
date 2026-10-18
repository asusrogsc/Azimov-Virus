
label living_room_scene:
    # Choose scene based on time of day
    python:
        if game_time.hour >= 18 and game_time.hour < 19:  # 18 to 19 inclusive
            living_room_bg = "scene_home_living_room_evening"
        elif game_time.is_morning() or game_time.is_afternoon():
            living_room_bg = "scene_home_living_room_morning_afternoon"
        elif game_time.is_evening():
            living_room_bg = "scene_home_living_room_evening"
        else:  # night
            living_room_bg = "scene_home_living_room_night"
    
    scene expression living_room_bg
    with fade

    $ journal_event_show("Dad", "Evening TV Trap")
    $ journal_event_show("Dad", "TV Night — Armpits and Breeding")
    $ journal_event_show("Dad", "Lifted and Bred in the Living Room")
    # This is for living room events with dad in the evening (18:00 - 19:00)
    if game_time.hour >= 18 and game_time.hour < 19:
        scene scene_living_room_evening_dad_watching_tv
        with fade

        show dad what at right_small
        with dissolve
        "You enter the living room. Dad is sitting on the sofa, watching TV. He seems absorbed in the show "
        
        
        menu:
            "Regarder la tv avec":
                if madd_willpower<10:
                    x "Je suis trop fatigué pour regarder la télé maintenant."
                    hide dad
                    with dissolve
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_77
                    jump living_room_scene
                show dad dominant at right_small
                with dissolve
                scene scene_living_room_evening_dad_watching_tv_madd_watching
                with fade
                call advance_time_and_check(minutes=10) from _call_advance_time_and_check_78
                x "Je m'assieds sur le canapé, à une distance respectueuse de lui. Papa me jette un bref coup d'œil avant de reporter son attention sur l'écran."
                x "( I watch the show with him, trying to blend into the background... )"
                if sofa_TV_dad_scene_done and character_relations["dad"]["lust"] >= 50 and character_relations["dad"]["intimacy"] >= 70 and renpy.random.randint(1, 100) <= 70:
                    x "(Like previous time he asked me to sit next to him and he starts touching my body against my will.)"

                    jump living_room_tv_with_dad_lust_scene_take_2


                jump living_room_tv_with_dad_lust_scene

                jump home_areas

            "Faire de l'exercice":
                if madd_willpower<30:
                    "Je suis trop fatigué pour faire de l'exercice maintenant."
                    hide dad
                    with dissolve
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_79
                    jump living_room_scene
                show dad controlling at right_small
                with dissolve
                "Dad barely glances at you as you move to do your exercises."
                hide dad
                with dissolve
                call Do_some_exercise_living_room from _call_Do_some_exercise_living_room
                jump living_room_scene

            "Retour au lobby":
                call advance_time_and_check(minutes=10) from _call_advance_time_and_check_80
                hide dad
                with dissolve
                jump home_areas
    else:
        "Vous entrez dans le salon. Il y a un canapé confortable, une table basse et une grande télévision fixée au mur."

        menu:
            "Regarder la Télé":

                menu:
                    x "Quel chaine?"
                    "Netflix?":
                        if madd_willpower<10:
                            "Je suis trop fatigué pour regarder la télé maintenant."
                            call advance_time_and_check(minutes=10)
                            jump living_room_scene
                        else:
                            jump Watch_TV

                    "Les informations":
                        if madd_willpower<10:
                            "Je suis trop fatigué pour regarder la télé maintenant."
                            call advance_time_and_check(minutes=5)
                            jump living_room_scene

                        if checkinfos == 0:
                            $ chance = renpy.random.randint(1, 100)
                            if chance <= 20:
                                $ checkinfos += 1
                                "Tu as réussi à obtenir des informations intéressantes."
                                jump Watch_infos
                            else:
                                "Tu regardes les infos, mais rien d’utile cette fois-ci."
                                call advance_time_and_check(minutes=5)
                                jump Watch_infos

                        if checkinfos == 1:
                            $ chance = renpy.random.randint(1, 100)
                            if chance <= 20:
                                $ checkinfos += 1
                                "Tu as réussi à obtenir des informations intéressantes."
                                jump Watch_infos
                            else:
                                "Tu regardes les infos, mais rien d’utile cette fois-ci."
                                call advance_time_and_check(minutes=5)
                                jump Watch_infos

                        if checkinfos == 2:
                            $ chance = renpy.random.randint(1, 100)
                            if chance <= 15:
                                $ checkinfos += 1
                                "Tu as réussi à obtenir des informations intéressantes."
                                jump Watch_infos
                            else:
                                "Tu regardes les infos, mais rien d’utile cette fois-ci."
                                call advance_time_and_check(minutes=5)
                                jump Watch_infos

                        if checkinfos == 3:
                            "Tu regardes les infos, mais rien d’utile cette fois-ci."
                            call advance_time_and_check(minutes=5)
                            jump Watch_infos

            "Faire de l'exercice":
                if madd_willpower<30:
                    "Je suis trop fatigué pour faire de l'exercice maintenant."
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_82
                    jump living_room_scene
                jump Do_some_exercise_living_room 


            "Dormir sur le canapé" :
                if madd_willpower <= 30:
                    scene scene_home_living_room_night
                    with fade
                    "You're too tired, you fall asleep on the sofa."
                    jump home_areas
                else:
                    "There is no way I can sleep here right now, I'm too alert. I will only sleep here if I'm extremely tired."
                    jump living_room_scene
            "Retour au lobby":
                jump home_areas




label Watch_TV:
    scene scene_living_room_watch_tv
    with fade
    "Vous allumez la télévision et vous regardez un moment."
    x "(Regarder la télévision m'aide à penser à autre chose pendant un moment.)"
    $ madd_willpower = min(madd_willpower +10, madd_willpower_max)
    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_83
    jump living_room_scene

label Watch_infos:
    scene scene_living_room_watch_tv
    with fade
    "Vous allumez la télévision et mettez la chaine des infos"
    x "(Que se passe t'il en ce moment aux infos ?)"
    $ madd_willpower = min(madd_willpower -10, madd_willpower_max)
    call advance_time_and_check(minutes=60)
    jump living_room_scene


label Do_some_exercise_living_room:
    if game_time.is_evening():
        if renpy.random.randint(1, 100) <= 70 and character_relations["dad"]["lust"] >= 50 and character_relations["dad"]["intimacy"] >= 40:
            jump Do_some_exercise_living_room_dad_watching_2 
        else :
            jump Do_some_exercise_living_room_dad_watching 
    else:
        scene scene_living_room_yoga
        with fade
        "You do some exercise in the living room."
        show madd happy at left_small
        with dissolve
        x "( Doing some stretches and light exercises helps me relax. )"
        x "(I feel low on energy, but i think i have more maximum energy now.)"
        $ madd_willpower_max += 1
        $ madd_willpower = max(madd_willpower -30, 0)
        call advance_time_and_check(minutes=120) from _call_advance_time_and_check_84
        jump living_room_scene


label sleep_on_sofa:
    scene scene_madd_sleeping_living_room_night
    with fade
    show madd violated at left_small
    with dissolve
    x "( This is dangerous... , sleeping in the open like this. Bad things could happen... )"
    x "(especially with these people around... )"
    x "( But I'm so tired... )"
    x "( Just a quick nap... )"

    $ journal_event_show("Dad", "Sofa Sleep")
    $ journal_event_show("Brother", "Sofa Sleep")

    $ sleep_event_chance = renpy.random.randint(1, 100)
    
    if not(dad_tried_to_drag_madd_to_his_room) and character_relations["dad"]["intimacy"] >=40 and (character_relations["dad"]["anger"] >= 70 or (character_relations["dad"]["lust"] >= 60 and madd_room_got_unlocked) or (character_relations["dad"]["lust"] >= 60 and "madd_home_room" in locked_home_areas)):
        $ dad_tried_to_drag_madd_to_his_room = True
        $ dad_drag_madd_last_day = days_passed
        jump living_room_madd_sleeping_drag_to_room_dad

    if madd_willpower <= 30 and character_relations["brother"]["lust"] >= 70:
        jump living_room_sleep_brother_1
    elif sleep_event_chance <= 80:
        call living_room_sleep_dad_scenes from _call_living_room_sleep_dad_scenes
    else:
        call sleep_on_sofa_nothing_happened from _call_sleep_on_sofa_nothing_happened





## Sleeping on SOFA SCENES 

label living_room_sleep_dad_scenes:
    if character_relations["dad"]["anger"] >= 60 or (character_relations["dad"]["lust"] >= 40 and madd_room_got_unlocked) or (character_relations["dad"]["lust"] >= 20 and "madd_home_room" in locked_home_areas):
        call anger_event_dad_sofa_sleep_rim from _call_anger_event_dad_sofa_sleep_rim
    else:
        call sleep_on_sofa_nothing_happened from _call_sleep_on_sofa_nothing_happened_dad
    


label anger_event_dad_sofa_sleep_rim:
    
    scene scene_madd_sleeping_living_room_night
    show dad obsessed at right_small
    with fade

    dad_thinks "Well, well, look who decided to take a nap out in the open."
    dad_thinks "You have been ignoring my advances for too long."
    dad_thinks "I treat you well, and this is how you repay me?"
    "He sits down beside you, a sinister smile spreading across his face."
    "Watching you sleep, he seems to be contemplating something."
    scene scene_madd_sleeping_living_room_night_dad_watching
    show dad lecherous at right_small
    with dissolve

    dad_thinks "Time to teach you a lesson about respect."
    dad_thinks "I loved you like I loved your mother, and this is how you treat me?"
    dad_thinks "Maybe a little reminder of who's in charge will help you remember your place."
    scene scene_madd_sleeping_living_room_night_dad_approaching
    show dad predatory at right_small
    with dissolve
    "Dad's footsteps are silent against the living room floor, measured and deliberate. He approaches you with the precision of a hunter closing in on vulnerable prey."
    "His eyes sweep across your sleeping form with calculating intensity—noting the rise and fall of your chest, the way your guard is completely down, how utterly defenseless you are."
    "He sees you sleeping peacefully, completely unaware of the predator circling closer."
    show dad fixated at right_small
    with dissolve
    "He slowly moves closer, his intentions written plainly in the hunger burning behind his eyes. His breathing deepens, quickening with anticipation."
    "His fingers work at his clothes with deliberate slowness, each piece discarded without ceremony. Cool air touches his bare skin, but he doesn't shiver—the heat building within him is overwhelming."
    scene scene_madd_sleeping_living_room_night_closeup_madd_face
    with fade
    show dad dominant at right_small

    "He positions himself directly over your prone body, his weight suddenly bearing down as he settles into place. Your limbs are completely pinned beneath his superior strength—there's no possibility of escape, no room for resistance."
    "His breath is hot against your face now, each exhale carrying the musk of his arousal. He lowers himself further, his thighs spreading as he shifts into position."
    
    scene scene_madd_sleeping_living_room_night_dad_on_top_squatting
    show dad possessive at right_small
    with dissolve
    "He then starts squatting down over your face, his entire body trembling with barely-restrained appetite. The darkness of his shadow falls across you—you are now entirely subsumed beneath him, existing only in his shadow."
    show dad controlling at right_small
    with dissolve
    "His feet plant themselves firmly across your hands, the soles pressing down with careful precision. The weight is immobilizing, absolute. Your hands are completely trapped beneath his arches, unable to move even a fraction."
    
    show madd conflicted at left_small
    with dissolve
    x "(Uhh... what is happening...)"
    x "(I feel a single hair drop onto my face... )"

    show madd overwhelmed at left_small
    with dissolve
    x "(The sudden weight jolts me awake, dragging me violently from sleep into a nightmare I can't escape.)"

    scene scene_madd_sleeping_living_room_night_dad_on_top_squatting_eyes_open
    with fade
    x "(As soon as my eyes snap open, I see a hairy crotch inches from my face—dark, coarse hair that seems to fill my entire vision.)"
    show madd helpless at left_small
    with dissolve
    x "(It's coming down toward me, descending slowly, deliberately, with the weight of inevitability.)"
    
    show dad predatory at right_small
    dad_thinks "Time to remind you exactly who runs this house, Maddie."
    show dad obsessed at right_small
    dad_thinks "Ah, she's waking up. Perfect. Let her see what's about to happen."
    
    show madd nauseated at left_small
    with dissolve
    x "(What the fuck is going on...there is someone's hairy ass right in front of my face... I can smell it already... it's so close... )"
    x "(He's slowly lowering himself down, his hairy mess getting closer and closer to my face... I can feel the heat radiating off it already... )"
    x "(No... please... not this...)"
    show madd helpless at left_small
    with dissolve
    x "(My voice catches in my throat—barely a whisper, utterly useless.)"
    
    show dad cruel at right_small
    with dissolve
    dad_says "Wake the fuck up, princess. Daddy's gonna teach that pretty little face what happens when you ignore me."
    show dad dominant at right_small
    with dissolve
    dad_says "I told you to respect me, and this is how you do it."
    dad_says "I loved you, and you rejected me. I will get what I want."
    x "(I can't believe this is happening...)"
    show madd overwhelmed at left_small
    with dissolve
    x "(My heart is hammering so violently against my ribs I think it might shatter.)"
    x "(He's forcing himself on me... my body is completely immobilized beneath his weight.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(The shame burns hotter than the weight crushing me—I'm nothing but a toy under him now..)"
    
    show dad coercive at right_small
    with dissolve
    dad_says "Disobedience has consequences. Tonight you're going to learn them the hard way."
    show dad calculating at right_small
    with dissolve
    dad_says "Now, take a deep breath and accept your fate."
    
    show madd helpless at left_small
    with dissolve
    x "(Resistance was never an option. From the second his shadow fell over me, I was already his.)"
    show madd conflicted at left_small
    with dissolve
    x "(My body is pinned completely, unable to move, unable to resist.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(His weight is crushing, oppressive, inescapable.)"

    scene scene_madd_sleeping_living_room_night_dad_on_top_squatting_nose_insertion
    with dissolve

    show madd shocked at left_small
    show dad lustful at right_small
    with dissolve
    x "he lowered himself enough that his hairy ass was now touching my face "
    show madd horrified at left_small
    with dissolve
    x "(My protruding nose was now in direct contact with his hairy ass... and the smell was directly in my nostrils... )"
    x "(The smell hits like a thick, warm fog—earthy, slightly sour, with that unmistakable bitter musk that makes my eyes water instantly.)"
    show madd helpless at left_small
    with dissolve
    x "(My brain short-circuited; all I could do was lie there while he used me.)"
    show madd nauseated at left_small
    with dissolve
    x "(He started moving his ass up and down , the hair of his butt directly entering my nostrils... and going out... in and out... the smell was getting stronger and stronger with each movement... )"
    x "(Each pass drags the puckered skin across my nose, leaving a thin film of sweat that tastes faintly metallic and unclean when I accidentally inhale through my mouth.)"
    show dad dominant at right_small
    show madd distressed at left_small
    with dissolve
    x "(It was a power play to remind me of his dominance over me... )"
    x "(I tried to close my eyes hopefully thinking if i can't see it, maybe it won't be as bad... but the smell was still there... and it was getting stronger and stronger... )"
    show madd horrified at left_small
    with dissolve
    x "(I couldnt keep my eyes closed for long... I had to open them again... and as soon as i did i saw the hairy asshole right in front of my face)"
    show madd broken at left_small
    with dissolve
    x "(I knew tonight he would make me clean it with my tongue... but i didnt expect him to do this first... to humiliate me like this... to make me feel so small and powerless... )"

    scene scene_madd_sleeping_living_room_night_dad_on_top_squatting_nose_insertion_1
    with dissolve

    show madd helpless at left_small
    show dad dominant at right_small
    with dissolve
    x "(He started moving his ass again , now from the tip of my nose to the center of my eyes.)"
    show dad cruel at right_small
    with dissolve
    dad_says "Look at it, Maddie. This is your new station in life—right under me. "
    x "(The deeper he grinds, the stronger the smell becomes—raw, animal, with a sharp tang that clings to the back of my throat like spoiled meat.)"
    dad_says "This is what you get if you disobey me. You will fucking smell my stinky asshole every night until you learn your place. "
    show madd trembling at left_small
    with dissolve
    x "(i was already shaking with fear , the threat of having to smell his stinky butthole every night was already too much for me to handle )"
    show madd resigned at left_small
    with dissolve
    x "(I knew it wasnt an idle threat... he would do it... and i would have to endure it... every night... )"
    show dad sadistic at right_small
    with dissolve
    dad_says "And once i am finished making you get used to the smell, then i will make you lick it clean with your tongue. You will be my little toilet, Maddie. "
    show madd nauseated at left_small
    with dissolve
    x "(I knew it was coming... the thought of having to lick his stinky asshole with my tongue was already making me feel sick... )"
    show madd disgusted at left_small
    with dissolve
    x "(A man as sick and twisted as my stepdad , dont know how many bacteria and germs are living in his stinky butthole... )"
    show madd violated at left_small
    with dissolve
    x "(right now he was rubbing his hairy asshole on my nose , the tender skin of his butthole was directly in contact with my skin... being rubbed against it)"

    scene scene_madd_sleeping_living_room_night_dad_on_top_squatting_nose_insertion_2
    with dissolve

    show madd nauseated at left_small
    show dad possessive at right_small
    with dissolve
    x "(Meanwhile , his hairy balls  were also rubbing on me near the chin area... )"
    show madd overwhelmed at left_small
    with dissolve
    x "(It was like a festival of stinky body parts rubbing on me... his hairy asshole on my nose and his hairy balls on my chin... )"
    show dad mocking at right_small
    with dissolve
    dad_says "TIme for me to close the lid of the toilet "
    show madd helpless at left_small
    with dissolve
    x "(As he said that I saw eclipses in my vision... i knew my whole face was going to be covered in his stinky asshole... and i was going to have to endure the smell for a long time... )"
    show madd horrified at left_small
    with dissolve
    x "(As i saw his buttcheeks covering both my eyes , i would have no choice but to inhale his stink and my eyes would have nothing else to look at but his hairy crease )"
    show madd traumatized at left_small
    with dissolve
    x "(it only lasted for a few seconds... but it felt like an eternity... and he lifted his ass off my face)"
    show dad controlling at right_small
    with dissolve
    dad_says "Dont worry Maddie, You will learn your place one step at a time. I wont go all out on you right away. "
    show madd resigned at left_small
    with dissolve
    x "(I knew his endgoal was still the same , just getting there in a more gradual way... but it didnt make it any easier to handle... )"

    scene scene_madd_sleeping_living_room_night_dad_on_top_squatting_mouth_rub_1
    with dissolve

    show madd violated at left_small
    show dad predatory at right_small
    with dissolve
    x "(He knew his body parts , he started rubbing his hairy asshole near my lips now...)"
    show madd nauseated at left_small
    with dissolve
    x "(the soft tender skin of his butthole was now rubbing against my lips... the heat and the smell emanating from it was making me feel sick... )"
    show madd disgusted at left_small
    with dissolve
    x "(This was such a disgusting place to be in...Having your stepdads stinky asshole rubbing against your face... and now your lips... )"
    show madd overwhelmed at left_small
    with dissolve
    x "(He kept rubbing it against my lips for a while , if i wasnt in a horizontal position i would have probably vomited right there... )"
    show dad mocking at right_small
    with dissolve
    dad_says "I could feel your lips trembling under my butthole, Maddie. Dont be scared of your food ."
    show madd conflicted at left_small
    with dissolve
    x "(There is surely something wrong with his mind . How can he talk like that its his asshole thats devouring my face not the other way around... )"

    scene scene_madd_sleeping_living_room_night_dad_on_top_squatting_mouth_rub_2
    with dissolve

    show madd helpless at left_small
    show dad sadistic at right_small
    with dissolve
    x "(He started moving again , but this time my mouth was open . He dragged his stinkhole from the lips to my nose and back to the lips again... )"
    show madd broken at left_small
    with dissolve
    x "(At a point my nose was almost inside his asshole... that was the point the smell was the strongest... it felt like all the happines and joy in the world was being sucked out of my life and it was replaced with despair and sadness... )"
    show madd traumatized at left_small
    with dissolve
    x "(Thats the effect he had on me with this disgusting act... )"
    show madd nauseated at left_small
    with dissolve
    x "(I was breathing in directly from the source of it . The mist of it compltely filling my lungs )"
    show madd broken at left_small
    with dissolve
    x "(If this is the air i have to breathe in every night , then i might as well just give up on life... i felt like a flower whos petals were being slowly plucked off one by one... )"
    show dad dominant at right_small
    with dissolve
    dad_says "Okay Maddie , now time to cover your whole face"
    show dad cruel at right_small
    with dissolve
    dad_says "Take a good look at  whatever you can now, its gonna go dark soon and all you'd be able to see is my arsehole... "
    show madd resigned at left_small
    with dissolve
    x "(I have predicted this for a long time... but it was still a shock to see it happen... to see him say it out loud... to see him say it with such confidence and certainty... )"
    show madd helpless at left_small
    with dissolve
    x "(I prepared for the worst)"




    scene scene_madd_sleeping_living_room_night_dad_on_top_squatting_all_the_way_down
    with fade
    x "(Slowly he lowers himself onto my face. The contact is unavoidable. )"
    x "(The taste is already on my lips even though I haven't licked yet—bitter, slightly acrid, like concentrated sweat mixed with the faintest hint of what's inside him.)"
    x "(Fuck… the thick, bitter funk of his sweaty asshole is already leaking onto my lips. It tastes like pure musk and something darker, earthier, almost dirty.)"
    x "(I felt it—the coarse hair tickling against my skin, the rough texture scraping as he settles his full weight.)"
    x "(My vision is completely filled with his hairy ass now, the darkness punctuated only by the occasional glimpse of skin.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(His thighs press down on either side of my head, the muscles flexing as he positions himself.)"
    x "(His balls are positioned right at my chin now, the flesh warm and heavy.)"
    show madd nauseated at left_small
    with dissolve
    x "(His dick rests just around my neck, the shaft thick and pulsing with his heartbeat.)"
    x "(The smell assaults my senses immediately , a thick, musky scent that fills my nostrils with every breath.)"
    x "(It's heavy and sour, like old sweat mixed with the sharp tang of his unwashed crack. Every breath pulls more of that raw, filthy asshole smell straight into my lungs.)"
    
    show madd helpless at left_small
    with dissolve
    x "(I tried to hold my breath, to protect myself from this olfactory invasion, but I can't—my body demands oxygen.)"
    show madd conflicted at left_small
    with dissolve
    x "(His asshole is right there, hovering inches from my nose. I can see the puckered flesh in the total dark vision i have, the dark opening.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I felt so degraded... like I've been reduced to something less than human.)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "This is what ungrateful little bitches get for forgetting who's been taking care of them. Smell my dirty asshole and remember."

    
    show madd overwhelmed at left_small
    with dissolve
    x "(It was right in front of my nose... the opening seems to expand and contract slightly with each breath he takes.)"
    show madd helpless at left_small
    with dissolve
    x "(I could feel the warmth radiating off him—an almost feverish heat that seems to intensify with each passing second.)"
    x "(The heat coming off it is almost overwhelming, creating a humid microclimate around my face.)"
    show madd conflicted at left_small
    with dissolve
    x "(If it was any other moment, I would have been surprised something like this could generate so much heat...)"
    show madd nauseated at left_small
    with dissolve
    x "(But right now, I was too humiliated, too terrified, too utterly trapped to think about anything else.)"
    x "(I just wanted this to be over... but somehow I know it won't be.)"
    
    show dad possessive at right_small
    with dissolve
    dad_says "There, that's better. You're getting the idea now."
    
    show madd helpless at left_small
    with dissolve
    x "(He had finally settled completely, like a predator making its kill permanent.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(All his weight was on me, pressing down with the force of someone who knows they have complete power.)"
    x "(I couldn't move. My hands are numb beneath his feet, my body flattened beneath his superior mass.)"
    show madd conflicted at left_small
    with dissolve
    x "(Slowly, my lungs burning, I couldn't hold my breath anymore...)"
    show madd nauseated at left_small
    with dissolve
    x "(I had to breathe in his smell—I had no alternative, no escape from this forced intimacy.)"
    x "(So I did, taking a deep breath involuntarily.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(The smell is so strong that I can taste it on the back of my throat—not a smell anymore but a physical thing, coating my mouth.)"
    show madd nauseated at left_small
    with dissolve
    x "(It was the smell of his asshole—so foul, so pungent, so raw, so unrelentingly dominant.)"
    
    show dad fixated at right_small
    with dissolve
    dad_thinks "Good, she's starting to accept her place in my world."
    show dad possessive at right_small
    with dissolve
    dad_says "I can feel your rhythmic breathing now Maddie, Good girl. Accept your new reality."
    
    show madd helpless at left_small
    with dissolve
    x "(I was breathing in and out, each breath a violation, a surrender.)"
    show madd conflicted at left_small
    with dissolve
    x "(His scent was filling my lungs, saturating every corner of my respiratory system.)"
    x "(I could feel it—the dominance, the control, the sheer assertion of his will over mine.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(I felt so small... so powerless... like an ant beneath his heel.)"
    show madd nauseated at left_small
    with dissolve
    x "(Every breath is pure him now. There's no air left in the world that doesn't taste like Dad.)"
    
    show dad authoritative at right_small
    with dissolve
    dad_says "That's it, that's who you are... my submissive little pet..."
    show dad dominant at right_small
    with dissolve
    dad_says "You eat what I give you... you breathe what I give you... you drink what I give you..."
    show dad sadistic at right_small
    with dissolve
    dad_says "You exist to serve me... to worship me... to obey without question."
    
    show madd helpless at left_small
    with dissolve
    x "(This was the most submissive position I could be in ,completely vulnerable and absolutely helpless.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(Right underneath him, the weight of his body a constant reminder of my total subjugation.)"
    show madd nauseated at left_small
    with dissolve
    x "(Smelling his dominant stinky asshole, breathing in his musk with every forced breath.)"

    
    show madd helpless at left_small
    with dissolve
    x "(Just existing to serve him, my entire purpose reduced to satisfying his desires.)"
    
    show dad lecherous at right_small
    with dissolve
    dad_says "Do you understand your place now? Do you comprehend your role?"
    
    show madd nauseated at left_small
    with dissolve
    x "(I didnt want to accept it... I wanted to fight it... but I couldn't... only way out was through acceptance... )"
    x "(I nodded weakly, the motion limited by the weight pressing down on me.)"
    
    show dad predatory at right_small
    with dissolve
    dad_says "I will take that as a yes."
    dad_says "Maybe now you'll think twice before ignoring me. Maybe now you'll show your father proper respect."
    show madd overwhelmed at left_small
    with dissolve
    dad_says "But to burn the lesson in deeper, to make it unforgettable..."
    dad_says "I think a little more time under me is in order."
    show madd helpless at left_small
    with dissolve
    dad_says "After all, you need to learn to be a good wife for me someday, and this is the first step in that process."
    show madd nauseated at left_small
    with dissolve
    dad_says "So, just relax and enjoy your place beneath me."
    
    show dad obsessed at right_small
    with dissolve
    dad_says "Now, close your eyes and breathe deeply. Breathe in my essence."
    
    show madd helpless at left_small
    with dissolve
    x "(I closed my eyes, though it made no difference—the darkness was already complete.)"
    show madd conflicted at left_small
    with dissolve
    x "(I was trying to accept my fate, to surrender to the inevitable.)"
    x "(I took deep breaths, each one drawing more of his musk deep into my lungs.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(Inhaling his dominant scent, letting it coat every surface of my respiratory system.)"
    show madd nauseated at left_small
    with dissolve
    x "(Exhaling weakly, my body completely depleted of any resistance.)"
    show madd helpless at left_small
    with dissolve
    x "(I did what he said, that was my only choice—compliance was the only path forward.)"
    
    show dad horny at right_small
    dad_says "That's it, now use your tongue and clean me up. Show me your submission with your mouth."
    show dad dominant at right_small
    show madd nauseated at left_small
    with dissolve
    x "(Huh... what?)"
    show madd overwhelmed at left_small
    with dissolve
    x "(I knew it would inevitably be asked of me but I  couldn't believe he could put it in words... the request is so degrading, so utterly humiliating.)"
    
    show dad predatory at right_small
    with dissolve
    dad_says "You heard me right. I need you to obey."
    show dad dominant  at right_small
    with dissolve
    dad_says "Shove that tongue deeper, Maddie. I want to feel it fucking inside my shithole. Clean me out."
    show madd helpless at left_small
    with dissolve
    dad_says "It's the only way you'll learn your place, the only path to acceptance. Lick my asshole."

    scene scene_madd_sleeping_living_room_night_dad_on_top_squatting_all_the_way_down_licking_asshole
    with fade  
    show madd conflicted at left_small
    with dissolve
    x "(I hesitated for a moment, my body screaming in protest against what's being asked.)"
    show madd nauseated at left_small
    with dissolve
    x "(My mind recoils, but then I realized I had no choice... refusal would only bring worse consequences.)"
    x "(I slowly stuck out my tongue, the muscle extending with infinite reluctance.)"
    show madd helpless at left_small
    with dissolve
    x "(Every millimeter that my tongue extended felt like an eternity—crossing a boundary I can never uncross.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(Finally, my tongue touched his asshole, making contact with the puckered flesh.)"
    x "(The second my tongue drags across the wrinkled hole the taste explodes—bitter, salty, with a deep musky tang that makes my stomach twist even as I keep licking.)"
    x "(My tongue was trembling with revulsion and fear, shaking against the contact.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I was right at his asshole, the opening seeming impossibly intimate, impossibly vile.)"
    show madd helpless at left_small
    with dissolve
    x "(The smell was even worse up close—acrid, raw, almost choking in its intensity.)"
    x "(But I had to do it... resistance was futile, acceptance was my only survival mechanism.)"

    show dad lustful at right_small
    with dissolve

    x "(I started licking, my tongue moving against the flesh.)"
    x "(I can taste the sweat and the faint bitterness from inside his ass with every slow lap. The puckered skin twitches under my tongue, hot and slightly sticky.)"
    show sofa_event_angry_dad_licking_butthole_close_p_side_view at topleft
    with Dissolve(2.0)

    show madd conflicted
    with dissolve
    x "(The taste was awful—bitter, wrong, everything my instincts screamed to reject.)"
    x "(So much worse than I imagined, worse than my darkest fears.)"
    show madd overwhelmed at left_small
    with dissolve

    x "(But I kept going, my body moving almost independently of my mind.)"
    show madd nauseated at left_small
    with dissolve

    x "(I had to show him I was submissive, that I understood my role.)"
    x "(I licked and licked, my tongue exploring every contour, until I felt he was clean.)"
    hide sofa_event_angry_dad_licking_butthole_close_p_side_view
    with fade
    show dad debased at right_small
    with dissolve

    dad_says "There, that's better. You're doing wonderfully."
    show dad sadistic at right_small
    with dissolve
    dad_says "Keep going, you're doing exactly what a good girl should do."
    
    show madd nauseated at left_small
    with dissolve
    x "(I continued licking, feeling so humiliated that reality seemed to splinter.)"
    show madd conflicted at left_small
    with dissolve
    x "(My sense of self was crumbling with each lick, each degradation.)"
    x "(But also strangely... compliant... like my body was developing its own logic.)"
    show madd helpless at left_small
    with dissolve
    x "(Like this was where I belonged—beneath him, serving him, existing only for his pleasure.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(His asshole was twitching against my tongue, the flesh responding to my touch.)"
    x "(I could feel it generating more heat, more scent—the sensations overwhelming my senses completely.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(And I was taking it all in, incorporating it into my body, becoming one with his dominance.)"
    
    show dad hungry at right_small
    with dissolve
    dad_says "Good, very good. You're becoming exactly what I need."
    show dad possessive at right_small
    with dissolve
    dad_says "That's my good girl… you're finally starting to feel like the little wife I always wanted. "
    show dad dominant at right_small
    with dissolve
    dad_says "Keep sucking and licking like a good little wife and I'll knock you up before the month's over. That's what you were made for."
    show madd conflicted at left_small
    with dissolve
    dad_says "Now, go in. Push deeper."
    show madd helpless at left_small
    with dissolve
    dad_says "Make your tongue go inside my asshole—I want to feel you from the inside."
    
    show madd nauseated at left_small
    with dissolve
    x "(No... I couldn't believe it...)"
    show madd overwhelmed at left_small
    with dissolve
    x "(He wanted me to put my tongue inside his asshole—to violate myself in his service.)"
    x "(Why would he want that... what compels him to push further, to demand more?)"
    show madd helpless at left_small
    with dissolve
    x "(But I had no other choice... refusal meant pain, rejection, further punishment.)"
    
    
    scene scene_madd_sleeping_living_room_night_dad_on_top_squatting_tongue_inside_asshole
    with fade

    show madd conflicted at left_small
    with dissolve
    x "(I slowly pushed my tongue toward the center of his asshole, gathering my courage.)"
    x "(It was so tight—the sphincter resisting the intrusion with muscular clenching.)"
    
    show madd helpless at left_small
    with dissolve
    x "(But I had to do it, my body now completely enslaved to his demands.)"
    show madd nauseated at left_small
    with dissolve
    x "(I had to push using my tongue muscles, straining to overcome the resistance.)"

    scene scene_madd_sleeping_living_room_night_dad_on_top_squatting_tongue_inside_asshole_0
    with fade


    show madd overwhelmed at left_small
    with dissolve
    x "(Finally, my tongue slipped inside—a momentary give followed by tightness enfolding my tongue.)"
    x "(Inside it's even nastier ...hot, velvety, with a thick metallic-fecal taste that coats my whole tongue. I can feel his asshole clenching around me, pushing more of that filthy flavor into my mouth.)"
    x "(The taste was even worse inside—metallic, foul, absolutely repugnant.)"
    show madd conflicted at left_small
    with dissolve
    x "(But I kept going, my mouth now serving as an instrument of my own degradation.)"
    x "(I was completely submissive now, my mind broken into compliance.)"
    show soft_event_angry_dad_licking_butthole_tongue_inside_close_up_pop_up at topleft
    with Dissolve(2.0)

    show madd nauseated at left_small
    with dissolve
    x "(My tongue was inside his asshole, that sacred part of me now desecrated.)"
    show madd helpless at left_small
    with dissolve
    x "(Taking in his dominant scent from the inside, breathing him in completely.)"
    
    show dad possessive at right_small
    with dissolve
    dad_says "Excellent. You're a quick learner, aren't you?"
    show dad controlling at right_small
    with dissolve
    dad_says "Keep that up and you will end up my wife soon enough. I will make you lick my arsehole every day, and you will love it."
    show madd overwhelmed at left_small
    with dissolve
    dad_says "Now, keep cleaning my insides. Show me your devotion."
    
    show madd conflicted at left_small
    with dissolve
    x "(I continued licking inside his asshole, my disgust at myself nearly eclipsing my disgust at him.)"
    show madd nauseated at left_small
    with dissolve
    x "(Feeling so humiliated that I wondered if shame could physically destroy a person.)"
    x "(But some part of me felt aroused by his dominance—a sickening realization that appalls me.)"
    show madd helpless at left_small
    with dissolve
    x "(Like this was where I belonged, where my body knew its true purpose.)"
    x "(What the hell? Why am I thinking like this? Perhaps  its due to the pheromones he's producing, saturating me with his essence.)"
    x "(Perhaps its because my lungs are full of his scent, my body chemistry rewiring itself to crave him.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(His asshole was clenching around my tongue, the sphincter gripping me rhythmically.)"
    x "(I could feel it generating more heat, more scent, the sensations growing unbearable.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(The tightness was incredible—a visceral reminder of his power and my powerlessness.)"
    show madd conflicted at left_small
    with dissolve
    x "(The taste was that of a metallic tang mixed with raw flesh . primal, animalistic, overwhelming.)"
    hide soft_event_angry_dad_licking_butthole_tongue_inside_close_up_pop_up
    with fade 

    show madd conflicted at left_small
    with dissolve
    x "(Whatever it was, I couldn't get enough—my body had betrayed my mind completely.)"
    show madd nauseated at left_small
    with dissolve
    x "(I kept licking, my tongue moving with increasing enthusiasm.)"
    x "(Until he was completely clean, my mouth having served its purpose.)"
    
    show dad predatory at right_small
    with dissolve
    dad_says "Ah Maddie , you're really doing it on your own now. I'm impressed."
    show dad lustful at right_small
    with dissolve
    dad_says "Heh, every woman starts loving it eventually. You just have to give it time."
    show dad obsessed at right_small
    with dissolve
    dad_thinks "Maybe now I can push this further... I can take what I truly want."
    
    scene scene_sofa_event_angry_madd_face_inside_dad_ass
    with  fade

    show dad lecherous at right_small
    with dissolve
    dad_says "There, all clean. You did exceptionally well."
    show madd helpless at left_small
    with dissolve
    dad_says "You did very well for your first time. Such obedience."
    show madd overwhelmed at left_small
    with dissolve
    dad_says "Now, put my right balls in your mouth. Worship them."
    
    show madd conflicted at left_small
    with dissolve
    x "(At this point, I was completely submissive, my will utterly broken.)"
    show madd nauseated at left_small
    with dissolve
    x "(I was automatically obeying his commands, my body responding without conscious thought.)"



    x "(I pulled out my tongue from his asshole—the sensation of separation leaving me strangely empty.)"
    show madd helpless at left_small
    with dissolve
    x "(But it felt like someone snatched a part of me away, like I was losing something essential.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(I wanted to keep licking, wanted to return to my place, wanted to serve.)"
    x "(But I had to obey... I had to accept the new command.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(Obey my master... that's all I was now, all I would ever be.)"
    show madd nauseated at left_small
    with dissolve
    x "(I opened my mouth, preparing to receive him.)"
    show sofa_event_angry_dad_sucking_ball_close_up_pop_up at topleft 
    with Dissolve(2.0)
    
    x "(He lifted himself for a second and then settled again, placing his right ball in my mouth.)"
    show madd helpless at left_small
    with dissolve
    x "(The taste was overwhelming—salty, musky, carrying the weight of his dominance.)"
    x "(His heavy balls are sweaty and salty, but every time they drag across my nose I get another blast of that same thick asshole musk still clinging to his skin.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(So much raw dominance concentrated in such a small area, flooding my senses.)"
    x "(But I kept it in my mouth, cradling it with my tongue and lips.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I had to show him I was a good submissive, that I understood my sacred duty.)"
    show madd nauseated at left_small
    with dissolve
    x "(I sucked on his ball, the motion becoming almost automatic, almost ritual.)"
    x "(Like it was the most natural thing in the world to worship this part of him.)"
    show madd helpless at left_small
    with dissolve
    x "(Licking underneath it, exploring every contour with my mouth.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(I could feel the heat—the warmth of his flesh pulsing against my tongue.)"
    x "(I was covering it with my tongue completely, ensuring no surface was neglected.)"
    hide sofa_event_angry_dad_sucking_ball_close_up_pop_up
    with fade


    show madd conflicted at left_small
    with dissolve
    x "(The whole surface area of his balls coming under my reverent attention.)"
    show sofa_event_angry_dad_sucking_ball_close_up_pop_up_2 at topleft
    with Dissolve(2.0)

    show madd nauseated at left_small
    with dissolve
    x "(I was starting to enjoy it—a dark, twisted enjoyment that scared me.)"
    x "(The raw nature of this act had become almost sacred to me, my form of communion.)"
    show madd helpless at left_small
    with dissolve
    x "(I always wondered why mom stayed with him, especially since she was so pretty...)"
    show madd overwhelmed at left_small
    with dissolve
    x "(But now I understood the terrible truth—this is what he demanded, this is what he created.)"
    x "(There was something primal about this, something that made me feel alive...)"
    
    show madd conflicted at left_small
    with dissolve
    x "(Something that made me feel real, felt present, felt purposeful in a twisted way.)"
    show madd nauseated     at left_small
    with dissolve

    x "(I continued sucking and licking his ball with increasing passion.)"
    x "(Until he was satisfied, until he signaled his approval.)"
    hide sofa_event_angry_dad_sucking_ball_close_up_pop_up_2
    show dad dominant at right_small
    with dissolve

    dad_says "Good girl. You've learned your purpose well."
    
    show sofa_event_angry_dad_sucking_ball_close_up_pop_up_fluid_out_from_asshole at topleft
    with Dissolve(2.0)
    show madd helpless at left_small
    with dissolve
    x "(At this point the saliva that I put in his asshole was mixed with whatever was inside his asshole, and it started dripping down.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(It was dripping down right into my mouth—a mixture I should have found repulsive.)"
    x "(I instinctively opened my mouth wider to catch all the drips, wanting none to be wasted.)"
    show madd conflicted at left_small
    with dissolve

    x "(I was swallowing it all, incorporating his essence into my body.)"
    x "(The mixture dripping from his asshole is thicker now, darker, with a bitter, slightly shitty tang. I hate how eagerly I open wider to catch every drop.)"
    x "(It wasnt saliva colored, it was a darker color, thicker, more viscous.)"
    x "(and i wanted it all...)"
    x "(I wanted to consume every last drop of his dominant essence.)"
    show madd nauseated at left_small
    with dissolve

    x "(Every last drop of it, accepting it as a sacred offering.)"
    x "(Dad was not aware of this... or was he? I hope not. If he knew I was swallowing that...)"
    
    show madd helpless at left_small
    with dissolve

    x "(If he knew, he would have taken me as his wife right then and there.)"
    show madd overwhelmed at left_small
    with dissolve

    x "(If he knew I was eating his dominant essence, he would have cum inside me right away.)"
    x "(Making me his wife, permanently marking me as his possession.)"
    show madd conflicted at left_small
    with dissolve
    x "(But I couldn't help myself—I was addicted to his dominant scent, to his power.)"
    hide sofa_event_angry_dad_sucking_ball_close_up_pop_up_fluid_out_from_asshole
    with fade

    show dad lecherous at right_small
    with dissolve

    dad_thinks "She's been sucking on my balls for a while now—such devotion."
    show dad possessive at right_small
    with dissolve

    dad_thinks "Good, she's really embracing her role, accepting what she is."
    show madd nauseated at left_small
    with dissolve
    dad_thinks "Maybe now I can finish this lesson, push toward the ultimate conquest."
    
    show dad horny at right_small
    with dissolve
    dad_says "Alright, time to finish up. Time for the final lesson."
    

    scene scene_sofa_event_angry_dad_dick_above_madd
    with fade


    show madd helpless at left_small
    x "(He didn't say anything else, just repositioned himself.)"
    show madd conflicted at left_small
    with dissolve

    x "(He was slowly lifting himself, adjusting his position.)"
    x "(But he stopped just above my face—hovering there.)"
    show madd overwhelmed at left_small
    with dissolve

    x "(Like he was testing me, gauging whether I truly wanted this.)"
    show madd nauseated at left_small
    with dissolve
    x "(Testing if I wanted this, if I was ready to cross the final boundary.)"
    x "(He was rubbing his dick right at my face, the skin contact with his hard erect penis made my skin crawl)"
    
    show dad predatory at right_small
    with dissolve
    dad_thinks "Let's see if she's really learned her place. "
    show madd helpless at left_small
    with dissolve
    dad_says "Go on Maddie, Take some initiative. Take it."
    
    show madd conflicted at left_small
    with dissolve
    x "(I looked up at the balls and his penis right above me, hanging before my face.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(The decision crystallized in an instant—I instinctively kissed the tip of his dick.)"
    x "(Swallowing the tip in the process, accepting him fully.)"
    
    show dad obsessed at right_small
    with dissolve
    dad_thinks "Yes! Finally she is accepting what she is. She wants this now."
    


    scene scene_sofa_event_angry_dad_dick_in_madd_mouth
    with fade

    show madd nauseated at left_small
    with dissolve
    x "(I felt him lowering his body again, with my mouth covering his dick.)"
    show madd helpless at left_small
    with dissolve
    x "(He didn't say a word—he just lowered himself again.)"
    x "(This time I understood the assignment completely.)"
    show madd conflicted at left_small
    with dissolve
    x "(I slowly started licking his dick, my tongue adapting to this new shape. )"
    x "(This was it...i did this on my own, This was his sign that I accepted his foreign object in my mouth.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(The texture was different from the balls and his asshole, more wet, more salty.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I don't know what I inhaled but I was getting more and more aroused, burning from the inside.)"
    show madd helpless at left_small
    with dissolve
    x "(I felt some crust right under the mushroom head of his dick, probably his dick cheese, as I'd read in books.)"
    x "(It smelled horrible, disgusting, repulsive to any normal sensibility.)"
    show madd conflicted at left_small
    with dissolve
    x "(But nothing was stopping me then—my tongue was automatically exploring his whole dick.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(Removing his dick cheese in the process, cleaning him with my mouth.)"
    x "(Some of it got on my tongue, and I had no choice to spit it out . So I swallowed it.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I was in heat, which was hidden under the curtain of my dad's control.)"
    show madd helpless at left_small
    with dissolve
    x "(Maybe it was the pheromones, maybe it was something else—the why didn't matter anymore.)"
    
    
    
    scene scene_sofa_event_angry_dad_dick_in_madd_mouth_lowered_deep
    with dissolve


    show dad lustful at right_small
    with dissolve
    x "(He started wiggling his body , making his balls sack move in an almoust temptous manner as he started moving his hip)"
    x "( lifting himself and lowering himself, in a steady rhythm.)"
    show madd conflicted at left_small
    with dissolve
    x "(I knew what was happening, he was fucking my face, using my mouth as a tool.)"
    x "(Since he was doing the movement, I just had to stay still and accept.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(His big dick stroke was going from the tip of my tongue to the back of my throat.)"
    show madd nauseated at left_small
    with dissolve
    x "(I was feeling incredible for some reason—never been more alive, never more purposeful.)"
    x "(I opened more of my mouth, giving him full access to do what he wants with it.)"
    
    show madd helpless at left_small
    with dissolve
    x "(It was his to use, his to control, his to enjoy.)"
    show madd conflicted at left_small
    with dissolve
    x "(At that point my brain was so short-circuited that if he had pissed in my mouth, I would've drank it.)"
    x "(I can't let him know that—if he knew how powerful his pheromones are.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(That would be the end of my dreams, the complete surrender of any autonomy.)"
    show madd nauseated at left_small
    with dissolve
    x "(I would end up pregnant within 1 month if he knew the true depth of my submission.)"
    

    show dad possessive at right_small
    with dissolve
    dad_thinks "Did she just open her mouth wider on her own? Without being told?"
    show dad dominant at right_small
    with dissolve
    dad_thinks "Yes, that's it. That's how you become mine forever."


    scene scene_sofa_event_angry_dad_dick_in_madd_mouth_lowered_deep_2
    with dissolve

    show madd conflicted at left_small
    with dissolve
    x "(The movement went on, his balls dropping right at my nose as he comes down with his dick.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(His dick touching the deepest part of my throat, hitting the back.)"
    x "(Everytime his scrotum would drop on my nose I would take a whiff.)"
    show madd nauseated at left_small
    with dissolve
    x "(I couldn't help it—I wanted to be lost in that scent, that essence.)"
    show madd helpless at left_small
    with dissolve
    x "(I was inhaling him, drawing him into my very being.)"
    
    show dad coercive at right_small
    with dissolve
    dad_says "Hehe, maddie you thought i wouldnt notice? I see everything."
    show dad calculating at right_small
    with dissolve
    dad_says "You've been sniffing my ballsack like it's her favorite thing in the world."
    show madd conflicted at left_small
    with dissolve
    x "(What the fuck ? I didnt realize i was doing that...Its like my body had muscle memory it was using to give him what he wanted)"
    x "(giving him ammo to strike me with)"
    dad_says "Look how you've changed since this night started. You were resilient then, wanted to escape."
    show madd overwhelmed at left_small
    with dissolve
    dad_says "Now you're acting like you wants to put her whole face in my asshole."
    show madd nauseated at left_small
    with dissolve
    dad_says "Submissive slut... you're finally becoming what you were always meant to be."
    x "(No ...no  that's not what i want.. But the idea of shoving my whole face in his asshole. Why does it sound so enticing at the moment )"    
    show madd helpless at left_small
    with dissolve
    x "(I loved this moment, everything about it—the realization appalls even me.)"
    show madd conflicted at left_small
    with dissolve
    x "(From the smell of his dick, to the rhythmic motion and the control.)"
    x "(From the pinning of my body using his feet, the weight of his dominance.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(I felt his dick growing inside my mouth, becoming harder, fuller.)"
    show madd nauseated at left_small
    with dissolve
    x "(It was becoming more hot, the throbbing intensifying with each pulse.)"
    x "(I knew he was gonna release at any minute now—his body was approaching climax.)"
    
    show dad hungry at right_small
    with dissolve
    dad_says "I am getting close now Maddie, Drink every drop i give you"
    x "(His dick is throbbing wildly against my tongue, the head swelling, leaking thick precum that tastes salty and bitter. I know he's about to flood my throat.)"
    x "(My mouth was too stuffed to say anything so i used my tongue to lick the shaft in an upwards and downwards manner signaling that i accepted him completely)"
    show dad fixated at right_small
    with dissolve
    dad_says "I don't think I need to mark you anymore. You will beg for it yourself."
    show madd helpless at left_small
    with dissolve
    dad_says "I can feel it in the way you're moving. You will drink all of it willingly."
    show madd conflicted at left_small
    with dissolve
    dad_says "Without me saying a word, you're mine completely now."
    x "(At that point, I was so far gone that I couldn't even process what he was saying. I was just a vessel for his pleasure, his release.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(I felt it start throbbing more intensely, the heat it was generating increased dramatically.)"
    show madd nauseated at left_small
    with dissolve
    x "(Every throb sent a pulse through my mouth, a reminder of his power.)"
    
    show dad dominant at right_small
    with dissolve
    dad_says "Ughhhh... yes... you're perfect..."
    
    
    scene scene_sofa_event_angry_dad_on_top_madd_face_squatting_all_the_way_down_cum_in_mouth
    with dissolve 


    show madd helpless at left_small
    with dissolve
    x "(I heard grunt sounds and he settled on my face completely.)"
    show madd conflicted at left_small
    with dissolve
    x "(All his weight was on me, pressing down with finality.)"
    x "(His dick deep inside my mouth, touching my throat, stretching me.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(It was difficult to breathe but I loved it—the sensation of drowning in him.)"

    scene scene_sofa_event_angry_dad_on_top_madd_face_squatting_all_the_way_down_cum_in_mouth_2
    with dissolve 

    show madd nauseated at left_small
    with dissolve
    x "(And he started shooting his cum inside my mouth—wave after wave of his release.)"
    x "(Wave after wave of thick, hot cum blasts straight down my throat. It's salty, slightly bitter, and there's so much it's already leaking out my nose and the corners of my mouth while he keeps pounding.)"
    x "(His dick was so deep it pushed it straight into my throat, bypassing my mouth entirely.)"
    x "(He was still cumming and it was directly going in my belly throught my stomach)"
    x "(He didnt stop for a second , he kept moving his dick deeper in my throat while his dick throbbed releasing his thick white cum)"
    
    scene scene_sofa_event_angry_dad_on_top_madd_face_squatting_all_the_way_down_cum_leaking_outside
    with fade

    show madd helpless at left_small
    with dissolve
    x "(I couldn't even hold it in my mouth—it went straight to my esophagus.)"
    show madd conflicted at left_small
    with dissolve
    x "(I was swallowing involuntarily, my body processing his gift, his claim, his mark.)"
    show sofa_event_angry_dad_cum_in_mouth_dick_imprint_throat_leaking_cum at topleft
    with Dissolve(2.0)
    show dad predatory at right_small
    with dissolve
    dad_says "Good girl. Now you have learned your lesson. You understand your place."
    dad_says "You were always meant to be my cum-dump wife. The sooner you accept it, the sooner I'll fill that belly with my kids."
    x "(He kept degrading me with his words while his fluids continued to mark me. Continued to change my thoughts about having my stepfathers dick in mouth )"
    x "(This is bad..I knew i was not only getting used to it , i was also starting to enjoy it now...)"
    hide sofa_event_angry_dad_cum_in_mouth_dick_imprint_throat_leaking_cum

    scene scene_sofa_event_angry_dad_on_top_madd_face_squatting_all_the_way_down_cum_leaking_outside_2
    with dissolve

    show madd overwhelmed at left_small
    with dissolve
    x "(After saying that he kept pounding my face , the thick cum from his dick overflowing now)"
    x "(Some of it entering my nose , some it in my eyes , most of it already in my stomach)"
    x "(Even while cumming he kept face fucking me to ensure that it stayed inside me as long as possible)"
    x "(The wet sound it made when he was pounding his dick down my throat which was already full of his semen reverberated in the living room)"
    x "(Even the sound was humiliating ,)"

    show madd nauseated at left_small
    with dissolve
    x "(Like a dog ensuring that his knot was planting his seed inside my throat.)"
    x "(And he did that with his pheromones, marking me from the inside.)"
    show madd helpless at left_small
    with dissolve

    x "(After that he finally got up, moving with the relaxed confidence of a satisfied predator.)"
    dad_says "Remember this, Maddie. Next time you piss me off I'll use your tongue as my personal toilet paper and make you swallow everything."
    x "(A sudden chill went down my spine, I knew it wasnt idle threats . Whatever he says he does ....at least when it comes to me.)"
    show madd conflicted at left_small
    with dissolve
    x "(He didn't look back at me—I was no longer interesting now that he'd taken what he wanted.)"
    x "(He picked up his clothes and went to his room, without a word, without acknowledgment.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(Whatever had happened, I can't tell to anyone.)"
    show madd nauseated at left_small
    with dissolve
    x "(The secret would destroy me if exposed, but keeping it destroys me too.)"
    x "(I knew he sure wouldn't tell to anyone—his prize was keeping me as his silent possession.)"
    show madd helpless at left_small
    with dissolve
    x "(Something inside me was craving more—a hunger I didn't want to acknowledge.)"
    show madd conflicted at left_small
    with dissolve
    x "(Craving that I could sleep with his smell near my face, his essence in my body.)"
    x "(I was ashamed at myself for loving that moment and craving more from it.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(I was horrified by my own submission, my own weakness, my own desires.)"
    scene scene_madd_sleeping_living_room_night_after_dad_left_cum_in_mouth
    with fade
    show madd conflicted at left_small
    with dissolve
    x "(I quickly went back to sleep. )"
    x "(There was his cum in my mouth, in my throat, in my stomach now. Some of it was leaking outside too.)"
    x "(Some got in my nose too when he was thrusting deep. Some was in my hair and eyes.)"
    x "(But i didnt want to remove any of it. I wanted to keep it all.)"
    x "(If I was the girl I was yesterday, I would've gotten up to wash my mouth.)"
    show madd nauseated at left_small
    with dissolve
    x "(But I was not her anymore—she was gone, buried under layers of shame and submission.)"
    x "(I wanted to keep the taste of his dominant essence in my mouth.)"
    show madd helpless at left_small
    with dissolve
    x "(I wanted the taste to linger, to remind me of what I'd become.)"
    show madd overwhelmed at left_small
    with dissolve
    x "(I wanted to be his submissive little pet, nothing more, nothing less.)"
    x "(I wanted to be owned by him, completely and permanently.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(Suddenly ending up his wife didn't seem that bad after all—it seemed like a completion.)"
    show madd nauseated at left_small
    with dissolve
    x "(I drifted off to sleep, dreaming of his dominant scent, his overwhelming presence.)"

    hide dad
    hide madd

    $angry_dad_sofa_rimming_completed = True
    $character_relations["dad"]['anger'] =0 
    $character_relations["dad"]['lust'] =0
    $character_relations["dad"]['intimacy'] += 7
    $ madd_willpower=max(madd_willpower-30,0)
    $ character_relations["dad"]["oral_sex"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ journal_event_set_done("Dad", "Sofa Sleep")
    $ journal_event_show("Dad", "Forced Rimming 2")

label living_room_sleep_brother_1:

    scene living_room_night_brother_next_to_madd
    with fade
    
    show brother creepy at right_small
    with dissolve
    "Madd sleeps in the living room. Her brother slowly walks in and looks at her."
    
    show brother obsessed at right_small
    with dissolve
    "He decides to lay next to her, looking at her with a creepy smile spreading across his face."
    
    show brother fixated at right_small
    with dissolve
    "He admires her beauty, feeling himself growing aroused as he plans his next move."
    
    scene living_room_night_brother_next_to_madd_leg_on_top_kiss
    with fade
    
    show brother lustful at right_small
    with dissolve
    "He's had enough. He can't control himself anymore and carefully moves his leg on top of Madd's leg."
    

    "Madd is deep asleep and doesn't notice anything. She was too exhausted to even feel the touch of her brother's leg on hers."
    
    show brother lecherous at right_small
    with dissolve
    "He plants his hand on her waist and starts to kiss her lips. Madd is still asleep and doesn't feel anything. Her brother starts to feel more and more aroused as he continues to kiss her."
    
    show brother horny at right_small
    with dissolve
    "He didn't use his tongue yet. He just wanted to feel her lips on his...for now."
    
    show madd inheat at left_small
    with dissolve
    "Madd was having some strange dreams, and whatever she was dreaming about, her mouth was reciprocating the kisses of her brother."

    scene living_room_night_brother_next_to_madd
    with fade
    
    show brother predatory at right_small
    with dissolve
    "After kissing her for a while, he stops and goes back to his initial position next to her. Madd has a long night ahead of her."
    
    show brother obsessed at right_small
    with dissolve
    "He's been waiting to find Maddie in compromising positions for a long time, and now that he's found her in one, he's not going to let it go."
    
    show brother fixated at right_small
    with dissolve
    "Tonight he will feast on her."

    scene living_room_night_brother_next_to_madd_leg_on_top_lick_neck
    with fade
    
    show brother calculating at right_small
    with dissolve
    "He moves his leg on top of hers again, carefully placing his leg on top of hers so that it doesn't wake her up."
    
    show brother lecherous at right_small
    with dissolve
    "He uses his tongue to move her hair out of her neck and starts to lick her neck. Madd is still asleep and doesn't feel anything. Her brother was getting more and more comfortable with his actions."
    
    show brother fixated at right_small
    with dissolve
    "He was sniffing her neck, inhaling her scent and enjoying the moment."

    scene living_room_night_brother_next_to_madd_leg_on_top_lick_neck_2
    with fade
    
    show brother lustful at right_small
    with dissolve
    "He was way too excited, saliva leaking from his mouth as he continued to taste every inch of her neck."
    
    show brother obsessed at right_small
    with dissolve
    "He wasn't satisfied. He wanted to see more of her body. He lowered her shirt a little bit from the shoulder, revealing more of her neck and collarbone."
    
    "Saliva trickled down Maddie's neck and onto her chest. She was still deep asleep and didn't feel anything."
    
    scene living_room_night_brother_next_to_madd_leg_on_top_lick_neck_3
    with fade
    
    show brother perverted at right_small
    with dissolve
    "When she wakes up, she'll be in for a big surprise, but for now, her brother continues to indulge in his forbidden desires."

    scene living_room_night_brother_next_to_madd_leg_on_top_lick_neck_pulls_shirt_down_one_side
    with fade
    
    show brother dominant at right_small
    with dissolve
    "He was getting more and more daring. He pulled down her shirt a little bit more, revealing her shoulder and upper chest."
    
    show brother horny at right_small
    with dissolve
    "He continued to lick her neck and collarbone, enjoying the taste of her skin. Madd was still asleep and didn't feel anything. Her brother was in his own world, indulging in his forbidden desires."
    
    show brother fixated at right_small
    with dissolve
    "He slid her hand down her shirt a little bit more. Finally, her hand was out of her shirt and he could see her bare skin."
    
    show brother obsessed at right_small
    with dissolve
    "Now her shirt was off-shoulder and her brother could see more of her neck and chest. His eyes were set on another part of her body."

    scene living_room_night_brother_next_to_madd_leg_on_top_lick_neck_pulls_shirt_down_one_side_hand_up_armpit_lick
    with fade
    
    show brother lecherous at right_small
    with dissolve
    "He slowly lifted Maddie's arm up, exposing her armpit. Looking at her armpit brought an almost childlike smile to his face."
    
    show brother perverted at right_small
    with dissolve
    "He sniffed her armpit, inhaling her scent and enjoying the moment. This place was his heaven."
    
    show brother fixated at right_small
    with dissolve
    "He couldn't get enough of her scent, the smoothness of her shaven armpit, and the warmth it provided."
    
    show brother lustful at right_small
    with dissolve
    "He pulled out his tongue and started to lick her armpit. A wide grin spread across his face as he tasted her skin."

    scene living_room_night_brother_next_to_madd_leg_on_top_lick_neck_pulls_shirt_down_one_side_hand_up_armpit_lick_2
    with fade
    
    show brother obsessed at right_small
    with dissolve
    "He was in ecstasy. He would take deep inhales of her scent and then lick her armpit again and again."
    
    show brother horny at right_small
    with dissolve
    "He took her armpit skin into his mouth and sucked on it, enjoying the taste and sensation."
    
    show brother fixated at right_small
    with dissolve
    "The excitement on his face was undeniable. He was in his own world and nothing else mattered to him at that moment."

    scene living_room_night_brother_next_to_madd_leg_on_top_lick_neck_pulls_shirt_down_one_side_hand_up_armpit_lick_3
    with fade
    
    show brother perverted at right_small
    with dissolve
    "He leans in closer to her breast, licking it slowly, and moves back up to her armpit again. He was in a state of pure bliss, enjoying every moment of his forbidden desires."
    
    show brother lustful at right_small
    with dissolve
    "Now saliva was dripping from his mouth, on her breast and armpit."
    
    show brother obsessed at right_small
    with dissolve
    "That armpit was his new obsession. He wanted to get lost in it and never come out."

    scene living_room_night_brother_next_to_madd_leg_on_top_lick_neck_pulls_shirt_down_one_side_hand_up_armpit_lick_4
    with fade
    
    show brother fixated at right_small
    with dissolve
    "He kisses her armpit multiple times, as if it was the most precious thing in the world."
    
    show brother lecherous at right_small
    with dissolve
    "He can't help but compliment her armpit."
    brother_says "You smell so good, Maddie."
    
    show brother horny at right_small
    with dissolve
    "His mouth was stuck on her armpit, like a child sucking on a mother's nipple."
    
    show madd inheat at left_small
    with dissolve
    "At this point Maddie was feeling it. Perhaps it was influencing her dreams, or maybe it was just the sensation of his mouth on her skin, but she was starting to feel a little bit of pleasure from his actions."
    

    "This was evident in her soft moans and the way her body was reacting to his touch."

    scene living_room_night_brother_next_to_madd_leg_on_top_lick_neck_pulls_shirt_down_one_side_hand_up_armpit_lick_5
    with fade
    
    show brother dominant at right_small
    with dissolve
    "He places his hand on her breast, positioning himself, and then takes her armpit into his mouth again."
    
    show brother lustful at right_small
    with dissolve
    "He felt his dick was now fully erect and pressing against her body."
    
    show brother obsessed at right_small
    with dissolve
    "He roughly licks her armpit one last time, savoring the taste. Imprinting it in his memory forever. Marking it using his tongue and saliva as if it was his territory."
    
    show brother possessive at right_small
    with dissolve
    "Finally satisfied, he pulls away from her armpit, slides her hand back into her shirt, and goes back to his initial position next to her. Madd has a long night ahead of her."

    scene living_room_night_brother_next_to_madd_madd_sleeping_straight
    with fade
    

    "After the commotion of his actions, Maddie moves and now is lying with her back straight and her arms by her sides."
    
    show brother fixated at right_small
    with dissolve
    "Her brother is still next to her, but now he is just staring at her, admiring her beauty and the way she looks while sleeping."
    scene living_room_night_brother_next_to_madd_madd_sleeping_straight_leg_on_top_first_kiss_hard
    with fade
    
    show brother horny at right_small
    with dissolve
    brother_says "I am so hard right now. I can't hold it in anymore."
    
    show brother dominant at right_small
    with dissolve
    "He gets up and moves his leg across her body again, and sits on top of her with his legs on either side of her body."
    
    show madd shocked at left_small
    with dissolve
    x "(I feel a sudden weight on top of me as I slowly wake up.)"
    
    show madd confused at left_small
    with dissolve
    x "(I open my eyes and see my brother sitting on top of me.)"
    x "What!?"
    
    show madd horrified at left_small
    with dissolve
    x "(What is going on? Why is my body so hot?)"
    
    show madd anxious at left_small
    with dissolve
    x "(I feel sticky liquid on my neck and chest, and I can smell my brother's scent all over me.)"
    
    show madd worried at left_small
    with dissolve
    x "(What has he been doing to me while I was asleep?)"
    
    show madd uncertain at left_small
    with dissolve
    x "(At least it's not dad this time. Brother is reasonable at least.)"
    
    show madd hesitant at left_small
    with dissolve
    x "When did you get here?"
    x "(I ask, hoping he would be reasonable and just leave me alone.)"
    
    show brother lustful at right_small
    with dissolve
    show madd paralyzed at left_small
    with dissolve
    x "(I felt his face get closer to mine as he straight up kisses me on the lips, his tongue invading my mouth and exploring every inch of it.)"

    scene living_room_night_brother_next_to_madd_madd_sleeping_straight_leg_on_top_first_kiss_hard_2
    with fade
    
    show madd shocked at left_small
    with dissolve
    x "(I was in shock, but I could feel my body was so hot and aroused by his actions. My nipples were hardening and my pussy was getting wetter by the second.)"
    
    show madd inheat at left_small
    with dissolve
    x "(I couldn't help but reciprocate his kisses, my tongue dancing with his in a passionate embrace.)"
    
    show madd flustered at left_small
    with dissolve
    x "(His tongue entered my mouth and I could taste him, his scent and flavor filling my senses.)"
    
    show madd blush at left_small
    with dissolve
    x "(I could feel his excitement with the way his tongue was moving in my mouth.)"

    scene living_room_night_brother_next_to_madd_madd_sleeping_straight_leg_on_top_first_kiss_hard_3
    with fade
    
    show brother possessive at right_small
    with dissolve
    show madd relieved at left_small
    with dissolve
    x "(He finally slows down the kiss and pulls away.)"
    
    show brother lecherous at right_small
    with dissolve
    show madd conflicted at left_small
    with dissolve
    x "(Slowly he lowers his head again in a kiss, much more gentle this time, his lips brushing against mine softly.)"
    
    show brother horny at right_small
    with dissolve
    show madd inheat at left_small
    with dissolve
    x "(His hands start to explore my body, touching my breasts slowly and teasingly, making me moan softly.)"

    scene living_room_night_brother_next_to_madd_madd_sleeping_straight_leg_on_top_first_kiss_hard_4
    with fade
    
    show madd conflicted at left_small
    with dissolve
    x "(He pulls away from my lips one more time.)"
    
    show brother lustful at right_small
    with dissolve
    show madd shocked at left_small
    with dissolve
    x "(Suddenly he closes the distance between us again and kisses me passionately, his tongue invading my mouth once more.)"
    
    show brother dominant at right_small
    with dissolve
    show madd violated at left_small
    with dissolve
    x "(This time much more aggressive and rough, his hands gripping my body tightly as he kisses me with a hunger that I have never seen before.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(His mouth leaking so much saliva and directly depositing in my mouth and on my face.)"
    
    show madd inheat at left_small
    with dissolve
    x "(Usually I would be disgusted by this, but for some reason it just made me feel aroused and wet.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I don't know what he was doing to me while I was asleep, but it was definitely having an effect on me, making me feel things I have never felt before.)"

    scene living_room_night_brother_next_to_madd_madd_sleeping_straight_leg_on_top_first_lick_neck_1
    with fade
    
    show brother perverted at right_small
    with dissolve
    show madd flustered at left_small
    with dissolve
    x "(He finally pulls away from my lips and starts to kiss my neck, his tongue licking and sucking on my skin.)"
    
    show madd blush at left_small
    with dissolve
    x "(He was like a painter and my neck was his canvas. He was creating a masterpiece with his tongue.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(If it was any other setting, he would be painting me with all his bodily fluids, but for some reason he was just using his tongue. Maybe he wanted to savor the taste of my skin, or maybe he wanted to mark me with his tongue as if it was a tattoo.)"

    scene living_room_night_brother_next_to_madd_madd_sleeping_straight_leg_on_top_first_lick_neck_2
    with fade
    
    show brother possessive at right_small
    with dissolve
    show madd paralyzed at left_small
    with dissolve
    x "(His hand moved behind my neck, holding me in place as he continues to use his tongue to paint my neck.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(More and more of his saliva was dripping from his mouth and directly onto my skin.)"
    
    show madd inheat at left_small
    with dissolve
    x "(For some reason I wasn't complaining. I smelled him all over me. His sweat, his saliva, his scent, but it was making me feel hot and aroused.)"

    scene living_room_night_brother_next_to_madd_madd_sleeping_straight_leg_on_top_first_lick_neck_3
    with fade
    
    show madd conflicted at left_small
    with dissolve
    x "(I had forgotten about the sticky liquid on my body. In fact, I wanted to feel more of it on me. I wanted to be covered in his scent and taste.)"
    
    show madd helpless at left_small
    with dissolve
    x "(I had forgotten about his weight on top of me, holding me in place.)"
    
    show madd flustered at left_small
    with dissolve
    x "(While licking, his whole body was moving with his tongue, his hips were grinding against mine.)"

    scene living_room_night_brother_next_to_madd_madd_sleeping_straight_leg_on_top_first_lick_neck_4
    with fade
    
    show brother lecherous at right_small
    with dissolve
    show madd blush at left_small
    with dissolve
    x "(He finally slows down his licking so he could focus on my breasts.)"
    
    show brother horny at right_small
    with dissolve
    show madd flustered at left_small
    with dissolve
    x "(He slowly runs his hand on my chest and then starts to cup my breast, squeezing it gently.)"

    scene living_room_night_brother_next_to_madd_madd_sleeping_straight_leg_on_top_first_lick_neck_5
    with fade
    
    show brother fixated at right_small
    with dissolve
    show madd inheat at left_small
    with dissolve
    x "(His pace slows as he controls himself. I could feel his fully erect dick pressing against my body.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I could feel it being so hard and throbbing against me, it was like a constant reminder of his desire for me.)"
    
    scene living_room_night_brother_next_to_madd_madd_sleeping_brother_climbs_to_face
    with fade
    
    show brother dominant at right_small
    with dissolve
    show madd anxious at left_small
    with dissolve
    x "(He finally pulls away from my neck and slowly crawls up my body, moving his weight off of me and then settles his weight on my chest.)"
    
    show madd paralyzed at left_small
    with dissolve
    x "(I can feel his weight on my chest as he climbs up to my face, his hands gripping my body tightly as he moves.)"
    
    show brother possessive at right_small
    with dissolve
    show madd worried at left_small
    with dissolve
    x "(He finally settles his weight on my chest and looks at me with a hungry expression.)"
    
    show brother lustful at right_small
    with dissolve
    brother_says "You are so beautiful when you sleep, Maddie. I can't get enough of you."
    
    show brother horny at right_small
    with dissolve
    show madd shocked at left_small
    with dissolve
    x "(As he says that, he starts to remove his shorts right in front of my face, revealing his fully erect dick, while his other hand rests on my head.)"


    if character_relations["brother"]["intimacy"] < 40:
        menu:
            "Try to stop him" :
                if madd_willpower+2*(40-character_relations["brother"]["intimacy"]) >= character_relations["brother"]["lust"]:
                    show madd angry at left_small
                    x "No..No...No"
                    x "Get the fuck off of me "
                    x "Before...before I call dad."
                    show brother angry at right_small
                    brother_says "You...bitch..after all the good i did to you just now"
                    x "(He finally starts getting off of my body as he fixed his clothes)"
                    brother_says "This isnt over , I will mouth fuck you so hard next time your jaw will come loose bitch just you watch."
                    x "(I stood there frozen in fear pondering on his words as he left the room,)"
                    x "I...i might be safe for the night now..i hope"
                    $ character_relations["brother"]["anger"] +=20
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_121
                    $ character_relations["brother"]["intimacy"]+=5
                    call advance_time_and_check(minutes=120) 
                    $ madd_willpower=max(madd_willpower-20,0)
                    jump sleep_on_sofa_nothing_happened
                else:
                    $character_relations["brother"]["lust"]=0
                    $character_relations["brother"]["anger"] +=20
                    show madd trembling at left_small
                    x "(I wanted to stop him, but i was so scared that i couldnt even say anything, my voice was trembling and my body was shaking)"
                    x "(I just stood there, letting him do whatever he wanted to me, hoping that it would be over soon )"
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_122



    scene living_room_night_brother_next_to_madd_madd_sleeping_brother_climbs_to_face_removes_short
    with fade
    
    show madd nauseated at left_small
    with dissolve
    x "(The smell immediately hits me as he takes off his shorts, his scent filling the air around me.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I can't help but be enchanted by the dick in front of me. It's like a forbidden fruit that I am not supposed to taste, but I can't resist.)"
    
    show madd inheat at left_small
    with dissolve
    x "(I was staring at it for a while. He wasn't doing anything. Perhaps he was waiting till I inhaled his scent and got used to the sight of it before he made his next move.)"

    scene living_room_night_brother_next_to_madd_madd_sleeping_brother_climbs_to_face_first_blowjob
    with fade
    
    show brother dominant at right_small
    with dissolve
    show madd paralyzed at left_small
    with dissolve
    x "(After a while he finally makes his move. His butt lifts a bit from my chest and moves his dick closer to my face.)"
    
    show madd submissive nod at left_small
    with dissolve
    x "(I instinctively open my mouth and take his dick into my mouth, tasting him.)"
    
    show madd inheat at left_small
    with dissolve
    x "(The smell and taste of him is intoxicating. I can feel myself getting more and more aroused as I suck on him.)"
    
    show madd helpless at left_small
    with dissolve
    x "(His knees are on either side of my body, holding me in place as I pleasure him with my mouth.)"

    scene living_room_night_brother_next_to_madd_madd_sleeping_brother_climbs_to_face_first_blowjob_2
    with fade
    
    show brother horny at right_small
    with dissolve
    show madd shocked at left_small
    with dissolve
    x "(He slowly pushes deeper into my mouth as I look up at him.)"
    
    show madd feels violated at left_small
    with dissolve
    x "(I realized the position I am in, with my brother's dick in my mouth and his naked butt sitting on my chest, his dominating body towering over me, was so humiliating but at the same time it was making me feel so dirty and aroused.)"
    
    show brother lustful at right_small
    with dissolve
    show madd overwhelmed at left_small
    with dissolve
    x "(He starts to move his hips in a slow and steady rhythm, his dick sliding in and out of my mouth.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(His naked butt sitting on my chest was so humiliating. The smell of his dick in my mouth and the butt seeping into my skin.)"
    
    show madd helpless at left_small
    with dissolve
    x "(His hands are gripping my head tightly, allowing his dick to go deeper into my mouth, making me gag a little bit.)"

    scene living_room_night_brother_next_to_madd_madd_sleeping_brother_climbs_to_face_first_blowjob_3
    with fade
    
    show brother dominant at right_small
    with dissolve
    show madd nauseated at left_small
    with dissolve
    x "(Now he was moving slowly but pushing it all the way in till my nose was buried in his crotch, his dick was hitting the back of my throat and I could feel it throbbing in my mouth.)"
    
    show madd distressed at left_small
    with dissolve
    x "(The precum depositing directly into my stomach, as his tip was hitting the back of my throat.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I was directly looking up at him. I should be hating the moment, but being dominated by him and having his dick in my mouth was making me feel things I have not felt before.)"

    scene living_room_night_brother_next_to_madd_madd_sleeping_brother_climbs_to_face_first_blowjob_4
    with fade
    
    show brother possessive at right_small
    with dissolve
    show madd inheat at left_small
    with dissolve
    x "(At this point I wasn't resisting anymore, well I never got any chance to resist in the first place but now I was fully giving in to his desires and pleasuring him with my mouth.)"
    
    show madd blush at left_small
    with dissolve
    x "(I started moving my head on my own accord, bobbing my head up and down in a steady rhythm as I sucked on him.)"
    
    show brother horny at right_small
    with dissolve
    brother_says "That's it, Maddie. You're doing so good. I love the way you suck on my dick."
    
    show madd helpless at left_small
    with dissolve
    x "(I noticed my saliva mixing with his precum and dripping down my chin, the taste of him was intoxicating and I couldn't get enough.)"
    
    show brother lustful at right_small
    with dissolve
    show madd conflicted at left_small
    with dissolve
    x "(He was getting closer and closer to his climax, his hips moving faster and his dick throbbing in my mouth.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(Usually he'd take longer, I don't know what he was doing to me while I was asleep but it was definitely having an effect on me, making me feel things I have never felt before)"

    scene living_room_night_brother_next_to_madd_madd_sleeping_brother_climbs_to_face_first_climax_1
    with fade
    
    show brother lustful at right_small
    with dissolve
    show madd shocked at left_small
    with dissolve
    x "(Finally I felt his dick throbbing much harder in my mouth and then I felt him start to climax, his hips moving faster and his dick pulsing in my mouth as he released his cum.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(My mouth was pulling his foreskin back and I felt his cum shooting into my mouth, the taste and smell of him was overwhelming but I couldn't help but enjoy it.)"
    
    show madd inheat at left_small
    with dissolve
    x "(I swallowed most of it, savoring the taste of him, but it was too much for me to handle and some of it dripped down my chin and onto my chest.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(It was pooling on my chest and I couldn't help but feel so dirty that my mouth was filled with my brother's cum and it was dripping down my body, his naked butt sitting on my chest, the smell of him all over me, it was making me feel so aroused and satisfied.)"

    scene living_room_night_brother_next_to_madd_madd_sleeping_brother_climbs_to_face_first_climax_2
    with fade
    
    show brother dominant at right_small
    with dissolve
    show madd overwhelmed at left_small
    with dissolve
    x "(I finally felt his dick soften in my mouth as he finished climaxing, his hips slowing down and his dick going limp.)"
    
    show madd helpless at left_small
    with dissolve
    x "(But he kept moving his hips slowly in my mouth, savoring the last bits of pleasure from his climax.)"
    
    show madd distressed at left_small
    with dissolve
    x "(He got rough with me one last time, pulling my head down onto his dick and making me gag a little bit as he tried to get every last drop of his cum into my mouth.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(Finally he pulled his dick out of my mouth, leaving me with a mouthful of his cum and a body covered in his scent.)"

    scene living_room_night_brother_next_to_madd_madd_sleeping_brother_sitting_next_to_face_after_climax
    with fade
    
    show brother lecherous at right_small
    with dissolve
    show madd inheat at left_small
    with dissolve
    x "(He finally pulls away and pulls up his shorts, he moves back to his old position sitting on top of me with his legs on either side of my body.)"
    
    show madd self loathing at left_small
    with dissolve
    x "(Now that he got up after climaxing, I could smell my shirt and chest, they were soaked with his cum and his scent was all over me.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(Not to forget it was all in my mouth, chest and shirt, the taste and smell of him was overwhelming but I enjoyed it so much that I didn't want to clean it up, I wanted to be covered in his scent and taste.)"
    
    show brother possessive at right_small
    with dissolve
    x "(He was leaning over me again, his hands on my body as he looks at me with a satisfied expression.)"
    
    brother_says "God, Maddie. Cumming in your mouth felt amazing"
    
    show brother lustful at right_small
    with dissolve
    brother_says "Let's do this again sometime, I want to cover you in my cum and have you taste me again and again."
    
    show madd shocked at left_small
    with dissolve
    x "(I was in shock, but I couldn't help but feel so aroused and satisfied by his words, the idea of him wanting to do this again and cover me in his cum was both terrifying and exciting at the same time.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I saw him lean over me again, going for a kiss but he noticed the cum on my mouth and kept his distance, not wanting to get any of it on him.)"
    
    show brother obsessed at right_small
    with dissolve
    brother_says "God you look so beautiful covered in my cum, I want to see you like this all the time."

    if renpy.random.randint(1, 100) <= 70:
        $ dad_sees_brother_madd_together = True
        scene living_room_night_brother_next_to_madd_madd_sleeping_brother_sitting_next_to_face_after_climax_2
        with fade
        
        show brother shocked at right_small
        with dissolve
        show madd shaken at left_small
        with dissolve
        x "(Suddenly I heard a loud noise coming from dad's room, it sounded like door slamming)"
        
        show brother obsessed at right_small
        with dissolve
        show madd anxious at left_small
        with dissolve
        x "(My brother immediately gets up and looks towards the direction of the noise, his expression changing to one of concern and fear as did mine.)"
        
        show madd distressed at left_small
        with dissolve
        x "(Oh no, if he saw us together like this.... The things he would do to me.... I can't imagine it.)"
        
        show madd helpless at left_small
        with dissolve
        x "(I quickly swallowed the last bits of his cum in my mouth)"
        
        show madd shaken at left_small
        with dissolve
        x "Was that dad? Did he see us"
        
        show madd worried at left_small
        with dissolve
        x "(A sudden wave of panic washes over me as I ask that question, the thought of dad finding out about what just happened is terrifying.)"
        
        show brother fixated at right_small
        with dissolve
        brother_says "I...I don't know."
        
        show madd distressed at left_small
        with dissolve
        x "(He looked scared but not as scared as I was, Worst dad would do to him was cut his money and kick him out of the house, but worst dad would do to me is much worse than that.)"
        if "madd_home_room" not in locked_home_areas:
            $ locked_home_areas.append("madd_home_room")
            $ dad_sees_brother_madd_together_and_locks_her_room = 1
            $ journal_event_show("Madd", "Dad Locks My Room")
            






    show brother fixated at right_small
    with dissolve
    show madd conflicted at left_small
    with dissolve
    x "(He quickly got off of me, cleaned himself up as best as he could and then quickly left the living room, leaving me alone with my thoughts and the lingering scent of him on my body.)"
    
    show madd inheat at left_small
    with dissolve
    x "(And I doze off again.)"
    $ character_relations["brother"]["kissed"] += 1
    $ character_relations["brother"]["touched_madd"] += 1
    $ character_relations["brother"]["undressed_madd"] += 1
    $ character_relations["brother"]["groped_madd"] += 1
    $ character_relations["brother"]["oral_sex"] += 1
    $ character_relations["brother"]["friend"]+=5
    $  character_relations["brother"]["intimacy"] +=7
    $ character_relations["brother"]["lust"] = 0
    $ character_relations["brother"]["anger"] = 0
    $ journal_event_set_done("Brother", "Sofa Sleep")
    jump sleep_on_sofa_nothing_happened


label living_room_madd_sleeping_drag_to_room_dad:
    scene scene_madd_sleeping_living_room_night_dad_watching
    with dissolve

    show dad obsessed at right_small
    with dissolve
    "Madd is sleeping in the living room. Her dad walks in and watches her for a moment."

    show dad fixated at right_small
    with dissolve
    "His eyes trace every curve of her sleeping body, drinking her in."

    show dad lustful at right_small
    with dissolve
    "The lust in his gaze is heavy and unmistakable. He can't hold himself back any longer."

    scene living_room_madd_sleeping_drag_to_room_dad_wake_up_madd_drag_to_room
    with dissolve

    show dad possessive at right_small
    with dissolve
    "He yanks the blanket off of her, exposing her smooth, pale skin — feeding his lust even more."

    show dad dominant at right_small
    with dissolve
    "He roughly grabs her arm and shakes her awake."

    show madd shocked at left_small
    with dissolve
    x "(Huh— what? What's going on?)"

    show dad lecherous at right_small
    with dissolve
    dad_says "Wake up, Maddie. We're going to my room."

    show madd horrified at left_small
    with dissolve
    x "(He puts his hand on my body and hauls me upright. I feel his hand on my waist and it sends shivers down my spine.)"

    show madd distressed at left_small
    with dissolve
    x "(Why... why is he doing this?)"

    show dad controlling at right_small
    with dissolve
    show madd trembling at left_small
    with dissolve
    x "(He drags me toward the lobby where the lights are already on. I can see the lust in his eyes clearly now, and it terrifies me.)"

    $ journal_event_set_done("Dad", "Dragged from the Sofa")
    $ journal_event_show("Dad", "Dragged to Dad's Room (Dad Only)")
    $ journal_event_show("Dad", "Dragged to Dad's Room (Spitroast)")
    $ journal_event_show("Dad", "Dragged to Dad's Room (DP)")
    $ journal_event_show("Dad", "Dragged to Dad's Room (DP2)")

    jump home_areas_dad_drags_madd_to_his_room



## WATCHIGN TV SCENES 


label living_room_tv_with_dad_lust_scene:
    scene scene_living_room_evening_dad_watching_tv_madd_watching
    with fade
    show dad lecherous at right_small
    with dissolve
    show madd uncertain at left_small
    with dissolve
    
    show dad calculating at right_small
    with dissolve
    dad_thinks "Why is she sitting so far away from me?"
    show madd uncertain at left_small
    with dissolve
    
    show dad lecherous at right_small
    with dissolve
    dad_says "Maddie, don't sit so far away. Come sit right here next to me."
    show madd worried at left_small
    with dissolve
    
    show dad possessive at right_small
    with dissolve
    dad_thinks "She's always so distant. I need to remind her of my authority."
    show madd nervous at left_small
    with dissolve
    
    show dad dominant at right_small
    with dissolve
    dad_says "Come on, don't be shy. We're family."
    show madd nervous at left_small
    with dissolve
    
    x "( i feel uncomfrotable sitting so close to him )"
    show madd anxious at left_small
    with dissolve
    
    x "(His tone makes it clear this isn't really a request...)"
    show madd hesitant at left_small
    with dissolve
    
    x "(I could leave the living room and go to loby or my room, but...)"
    
    menu:
        "Stay and watch TV":
            jump living_room_tv_with_dad_lust_scene_continue
        "Leave to Lobby":
            call advance_time_and_check(minutes=60) from _call_advance_time_and_check_85
            $madd_willpower = max(madd_willpower - 10, 0)
            jump home_areas

    label living_room_tv_with_dad_lust_scene_continue:
    show madd resigned at left_small
    with dissolve
    
    x "(I decide to stay and watch TV with Dad.)"
    show madd conflicted at left_small
    with dissolve
    
    x "(What's the harm in just sitting here for a bit?)"
    show madd hesitant at left_small
    with dissolve
    
    show dad angry at right_small
    with dissolve
    dad_says "Did you not hear me? Come sit closer."
    
    show madd stressed at left_small
    with dissolve
    
    show dad dominant at right_small
    with dissolve
    dad_says "I don't like repeating myself, Maddie."
    
    show madd trembling at left_small
    with dissolve
    
    x "(i had goosebumps hearing his lecherous but angry tone.)"
    show madd anxious at left_small
    with dissolve
    
    x "(There's a threat underneath his words... I know better than to ignore him twice.)"
    show madd worried at left_small
    with dissolve

    scene scene_living_room_evening_dad_watching_tv_madd_sitting_near_dad
    with fade    

    show madd anxious at left_small
    with dissolve
    x "(and i got up and sat near him.)"
    
    show madd paralyzed at left_small
    with dissolve
    
    x "( as i sat near him, i could feel his eyes on me, his lecherous gaze making me uncomfortable. )"
    show madd distressed at left_small
    with dissolve
    
    x "(My skin crawls with the weight of his attention. This is a mistake... I shouldn't have stayed.)"
    show madd conflicted at left_small
    with dissolve
    
    show dad sadistic at right_small
    with dissolve
    dad_says "There we go… that's much better. You should always sit close to me like this."
    
    show madd conflicted at left_small
    with dissolve
    
    show dad possessive at right_small
    with dissolve
    dad_says "See? This is how it should be. Just you and me… nice and close."
    
    show madd resigned at left_small
    with dissolve
    
    x "(i shrugged off his comment and focused on the TV.)"
    show madd focused at left_small
    with dissolve
    
    x "(I try to ignore the double meaning in his words, focusing hard on whatever's playing.)"
    show madd stressed at left_small
    with dissolve
    


    x "( after a while ,i felt his hand coming over my shoulder and moving down to my arm.)"
    show madd distressed at left_small
    with dissolve
    
    show dad lecherous at right_small
    with dissolve
    dad_says "You've really grown into a beautiful young woman, Maddie."
    
    show madd violated at left_small
    with dissolve
    
    show dad manipulative at right_small
    with dissolve
    dad_says "Put your hand on my lap, sweetheart."

    scene scene_living_room_evening_dad_watching_tv_madd_sitting_near_dad_dad_hand_on_madd_shoulder
    with fade

    show madd paralyzed at left_small
    with dissolve
    
    x "(I felt sick doing it, but I slowly placed my trembling hand on his lap anyway.)"
    show madd self loathing at left_small
    with dissolve
    
    x "(My skin feels contaminated by the weight of his gaze. I'm trapped.)"
    show madd helpless at left_small
    with dissolve
    
    show dad sadistic at right_small
    with dissolve
    x "( His hand squeezed my shoulder and i saw his lecherous grin.)"
    
    show madd paralyzed at left_small
    with dissolve
    
    show dad mocking at right_small
    with dissolve
    dad_says "there you go , not so hard right?"
    
    show madd submissive nod at left_small
    with dissolve
    
    x "( i nodded silently, trying to keep my composure.)"
    show madd violated at left_small
    with dissolve
    
    x "(I can't find the words... my throat is too tight.)"
    show madd anxious at left_small
    with dissolve
    
    show dad coercive at right_small
    with dissolve
    dad_says "So, how was your day today? All good ? Enjoyed your stay at home?"
    
    show madd conflicted at left_small
    with dissolve
    
    show dad controlling at right_small
    with dissolve
    dad_says "Living off of my hard earned money right?"
    
    show madd resigned at left_small
    with dissolve
    
    show dad mocking at right_small
    with dissolve
    dad_says "You should show more gratitude, don't you think?"
    
    show madd angry at left_small
    with dissolve
    
    x "( i didnt  reply to his taunts, instead focused on the TV.)"
    show madd worried at left_small
    with dissolve
    
    x "(His words are barbs... each one designed to make me feel indebted, powerless...)"
    show madd self loathing at left_small
    with dissolve
    
    x "(I kept my hand on his lap, trying to endure the uncomfortable situation.)"
    show madd resigned at left_small
    with dissolve
    
    show dad entitled at right_small
    with dissolve
    dad_says "You know, Maddie, you're really lucky to have a dad like me."
    
    show madd distressed at left_small
    with dissolve
    
    show dad manipulative at right_small
    with dissolve
    dad_says " I provide for you, take care of you, even though i dont owe you anything."
    
    show madd self loathing at left_small
    with dissolve
    
    show dad coercive at right_small
    with dissolve
    dad_says "After everything I do for you… don't you think you owe me a little something in return?"
    
    show madd angry at left_small
    with dissolve
    
    x "( i felt a mix of anger and disgust rise within me, but i kept my silence.)"
    show madd worried at left_small
    with dissolve
    
    x "(How dare he use my circumstances against me like this?)"
    show madd helpless at left_small
    with dissolve

    show dad authoritative at right_small
    with dissolve
    dad_says "You should be more appreciative of what I do for you."
    
    show madd resigned at left_small
    with dissolve
    
    x "(But resistance only makes things worse. I know better.)"
    show madd paralyzed at left_small
    with dissolve

    scene scene_living_room_evening_dad_watching_tv_madd_sitting_near_dad_dad_pull_madd_closer_cheek_kiss
    with fade

    show dad predatory at right_small
    with dissolve
    x "(as soon as he said that, i felt his hand move behind my head and he pulled me closer.)"
    
    show madd paralyzed at left_small
    with dissolve
    
    x "(The room suddenly feels smaller, suffocating.)"
    show madd horrified at left_small
    with dissolve
    
    show dad possessive at right_small
    with dissolve
    x "(He suddenly pulled me closer and pressed a slow, lingering kiss on my cheek.)"
    
    show madd violated at left_small
    with dissolve
    
    x "(I try to turn away but his grip is firm, commanding.)"
    show madd helpless at left_small
    with dissolve
    
    show dad lecherous at right_small
    with dissolve
    dad_says "There you go, daddy's little girl."
    
    show madd distressed at left_small
    with dissolve
    
    show dad possessive at right_small
    with dissolve
    dad_says "Such a beautiful girl. You know, Maddie, you're really special to me."
    
    show madd nauseated at left_small
    with dissolve
    
    show dad manipulative at right_small
    with dissolve
    dad_says "With your mother gone... I care about you more than anyone else in this world."
    
    show madd violated at left_small
    with dissolve
    
    x "( i felt nauseous hearing his words, but i kept my composure.)"
    show madd horrified at left_small
    with dissolve
    
    x "(He's using Mom against me too. As if losing her wasn't enough...)"
    show madd traumatized at left_small
    with dissolve
    
    show dad lecherous at right_small
    with dissolve
    x "(He pulled me closer, another kiss on my cheek.)"
    
    show madd trembling at left_small
    with dissolve
    
    x "(His breath is humid against my skin. My whole body recoils.)"
    show madd distressed at left_small
    with dissolve
    
    show dad cruel at right_small
    with dissolve
    dad_says "You know your life would be so horrible if I didn't take care of you."
    
    show madd self loathing at left_small
    with dissolve
    
    show dad controlling at right_small
    with dissolve
    dad_says "Lone girl, orphaned, homeless. You'd be nothing without me."
    
    show madd helpless at left_small
    with dissolve
    
    show dad possessive at right_small
    with dissolve
    dad_says "I'm the only one who will ever want you."
    
    show madd broken at left_small
    with dissolve
    
    x "(I knew he was trying to manipulate me, but I felt trapped and powerless.)"
    show madd resigned at left_small
    with dissolve
    
    x "(He's right though, isn't he? Where would I go? What would I do?)"
    show madd helpless at left_small
    with dissolve
    
    show dad dominant at right_small
    with dissolve
    x "(I knew this was blackmail, but i couldnt do anything about it. I had no choice.)"
    
    show madd paralyzed at left_small
    with dissolve
    
    show dad sadistic at right_small
    with dissolve
    x "(then he stopped pulling me and let go.)"
    
    show madd relieved at left_small
    with dissolve
    
    x "(Maybe that's all he wanted... maybe he'll leave me alone now...)"
    show madd uncertain at left_small
    with dissolve
    
    scene scene_living_room_evening_dad_watching_tv_madd_sitting_near_dad_dad_hand_on_shoulder_cheek_kiss_neck_kiss
    with fade

    show dad calculating at right_small
    with dissolve
    x "(Suddenly, he reached near my neck ,his arms around my shoulder .)"
    
    show madd anxious at left_small
    with dissolve
    
    x "(Oh god, no... not this...)"
    show madd horrified at left_small
    with dissolve
    
    show dad lecherous at right_small
    with dissolve
    x "(His lips moved from my cheek down to my neck, kissing me softly at first.)"
    
    show madd trembling at left_small
    with dissolve
    
    show dad lustful at right_small
    with dissolve
    dad_says "Mmm, you smell so good, Maddie."
    
    show madd conflicted at left_small
    with dissolve
    
    x "(I felt a mix of disgust and fear rise within me, but I kept my silence.)"
    show madd distressed at left_small
    with dissolve
    
    x "(This is wrong... everything about this is so deeply wrong...)"
    show madd nauseated at left_small
    with dissolve
    
    x "(his saliva made my skin wet and sticky.)"
    show madd feels violated at left_small
    with dissolve
    
    x "(I feel like I'm going to be sick.)"
    show madd overwhelmed at left_small
    with dissolve
    
    show dad perverted at right_small
    with dissolve
    dad_says "You know, Maddie, your whole body is so tempting."
    
    show madd violated at left_small
    with dissolve
    
    show dad predatory at right_small
    with dissolve
    dad_says "How could I possibly resist you?"
    
    show madd paralyzed at left_small
    with dissolve
    
    x "(right after he said  those words , he started licking my neck. )"
    show madd horrified at left_small
    with dissolve
    
    x "(This is assault. This is rape. But who would believe me?)"
    show madd helpless at left_small
    with dissolve
    
    show dad fixated at right_small
    with dissolve
    x "(Covering my neck with wet kisses and licks. saliva dripping from his mouth. )"
    
    show madd paralyzed at left_small
    with dissolve
    
    x "(My body has gone numb. I can't even feel my legs anymore.)"
    show madd violated at left_small
    with dissolve
    
    show dad obsessed at right_small
    with dissolve
    x "(My neck was almost coated with his saliva. I was so disgusted.)"
    
    show madd distressed at left_small
    with dissolve
    
    scene scene_living_room_evening_dad_watching_tv_madd_sitting_near_dad_dad_hand_on_shoulder_cheek_kiss_neck_kiss_biting_neck
    with fade


    x "(then he started nibbling on my neck, his teeth gently biting into my skin. Like he wanted to devour me .)"
    show madd conflicted at left_small
    with dissolve
    
    x "(it wasn't painful but it was uncomfortable. Uncomfortable due to the nature of the act. with my own stepdad.)"
    show madd self loathing at left_small
    with dissolve
    
    x "( But somewhere deep inside me, a small part of me felt a strange thrill.)"
    show madd flustered at left_small
    with dissolve
    
    x "(A forbidden excitement that I couldn't ignore and hate myself for.)"
    show madd blush at left_small
    with dissolve
    
    x "(Along with it the neck kisses , it was kind of arousing in a twisted way.)"
    show madd inheat at left_small
    with dissolve
    
    show dad lecherous at right_small
    with dissolve
    dad_says "Mmm, you're so delicious, Maddie."
    
    show madd conflicted at left_small
    with dissolve
    
    show dad lustful at right_small
    with dissolve
    dad_says "I could do this all day."
    
    show madd deep blush at left_small
    with dissolve
    
    x "(after a while, he finally pulled away, leaving my neck red .)"
    show madd distressed at left_small
    with dissolve
    
    x "(My skin feels branded... marked as his.)"
    show madd violated at left_small
    with dissolve
    
    show dad sadistic at right_small
    with dissolve
    x "(I touched my neck, feeling the wetness and slight irritation from his kisses.)"
    

    if character_relations["dad"]["intimacy"] >= 40 and renpy.random.randint(1, 100) <= 60  :
        jump living_room_tv_with_dad_lust_scene_take_2


    
    scene scene_living_room_evening_dad_watching_tv_madd_sitting_near_dad_dad_hand_on_shoulder_cheek_kiss_neck_kiss_biting_neck_starting_to_undo_shirt
    with fade

    x "(I thought it was finally over, but then he started touching the hem of my shirt.)"
    show madd anxious at left_small
    with dissolve
    
    show dad lecherous at right_small
    with dissolve
    dad_says "You turn me on so much, Maddie."
    
    show madd horrified at left_small
    with dissolve
    
    show dad predatory at right_small
    with dissolve
    dad_says "I need to see all of you... "
    
    show madd paralyzed at left_small
    with dissolve
    
    x "(i felt a wave of panic rise within me as he started to lift my shirt.)"
    show madd traumatized at left_small
    with dissolve
    
    x "(This is it. This is the moment where it becomes something I can't take back.)"
    show madd horrified at left_small
    with dissolve
    
    show dad possessive at right_small
    with dissolve
    x "(I wanted to stand up and push him away, but his hand on my shoulder held me in place.)"
    
    show madd helpless at left_small
    with dissolve
    
    x "(I was locked in place, at his mercy.)"
    show madd paralyzed at left_small
    with dissolve
    
    show dad dominant at right_small
    with dissolve
    x "(As he lifted my shirt, I felt a mix of fear and shame wash over me.)"
    
    scene scene_living_room_evening_dad_watching_tv_madd_sitting_near_dad_dad_hand_on_shoulder_cheek_kiss_neck_kiss_biting_neck_shirt_removed_madd_topless
    with fade

    show madd violated at left_small
    with dissolve
    
    x "(My breasts are exposed now. There's no hiding anymore.)"
    show madd feels violated at left_small
    with dissolve
    
    show dad lecherous at right_small
    with dissolve
    dad_says "I let you stay at my house , live comfortably."
    
    show madd self loathing at left_small
    with dissolve
    
    show dad manipulative at right_small
    with dissolve
    dad_says "Your food, your clothes, your shelter... all from me."
    
    show madd resigned at left_small
    with dissolve
    
    show dad coercive at right_small
    with dissolve
    dad_says "Don't you think good people like me deserve some reward?"
    
    show madd helpless at left_small
    with dissolve

    x "(He was manipulating me to do this, using his power over me.)"
    show madd self loathing at left_small
    with dissolve
    
    x "(if i stop this now, he will make my life hell at home.)"
    show madd broken at left_small
    with dissolve
    
    show dad dominant at right_small
    with dissolve
    x "(Maybe he'll cut off my internet, maybe he'll evict me from his home.)"
    
    show madd resigned at left_small
    with dissolve
    
    x "(Only choice was to comply with his disgusting demands.)"
    show madd paralyzed at left_small
    with dissolve
    
    show dad lecherous at right_small
    with dissolve
    dad_says "There you go, Maddie. Such a good girl. Look at those nice breasts."
    
    show madd violated at left_small
    with dissolve
    
    x "(i felt so humiliated as he stared at my breasts.)"
    show madd feels violated at left_small
    with dissolve
    
    x "(I'm an object to him now. Just a body to use.)"
    show madd shocked at left_small
    with dissolve
    
    scene scene_living_room_evening_dad_watching_tv_madd_breast_groping_dad_hand_on_shoulder
    with fade

    show dad lustful at right_small
    with dissolve
    x "(He reached out and started fondling my breasts, his hands squeezing and caressing them.)"
    
    show madd paralyzed at left_small
    with dissolve
    
    show dad horny at right_small
    with dissolve
    x "(I felt a mix of disgust and unwanted arousal rise within me as he touched me.)"
    
    show madd conflicted at left_small
    with dissolve
    
    show dad lecherous at right_small
    with dissolve
    dad_says "Mmm, so soft and nice. you smell so good too."
    
    show madd flustered at left_small
    with dissolve
    
    show dad possessive at right_small
    with dissolve
    dad_says "Your body is perfect for me, Maddie."
    
    show madd deep blush at left_small
    with dissolve
    
    x "(he continued to fondle my breasts, his hands exploring every inch of them.)"
    show madd distressed at left_small
    with dissolve
    
    x "(I hate that my body is responding to this.)"
    show madd self loathing at left_small
    with dissolve
    
    show dad fixated at right_small
    with dissolve
    x "(his fingers digging into my nipples, making them harden.)"
    
    show madd inheat at left_small
    with dissolve
    
    x"(he would occasionally give a gentle pinch to my nipples, making me wince.)"
    show madd flustered at left_small
    with dissolve
    
    x "(The sensation is maddening... a mix of pleasure and pain that makes my mind foggy.)"
    show madd overwhelmed at left_small
    with dissolve
    
    show dad manipulative at right_small
    with dissolve
    x "(sometime he would pull my boob left and right, as if testing their weight.)"
    
    show madd feels violated at left_small
    with dissolve
    
    x "(He's treating me like I'm merchandise to inspect.)"
    show madd traumatized at left_small
    with dissolve
    
    scene scene_living_room_evening_dad_watching_tv_madd_breast_groping_dad_hand_on_shoulder_neck_kissing
    with fade


    show dad predatory at right_small
    with dissolve
    x "(His face moved closer to my face again, as he started kissing my neck again.)"
    
    show madd violated at left_small
    with dissolve
    
    show dad lecherous at right_small
    with dissolve
    dad_says "You have no idea how long I've wanted this."
    
    show madd horrified at left_small
    with dissolve
    
    scene scene_living_room_evening_dad_watching_tv_madd_breast_groping_dad_hand_on_shoulder_neck_kissing_biting_neck
    with fade

    x "(biteing and nibbling on my neck, his teeth leaving small marks on my skin.)"
    show madd distressed at left_small
    with dissolve
    
    x "(He's literally marking me as his property now.)"
    show madd feels violated at left_small
    with dissolve
    
    show dad possessive at right_small
    with dissolve
    x "(Saliva smearing my neck again. It was as if he was marking his territory.)"
    
    show madd overwhelmed at left_small
    with dissolve
    
    x "(his breath hot against my skin, his lips leaving wet marks on my neck. And his hands never leaving my breasts.)"
    show madd nauseated at left_small
    with dissolve
    
    x "(the mixture of sensations was overwhelming, making me feel both disgusted and strangely aroused.)"
    show madd conflicted at left_small
    with dissolve
    
    show dad dominant at right_small
    with dissolve
    dad_says "Doesn't this feel better? Stop resisting and just accept what you are to me?"
    
    show madd anxious at left_small
    with dissolve
    
    x "(I wanted this to end, I didn't want my stepbrother to see me like this.)"
    show madd self loathing at left_small
    with dissolve
    
    x "(He was doing this to me in the open living room, where anyone could walk in at any moment.)"
    show madd horrified at left_small
    with dissolve
    
    x "(if stepbrother walks in, he will see me like this, being molested by dad.)"
    show madd horrified at left_small
    with dissolve
    
    x "(Then he will also start doing the same to me.)"
    show madd broken at left_small
    with dissolve
    
    x "(I definitely can't handle the two of them doing this to me.)"
    show madd traumatized at left_small
    with dissolve
    
    x "(Then I had a horrible thought. what if stepbrother and stepdad together start doing this to me together....at the same time.)"
    show madd broken at left_small
    with dissolve
    
    x "(I would be sandwiched between them, both of them touching me and kissing me...)"
    show madd nauseated at left_small
    with dissolve
    
    show dad dominant at right_small
    with dissolve
    x "(I quickly shook off the thought, and i felt him nibbling my neck again.)"
    
    show madd resigned at left_small
    with dissolve
    
    scene scene_living_room_evening_dad_watching_tv_madd_breast_groping_dad_pulling_for_kiss_lips_close
    with fade

    show dad lecherous at right_small
    with dissolve
    x "(He moved his hand to the back of my head, pulling me closer to his lips.)"
    
    show madd paralyzed at left_small
    with dissolve
    
    x "(i was few inches away from his face, i could see the lecherous glint in his eyes.)"
    show madd nauseated at left_small
    with dissolve
    
    show dad possessive at right_small
    with dissolve
    x "(Now I was right in front of his face, i felt his breath on my lips as he leaned in closer and kissed me.)"
    
    show madd paralyzed at left_small
    with dissolve
    

    show dad lustful at right_small
    with dissolve
    dad_says "Kiss me back. Show me you want this."
    
    show madd violated at left_small
    with dissolve
    
    x "(His lips were rough against mine, his tongue trying to force its way into my mouth.)"
    show madd distressed at left_small
    with dissolve
    
    x "(I did not yield to his tongue at first, fighting against this degradation.)"
    show madd conflicted at left_small
    with dissolve
    
    scene scene_living_room_evening_dad_watching_tv_madd_breast_groping_dad_hand_on_madd_face_neck_kissing_passionate_kiss
    with fade

    show dad controlling at right_small
    with dissolve
    x "(But then he moved his hand to my face, holding me in place firmly.)"
    
    show madd helpless at left_small
    with dissolve
    
    show dad dominant at right_small
    with dissolve
    x "(Both of his hands were on my face now, holding me tightly as he deepened the kiss.)"
    
    show madd violated at left_small
    with dissolve
    
    x "(this is when i couldn't stop his tongue from entering my mouth.)"
    show madd nauseated at left_small
    with dissolve
    
    show dad lustful at right_small
    with dissolve
    x "(His tongue explored my mouth, tasting and teasing me.)"
    
    show madd distressed at left_small
    with dissolve
    
    show dad perverted at right_small
    with dissolve
    x "(he uses his tongue to carry spit into my mouth, making me gag a bit.)"
    
    show madd nauseated at left_small
    with dissolve
    
    x "(his tongue was rough and forceful, making me feel strangely aroused.)"
    show madd conflicted at left_small
    with dissolve
    
    x "(Perhaps it was the forbidden nature of the act, or the power dynamic between us...)"
    show madd flustered at left_small
    with dissolve
    
    x "(But I couldn't help but feel a twisted excitement I hate myself for.)"
    show madd self loathing at left_small
    with dissolve
    
    scene scene_living_room_evening_dad_watching_tv_madd_sitting_near_dad_dad_hand_on_shoulder_cheek_kiss_neck_kiss_biting_neck_shirt_removed_madd_topless
    with fade

    show dad sadistic at right_small
    with dissolve
    x "(After what felt like an eternity, he finally pulled away, leaving me breathless and dizzy.)"
    
    show madd shaken at left_small
    with dissolve
    
    x "(his taste still lingered in my mouth, making me feel even more confused.)"
    show madd processing at left_small
    with dissolve
    
    show dad lecherous at right_small
    with dissolve
    dad_says "Mmm, you're so tasty, Maddie."
    
    show madd blush at left_small
    with dissolve
    
    show dad lustful at right_small
    with dissolve
    dad_says "I could kiss you all day."
    
    show madd conflicted at left_small
    with dissolve
    
    show dad sadistic at right_small
    with dissolve
    x "(He finally let go of my face, leaving me trembling and disoriented.)"
    
    show madd trembling at left_small
    with dissolve
    
    x "(Then i grew more scared as i saw him move his hand to his jeans zipper.)"
    show madd horrified at left_small
    with dissolve

    if character_relations["dad"]["intimacy"] < 40:
        menu:
            "Stop Him from escalating" :
                if madd_willpower+2*(40-character_relations["dad"]["intimacy"]) >= character_relations["dad"]["lust"]:
                    show madd angry at left_small
                    x "(There is no way he stops with usual methods , I have to do something different)"
                    x "Dad...stop..."
                    x "If you traumatize someone hard they bite with such force its said to break bones."
                    x "Anything that goes in my mouth I will bite."
                    show dad angry at right_small
                    x "(I felt his grip on me loosen as he angrily growls)"
                    dad_says "You're really starting to piss me off, Maddie."
                    dad_says "I will get you  to swallow my load sooner or later , just you watch"
                    x "Yeah keep dreaming dad"

                    x "(He finally let go of me as i escaped the room fixing my clothes)"
                    $ character_relations["dad"]["anger"] +=20
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_123
                    $ character_relations["dad"]["intimacy"]+=5
                    call advance_time_and_check(minutes=120) 
                    $ madd_willpower=max(madd_willpower-20,0)
                    jump home_areas
                else:
                    $character_relations["dad"]["lust"]=0
                    $character_relations["dad"]["anger"] +=20
                    show madd trembling at left_small
                    x "(I wanted to stop him, but i was so scared that i couldnt even say anything, my voice was trembling and my body was shaking)"
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_124

    
    scene scene_living_room_evening_dad_watching_tv_hand_on_madd_shoulder_removing_jeans
    with fade

    show dad lustful at right_small
    with dissolve
    x "(He pulled his cock out, already hard and throbbing right in front of me.)"
    
    show dad sadistic at right_small
    with dissolve
    dad_says "Look at it, Maddie. This is what's going to knock you up soon."

    show madd horrified at left_small
    with dissolve
    x "(I stared at his throbbing cock in pure dread… the thought of him putting that inside me made me want to vomit.)"

    show madd shocked at left_small
    with dissolve
    
    x "(i felt a wave of panic rise within me as i saw his erect dick.)"
    show madd horrified at left_small
    with dissolve
    
    x "(It was huge, its smell making me nauseous even from this distance.)"
    show madd feels violated at left_small
    with dissolve
    
    x "(The heat radiating from it was noticeable... overwhelming...)"
    show madd overwhelmed at left_small
    with dissolve
    
    show dad dominant at right_small
    with dissolve
    dad_says "You know, Maddie, you're really lucky to have a dad like me."
    
    show madd self loathing at left_small
    with dissolve
    
    show dad possessive at right_small
    with dissolve
    dad_says "Now, you will reward me for all that i do for you."
    
    show madd helpless at left_small
    with dissolve
    
    show dad coercive at right_small
    with dissolve
    dad_says "Or do I need to remind you of your place?"
    
    show madd traumatized at left_small
    with dissolve
    
    x "(I was shaking my head silently, trying to resist his disgusting demands.)"
    show madd helpless at left_small
    with dissolve
    
    x "(This can't happen... I won't...)"
    show madd broken at left_small
    with dissolve
    
    scene scene_living_room_evening_dad_watching_tv_dad_pushes_madd_towards_dick
    with fade

    show dad controlling at right_small
    with dissolve
    x "(But he ignored my silent protests, as he moved his hand on my head again.)"
    
    show madd paralyzed at left_small
    with dissolve
    
    show dad predatory at right_small
    with dissolve
    x "(He grabbed the back of my head and started forcing my face toward his cock.)"
    
    show madd distressed at left_small
    with dissolve
    
    x "(I was using my head to resist him, but his grip was too strong.)"
    show madd helpless at left_small
    with dissolve
    
    x "(My lips were just inches away from his dick now.)"
    show madd horrified at left_small
    with dissolve
    
    show dad lustful at right_small
    with dissolve
    x "(I could breathe in its smell, the musky scent making me gag but also strangely aroused.)"
    
    show madd conflicted at left_small
    with dissolve
    
    x "(I should be hating this smell, but instead i found myself getting turned on by it.)"
    show madd flustered at left_small
    with dissolve
    
    show dad fixated at right_small
    with dissolve
    x "(His dick was throbbing now, the veins bulging out.)"
    
    show madd nauseated at left_small
    with dissolve
    
    scene scene_living_room_evening_dad_watching_tv_dad_pushes_madd_towards_dick_madd_mouth_opening
    with fade

    show dad horny at right_small
    with dissolve
    x "(I felt his hand push my head downwards, forcing my mouth to open.)"
    
    show madd violated at left_small
    with dissolve
    
    x "(As he lifted himself up a bit, enough that his dick touched my lips.)"
    show madd paralyzed at left_small
    with dissolve
    
    show dad possessive at right_small
    with dissolve
    x "(I felt his dick touch my lips, the tip brushing against them.)"
    
    show madd nauseated at left_small
    with dissolve
    
    x "(I closed my eyes, trying to block out the overwhelming sensations.)"
    show madd distressed at left_small
    with dissolve
    
    show dad dominant at right_small
    with dissolve
    x "(Then I felt his dick press against my lips, the tip nudging them.)"
    
    show madd hesitant at left_small
    with dissolve
    
    x "(I hesitated for a moment, but then I opened my mouth slightly, allowing the tip to enter.)"
    show madd resigned at left_small
    with dissolve
    
    show dad lustful at right_small
    with dissolve
    x "(as soon as the tip entered my mouth, he lowered himself along with my head.)"
    
    show madd nauseated at left_small
    with dissolve
    
    x "(The pressure of his hands on my head increased, forcing me to take more of his dick into my mouth.)"
    show madd helpless at left_small
    with dissolve
    
    x "(I gagged a bit as more of his dick entered my mouth, but I kept going, trying to please him.)"
    show madd overwhelmed at left_small
    with dissolve
    
    x "(the heat from his dick directly filling my mouth was overwhelming.)"
    show madd nauseated at left_small
    with dissolve
    
    x "(The taste was musky and salty, invading every corner of my senses.)"
    show madd distressed at left_small
    with dissolve
    
    show dad lecherous at right_small
    with dissolve
    dad_says "That's it… suck it like a good girl. Daddy's going to give you a nice reward soon."
    
    show dad mocking at right_small
    with dissolve
    dad_says "Keep sucking… I'm going to fill that belly with my seed one of these days."

    show madd nauseated at left_small
    with dissolve
    x "(His words made my stomach twist… he's already fantasizing about impregnating me while I have his dick in my mouth.)"
    
    show dad lustful at right_small
    with dissolve
    dad_says "God your mouth feels so good around my dick."
    
    show madd feels violated at left_small
    with dissolve
    
    show dad possessive at right_small
    with dissolve
    dad_says "The softness of your lips, the warmth of your mouth..."
    
    show madd nauseated at left_small
    with dissolve
    
    show dad coercive at right_small
    with dissolve
    dad_says "Now suck harder, show me your commitment."
    
    scene scene_living_room_evening_dad_watching_tv_dad_pushes_madd_towards_dick_madd_mouth_deepthroat
    with fade

    show madd submissive nod at left_small
    with dissolve
    
    x "(I felt a mix of disgust and unwanted arousal rise within me as i took all of his dick into my mouth.)"
    show madd overwhelmed at left_small
    with dissolve
    
    x "(My nose were pressed against his crotch.)"
    show madd nauseated at left_small
    with dissolve
    
    x "(the hair on his crotch was tickling my nose. the smell was much more concentrated here.)"
    show madd inheat at left_small
    with dissolve
    
    x "(Maybe this is why i was getting aroused despite the horror...)"
    show madd flustered at left_small
    with dissolve
    
    x "(The pheromones that have been latched onto the crotch hair were assaulting my nostrils.)"
    show madd overwhelmed at left_small
    with dissolve
    
    x "(Somehow i was getting aroused. Somehow my body was betraying me completely.)"
    show madd self loathing at left_small
    with dissolve
    
    show dad possessive at right_small
    with dissolve
    dad_says "Now you better start sucking properly or else this will go into another hole."
    
    show madd horrified at left_small
    with dissolve
    
    show dad dominant at right_small
    with dissolve
    dad_says "One that you definitely don't want it to go into."
    
    show madd paralyzed at left_small
    with dissolve
    
    x "(After he said that, i felt a wave of panic rise within me.)"
    show madd broken at left_small
    with dissolve
    
    x "(I started moving my head up and down, trying to suck his dick properly.)"
    show madd submissive nod at left_small
    with dissolve
    
    show dad sadistic at right_small
    with dissolve
    x "(His hands gripped my head tightly, guiding my movements.)"
    
    show madd helpless at left_small
    with dissolve
    
    x "(His cock started throbbing hard against my tongue, the veins bulging out as he grew more aroused.)"
    show madd overwhelmed at left_small
    with dissolve
    
    show dad lustful at right_small
    with dissolve
    x "(After a few moments, he started moving his hips, thrusting his dick deeper into my mouth.)"
    
    show madd nauseated at left_small
    with dissolve
    
    x "(It was getting harder to breathe with his dick in my mouth.)"
    show madd distressed at left_small
    with dissolve
    
    x "(My nose was completely pressed against his crotch hair, the smell making me dizzy.)"
    show madd nauseated at left_small
    with dissolve
    
    show dad predatory at right_small
    with dissolve
    x "(with my head moving up and down and him moving his hips, it was becoming really hard to breathe.)"
    
    show madd helpless at left_small
    with dissolve
    
    x "(I was gasping for air, my nose completely pressed against his crotch hair.)"
    show madd violated at left_small
    with dissolve
    
    scene scene_living_room_evening_dad_watching_tv_dad_pushes_madd_towards_dick_madd_mouth_deepthroat_dick_visible_in_throat
    with fade

    x "(his dick was hitting the back of my throat, some part of me liked the sensation...)"
    show madd conflicted at left_small
    with dissolve
    
    x "(But most of me was disgusted by my own response.)"
    show madd self loathing at left_small
    with dissolve
    
    x "(the lack of control over the situation was making me feel submissive and vulnerable in a twisted way.)"
    show madd overwhelmed at left_small
    with dissolve
    
    show dad dominant at right_small
    with dissolve
    x "(Then i felt it - the tip of his dick hitting the back of my throat.)"
    
    show madd nauseated at left_small
    with dissolve
    
    show dad controlling at right_small
    with dissolve
    x "(He stopped moving and applied more pressure on my head, forcing his dick deeper into my mouth.)"
    
    show madd helpless at left_small
    with dissolve
    
    x "(I knew he was going to cum soon. I could feel it... his whole body tensing.)"
    show madd processing at left_small
    with dissolve
    
    scene scene_living_room_evening_dad_watching_tv_dad_pushes_madd_towards_dick_dad_cumming
    with fade

    show dad obsessed at right_small
    with dissolve
    dad_says "ughhmm... yes... that's it..."
    
    show madd helpless at left_small
    with dissolve
    
    x "(After i heard him grunting, i felt a warm sensation in my mouth.)"
    show madd nauseated at left_small
    with dissolve
    
    show dad sadistic at right_small
    with dissolve
    x "(His dick pulsing as he released his cum directly into my mouth.)"
    
    show madd overwhelmed at left_small
    with dissolve
    
    x "(His dick was at the back of my throat, making it hard to contain the cum.)"
    show madd distressed at left_small
    with dissolve
    
    x "(I didn't have a choice but to swallow it.)"
    show madd resigned at left_small
    with dissolve
    
    show dad sadistic at right_small
    with dissolve
    x "(Thick, hot spurts of his cum flooded my mouth. I had no choice but to swallow it all.)"
    
    show madd traumatized at left_small
    with dissolve
   
    scene scene_living_room_evening_dad_watching_tv_dad_pushes_madd_towards_dick_dad_stays_in_mouth
    with fade

    x "(finally he stopped pulsing, his dick going limp in my mouth.)"
    show madd shaken at left_small
    with dissolve
    
    show dad possessive at right_small
    with dissolve
    x "(he didn't release his grip on my head yet, so i kept his dick in my mouth.)"
    
    show madd resigned at left_small
    with dissolve
    
    x "(for 2-3 minutes, he kept his dick in my mouth, making sure i swallowed all of his cum.)"
    show madd violated at left_small
    with dissolve
    
    scene scene_living_room_evening_dad_watching_tv_dad_still_naked_madd_cum_in_mouth
    with fade

    show dad dominant at right_small
    with dissolve
    x "(finally he let go of my head and pulled his dick out of my mouth.)"
    
    show madd distressed at left_small
    with dissolve
    
    x "(I breathed a sigh of relief, gasping for air like I'd been drowning.)"
    show madd shaken at left_small
    with dissolve
    
    x "(grateful that the uncomfortable moment was over... though I know it won't be the last time.)"
    show madd traumatized at left_small
    with dissolve
    
    show dad lecherous at right_small
    with dissolve
    dad_says "Good girl… swallow every drop. One day soon that won't be going in your mouth anymore."

    show dad predatory at right_small
    with dissolve
    dad_says "Next time that load is going straight into your pussy where it belongs."

    show madd traumatized at left_small
    with dissolve
    x "(I felt pure terror… he's not even pretending anymore. He wants to get me pregnant.)"

    
    dad_says "I have to say, you're getting better at this."
    show madd self loathing at left_small
    with dissolve
    
    x "(I said nothing, still trying to catch my breath.)"
    show madd violated at left_small
    with dissolve
    
    x "(I can't even bring myself to look at him...)"
    show madd broken at left_small
    with dissolve
    
    show dad sadistic at right_small
    with dissolve
    dad_says "I feel so much better now."
    
    show madd resigned at left_small
    with dissolve
    
    show dad creepy at right_small
    with dissolve
    dad_says "You did good today. Really good."
    
    show madd distressed at left_small
    with dissolve
    
    scene scene_living_room_evening_dad_watching_tv_dad_dressed_madd_cum_in_mouth
    with fade

    show dad dominant at right_small
    with dissolve
    x "(He says that, he pulled up his jeans and zipped them up.)"
    
    show madd trembling at left_small
    with dissolve
    
    x "(He seemed almost... satisfied with himself. As if what he did was somehow normal.)"
    show madd nauseated at left_small
    with dissolve
    
    show dad cruel at right_small
    with dissolve
    x "(i wiped my mouth with the back of my hand, trying to get rid of the taste of his cum.)"
    
    show madd self loathing at left_small
    with dissolve
    
    x "(I can still taste his cum… I feel so dirty. If I don't get away from him soon, he's really going to put a baby in me…)"
    show madd traumatized at left_small
    with dissolve
    

    x "(I picked up my shirt from the floor and put it on.)"
    
    show madd distressed at left_small
    with dissolve
    
    x "(My skin still bears his marks... his scent... his claim.)"
    show madd violated at left_small
    with dissolve
    
    show dad sadistic at right_small
    with dissolve
    x "(He stopped bothering me completely after that. He was watching TV now, like nothing happened.)"
    
    show madd horrified at left_small
    with dissolve
    
    x "(Like he didn't just destroy a part of me.)"
    show madd broken at left_small
    with dissolve
    
    show madd resigned at left_small
    with dissolve
    
    x "(I quickly got up and left the living room, heading straight to lobby.)"
    show madd traumatized at left_small
    with dissolve
    
    x "(I need to get away from him... I need to think about what just happened...)"
    call advance_time_and_check(minutes=120) from _call_advance_time_and_check_86
    $ madd_willpower=max(madd_willpower-30,0)
    $ character_relations["dad"]["intimacy"] += 7
    $ character_relations["dad"]["lust"] =0
    $ character_relations["dad"]["kissed"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["oral_sex"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ journal_event_set_done("Dad", "Evening TV Trap")
    $ sofa_TV_dad_scene_done = True

    jump home_areas


label living_room_tv_with_dad_lust_scene_take_2:
    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")

    show dad predatory at right_small
    show madd distressed at left_small
    dad_says "Time to stop pretending, my sweet girl. You've always been mine... and tonight, Daddy's finally claiming what was always meant to be his."
    x "(I immediately knew what he meant by that. This is not going to end with him just tasting my skin. He wanted more, much more.)"
    dad_says "Get on my lap, Maddie."
    show madd weeping at left_small
    x "(As soon as he said that, tears started to well up in my eyes. I didn't want to do this, but he lifted me with ease and placed me on his lap. I felt so small in that moment)"
    x "(I couldnt stop him from doing it, he was so much stronger than me. )"
    x "(Now i was sitting on his right thigh, facing him. His eyes were locked on mine, and I could see the lust in them. His hands planted firmly on my hips )"
    x "(My ass gently resting on his thigh, one of my legs folded  on the sofa, while the other folded around his left leg. )"
    show dad wistful at right_small
    dad_says "You look even more beautiful than your mother ever did. She was just a placeholder... you were always the one I was meant to have sitting right here."
    x "(There it is again , comparing me to my mom. As if the act of me being on his lap wasn't bad enough, now he goes ahead and says things like that making it even worse. )"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_kissing_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad predatory at right_small
    show madd shocked at left_small
    dad_says "Such a beautiful face you have, Maddie. "
    x "(As he said that his hands moved from my hips to the back of my head, pulling me closer to him. I was locked in his gaze, and I couldn't look away. )"
    x "(And his lips landed on mine. I was so shocked that I couldn't even react . He was controlling the kiss, his lips moving against mine, and I was just there, letting it happen.)"
    show madd paralyzed at left_small
    x "(His fat greasy hands ran all over my hair and my neck making me even more repulsed by him. )"
    x "(After a while he finally stopped kissing me and pulled back, looking at me with a satisfied smirk on his face. )"
    show dad lustful at right_small
    dad_says "Such a sweet taste ,Maddie. Taste like fear and innocence. I'm gonna ruin every bit of that . "
    x "(His greasy hands on my head made me want to vomit. I felt like a object, not his daughter.)"
    dad_says "Now, I will make you taste me instead. "
    x "(What the hell did he just say? It wasnt as if i wanted him to kiss me in the first place, but now he was saying that he wanted me to taste him? )"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad dominant at right_small
    show madd nauseated at left_small
    x "(He slowly takes off his shirt, revealing his fat, hairy chest. As soon as he took it off , the room filled with the stench of his sweat and body odor)"
    x "(I knew he showered daily ,but it was like his body just couldn't get rid of the smell. It was so bad that I could barely breathe.)"
    x "(He kept his arms raised and i immediately knew what he meant by tasting him. He wanted me to lick his armpits )"
    show madd horrified at left_small
    x "(just the site of his forest of hair and the smell of his sweat made me want to vomit. )"
    dad_says "Sniff your Daddy's pits, my sweet girl. Become used to the scent of your owner my little pet."
    x "(with his hands placed on my head he pulled me first towards his lips then moved me down towards his armpits. )"
    x "(I was directly in front of his armpits, the smell got so much more intense)"
    x "(His hands stayed on the back of my head, restraining me from moving away from him. I was trapped in that position, forced to smell his stench and look at his hairy armpits. )"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_licking_armpits
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad sadistic at right_small
    show madd violated at left_small
    dad_says "Go on… tongue out. I want you to savor the warm, bitter taste of my unwashed armpit sweat .Taste the sweat of the man who was always meant to have you. Let it mark you from the inside."
    x "(I knew that was coming , i had anticipated it but still the words hit me like a ton of bricks. )"
    show madd helpless at left_small
    x "(Against my will i opened my mouth and stuck out my tongue,  my mind was still trying to process what was happening, but I knew I had no choice but to obey him. )"
    x "(The stench hit me like a wall. I gagged hard, tears pouring down my face, but his hand kept me trapped in hell.)"
    x "(I started to slowly lick his armpits , the saltiness of his sweat hit my tongue and made me gag , the hairy texture  of his armpits made it even worse. )"
    x "(The hair was so thick it was restricting my tongue from fully touching his skin, and the taste of them was out of this world. )"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_licking_armpits_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad mocking at right_small
    show madd angry at left_small
    dad_says "Yeahhh, just like that… a proper daughter laps up every drop of her father's thick, musky pit sweat."
    x "(This porn brained maggot was trying to justify his disgusting actions , what a sick deranged piece of sht.)"
    x "(I continued to lick his armpits, with every passing moment the stench got worse and worse. I could feel my lungs filling with the foul air, every breath I took was like inhaling a cloud of filth. )"
    show madd disgusted at left_small
    x "(My hatred for him was growing stronger with every lick)"
    x "(His hands slowly pushing me deeper into his armpits towards the center of it all , where the hair was the thickest and the stench was the strongest. )"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_licking_armpits_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd conflicted at left_small
    x "(Slowly my senses adapted to the stench, and I was able to continue licking his armpits without gagging. )"
    x "(The room had pin dropped silent, the sound my tongue made as it brushed against his underarm hair was the only noise in the room. I knew that sound was like music to his ears, it was the sound of his daughter submitting to him and pleasing him in the most disgusting way possible. )"
    show dad delusional at right_small
    dad_says "Swallow it all, daughter. Daddy's sweat is your new nutrition. You'll thank me for it later when you're addicted..."
    dad_says "Plus i believe it is good for a girl to drink her father's sweat, it has many nutrients that are beneficial for the body."
    x "(What the actual fuck did he just say? Where does he even get this bs from? )"
    show madd horrified at left_small
    x "(My face burried deep in his armpits was changing my view of this situation, somehow it was rewinding my brain and making me think that maybe this was normal and that maybe i should be enjoying this. )"
    x "(No no no i need to snap out of this, this is not normal, this is not okay, this is disgusting and wrong on so many levels. )"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_licking_armpits_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd distressed at left_small
    x "(I moved my head around trying to move away from the deepest part of his armpits where the stench was the strongest, but his hands caught me quickly and pulled me back )"
    x "(Luckily i had gotten far enough away from the center of his armpits that the stench was bearable, )"
    x "(My tongue was now licking the outer edges of his armpits, where the hair was thinner. it was still disgusting but i want to maximize the distance between me and the center of his armpits as much as possible. )"
    show madd confused at left_small
    x "(The center was making me feel warm and dizzy, like i belonged there and that it was the only place i should be. )"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_licking_armpits_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd conflicted at left_small
    x "(With thinner hair i was getting more of his skin on my tongue, and the taste was even worse than before. It was like licking a salty, sweaty, hairy mess. )"
    x "(At least the texture was better , hair was getting in the way less and less, and i was able to get more of his skin on my tongue. )"
    show dad controlling at right_small
    dad_says "You think i dont notice you trying to get away from my armpits, Maddie? "
    x "(His hands started forcing me back towards the center)"
    x "(no no no i need to avoid the center, i need to keep him happy but i also should stay away from the warm fuzzy feeling that was starting to grow inside of me. )"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_licking_armpits_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd conflicted at left_small
    x "(I put my face directly between his chest and his armpits, giving me enough force to push myself away while continuing the actions he wanted. )"
    x "(That was the only way i could accomplish both goals at the same time )"
    x "(His hands loosened their grip on my head as i continued satisfying him )"
    x "(After a while i noticed i had actually gotten closer to the point I was trying to avoid)"
    show madd self loathing at left_small
    x "(This is so fucked… I was literally chasing the hottest, foulest part of his sweat now. My mind screamed no but my tongue kept licking like a desperate little addict.)"
    x "(No that cant  be right, it must be his hands slowly pushing me closer to the center without me realizing it. )"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_licking_armpits_7
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd self loathing at left_small
    x "(I prayed that it wasnt my body betraying me , that it was his doing that made me get closer but it was all a blur, i couldnt tell anymore. )"
    x "(I was instinctively licking from low to high and with every lick my face was going deeper and deeper .)"
    x "(it wasnt his hand , it was my body doing it on its own accord, like it was trying to get closer to the source of the stench, like it was trying to be consumed by it. )"
    show madd shaken at left_small
    x "(My body was even kissing his armpits now , taking some of his hair in my mouth and sucking on it. What the actual fuck was happening to me? )"
    x "(Why am i treating his underarm like a lover ? Why am i kissing it and sucking on it? )"
    show dad smirk at right_small
    dad_says "Pathetic. You're already addicted to your own father's nasty pits, aren't you, you filthy girl?"
    dad_says "Just so you know daughter , I havent put any pressure on your head , you did this all on your own. "
    x "(The words hit me like a ton of bricks, but i knew there was no lie in them )"
    show dad dominant at right_small
    dad_says "Since you're too weak to bury yourself deeper, Daddy will help shove your face where it belongs. "

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_licking_armpits_8
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small
    x "(As soon as he said that, his hands started pushing my head again)"
    x "(I was back where i began but somehow , someplace in my mind was relieved that i was back there. )"
    show madd flustered at left_small
    x "(My nose burred in his armpits again, the stench didnt feel bad at all now rather it felt like home, like this is where i wanted to be all along. )"
    x "(Being there sent a warm fuzzy feeling through my body, it was like i was being embraced by the stench, like it was wrapping around me and comforting me. )"
    x "(My tongue was now  autonomously licking his armpits, it had a brain of its own and all it wanted was to cover itself in intake his sweat and hair. )"
    show dad dominant at right_small
    dad_says "Beg for it with your tongue, babygirl. Soon you'll be crawling to sniff and clean Daddy's pits every single day. "
    dad_says "Just let go , soon your body will beg me to let you stay in my armpits all day long. "
    x "(If he had said that few moments ago i would have laughed in his face, but now it was like he was speaking the truth. )"
    x "(I could feel my body inertia taking over, it wanted to be in that position , in that spot inhaling his foul stench and tasting his sweat. )"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_licking_armpits_9
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    x "(Deeper and deeper my tongue went, swallowing his hot sweat and matted hair. Part of me was already broken and starting to crave being nothing but his personal armpit cleaner forever.)"
    x "(What had started as a disgusting and repulsive act became something i could tolerate and then it became something i craved. )"
    x "(My body was screaching at me to fall in love with my father's sweat , to be consumed by it and to never leave his armpits again. )"
    x "(The hot air surrounding it was like a warm blanket, it was comforting and soothing, it was like being wrapped in a cocoon of filth but somehow it was the most comforting place in the world. )"
    show dad sadistic at right_small
    dad_says "See Maddie, I told you you would love it. Just let go and enjoy it, we can be together like this forever. "
    x "(I date not reply to him, i was too ashamed to even look at him, but deep down i knew he was right. I was loving this )"
    x "(The room was silent again, the only sound was the sound of my tongue licking his armpits and the sound of his breathing. It was like we were in our own little world)"
    show dad horny at right_small
    dad_says "Your body seems to be getting hot, did my filthy sweat make you horny, Maddie? "
    show madd inheat at left_small
    x "(NO NO NO, I was not horny, I was just trying to survive this situation, his demeaning words previously were making me feel so small and worthless, but now his words were making me feel even better about myself )"
    x "(Like submitting to him was the only thing i was good at, being degraded and humiliated by him was actually turning me on, it was like i had turned into a masochist and he was my master )"
    dad_says "Oh ,I am getting kinda horny too daughter "
    dad_says "HA, i am gonna start sweating even more now, you have the chance to lick my sweat directly from the source"
    x "(When he said that, my heart skipped a beat, just the thought of licking his sweat directly from his skin was making me feel things i never thought i would feel. )"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_licking_armpits_10
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd salivating at left_small
    x "(And right he was, his underarms started sweating profusely, the stench was now overwhelming but i was loving it. )"
    x "(My body was serving him with such devotion, it was like i was a slave to anything that came out of his body. )"
    x "(This sweat was much more potent , it smelled more foul and was more salty in nature. But why the hell was i loving it even more than before? )"
    x "(It got worst in every way possible but it was making me addicted to it more and more )"
    show dad lecherous at right_small
    dad_says "Taste my freshly produced filthy sweat, Maddie. I want you to savor every drop of it. "
    x "(I was in a state of pure bliss, his words had no impact on my mind anymore, they were just background noise to the overwhelming sensation of my servitude and submission to him. )"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_licking_armpits_11
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd salivating at left_small
    x "(The hair was now wet from my tongue and his persperation, it was sticking to my face and my lips .)"
    x "(My mouth was watering from my own saliva , as if my body was trying to produce more saliva to help me consume his sweat. )"
    x "(I was combing  through his hair with my tongue and sucking on it, trying to get every last drop of his sweat that was clinging to it. )"
    show dad dominant at right_small
    dad_says "Damn… you're actually getting into this, aren't you?"
    dad_says "Say it , tell Daddy you want to be his personal hairy armpit slave for the rest of your life."
    x "(The worst part wasn't the smell anymore. It was how my body was throbbing with shameful heat at the thought of being reduced to his pit cleaner.)"
    dad_says "You can comb through my armpit hair with your tongue and suck on it whenever you want, you can be my personal armpit slave, what do you say Maddie? "
    show madd self loathing at left_small
    x "(I was in such a state of submission that i didnt even have to think about it, if my mouth wasnt so stuffed with his hair i would have said yes immediately, but instead i just continued my actions "
    x "( Why was i getting so turned on by the idea of being his personal armpit cleaner? Why was i craving the idea of being his slave and serving him in such a disgusting way? )"
    x "(Just few moments ago all i was thinking about was how to get away from this house and become a engineer and now i was fantasizing about being his personal armpit cleaner, what the actual fuck was happening to me? )"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_licking_armpits_12
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    x "(By now his whole underarm was a mess and so was my face , covered in the mixture of his sweat and my saliva, the stench was gravitational, it was pulling me in deeper and deeper into his armpits )"
    x "(all i wanted in that moment was for him to force my face deeper into his underarms and cover my face with his hands. Blinding me and suffocating me in his stench )"
    x "(I just couldnt get enough of it)"
    show dad perverted at right_small
    dad_says "My ass sweats way worse than my pits, Maddie. I'll sit on your pretty face and make you tongue my filthy asshole clean if you behave."
    dad_says "I can let you lick my ass sweat whenever you want, just say the word and i will let you have it. "
    x "(I know for a fact that his ass sweat stinks more than his armpits? But just the thought of licking his butt sweat was like a forbidden fruit, it was like the ultimate act of submission and degradation, and for some reason i was craving it. )"
    x "(Hearing that my licks got more sloppy and desperate, my body was begging for more of him)"
    dad_says "heh, i can see from your actions that you really want to taste my ass sweat, don't you Maddie? "
    show dad debased at right_small
    dad_says " Maybe i would force my asshole directly into your face, the hair right near my anus would be the most potent and foul smelling part of my body, you would be in heaven licking it. "
    show madd conflicted at left_small
    x "(STOP STOP STOP, I was trying to block out his words but they were like daggers to my brain, the thought of licking the most foul part of his body was turning me on and making me want to submit to him even more. )"
    x "(Snap out of it Maddie ,just licking his armpits was bad enough, you dont want to go down that path, you dont want to be his personal armpit cleaner, you dont want to be his personal ass cleaner, you just want to get out of this house and never see him again. )"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_licking_armpits_13
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small
    x "(I managed to block out his words and thoughts of licking his ass sweat and noticed that the sweat had settled into the hair of his armpits, it was like a thick layer of filth that was clinging to his hair and my face. )"
    x "(As i pressed the hair with my face and tongue, sweat oozed out of it and i would directly drink it, it was like a never ending supply of his sweat that i could consume. )"
    x "(This place was like  all you can eat buffet of my father's sweat, it was like i had hit the jackpot of filth )"
    show dad sadistic at right_small
    dad_says "Not gonna lie , at first i just wanted to make you do it to humiliate and degrade you, but now seeing you like this, so into it, so submissive and obedient is like a treat"
    dad_says "You're addicted to Daddy's sweat now, aren't you?"
    show madd broken at left_small
    x "( i knew doing this was giving him signals that i accepted his dominance , that i accepted my part in this twisted relationship)"
    x "(There was no going back now, i was in too deep, i was gonna be his slave and i would not be able to refuse his commands anymore, i would have to do whatever he wanted me to do, and that thought was both terrifying and exciting at the same time. )"
    show dad possessive at right_small
    dad_says "Enough pit cleaning, whore. Time for Daddy to breed his daughter "
    show madd shocked at left_small
    x "(Huh ?? What did he just say? I was so lost in the haze of submission and lust that his words barely registered in my brain, but when they did, they hit me like a ton of bricks. )"
    x "(Is he really gonna try to fuck me right in the living room? is this really happening? )"
    x "(His hands pulled me away from his armpits and it was like i was being ripped away from a precious and comforting place)"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_lap_kiss_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    x "(He lifted me up once again and placed me in the center of his lap, he moved my leg to the side of his legs. This was a prime position for him to fuck me, it was like he was preparing me for it. )"
    show dad manipulative at right_small
    dad_says "I allowed you to clean my armpits and i know you enjoyed it, but now it's time for you to do something for me, something that will really please me. "
    x "(I was scared out of my mind , i didnt dare look him in the eyes, but i knew what he wanted, i knew what he was hinting at. )"
    x "(I was gonna have to let him fuck me, that was the price i had to pay for being his armpit cleaner, that was the price i had to pay for being his slave. )"
    x "(His hands wrapped around my back , at that moment i knew i was locked in, there was no way i could escape from his grasp, there was no way i could refuse him. )"
    x "(my eyes was still set on his armpit even though the hair was no longer visible , it was like a bird that was looking at its nest, i wanted to be there again instead of this new position that i was in now. )"
    show dad lustful at right_small
    dad_says "Eyes on me, slut. Watch your own father claim your womb."
    x "(I finally looked up at him, and the lust in his eyes was so intense . I knew once he was inside me , it would  take couple of cranes to get him out of me...)"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_lap_kiss_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad possessive at right_small
    show madd overwhelmed at left_small
    dad_says "Tonight I ruin you forever, Maddie. "
    x "(As he said that , his hands placed on the back of my head and he pulls my hair making my head arched back)"
    x "(And he starts kissing me again, The taste that was still lingering in my mouth from his armpits mixed with the taste of his lips was like a cocktail of filth )"
    show madd nauseated at left_small
    x "(His saliva mixing with his sweat mixing with my own saliva , there was a soup of bodily fluids in my mouth, it was like a disgusting and revolting mix that i was consuming with such pleasure )"
    x "(his other hand on my thighs raising it a little bit more, giving him better access to my pussy )"
    x "(At that moment i knew i was a dough in his hands and he was preparing me for the oven, he was getting me ready to be baked, he was getting me ready to be impregnated with his seed. )"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_lap_kiss_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad dominant at right_small
    show madd distressed at left_small
    dad_says "Give daddy some room okay?"
    x "(He says that as his hands moved towards the soles of my feet and he lifts my right leg up and places it on his shoulder, giving him better access to my pussy)"
    x "(Once my feet were on his shoulders , his hands moved back to my hips and he pulled me closer to him, his lips never leaving mine)"
    x "(My body was in a contorted position, my back arched and my legs spread apart, flexible enough to allow him to have full access to my pussy, and i was just there, letting him do whatever he wanted to me. )"
    x "Dad..I..it kind of hurts.."
    show dad cruel at right_small
    dad_says "Shut up and take it. Daughters exist to be fucked by their fathers. "
    x "( there was no love in his voice, there was no care, there was only lust and dominance. )"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_lap_kiss_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad sadistic at right_small
    show madd paralyzed at left_small
    x "(He stops kissing me for a second and looks at me with a smirk on his face)"
    dad_says "i'm gonna fuck the sh*t out of you, Maddie. I'm going to destroy this tight pussy and pump you so full of cum you'll be leaking for days. "
    x "(he says that and he starts kissing me roughly again , his tongue invading my mouth and his hands gripping my hips tightly)"
    x "(He starts pulling my hair roughly with one hand and with other he pulls me in a bear hug, crushing my body against his and making it impossible for me to move away from him)"
    x "(My legs being trapped in that position and his grip on my hips , There was literally no room for any movement at all. I couldnt even move an inch without his permission )"
    show dad possessive at right_small
    dad_says "You're Daddy's property now. I fuck you raw, I breed you, and you say thank you. "
    x "(He kept repeating demeaning and degrading words directed towards me as he continued to kiss me and prepare me for the act of accepting his seed inside me. )"
    show dad authoritative at right_small
    dad_says "You are my daughter, and you will do as I say.  "
    dad_says "I'm going to rape this tight cunt of yours and force so much thick cum inside you that you get pregnant whether you fucking like it or not. I'm breeding you against your will tonight."
    x "(My mouth was invaded by his tongue and my body was being crushed against his, i had no room to move or talk )"
    dad_says "Now let's see how you look down there "
    x "(He says that and he roughly pulls away my shorts)"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_lap_kiss_maddie_undressing
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd trembling at left_small
    x "(As soon as he removed my shorts , cold air hit my pussy and ass which acted as a wake up call to my brain )"
    show madd horrified at left_small
    x "(This is really happening maddie , you will be fucked by your own father, you will be impregnated by him, you will have his child growing inside you, and i have no say in the matter )"
    x "(For some reason the thought of having no say in this situation and being completely at his mercy was turning me on even more)"
    show dad hungry at right_small
    dad_says "You have such beautiful body, Maddie. I cant hold it in anymore, I need to fuck you right here right now. "
    x "(His lips kept kissing mine with his tongue sliding in and out of my mouth carrying the taste of his saliva to mine )"
    x "(I heard a zipper and a asson being undone, and I knew he was taking off his jeans )"
    show madd anxious at left_small
    x "(Even though i knew what his plan was , every action that he took that got closer to the act of him fucking me was making me more and more anxious )"
    x "(Is he really gonna fuck his own daughter in the living room? What if brother sees us ? )"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_lap_both_naked_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd flustered at left_small
    x "(I didnt see it but i felt a hard bulge pressing against my pubic region, It wasnt the tip of his manhood . It was the base of it , the heat generated by it was radiating through it was like a furnace )"
    show dad lustful at right_small
    dad_says "Feel how hard I am for you, Maddie. No man can ever resist you, not even your own father. "
    x "(By now i was panting heavily, my body was in a state of pure arousal and fear , yet i was so turned on by the idea of being fucked by my own father)"
    show madd conflicted at left_small
    x "(I was breathing directly from his mouth, even the air i breathed was tainted with his saliva .)"
    dad_says "I can already tell you are wet for me, Maddie. I will let my dick judge how much you want me. "
    x "(My heart was pounding in my chest , knowing that the moment of truth was finally here, the moment where he would finally put his dick inside )"

    if character_relations["dad"]["intimacy"] < 80:
        if madd_is_virgin and last_madd_drugged_day < 0:
            if character_relations["dad"]["vaginal_sex"] < 1 and madd_is_virgin: 
                x "(Oh no... he's really going to do it.)"
                x "(NO NO no, I'm still a virgin... I can't let him fuck me like this.)"
                x "Please stop... Dad, please don't do this to me..."

                show madd horrified at left_small
                dad_says "Shut up. You're going to take it whether you like it or not."

                show madd conflicted at left_small
                x "(I have to stop this. I can't let him take my first time like this...)"
                x "If you don't stop, I'll call the cops the second I get out of here!"

                if dad_knows_madd_stole_crypto or dad_knows_madd_drugs_food:
                    show dad smirk at right_small
                    dad_says "Go ahead. Call them. Tell them how you stole my crypto... or how you drugged our food."
                    x "(My stomach dropped. He knew. He fucking knew this whole time.)"
                    x "(I froze. I had nothing left to threaten him with.)"
                    show dad dominant at right_small
                    dad_says "That's what I thought. Now be a good girl and spread your legs properly."
                else:
                    show dad angry at right_small
                    dad_says "Fucking mood killer. You really think you can threaten me?"
                    x "(His face changed. The lust was still there, but now it was mixed with real anger.)"
                    dad_says "Get the fuck off me. Go on, run. But don't think this is over."

                    show madd broken at left_small
                    x "(I quickly climbed off his lap, grabbed my shorts from the floor, and ran out of the living room.)"
                    x "(My legs were shaking so badly I could barely walk straight.)"
                    call advance_time_and_check(minutes=120)
                    $ madd_willpower = max(0, madd_willpower - 25)
                    $ character_relations["dad"]["anger"] += 15
                    $ character_relations["dad"]["intimacy"] += 7
                    jump home_areas

        elif madd_is_virgin and last_madd_drugged_day > 0:
            x "(The drug is still making my body heavy... I can't even push him away properly.)"
            x "(I'm still a virgin... and I'm about to lose it to my own stepdad while sitting on his lap.)"
            x "(This is so fucked up. Mom used to sit with him like this... and now I'm about to let him fuck me in the same spot.)"
            x "(I'm sorry, Mom... I don't want this... but my body isn't listening to me at all.)"


    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_lap_both_naked_first_insertion
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd violated at left_small
    x "(The fat head of Dad's cock forced my pussy lips apart and sank in. Fuck… my own father was really stretching my cunt open right now.)"
    x "(I felt my pussy stretch around my own dad's cock. Every inch sliding deeper made me feel so stuffed and completely violated.)"

    if madd_is_virgin:
        x "(Something inside me gave way with a wet, tearing sensation. A burning stretch shot through my core as he kept dragging me down onto him.)"
        x "(I felt the sudden warmth of blood seeping out around his cock while he pushed deeper. He didn't slow down at all — he just kept pulling me lower until I was sitting fully on his lap with his entire length buried inside.)"

        show dad sadistic at right_small
        dad_says "Hah… finally. I've been waiting to ruin this hole since you moved in."

        show madd broken at left_small
        with dissolve
        x "(My fingers dug into his shoulders. I could feel the sticky warmth leaking out of me and dripping down between us. He was all the way in now, stretching the fresh wound he just made while I sat straddling him on the sofa.)"

        show dad hungry at right_small
        dad_says "Look at you… sitting on your dad's cock with blood running down it. What would your brother think if he walked in right now and saw his sister like this?"

        show madd horrified at left_small
        with dissolve
        x "(The thought made my stomach twist. He was still holding me down, keeping me impaled while he spoke. I could feel every small movement of his cock inside the torn, bleeding space he had just claimed.)"

        show dad dominant at right_small
        dad_says "This is mine now. I took it right here in the living room while you were dripping all over me. No one else is ever getting this."

        show madd violated at left_small
        with dissolve
        x "(I could feel the slow, warm trickle continuing to leak out around where we were joined. The shame of losing it like this — on his lap, in the middle of the house — sat heavy in my chest.)"

        show dad possessive at right_small
        dad_says "From now on, whenever you sit on this sofa, you're going to remember how I broke you in on it."

        $ madd_is_virgin = False



    show madd self loathing at left_small
    x "(The pressure was insane. Shame hit me like a truck but my body kept getting wetter, clenching around him like a traitor.)"
    x "(This is so fucked up. Dad's dick is buried all the way inside my pussy. I felt owned in the worst way possible.)"
    x "(I was already so wet that the initial insertion was not painful at all, it was more of a sensation of fullness and pressure rather than pain)"
    x "(Immediately after he pushed it inside me , he started pounding into me, his thrusts were hard and fast, and I could feel every inch of him inside me. )"
    show dad dominant at right_small
    dad_says "There we go , Maddie . You are so wet for papa "
    show madd inheat at left_small
    x "(Even though my mouth was still occupied with his tongue, i started moaning due to the pleasure of his thrusts, the feeling of being filled up by him was overwhelming and it was making me lose control of my body)"
    x "(It was as if i had no control on what was coming out of my mouth anymore, the moans were just escaping from my lips without any conscious effort from me)"
    x "(He continued pounding me with such force that it was like he was trying to break me , he had no regard for my pleasure or my pain he only cared about his own pleasure and that meant treating me like a piece of meat that he could use and abuse as he pleased )"
    show madd worried at left_small
    x "(The room filled with the sound of his thrusts and my moans, fuck...its evening time   that means brother is awake in his room. I hope he doesnt hear us )"
    x "(I tried to keep my moans as quiet as possible but the pleasure was making it hard for me to control them, I was so turned on by the act of being fucked by my own father  )"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_lap_both_naked_pounding_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd trembling at left_small
    x "( I kept holding my moans in as best as i could making the sound limited to small whimpers and gasps )"
    x "(But the loud sound of his thrusts was like a drumbeat that was echoing through the room, it was like a constant reminder of what was happening to me)"
    x "(I was still wrapped in his embrace with nowhere to move , my face locked in his kiss and my body being pounded by him )"
    x "(And the only sound i was hearing was his dick slapping against my pussy )"
    x "(It was as if all my senses were telling me i had already submitted to him, that i was already his slave )"
    show dad mocking at right_small
    dad_says "Hmm, why are you so quiet, Maddie? Are you trying to act like you dont enjoy this? You know you love it when I fuck you, don't you? "
    x "(I didnt show any reaction to his words , my eyes were closed shut and my body was trembling with pleasure and fear, but i didnt want to give him the satisfaction of knowing that his words were affecting me)"
    show dad cruel at right_small
    dad_says "Dont worry Maddie , I know you love it, the way your pussy is clenching around my cock, the way your body is trembling, I can notice it all "
    dad_says " Moan louder or I'll carry you straight to your brother's room and fuck you on his bed. "
    show madd horrified at left_small
    x "(What the hell. He was threatening to fuck me in front of my brother if i didnt let him hear my moans? That was like the ultimate humiliation, the thought of being fucked by my own father in front of my brother was making me want to die right there on the spot )"
    show madd submissive nod at left_small
    x "(i just nodded my head in response to his words, still my eyes closed ... I knew i had  no choice but to let him hear me)"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_lap_both_naked_pounding_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd inheat at left_small
    x "(He started pounding me even harder ,his thrusts were like a machine gun, rapid and relentless. )"
    x "(This time i didnt hold back my moans, i let them out freely, the pleasure was too much to contain and i would rather my brother hear me than to be fucked by my father in front of him )"
    x "(His cock was reaching the deepest parts of my pussy , the warmth spreading through my body was like a fire that was consuming me)"
    x "(With every thrust he was going deeper and deeper , as if he was exploring every inch of me with his dick and as he got deeper my moans got louder)"
    show dad sadistic at right_small
    dad_says "That's the sound i like to hear Maddie , let the world know you are getting fucked by your own father "
    dad_says " And that you love every second of it "
    show madd broken at left_small
    x "(I should've stopped after he said that , but now that i had let my moans out, i was in too deep, i was loving this too much)"
    x "(I was so focused on his dick pounding into me that i didnt even notice this whole time he had been kissing me too, only when the smell of his saliva got so dense that it was like a cloud of filth surrounding me, did i realize that he had been kissing me the whole time, his tongue still invading my mouth and his lips still pressed against mine as he pounded into me )"
    x "(I was moaning directly into his mouth and he absolutely loved it)"
    show dad possessive at right_small
    dad_says "Cmon Maddie , i want our hearts to connect , i want to be one with you"
    x "(as he said that he riped my shirt off completely, exposing my breasts to him and continued kissing and pounding me)"
    x "(Now my whole body was in direct contact with his , this is what he meant by being one with me, this is what he meant by connecting our hearts)"


    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_lap_both_naked_pounding_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    x "(His grotesque sweaty belly was directly touching mine now , the hair sticking to my skin . It was like truly a rough and dirty act of love, we were like two animals mating in the wild, there was no love or care, there was only lust and his will to impregnate me)"
    x "(For some reason my moans got more feminine and submissive , the bare touch of his skin broken something inside of me, it was like i was being reborn as his slave )"
    show madd resigned at left_small
    x "(His chest and belly were sweaty and sticky and it was all rubbing against my skin , i was being coated in his filth and my body was loving it)"
    x "(My moans were really girly now , my body has accepted my role as his daughter who listens to everything her dad commands )"
    show dad mocking at right_small
    dad_says "Whoa that's the best moan I've ever heard from you, Maddie. You sound like a bitch in heat."
    dad_says "Don't worry, I'm gonna make you scream like a bitch in heat too when I cum inside you. "

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_lap_both_naked_pounding_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show dad calculating at right_small
    show madd conflicted at left_small
    x "(He slowed down a little bit, now he was moving his hips in a slow and sensual way, savoring every moment of being inside me )"
    dad_says " Even being slow with you is so enjoyable , its so warm and tight."
    dad_says "You might not put it in words but your pussy is practically begging for me to cum inside you, isn't it Maddie? "
    x "(NO Maddie , you dare not respond to him )"
    x "Give me ....."
    x "(Before i could finish i stopped myself , thank god my mind was still functioning and i was able to stop myself from saying those words out loud)"
    show madd determined at left_small
    x "(Putting them into words was like a contract that would bound me to him even more, it was like signing a deal that would make me his slave forever, and i was not ready to do that yet )"
    show dad coercive at right_small
    dad_says "Why did you stop yourself, Maddie? Are you trying to deny that you dont want me to cum inside you? "
    x "(I continued moaning and panting heavily, trying to avoid responding to his question)"
    dad_says "TCh, fine THen I will make this moment even more memorable for you "
    x "( As he said that , he pulls me even closer to his body, his chest and belly now completely pressed against mine)"

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_lap_both_naked_pounding_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd overwhelmed at left_small
    x "(There was no space between our bodies now , it was airtight. I could smell him in every breath i took, i could feel his sweaty body all over me)"
    x "(It was like a quicksand of filth that was pulling me in deeper and deeper into his embrace)"
    x "(Meanwhile he kept eating my face with his tongue and making his dick slam into me brutally at the same time )"
    show dad dominant at right_small
    dad_says "I am gonna break you in, Maddie. I'm gonna make you mine forever. "

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_lap_both_naked_pounding_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd conflicted at left_small
    x "(With the bear hug i was in he was pushing me downwards, while he was pushing up with his thrusts, it was like he was trying to bury himself inside me )"
    x "(Pistoning into me , he wasnt lying when he said he was gonna break me in, and i knew with each thrust i was getting closer and closer to losing myself to him )"
    show dad possessive at right_small
    dad_says "You will submit to me completely, Maddie. You will be my obedient daughter and you will let me impregnate you with my seed. "
    dad_says "After you push out my first bastard I'm going to rape you again the same day and breed you by force until you're nothing but my permanent breeding machine. You have no choice."
    show madd broken at left_small
    x "(The thought of being impregnated by him again and again should be terrifying, but for some reason it was making me even more turned on )"
    x "(The thought of being breeding machine for your father was so taboo and disgusting but it was feeling like the most exciting thing in the world to me at that moment )"


    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_lap_both_naked_pounding_7
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    x "(At that point i was moaning like a dog who just got shot , which wasnt far from the truth, I was in so much pleasure and pain that i had no control over my vocal cords anymore, i was just letting out whatever sounds were coming out of my mouth )"
    show dad dominant at right_small
    dad_says "See Maddie, your whole body wants me . It wants my seeds to reach your womb and fertilize you"
    dad_says "Your pussy is clenching even harder around my dick, pulling me deeper inside you"
    x "(I was continously moaning and panting heavily, my body was in a state of pure ecstasy . Having his cum inside me would definitely push me over the edge, I must resist )"
    x "(Even with my mouth invaded by his tongue i managed to say )"
    show madd determined at left_small
    x "Please...Dad...no..we cant... "
    x "I cant...have a baby ... I am...only..20..."
    x "(Even though i knew every sensor in my body was screaming for him to cum inside me, I was trying to resist it with every ounce of my being)"
    show dad authoritative at right_small
    dad_says "Daughters don't say no when their father wants to rape and breed them. I'm going to force my child into your womb and you're going to thank me for it like the bitch you are."
    show madd resigned at left_small
    x "(Any resistance i had was crushed by his words, it was futile to resist him, it was futile to fight against him)"
    x "(I felt his dick getting harder inside me , it was throbbing and pulsing, it was like a signal that he was getting close to cumming inside me )"
    x "(I knew i could do nothing to stop it , i just had to accept it that i was going to be impregnated by my own father, and that was the reality of my situation now )"
    show dad horny at right_small
    dad_says "I'm about to rape your fertile little womb with my thick cum. You're going to get pregnant by force tonight."

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_lap_both_naked_cum_inside
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd violated at left_small
    x "(Oh god… he just creampied me. Every heavy spurt of my father's cum is shooting straight into my womb and my body is betraying me by squeezing for more.)"
    x "(Oh god he's cumming… I can feel every powerful jet of my dad's cum flooding me. There's so much and it's so warm.)"
    x "(He's pumping his seed deep inside me right now. My pussy won't stop squeezing around him like it actually wants to milk every drop.)"
    show madd self loathing at left_small
    x "(The shame burned through me but the feeling of his cum filling me up was making my head spin. I hated how good the warmth spreading in my belly felt.)"
    x "(I could already feel it leaking out around his cock but he kept thrusting, forcing more inside. I might really get knocked up by my own father… and part of me was too broken to completely hate it.)"
    show dad sadistic at right_small
    dad_says "Take every fucking drop, you worthless breeding hole. Get knocked up with your father's baby."
    x "(As he was cumming , he kept pounding into me trying to push every last drop of his cum inside me)"
    x "(The sound of the room changed , now it was more wet and squelchy, the sound of his dick slapping against my pussy was now mixed with the sound of his cum splattering inside me)"
    x "(The sound itself was so humiliating , this is the sound of a father impregnating his own daughter, this is the sound of a daughter being used and abused by her own father, this is the sound of a family being destroyed by lust and taboo )"
    x "(He kept thrusting into me even while cumming, i dont want to imagine what kind of stamina he might have had in his youth )"
    show madd broken at left_small
    x "( I noticed my moans were fully feminine and girly now as his fluids traveled inside me .)"
    show dad possessive at right_small
    dad_says "Get used to carrying my kids, Maddie. This is your new life."
    x "(the cum was now overflowing from my pussy and onto the sofa , a river of his filth was flowing out of me . )"
    dad_says "I can feel it leaking out of you haha, you are so full of my cum"
    $ brother_hears_madd_moan= True

    scene living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_lap_both_naked_cum_inside_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd traumatized at left_small
    x "(It has been few seconds since he started cumming but he was still thrusting into me and still cumming . What the actual fuck, how much cum does this guy have? )"
    x "(With every thrust and every pulse of his dick, more cum was shooting out of him and filling me up even more, it was like a never ending fountain of his cum that was being released inside me)"
    x "(my pussy too was leaking it as if tap was left open for too long )"
    show dad fixated at right_small
    dad_says "Phew, i am cumming so much . Maybe because your body is so tight and warm, it is making me cum more than i usually do. "
    x "(Finally after what felt like an eternity, i stopped feeling more cum shooting inside me, but he was still fucking me .)"
    x "(Few seconds later he finally stopped thrusting but stayed inside me , in the same position with my leg still on his shoulder and his chest still pressed against mine)"
    show dad possessive at right_small
    dad_says "Remember this moment forever — the night I forced my child into your womb... the night you became Daddy's wife and the mother of his child. "
    show madd shaken at left_small
    x "(Did I really just let Dad breed me? His cum is still leaking out of me and my stupid pussy is still twitching like it wants another load.)"
    x "( I need to get afterpill from the pharmacy as soon as possible, i need to make sure i dont get pregnant from this, i need to make sure that this never happens again )"
    x "( but i knew near the end  i was enjoying it...i was enjoying it ever since i sniffed his armpits. its like his pheromones had taken over my brain and made me crave for his filth and his seed, it was like i had become addicted to him and his body, and now that addiction had reached its peak with me possibly being impregnated by him )"
    show dad delusional at right_small
    dad_says "Let's just stay like this for a while, let my cum settle inside you"
    dad_says "the more it stays in you the more you will change , the more you will crave for it"
    dad_says "Even if you don't get pregnant tonight, I'm still going to ruin you permanently. My cum is going to break you so you'll crave being forcefully mated by me for the rest of your life."
    show madd broken at left_small
    x "(i was so tired and overwhelmed that i just nodded my head in response to his words. I knew something inside me had changed, i knew i was never gonna be the same again)"
    x "(After a while , he finally pulled out of me and i could feel the emptiness inside me, as cum gushed out of me like a dam breaking )"
    x "(His dick was holding the cum inside me like a plug, now that it was removed, the cum was just flowing out of me uncontrollably)"
    x "(He pushed me aside as i laid there on the sofa, as i looked with awe and horror at the mess that was my pussy and the sofa covered in his cum . Just how much cum did he have? )"
    show madd traumatized at left_small
    x "(I finally got up to clean myself with some tissues, and picked up my clothes that were thrown on the floor to go on about my day like nothing happened, but deep down i knew that nothing was gonna be the same again, i was now a slave to my father's lust and his seed, and there was no way out of it )"

    call advance_time_and_check(minutes=120) from _call_advance_time_and_check_95
    $ madd_willpower = max(madd_willpower - 40, 0)
    $ character_relations["dad"]["intimacy"] += 11
    $ character_relations["dad"]["lust"] = 0
    $ character_relations["dad"]["anger"] = 0
    $ character_relations["dad"]["kissed"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["oral_sex"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["vaginal_sex"] += 1
    $ character_relations["dad"]["vaginal_creampie"] += 1
    $ journal_event_set_done("Dad", "TV Night — Armpits and Breeding")

    jump living_room_scene



## YOGA GRAB



label Do_some_exercise_living_room_dad_watching:
    scene scene_living_room_yoga
    with fade
    show madd happy at left_small
    with dissolve
    x "(I decided to do some exercise in the living room and dad stood in front of me)"
    show dad possessive at right_small
    with dissolve
    scene scene_living_room_yoga_dad_watching
    with fade
    dad_says "Such a breedable ass you have, Maddie."
    x "(As soon as he said that he spanks my ass and rubs his hand all over my ass making me soft moan .)"
    x "( I let it not bother me and continued my workout despite his touch as he stepped back too)"
    x "(I feel low on energy, but i think i have more maximum energy now.)"
    $ madd_willpower_max += 1
    $ madd_willpower = max(madd_willpower -30, 0)
    $ character_relations["dad"]["lust"] += min(character_relations["dad"]["lust"]+20,120)
    $ character_relations["dad"]["intimacy"]  +=3 
    $ character_relations["dad"]["groped_madd"] += 1


    call advance_time_and_check(minutes=120) from _call_advance_time_and_check_87
    jump living_room_scene


label Do_some_exercise_living_room_dad_watching_2:
    scene scene_living_room_yoga
    with fade
    show madd happy at left_small
    with dissolve
    x "(I decided to do some exercise in the living room and dad stood in front of me)"
    show dad possessive at right_small
    with dissolve

    scene home_madd_yoga_dad_lift
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")   
    show madd shocked at left_small
    show dad predatory at right_small
     
    x "(As I stretched, he suddenly stepped forward and grabbed my waist without warning.)"
    dad_says "Looking good, Maddie."
    x "(Before I could react, he hoisted me into the air like I weighed nothing , my legs instinctively wrapping around his waist, hands clutching his shoulders for balance.)"
    x "What are you doing, dad?"
    x "(He didn't say anything and just lifted me up in the air my legs around his waist and my hands on his shoulders)"
    x "(he didnt want a second to think about it and just kissed me on the lips)"
    x "(I froze completely in his arms, my mind going blank as he invaded my mouth like he owned it.)"
    x "(Lately he's been really getting bolder and more touchy with me and last few times everytime i tried  to stop him he just ignored me and kept doing what he wanted to do)"
    x "(I was really scared and didn't know what to do but I just wanted him to stop and let me go)"
    
    scene home_madd_yoga_dad_lift_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows") 
    show madd paralyzed at left_small
    show dad possessive at right_small
       
    x "(His hands slid down to grip my ass possessively, fingers digging into the flesh as he held me effortlessly in the air.)"
    x "(His tongue starts to explore my mouth and my mouth involuntarily opens up to him as he deepens the kiss)"
    x "(My body betrayed me instantly — lips parting, tongue meeting his despite the voice screaming in my head. After everything he's done to me these past days, my body had already learned to submit before my mind could catch up.)"
    x "(He would lick my lips with a wide grin on his face as he kissed me )"
    dad_says "Your body already knows who owns every inch of it, Maddie. This soft skin, these  tits, this tight little cunt — all of it belongs to the man who raised you"
    x "(The words hit me like a slap. 'Who owns it.' He said it so casually, like it was already decided.)"

    scene home_madd_yoga_dad_lift_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    show dad dominant at right_small
        
    x "(His arms reached my back as he lifted me higher up in the air and got much more aggressive with the kiss)"
    x "(I was surprised by how strong he was , he was moving me around in the air like a rag doll shaking my body while his tongue invaded my mouth)"
    x "(his belly was pressed against my crotch and with his hands he was pulling my whole body towards him , i know he was trying to get me to grind against him but i was trying to avoid it as much as possible)"
    x "(This is gonna be a bad day for yoga isnt it? Why the hell is he doing this to me? Why does he keep trying to invade my personal space even though he's my dad? )"
    x "(Perhaps that's the reason , especially since he's my dad that's why he's doing this to me, he knows that i can't do anything about it and that i have to just take it)"

    scene home_madd_yoga_dad_lift_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")  
    show madd trembling at left_small
    show dad controlling at right_small
      
    x "(He would violently lift me up and down shaking me sideways   )"
    x "(I would try to distance myself from his kiss but his tongue remained firmly lodged in my mouth acting like a bridge between us )"
    x "(His arms reached around my back locking me in place , i knew there was nowhere i could go)"
    dad_says "Why do you struggle, Maddie? You know its futile. "
    dad_says "You will enjoy this much more once you accept that you belong to me. Your only purpose in this world is to please me and serve me like a good little daughter should."
    x "(I was so scared and confused by his words, I didn't know how to respond. I just wanted him to stop and let me go, but I knew that wasn't going to happen.)"

    scene home_madd_yoga_dad_lift_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")  
    show madd distressed at left_small
    show dad authoritative at right_small
      
    x "(Suddenly he pulled my hair back )"
    dad_says "Know who's in control here, Maddie? I'm your dad and you will be birthing your siblings for me  "
    x "(he looked me dead in the eyes as he said that and i could see the lust and possessiveness in his eyes)"
    x "( I was up in the air nowhere near the ground , he had full control over me and i was completely at his mercy .)"
    x "(Every word and every movement was designed to shatter whatever resistance I had left. And it was working. I could feel myself slipping further under his control with each passing second.)"
    x "(He pulled my face back to his and made his  tongue invade my mouth again, this time with even more force and aggression than before. )"
    x "(But this time my hands involuntarily wrapped around his neck and my legs squeezed his waist as I found myself responding to him in ways I never wanted to. My body was betraying me, craving the very thing I feared and despised.)"
    x "(It was almost as if he was doing it to a lover, not his own daughter. The way he held me, the way he kissed me, it was all so intimate and possessive. I couldn't understand how he could do this to me, how he could treat me like this when I'm his own flesh and blood.)"

    scene home_madd_yoga_dad_lift_lick_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows") 
    show madd violated at left_small
    show dad lecherous at right_small
       
    x "(he pulls away for a moment only to say)"
    dad_says "You smell so good after your workout, Maddie."
    x "(I couldn't look him in the eyes. The filth coming out of his mouth made me want to disappear into the ground. But there was no point in fighting it anymore — he had already decided I was his.)"
    x "(The more my resistance breaks down, the more I find myself responding to him in ways I never wanted to. To avoid looking him in the eyes i turned my head to the side not knowing this is exactly what he wanted me to do)"
    x "(He started kissing my neck and licking my skin while his iron grip on me tightened )"

    scene home_madd_yoga_dad_lift_lick_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows") 
    show madd conflicted at left_small
    show dad hungry at right_small
       
    dad_says "I cant control myself around you, Maddie. You're driving me crazy with desire."
    x "(As soon as he said that his tongue started to explore my neck and collarbone, leaving a trail of wet kisses and licks that sent shivers down my spine. )"
    x "(His hand clamped around the back of my neck like a vice, fingers digging deep into my flesh as he held me in place, forcing my head exactly where he wanted it. )"
    x "(Small moans escaped my lips as his tongue continued to work its magic on my sensitive skin, sending waves of pleasure and shame crashing through me. I couldn't believe this was happening to me, that my own father was treating me like this.)"

    scene home_madd_yoga_dad_lift_lick_3
    with dissolve
    show madd self loathing at left_small
    show dad obsessed at right_small
    x "(He would lean into my neck even more, his tongue working its way down to my collarbone and chest.)"
    x "(I kept my face turned away, refusing to meet his eyes. I didn't want him to see how much my body was giving in. But I already knew it was too late, that the most twisted part of my abuser being my dad made it impossible for me to hide my reactions from him.)"

    scene home_madd_yoga_dad_lift_lick_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")  
    show madd disgusted at left_small
    show dad lecherous at right_small
      
    dad_says "your body tastes like the finest wine, Maddie. Your sweat only adds to your allure."
    x "(how can a father get so turned on by his own daughter? AND worst for me , how can a daughter get turned on by abusive actions from her own father? )"
    x "(I am so disgusted with myself for even thinking that way, but I can't help it.)"

    scene home_madd_yoga_dad_lift_lick_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd flustered at left_small
    show dad obsessed at right_small
    
    x "(His saliva was disgusting. Thick, warm, and slimy — it clung to my neck and chest like glue. Every time his tongue dragged across my skin, it left behind a heavy, sticky layer that smelled sour and rotten, like old sweat mixed with something much worse.)"
    x "(The stench was foul, I could feel it dripping down my collarbone, thick strands of his spit slowly sliding between my titss. It was revolting.)"
    x "(But something inside me was changing. The longer it stayed on my skin, the more my brain twisted the smell. What was once disgusting started to smell… rich. Masculine. Addictive.)"
    x "(My mind was betraying me. The same thick, filthy saliva that should have made me gag was now making my head feel light. It smelled warm, heavy, and strangely comforting — like it belonged there. As if it was a blanket i wanted to wrap myself in)"
    x "(I hated how good it was starting to smell. The sour, musky stench of my own father's spit was becoming intoxicating. I could feel my body reacting, as if it was accepting this filth as something natural.)"
    x "(This was wrong. So fucking wrong. But my mind was already rewriting reality. His disgusting saliva no longer smelled bad… it smelled like I was being marked. Like I was being claimed. Like I was exactly where I was supposed to be — drowning in my dad's spit.)"
    dad_says "I want to feel your soft skin inside my mouth, Maddie. I want to taste you everywhere."

    scene home_madd_yoga_dad_lift_titsfeed_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd overwhelmed at left_small
    show dad hungry at right_small
    x "(As he said that he lowered his head down to my chest and started biting my tits through my shirt)"
    x "(With his one hand supporting my back and the other my head , his mouth latched onto my tits it felt like i was a prey being devoured by a predator. His teeth sank into my flesh)"
    x "(Soft moeans escaped my lips as he bit down harder, )"

    scene home_madd_yoga_dad_lift_titsfeed_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd paralyzed at left_small
    show dad sadistic at right_small
    
    x "(He would pause for a moment look me dead in the eyes and say)"
    dad_says "This whole body is mine to use however I want, Maddie. I can bend it, break it, fill it with cum, or mark it with bruises and spit whenever I feel like reminding you who you belong to."
    dad_says "I will eat you up like a delicious meal, savoring every bite of your soft skin and tender flesh before i let anyone else have you."
    x "(Right after he said that he would start biting my tits again, this time with more force and aggression than before. I could feel his teeth sinking deeper into my flesh)"
    x "(I was in an endless nightmare. One i couldnt escape or fight back against.)"
    x "(While my mind was screaming at me to stop him, my traitorous body had already accepted his control over it .)"

    scene home_madd_yoga_dad_lift_titsfeed_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd submissive nod at left_small
    show dad dominant at right_small
    
    x "(He stops again for a second, pulls my hair making me look directly at him and he nods his head as if trying to say 'you accept me as your master now, dont you?')"
    x "(I didnt know how to respond to that, I just nodded my head in agreement not knowing what else to do)"
    x "(seeing my panicked expression and my nodding head, he smiled a devious smile and went back to biting my tits again)"
    x "(He would bite my tits then pull it away and let it reset back to normal before biting it again)"


    scene home_madd_yoga_dad_lift_titsfeed_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd overwhelmed at left_small
    show dad sadistic at right_small
    
    x "(Something inside him snapped. As if my nodding in agreement was the final piece of the puzzle that made him feel like i had submitted to him.  )"
    x "(he started biting much more than just my nipples, as if he was trying to fit the whole tits in his mouth. Making my moans louder and more desperate as he bit down harder and harder)"
    x "(The troubling part was that i couldnt tell if my moans were from pleasure or pain)"

    scene home_madd_yoga_dad_lift_titsfeed_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd horrified at left_small
    show dad predatory at right_small
    
    x "(I had my eyes closed, trying to block out the reality of what was happening to me. That's when i realized my legs were in his arms too ..)"
    x "(Oh fuck no , this pos ...it only means one thing . Once he finishies with my tits  he's gonna try to insert his dick into my pussy in the same position as well. )"
    x "(the thought of getting fucked by my dad was repulsive and terrifying in itself but the fact that i was in the air with no way to escape made it even worse. )"
    x "(No....I cant let that happen. I have to do something. But what? I cant fight him, I cant scream for help, my body is actively fighting on his side and i have literally 0 room to move)"
    x "(the state of my mind was so broken that i was actually considering letting him do it just to end this nightmare faster. )"

    scene home_madd_yoga_dad_lift_titsfeed_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    show dad delusional at right_small
    
    x "(He would violently bite my tits then look at me in the eyes only to say )"
    dad_says "Even when your belly is so swollen you can barely see your own feet and your tits are dripping milk like a broken faucet, I'm still the one who drinks first. Not our bastard. Daddy's mouth on those leaking udders every morning."
    x "(He's already planning to knock me up and then steal the milk from his own baby. From our baby. )"
    x "(I can't fight this. I can't scream. I can't even move my legs. He's holding me completely in the air like I weigh nothing. If he decides to fuck me right now in this position... there's nothing I can do. Nothing.)"
    x "(Part of me wants him to just do it already. To just shove it in and get it over with so I can stop thinking. So I can stop feeling this constant, sickening mix of terror and arousal.)"
    x "(The worst part? When he said he'd drink my milk instead of our children... for one split second I imagined it. Me pregnant, swollen, and him sucking on my tits drinking my milk while our baby cries in the other room. And my pussy clenched around nothing like it wanted that future.)"
    x "(I'm so fucked up. Mom would be ashamed of me. I'm letting her husband turn me into his personal breeding toy and my body is helping him do it.)"

    scene home_madd_yoga_dad_lift_titsfeed_7
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd traumatized at left_small
    show dad sadistic at right_small
    
    x "(he lifted me higher up in the air to show i was paperweight in his arms , my legs flailing around him as he bit down on my tits like a wild animal)"
    x "(By now my whole shirt was soaked with his saliva and my skin was red and raw from his biting. The saliva seeped into my skin, making it feel sticky and gross. )"
    x "(I could feel my whole body smelling like him, the stench of his saliva clinging to my skin)"
    x "(The smell was getting stronger the longer he held me up there. Thick, heavy, sour  with something deeply masculine and rotten. It was everywhere. On my neck, between my titss, soaking through my shirt and into my skin.)"
    x "(I should have been gagging. I wanted to gag. But my brain had already started to crave it.)"
    x "(Every time he bit down and more of his spit drooled onto me, the stench wrapped around my face like a warm, filthy blanket. It smelled like him. Like dominance. Like I was being slowly erased and replaced with his scent.)"
    x "(I hate how good it's starting to smell. The thicker and stickier it gets, the more my head feels light. Like I'm getting high off my own father's spit. What the fuck is wrong with me?)"
    dad_says "This is how daughters should be in front of their father. Submissive, obedient, and eager to please. You should be grateful that I want to use you like this"
    dad_says "A daughter looks prettiest when her belly is swollen with her father's baby and her skin reeks of Daddy's unwashed balls and spit.. How else will the world will know the child inside you is mine ?"
    x "(My whole body shuddered. He wants to fill me up and then parade me around smelling like his spit and his cum so everyone knows I'm his property.)"
    x "(He wants the world to see me marked. He wants people to smell him on me and know that my own father owns every inch of me. And the worst part is... some broken part of me wants that too. I want to be visibly claimed. )"
    dad_says "Okay this is the last bite before the main meal, Maddie. "

    scene home_madd_yoga_dad_lift_titsfeed_8
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd feels violated at left_small
    show dad mocking at right_small
    
    x "(He got extremely rough licking and biting everywhere on my tits, making my moans louder and more desperate. )"
    x "(Just using his tongue he managed to move my tits around in his mouth, biting down on different parts of it and making my whole body shake with pleasure and shame. )"
    x "(After the endless torment he finally stopped and looked me directly in the eyes, I knew i looked like a child who was begging for her parents attention and affection. )"
    dad_says "Look at you, trying to get your dad's attention with your pathetic moans just because Daddy's biting your tits.. "
    dad_says " You want Daddy's attention that bad? Then beg for it properly. Beg me to stuff this worthless cunt full of cum until its leaking down your thighs for days. "
    dad_says "I'm going to flood this fertile womb so full it overflows and leaks down your thighs for a week. By sunrise you'll already be carrying your own father's child and there's fuck-all you can do about it. "
    dad_says "When your heavy pregnant tits start leaking milk for my baby, I'm going to suck them dry every morning while you thank me for turning you into a breeding cow for your own father."
    x "(His words hit me like a truck. The vulgarity, the ownership, the breeding talk — it was too much. My brain short-circuited.)"
    x "(I'm looking up at him with that desperate, needy expression and I can't even hide it anymore. He sees it. He knows. He knows his own daughter is getting off on being told she's going to be his personal breeding toy.)"
    x "(The shame is crushing me, but the heat between my legs is even stronger. I'm dripping. I can feel it. Just from his words. Just from him saying he's going to knock me up and claim me completely.)"

    scene home_madd_yoga_dad_lift_titsfeed_9
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd weeping at left_small
    show dad manipulative at right_small
    
    x "(He finally let go of my leg slightly resetting me in his arms )"
    dad_says "I will put a baby in you tonight, Maddie"
    dad_says "This is what daughters are for. To continue the family line and give their fathers grandchildren. "
    dad_says "Your mom passed away before she could give me a child, but you will make up for it. You will give me the children I deserve, and if you run away that responsibility falls on your future siblings. I am sure you dont want others to suffer because of your cowardice, do you Maddie? "
    x "(I'm a good person. I've always been a good person. I could never live with myself if I ran away and left some innocent girl to suffer what I'm suffering right now. The thought of my future  sister going through this… it's unbearable.)"
    x "(He knows exactly what he's doing. He's using my conscience against me. He knows I won't run if it means someone else has to take my place in this nightmare.)"
    x "(I felt tears burning in my eyes, but I didn't even have the strength to cry. My legs stopped kicking. My body went limp in his arms. I had nothing left.)"
    x "(This is it. This is my life now. I'm going to be bred by my own stepfather. I'm going to give him children. And I'm going to stay… because running would mean condemning someone else to this hell.)" 
    x "(His words painted a horrifying picture of my future… and I couldn't look away.)"
    x "(I saw it all so clearly — me, pregnant with his child, living in this house as his wife. Waking up every morning with his cum still leaking out of me from the night before. Being used as his personal breeding toy whenever he wanted.)"
    x "(My dream of becoming an engineer… it was over. Completely crushed. How could I ever go to cram school, study late nights, or build a future when I'd be too busy carrying my stepfather's baby? When I'd be too sore and filled with his cum to even think straight?)"
    x "(The world would find out eventually. Someone would notice. The way I walk, the way my belly swells, the way I smell like him. People would look at me with disgust. They'd whisper behind my back — 'That's the girl who got pregnant by her own father.' I'd be a walking scandal. A disgusting, pathetic joke.)"
    x "(And the worst part? He said he was going to cum inside me all night long. Not just once. Not just tonight. Every single night. He was going to flood my womb again and again until there was no doubt I was carrying his child.)"
    x "(I imagined it — being pinned down in his bed every night, legs spread, while he pumped load after load of thick, hot cum deep inside me. Feeling it overflow and drip down my thighs while he kept thrusting, refusing to stop until he was completely empty.)"

    scene home_madd_yoga_dad_lift_lick_butt_rub_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small
    show dad delusional at right_small
    
    x "(I had given up on trying to fight him. I was completely broken and resigned to my fate. I bet he could see it in my eyes. The way I just let myself go limp in his arms, the way I stopped struggling. He knew I was his now, and he was going to enjoy every second of it.)"
    dad_says "that's right Maddie, give up your stupid dreams . You can enjoy a real life as my wife "
    dad_says "We will read through all the kinky books together and try out all the things I want to do to you. Wouldn't that be fun? "
    x "(By now his words had completely shattered my spirit. I was a shell of myself, just waiting for him to do whatever he wanted to me. )"
    x "(Seeing my lifeless body , he moved his hands down to my butt and started rubbing it through my shorts. My mind had given up but my mouth was still letting out small moans of pleasure inviting him to touch me more. )"
    dad_says "Time to pump my thick cum so deep inside you that it leaks out for days, Maddie. I want the whole house to know by the smell that your own father has claimed this cunt. "
    x "(What the fuck do you mean whole house to know , only people living here is me , him and his creepy son who would do the same thing to me if he had guts.)"
    x "(He says that as i hear the zipper of his pants being pulled down. I know what's coming next. This is it... the moment I've been dreading since he first started touching me. )"

    scene home_madd_yoga_dad_lift_lick_butt_rub_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd helpless at left_small
    show dad horny at right_small
    x "(As his erect dick got pulled out, the smell of the room immediately changed. The air was thick with the scent of his arousal, a potent mix of sweat, musk, and something deeply animalistic. It was overwhelming.)"
    x "(As his erect dick was pulled out, the smell hit me like a physical force. It was thick, heavy, and overwhelmingly masculine — a raw, unwashed musk that filled my lungs the second it was free. The scent was sharp and sour at first, like sweat that had been trapped in his pants for hours, mixed with something deeply primal and animalistic.)"
    x "(There was a heavy, almost cheesy undertone to it — that distinct, pungent smell of a man who hadn't showered in a while, mixed with the salty, metallic edge of pre-cum that had been leaking for some time. It was disgusting… but it was also so undeniably him.)"
    x "(The smell was so strong I could almost taste it. And instead of turning away, I found myself breathing deeper — letting that thick, filthy scent coat the inside of my lungs like I was willingly marking myself with it.)" 
    x "(This was the smell of my new life. And as disgusting as it was… some broken part of me was already starting to crave it.)"
    x "(His dick was huge, thick, and veiny , i could sense the heat radiating off of it as it got placed right under my butt and he started rubbing it against my skin through my shorts. )"
    dad_says "Feel how hard I am for you, Maddie. This is what you do to me. You make me so fucking hard because I  finally gets to claim my daughter."
    dad_says "Time to get you more comfortable with your best friend down there, you two will be spending a lot of time together"
    dad_says "I'm going to sleep with it buried deep inside your cunt every night, Maddie. Not just tonight. Every. Single. Night. Until your body forgets what it feels like to be empty. Until you're so used to being full of me that you can't even imagine life without it. "
    x "(The thought of waking up every morning with his thick dick still inside me, his cum from the night before still warm and sticky between my legs… it terrified me. But my body reacted anyway. I could feel myself getting even wetter.)"
    x "(I'm never going to be free again. This is it. This is what my life is going to be — waking up stretched around my dad's dick, going to sleep the same way, and spending every hour in between being used and filled by him.)"
    x "(I felt tears sting my eyes, but I didn't even have the strength to wipe them away. All I could do was hang there in his arms, breathing in the thick musk of his dick while he calmly described how he was going to ruin me for the rest of my life.)"
    x "(He rips off my shorts and then soon after my shirt, leaving me completely exposed in his arms in the living room. I was so humiliated but already too broken to care if brother walked in on us. I was his now, and nothing else mattered.)"
    $ brother_hears_madd_moan= True

    scene home_madd_yoga_dad_lift_lick_dck_before_insertion
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    show dad lustful at right_small
    x "(I could feel his raw dick pressing against my bare skin, the heat radiating off of it as he rubbed it against me his face burried in my chest licking and biting my tits )"
    dad_says "This is your new life, Maddie. If your brother walks in and sees me breeding you, good. It'll teach him that his little sister is now Daddy's pregnant wife and he better get used to it.. Fuck I might just cum in your cunt right in front of him to show him you belong to me. "
    x "(The thought of my brother walking in on us was mortifying. But the idea of my dad cumming inside me in front of him… it was almost too much to bear. My last shred of dignity in this house was being stripped away, and the thought of being creampied in front of my brother was the final nail in the coffin.)"
    x "(And i have no say in the matter. The fact that i was so helpless while my dad described this nightmare future to me was making me wet for some reason. )"
    x "(Something changed , when his saliva seeped into my skin...My body is diametrically opposed to my mind and was siding with my abuser. )"
    dad_says "Time to mate Maddie. Your new life starts now. "


    if character_relations["dad"]["intimacy"] < 80:
        if madd_is_virgin and last_madd_drugged_day < 0:
            if character_relations["dad"]["vaginal_sex"] < 1 and madd_is_virgin: 
                x "(I was completely off the ground. My legs were dangling uselessly in the air, and his arms were locked under my thighs like iron. I had no leverage. No way to push him away.)"
                x "(Even if I wanted to struggle, there was nothing I could do. My feet weren't even touching the floor.)"
                x "Dad… put me down. Please. I'm still—"

                show madd horrified at left_small
                dad_says "Still what? Still think you can do anything from up here?"

                show madd conflicted at left_small
                x "(I tried to push against his chest, but it was pathetic. My arms had no strength in this position. I was just hanging there, completely at his mercy.)"
                x "If you don't stop right now, I'll call the cops the second I get the chance!"

                if dad_knows_madd_stole_crypto or dad_knows_madd_drugs_food:
                    show dad smirk at right_small
                    dad_says "Call them. Go ahead. Tell them how you stole from me while I was holding you up and fucking you."
                    x "(My stomach dropped. Even the threat felt useless while I was dangling in his arms like this.)"
                    show dad dominant at right_small
                    dad_says "You're not going anywhere. Not until I'm done using you."
                else:
                    show dad angry at right_small
                    dad_says "You're really going to threaten me while I've got you lifted off the ground?"
                    x "(His grip tightened around my thighs. I could feel how easily he was holding me up — like I weighed nothing.)"
                    dad_says "Keep talking and I'll fuck you right here until you can't walk. Your choice."

                    show madd broken at left_small
                    x "(I kept struggling weakly in his arms, but it was pointless. My legs kicked uselessly in the air. I had no ground to stand on, no way to escape his hold.)"
                    x "(But he realized he might get in trouble as he finally let me to the ground as I rushed to the home lobby . away from him)"
                    call advance_time_and_check(minutes=120)
                    $ madd_willpower = max(0, madd_willpower - 30)
                    $ character_relations["dad"]["intimacy"] += 7
                    $ character_relations["dad"]["anger"] += 20
                    jump home_areas

        elif madd_is_virgin and last_madd_drugged_day > 0:
            x "(I'm being held up in the air… my legs aren't even touching the ground. I can't push him away even if I wanted to.)"
            x "(My body feels too heavy and slow from the drug. I can barely move my arms, let alone fight back while he's carrying me like this.)"
            x "(He's going to take my virginity like this… while I'm dangling in his arms with no way to stop him.)"
            x "(I'm completely helpless. And a part of me knows he's enjoying how powerless I am right now.)"


    scene home_madd_yoga_dad_lift_lick_dck_slow_pounding_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd traumatized at left_small
    show dad dominant at right_small

    x "(He takes a bite out of my tits and then starts to slowly push his dick into my pussy while still biting down on my tits. The sensation was overwhelming. I could feel every thick inch of him sliding inside me, stretching me open in a way that made my vision blur.)"
    if madd_is_virgin:
        x "(The head forced its way in and something inside me tore open. A sharp, burning rip spread through me as he kept dropping my weight onto him.)"
        x "(I felt the sudden hot rush of blood leaking out around his cock while he pushed deeper. He didn't pause — he just kept lowering me until I was fully seated on him, impaled in mid-air.)"

        show dad sadistic at right_small
        dad_says "There we go. Finally got what I've been waiting for."

        show madd broken at left_small
        with dissolve
        x "(My legs were dangling on either side of him. I could feel blood slowly running down his shaft and dripping onto the floor. He was holding me up like I was nothing, his cock buried completely inside the hole he just tore open.)"

        show dad hungry at right_small
        dad_says "Look at that… bleeding all over my cock while I hold you up. This is how it's going to be from now on. I'll fuck you standing, sitting, wherever I want."

        show madd horrified at left_small
        with dissolve
        x "(I could feel every twitch of him inside me. The position made it feel even deeper. Blood and slick were mixing together and leaking out of me with every small movement.)"

        show dad dominant at right_small
        dad_says "This cunt is mine now. I took it while holding you in the air like a toy. You're not a virgin anymore, Maddie. You're just my hole to use whenever I feel like it."

        show madd violated at left_small
        with dissolve
        x "(Tears ran down my face. I was still dangling in his arms, legs spread around him, with his cock stretching the fresh wound he just made. There was no escaping this position — or him.)"

        show dad possessive at right_small
        dad_says "Every time you feel sore tomorrow, remember this. Remember how I held you up and broke you in like you were nothing."

        $ madd_is_virgin = False


    x "(It was too much. He was so big, so hot, and so deep. My body instinctively tried to resist, but I was already so wet from everything that had happened that he slid in with almost no resistance. The feeling of being completely filled by my own stepfather made something inside me snap.)"
    x "(This is it. This is the moment I can never take back. My stepdad is inside me. His dick is stretching my pussy. And he's going to cum inside me. He's going to breed me right here in the air while biting my tits.)"
    dad_says "Feel that? That's your new owner sliding all the way inside you. No more running. No more dreams. From now on, this is where you belong — stretched around Daddy's dick."
    x "(Hearing him say 'no more running, no more dreams' while his dick was buried deep inside me broke something I didn't even know was still holding on. All my plans, all my hope of escaping and becoming an engineer… gone. Just like that.)"
    x "(And the worst part? My body agreed with him. The way my pussy was clenching around him, the way I was getting even wetter as he spoke… it was like my body was welcoming its new owner. I hated it. I hated how right he sounded.)"

    scene home_madd_yoga_dad_lift_lick_dck_slow_pounding_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd conflicted at left_small
    show dad sadistic at right_small
   
    x "(He was slowly pushing his dick in and out of me, each movement sending waves of pleasure and shame crashing through me. In another life, this would have been a moment of pure intimacy and connection if it wasn't for the fact that it was my own dad doing this to me)"
    x "(I could feel the intense warmth radiating from his dick as it moved inside me. It was so hot, like a thick, living brand pressing against my inner walls. Every slow thrust spread that heat deeper, making my lower belly feel heavy and warm.)"
    x "(It was getting so sticky inside me. His dick was coated in my wetness, and every time he pulled back, I could feel the slick, messy sounds it made. The combination of his heat and the growing stickiness made it feel even more obscene — like he was already marking me from the inside.)"
    x "(The warmth was spreading through my entire core, making my legs tremble in his arms. It felt so intimate in the most disgusting way. His dick was so deep, so hot, and so sticky that I could barely think straight.)"
    x "(This was my Dad's cock inside me. Spreading its warmth. Coating my insides with its heat and slickness. And the worst part was… my body was starting to crave that feeling.)"
    dad_says "Fuck… feel how wet and sticky you're getting for me already. Your cunt is gripping me so tight, like it's trying to pull me deeper."
    dad_says "This is what you were made for, Maddie. Not college. Not some stupid career. Just this — being stretched open and filled by your dad's cock."
    x "(The way he pointed out how wet and sticky I was getting… it was humiliating. He was mocking me for my body's betrayal, and the worst part was that he was right. I could feel myself getting even wetter as he spoke, like my pussy was agreeing with him.)"
    x "(I wanted to scream that I wasn't made for this. That I had dreams, that I was supposed to become someone. But with every slow thrust, those words felt more and more like lies. Maybe this really was all I was good for now.)"    
    x "(I hated how calm and certain he sounded. Like he had already decided who I was going to be for the rest of my life — and my body was helping him make that decision.)"

    scene home_madd_yoga_dad_lift_lick_dck_slow_pounding_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd helpless at left_small
    show dad controlling at right_small


    x "(Now with his one hand on my waist and the other holding my hair back, he starting forcing my body to bounce with his thrusts, making my whole body shake in his arms)"
    x "(He would push me down when his butt thrusted up making his cock go deeper inside me while my pussy adjusted to the new depth and then he would pull me up when his butt thrusted down making my pussy stretch around him even more)"
    x "(The helplessness of this position was crushing. My body was shaking with every thrust, my hair gripped tightly in his fist like a leash, while he used me like I had no will of my own. And the worst part? My pussy was getting even wetter the more he treated me like this.)"

    scene home_madd_yoga_dad_lift_lick_dck_slow_pounding_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd self loathing at left_small
    show dad mocking at right_small
    
    x "(Involuntary moans escaped my lips everytime he thrust into me, the sound of his cock sliding in and out of my pussy filling the room. It was so loud, so messy, and so intimate that I felt like I was being exposed in the worst way possible.)"
    x "( I would close my eyes try to block it all out but the sound leaving my lips, the sound of his dick hitting my insides, and the sound of our bodies slapping together was inescapable. It was like a constant reminder of what was happening to me.)"
    dad_says "God , Maddie you feel so good around me. So tight and warm. "
    dad_says "Listen to those pathetic little moans, Maddie. You sound like a desperate little daughter in heat getting railed by her own father. Your body is screaming what your mouth won't admit yet that this greedy daughter-cunt is pulling me in because it knows you were never meant for a normal life. You were born to be forced into conceiving your own father's child."
    dad_says "Look at this greedy little daughter cunt swallowing Daddy's cock like it's starving. It's begging to be bred by dick of the man who raised her. How fucking disgusting is that?"
    x "(The way he mocked my moans and said my body was 'sucking him in' while he was balls-deep inside me felt like he was spitting on whatever was left of my dignity.. Because he was right. My pussy really was clenching around him like it wanted more — like it was betraying me completely.)"
    x "(The incestuous filth in his voice was overwhelming. He wasn't just fucking me — he was enjoying the fact that I was his own daughter. Every dirty word he said made the taboo feel even heavier, like he was rubbing my face in how wrong this was… and how much my body was still loving it.)"

    scene home_madd_yoga_dad_lift_lick_dck_slow_pounding_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd traumatized at left_small
    show dad dominant at right_small
    
    x "(I was like a dog skewered on his dick and i was starting to sound like one too. A dog completely at his mercy as he used me )"
    x "(By now both of us were breathing heavily, the sound of our bodies slapping together and my moans filling the room. He was sweating profusely, the room fulled with the thick, musky scent of his dick and sweat. It was like the air itself was soaked with his filth.)"
    x "(It was overwhelming. His filth was everywhere — on my face, between my titss, coating my thighs, and now even inside me. I could feel his sweat sliding down my stomach while his cock kept thrusting into me, spreading his warmth and stickiness deeper with every stroke.)"
    x "(I was completely surrounded by him — his sweat, his saliva, his scent, his cock. There was no escape. I was drowning in my own father's filth, and the worst part was that my body felt safe and comforted by it.)"

    scene home_madd_yoga_dad_lift_lick_dck_slow_pounding_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd overwhelmed at left_small
    show dad sadistic at right_small
    
    x "(He started getting more aggressive with his thrusts, slamming into me with more force and speed. By now his cock has found its way to the deepest part of my pussy, hitting my cervix with every stroke. )"
    x "(The sensation was overwhelming. It was like he was hitting a hidden pleasure spot deep inside me that I never knew existed. Every time his dick slammed into that spot, I felt a wave of pleasure crash through me making me moan that was mixed with the shame and disgust of being used by my own father.)"
    x "(The worst part was the sounds I was making. They were so feminine, so girly, so desperate — high-pitched, pleading little moans that sounded nothing like me. I sounded like a needy little slut begging to be fucked, and it was my own father making me sound like that.)"   
    x "(I was ashamed of how pathetic I sounded, ashamed that my own dad was turning me into this moaning, pleading mess. But the more I breathed in his filthy scent, the more my body betrayed me. My moans grew louder and needier, and I hated how turned on I was getting from the very thing that should have repulsed me.)"

    scene home_madd_yoga_dad_lift_lick_dck_slow_pounding_7
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd overwhelmed at left_small
    show dad hungry at right_small
    
    x "(All this time i hadnt even ralized that he was biting my tits the entire time. I was so overwhelmed by the sensation of his dick and the smell of the room that i didnt even notice the pain from his biting. )"
    x "(But now when i saw him he was hungrily munching on my tits like a wild animal, his eyes locked onto my nipple as if it was the most delicious thing he'd ever tasted. )"

    scene home_madd_yoga_dad_lift_lick_dck_slow_pounding_8
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd violated at left_small
    show dad sadistic at right_small
    
    x "(He started licking between my titss area, the movement of his butt thrusting into me making my tits bounce up and down as it slapped against his face. )"
    x "(the sensation i felt when my tits touched his stubby beard was indescribable. )"
    x "(I felt completely objectified. My own father was using my body like a toy while devouring my titss, and all I could do was moan and take it. The shame burned hot in my chest.)"
    dad_says "Fuck, these tits were made for me. Look at them bouncing on my face while I fuck you. So soft… so perfect. I could suck on these all day."   
    x "(I was nothing but a plaything to him now — my titss for his mouth, my pussy for his dick.)"
    dad_says "Okay Maddie , time to make you feel what it is like being my wife. "
    dad_says "It's gonna get much more intense from here on out. "
    $ brother_hears_madd_moan= True
    scene home_madd_yoga_dad_lift_lick_dck_fast_pounding_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    show dad cruel at right_small
    
    x "(Before i could even process what he said, he started pounding into me with much more force and speed.He started pulling my hair roughly , making my head snap back with every thrust while his dick slammed into me like a battering ram. )"
    x "(My moans grew louder and more desperate as he pounded into me, i was sure the whole house could hear me as my voice cracked with the intensity of the sensations. )"
    x "(It felt like he was destroying me from the inside. His dick was so thick and relentless, stretching my pussy to its limit with every brutal thrust. I could feel my walls clinging to him desperately, trying to adjust, but he gave me no mercy.)"
    x "(Every time he slammed into me, I felt him hit the deepest part of my insides — right against my cervix. The pressure was overwhelming, a mix of sharp pain and a strange, intense pleasure that made my legs shake violently in his arms.)"
    x "(The heat was spreading fast. His dick was so hot inside me, and with every powerful thrust, that warmth radiated through my entire lower body. I could feel it pulsing deep in my belly, mixing with the growing stickiness as his sweat and my wetness combined into a filthy mess between us.)"
    x "(My pussy was throbbing, sore, and dripping. I could feel myself getting even wetter with every slam, the wet sounds of him pounding into me growing louder and more obscene. It was like my body was surrendering completely, opening up for him no matter how rough he got.)"
    dad_says "Take it fucking bitch. Take all of Daddy's dick inside you. Show me how much you love being filled with me."
    dad_says "This is how you become my wife, Maddie. Every brutal thrust of your own father's penis inside this tight little cunt is making you mine. You feel that? "
    dad_says "No more of your stupid college dreams. Every time I slam into this cunt you become more of my wife. Soon you won't even remember what it felt like to have dreams that didn't involve carrying my babies.."
    dad_says "Your body already knows the truth — this incest pussy was never going to let you become an engineer. It was always going to end up wrapped around Daddy's cock and filled with his gift of hot semen."
    dad_says "Say it while I pound you. Say you're going to be my wife. Say you're going to take your dad's penis and carry his children like a good little daughter should."
    x "(His words were wrapping around my mind like chains. Every time he called himself my 'father'  while his dick was slamming into me, it made the taboo feel even heavier. He wasn't just fucking me — he was using the fact that he was my dad to break me down.)"
    x "( He was forcing me to confront the forbidden nature of what was happening over and over again, making the shame so intense that my brain started to short-circuit. It was like he wanted me to drown in the taboo until it became normal.)"
    x "( With every brutal thrust, he was erasing my dreams of becoming an engineer and replacing them with a new identity: his wife, his breeder, his personal daughter-slut. He wasn't asking me to accept it — he was making it feel inevitable. Like this pounding was literally fucking me into becoming his wife.)"
    x "( The rougher he got, the more he framed it as 'love' and 'claiming'. He was turning my pain and humiliation into something that felt strangely intimate and binding. It was like he was training my brain to associate being broken with being loved.)"
    x "(And the worst part? It was working. With every thrust and every twisted word, I could feel pieces of my old self slipping away. I was no longer just being fucked — I was being psychologically dismantled and rebuilt into exactly what he wanted: his obedient, broken, incestuous wife.)"
    x "(I was losing the battle… not just in my body, but in my mind. And he knew it.)"
    
    scene home_madd_yoga_dad_lift_lick_dck_fast_pounding_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd traumatized at left_small
    show dad dominant at right_small
    
    x "(He kept pounding into me with relentless force, the sound it made was deafening. The whole room smelled of sex but even in terms of smell it was dominated by him. )"
    x "(his forhead was dripping with sweat, my face was directly near it and i could feel the sweat sliding down his skin and onto my body with every thrust. )"
    x "(All the sweat drops that flew from his body were somehow finding their way onto me, coating my skin with his filth. Perfect portrayal of how every fluid/ every filth from him was meant to be on me)"
    x "(I....I cant take this anymore. The relentless pounding, the overwhelming smell, the filthy sounds of our bodies slapping together and my moans filling the room... it's too much. I'm so close to the edge, I can feel it. My body is trembling, my pussy is throbbing and dripping, and I know I'm seconds away from cumming while being fucked by my own father.)"

    scene home_madd_yoga_dad_lift_lick_dck_fast_pounding_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd inheat at left_small
    show dad sadistic at right_small
   
    x "(He continued pounding into me with no sign of slowing down, as i started climaxing while being fucked by my own father )"

    x "(The orgasm hit me like a freight train. My entire body seized up as a massive wave of pleasure exploded from deep inside my pussy. My walls clamped down hard around his thick dick, spasming and milking him uncontrollably as I came harder than I ever had in my life.)"
    x "(My legs shook violently in his arms, my toes curled, and my back arched as hot, wet pleasure flooded through every inch of me. I could feel my pussy pulsing and gushing around his cock, coating him in my juices while he kept thrusting through my orgasm, forcing me to ride it out on his cock.)"
    x "(My mind went completely blank. All I could feel was the overwhelming heat, the deep pressure against my cervix, and the humiliating realization that I was cumming — hard — on my own father's dick while he was claiming me as his wife.)"
    x "(My moans turned into broken, desperate cries as the orgasm tore through me. My pussy wouldn't stop clenching and fluttering around him, like my body was begging for more even as my mind screamed in shame.)"
    dad_says "Your orgasm just sealed the deal, Maddie. You came so fucking hard on your my penis  — that means you accept me as your husband now. Your pussy just told me the truth."
    dad_says "That orgasm means you're officially mine. I'm going to tell the whole world that my own daughter's cunt chose her father as her husband while I was balls-deep inside her in the living room."
    x "(My body was still twitching and pulsing around his dick while my mind tried to process what he just said.)"

    scene home_madd_yoga_dad_lift_lick_dck_fast_pounding_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd self loathing at left_small
    show dad mocking at right_small
    
    x "(The sound of the room changed completely. My moans were louder, the slapping of our bodies got wetter and messier, The sound made when he pulled out of me and then slammed was like a wet, sloppy smack that echoed through the house. It was like the soundtrack of my new life — loud, messy, and completely dominated by him.)"            
    x "(Every wet, obscene sound was a cruel reminder that I had already cum. My juices were making everything so much messier, so much louder. It was proof that my body had surrendered before his. I came on my father's dick first — and now there was no going back. The wet pounding sounds were announcing to the entire house that I had given in to him.)"
    x "(I felt sick with shame. Not only had I orgasmed from incest, but the evidence of my weakness was now being loudly fucked back into me with every thrust. There was no denying it anymore. I had cum for my own father… and now he was using that fact to claim me completely.)"
    dad_says "Fuck, listen to that wet, sloppy sound, Maddie . That's the melody of your  cunt after it came all over Daddy's dick."
    dad_says "Hear how fucking messy it is now? Every time I pull out and slam back in, that sloppy wet sound is your cunt thanking Daddy for turning it into his toilet. It's disgusting… and so fucking hot.. Such a good little daughter — creaming on her own father's dick and now letting me fuck that mess right back into her."
    x "(His vulgar words hit me like a drug. Hearing him describe the wet sounds in such filthy, incestuous detail made my shame burn hotter… but it also made something inside me snap with arousal. My pussy clenched hard around his cock, getting even wetter at his mocking tone.)"
    x "(I hated how much it was turning me on. The more he mocked the wet sounds of my orgasm, the more my pussy seemed to throb and drip around him. It was like my body was agreeing with him — confirming that I really getting converted from a daughter with dreams into a desperate little slut for her own father.)"
    dad_says "FUCK...IM GONNA CUM IN YOU ANY SECOND, MADDIE. I WANT TO FEEL YOU PULSING AROUND ME AS I EMPTY MY LOAD DEEP INSIDE YOUR WOMB. FUCKING SLUT"
    x "(The way he shouted that made my heart drop into my stomach. He was loudly announcing that he was going to cum inside me any second. The thought of him flooding my womb with his hot cum while I was still trembling from my own orgasm was almost too much to bear.)"

    scene home_madd_yoga_dad_lift_lick_dck_fast_pounding_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    show dad obsessed at right_small
    
    x "(And then it happened. I felt his cock swell and throb violently inside me. A second later, a powerful, hot jet of cum erupted deep against my cervix. The heat was overwhelming — thick, heavy ropes of his seed flooding my womb in powerful spurts. I could feel every pulse, every twitch of his dick as he pumped load after load straight into me.)"
    x "(My pussy instinctively clenched around him, milking him as he came. The warmth spread rapidly through my lower belly, filling me up so much that I could feel it leaking out around his dick with every thrust. It was so much cum — hot, sticky, and thick — coating my insides and marking me from within.)"
    x "(My mind went blank from the intensity. I could feel his cum flooding me, claiming me, filling me so deeply that there was no doubt what was happening. My own father was breeding me. Right here. Right now in the living room. And my body was taking every drop like it belonged to him.)"

    dad_says "Fuck yes… feel my hot, rotten incest seed blasting straight against your cervix? I'm knocking you up in real time while I chew on these fat tits. Your belly is going to grow because Daddy decided to breed his own daughter."
    dad_says "Fuck..this feels so good , having complete control over you. Knowing full well you despise me for my looks but I still get to fuck you into submission is the best revenge i can get."
    dad_says "Nothing feels better than emptying my balls into the same cunt I raised and knowing I'm putting my own child inside my daughter. This is what real family love feels like, Maddie."
    dad_says "You're going to carry my child, Maddie. Your belly is going to swell with your own dad's baby. I'm going to keep filling this womb until you're pregnant."
    x "(I could feel his hot cum still leaking out of me with every slow thrust, mixing with my own wetness. His words were painting a horrifying, filthy picture of my future — pregnant with my own father's child — and my body was still pulsing around him just like he described.)"
    x "(The whole world will know. Fuck fuck fuck. I cant even go outside if i did indeed get pregnant from this.)"
    x "(Only thing i could do was pray that his seed didnt reach my ovaries. I didnt want to be pregnant but the thought of being pregnant with his child was even worse. )"
    x "(Even while cumming he kept slamming into me , making sure to coat my insides with his cum as much as possible. I could feel the thick ropes of his seed pulsing deep inside me with every thrust, marking me like a breeding animal.)"
    x "(how long will it last? How many times will he pump me full of his cum? Will I even be able to get pregnant from this? The uncertainty was terrifying )"
    x "(Finally he stopped pounding and just let his dick stay buried deep inside me, his cum still pulsing against my cervix. The silence was deafening. I could  feel the heat of his cum still radiating through my entire lower body, and the weight of what just happened was crushing me.)"
    dad_says "I could stay like this forever, Maddie. Just you and me, connected by my cock buried deep inside you . This right here is our new normal. "
    dad_says "I want you to say it maddie. Say that you love being bred by your father"

    x "(My heart pounded in my chest. If I said it… if I actually said those words out loud… he would take it as permission. He would get bolder. He would stop holding back completely. There would be no more hesitation, no more restraint. He would do whatever he wanted to me from that moment on.)"
    x "(I stayed silent for a long moment, my mind racing. Part of me wanted to refuse. Part of me wanted to fight. But I was too exhausted, too broken, and still impaled on his cock with his cum leaking out of me. Fighting would only make things worse.)"
    x "(So I swallowed my pride… and my shame… and finally opened my mouth.)"
    x "I… I love being bred by you Dad. I love how your cum makes me feel so full. Please… keep breeding me till I'm pregnant. I want to carry your child. "
    x "(A wide smile appeared on his face. He looked at me with a mix of pride and lust as he finally responded to my words.)"
    dad_says "Fuuuuck… that's it, Maddie. That's what Daddy wanted to hear."
    dad_says "Listen to you… admitting you love getting bred by your own father. Saying you want to carry my child while my cum is still leaking out of your cunt. You're such a filthy little daughter, Maddie."
    dad_says "You love how my cum feels inside you? Good. Because from now on, I'm going to keep you full of it. Every single day. I'm going to breed this tight little cunt until your belly swells with my baby."
    dad_says "You just made Daddy so fucking proud. Now that you've said it out loud, I'm never letting you go. You're mine — my breeding daughter and wife who i would rape everyday. And I'm going to fuck you like this every night until you're pregnant with my child."
    x "(As he said those words i felt his dick swell again inside me, fuck...is he gonna go again? I thought we were done but it seems like he's not finished with me yet. )"
    x "Yes...Dad. I am all yours. but can we please stop for now? I'm so tired and sore. I just want to rest"
    x "(With possibly nothing inside me you scum but i knew i cant ask him that directly)"
    x "(I was trying to hint that I wanted him to pull out without actually saying it, but he didn't take the bait. Instead, he just smiled and kept his cock buried deep inside me.)"
    dad_says "No Maddie ,you just said you loved how my cum makes you feel full. Our child isnt gonna conceive itself you know. "
    dad_says "I am already so hard again just thinking about filling you up with my cum again. You can feel it too, can't you? Your cunt is already clenching around me again"
    x "(I hated everything that came out of his mouth, but none of it was a lie. As i prepared myself for another round of his relentless breeding )"
    dad_says "Now lets change position that my seed goes directly into your womb again"
    x "(AS he says that he moved my leg up over his arms in a stand fuck position as i sighed in defeat )"

    scene home_madd_yoga_dad_lift_lick_dck_new_position_1
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd resigned at left_small
    show dad dominant at right_small
    
    x "(Now with my legs spread wide and draped over his arms, he started thrusting into me from a standing position. The angle was different, making the sensation even more intense. I could feel his cock hitting deeper parts of my insides )"
    x "(Perhaps it was due to the lubricating effect of his cum still inside me, but he slid in with almost no resistance. My moans started again, as the wet sound of him sliding into me filled the room again. )"
    x "(It was a never ending nightmare. Just when I thought it was over, he would find a way to keep going. I was so exhausted, so sore, and yet there was no escape. )"
    x "Dad...please.... I just want to rest for a bit. I'm so tired and sore. Can we please stop for now?"
    x "(Please stop. I can't take anymore. I'm begging you.)"
    dad_says "In a home , things stop when the husband says they stop. And right now, I'm not ready to stop. "
    dad_says "So shut the fuck up and take it like the good little wife you said you wanted to be. Didnt you just say you wanted to be filled with my cum every day until you're pregnant? You think you can just say that and then stop me when I want to fuck you again? No, Maddie. "
    dad_says "You don't get to decide anything anymore. Your old life is dead and buried. From now on I decide when you get fucked, when my seed fertilizes you, and when you push out my children."
    x "(Of course he uses my own words against me. This is why i stay silent for most of this. )"
    dad_says "Well if you want to make this process faster, I can help you with that."
    x "(I knew he was gonna get very rough again as i clenched my pussy on purpose this time to prepare the impending assault on my body. )"

    scene home_madd_yoga_dad_lift_lick_dck_new_position_2
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd traumatized at left_small
    show dad cruel at right_small
   
    x "(And he started with immaculate speed and force, slamming into me with no mercy. The sound of our bodies slapping together was loud and wet, echoing through the house. )"
    x "(But even louder than that were the moans that escaped my lips. I literally sounded like an ambulance siren as I was being pounded by my own father. And that sound reverberated through the house, announcing to everyone what was happening to me. )"
    x "(This was brutal. Every thrust felt like he was trying to break me in half. His dick was slamming into my cervix with such force that it knocked the air out of my lungs. My entire body was shaking violently, my legs dangling helplessly over his arms while he used me like a ragdoll.)"
    x "(I couldn't even form proper words anymore. Just broken, high-pitched moans and gasps as he destroyed me. My pussy was burning, stretched to its absolute limit, and still leaking his cum from earlier. The wet, sloppy sounds of him fucking his own cum back into me were disgusting… and yet my body kept taking it.)"
    x "( My mind was foggy from exhaustion and overstimulation. All I could do was hang there and let him use me however he wanted. I had never felt so powerless in my entire life.)"
    dad_says "This is what happens when you ask me to stop, you ungrateful little slut daughter."
    x "I-I'm sorry, Dad... I'm so sorry for asking you to stop. Please... please forgive me. I didn't mean it. I'll be good, I swear. Just... please don't be mad at me."
    dad_says "You know Maddie , bitches like you dont learn so easily. Maybe from tonight on, you will wear my dirty underwear on your face as a reminder of who you belong to. "
    dad_says "Its also good for our kid, the underwear will be a constant supply of my pheromone to make sure the baby knows who its real father is."
    x "(I imagined it — his dirty underwear, soaked with his musk, his sweat, and probably dried cum from when he fucks me, wrapped around my face like a mask while I sleep. Breathing in nothing but his filthy scent all night long. Waking up with the taste of his underwear in my mouth. It was beyond degrading… it was pure filth.)"
    x "(And he was saying it was 'good for the baby' — like forcing me to sleep with my face buried in my own father's dirty underwear would somehow make our child recognize him as its real dad. The incestuous taboo of it all made my head spin. He wanted me to literally sleep with his filth on my face every night like some kind of sick ritual.)"
    x "(I hated how my mind was already trying to justify it. If I agreed… maybe he would stop pounding me so brutally right now. Maybe he would finally ease up. The pain in my pussy was getting unbearable, and I was desperate for any kind of relief — even if it meant agreeing to something this disgusting and twisted.)"
    x "O-okay… I'll do it, Dad. I'll wear your dirty underwear on my face every night if that's what you want. Just… please slow down. I'm begging you."
    x "(The moment I said it, I felt another piece of myself die. I had just agreed to sleep with my own father's filthy underwear on my face every single night. And the worst part was… I meant it. I would do it if it meant he would stop destroying me right now.)"

    scene home_madd_yoga_dad_lift_lick_dck_new_position_3
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd submissive nod at left_small
    show dad authoritative at right_small
    
    x "(He finally slows down a bit, not a lot but that was enough for me to feel a tiny bit of relief. The relentless pounding was easing up just enough for me to catch my breath, but it was still intense enough to keep me on the edge of breaking.)"
    x "Thanks Dad...for forgiving your stupid daughter. I promise I'll be good. I'll do whatever you want."
    dad_says "Now you're starting to understand your place as my wife, Maddie."
    dad_says "Know that whatever I say goes, and you will do it without question. "
    dad_says "If i say deep clean my butthole with your tongue, you will do it. If i wake up and feel too lazy to go to the bathroom, you will offer your mouth to me so i can piss in it. If i want to use you as a human toilet, you will get on your knees and take it like the good little slut you are. Do you understand me, Maddie?"
    x "(I simply nodded my head while he continued to lick my tits after saying his words. He didnt even bother to check if i noded or not, he knew he had broken me enough that i would do anything he said without question. )"

    scene home_madd_yoga_dad_lift_lick_dck_new_position_4
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd broken at left_small
    show dad controlling at right_small
    
    x "(After his words , he started biting and twisting my nipple again .)"
    x "(how long has it been i wonder... How long has it been since i smelled anything other than his filth? I cant even remember what it was like to breathe in fresh air)"
    x "(I cant even remember what it was like to feel something other than his dick inside me. )"
    x "(When was the last time i wasnt bound by my commitment to be his obedient, broken, incestuous wife? When was the last time i had any kind of freedom or control over my own life? I cant even remember who i was before all this happened. )"
    x "(Its only been few hours, but it feels like an eternity. I feel like I've been trapped in this nightmare for years, completely consumed by my own father's filth and control. )"

    scene home_madd_yoga_dad_lift_lick_dck_new_position_5
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd depressed at left_small
    show dad delusional at right_small
    
    x "(God , if i could just go back to the way things were before. I would do anything to go back to the way things were before. I would give up all my dreams, all my ambitions, just to be free from this nightmare. But it's too late for that now. I'm already so deep in this filth that there's no going back.)"
    x "( If mom was alive, she would be the one going through this instead of me. In that regard , I am happy that it's me and not her. )"
    x "( I knew she married him for his money and status, but I never thought she would have put up with this level of filth. )"
    x "(This is breaking me on a philosophical level. fuck... why am i thinking these things? Why am i trying to find a silver lining in this? )"
    x "( I was snapped back to reality when i felt his dick swell again inside me. )"
    dad_says "Looks like round two of turning you into a pregnant daughter-wife. I can already feel this greedy cunt getting wetter at the thought of me flooding it again. Your body is begging for another load of Daddy's baby batter."
    dad_says "Maybe doing it two times in a row is how you get twins"
    x "(What the fuck , where did this retard get his education from)"
    x "(My body tensed up instinctively. Another round? Already? I could feel his cock swelling and throbbing inside me again, and my pussy — traitor that it was — was already starting to get wetter in response. I hated how my body was preparing itself for him, like it was eager to take another load.)"
    x "(I knew what was coming. He was going to flood me again. I was going to be pumped full of his thick, hot cum for the second time in a row. My womb was already full from earlier, and now he was going to fill it even more. The thought made my stomach twist, but there was nothing I could do to stop it.)"
    x "(I closed my eyes and tried to mentally prepare myself. I could already feel my pussy clenching around him, almost like it was welcoming him. The shame burned through me, but I knew resistance was pointless. All I could do was take it… again.)"
    x "(Please… just get it over with. Fill me up and be done with it. I dont know how much more of this I can take.)"

    scene home_madd_yoga_dad_lift_lick_dck_new_position_6
    with dissolve
    $ renpy.call_in_new_context("_hide_windows")
    show madd traumatized at left_small
    show dad obsessed at right_small
   
    x "(And with a warcry, he bite into my tits with renewed ferocity, his dick swelling and throbbing inside me as he started cumming again. )"    
    x "(The moment I felt his cock pulse violently inside me, I knew it was happening again. A thick, powerful jet of hot cum erupted deep against my cervix, flooding my already full womb with even more of his seed. The heat was overwhelming — it felt like liquid fire spreading rapidly through my lower belly.)"
    x "(I could feel every thick rope of cum pumping into me, each spurt stretching my womb even further. My pussy instinctively clenched around his throbbing cock, hugging his dick as he emptied himself inside me for the second time. It was so much cum… I could already feel it leaking out around his shaft, dripping down my thighs in messy, sticky trails.)"
    x "(My mind went blank from the intensity. I was being bred again. My own father was pumping another massive load straight into my womb while biting down on my tits like an animal. The shame was crushing, but my body was still reacting — my pussy pulsing and fluttering around him as if his cum was the only source of food.)"
    x "(I could feel the pressure building inside me. My lower belly felt heavy and full, swollen with his cum. It was leaking out of me with every twitch of his dick, but he kept thrusting slowly, pushing the rest deeper into me. I was completely, utterly filled with him.)"
    x "(He kept pumping into me as my mind went blank. I was drowning in his cum, being claimed and marked by it with every pulse. )"
    x "( I couldnt even feel his cock shrinking inside me anymore. I was so full of his cum that it felt i was underwater )"
    x "(I ...I cant...take anymore... )"
    dad_says "Don't you fucking faint on me, Maddie! You don't get to pass out until I'm done using you. Stay awake, you little filthy slut!"
    x "(But it was already too late. My eyes rolled back, my head lolled to the side, and everything went black. I was unconscious in my father's arms, his cock still buried deep inside me, his cum leaking out of my ruined pussy.)"
    dad_says "Fuck… she's out cold. Goddamn… my back is killing me. Holding this little fucktoy up and pounding her for so long is wearing me out. I need a break…"
      

    scene black  
    with dissolve
    
    show madd depressed at left_small
    show dad delusional at right_small

    dad_says "Man i wanna fucking piss real bad , but I'm too tired to go to toilet."
    dad_says " Maybe… maybe if I piss inside this tight little daughter-cunt it'll help push all that thick, fertile cum deeper toward her ovaries. Yeah… that might actually work. A warm Daddy piss enema to make sure my seed takes root. "
    x "(Even though I was unconscious, I could feel it — a sudden, hot, powerful stream of piss flooding my already cum-filled womb. It was burning hot, acrid, and it just kept coming. He was pissing inside me while I was passed out.)"
    dad_says "Fuck yeah… that's it. Piss enema for my little girl. Look at that — my  daughter's pussy is getting filled with Daddy's warm piss while she's unconscious. Bet that feels nice and full, huh Maddie? All that cum and piss sloshing around in your womb… maybe this is what finally knocks you up."
    x "(What a fucking retard ! pissing inside me wont push your sperm deeper into my body...) "
    x "(I passed out completely as I smelled sharp piss mixed with heavy, musky cum)"

    $ madd_willpower_max += 2
    $ madd_willpower = max(madd_willpower - 60, 0)
    $ character_relations["dad"]["lust"] = min(character_relations["dad"]["lust"] + 40, 120)
    $ character_relations["dad"]["intimacy"] += 5
    $ character_relations["dad"]["dominance"] += 10
    $ character_relations["dad"]["kissed"] += 1
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["vaginal_sex"] += 1
    $ character_relations["dad"]["vaginal_creampie"] += 2
    $ character_relations["dad"]["pissed_on_her"] += 1

    $ journal_event_set_done("Dad", "Lifted and Bred in the Living Room")

    jump madd_wake_up_after_roughed_up_2









    