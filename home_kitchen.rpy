# ════════════════════════════════════════════
#  Cuisine - Base
# ════════════════════════════════════════════

label kitchen_scene:
     python:
        if game_time.is_morning():
            home_kitchen = "kitchenmor"
        elif game_time.is_afternoon():
            home_kitchen = "kitchenaft"
        elif game_time.is_evening():
            home_kitchen = "kitcheneve"
        else:  # night
            home_kitchen = "kitchennig"

     scene expression home_kitchen
     with fade
     "Vous êtes dans la cuisine. L'arôme des ingrédients frais embaume l'air."

     $ journal_event_show("Brother", "Kitchen Ambush (Miss Event)")
     $ journal_event_show("Dad", "Kitchen Ambush (Miss Event)")


     menu:
         "Cuisiner":
                if cooked_today:
                    x "J'ai déjà cuisiné une fois aujourd'hui. Je devrais me reposer et préparer à nouveau demain."
                    call advance_time_and_check(minutes=5) from _call_advance_time_and_check_70
                    jump kitchen_scene
                else:
                    if madd_willpower < 20:
                        x "Je n'ai pas la force de cuisiner maintenant. Je devrais d'abord me reposer."
                        call advance_time_and_check(minutes=5) from _call_advance_time_and_check_71
                        jump kitchen_scene
                    $ cooked_today = True
                    jump kitchen_cook_minigame
        
         "Manger":
                if  meal_prepared>=1:
                    call advance_time_and_check(minutes=30) from _call_advance_time_and_check_72
                    x "J'ai mangé un repas préparé plus tôt et j'ai repris de l'énergie."
                    $ madd_willpower = min(madd_willpower + 50, madd_willpower_max)
                    $ meal_prepared -= 1
                else:
                    x "Je n'ai pas de repas préparé à manger pour le moment."
                jump kitchen_scene
        
         "Cuisiner pour la famille" if game_time.hour >= 18 and game_time.hour < 20:
            jump cooking_for_family
        
         "Eat with family" if game_time.hour >= 20 and game_time.hour < 22 and family_meal_prepared >= 1:
            jump kitchen_eating_with_family
         "Eat with family (No meal prepared)" if game_time.hour >= 20 and game_time.hour < 22 and family_meal_prepared < 1:
            show dad angry at right_small
            dad_says "Fuck outta here, you didnt make this food I paid for it."
            dad_says "If you cook it then you can eat with us."
            jump kitchen_scene
        
         "Retourner au lobby":
            jump home_areas


label cooking_complete:

    $ kitchen_scene = "home_kitchen_morning" if game_time.is_morning() else ("home_kitchen_afternoon" if game_time.is_afternoon() else ("home_kitchen_evening" if game_time.is_evening() else "home_kitchen_night"))
    scene expression kitchen_scene
    with fade
    
    $madd_willpower = max(madd_willpower -20 , 0)

    "Vous avez réussi à cuisiner le repas !"
    show madd happy at left_small
    with dissolve
    p "Tout s'est déroulé à merveille. Le timing, la technique, les saveurs…"
    p "C'est exactement ce que je devais faire. Je suis fière de moi."

    show madd hopeful at left_small
    with dissolve
    p "Je peux maintenant manger le repas que j'ai préparé pour reprendre des forces."
    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_73
    $ meal_prepared += 1
    jump kitchen_scene


label kitchen_cook_minigame:

    scene scene_kitchen_minigame_madd_standing
    with fade
    
    p "Je me mets à cuisiner, l'esprit vagabondant tandis que je coupe les légumes et prépare le repas."
    p "Il est difficile de se concentrer sur autre chose ces temps-ci."
    p "Les événements qui se déroulent chez moi continuent de me hanter, malgré tous mes efforts pour les chasser."
    
    $ random_event = renpy.random.random()
    
    # Afternoon: miss_event_dad with 50% probability
    if game_time.is_afternoon() and character_relations["dad"]["lust"] >= 40:
        if random_event < 0.6:
            call miss_event_dad from _call_miss_event_dad_cooking
        else:
            jump cooking_complete
    # Evening: miss_event_dad or miss_event_brother with 0.33 probability each
    elif game_time.is_evening() and character_relations["dad"]["lust"] >= 40 and character_relations["brother"]["lust"] >= 40:
        if random_event < 0.33:
            call miss_event_dad from _call_miss_event_dad_cooking_evening
        elif random_event < 0.6:
            call miss_event_brother from _call_miss_event_brother_cooking_evening
        else:
            jump cooking_complete
    # Night: miss_event_brother with 50% probability
    elif game_time.is_night() and character_relations["brother"]["lust"] >= 40:
        if random_event < 0.6:
            call miss_event_brother from _call_miss_event_brother_cooking
        else:
            jump cooking_complete
    else:
        jump cooking_complete
    
    jump cooking_complete



label kitchen_eating_with_family:
    scene scene_kitchen_eating_with_family
    with fade

    show madd uncertain at left_small
    with dissolve
    x "(I sat down to eat with my step brother and step father, trying to enjoy the meal and the company.)"
    x "(I was sitting in between them, all three of us were eating in silence. No one was talking, the atmosphere was tense and uncomfortable.)"
    
    # Check conditions for different eating scenarios
    $ random_value = renpy.random.random()
    
    if character_relations["dad"]["lust"] >= 70 and dad_sees_brother_madd_together and not(brother_sees_madd_blow_dad):
        # Dad caught them together and has high lust
        if random_value < 0.6:
            jump kitchen_eating_with_family_dad_caught_madd_playing_with_brother_aftermath
        else:
            jump kitchen_eating_with_family_normal_eat
    elif character_relations["dad"]["lust"] >= 70 and dad_sees_brother_madd_together and brother_sees_madd_blow_dad:
        if random_value < 0.2:
            jump kitchen_eating_with_family_dad_caught_madd_playing_with_brother_aftermath
        else:
            jump kitchen_eating_with_family_normal_eat

    else:
        # Normal scenarios
        if random_value < 0.1:
            jump kitchen_eating_with_family_bad_food
        else:
            jump kitchen_eating_with_family_normal_eat


label kitchen_eating_with_family_dad_caught_madd_playing_with_brother_aftermath:
    scene scene_kitchen_eating_with_family
    with fade

    show madd uncertain at left_small
    with dissolve
    x "(Suddenly, my step father broke the silence.)"
    
    show dad smirk at right_small
    with dissolve
    dad_says "So, Adam. I see you like playing with your sister, don't you?"
    

    show madd shocked at left_small
    with dissolve
    x "(I was taken aback by his comment, not sure how to respond. My fork stops mid-air.)"
    
    hide dad

    show brother amused at right_small
    with dissolve
    brother_says "What are you talking about ?"
    
    show madd distressed at left_small
    with dissolve
    x "(I let him answer on my behalf, not wanting to cause any more tension at the table.)"
    
    scene scene_kitchen_eating_with_family_dad_angry_stay_away_from_madd
    with fade
    
    show madd anxious at left_small
    with dissolve
    show dad angry at right_small
    with dissolve
    dad_says"I've seen what you did to her in the living room " 
    
    show madd trembling at left_small
    with dissolve
    x "(He slams his hand on the table, his voice rising with anger.)"
    
    show madd horrified at left_small
    with dissolve
    dad_says "She's my wife !"
    
    show madd violated at left_small
    with dissolve
    x "(His hand now landed on my head. Claiming me as his own.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I was just looking down at my plate, trying to avoid eye contact with him.)"
    
    show madd anxious at left_small
    with dissolve
    dad_says " STay away from her , you got that ?"
    
    show madd paralyzed at left_small
    with dissolve
    x "(He was pissed off, his face red with rage. I could feel the tension in the room rising.)"
    x "(Step Brother didnt say anything, i didnt dare raise my head so i dont know if he was angry or not but i am sure he must be pissed.)"
    scene scene_kitchen_eating_with_family_dad_only
    with fade 
    
    show madd uncertain at left_small
    with dissolve
    show dad smirk at right_small
    with dissolve
    dad_says "This tastes good, wife!"
    
    show madd paralyzed at left_small
    with dissolve
    x "(As soon as he said that , he put his hands on my neck and kissed me on the lips, claiming me as his own in front of my step brother.)"
    
    show madd violated at left_small
    with dissolve
    x "(I was shocked and disgusted by his actions, but I couldn't do anything to stop him. I just sat there, frozen in place as his tongue invaded my mouth.)"
    x "( there was still chewed bread in his mouth , that he poured into my mouth as he kissed me , i could feel the pieces of bread in my mouth as he kissed me )"
    
    show madd distressed at left_small
    with dissolve
    x "(That was the moment I realized how much control he had over me)"
    x "(But this time I was not the one on his radar , it was my step brother. )"
    x "(It was a tug of war between them, both trying to claim me as their own. I was the prize they were fighting over, and I felt like I had no say in the matter.)"
    
    scene scene_kitchen_eating_with_family_dad_only_kiss_1
    with fade
    
    show madd helpless at left_small
    with dissolve
    x "(He continues to kiss me , his other hand now placed on my head too , pulling me closer to him locking me in place as he kissed me.)"
    x "(his tongue was touching the roof of my mouth, his hands were gripping my head tightly, and I could feel his breath on my face as he kissed me.)"
    x "(He stopped for a moment to compliment me or the food , i dont even know . I was food for him , i was his meal and he was enjoying every bite of me . )"
    
    show madd resigned at left_small
    with dissolve
    show dad smirk at right_small
    with dissolve
    dad_says "Taste just like you , my delicious wife !"
    
    show madd distressed at left_small
    with dissolve
    x "(He said that with a smirk on his face, as if he was enjoying the thought of me being his meal.)"
    x "(He continued to kiss me roughly )"
    
    scene scene_kitchen_eating_with_family_dad_only_kiss_2
    with fade
    
    show madd overwhelmed at left_small
    with dissolve
    x "(He pulled back a bit , his tongue slightly pulling away from my mouth, but his hands still gripping my head tightly.)"
    x "(He started to lick my lips, his tongue tracing the outline of my mouth as he kissed me.)"
    x "(So much saliva was being produced from his mouth as he kissed me, it was like a river flowing into my mouth.)"
    x "(I could smell his stinky saliva as it trickled down my chin, and I could feel the taste of the chewed bread in my mouth as he kissed me.)"
    
    show madd nauseated at left_small
    with dissolve
    x "All his saliva dripped down my chin and onto my shirt, soaking it with his stinky saliva."
    
    scene scene_kitchen_eating_with_family_dad_only_kiss_3
    with fade
    
    show madd distressed at left_small
    with dissolve
    x "(Even on my lips , he started to get aggressive with his tongue, trying to force it into my mouth as he kissed me.)"
    x "(my whole mouth was filled with his tongue , he was swirling it around in my mouth)"
    
    show madd helpless at left_small
    with dissolve
    x "(I was so disgusted and uncomfortable, but I couldn't do anything to stop him. I just sat there, frozen in place .)"
    
    scene scene_kitchen_eating_with_family_dad_only_kiss_4
    with fade
    
    show madd shocked at left_small
    with dissolve
    x "(Suddenly he stood up , pulled my hair making me look up at him)"
    
    show madd distressed at left_small
    with dissolve
    x "(He continued to forcefully kiss me, his hands still gripping my head tightly as he kissed me.)"
    x "(I had no where to go, I was trapped in his embrace as he kissed me.)"
    
    scene scene_kitchen_eating_with_family_dad_only_kiss_5
    with fade 
    
    show madd violated at left_small
    with dissolve
    x "(One more time he pulled my hair, making me look up at him as he kissed me passionately . )"
    x "(His mouth was watering like crazy as he kissed me , it was now seeping directly on my shirt. )"
    
    show madd nauseated at left_small
    with dissolve
    x "(My shirt was now completely soaked with his saliva, the stinky smell was overwhelming.)"
    
    scene scene_kitchen_eating_with_family_dad_only_neck_kiss_1
    with fade 
    
    show madd trembling at left_small
    with dissolve
    x "(He finally stopped kissing my lips, but he wasn't done with me yet. He used his hands to pull my head back, exposing my neck to him.)"
    x "(He started to lick my neck, his tongue tracing circles around the sensitive skin as he kissed me.)"
    
    show madd distressed at left_small
    with dissolve
    x "(he was trying to mark me whole as his territory, his saliva was like a marker, leaving his scent on me as he kissed me.)"
    x "(He was trying to show to step brother that I was his, that I belonged to him and only him. and me letting him do that was like a sign of submission to him, it was like I was accepting his claim on me.)"
    
    show madd resigned at left_small
    with dissolve
    x "(He wasnt wrong though, I did belong to him, I was his meal, his property, and there was nothing I could do about it.)"
    
    scene scene_kitchen_eating_with_family_dad_only_neck_kiss_2
    with fade 
    
    show madd conflicted at left_small
    with dissolve
    x "(he started licking my neck from collarbone to jawline, his tongue tracing the sensitive skin as he kissed me.)"
    
    show madd trembling at left_small
    with dissolve
    x "(I felt so helpless and trapped, but only moans of pleasure were escaping my lips as he licked me.)"
    x "(I hated that I was enjoying it, that I was getting pleasure from his touch, but I couldn't help it. )"
    
    show madd anxious at left_small
    with dissolve
    x "(Just then a thought crossed my mind )"
    
    show madd horrified at left_small
    with dissolve
    x "(in the future if i keep letting him do this to me , its not farfethced to think that he might just remove my clothes and pin me down on the floor and..)"
    x "(Push his dick in my pussy right in front of my step brother just to show him that he's the alpha in this house and that I belong to him and only him )"
    x "(He would obviously be on top of me, dominating me, and my step brother would be forced to watch as his father claimed me as his wife in front of him )"
    x "(knowing him , he would probably even piss on me while he's at it, just to show his dominance and to humiliate me even more )"
    
    show madd shaken at left_small
    with dissolve
    x "(SNAP out of it madd , you need to focus on the meal and not let your mind wander to such dark places )"
    
    show madd paralyzed at left_small
    with dissolve
    x "(I tried to push those thoughts out of my head and focus on the meal, but it was hard to concentrate with his hands still gripping my head tightly as he kissed me.)"
    
    scene scene_kitchen_eating_with_family_dad_only_neck_kiss_3
    with fade
    
    show madd nauseated at left_small
    with dissolve
    x "(He continued licking my neck , saliva dripping down my shirt and now it was landing on my plate .)"
    x "(Oh no , even my food is getting soaked with his saliva now , this is so disgusting )"
    
    show madd distressed at left_small
    with dissolve
    x "(Meanwhile only moans of pleasure were escaping my lips as he continued to lick my neck, I hated that I was enjoying it but I couldn't help it.)"
    
    scene scene_kitchen_eating_with_family_dad_only_neck_kiss_4
    with fade
    
    show madd uncertain at left_small
    with dissolve
    x "(He pushed me slightly back, his hands still gripping my head tightly as he kissed me.)"
    
    show madd horrified at left_small
    with dissolve
    x "(That's when I noticed what was happening.)"
    x "(He was slowly and slowly pushing me back so he could show me getting violated closer to step brother)"
    x "(It was like showing a chocolate cake to a starving child and slowly moving it away from him, teasing him with it but never letting him have it )"
    
    show madd distressed at left_small
    with dissolve
    x "(I could see the anger and jealousy in step brother's eyes as he watched his father claim me as his own, it was like a silent battle between them for control over me )"
    x "(I was the prize they were fighting over, and i wont get to decide who wins, i just have to accept it and go with the flow )"

    
    scene scene_kitchen_eating_with_family_dad_only_dad_stand_up
    with fade 
    
    show madd anxious at left_small
    with dissolve
    x "(Finally , he stopped licking my neck and stood up)"
    
    show madd uncertain at left_small
    with dissolve
    show dad smirk at right_small
    with dissolve
    dad_says "So , how did i taste ?"
    
    show madd helpless at left_small
    with dissolve
    x "(His hand put on the back of my head, pulling me closer to his belly as he said that.)"
    
    show madd horrified at left_small
    with dissolve
    show dad smirk at right_small
    with dissolve
    dad_says "Wanna have some more ?"
    
    show madd nauseated at left_small
    with dissolve
    x "(My head was now resting on his belly, his hand still gripping the back of my head as he said that.)"
    x "(I could smell his sweaty belly as he said that, and I could still the taste of his saliva in my mouth as I rested my head on his belly.)"
    
    scene scene_kitchen_eating_with_family_dad_only_dad_stand_up_lowering_jeans
    with fade
    
    show madd paralyzed at left_small
    with dissolve
    x "(He was looking down at me with a smirk on his face, as if he was planning his next move.)"
    x "(His hands starts to move down his body, lowering his jeans slightly to reveal his hard dick )"
    
    show madd shocked at left_small
    with dissolve
    show dad smirk at right_small
    with dissolve
    dad_says "Thanks for the meal, wife. Now it's time for dessert."
    
    show madd trembling at left_small
    with dissolve
    x "(He pulls down his whole jeans, exposing his hard dick to me and step brother as he said that.)"
    x "(He's gonna make me take his dick in my mouth right in front of step brother just to show him that he can do anything he wants to me no matter the location or the time of day )"
    
    show madd distressed at left_small
    with dissolve
    x "(I knew it was coming, but all i can do is prepare myself for the worst as he stood there with his hard dick exposed to me and step brother.)"
    
    scene scene_kitchen_eating_with_family_dad_only_dad_stand_up_dick_out
    with fade 
    
    show madd paralyzed at left_small
    with dissolve
    x "(His hands was on my head , his big dick now touching my throat .I had no where to go only way out was to obey him.)"

    scene scene_kitchen_eating_with_family_dad_only_dad_stand_up_start_bj
    with fade
    
    show madd nauseated at left_small
    with dissolve
    x "(I could feel him pressing against my throat, the warmth and scent of him making me feel lightheaded.)"
    x "(I knew what i had to do , he pulled my head a bit further away from him then pulled it back but towards his dick )"
    
    show madd distressed at left_small
    with dissolve
    x "(I instinctively opened my mouth and took his dick into my mouth , the warmth of it and the scent of it making me feel so disgusted from it)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(I could feel his dick throbbing in my mouth )"
    x "(I felt it grow bigger and bigger in my mouth ,i could smell the scent of it getting stronger and stronger , the taste of it getting worse and worse.)"
    
    show madd helpless at left_small
    with dissolve
    x "(Using his hand to hold the back of my head, he was controlling the pace of my sucking, starting it slow )"
    x "(I dont know why he was starting slow , maybe he was allowing me to adjust to the feeling of his dick in my mouth )"
    x "(Maybe he was just showing that he controlled the pace to StepBrother. TO show him that i would allow him to do whatever he wants with me )"
    x "(He starts moving his hips now, the pace adding up making his dick go deeper into my throat , the warmth of it spreading through my mouth and throat )"
    
    scene scene_kitchen_eating_with_family_dad_only_dad_stand_up_bj_1
    with fade
    
    show madd trembling at left_small
    with dissolve
    x "(his dick was going deeper and deeper into my throat, my body was starting to get used to the feeling of it in my mouth and throat  )"
    
    show madd conflicted at left_small
    with dissolve
    x "(Although i hated it, my body was starting to like the taste of it, the scent of it should make me feel disgusted but it was making me feel a little bit aroused )"
    x "(I hate when this happens. His pheromones accumulate in my body, making me feel aroused despite my disgust.)"
    
    scene scene_kitchen_eating_with_family_dad_only_dad_stand_up_bj_2
    with fade
    
    show madd paralyzed at left_small
    with dissolve
    x "(The rhythm of his hips were getting consistent )"
    x "(There was a sync between him pulling my head towards him and the movement of his hips, and due to that sync it was making it go all the way to the back of my throat. )"
    
    scene scene_kitchen_eating_with_family_dad_only_dad_stand_up_bj_3
    with fade
    
    show madd horrified at left_small
    with dissolve
    x "(He did few more thrusts and then suddenly increased the pace of his thrust )"
    x "(The sudden increase made me feel like i was going to gag , made me split my saliva and made his dick go all the way to the back of my throat )"
    
    show madd distressed at left_small
    with dissolve
    x "(Those hard thrusts going all the way to the back of my throat was so intense )"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(Losing all control of my body to my StepFather was making me feel so disgusted and aroused at the same time . )"
    
    scene scene_kitchen_eating_with_family_dad_only_dad_stand_up_bj_4
    with fade
    
    show madd trembling at left_small
    with dissolve
    x "(His pace increased further and further , this whole time i had my eyes closed and i was just trying to get used to the feeling of his dick in my mouth and throat )"
    
    show madd shocked at left_small
    with dissolve
    x "(But this increase in pace made me open my eyes and look at him , the sight of him thrusting his crotch in my face , the position i was in . All of it was such a submissive place to be. )"
    
    show madd trembling at left_small
    with dissolve
    x "(more and more saliva leaking out of my mouth , his dick displacing the saliva and making it leak out even more )"
    x "(This is what being dominated by my StepFather felt like , this is what mom felt every day of her life. I cant help but feel jealous of her.)"
    x "(Perhaps in that moment if he had asked me to marry me i would've said yes. Then again asking someone to marry you while your cock is down her throat is exactly what i expect of him.)"    
    scene scene_kitchen_eating_with_family_dad_only_dad_stand_up_climax_1
    with fade
    
    show madd shocked at left_small
    with dissolve
    x "(Suddenly I felt him throbbing in my mouth more and more. The temperature getting hotter. I knew what was coming, and I was both scared and excited for it.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(then i felt it, the first spurt of his cum shooting into my mouth and throat , the warmth of it, instantly i felt the taste and scent hit me . )"
    
    show madd distressed at left_small
    with dissolve
    x "(Here i was , being filled with my StepFathers cum during dinner time right in front of stepBrother . I was eating his cum and i was loving it . )"
    
    show madd conflicted at left_small
    with dissolve
    x "(I was loving the position of being dominated by my StepFather , the feeling of his dick in my mouth and throat was making me feel so turned on. )"
    x "(it must be his phermones or something but i was loving the feeling of being dominated by him  )"
    
    show madd resigned at left_small
    with dissolve
    x "(He could have breeded me right there in the kitchen and i would have loved it , i just cant stand up to him when he goes into his dominant mode , i just cant say no to him when he wants to do something with me )"
    
    show madd helpless at left_small
    with dissolve
    x "(He kept cumming and kept filling my mouth and throat with his cum  )"
    
    scene scene_kitchen_eating_with_family_dad_only_dad_stand_up_climax_2
    with fade 
    
    show madd nauseated at left_small
    with dissolve
    x "(Finally i felt it getting less and less hot and throbby , the pace of it getting slower and slower . )"
    
    show madd distressed at left_small
    with dissolve
    x "(But he didnt stop , he kept moving my head and kept thrusting his dick into my mouth and throat while he was cumming , a lot of it was leaking out of my mout and directly on my plate but i didnt care , i was loving the moment .)"
    
    show madd resigned at left_small
    with dissolve
    x "(his cum was getting pooled on my plate forming a puddle of it , if no one else was there i would have licked it whole  )"
    
    show madd helpless at left_small
    with dissolve
    x "(He kept thrusting , his balls slapping against my chin and his dick going all the way to the back of my throat  )"
    
    show madd distressed at left_small
    with dissolve
    x "(Finally he stopped thrusting and just let his dick sit in my mouth and throat while he was cumming ,I could feel it shrinking in real time while it was in there.)"
    
    show madd uncertain at left_small
    with dissolve
    show dad smirk at right_small
    with dissolve
    dad_says "Go ahead and swallow it all , i want you to swallow every drop of it ."
    
    show madd resigned at left_small
    with dissolve
    x "(I didnt even have to think about it, i just instinctively swallowed all of his cum that was in my mouth and throat , he didn t even have to tell me to do it, i just did it without even thinking about it )"
    
    show madd distressed at left_small
    with dissolve
    x "(Eventually he pulled his dick out of my mouth and throat and i could see the cum dripping out of my mouth and down my chin , and he picked up his jeans and started putting them on while looking at me .)"
    
    show madd helpless at left_small
    with dissolve
    x "(He sat back down at the table and started eating his food like nothing happened , i was just sitting there with cum dripping out of my mouth and down my chin  )"
    
    show madd violated at left_small
    with dissolve
    x "(He finally noticed, the cum that was on my plate that probably gave him an idea to humiliate me more , he looked at the cum on my plate and then looked at me and said )"
    
    scene scene_kitchen_eating_with_family_dad_only_dad_eat_cum
    with fade
    
    show madd horrified at left_small
    with dissolve
    show dad smirk at right_small
    with dissolve
    dad_says "GO on , eat it wife ."
    
    show madd paralyzed at left_small
    with dissolve
    x "(He put his hand on my head and pushed my face down towards the cum that was on my plate , i could feel his hand pushing my face down  )"
    
    show madd distressed at left_small
    with dissolve
    show dad smirk at right_small
    with dissolve
    dad_says "Dont you want to  eat , what your husband just gave you ?"
    
    show madd resigned at left_small
    with dissolve
    x "(I was so humiliated but i couldnt say no to him , i just had to obey him and eat the cum that was on my plate )"
    
    show madd conflicted at left_small
    with dissolve
    x "(I pulled out my tongue and started licking the cum that was on my plate )"
    
    show madd resigned at left_small
    with dissolve
    x "( i didnt feel anything bad about it , i was loving the moment .In fact him telling me to eat the cum that was on my plate was exactly what i wanted to do but i was too scared to do it on my own . )"
    
    show madd distressed at left_small
    with dissolve
    x "(is that how i win? By being submissive to others ? By becoming a degenerate and just letting others do whatever they want to me ? )"
    
    scene scene_kitchen_eating_with_family_dad_only_dad_eat_cum_finish
    with fade

    show madd uncertain at left_small
    with dissolve
    x "(I licked the cum on my plate and then looked up at him , he was looking at me with a smile on his face and said )"
    
    show madd resigned at left_small
    with dissolve
    show dad smirk at right_small
    with dissolve
    dad_says "Good job wife , you know your place ."
    
    show madd shocked at left_small
    with dissolve
    x "(Then he angrily shouts at brother )"
    
    show madd distressed at left_small
    with dissolve
    show dad angry at right_small
    with dissolve
    dad_says "Remember this moment. "
    dad_says "She is my wife , never touch her again."
    
    show madd resigned at left_small
    with dissolve
    x "(I just kept my head low and licked the plate clean . I was loving the moment , i was loving being dominated by my StepFather and being humiliated by him in front of my StepBrother . )"
    x "(After that moment , i finished my food . his cum . And then put the plate in the sink and went to my room to change my clothes .  )"

    $ character_relations["dad"]["intimacy"] +=7
    $ character_relations["dad"]["kissed"] += 1
    $ character_relations["dad"]["oral_sex"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["lust"]=0
    $ character_relations["brother"]["lust"]+=20
    $ brother_sees_madd_blow_dad = True
    $ journal_event_set_done("Dad","Dinner Table Claim") 
    show screen stat_notification
    $ stat_notification = "Willpower +20 "
    pause 4.0
    $ stat_notification = ""
    hide screen stat_notification
    show screen stat_notification
    $ stat_notification = "Intimacy with Dad +7"
    pause 4.0
    $ stat_notification = ""
    hide screen stat_notification

    $ madd_willpower = min(madd_willpower_max, madd_willpower + 30)
    
    show screen stat_notification
    $ stat_notification = "Willpower +30"
    pause 4.0
    $ stat_notification = ""
    hide screen stat_notification
    
    $ family_meal_prepared -= 1
    call advance_time_and_check(minutes=45) 

    jump home_areas
    

label kitchen_eating_with_family_bad_food:

    scene scene_kitchen_eating_with_family
    with fade
    
    show madd uncertain at left_small
    with dissolve
    x "(As we started eating, I noticed something was off with the food.)"
    


    show madd nervous at left_small
    with dissolve
    x "(The vegetables were overcooked, the seasoning was off... This wasn't my best work.)"
    
    scene scene_kitchen_eating_with_family_bad_food_reaction
    with fade

    show dad wistful at right_small
    with dissolve
    dad_says "Maddie, what the fuck is this? "
    
    show madd anxious at left_small
    with dissolve
    x "I... I'm sorry, Dad. I must have messed something up while cooking."
    
    hide dad
    show brother dismissive at right_small
    with dissolve
    brother_says "Yeah, this is pretty bad. I can barely eat it."
    
    show madd distressed at left_small
    with dissolve
    x "(I felt embarrassed and ashamed. I tried my best, but I clearly failed.)"
    
    show dad angry at right_small
    with dissolve
    hide brother
    dad_says "Are you trying to poison me?"
    
    
    show madd uncertain at left_small
    with dissolve
    x "(The rest of the meal was eaten in uncomfortable silence. I could feel their disappointment.)"
    x "(After finishing, I quickly cleared the plates and cleaned up, eager to escape the tense atmosphere.)"
    

    $ madd_willpower = min(0, madd_willpower + 20)
    
    show screen stat_notification
    $ stat_notification = "Willpower +20"
    pause 4.0
    $ stat_notification = ""
    hide screen stat_notification

    
    $ family_meal_prepared -= 1
    call advance_time_and_check(minutes=45) from _call_advance_time_and_check_bad_food
    
    jump home_areas


label kitchen_eating_with_family_normal_eat:

    scene scene_kitchen_eating_with_family
    with fade
    
    show madd uncertain at left_small
    with dissolve
    x "(We ate together in relative peace. The food turned out well.)"
    
    show madd rbg at left_small
    with dissolve
    x "(There wasn't much conversation, but at least the atmosphere wasn't hostile.)"
    
    show dad thinks at right_small
    with dissolve
    dad_says "The food is good today."
    
    show madd uncertain at left_small
    with dissolve
    x "Thank you, Dad."
    
    hide dad
    show brother think at right_small
    with dissolve
    brother_says "Yeah, not bad."

    if todays_food_drugged:
        show madd think at left_small
        with dissolve
        x "(I carefully only ate the parts of the meal that I didn't drug, trying to avoid any suspicion.)"
        if renpy.random.random() < 0.4:
            hide brother
            show dad thinks at right_small
            with dissolve
            dad_thinks "(This tastes a little different than usual, but I can't quite put my finger on it.)"
            show dad calculating at right_small
            with dissolve
            dad_thinks "(Maybe she put in something in the food... it's making me feel a little bit different.)"
            dad_thinks "(Only way to make sure is to make her eat the same food, see if she accepts it or not.)"
            show dad manipulative at right_small
            with dissolve
            dad_says "Maddie, try this soup — it's really good!"
            show madd anxious at left_small
            with dissolve
            x "(He offered me some of the soup, which I had drugged. Oh god, is he suspicious now? I have to eat it to avoid suspicion.)"
            show madd nervous at left_small
            with dissolve
            x "(I took a small spoonful of the soup and tasted it, trying to act natural.)"
            x "Thanks for letting me have some, Dad."
            show madd flustered at left_small
            with dissolve
            x "(Immediately I feel the effects of the drug hit me, my body is getting hotter.)"
            show madd distressed at left_small
            with dissolve
            x "(I have to endure it... Maybe I shouldn't have put the pill in the food, maybe I should have just put stress pills instead...)"
            show madd inhead at left_small
            with dissolve
            x "(Just endure, Maddie... you can get through this... just focus on the meal and not the drug effects...)"
            $ maddie_is_drugged = True
            $ last_madd_drugged_day = days_passed


    
    show madd rbg at left_small
    with dissolve
    hide brother
    x "(We finished our meal without any drama. I guess that's the best I can hope for these days.)"
    x "(After dinner, I cleaned up the dishes and put everything away.)"
    
    # Update stats - minor positive impact
    $ madd_willpower = min(madd_willpower_max, madd_willpower + 30)
    
    show screen stat_notification
    $ stat_notification = "Willpower +30"
    pause 4.0
    $ stat_notification = ""
    hide screen stat_notification
    
    $character_relations["dad"]["intimacy"] += 1
    $character_relations["brother"]["intimacy"] += 1

    $ family_meal_prepared -= 1
    call advance_time_and_check(minutes=45) from _call_advance_time_and_check_normal_eat
    $ character_relations["brother"]["friend"]+=2
    
    jump home_areas


label cooking_for_family:
    
    scene scene_kitchen_cooking_for_family_solo_madd
    with fade


    show madd rbf at left_small
    with dissolve

    x "(I had to cook for my StepFather and StepBrother . I was instructed to prepare a meal for them, and I had no choice but to comply.)"
    x "(I was in the kitchen, cooking and preparing the meal .)"


    $ journal_event_show("Dad", "Dinner Table Claim")
    $ journal_event_show("Dad", "Sandwich in the Kitchen")
    $ journal_event_show("Dad", "Bred in the Kitchen")

    if character_relations["brother"]["lust"] >= 10 and character_relations["dad"]["lust"] >= 60 :
        jump cooking_for_family_brother_and_dad_join

        

    show madd think at left_small
    with dissolve
    x "(While preparing the meal, I could slip something into their food if I wanted to...)"
    x "(I dont want to add more than 1 pill to the meal, because if they get too drugged then they might get suspicious and i dont want that to happen.)"
    x "(Worst case scenario, if they die from the drugs i am going straight to jail )"

    menu:
        "Add nothing — serve the meal as is":
            pass

        "Slip in an Aphrodisiac" if inv_aphrodisiac >= 1:
            show madd think at left_small
            with dissolve
            x "(Whose portion should I slip it into...?)"
            menu:
                "Target Dad only":
                    scene scene_kitchen_cooking_for_family_solo_madd_adding_drugs
                    with dissolve
                    show madd processing at left_small
                    with dissolve
                    x "(I crushed an aphrodisiac tablet and slipped it into Dad's plate only. He won't notice.)"
                    x "(This will stir up his desires...)"
                    $ inv_aphrodisiac -= 1
                    $ character_relations["dad"]["lust"] = min(100, character_relations["dad"]["lust"] + 100)
                    $ todays_food_drugged = True
                    show screen stat_notification
                    $ stat_notification = "Dad Lust +100"
                    pause 3.0
                    $ stat_notification = ""
                    hide screen stat_notification
                    if renpy.random.random() < 0.1:
                        $ dad_knows_madd_drugs_food = True
                        dad_thinks "(That little brat... she just slipped something into the food. )"
                        dad_thinks "Knowing her ,she probably didnt use anything lethal ...if i still ate the food  then i can blackmail her later and make her do whatever i want . )"
                        dad_thinks "Heh, gotta risk it for her sweet beautiful pussy. )"
                "Target Brother only":
                    scene scene_kitchen_cooking_for_family_solo_madd_adding_drugs
                    with dissolve
                    show madd processing at left_small
                    with dissolve
                    x "(I crushed an aphrodisiac tablet and slipped it into Brother's plate only. He won't even taste it.)"
                    x "(This will mess with his head...)"
                    $ inv_aphrodisiac -= 1
                    $ character_relations["brother"]["lust"] = min(100, character_relations["brother"]["lust"] + 100)
                    $ todays_food_drugged = True
                    show screen stat_notification
                    $ stat_notification = "Brother Lust +100"
                    pause 3.0
                    $ stat_notification = ""
                    hide screen stat_notification
                "Target both":
                    scene scene_kitchen_cooking_for_family_solo_madd_adding_drugs
                    with dissolve
                    show madd processing at left_small
                    with dissolve
                    x "(I crushed an aphrodisiac tablet and mixed it into both their servings. Neither of them will notice.)"
                    x "(This will stir up both their desires...)"
                    $ inv_aphrodisiac -= 1
                    $ character_relations["dad"]["lust"] = min(100, character_relations["dad"]["lust"] + 100)
                    $ character_relations["brother"]["lust"] = min(100, character_relations["brother"]["lust"] + 100)
                    $ todays_food_drugged = True
                    show screen stat_notification
                    $ stat_notification = "Dad Lust +100 | Brother Lust +100"
                    pause 3.0
                    $ stat_notification = ""
                    hide screen stat_notification
                    if renpy.random.random() < 0.1:
                        $ dad_knows_madd_drugs_food = True
                        dad_thinks "(That little brat... she just slipped something into the food. )"
                        dad_thinks "Knowing her ,she probably didnt use anything lethal ...if i still ate the food  then i can blackmail her later and make her do whatever i want . )"
                        dad_thinks "Heh, gotta risk it for her sweet beautiful pussy. )"
                "Nevermind, that's a bad idea":
                    show madd think at left_small
                    with dissolve
                    x "(Actually... let's not. Too risky.)"

        "Slip in Stress Reduction Pills" if inv_stress_pills >= 1:
            show madd think at left_small
            with dissolve
            x "(Whose portion should I slip it into...?)"
            menu:
                "Target Dad only":
                    scene scene_kitchen_cooking_for_family_solo_madd_adding_drugs
                    with dissolve
                    show madd processing at left_small
                    with dissolve
                    x "(I dissolved a stress reduction pill into Dad's serving. This should calm him down.)"
                    x "(Hopefully dinner will be a little less tense.)"
                    $ inv_stress_pills -= 1
                    $ character_relations["dad"]["anger"] = max(0, character_relations["dad"]["anger"] - 50)
                    $ character_relations["dad"]["lust"] = max(0, character_relations["dad"]["lust"] - 50)
                    $ todays_food_drugged = True
                    show screen stat_notification
                    $ stat_notification = "Dad Anger -50 | Dad Lust -50"
                    pause 3.0
                    $ stat_notification = ""
                    hide screen stat_notification
                    if renpy.random.random() < 0.1:
                        $ dad_knows_madd_drugs_food = True
                        dad_thinks "(That little brat... she just slipped something into the food. )"
                        dad_thinks "Knowing her ,she probably didnt use anything lethal ...if i still ate the food  then i can blackmail her later and make her do whatever i want . )"
                        dad_thinks "Heh, gotta risk it for her sweet beautiful pussy. )"
                "Target Brother only":
                    scene scene_kitchen_cooking_for_family_solo_madd_adding_drugs
                    with dissolve
                    show madd processing at left_small
                    with dissolve
                    x "(I dissolved a stress reduction pill into Brother's serving. This should mellow him out.)"
                    $ inv_stress_pills -= 1
                    $ character_relations["brother"]["anger"] = max(0, character_relations["brother"]["anger"] - 50)
                    $ character_relations["brother"]["lust"] = max(0, character_relations["brother"]["lust"] - 50)
                    $ todays_food_drugged = True
                    show screen stat_notification
                    $ stat_notification = "Brother Anger -50 | Brother Lust -50"
                    pause 3.0
                    $ stat_notification = ""
                    hide screen stat_notification
                "Target both":
                    scene scene_kitchen_cooking_for_family_solo_madd_adding_drugs
                    with dissolve
                    show madd processing at left_small
                    with dissolve
                    x "(I dissolved a stress reduction pill into the food. It should calm them both down.)"
                    x "(Hopefully this makes dinner a little less tense.)"
                    $ inv_stress_pills -= 1
                    $ character_relations["dad"]["anger"] = max(0, character_relations["dad"]["anger"] - 50)
                    $ character_relations["brother"]["anger"] = max(0, character_relations["brother"]["anger"] - 50)
                    $ character_relations["dad"]["lust"] = max(0, character_relations["dad"]["lust"] - 50)
                    $ character_relations["brother"]["lust"] = max(0, character_relations["brother"]["lust"] - 50)
                    $ todays_food_drugged = True
                    show screen stat_notification
                    $ stat_notification = "Dad Anger -50 | Brother Anger -50"
                    pause 3.0
                    $ stat_notification = ""
                    hide screen stat_notification
                    if renpy.random.random() < 0.1:
                        $ dad_knows_madd_drugs_food = True
                        dad_thinks "(That little brat... she just slipped something into the food. )"
                        dad_thinks "Knowing her ,she probably didnt use anything lethal ...if i still ate the food  then i can blackmail her later and make her do whatever i want . )"
                        dad_thinks "Heh, gotta risk it for her sweet beautiful pussy. )"
                "Nevermind, that's a bad idea":
                    show madd think at left_small
                    with dissolve
                    x "(Actually... let's not. Too risky.)"

        "Slip in Testosterone Pills" if inv_testosterone >= 1:
            show madd think at left_small
            with dissolve
            x "(Whose portion should I slip it into...?)"
            menu:
                "Target Dad only":
                    scene scene_kitchen_cooking_for_family_solo_madd_adding_drugs
                    with dissolve
                    show madd processing at left_small
                    with dissolve
                    x "(I crush a testosterone pill and mix it into Dad's serving. This will make him more volatile...)"
                    $ inv_testosterone -= 1
                    $ character_relations["dad"]["anger"] += 60
                    $ character_relations["dad"]["lust"] = min(100, character_relations["dad"]["lust"] + 20)
                    $ todays_food_drugged = True
                    show screen stat_notification
                    $ stat_notification = "Dad Anger +60 | Dad Lust +20"
                    pause 3.0
                    $ stat_notification = ""
                    hide screen stat_notification
                    if renpy.random.random() < 0.1:
                        $ dad_knows_madd_drugs_food = True
                        dad_thinks "(That little brat... she just slipped something into the food. )"
                        dad_thinks "Knowing her ,she probably didnt use anything lethal ...if i still ate the food  then i can blackmail her later and make her do whatever i want . )"
                        dad_thinks "Heh, gotta risk it for her sweet beautiful pussy. )"
                "Target Brother only":
                    scene scene_kitchen_cooking_for_family_solo_madd_adding_drugs
                    with dissolve
                    show madd processing at left_small
                    with dissolve
                    x "(I crush a testosterone pill and mix it into Brother's serving. A riskier move...)"
                    $ inv_testosterone -= 1
                    $ character_relations["brother"]["anger"] = min(100, character_relations["brother"]["anger"] + 60)
                    $ character_relations["brother"]["lust"] = min(100, character_relations["brother"]["lust"] + 20)
                    $ todays_food_drugged = True
                    show screen stat_notification
                    $ stat_notification = "Brother Anger +60 | Brother Lust +20"
                    pause 3.0
                    $ stat_notification = ""
                    hide screen stat_notification
                "Target both":
                    scene scene_kitchen_cooking_for_family_solo_madd_adding_drugs
                    with dissolve
                    show madd processing at left_small
                    with dissolve
                    x "(I crush a testosterone pill and mix it into the food. This will make them both volatile...)"
                    x "(A riskier move, but it might make them more aggressive and easier to provoke.)"
                    $ inv_testosterone -= 1
                    $ character_relations["dad"]["anger"] = min(100, character_relations["dad"]["anger"] + 60)
                    $ character_relations["brother"]["anger"] = min(100, character_relations["brother"]["anger"] + 60)
                    $ character_relations["dad"]["lust"] = min(100, character_relations["dad"]["lust"] + 20)
                    $ character_relations["brother"]["lust"] = min(100, character_relations["brother"]["lust"] + 20)
                    $ todays_food_drugged = True
                    show screen stat_notification
                    $ stat_notification = "Dad Anger +60 | Brother Anger +60 | Dad Lust +20 | Brother Lust +20"
                    pause 3.0
                    $ stat_notification = ""
                    hide screen stat_notification
                    if renpy.random.random() < 0.1:
                        $ dad_knows_madd_drugs_food = True
                        dad_thinks "(That little brat... she just slipped something into the food. )"
                        dad_thinks "Knowing her ,she probably didnt use anything lethal ...if i still ate the food  then i can blackmail her later and make her do whatever i want . )"
                        dad_thinks "Heh, gotta risk it for her sweet beautiful pussy. )"
                "Nevermind, that's a bad idea":
                    show madd think at left_small
                    with dissolve
                    x "(Actually... let's not. Too risky.)"
    jump cooking_for_family_finish

    # Check conditions based on lust levels



label cooking_for_family_brother_and_dad_join:
    """
    Event when both brother and dad join the cooking session.
    Triggers when brother lust >= 50 and dad lust >= 80.
    """
    scene scene_kitchen_cooking_for_family_solo_madd
    with fade
    
    show madd focused at left_small
    with dissolve
    x "(As I was cooking, I heard footsteps approaching the kitchen...)"
    
    show madd anxious at left_small
    with dissolve
    x "(Both my StepFather and StepBrother entered the kitchen, their eyes fixed on me.)"
    
    scene cooking_for_family_brother_and_dad_join_madd_standing_between_them
    with fade
    
    show madd shocked at left_small
    with dissolve
    x "(Suddenly, I felt a hand on my back, and another hand on the back of my head)" 
    
    show madd trembling at left_small
    with dissolve
    x "(Dad was standing to my right, while Brother was standing to my left, both of them staring at me with lustful eyes.)"

    
    scene cooking_for_family_brother_and_dad_join_madd_standing_between_them_spank_1
    with fade
    
    show madd shocked at left_small
    with dissolve
    x "(Suddenly, I felt a sharp spank on my ass, making me yelp in surprise.)"
    
    show dad controlling at right_small
    with dissolve
    dad_says "How long do I have to wait for dinner, Maddie?"
    
    show madd nervous at left_small
    with dissolve
    x "(I was still reeling from the unexpected spank, stammering in response.)"
    x "A..Almost done, Dad..."
    
    hide dad
    show brother amused at right_small
    with dissolve
    x "(Seeing my hesitation, even Brother was emboldened.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I saw his hand reaching for my ass and he spanked me as well, multiple spanks followed in quick succession.)"
    
    show brother smirk at right_small
    with dissolve
    brother_says "I need food fast! I have to get back to my game soon!"
    
    hide brother
    show madd trembling at left_small
    with dissolve
    x "(They finally stopped spanking me. I went back to cutting the vegetables, trying to focus on my task while they continued to watch me with lustful gazes.)"

    
    scene cooking_for_family_brother_and_dad_join_madd_standing_between_them_spank_2
    with fade
    
    show madd paralyzed at left_small
    with dissolve
    x "(Just when I thought they would leave me alone, I felt another spank on my ass, this time from my StepFather.)"
    x "(He didn't say anything. His hand reached out to my neck, making me bend down slightly, while his other hand rubbed my ass.)"
    
    show madd helpless at left_small
    with dissolve
    x "(I was frozen in place, unable to move or speak as he continued to touch me in whatever way he pleased.)"
    x "(Seeing my StepFather's actions, my StepBrother couldn't resist joining in as well, his hand also reaching out to touch me.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(I had two hands on my ass, one from my StepFather and another from my StepBrother, both of them rubbing each side of my ass, making me feel overwhelmed and helpless.)"
    x "(I could feel the fabric of my shorts cutting into my skin as they continued to spank and grope me.)"

    
    scene cooking_for_family_brother_and_dad_join_madd_standing_between_them_spank_3
    with fade
    
    show madd helpless at left_small
    with dissolve
    x "(I was completely at their mercy, unable to resist or escape as they continued to spank and touch me in whatever way they pleased.)"
    
    show madd shocked at left_small
    with dissolve
    x "(Suddenly, one more loud spank echoed through the kitchen, again from my StepFather, making me jump in surprise.)"
    x "(He then lifts my body up, holding me in the air and dragging me away from the counter.)"
    
    show dad lustful at right_small
    with dissolve
    dad_says "Come here, Maddie. Useless bitch takes so long to cook"
    dad_says "Let me put you to a different use."
    
    show madd trembling at left_small
    with dissolve
    x "(He turned me around to face him, his eyes filled with lust as he looked at me.)"
    x "(I was now in his embrace. Watching this scene, my StepBrother also joined in, his lips touching the hair on the back of my head.)"


    if character_relations["dad"]["intimacy"] < 60:
        menu:
            "Stop this now before this escalates" :
                if madd_willpower+2*(60-character_relations["dad"]["intimacy"]) >= character_relations["dad"]["lust"]:
                    show madd angry at left_small
                    x "STOP THIS NOW YOU FUCKING ASSHOLES"
                    x "(I could see both their faces filled to the brim with shock)"
                    x "You do anything to me and I will make sure you regret it! Both of you fat fucks will make good bitches in a prison for sure if you keep this up!"
                    show dad angry at right_small
                    x "(I felt his grip on me loosen as he angrily growls)"
                    dad_says "Why...you... how dare you talk to me like that! "
                    brother_says "Cmon, Dad... we can do this some other time..."
                    dad_says "This isn't over, Maddie. You just wait and see..."
                    x "(they both stop their actions and leave me alone for now, but I know this isn't the end of it. )"
                    x "(Once they leave, I take a moment to collect myself, my heart racing from the confrontation. As i continue cooking, I can feel their frantic motions from outside the kitchen, probably talking about what just happened.)"


                    $ character_relations["dad"]["anger"] +=10
                    $ character_relations["brother"]["anger"] +=10
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_119
                    $ character_relations["dad"]["intimacy"]+=5
                    $ character_relations["brother"]["intimacy"]+=5
                    call advance_time_and_check(minutes=120) 
                    $ madd_willpower=max(madd_willpower-20,0)
                    jump cooking_for_family_finish
                else:
                    $character_relations["dad"]["lust"]=0
                    $character_relations["dad"]["anger"] +=10
                    $character_relations["brother"]["anger"] +=10
                    show madd trembling at left_small
                    x "(I wanted to stop him, but i was so scared that i couldnt even say anything, my voice was trembling and my body was shaking)"
                    call advance_time_and_check(minutes=10) from _call_advance_time_and_check_120

    scene cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_1
    with fade
    
    show madd paralyzed at left_small
    with dissolve
    x "(I was now sandwiched between my StepFather and StepBrother. I could feel their bodies pressed against mine, I could feel their hot breath on my skin as I was smaller than both of them.)"
    
    show dad angry at right_small
    with dissolve
    x "(Suddenly, StepFather raised his voice and said angrily to my StepBrother.)"
    dad_says "Maddie is mine, you can kiss her all you want, but her holes belong to me, understand?"
    
    hide dad
    show brother shocked at right_small
    with dissolve
    x "(My StepBrother looked at my StepFather with fear and submission, his head lowered in response.)"
    brother_says "I..I understand, Dad..."
    
    hide brother
    show dad dominant at right_small
    with dissolve
    show madd horrified at left_small
    with dissolve
    x "(Hearing this, my StepFather's hand reached out to my face, pulling it to look at him and immediately kissed me, his lips pressing against mine with a force that left me breathless.)"
    
    show madd violated at left_small
    with dissolve
    x "(This was a power demonstration. My StepFather was asserting his dominance over me to my StepBrother. He wanted to show my StepBrother that he was the one in control and that I belonged to him.)"

    
    scene cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_2
    with fade
    
    show dad possessive at right_small
    with dissolve
    show madd trembling at left_small
    with dissolve
    x "(He pulled away from the kiss, his eyes still filled with lust as he looked at me.)"
    
    show dad smirk at right_small
    with dissolve
    dad_says "Good, now that you know your place."
    x "(A smirk appeared on my StepFather's face as he said this, his eyes filled with satisfaction and dominance.)"
    dad_says "I am gonna taste my wife."
    
    hide dad
    show madd shocked at left_small
    with dissolve
    brother_says "Thanks, Dad..."
    
    x "(There was genuine gratitude in my StepBrother's voice as he said this.)"
    x "(Immediately after saying this, my stepbrother's lips pressed against my cheeks, his tongue licking and sucking on my skin, leaving a trail of wetness in its wake.)"
    
    show madd distressed at left_small
    with dissolve
    x "(At the same time, my Dad's tongue reached out to my mouth. He kissed me again.)"
    x "( My mouth was wide open from shock and he used this opportunity to stick his tongue into my mouth, exploring every inch of it with his own tongue.)"
    

    scene cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_3
    with fade
    
    show madd overwhelmed at left_small
    with dissolve
    x "(Getting Dad's approval, both were emboldened to continue their actions.)"
    x "(They both pulled back for a moment, then they both attacked me at the same time.)"  
    
    show madd distressed at left_small
    with dissolve
    x "(Both roughly touching my body, manhandling me in whatever way they pleased. I was completely at their mercy, unable to resist or escape as they continued to touch me in whatever way they pleased.)"
    x "(Dad's tongue was inside my mouth again, while my StepBrother's tongue was licking and sucking on my neck.)"

    
    scene cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_4
    with fade
    
    show madd trembling at left_small
    with dissolve
    x "(Suddenly, they both slowed down their actions. It was as if to give me a moment to catch my breath, but I knew it was just a temporary pause before they continued their assault on me.)"
    x "(My StepFather was slowly licking my face while StepBrother moved the hair on the back of my head out of the way and kissed the back of my neck.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(This slow movement could almost be called passionate. I was in such a state but even then I liked it. I was enjoying the attention and affection from both of them, even though it was overwhelming and intense.)"    

    
    scene cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_5
    with fade
    
    show madd overwhelmed at left_small
    with dissolve
    x "(After a few slow and passionate moments, they both suddenly increased the intensity of their actions again. It was as if they were trying to make up for lost time during the slow moment.)"
    
    show madd nauseated at left_small
    with dissolve
    x "(I could smell their saliva on me now. My whole body was covered in their saliva. I could feel the wetness on my skin and the taste of their saliva in my mouth.)"
    
    show madd helpless at left_small
    with dissolve
    x "(It was as if the whole world had disappeared around me, and the only thing left was the two of them and me. I was breathing in their scent and their touch.)"

    
    scene cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_6
    with fade
    
    show madd distressed at left_small
    with dissolve
    x "(As they slowed down again, my hair reset to its original position, covering my neck again.)"
    x "(Once again my StepBrother had to move the hair on the back of my head out of the way to kiss the back of my neck, while my StepFather continued to lick my face.)"
    x "(StepBrother was licking my neck from the bottom to the ear while my StepFather was licking the inside of my mouth.)"

    
    scene cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_7
    with fade
    
    show madd resigned at left_small
    with dissolve
    x "(I was done resisting. I was completely at their mercy and I accepted my fate. Might as well let them have their fun with me.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(At this point their mouths watering like crazy. They were both so into it, they were both enjoying the moment so much.)"
    x "(I could feel lots of saliva from both of them on me. I was completely drenched in their saliva.)"
    
    show madd shocked at left_small
    with dissolve
    x "(While I was focusing on the smell, taste and feel of their saliva on me, I barely noticed that StepDad had moved his hand down to my shorts. He was squeezing my ass through the fabric of my shorts.)"
    
    show madd trembling at left_small
    with dissolve
    x "(It wasn't a tender touch. It was a rough and forceful squeeze, making me gasp in surprise and pleasure at the same time.)"


    scene cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_8
    with fade
    
    show madd distressed at left_small
    with dissolve
    x "(He started rubbing my ass through the fabric of my shorts, his hand moving in circular motions as he continued to squeeze and fondle me.)"
    x "(Then Brother also joined in, his hand reaching out to my other ass and squeezing it as well. I noticed that Dad's hand withdrew from my shorts as if giving StepBrother the opportunity to take over.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(I was between my Brother and Dad, covered in their saliva, my body marked by their fluids, my nose filled with their musky scent and they would probably continue to do these actions for a long time.)"
    
    show madd weeping at left_small
    with dissolve
    x "(Having these thoughts in my mind, I couldn't hold back as tears started to stream down my face.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I was crying, but I was also enjoying the moment. It was a mix of emotions that I couldn't quite understand. They weren't bothered by my tears.)"
    x "( They continued to touch me in whatever way they pleased, completely ignoring my emotional state.)"


    scene cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_9
    with fade
    
    show madd distressed at left_small
    with dissolve
    x "(Their rough assault continued for a while.)"
    
    show madd shocked at left_small
    with dissolve
    x "(Then StepBrother's hand reached out to my chest. He lowered it from my shoulder down to my breast, squeezing it through the fabric of my shirt, making me gasp in surprise and pleasure at the same time.)"
    x "(Meanwhile, my StepFather's hand moved down to my shorts again. He was squeezing my ass through the fabric of my shorts again.)"


    scene cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_10
    with fade
    
    show madd overwhelmed at left_small
    with dissolve
    x "(They got rougher and rougher. They were both so into it, they were both enjoying the moment so much.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I couldn't help but get lost in the sensations, the pleasure and the pain. Being sandwiched between my StepFather and StepBrother didn't feel so bad.)"
    
    show madd flustered at left_small
    with dissolve
    x "(My nipples were hardening under the fabric of my shirt as I understood my submissive role in this situation and it made me feel even more submissive and obedient to them.)"

    if character_relations["dad"]["anger"]>=60 or character_relations["dad"]["vaginal_sex"]>=1 or character_relations["brother"]["lust"]<60 :
        if renpy.random.random() < 0.9:
            dad_says "God im so angry today, i am gonna fuck this bitch raw."
            jump cooking_for_family_brother_and_dad_join_dad_only_vaginal

    scene cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_lift_1
    with fade
    
    show madd anxious at left_small
    with dissolve
    x "(After a while they stopped touching me for a moment. I knew the next phase of their assault was coming.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(But I was excited and looking forward to it. I was ready for whatever they had in store for me next.)"
    
    show madd shocked at left_small
    with dissolve
    x "(Suddenly, they started kissing me again. Brother's hand came across my neck in a dominant way while my StepFather's hand reached out to my shorts again.)"
    
    show madd trembling at left_small
    with dissolve
    x "(I felt force on my neck and my ass as they both lifted me up into the air, holding me in their arms as they continued to kiss me passionately.)"
    x "(I can't believe they were so strong, they were able to lift me up so easily.)"

    scene cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_lift_2
    with fade
    
    show madd helpless at left_small
    with dissolve
    x "(I was now completely at their mercy. I was in the air, held by both of them, completely vulnerable and exposed to their touch and their lustful gazes.)"
    x "(Dad lifted my legs up. Now they were on his shoulders, while Brother was holding my upper body, his hand still on my neck as they continued to kiss me passionately.)"

    scene cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_lift_3
    with fade
    
    show madd violated at left_small
    with dissolve
    x "(Now with my legs on his shoulders, I knew this was a sign to him that I was his. I was his property, and I belonged to him.)"
    x "(Dad's hand moved down to my ass again, and he was rubbing my ass again.)"
    
    show madd horrified at left_small
    with dissolve
    x "(I knew he was priming me for something. I wasn't ready to be bred yet. I don't wanna end up pregnant.)"
    
    show madd anxious at left_small
    with dissolve
    x "(I was still enjoying the moment, but I was also scared and nervous about what might happen next.)"
    
    scene cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_lift_madd_naked
    with fade
    
    show madd shocked at left_small
    with dissolve
    x "(StepDad's hand moved down to my shorts again. This time he started pulling them, and they slid through my legs that were on his shoulders, exposing my bare ass to both of them.)"
    
    show dad hungry at right_small
    with dissolve
    show madd trembling at left_small
    with dissolve
    x "(I saw the hunger in his eyes as he knew I was vulnerable and exposed to him.)"


    scene cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_lift_madd_naked_dad_removes_shorts
    with fade
    
    show madd horrified at left_small
    with dissolve
    x "(Now that my ass were exposed, his hand moved down to his own shorts. He pulled them down and exposed his own hard dick.)"
    x "(The whole time his face was still kissing me but I could feel his dick was now out in the open based on the temperature change in the air.)"
    
    show dad lustful at right_small
    with dissolve
    dad_says "Ready for me, Maddie?"
    
    show madd trembling at left_small
    with dissolve
    x "(I was trembling with a mix of fear and excitement. I knew what was coming next, but I wasn't sure if I was ready for it.)"
    x "Please, Dad....Take my ass...not my pussy...I don't wanna get pregnant..."
    
    show dad coercive at right_small
    with dissolve
    x "(I was begging him, trying to negotiate with him.)"
    dad_says "Tch, you know I want to breed you, and I want to breed you in your pussy, but if you don't wanna get pregnant, then I guess I'll have to use your ass instead."
    
    show madd shocked at left_small
    with dissolve
    x "(I was surprised by his response. I didn't expect him to be so understanding and accommodating, but at the same time, I was also scared and nervous about what might happen next.)"

    scene cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_lift_madd_lowered_on_to_dad
    with fade
    
    show madd paralyzed at left_small
    with dissolve
    x "(Without saying anything else, my StepFather lowered me down onto his hard dick, his hand still on my ass as he guided me down onto him.)"
    
    show madd distressed at left_small
    with dissolve
    x "(I was now impaled on my StepFather's dick. I could feel every inch of him inside me, filling me up completely.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(I felt it growing inside me, stretching out my butthole as it went deeper and deeper inside me. I was both in pain and pleasure at the same time.)"
    x "(His mouth was still on mine, consuming my lips and my tongue with his own.)"
    
    show madd shocked at left_small
    with dissolve
    x "(To my surprise, my StepBrother was pushing me back and forth on my StepFather's dick.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(He was helping out his Dad, huh. The rhythm of Dad impaling me and my StepBrother pushing me back and forth was actually pretty good. It was making me feel really good.)"
    x "( I was really enjoying the sensation of being impaled on my StepFather's dick while being pushed back and forth by my StepBrother.)"


    scene cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_lift_madd_lowered_on_to_dad_2
    with fade
    
    show madd overwhelmed at left_small
    with dissolve
    x "(I was now completely lost in the sensations, the pleasure and the pain.)"
    x "( Being sandwiched between my StepFather and StepBrother while being impaled on my StepFather's dick was an experience unlike anything I had ever felt before.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I was moaning and crying out in pleasure as my StepFather continued to thrust into me.)"
    x "(But my moans were going inside StepDad's mouth as he continued to kiss me passionately. In return, his saliva was filling my mouth.)"
    
    show madd distressed at left_small
    with dissolve
    x "(He picked up the pace. I feel like his dick was hitting the deepest part of my butthole now. It was making me feel so full and so good at the same time.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I couldn't hold back anymore. The submissiveness and obedience to my StepFather and StepBrother was overwhelming me.)"
    
    show madd shocked at left_small
    with dissolve
    x "(Suddenly I felt a wave of pleasure building up inside me as liquid came gushing out of my body. I was cumming hard, my whole body was shaking with pleasure as I came on my StepFather's body.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(He was still inside my butthole, his dick throbbing inside me as he continued to thrust into me, prolonging my orgasm and making it even more intense.)"
    x "(The liquid lubricated my butthole, making it easier for my StepFather to continue thrusting into me.)"
    x "(The sound of skin on skin changed. It was now more of a wet slapping sound.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(The whole room was silent other than the sound of my moans and my StepFather's thrusting into me lubricated by my cum.)"
    
    show madd horrified at left_small
    with dissolve
    x "(Oh god, he made me cum...They both know it...They can hear it...Dad can feel it.)"
    
    show madd resigned at left_small
    with dissolve
    x "(There is no going back now. I am completely at their mercy. I am their submissive little plaything, and I belong to them.)"


    scene cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_lift_madd_lowered_on_to_dad_climax
    with fade
    
    show madd overwhelmed at left_small
    with dissolve
    x "(Noticing that I came hard, my Dad's dick was throbbing much more now. He was close to climaxing as well, and I knew it was coming soon.)"
    
    show madd distressed at left_small
    with dissolve
    x "(Suddenly my StepFather's thrusts became more erratic and more forceful, as I felt thick warm liquid filling up my butthole. It was his cum, filling me up completely as he climaxed inside me.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I could feel it gushing into me, my body was shaking with pleasure as I was being filled up with my StepFather's cum.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I should be ashamed of myself, should be scared of what just happened, but instead I was enjoying the moment.)"
    
    show madd overwhelmed at left_small
    with dissolve
    x "(My butthole was greedily accepting my StepFather's cum, but it was too much for it to handle, and some of it started to leak out of me, dripping onto the floor below.)"
    
    show madd conflicted at left_small
    with dissolve
    x "(I was loving the sensation!)"
    
    show madd resigned at left_small
    with dissolve
    x "(Pinned between Dad and Brother, covered in their saliva with Dad's cum swimming in my butthole, I was in a state of pure bliss. I was completely at their mercy, and I loved it.)"
    x "(I could smell the scent of my StepFather's cum on me. It was a mix of his saliva and his cum.)"
    x  "( It was a scent that I had come to associate with pleasure and submission, and I found myself getting aroused just by the smell of it on me.)"
    
    show madd helpless at left_small
    with dissolve
    x "(After a while, my StepFather finally pulled out of me, leaving me feeling empty and yet still filled with the sensation of his cum inside me.)"
    
    show madd resigned at left_small
    with dissolve
    x "(I was now completely spent. I was exhausted from the intense experience, but I was also satisfied and content in a way that I had never felt before.)"
    x "(Both my StepBrother and StepFather left me alone in the kitchen. )"
    x "(They went back to their own activities, as I cleaned up the mess and finished cooking dinner, trying to process everything that had just happened and what it meant for my relationship with them moving forward.)"
    
    # Update stats based on acts performed
    $ madd_willpower = max(0, madd_willpower - 40)
    $ character_relations["dad"]["intimacy"] +=9
    $ character_relations["brother"]["intimacy"] +=5
    $ character_relations["dad"]["kissed"] += 1
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["anal_sex"] += 1
    $ character_relations["dad"]["anal_creampie"] += 1
    $ character_relations["dad"]["lust"]=0
    $ character_relations["dad"]["anger"]=0
    $ character_relations["brother"]["kissed"] += 1
    $ character_relations["brother"]["groped_madd"] += 1
    $ character_relations["brother"]["touched_madd"] += 1
    
    $ journal_event_set_done("Dad","Sandwich in the Kitchen") 
    # Show stat notifications
    show screen stat_notification
    $ stat_notification = "Willpower -40"
    pause 4.0
    $ stat_notification = ""
    hide screen stat_notification
    
    show screen stat_notification
    $ stat_notification = "Intimacy with Dad +15"
    pause 4.0
    $ stat_notification = ""
    hide screen stat_notification
    
    show screen stat_notification
    $ stat_notification = "Intimacy with Brother +10"
    pause 4.0
    $ stat_notification = ""
    hide screen stat_notification

    $ family_meal_prepared += 1
    call advance_time_and_check(minutes=120) 

    $ dad_anal_scene_completed = True
    $ brother_watched_madd_anal_with_dad = True

    jump home_areas


label cooking_for_family_brother_and_dad_join_dad_only_vaginal:
    scene cooking_for_family_brother_and_dad_join_dad_only_dad_shouts_at_brother
    with fade

    show madd shocked at left_small
    with dissolve
    x "(While I was sandwiched between my brother and Dad, my Dad suddenly shouted at my brother to get out of the kitchen and leave us alone.)"

    show dad dominant at right_small
    with dissolve
    dad_says "Step back. She's mine."

    show madd trembling at left_small
    with dissolve
    x "(My Dad's voice was so loud and commanding that even my brother was frightened and stepped back. I heard his footsteps as he left the kitchen.)"
    x "(I knew things would only escalate from here, and I was right. My Dad's eyes were filled with lust and desire as he looked at me.)"

    hide dad
    show madd paralyzed at left_small
    with dissolve
    x "(He continued kissing my lips passionately while lifting my whole body with his strong arms.)"

    scene cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_spanks_madd
    with fade

    show madd conflicted at left_small
    with dissolve
    x "(He lifted me a little higher and then started spanking my behind with his hand, making me moan in pleasure.)"

    show dad sadistic at right_small
    with dissolve
    dad_says "Ah, Maddie... you make me so horny when you moan like that. You're such a good girl."

    show madd flustered at left_small
    with dissolve
    x "(He continued spanking me and kissing my mouth while I moaned louder and louder.)"

    scene cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_spanks_madd_2
    with fade

    show madd overwhelmed at left_small
    with dissolve
    x "(He got rougher with my whole body and I was loving every second of it.)"

    show dad predatory at right_small
    with dissolve
    x "(He was stretching the skin on my thighs while spanking my behind, and the whole time I was suspended in the air as he held me up effortlessly.)"

    hide dad
    show madd resigned at left_small
    with dissolve
    x "(I hated that I was letting this happen. I hated even more that part of me didn't want it to stop.)"

    scene cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_spanks_madd_3
    with fade

    show madd horrified at left_small
    with dissolve
    x "(He lifted me up even higher with my legs on his shoulders now.)"
    x "(Instead of spanking he started rubbing my behind in slow circles.)"

    show dad possessive at right_small
    with dissolve
    dad_says "I'm going to breed you, Maddie. My seed will fertilize your egg before dinner tonight ."

    show madd horrified at left_small
    with dissolve
    x "(I was surprised at how easily he could lift me up, and I was shocked at how aroused I was getting from all of this.)"

    show dad delusional at right_small
    with dissolve
    dad_says "Tonight you will eat the food while my cum swims inside you."

    show madd resigned at left_small
    with dissolve
    x "(All of this was so degrading, but somehow it made me even more obedient to him.)"

    scene cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_spanks_madd_4
    with fade

    show madd conflicted at left_small
    with dissolve
    x "(Slowly I was lowered again with my legs by his sides, trapped under his arms, my behind still being rubbed by him.)"
    x "(My body was fully accepting him — his touch, his smell, his claim on me.)"

    show dad obsessed at right_small
    with dissolve
    x "(I was in the kitchen moaning loudly. I was sure my brother could hear me from wherever he was.)"

    show madd resigned at left_small
    with dissolve
    x "(I was so turned on and submissive to my Dad that I didn't care if my brother or the whole town heard me.)"

    hide dad

    scene cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_spanks_madd_5
    with fade

    show madd flustered at left_small
    with dissolve
    x "(His pace slowed down completely.)"
    x "(He carried me over to the chair at the table and sat down with me on his lap.)"
    x "(I instinctively spread my legs for him. Now I was sitting on his lap with my legs around his waist.)"

    show madd horrified at left_small
    with dissolve
    x "(I knew the position I was in. I knew this would give him direct access to my pussy, but I wanted it.)"
    x "(His degrading words and actions were making me want to do those very things even more.)"

    scene cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_sitting_on_chair_madd_on_lap_1
    with fade

    show madd nervous at left_small
    with dissolve
    x "(He kissed and rubbed my behind one more time before looking up at me.)"

    show dad smirk at right_small
    with dissolve
    dad_says "How do you feel, Maddie?"

    show madd flustered at left_small
    with dissolve
    x "(He then started kissing my mouth again, his tongue sliding in before I could say a single word.)"
    x "(He was preparing me for what was about to happen next.)"
    x "(He pulled back from the kiss and said—)"

    show dad hungry at right_small
    with dissolve
    dad_says "How do you like being on my lap? You'll be Daddy's little girl tonight."

    show madd deep blush at left_small
    with dissolve
    x "(My heart skipped a beat at his words.)"

    hide dad

    scene cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_sitting_on_chair_madd_on_lap_2
    with fade

    show madd trembling at left_small
    with dissolve
    x "(He pulled away from the kiss again, then gently pulled my hair back.)"
    x "(I knew he was going for my neck next, so I obliged and tilted my head back, exposing my neck to him.)"

    show dad yearning at right_small
    with dissolve
    dad_says "You taste so good, Maddie..."

    show madd conflicted at left_small
    with dissolve
    x "(He started licking my neck and I felt like I was in bliss.)"

    hide dad

    scene cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_sitting_on_chair_madd_on_lap_3
    with fade

    show madd conflicted at left_small
    with dissolve
    x "(He was slow with his approach — gentle, perhaps because he wanted to savour the moment, or maybe because he wanted to make sure I was fully ready for him.)"
    x "(Maybe this is how he treats someone he thinks is his wife... much more tender than he treats me usually...)"

    show dad possessive at right_small
    with dissolve
    x "(With his hand behind my neck holding me in place, his tongue ran all over my neck and collarbone. I was in heaven.)"

    show madd resigned at left_small
    with dissolve
    x "(I couldn't tell any more whether I was drowning in shame or pleasure. Both felt the same.)"

    hide dad

    scene cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_sitting_on_chair_madd_on_lap_4
    with fade

    show madd horrified at left_small
    with dissolve
    x "(I was like a feast laid out before him — and like real food, I had no choice but to be devoured by him.)"

    show dad dominant at right_small
    with dissolve
    dad_says "Oh, Maddie... I can't get enough of you..."
    x "(He would take intermittent licks between his words.)"
    dad_says "Your body... it's so inviting."

    show madd resigned at left_small
    with dissolve
    x "(Every word he said landed somewhere inside me.)"

    show dad delusional at right_small
    with dissolve
    dad_says "No man could resist you, Maddie. I want to breed you every day until you're pregnant with my child, and then I'll breed you some more after that."
    dad_says "The only way to keep you from other men is to keep you pregnant with my child... and I will do just that."

    show madd resigned at left_small
    with dissolve
    x "(I was so turned on and submissive to him that I didn't care about the nature of this relationship or the fact that I was being treated like a piece of meat.)"
    x "(I knew that he was right... and somehow, hearing it out loud only made it worse — because part of me agreed.)"

    hide dad

    scene cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_sitting_on_chair_madd_on_lap_5
    with fade

    show madd paralyzed at left_small
    with dissolve
    x "(He licked my neck some more before saying—)"

    show dad predatory at right_small
    with dissolve
    dad_says "Now prepare yourself, Maddie... I can't hold back any more."
    dad_says "I'm going to cum inside you right here on my lap. Let your brother hear you moan for me. I want him to know that you belong to me and only me."

    if character_relations["dad"]["intimacy"] < 80:
        if character_relations["dad"]["vaginal_sex"]<1 and madd_is_virgin: 
            x "(NO NO no , i am still a virgin... I can't let them do this to me... )"
            x "Please stop this! Please don't do this to me!"
            show madd horrified at left_small
            dad_says "Shut up, Maddie... you are going to enjoy this whether you like it or not..."
            show madd conflicted at left_small
            x "(I have to be tough on him, I have to let him know the consequences..."
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
                x "(I have no choice but to comply with his demands, i have to let fck me raw ...its all over if i end up in jail)"
            else :
                dad_says "Fucking buzz kill , Just wait till i catch some dirt on you and then i will make you scream for me"
                x "(suprisingly he let his grip loose on me and i got off his lap and stood up , he was looking at me with a seriously angry expression)"
                x "(This is gonna make him so mad...)"
                x "(I hurried up outside to the main lobby..)"
                call advance_time_and_check(minutes=120)
                $ madd_willpower = max(0, madd_willpower - 20)
                jump home_areas



    show madd distressed at left_small
    with dissolve
    x "(After saying that he started removing my shorts. I didn't resist him at all — I just let him do whatever he wanted to me.)"

    hide dad

    $ brother_hears_madd_moan = True

    scene cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_sitting_on_chair_madd_on_lap_madd_naked
    with fade

    show madd trembling at left_small
    with dissolve
    x "(The cold air of the kitchen hit my exposed pussy and I shivered with anticipation, knowing it wouldn't be cold for much longer.)"
    x "(Soon it would be filled with my Dad's warmth, and I would have no say in the matter because I was his property.)"

    show dad hungry at right_small
    with dissolve
    dad_says "I can feel you shivering, Maddie... I know you're ready for me."

    show madd resigned at left_small
    with dissolve
    x "(After saying that he started removing his pants and underwear.)"

    hide dad

    scene cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_sitting_on_chair_madd_on_lap_madd_naked_dad_naked
    with fade

    show madd paralyzed at left_small
    with dissolve
    x "(Once his pants and underwear were off I couldn't see his dick yet, but I could feel its heat radiating up toward me.)"
    x "(I was on his lap and his dick was right beneath my pussy. I knew it was aching to get inside me.)"
    x "(I was hugging him tightly like a child hugging a parent for comfort — except that parent was about to use that closeness entirely for his own pleasure.)"

    show madd horrified at left_small
    with dissolve
    x "(My whole body was sweating. I knew it was only a matter of time before he would start thrusting inside me.)"
    x "(And I clung to him, holding him tightly.)"

    scene cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_sitting_on_chair_madd_on_lap_madd_naked_dad_naked_vaginal_penetration
    with fade

    show madd overwhelmed at left_small
    with dissolve
    x "(Finally he started moving. He lifted my hips up slightly and shifted his own so that his dick was right at the entrance of my pussy.)"
    x "(I could feel the head of it pressing against me, and I was so wet that it just slid in without any resistance.)"

    if madd_is_virgin:
        x "(It tore. A sudden, ugly rip deep inside me as the head forced its way through. My dad's cock just broke my hymen while I was sitting on his lap in the kitchen.)"
        x "(I felt the sharp sting as he kept lowering me, pushing through the fresh tear. Something warm and wet leaked out around him — blood. I could feel it dripping down his shaft and onto his balls.)"
        x "(He didn't stop. He kept pulling me down until I was fully seated on him, his cock buried all the way inside my no longer virgin pussy. I could feel every inch of him stretching the fresh wound he just made.)"
        dad_says "There it is… fuck. I just took your virginity Maddie. You will definitely never forget this."
        x "(My hands were gripping his shoulders so tight my nails dug into his skin. I couldn't move. Couldn't think. All I could feel was the thick, hot length of him inside me and the slow trickle of blood running down between us.)"
        x "(The shame hit me so hard I almost couldn't breathe. He was still holding my hips down, keeping me impaled on him while he talked about my mom. I could feel his cock twitching inside the torn, bleeding mess he'd just made.)"
        dad_says "No more pretending you're innocent now. This cunt's mine. I popped it right here in the kitchen . You're never getting this back."
        $ madd_is_virgin=False

    show dad dominant at right_small
    with dissolve
    x "(And then it finally happened. He slid inside me and I felt a wave of pleasure hit me all at once.)"

    show madd overwhelmed at left_small
    with dissolve
    x "(I felt as though an empty void inside me was finally being filled and I was being made whole.)"
    x "(I wanted to scream with pleasure but all I could do was moan and whimper as he started thrusting inside me.)"
    x "(He was moving at a slow, steady pace... for now, at least.)"

    hide dad

    scene cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_sitting_on_chair_madd_on_lap_madd_naked_dad_naked_vaginal_penetration_2
    with fade

    show madd conflicted at left_small
    with dissolve
    x "(He started moving his hips faster and harder, making his dick go deeper inside me with each thrust.)"
    x "(Every time he went all the way in I felt this surge of panic and pleasure at the same time.)"
    x "(Being with Dad was like being on a rollercoaster of emotions — one moment I hated him for what he was doing to me, and the next I was loving him for the very same thing.)"

    show madd resigned at left_small
    with dissolve
    x "(Earlier I was so against the idea of even him touching me.)"
    x "(But now I wanted him inside me. I wanted him to use me for his pleasure. I wanted to be his — in every shameful and unforgivable way that word implied.)"

    scene cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_sitting_on_chair_madd_on_lap_madd_naked_dad_naked_vaginal_penetration_3
    with fade

    show madd distressed at left_small
    with dissolve
    x "(He continued with a relentless pace, pounding into me without letting up.)"

    show dad sadistic at right_small
    with dissolve
    dad_says "You like it, Maddie? You like being fucked by your Daddy?"

    show madd resigned at left_small
    with dissolve
    x "(I was so overloaded with pleasure that I could barely form words to answer him.)"
    x "(I just grunted in pleasure and nodded my head.)"

    show dad mocking at right_small
    with dissolve
    dad_says "That's right, Maddie... you know you love it."
    dad_says "If you were my wife I would take you like this every single day..."
    dad_says "I would sleep with my dick buried deep inside you every night. You would wake up with it still inside you."
    dad_says "You would serve me like a good little wife and your place would be between my legs..."
    dad_says "You would lick my feet and worship me, and as your reward I would make you drink my piss and swallow my cum every single day..."

    show madd violated at left_small
    with dissolve
    x "(GOD — all these words were so degrading, but why do they make me want to do those things even more?)"
    x "(Why do they feel so good to hear? My mind is so messed up.)"
    x "(Hearing that, I instinctively started moaning louder and louder.)"

    hide dad

    scene cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_sitting_on_chair_madd_on_lap_madd_naked_dad_naked_vaginal_penetration_4
    with fade

    show madd conflicted at left_small
    with dissolve
    x "(At this point even I was surprised at how much I was enjoying this. My hips started moving in sync with his thrusts.)"
    x "(I was grinding myself against my Dad's dick while he was thrusting inside me.)"

    show madd distressed at left_small
    with dissolve
    x "(That's when I heard footsteps coming from the direction of the kitchen door. I knew it was my brother coming back.)"

    show dad controlling at right_small
    with dissolve
    dad_says "Ah... there you are, Adam."

    show brother fixated at right_small
    with dissolve
    x "(As soon as he said that, he started thrusting even harder and faster inside me. He wanted to show my brother that I was his property and that he could do whatever he wanted to me, whenever he wanted.)"

    hide brother
    show madd distressed at left_small
    with dissolve
    x "(I was facing away from the door so I couldn't see my brother's reaction, but all I could do was moan louder.)"

    show dad mocking at right_small
    with dissolve
    dad_says "You hear that? Hear how she moans like a bitch in heat..."

    show madd distressed at left_small
    with dissolve
    x "(I was whimpering and moaning in pleasure while my Dad was pounding into me and talking about me like I was a piece of meat in front of my brother.)"
    x "(I should have been mortified by this but I let him say whatever he wanted.)"
    $ brother_hears_madd_moan= True

    show dad dominant at right_small
    with dissolve
    dad_says "Watch closely, Adam... watch as I impregnate your sister with my cum right here."

    show madd shocked at left_small
    with dissolve
    x "(Eh? Is he really going to do that right here in front of my brother?)"

    hide dad

    scene cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_sitting_on_chair_madd_on_lap_madd_naked_dad_naked_vaginal_penetration_5
    with fade

    show madd overwhelmed at left_small
    with dissolve
    x "(He continued thrusting his dick inside me with a relentless pace... and finally I felt the familiar sensation of his dick throbbing inside me as he was about to cum.)"
    x "(His dick was growing even harder and bigger inside me as he was about to cum.)"
    x "(And finally it happened.)"

    show dad predatory at right_small
    with dissolve
    dad_says "I'm going to breed you now, Maddie..."

    show madd overwhelmed at left_small
    with dissolve
    x "(As soon as he said that I felt hot spurts of his cum shooting inside me... going to the deepest parts of my pussy and filling me up with his cum.)"
    x "(When I felt his cum filling me up I was in a state of pure bliss... I made a sound that was a mixture of a moan and a scream... I was so overwhelmed with pleasure that I couldn't even form words to express how I felt.)"

    show madd conflicted at left_small
    with dissolve
    x "(He kept moving his hips inside me even after he started cumming... it didn't end, he kept cumming inside me and thrusting.)"
    x "(I was so full of his cum that I felt like I was going to burst... I felt parts of his cum leaking out of my pussy.)"

    show dad sadistic at right_small
    with dissolve
    dad_says "See how much she loves being filled with my cum, Adam? She is Daddy's little cum dumpster..."

    show madd resigned at left_small
    with dissolve
    x "(I had no energy left to care about what he was saying or doing at this point... I was just basking in the pleasure.)"
    x "(I wanted to stay in this position forever... being in his lap with his dick buried deep inside me and his cum filling me up.)"

    scene cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_sitting_on_chair_madd_on_lap_madd_naked_dad_naked_vaginal_penetration_dad_show_madd_vagina
    with fade 

    show dad dominant at right_small
    with dissolve
    x "(Suddenly he pulled out of my which made me feel empty then I felt his hand on my hips as he spread my legs apart )"
    x "(He was showing my naked wet pussy which was full of his cum and still dripping to my brother)"
    x "(I felt like a dog who was pissing in front of her 2 owners ...which wasnt far from reality. I was a bitch of these 2 men )"
    dad_says "See that? How her body swallowed my cum so well? A few more days of fucking her and she will be pregnant with my child... and then I will breed her some more after that."

    show brother shocked at right_small
    with dissolve
    x "( I heard footsteps again, but this time they were going away from the kitchen door. I knew it was my brother leaving.)"
    x "(He must have been defeated by the sight of his sister being fucked by his Dad and getting bred by him right in front of him.)"

    hide brother
    show dad laugh at right_small
    with dissolve
    dad_says "Ha ha ha... I'm sure your brother is going to be pissed now, Maddie."

    show madd broken at left_small
    with dissolve
    x "(I was out of breath... my body was trembling with pleasure and exhaustion.)"

    show dad possessive at right_small
    with dissolve
    dad_says "I'm tired now, Maddie... I no longer need to eat food... I feel satisfied now that I have filled you up with my cum. I'm going to go back to my room and rest now."

    show madd submissive nod at left_small
    with dissolve
    x "(I just nodded my head... if I said any words that would make it very clear that I was enjoying this, and that would be very bad for me.)"
    x "(He would take me for a wife and he would sleep with me every night.)"

    show dad dominant at right_small
    with dissolve
    dad_says "Remember, Maddie... you belong to me... you are my property... and you better start acting like it from now on."

    show madd resigned at left_small
    with dissolve
    x "(I nodded my head again... gently this time.)"

    hide dad
    show madd broken at left_small
    with dissolve
    x "(He finally stood up and let me down from his lap, and then he started getting dressed again.)"
    x "(Cum was still leaking out of my pussy and onto the chair and the floor... if he hadn't been there I would have licked it up.)"

    show madd processing at left_small
    with dissolve
    x "(With that he left the kitchen and went to his room. I was left standing there with my legs still spread apart and my pussy still leaking his cum. I was in a daze... I didn't know what to do or how to react to all of this.)"

    call advance_time_and_check(minutes=240)

    # Stats update after vaginal sex + creampie scene
    $ madd_willpower = max(0, madd_willpower - 40)
    $ character_relations["dad"]["intimacy"] +=11
    $ character_relations["dad"]["dominance"] = min(character_relations["dad"]["dominance"] + 10, 100)
    $ character_relations["dad"]["kissed"] += 1
    $ character_relations["dad"]["groped_madd"] += 1
    $ character_relations["dad"]["touched_madd"] += 1
    $ character_relations["dad"]["undressed_madd"] += 1
    $ character_relations["dad"]["vaginal_sex"] += 1
    $ character_relations["dad"]["vaginal_creampie"] += 1
    $ character_relations["dad"]["lust"] = 0
    $ character_relations["brother"]["touched_madd"] += 1
    $ character_relations["dad"]["anger"]=0
    $ journal_event_set_done("Dad","Bred in the Kitchen")
    
    call advance_time_and_check(minutes=120)
    $ brother_watched_madd_vaginal_with_dad = True
    $ madd_is_virgin = False
    $ family_meal_prepared += 1

    jump kitchen_scene

label cooking_for_family_finish:

    scene scene_kitchen_cooking_for_family_solo_madd
    with fade
    
    show madd rbf at left_small
    with dissolve
    x "(I finished cooking the meal for my StepFather and StepBrother.)"
    x "(The food is ready. I should serve it to them.)"
    
    
    $ family_meal_prepared += 1
    call advance_time_and_check(minutes=60) from _call_advance_time_and_check_cooking_family
    
    jump home_areas

# ════════════════════════════════════════════
#  Cuisine - Peek & Grope
# ════════════════════════════════════════════

label rockygropelinkitchenntr:
    python:
        if game_time.is_morning():
            home_kitchen = "kitchenmor"
        elif game_time.is_afternoon():
            home_kitchen = "kitchenaft"
        elif game_time.is_evening():
            home_kitchen = "kitcheneve"
        else:  # night
            home_kitchen = "kitchennig"

    scene expression home_kitchen
    "Je me dirige vers la cuisine."
    scene rockylindsaykitchengrab
    if lindscorr != game_time.day:
        p "(Oh Rocky et Lindsay sont là, ils sont fort proche... je vais regarder.)"
        p "(Il l'a touche ???)"
        p "(Et elle dit rien ???)"
        $ persistent.linds_corruption = getattr(persistent, 'linds_corruption', 0) + 1
        $ lindscorr = game_time.day
        jump home_areas   
    else:
        p "(Il est encore occuper...)"
        jump home_areas

label rockylindsaykitchentalk:
    python:
        if game_time.is_morning():
            home_kitchen = "kitchenmor"
        elif game_time.is_afternoon():
            home_kitchen = "kitchenaft"
        elif game_time.is_evening():
            home_kitchen = "kitcheneve"
        else:  # night
            home_kitchen = "kitchennig"

    scene expression home_kitchen
    "Je me dirige vers la cuisine."
    scene kitchenlindsrocky talk
    p "(Oh Rocky et Lindsay sont là, ils sont fort proche... je vais regarder.)"
    p "(1)"
    p "(2)"
    jump home_areas

label rockylindsaykitchentalk2:
    python:
        if game_time.is_morning():
            home_kitchen = "kitchenmor"
        elif game_time.is_afternoon():
            home_kitchen = "kitchenaft"
        elif game_time.is_evening():
            home_kitchen = "kitcheneve"
        else:  # night
            home_kitchen = "kitchennig"

    scene expression home_kitchen
    "Je me dirige vers la cuisine."
    scene kitchenlindsrocky talk2
    p "(Oh Rocky et Lindsay sont là, ils sont fort proche... je vais regarder.)"
    p "(1)"
    p "(2)"
    jump home_areas

label davetalklindskitchen:
    python:
        if game_time.is_morning():
            home_kitchen = "kitchenmor"
        elif game_time.is_afternoon():
            home_kitchen = "kitchenaft"
        elif game_time.is_evening():
            home_kitchen = "kitcheneve"
        else:  # night
            home_kitchen = "kitchennig"

    scene expression home_kitchen
    show dave happy at left_small
    with fade
    "Je me dirige vers la cuisine."
    scene lindsaykitchenpeek
    p "Coucou Lindsay."
    p "Elle m'a pas entendu, oh lala la vue"
    jump lindsay_kitchen_menu

label lindsay_kitchen_menu:

    menu:
        "Profiter":
            $ liste_videos = ["images/kitchen/kitchenlindsmor10.webm", "images/kitchen/kitchenlindsmor11.webm", "images/kitchen/kitchenlindsmor12.webm"]
            $ video_choisie = renpy.random.choice(liste_videos)
            $ renpy.movie_cutscene(video_choisie)
            p "Elle se lave les mains surement."
            jump lindsay_kitchen_menu   # ⬅️ Retour direct au menu

        "Parler à Lindsay":
            p "Coucou Lindsay."
            l "Ah coucou!"
            jump lindsay_kitchen_menu

        "Retour":
            jump home_areas

    