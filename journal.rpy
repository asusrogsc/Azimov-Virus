# Journal System -- journal.rpy
# Two sections: Characters (with per-character event pages) and Events.
# Each scene/event has a "done" flag; characters pages have Done/Available tabs.

init python:

    # ---------------------------------------------------------------
    # Data stores
    # ---------------------------------------------------------------
    journal_characters  = []   # [{name, portrait, desc, events:[...]}]
    journal_events_list = []   # [{name, desc, req, image, done}]

    # Mutable order counter — incremented each time an event changes state.
    # Stored as a single-element list so inner functions can mutate it without 'global'.
    _journal_order_counter = [0]

    # ---------------------------------------------------------------
    # Character functions
    # ---------------------------------------------------------------
    def journal_char_add(name, desc, portrait=""):
        """Register a character in the journal. Safe to call multiple times."""
        for char in journal_characters:
            if char["name"] == name:
                return
        journal_characters.append({
            "name":      name,
            "portrait":  portrait or "gui/journal_icon.png",
            "desc":      desc,
            "base_desc": desc,   # original description — never overwritten by events
            "events":    [],
        })

    def journal_char_set_desc(name, new_desc):
        """Update a character's base description text (call after relationship changes, etc.).
        The full displayed desc is rebuilt automatically from this base + completed events."""
        for char in journal_characters:
            if char["name"] == name:
                char["base_desc"] = new_desc
                _journal_rebuild_char_desc(name)
                return

    # ---------------------------------------------------------------
    # Character event (scene) functions
    # ---------------------------------------------------------------
    def journal_event_add(char_name, event_name, desc, req="", image="", done=False, hidden=False, char_thought=""):
        """Add a scene to a character's journal page.
        If the scene already exists it is updated in-place.
        done=True        -> immediately shows in the Done tab.
        done=False       -> shows in the Available tab.
        hidden=True      -> hidden from journal until journal_event_show() is called.
        char_thought     -> Madd's short personal thought appended to the character
                            description when this event is marked done.
        """
        for char in journal_characters:
            if char["name"] == char_name:
                for ev in char["events"]:
                    if ev["name"] == event_name:
                        ev["desc"]        = desc
                        ev["req"]         = req
                        ev["char_thought"] = char_thought
                        if image:
                            ev["image"] = image
                        return
                char["events"].append({
                    "name":        event_name,
                    "desc":        desc,
                    "req":         req,
                    "image":       image or char.get("portrait", "gui/journal_icon.png"),
                    "done":        done,
                    "hidden":      hidden,
                    "new":         False,
                    "order":       0,
                    "char_thought": char_thought,
                })
                return

    def _journal_rebuild_char_desc(char_name):
        """Rebuild a character's displayed description by appending Madd's personal
        thoughts (char_thought) from every completed event beneath the base description."""
        for char in journal_characters:
            if char["name"] == char_name:
                base = char.get("base_desc", char["desc"])
                done_evs = sorted(
                    [ev for ev in char.get("events", []) if ev.get("done", False) and ev.get("char_thought", "")],
                    key=lambda e: e.get("order", 0)
                )
                if done_evs:
                    parts = [base, ""]
                    for ev in done_evs:
                        parts.append(ev["char_thought"])
                    char["desc"] = "\n".join(parts)
                else:
                    char["desc"] = base
                return

    def _journal_save_ev(char_name, ev):
        """Write one event's mutable fields (done, hidden, order) into journal_save_state.
        Uses renpy.store for guaranteed store access from init python context.
        Does NOT save 'new' — that is tracked separately via journal_cleared_events.
        """
        new_state = dict(renpy.store.journal_save_state)
        new_state[char_name] = dict(new_state.get(char_name, {}))
        new_state[char_name][ev["name"]] = {
            "done":   ev["done"],
            "hidden": ev["hidden"],
            "order":  ev["order"],
        }
        renpy.store.journal_save_state = new_state
        renpy.store._journal_counter_store = _journal_order_counter[0]

    def _journal_toast_enqueue(char_name, event_name):
        """Queue a toast. Shows immediately if nothing is on screen, otherwise waits."""
        q = list(renpy.store.journal_toast_queue)
        q.append((char_name, event_name))
        renpy.store.journal_toast_queue = q
        if not renpy.get_screen("journal_toast") and not renpy.get_screen("journal_toast_delay"):
            _journal_toast_show_next()

    def _journal_toast_show_next():
        """Pop and display the next toast from the queue."""
        q = list(renpy.store.journal_toast_queue)
        if q:
            _cn, _en = q.pop(0)
            renpy.store.journal_toast_queue = q
            try:
                renpy.show_screen("journal_toast", char_name=_cn, event_name=_en)
            except Exception:
                pass

    def journal_event_set_done(char_name, event_name, done=True):
        """Mark a character scene as done. When done=True and not already done,
        marks as new and updates sort order. Re-calling with done=True on an already
        done event is a no-op so the NEW badge is not re-triggered."""
        for char in journal_characters:
            if char["name"] == char_name:
                for ev in char["events"]:
                    if ev["name"] == event_name:
                        if done and ev["done"]:
                            return  # already done — don't re-badge or reorder
                        ev["done"] = done
                        if done:
                            ev["hidden"] = False  # unhide if still hidden
                            _journal_order_counter[0] += 1
                            ev["order"] = _journal_order_counter[0]
                            ev["new"]   = True
                            _journal_toast_enqueue(char_name, event_name)
                        _journal_save_ev(char_name, ev)
                        _journal_rebuild_char_desc(char_name)
                        return

    def journal_event_show(char_name, event_name):
        """Make a hidden event visible in the journal, marking it as new."""
        for char in journal_characters:
            if char["name"] == char_name:
                for ev in char["events"]:
                    if ev["name"] == event_name:
                        if not ev.get("hidden", False):
                            return  # already visible — do nothing
                        ev["hidden"] = False
                        if ev.get("done", False):
                            # already done but was hidden (old-save edge case) —
                            # reveal silently: no new order, no badge, no toast
                            _journal_save_ev(char_name, ev)
                            return
                        _journal_order_counter[0] += 1
                        ev["order"]  = _journal_order_counter[0]
                        ev["new"]    = True
                        _journal_toast_enqueue(char_name, event_name)
                        _journal_save_ev(char_name, ev)
                        return

    def journal_char_has_new(char_name):
        """Return True if this character has any new (unseen) journal events."""
        ce = renpy.store.journal_cleared_events
        for char in journal_characters:
            if char["name"] == char_name:
                for ev in char.get("events", []):
                    if not ev.get("hidden", False):
                        key = char_name + "::" + ev["name"]
                        if ev.get("order", 0) > ce.get(key, 0):
                            return True
        return False

    def journal_any_new():
        """Return True if any character has new (unseen) journal events."""
        ce = renpy.store.journal_cleared_events
        for char in journal_characters:
            for ev in char.get("events", []):
                if not ev.get("hidden", False):
                    key = char["name"] + "::" + ev["name"]
                    if ev.get("order", 0) > ce.get(key, 0):
                        return True
        return False

    def journal_clear_new_for_char(char_name):
        """Mark all of a character's events as seen."""
        ce = dict(renpy.store.journal_cleared_events)
        for char in journal_characters:
            if char["name"] == char_name:
                for ev in char.get("events", []):
                    key = char_name + "::" + ev["name"]
                    ce[key] = ev.get("order", 0)
                renpy.store.journal_cleared_events = ce
                return

    def journal_event_clear_new(char_name, event_name):
        """Mark a single event as seen when the player opens its detail popup."""
        for char in journal_characters:
            if char["name"] == char_name:
                for ev in char.get("events", []):
                    if ev["name"] == event_name:
                        key = char_name + "::" + event_name
                        renpy.store.journal_cleared_events = dict(
                            renpy.store.journal_cleared_events,
                            **{key: ev.get("order", 0)}
                        )
                        return

    # ---------------------------------------------------------------
    # World Events section functions
    # ---------------------------------------------------------------
    def journal_world_event_add(name, desc, req="", image="", done=False):
        """Add an event to the global Events section."""
        for ev in journal_events_list:
            if ev["name"] == name:
                ev["desc"] = desc
                ev["req"]  = req
                if image:
                    ev["image"] = image
                return
        journal_events_list.append({
            "name":  name,
            "desc":  desc,
            "req":   req,
            "image": image or "gui/journal_icon.png",
            "done":  done,
        })

    def journal_world_event_set_done(name, done=True):
        """Mark a world event as done."""
        for ev in journal_events_list:
            if ev["name"] == name:
                ev["done"] = done
                new_state = dict(store.journal_save_state)
                world_dict = dict(new_state.get("_world", {}))
                world_dict[name] = {"done": done}
                new_state["_world"] = world_dict
                store.journal_save_state = new_state
                renpy.store._journal_counter_store = _journal_order_counter[0]
                return

    # ---------------------------------------------------------------
    # Legacy stubs -- keeps existing call-sites in other files safe
    # ---------------------------------------------------------------
    journal_scenes = []

    def journal_add(name, desc, req="", section="Events", image=""):
        pass

    def journal_remove(name):
        return False

    # ---------------------------------------------------------------
    # Seed characters (move these calls to the unlock scene files
    # once you wire up the meet triggers)
    # ---------------------------------------------------------------
    journal_char_add(
        "Lindsay",
        "C'est une femme que vous avez receuilli.",
        "images/LindsayPortrait/lindsay portrait.png",
    )

    # Lindsay events
    journal_event_add(
        "Lindsay",
        "Emplois du temps",
        "Entre 8h et 9h, Lindsay prendre sa douche.",
        "Entre 8h et 9h, Lindsay prendre sa douche.",
        "images/Dream_sequence/dream_sequence_2_moms_memory_brother_helps_mom_getting_roughed_up.jpg",
        done=False,
        hidden=True,
        char_thought="J'ai voulu entrer dans la salle de bain mais Lindsay y était déjà, je me demande si je peux en profiter...",
    )
    journal_event_add(
        "Lindsay",
        "Emplois du temps",
        "Entre 10h et 11h, elle est en cuisine.",
        "Entre 10h et 11h, elle est en cuisine.",
        "images/Dream_sequence/scene_notice_board_mom_obituary_memories_madd_finds_mom_body_2.JPG",
        done=False,
        hidden=True,
        char_thought="J'ai voulu entrer dans la salle de bain mais Lindsay y était déjà, je me demande si je peux en profiter...",
    )

    journal_event_add(
        "Lindsay",
        "Emplois du temps",
        "Entre 16h et 16h20, elle est dans la cour.",
        "Entre 16h et 16h20, elle est dans la cour.",
        "scene_madd_research_athome",
        done=False,
        hidden=True,
        char_thought="J'ai voulu entrer dans la salle de bain mais Lindsay y était déjà, je me demande si je peux en profiter...",
    )
    journal_event_add(
        "Lindsay",
        "Emplois du temps",
        "Entre 15h et 15h30, elle est dans le park.",
        "Entre 15h et 15h30, elle est dans le park.",
        "scene_madd_research_athome",
        done=False,
        hidden=True,
        char_thought="J'ai voulu entrer dans la salle de bain mais Lindsay y était déjà, je me demande si je peux en profiter...",
    )
    journal_event_add(
        "Madd",
        "Research: The Escape Budget",
        "I ran the numbers. Cram school entrance: 2,000 dollars. Hostel deposit: 800 dollars. Total needed: 2,800 dollars. I barely have anything. The only way to get that much fast is to steal the cash my stepfather hides around the house and work some petty jobs from brother or someone else. Once I'm out, I can work part-time to sustain myself. Maybe i would have to give in to brother's demands or dads demands",
        "I know which cram school and hostel I want to go to, so I can research how much money I need to escape. I have to be realistic about this",
        "scene_madd_research_athome",
        done=False,
        hidden=True,
        char_thought="I need 2,800 dollars to escape. I know My stepfather hides cash around this house and maybe brother has some money too. I'm going to find it and take it. Once I'm gone, I'm never coming back.",
    )
    journal_event_add(
        "Madd",
        "Dad Locks My Room",
        "Dad saw me and brother together. His punishment was immediate — he taped a note to my door and locked it. No key. No privacy. No sanctuary. The only places left to sleep are the living room, his room, or brother's room. There is no safe option. He's stripped away the last space that was mine.",
        "I think Dad saw me and brother together. I don't know what he saw or how much, but i need to get back to my room , outside is not safe anymore. ",
        "images/scene_home_lobby_area/scene_madd_door_locked_morning_afternoon.jpg",
        done=False,
        hidden=True,
        char_thought="He took my room. The one place I had to myself — gone. He left a note on the door like it was nothing. Now I have to choose between sleeping with him, sleeping with brother, or passing out on the sofa and hoping neither of them finds me. There's no good choice.",
    )
    journal_event_add(
        "Madd",
        "Redo Research: Cram School",
        "My room is locked and all my notes are trapped inside. I had to redo my cram school research using brother's computer while he snored next to me. I confirmed the same choice — Akira Cram School, 2,000 dollar entrance fee, 98 percent placement rate. Then he woke up and groped my breasts the whole time I was trying to finish. That's the price of using his computer.",
        "My room is locked and I lost all my research. I need to redo it using brother's computer — but using his things always costs something.",
        "images/BrotherScenes/scene_brother_room_morning_afternoon_madd_on_pc_madd_shocked_school_prices.JPG",
        done=False,
        hidden=True,
        char_thought="I lost everything when he locked my room. All my notes. All my progress. I had to start over, sitting at brother's computer while he squeezed my chest from behind and called it a fair trade.",
    )
    journal_event_add(
        "Madd",
        "Redo Research: Boys Hostel",
        "Second research session in brother's room. Girls hostels near Akira: 800 dollars a month. Boys hostels: 200 dollars. I confirmed my plan to disguise myself as a boy and use a fake identity. Brother found me mid-research, kissed me until I couldn't breathe, bit my neck, groped me, and licked me all over before going back to bed satisfied. The plan is worth it. This house isn't.",
        "I've confirmed the cram school. Now I need to redo the housing research in brother's room — and brace for whatever he decides to take as payment this time.",
        "images/BrotherScenes/scene_brother_room_morning_afternoon_madd_on_pc_research_2_pass_as_boy_thought.JPG",
        done=False,
        hidden=True,
        char_thought="I was staring at the screen deciding to live as a boy when his hands were suddenly in my hair. He kissed me, bit my neck, licked me until I was soaked in his saliva. Then he just went back to bed. I wiped my neck and kept researching.",
    )
    journal_event_add(
        "Madd",
        "Redo Research: Escape Budget",
        "Final research session — I ran the numbers again. 2,800 dollars total. I have barely anything. I'll need to steal what dad hides around the house. Brother demanded payment for the session: he pushed my face into his crotch and made me suck him off while gripping my hair. He came in my mouth and made me swallow all of it. I gagged. I swallowed. I kept the plan.",
        "I've done the cram school and hostel research. The last thing I need to redo is the budget calculation. Using brother's computer for research . With each session the price gets higher and higher. ",
        "images/BrotherScenes/scene_brother_room_morning_afternoon_r3_determined_to_leave.JPG",
        done=False,
        hidden=True,
        char_thought="2,800 dollars to escape. His cum still coating my throat as I wrote that number down. I know exactly what I need and exactly what it's costing me to figure it out. I'm doing it anyway.",
    )
    journal_event_add(
        "Madd",
        "Stealing the Keys",
        "The night I actually did it. I was wearing my brother's underwear against my bare skin — his sweaty boxers pressed against me as I moved through the dark house. His saliva still sticky on my neck and chest from an hour before. I pushed open Dad's bedroom door and stood there in the dark listening to him breathe. The man who has put his cock in my mouth, sat on my face, made me swallow his cum, and treated me like livestock — sleeping two feet away from me, completely unaware. I could feel his heat from across the room. I moved to the second drawer. My fingers found the keys immediately. Cold metal in my palm. I stood over him for a second longer than I needed to. Looking at him. Remembering every single thing he's done to me in this house. Then I walked out. I unlocked the front door and stepped into the night air and it hit my face like cold water. I was wearing my abuser's underwear. I had his cum coating the back of my throat from days prior. I was free.",
        "I Already know where main door's keys are . I need to pay Cram school fees from my computer or brothers computer and get some male clothes. All that's left is getting through the front door. Dad's keys are in his room. He's asleep. This is the moment everything has been building toward.",
        "scene_continue_runaway_preparation_brother_room_keys_from_dads_room",
        done=False,
        hidden=True,
        char_thought="I stood over him in the dark with his keys in my fist. His chest rising and falling. The same man who held my head down and made me his. I didn't wake him. I just took what I needed and walked out. His brother's underwear against my skin as I crossed the threshold into the open air. I was free. I am free.",
    )

    journal_char_add(
        "Rocky",
        "Your older brother. Entitled, manipulative, and watching your every move.",
        "images/brother/brother portrait.png",
    )
    journal_char_add(
        "LeVieu",
        "Your stepfather. Possessive and dangerous -- the walls he builds grow tighter every night.",
        "images/dad/dad portrait.png",
    )

    # Brother events
    ##################################################################
    ################################################################## 

    journal_event_add(
        "Brother",
        "Gaming Session (Event 1)",
        "He made me sit between his legs, said he was teaching me gaming. His arms wrapped around me as he \"guided\" my hands, pressing himself against my back. Then he shoved his hand under my shirt and touched my bare skin. I pushed him away and ran.",
        "Brother sleeps most of the day and morning, He's usually awake from evening to night. If I talk to him in his room when he's awake he might help me with my money problems...",
        "images/brotheroom/scene_brother_event1_hand_under_shirt.jpg",
        done=False,
        hidden=True,
        char_thought="He slid his hand under my shirt and groped my bare skin like he had every right to. He had me completely pinned between his legs — I couldn't move. He's getting bolder and I don't think I can stop him.",
    )
    journal_event_add(
        "Brother",
        "Bare Ass (Demands)",
        "He told me his demands—he wanted to touch my body. I let him, for 200 dollars. He wrapped his arms around me, pulled down my shorts, and spent what felt like an eternity kneading and squeezing my bare ass like it was his. When he finally let go he handed me the money and told me he'd pay a million if he could have my virginity. He clearly wants to do more than just touch me ",
        "After talking to brother more than twice I know he would offer me lots of money to let him touch me without any fabric in between...Why should i let him do that ? Not like I need anything from that money . Perhaps i should do some research on how i can escape this nightmare of a home",
        "images/brotheroom/brother_let_him_touch_bare_butt_5.jpg",
        done=False,
        hidden=True,
        char_thought="He pulled my shorts down and grabbed my bare ass with both hands like it was already his — kneading it, squeezing it, taking his time. He smiled the whole time. He told me he'd pay anything to take my virginity. He's not hiding what he wants anymore.",
    )
    journal_event_add(
        "Brother",
        "Bare Breast (Demands)",
        "He told me his demands—he wanted to touch my body. I agreed, for 200 dollars. He pulled my shirt off, sniffed it like a trophy, then squeezed my bare breast until I could feel every finger. He stared at my face the whole time, watching for pleasure. When it was finally over he paid me and told me it was a dream come true.",
        "After talking to brother more than twice I know he would offer me lots of money to let him touch me without any fabric in between...Why should i let him do that ? Not like I need anything from that money . Perhaps i should do some research on how i can escape this nightmare of a home",
        "images/brotheroom/brother_let_him_touch_bare_breast_pull_shirt_6.jpg",
        done=False,
        hidden=True,
        char_thought="He stripped my shirt off and buried his face in it before grabbing my bare breasts and squeezing them until it hurt. He stared into my eyes the whole time — he wanted to see what it did to me. He's treating my body like something he's entitled to unwrap.",
    )
    journal_event_add(
        "Brother",
        "Kitchen Ambush (Miss Event)",
        "He cornered me while I was cooking. He kissed and licked my neck, groped my breasts, lifted my shirt, and when I called him out he pulled his pants down and rubbed himself on my bare back until he finished. He left me there drenched and humiliated, telling me I smelled like him now.",
        "Ever since mom died , when  i cook in the kitchen at evening or night, brother walks in and just stares at me...i should be careful , if he ever loses control on himself he might end up escalating to something worse than just staring at me",
        "images/brotheroom/scene_miss_event_brother_misses_brother_rubbing_his_manhood_on_madd_2.jpg",
        done=False,
        hidden=True,
        char_thought="He cornered me, groped my breasts, yanked my shirt up — and when I pushed back he pulled himself out and used my bare back like I was nothing. He finished on me and told me I smelled like him now. He's completely lost whatever restraint he had.",
    )
    journal_event_add(
        "Brother",
        "Bathroom Ambush (Shower)",
        "He walked in while I was in just a towel—no knock, no apology. He gripped my shoulders, kissed my cheek, and when I told him to stop he tore it off me entirely and grabbed my bare breasts with both hands. He squeezed and stretched them, staring at my face the whole time, told me they were his and that one day he'd milk me like a cow. Then he threatened me so I wouldn't tell anyone, made me nod in agreement like a good girl, and finally walked away like nothing happened.",
        "Brother room is right next to the bathroom...I should be careful about when I shower. Especially during evening and night. If his lust gets too high he might not be able to control himself if he catches me there.",
        "images/homeshower/scene_brother_walks_in_home_bathroom_madd_in_towel_groped_by_brother_4.JPG",
        done=False,
        hidden=True,
        char_thought="He ripped the towel off me and grabbed my bare breasts with both hands — squeezing, stretching them, telling me they belonged to him. He looked me dead in the eyes and said one day he'd milk me like a cow. Then he threatened me into silence and walked away like he owned me. I nodded. I just... nodded.",
    )
    journal_event_add(
        "Brother",
        "Lap Trap (Event 2)",
        "He pulled me onto his lap, said it was to teach me. I was completely trapped in his arms. He groped my thighs, squeezed my ass through my clothes like it was nothing. When his hand reached my waistband and lowered my shorts exposing my butt but immediately after that something in me snapped and I finally managed to pull away.",
        "Brother sleeps most of the day and morning, He's usually awake from evening to night. If I talk to him in his room when he's awake he might help me with my money problems...",
        "images/brotheroom/scene_brother_event2_frozen_violation.jpg",
        done=False,
        hidden=True,
        char_thought="He had me locked on his lap, arms caged around me, hands all over my thighs and ass like I was his toy. He shoved his hand into my waistband and pulled my shorts down. He's stopped pretending. He takes what he wants now and expects me to just let it happen.",
    )
    journal_event_add(
        "Brother",
        "Ask to Sleep in Brother's Room",
        "My room was locked and I had nowhere else to go. I swallowed every bit of pride I had left and knocked on his door. He didn't even let me finish asking — he grabbed my waist and pulled me straight in. His tongue was on my neck before the door even closed. I paid in kisses, bites, and submission just for a place to sleep. He let me stay when he decided he'd taken enough.",
        "Now that my room is locked I have no place to sleep other than the living room, dad's room, or brother's room. If I need to ask him I should be prepared for what it's going to cost me.",
        "images/BrotherScenes/ask_brother_to_sleep_in_room_standing_face_to_face.JPG",
        done=False,
        hidden=True,
        char_thought="He pulled me in before I could finish the question. His hands were on my waist and his tongue was on my neck while I stood there bracing for it. I paid with my body just to have a place to sleep. And I'll have to do it again tomorrow.",
    )
    journal_event_add(
        "Brother",
        "Sofa Sleep",
        "I woke up with his weight pressing down on me and his saliva still wet on my neck. He had been there the whole time — kissing me, licking my neck, my armpit, touching me — while I slept without knowing. And when I finally opened my eyes, he was already sitting on top of me with that smile. I thought sleeping on the sofa would be the safe option.",
        "I will only sleep on the sofa in living room if i am very tired or i have no other place to sleep. Sleeping out in the open is a gamble — if brother finds me sleeping on the sofa he won't just walk past.",
        "images/Living room scenes/living_room_night_brother_next_to_madd_madd_sleeping_brother_climbs_to_face_first_blowjob_4.JPG",
        done=False,
        hidden=True,
        char_thought="I told myself sleeping on the sofa was safer. I woke up to him sitting on top of me, my whole body wet with fluid which was probably his saliva. I was wrong.",
    )

    journal_event_add(
        "Dad",
        "Dad Gropes: Shirt Lifted",
        "I went to ask Dad for money. He hugged me, started running his hands over my body, used Mom's death to guilt me, groped and squeezed my breasts repeatedly while I froze — then started lifting my shirt from the hem, inch by inch. He made it as slow and humiliating as possible. He offered me money if I'd sleep next to him and let him touch me like this whenever he wanted.",
        "I can talk to Dad in evening about getting some money , Perhaps he will give me some allowance but he might demand something of me .",
        "scene_dad_talk_event1_madd_and_dad_sitting_on_bed_hand_around_madd_hand_running_on_body_3",
        done=False,
        hidden=True,
        char_thought="He groped my breasts with both hands and squeezed them until I felt every finger, then started pulling my shirt up inch by inch while staring into my eyes. He used Mom's death as his excuse. He offered money if I'd just let him touch me whenever he wanted. I said no. But I could feel myself beginning to calculate.",
    )
    journal_event_add(
        "Dad",
        "Dad Gropes: Thigh Rub",
        "I sat next to him on the bed. He put his hand on my thigh without warning and started rubbing it slowly, comparing me to Mom the whole time. His eyes kept dropping to the gap between my shorts and my skin. When I finally got up and told him to stop, he barely reacted — just watched me leave.",
        "I can talk to Dad in evening about getting some money , Perhaps he will give me some allowance but he might demand something of me .",
        "images/dadroomscenes/scene_dad_talk_event2_madd_and_dad_sitting_on_bed_hand_around_madd_hand_running_on_thighs.jpg",
        done=False,
        hidden=True,
        char_thought="His hand was on my thigh the whole time he talked about how much I reminded him of Mom. He wouldn't stop staring between my legs. I had to stand up and say it out loud — stop touching me like that. He just looked at me. He's not embarrassed. He's patient.",
    )

    # Sample event seeded on Dad
    ##################################################################
    ################################################################## 
    journal_event_add(
        "Dad",
        "Room Cleaning Deal",
        "I asked Dad if I could earn money by cleaning his room. He agreed — 100 dollars a day. But the way he looked at me the whole time... possessive, calculating, comparing me to my mother. It's not just a cleaning job. I could feel it. Every word was a trap being set.",
        "Dad told me to clean his room , perhaps i could ask for some money while i clean it too",
        "scene_madd_dad_talk_first_maid_event_predatory_eyes",
        done=False,
        hidden=True,
        char_thought="He agreed to pay me 100 dollars a day to clean his room. He kept comparing me to my mother — the same woman he broke. I accepted anyway. I need the money. But I know this arrangement comes with a price I haven't been told yet.",
    )
    journal_event_add(
        "Dad",
        "Room Cleaning: Dusting & Groping",
        "He sent me under the bed to dust. While I was bent over, he grabbed my exposed ass with both hands — groping and squeezing. Then he slapped me. He said I sounded just like my mother. He's conditioning me, one cleaning session at a time.",
        "Now that I will be paid for cleaning dad's room perhaps i wont feel so bad doing it. I hope his lust doesnt come out seeing me clean...Last time he was comparing me with mom.",
        "scene_dad_room_cleaning_event_second_time_dust_under_bed_dad_grope_ass",
        done=False,
        hidden=True,
        char_thought="He shoved his hands down and grabbed my bare ass while I was helpless under the bed, then spanked me and compared the sound to my mother. He's treating this like a game he's already won.",
    )
    journal_event_add(
        "Dad",
        "Room Cleaning: Folding Clothes",
        "He made me fold his laundry — then forced me to hold each pair of socks and underwear to my nose and sniff. By the end I was shaking and disgusted... and something dark in me started to crave it. He told me tomorrow we'd do something more engaging.",
        "Now that I will be paid for cleaning dad's room perhaps i wont feel so bad doing it. I hope his lust doesnt come out seeing me clean...Last time he was comparing me with mom.",
        "dad_room_cleaning_event_second_time_clothes_underwear_sniff_open_underwear",
        done=False,
        hidden=True,
        char_thought="He made me sniff his dirty socks and underwear one by one while he watched. The worst part is something in me started to want more of his smell. He's rewriting me piece by piece.",
    )
    journal_event_add(
        "Dad",
        "Room Cleaning: Anger",
        "Right after I finished folding his clothes he snapped. He sat beside me, grabbed my jaw, pulled my shirt up and pushed his thumb deep into my mouth. He held me like that for ten minutes — groping me with one hand while I sucked. Something in me loved it. I hate myself for that.",
        "I noticed after i folded his clothes he looked at me with so much anger and lust in his eyes, he saw that his scent had an impact on me...I should be careful around him, if he is angry with me he might do something and blame it on his anger",
        "scene_dad_clean_smell_anger_event_1_thumb_inside_mouth",
        done=False,
        hidden=True,
        char_thought="He forced his thumb into my mouth and groped my bare skin while I just sat there and let it happen. Part of me stopped fighting. Part of me was excited. I don't know who I'm becoming.",
    )
    journal_event_add(
        "Dad",
        "Room Cleaning: Foot Cleaning",
        "After I finished he pressed his bare foot against my face. The smell was overwhelming — disgusting and somehow addictive. He pushed his toes into my mouth and held them there for ten minutes while I sucked like a pacifier. When he finally pulled away I felt the loss like something had been taken from me.",
        "Dad's been getting more and more aggressive, I believe he thinks its intimacy even though I try to keep him away. Well that intimacy is pretty high now . I dont know what else he might ask to clean after i clean his room",
        "images/dadroomscenes/dad_room_cleaning_event_clean_feet_dad_first_clean_my_feet_4.JPG",
        done=False,
        hidden=True,
        char_thought="His toes were in my mouth for ten minutes and I didn't want it to end. His foot had rewritten something in my brain. I got up feeling like I'd already been paid just from licking it. I'm terrified of what I'm becoming.",
    )
    journal_event_add(
        "Dad",
        "Room Cleaning: Armpit",
        "He called me close and pushed my face into his armpit, making me lick it clean. The smell hit me like a drug. He told me one day I'd be licking his ass sweat too. My body reacted with arousal. I had to physically pull away before I asked him to let me start right then.",
        "Dad's been getting more and more aggressive, I believe he thinks its intimacy even though I try to keep him away. Well that intimacy is pretty high now . I dont know what else he might ask to clean after i clean his room",
        "images/dadroomscenes/dad_room_cleaning_event_clean_armpit_sitting_on_bed_looking_at_stepdad_dad_raises_arm_madd_in_dads_armpit_2.JPG",
        done=False,
        hidden=True,
        char_thought="He made me lick his armpit clean and told me I'd be cleaning his ass next. My body was excited by the thought. I had to stop myself from begging him to let me do it right there. He's turned me into something I don't recognize.",
    )
    journal_event_add(
        "Dad",
        "Room Cleaning: Final Domination",
        "He climbed on top of me while I was under the table. Spanked me. Bit me. Licked me. Then pinned my head to the floor with his foot and took both holes without mercy. He made me beg to take his cum. I did. I passed out on his floor, leaking from everywhere, broken in a way I can't come back from.",
        "Dad gets more dangerous every cleaning session his so called intimacy with me keeps getting higher. At some point there wont be a line he hasn't crossed... I don't know what happens after that. Especially if he's angry at me, Even worst if he's angry and lustful.",
        "images/dadroomscenes/Clean event/scene_dad_room_cleaning_event_dusting_under_table_dad_on_top_of_madd_foot_on_madd_head_dad_pounding_madd_butt_16.JPG",
        done=False,
        hidden=True,
        char_thought="He used my body like property. Foot on my face, cum in both holes. He made me beg for it and I did. I passed out on his floor completely broken. This is the worst thing that has ever happened to me and my body betrayed me every step of the way.",
    )
    journal_event_add(
        "Dad",
        "Dad Walks In Shower",
        "He walked in while I was stepping out of the shower — no knock. Just him, closing the door behind himself with that smile. He said he didn't know I was in there like it was an accident. Then his hand was on my shoulder. Then the towel was on the floor. He stripped me completely bare and didn't stop until I came on his fingers while he mocked me for it. He left laughing. I was left standing in a puddle of my own shame.",
        "Dad works during morning and sleeps all night but during afternoon to evening he is usually awake and at home. I should be careful about when i shower, if he catches me there I would already be wearing very little clothing especially if his lust is high.",
        "images/Homeshower/shower walkin/scene_dad_walks_in_home_bathroom_madd_in_towel_removes_towel_rubbing_3.JPG",
        done=False,
        hidden=True,
        char_thought="He stripped me in the bathroom, fingered me until I came, then laughed in my face while I fell apart. He called me a whore for reacting to it. I couldn't move. I just stood there and let it happen and hated myself more with every second.",
    )
    journal_event_add(
        "Dad",
        "Morning Shower Assault",
        "He cornered me in the shower at 5 AM. He choked me, slapped me, kissed me against my will, bit my neck, then shoved his dick in my mouth and held me there until he finished. I ended up on my knees, completely broken. And the worst part—I felt like i belonged there",
        "I remember Dad telling me he uses shower around 5 AM in the morning..Guess i should stay away from the bathroom during that time",
        "images/Homeshower/scene_dad_shower_morning_anger_event_madd_on_knees_dad_blowjob_2.JPG",
        done=False,
        hidden=True,
        char_thought="He choked me, slapped me, forced himself into my mouth and held my head there until he was done with me. I was on my knees, completely broken, and he didn't even flinch. He's not scared of consequences. He takes what he wants and he's completely in control.",
    )
    journal_event_add(
        "Dad",
        "Morning Eavesdrop",
        "I stood outside his door in the morning and heard something... he was in a meeting. Talking to people through his laptop. I had no idea he even worked.",
        "Hmm, according to dad he is working in the morning, maybe if i stood outside his room I would learn more about what he does for a living and how the fuck does he always stay at home!",
        "images/scene_home_lobby_area/scene_madd_knock_home_morning_afternoon.jpg",
        done=False,
        hidden=True,
        char_thought="He was on a work call. I didn't know he actually had a job. He's always home... so what exactly is he doing here all day?",
    )
    journal_event_add(
        "Dad",
        "Cracking His Schedule",
        "He said the same thing again — that he has to stay home because of me. His sick daughter. His excuse. I listened long enough to notice a pattern: they always push him around 10:59. If I time it right and walk in between 10:55 and 10:58... maybe I can finally get him called back into that office.",
        "He's always on those morning calls. If there's a pattern, I can use it.",
        "images/scene_home_lobby_area/scene_madd_knock_home_morning_afternoon.jpg",
        done=False,
        hidden=True,
        char_thought="He uses me as his excuse every single time. \"My daughter is sick.\" \"She needs me.\" I heard the whole thing. But I also heard the timing. 10:59. Every time. If I get into that room between 10:55 and 10:58 and get in frame, they'll see I'm perfectly fine. And then he loses his cover story.",
    )
    journal_event_add(
        "Dad",
        "Second Interruption",
        "I timed it right this time. I walked in during the meeting and got on camera — they actually saw me. They questioned why he needed to stay home. He lost it. He dragged me, stripped me, forced himself into my mouth in front of the locked door, then made me drink his piss. He came on me. When it was finally over he locked my room and took away my freedom anyway. I failed again. But they saw me.",
        "If I time it right between 10:55 and 10:58, I can walk in and get in front of the camera this time. But am i prepared for it ? Prepared for what might happen",
        "images/dadroomscenes/scene_madd_interrupt_dad_meeting_event_two_oral_forced.jpg",
        done=False,
        hidden=True,
        char_thought="I got on camera. They saw me. They pushed back on him. For one second I thought I'd won. Then he locked the door. He put himself in my mouth until I couldn't breathe and made me swallow everything. He's not going anywhere. And now I have even less freedom than before.",
    )
    journal_event_add(
        "Dad",
        "Dad's Work Secret",
        "I interrupted his meeting on purpose — I wanted his coworkers to see me healthy so they'd call him back to the office. But the camera was off. He caught me, stripped me naked, and punished me. And I learned the truth: he uses me as his excuse to keep working from home. Mom dying was his golden ticket to never show up again. He has no intention of ever leaving.",
        "I've heard him on those meetings before... maybe if I actually walked in I could get his coworkers to see I'm fine and get him sent back to work. I need to check multiple times before 11. If I can get in front of the camera and they see me, they might call him back to the office.",
        "images/dadroomscenes/scene_madd_interrupt_dad_meeting_event_one_hair_pull_other_hand_at_butt_madd_open_mouth_dad_spitting_into_mouth.jpg",
        done=False,
        hidden=True,
        char_thought="He turned the camera off before I even got close to the screen. He caught me. He stripped me, fingered me, pressed his foot on my head until I begged him to stop. And all of it was for nothing — he'll never go back to that office. He uses me as his excuse. I'm his cover story.",
    )
    journal_event_add(
        "Dad",
        "Morning Knock at 11",
        "I knocked on his door right as his meeting ended. He pulled me inside before I could even react, locked the door, pinned me against the wall and stripped me completely. He used my body for his stress relief—twice over. First against my front, then turned me around and used me from behind, biting my neck as he finished. He made me put my shorts on with his cum still on me and sent me out. I felt like a used rag.",
        "I know dad's work ends around 11, I best not disturb him right after that. If he is pissed off over something it would be bad for me",
        "images/dadroomscenes/scene_dad_event_at_11_madd_pushed_against_wall_madd_naked_turn_around_ass_grope_neck_kiss_ass_spread_dick_between_cheeks_moving_precumpenis.jpg",
        done=False,
        hidden=True,
        char_thought="He pulled me inside the moment I knocked. Stripped me completely. Used my body for his stress relief—twice—without a second thought. His cum was all over me when I left. He made me put my shorts on over it while it was still wet. I can still feel it. I should never knock on his door at 11.",
    )
    journal_event_add(
        "Dad",
        "Sleep in Dad's Room",
        "My room was locked. I had nowhere to sleep. I went to his room in the dark and lay down next to him, hoping he was out cold. He wasn't. The moment I settled his arms wrapped around me and pulled me against him. He licked my neck, stripped my shirt off, groped me, bit me, and spent the whole night using my body. In the morning I was shoved out of the room before I could even gather myself.",
        "Only way i will sleep next to him on his bed is if my room is locked or he has pushed me far enough that i no longer care about sleeping next to him. But i know that sleeping in his room is a gamble. ",
        "images/dadroomscenes/step_parent_room_scene_night_enter_madd_inside_dad_sleeping_dad_push_madd_back_to_old_position_cum_on_madd.jpg",
        done=False,
        hidden=True,
        char_thought="He was awake the whole time, waiting for me to come to him. The moment I lay down his arms locked around me. He stripped me, bit my neck, used my body until morning. I was pushed out with his marks still on my skin. Sleeping in his room is not sleeping at all.",
    )
    journal_event_add(
        "Dad",
        "Evening TV Trap",
        "He told me to sit closer while he watched TV. I stayed because I was too scared to refuse. His arm wrapped around my shoulder, his other hand guided mine onto his lap — right onto his crotch. He was already hard. I could feel it through the fabric. He talked the whole time. About gratitude. About everything he provides. His hand pressed down on mine, making me rub him slowly while he pretended to watch the screen. Then without a word he grabbed the back of my head and pushed it down. I tried to resist. He just tightened his grip. His cock was already out when my face reached his lap — thick, hot, smelling of sweat and arousal. He forced it past my lips and held me there, grinding slowly, using my throat like I was built for it. I gagged. Saliva ran down my chin. He didn't care. He kept one hand on the remote and the other buried in my hair, controlling every movement. When he finally came he pushed in all the way and held me down until I swallowed every drop. Then he let go. Patted my head. Went back to watching TV.",
        "Watching TV with Dad in the evening is never just watching TV. If his lust is high enough, sitting beside him on that sofa means ending up on my knees with his cock down my throat while he watches the screen.",
        "images/dadroomscenes/scene_living_room_evening_dad_watching_tv_dad_pushes_madd_towards_dick_dad_cumming.jpg",
        done=False,
        hidden=True,
        char_thought="He made me rub him through his pants while he lectured me about gratitude. Then he grabbed my hair and pushed my face into his lap. His cock was already out. He held me down until he came and made me swallow all of it — then patted my head like I was a good dog. He went back to watching TV. I sat back up and stared at the screen with his taste still coating my throat and I didn't even leave. I just sat there.",
    )
    journal_event_add(
        "Dad",
        "TV Night — Armpits and Breeding",
        "He pulled me onto his lap while we were watching TV. Then he took his shirt off, raised his arms, and pushed my face into his armpits. His hands on the back of my head — holding me there while I licked his sweat out of the hair. The stench was overwhelming at first but the longer he kept me there, the more my body stopped fighting it. By the time he finally pulled me away I actually felt relief when he pushed me back in. He noticed. He made it clear he noticed. Then he repositioned me on his lap, spread my legs, and bred me right there on the sofa. He came inside me. A lot. It took a long time for him to stop.",
        "Watching TV with Dad in the evening can escalate far beyond anything. If his lust is high enough and he gets his hands on me, it won't stop at a kiss ",
        "images/Living room scenes/living_room_tv_with_dad_lust_scene_take_2_maddie_in_dad_lap_dad_takes_off_his_shirt_lap_both_naked_cum_inside.JPG",
        done=False,
        hidden=True,
        char_thought="He kept my face buried in his armpits until something inside me stopped resisting. I started going deeper on my own. He saw it happen and didn't say a word — he just smiled and pushed my head back when I drifted away. Then he bred me on the sofa. His cum flooded me. He stayed inside after he finished and told me to get used to carrying his kids. Part of me didn't argue.",
    )
    journal_event_add(
        "Dad",
        "Sofa Sleep",
        "I slept on the living room sofa with nowhere else to go. I thought being out in the open might keep me safer. I was wrong. Dad found me there, pinned my hands under his feet, and lowered himself over my face while I couldn't move or turn away. He used me completely, took whatever he wanted, and left me broken on that sofa.",
        "I will only sleep in living room if i am absolutely tired or i have nowhere to sleep. Sleeping out in the open might feel safer — but it isn't. If dad's anger or lust is high enough, then i might wake up to a truly disgusting sight.",
        "images/Living room scenes/scene_madd_sleeping_living_room_night_dad_on_top_squatting_eyes_open.jpg",
        done=False,
        hidden=True,
        char_thought="I thought being out in the open would protect me. He found me on the sofa, pinned my hands under his feet, and sat directly over my face. There was nowhere to go. My tongue was deep in his asshole and he didnt allow it to leave , my lungs were full of his stinky smell. There is no safe place in this house.",
    )
    journal_event_add(
        "Dad",
        "Dragged from the Sofa",
        "I was asleep on the sofa when he found me. He yanked the blanket off, grabbed my arm and hauled me upright — his hand on my waist, lust unmistakable in his eyes. He told me we were going to his room. I couldn't shake free. He dragged me through the lobby and toward the stairs before I'd even fully woken up.",
        "Now that Dad has done such horrible things to me , I should be careful if i sleep in living room sofa, if he is in the mood and he finds me there he might just drag me to his room and do whatever he wants to me there",
        "images/dadroomscenes/living_room_madd_sleeping_drag_to_room_dad_wake_up_madd_drag_to_room.jpg",
        done=False,
        hidden=True,
        char_thought="I woke up to him ripping the blanket off and grabbing my arm. He said 'Wake up, Maddie. We're going to my room.' His hand was already on my waist before I could process what was happening. The sofa didn't protect me at all.",
    )
    journal_event_add(
        "Dad",
        "Dragged Upstairs",
        "He held both my arms the entire way up the stairs, blocking every escape. He told me I'd be fulfilling my role as his wife tonight. At the top he dragged me straight to his room and closed the door. I had one moment on the stairs to make noise and hope my brother would come — but whether he did or not, I ended up in that room.",
        "Now that Dad has done such horrible things to me , I should be careful in the afternoon when in lobby area, that's right after his work calls and if he is in the mood he might just drag me to his room and do whatever he wants to me there",
        "images/dadroomscenes/home_areas_dad_drags_madd_to_his_room_upstairs.JPG",
        done=False,
        hidden=True,
        char_thought="He had both my arms pinned on the stairs. No way to run. He said 'Tonight you will be fulfilling your role as my wife.' I had one choice — make noise and hope, or stay quiet and endure. Either way I ended up shut inside his room.",
    )
    journal_event_add(
        "Dad",
        "Forced Rimming 2",
        "He called me in, reminded me of the first time, and then demanded I do it again. I ended up on the floor while he backed his ass into my face. His hand gripped my head and pushed me in deeper until my nose was buried in his crack and all I could breathe was his stink. He made me put my tongue inside and clean him out completely — then when he came on the floor he made me lick that up too. On my hands and knees, tongue on the floor, licking his cum like an animal.",
        "He's already made me clean his asshole once and i knew he bloody loved it ...If i listen to his demands and he's in that mood again, he'll make me do it again — tongue inside his stinkhole until he's satisfied. I need to think about whether whatever I'm going in there for is worth that.",
        "images/dadroomscenes/step_dad_rimming_2_aftermath_dad_standing_butt_facing_madd_dad_naked_ass_touch_madd_face_hand_behind_madd_head_more_deep.jpg",
        done=False,
        hidden=True,
        char_thought="He's already made me clean his asshole now. If I listen to his demands again he might try to make me clean his stinkhole again. My tongue was buried inside him and I couldn't pull away — his hand made sure of that. Then he came on the floor and made me lick it up too. I can still taste both of them.",
    )
    journal_event_add(
        "Dad",
        "Dad's Room Night 3",
        "The moment I lay down he had his hands all over me. He licked my neck, bit me, stripped me bare, groped me, then flipped me and pushed himself inside my ass. I couldn't stop him — he had me pinned, holding my elbows and thrusting until he came inside me. I came too. My whole body shaking while he filled me up. He came inside me and I felt it flooding my insides, pouring out. That was the night he took my ass completely.",
        "Sleeping in his room a third time will push things further than before — he's been escalating every visit. The third night ends with him inside me either my pussy or my butthole. If I go back there, I need to be ready for what it means but he might unlock my room...",
        "images/dadroomscenes/scene_sleep_next_to_dad_night_after_locked_room_3_first_anal_sex_cumming.JPG",
        done=False,
        hidden=True,
        char_thought="I told myself I was just sleeping there. I woke up with him inside me and his cum flooding my insides. My ass throbbing, his hands still gripping my waist. And the worst part — I came with him. I can't pretend that was only his doing.",
    )
    journal_event_add(
        "Dad",
        "Found the Keys",
        "I woke up after he came inside me twice, every step torture from what he did to my ass. While he slept deeply I searched his drawer. I found a USB with 2000 dollars in crypto — the exact amount I needed. And at the back of the drawer, the main door keys. My way out. I put them back for when I'm actually ready to use them.",
        "The more I sleep with dad the more he ups the anti — once he's spent and sleeping hard — there's a window to search his drawers for the main door keys and some money maybe. But he forces himself on me which drains most of my energy , i need to save some energy to serach for the money and the keys",
        "images/dadroomscenes/scene_sleep_next_to_dad_night_after_locked_room_3_hated_it_walk_to_drawer_search_keys_found_keys.JPG",
        done=False,
        hidden=True,
        char_thought="His cum was still inside me when I found them. The keys to the front door. My entire body was aching and I was leaking his cum onto the floor as I stood there holding them. I put them back. But I know exactly where they are now.",
    )
    journal_event_add(
        "Dad",
        "Kitchen Ambush (Miss Event)",
        "I was cooking when he came up behind me. He wrapped his arms around me, pressed his face into my neck and licked me slow and deep. He groped my breasts with both hands while I tried to keep cutting the vegetables. Then he yanked my shorts down, spread me open and buried his face between my cheeks — his tongue inside me, holding my hips so I couldn't move. When he was done he stood up, rubbed himself between my cheeks until he finished all over my ass. He made me pull my shorts back up over the mess and told me to keep cooking.",
        "Ever since mom died , when  i cook in the kitchen during afternoon or evening, dad walks in and just stares at me and often comments that i remind him of my mom , if he is in the mood he might end up escalating to something worse than just staring at me",
        "images/kitchen/scene_kitchen_minigame_madd_dad_standing_licks_neck_naked_maddie_touches_maddie_rubbing_3.JPG",
        done=False,
        hidden=True,
        char_thought="He cornered me at the stove and used me like I was part of the meal. His tongue in my ass while I gripped the counter. His cum all over me when it was done. He made me pull my shorts back on wet and told me to finish cooking. I stood there cutting the vegetables with his cum soaking through the fabric. I didn't say a single word.",
    )
    journal_event_add(
        "Dad",
        "Dragged to Dad's Room (DP)",
        "He dragged me to his room. Stepbrother barged in and instead of helping me he joined in. Both of them took me at the same time in an airtight position — dad entered inside my vagina, stepbrother filling my asshole. I was stretched between them, completely overwhelmed, until they both came inside me, Their intense motions even made me squirt...God it was so embarassing. They talked about me afterward like I wasn't even in the room. I fell asleep on top of dad, too broken to move.",
        "Once dad starts to drag me to his room via the stairs i can call for help . If stepbrother's lust is also high he won't protect me — he'll take his turn too. I need to stop both of them from reaching that point at the same time. If i am a virgin i can push them away saying that i need to save it but if they know anything that they might blackmail me with they might just force me to do it anyway. I shouldnt be caught stealing or adding anything to their food. Hopefully i am not drugged at this point because if i am drugged i wont be able to refuse them at all and they might just do whatever they want to me without any resistance",
        "images/dadroomscenes/home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_madd_being_penetrated_by_dad_and_brother_3.JPG",
        done=False,
        hidden=True,
        char_thought="Dad was inside my vagina and stepbrother was filling my asshole at the exact same time. I was pinned between them, completely full, with nowhere to go and nothing left to hold back. They both finished inside me. Afterward they talked about me like I was furniture. I fell asleep on top of dad with both of their cum still leaking out of me",
    )
    journal_event_add(
        "Dad",
        "Dragged to Dad's Room (DP2)",
        "They brought me back to his room again. This time it lasted the entire night. Dad and stepbrother took turns and then took me together — three times each, both holes filled at once while they talked about me like I was furniture. Dad wiped his butt sweat on my face while I was unconscious. Then stepbrother climbed on top of me and slept with his manhood buried in my mouth and his sweaty balls pressed against my nose for the whole night. I woke up tasting him.",
        "Once they have already double penetrated me, there's nothing stopping them from doing it again. Next time his lust is high in the afternoon I am done for. If both their lusts are high enough when dad drags me upstairs, they'll use me the entire night. There's no version of this I survive without something breaking.",
        "images/dadroomscenes/dp2/dad_brother_dp2_clothes_off_fast_12.JPG",
        done=False,
        hidden=True,
        char_thought="They used both my holes all night. Three times each. Dad wiped his butt sweat on my face while I was passed out and then stepbrother slept on top of me with his manhood in my mouth and his sweaty balls on my nose. I had no choice but to breathe him in all night. I woke up with the taste of both of them still in me.",
    )
    journal_event_add(
        "Dad",
        "Dragged to Dad's Room (Spitroast)",
        "He flipped me onto all fours and positioned stepbrother in front of my face. Dad entered me from behind while stepbrother forced himself into my mouth. They used me completely at both ends until stepbrother finished down my throat and dad filled me from behind. Afterward dad claimed me in front of stepbrother — kissed me, called me his wife, and told stepbrother to stay away from me.",
        "Once dad starts to drag me to his room via the stairs i can call for help. Dad sometimes wants to put on a show for stepbrother — proving who owns me. If both their lusts are high enough when he drags me to his room, he might arrange this himself. I have no say when he decides to use me to establish dominance. If i am a virgin i can push them away saying that i need to save it but if they know anything that they might blackmail me with they might just force me to do it anyway.I shouldnt be caught stealing or adding anything to their food. Hopefully i am not drugged at this point because if i am drugged i wont be able to refuse them at all and they might just do whatever they want to me without any resistance",
        "images/dadroomscenes/home_areas_dad_drags_madd_to_his_room_brother_joins_in_dad_room_spitroast_madd_dad_inserts_brother_joins_in_spitroast_complete_4.JPG",
        done=False,
        hidden=True,
        char_thought="I was on all fours between them. Stepbrother in my mouth, dad behind me. They moved in rhythm like they'd planned it. Stepbrother came down my throat and dad filled me from behind at nearly the same time. Then dad kissed me in front of stepbrother and called me his wife. I was being used to send a message I had no part in writing.",
    )
    journal_event_add(
        "Dad",
        "Dragged to Dad's Room (Dad Only)",
        "He dragged me to his room alone. He pinned me to the bed, stripped me bare, kissed me slowly then climbed on top and took me completely. He pounded into me until I was begging him for more — moaning his name, asking him to breed me. He came inside me with nothing between us. He told me I was his wife now. I fell asleep in his bed still full of him, his scent all over me.",
        "Once dad starts to drag me to his room via the stairs i can call for help , if no help arrives it's just the two of us. If his lust is high enough he won't hold back at all. I need to keep him from reaching that point or I won't be able to stop what happens next. If i am a virgin i can push him away saying that i need to save it but if he knows anything that he might blackmail me with he might just force me to do it anyway.I shouldnt be caught stealing or adding anything to their food. Hopefully i am not drugged at this point because if i am drugged i wont be able to refuse him at all and he might just do whatever he wants to me without any resistance",
        "images/dadroomscenes/home_areas_dad_drags_madd_to_his_room_dad_only_in_dad_room_dad_on_top_pounding_maddie_4.JPG",
        done=False,
        hidden=True,
        char_thought="He was on top of me pounding into me and I stopped fighting it. I started begging him. I asked him to breed me and I meant it. He came inside me raw and I felt everything. He called me his wife and I fell asleep in his bed leaking him. I don't know who I was in that room but it wasn't the girl who walked in.",
    )
    journal_event_add(
        "Dad",
        "Dinner Table Claim",
        "We were eating in silence when he suddenly started talking to my brother about me like I wasn't there — telling him I was his wife, that he'd seen what they'd been doing and it ends now. Then his hand came down on my head. Not a stroke. A claim. He pulled my face to his and kissed me at the table with chewed food still in his mouth, his tongue shoving it past my lips while brother watched. He kissed me until saliva was dripping off my chin onto my shirt. Then he licked my neck from the collar to my ear, his spit pooling and soaking through my clothes. He stood up. He pulled his jeans down right there. His cock was already out by the time he guided my head toward it. He thrust into my mouth slow at first — controlling the pace, showing my brother that I would let him do this anywhere, anytime. Then harder. His hands in my hair, hips moving, cock down the back of my throat. He came inside me — hot, thick, relentless — and some of it spilled onto my plate. He told me to eat it. He pushed my face down toward the plate. I pulled out my tongue and licked his cum off my own dinner while he watched with a smirk and then told my brother: she's mine, never touch her again.",
        "We usually eat dinner as a family around 8PM . If i sleep in living room, brother might do something to me and dad might just hear us. If he found out that I let brother do things to me he will surely make an example just to show i belong to him and him alone. ",
        "images/kitchen/scene_kitchen_eating_with_family_dad_only_dad_stand_up_start_bj.JPG",
        done=False,
        hidden=True,
        char_thought="He pushed my face into my own plate and made me lick his cum off it in front of my brother. I didn't fight him. I just pulled my tongue out and did it — and the worst part is I wanted to do it before he even asked. His cum tasted like dominance and I swallowed every drop of it with my brother watching.",
    )
    journal_event_add(
        "Dad",
        "Sandwich in the Kitchen",
        "I was cooking when they both appeared. They took turns spanking me — first Dad, then brother, back and forth while I stood at the counter trying to hold my composure. Dad lifted me off my feet, turned me around, and kissed me deep while brother's mouth went to my neck. They had me sandwiched between them, both sets of hands everywhere at once — my ass, my waist, my chest — brother licking up one side of my neck while Dad's tongue was inside my mouth. Dad made the rules clear: my holes were his and his alone. Then he lifted me higher, positioned himself underneath me, and lowered me down onto his cock — into my ass. I felt every inch of him filling me up as I sank down. Brother started pushing me back and forth on him, rocking me in rhythm while Dad thrust upward. The three of us moving in sync. I came. Hard. I couldn't stop it — I gushed all over him, the sound of it loud and humiliating. That made Dad even harder. He finished inside me completely, flooding my ass with his cum while I shook with the aftershock of my own orgasm. They both left without a word. I finished cooking with his cum leaking out of me and running down my thighs.",
        "Around 7 PM i have to cook dinner for family or else Dad would get angry . When I am cooking for these creeps they stand behind me sometimes...I know they are upto no good but if these apes cant control their lust I might be in trouble because cooking puts me in a vulnerable spot. Especially that oaf of a stepfather. If brother isnt as interested or if Dad isnt angry he might just let brother stay while he abuses me.",
        "images/kitchen/cooking_for_family_brother_and_dad_join_madd_sandwiched_between_them_lift_madd_lowered_on_to_dad_2.JPG",
        done=False,
        hidden=True,
        char_thought="Brother was rocking me back and forth on Dad's cock in my ass while Dad kissed me. I came on his dick in front of my own stepbrother — all over him, wet and loud and completely out of my control. Then Dad came inside me. Both of them left and I stood there at the stove with his cum trickling down my leg, finished cooking, and served them dinner.",
    )
    journal_event_add(
        "Dad",
        "Bred in the Kitchen",
        "Dad shouted at my brother to get out and he listened. Then it was just us. He kissed me and lifted me off my feet — his hands on my ass, spanking me while I dangled in his arms, making me moan in front of whoever could hear. He told me he was going to breed me. He said it calmly, like it was a scheduling matter. He carried me to the chair, sat down, and had me straddle his lap with my legs around him. He licked my neck slow and thorough while I sat there, stripped my shorts off, then removed his own. I could feel the heat from his cock before it ever touched me. Then he moved my hips and pushed inside my pussy — all the way in one slow stroke that made me lose my breath. He fucked me on that chair while I clung to him. When my brother came back through the door he went harder — on purpose, making me moan louder for an audience. He kept calling me his cum dumpster. He told my brother to watch. He came inside me deep, filling my pussy with his seed while I shook on his lap, both of us visible to my brother standing in the doorway. When he finally pulled out he spread my legs and showed my brother what he'd left inside me. Then he got up, got dressed, told me I belonged to him, and walked away. I sat there on the chair, his cum dripping out of me and onto the seat, staring at nothing.",
        "Around 7 PM i have to cook dinner for family or else Dad would get angry. When I am cooking for these creeps they stand behind me sometimes...I know they are upto no good but if these apes cant control their lust I might be in trouble because cooking puts me in a vulnerable spot. Especially that oaf of a stepfather. If brother isnt as interested or if Dad is angry he might just kick out brother and take me for himself.",
        "images/kitchen/cooking_for_family_brother_and_dad_join_dad_only_vaginal_dad_sitting_on_chair_madd_on_lap_madd_naked_dad_naked_vaginal_penetration_5.JPG",
        done=False,
        hidden=True,
        char_thought="He spread my legs and showed my brother my pussy — still full of his cum, still wet and open — like he was proudly showing off a trophy. My body was trembling. I had nothing left to say. He got dressed and left me sitting there leaking onto the chair. I wanted to lick every drop of it up and I hated myself for it.",
    )
    journal_event_add(
        "Dad",
        "Sleep With Dad: Breast Night",
        "He pulled me into his bed, turned off the light, and used the darkness like a weapon. His hands found my breasts through my shirt first — squeezing, kneading, teasing my nipples until they hardened against my will. Then he pulled my shirt off and went bare skin. He groped me, bit my neck, left marks on my body that I'd have to hide in the morning. He kept comparing me to Mom. When he finally fell asleep I searched the room for money and found nothing. I crawled back into bed and lay there while he pulled me against him in his sleep, his hand finding my breast again.",
        "If I listen to his demands and agree to sleep next to Dad he will surely try to touch me in his sleep. ",
        "scene_dad_breast_bare_grope_neck_bite",
        done=False,
        hidden=True,
        char_thought="He had both hands on my bare breasts in the dark, biting my neck hard enough to leave bruises. He compared me to Mom the entire time. I got nothing out of it. I crawled back under his arm and lay there while he groped me in his sleep.",
    )
    journal_event_add(
        "Dad",
        "Lifted and Bred in the Living Room",
        "He grabbed me mid-yoga and hoisted me completely off the ground — my legs wrapped around his waist, his hands owning every inch of me before I could say a word. He kissed me with his tongue shoved deep into my mouth, licked every inch of my neck and collarbone, then spent what felt like forever biting my breasts through my shirt like I was his personal meal. He used my conscience against me — told me if I ran, the next girl in this house would suffer in my place. That was what finally broke me. I stopped fighting. He ripped my clothes off, pulled out his cock, and pushed it inside me right there in the air. He pounded me slow at first, then brutal — hair pulled, body shaking in his arms, cervix taking every thrust. I orgasmed on his dick. He announced it to the empty room and used it as proof that I'd accepted him as my husband. He came inside me the first time while biting my tits, calling it breeding in real time. He made me say out loud that I loved it, that I wanted to carry his child. My own words. Then he changed position, told me things stop when he says they stop, and went again with no mercy. He came inside me a second time while I was already full from the first. I passed out in his arms with his cock still buried in me. When I was unconscious he pissed inside me. I could feel it even blacked out — burning hot, flooding my already ruined womb. I came back to the smell of it.",
        "He's been looking at me creepily when i exercise in the living room in evening. Even commenting things like my ass looks breedable. If I'm in there doing yoga when his lust is high enough and the boundaries between us keep getting removed, he might use my stretched position against me. ",
        "images/Living room scenes/dad_yoga/home_madd_yoga_dad_lift_lick_dck_new_position_1.JPG",
        done=False,
        hidden=True,
        char_thought="He lifted me off the ground mid-yoga and didn't put me down until I was full of his cum twice over and unconscious. He made me say I wanted to carry his child while he was still inside me — and I said it. He pissed in me while I was blacked out. The living room is his territory now. I don't know how to walk back in there.",
    )
    journal_event_add(
        "Dad",
        "Sleep With Dad: Ass Night",
        "He called me a whore and told me to get in his bed. The moment the lights went out he turned toward me, his hand finding my hip, pulling me against him. He groped my ass through my shorts first — kneading, squeezing, telling me his fantasies about getting me pregnant. Then his fingers worked inside my waistband and he pulled my shorts down. He spent the rest of the night with his bare hands on my bare ass, claiming every inch of me while I lay completely frozen. By morning I was hollow and empty, his marks invisible but burned into my skin.",
        "If I listen to his demands and agree to sleep next to Dad he will surely try to touch me in his sleep.",
        "scene_dad_ass_bare_grope",
        done=False,
        hidden=True,
        char_thought="He pulled my shorts down in the dark and spent the entire night groping my bare ass. He talked about getting me pregnant. By morning I walked out feeling like I'd been erased.",
    )
    journal_event_add(
        "Dad",
        "Room Intrusion: Anal",
        "I was asleep when he came in. He sat beside my bed in the dark, ran his hands through my hair, slipped his finger into my mouth. Then he lifted me onto his lap, kissed me, stripped me, and took me completely — his cock buried in my ass while I sat on top of him, unable to stop any of it. He came inside me and told me his seed was inside me now. That I was his. He kissed me one last time and walked out, leaving me alone with his cum leaking out of me in the dark.",
        "Once my room gets unlocked by Dad , it is never gonna be locked again. That means he can walk in whenever he wants especially when I am sleeping. If his lust gets high enough while I'm sleeping, I won't get a warning — he'll just be there.",
        "images/MaddHomeRoomscenes/scene_dad_walks_in_madd_room_sleep_naked_madd_on_dad_anal_climax.JPG",
        done=False,
        hidden=True,
        char_thought="He came into my room while I was asleep and took me from behind before I was fully awake. His cum was inside me before I could even process what was happening. He told me his seed was in me now. That I belonged to him. Then he just left.",
    )
    journal_event_add(
        "Dad",
        "First Vaginal: Punishment Night",
        "He found out I stole from him. He found out about me and my stepbrother. He came into my room furious — and used both as leverage. Report me to the cops, or give him what he wanted. The front hole. His seed inside me. He wanted to make sure I was pregnant with his child so I could never leave. I said yes. I had no other choice. He kissed me for a long time first — slow, then rough, then his tongue everywhere. He licked my neck until it was soaked. He buried his face in my armpits. Then he stripped me, positioned himself between my legs, and entered me for the first time. My first time. He came inside me raw, called me his wife, and left me lying in a pool of his cum.",
        "when I am sleeping in my room and the door got unlocked after dad locked it. If He knows about the money I stole or if he knows that i have been manipulating their emotions using drugs in food he will use it as leverage. I think he saw brother forcing his dick in my mouth in living room. He will definitely  If his lust is high enough and he has enough leverage, he'll use both to take the one thing he hasn't taken yet. If he thinks he's already done too many things to me and his lust is high he doesnt need any leverage to claim my pussy",
        "images/MaddHomeRoomscenes/dad_walks_in_madd_room_sleep_vag_maddie_legs_in_air_madd_waking_up_dad_on_top_first_vag_penetration.JPG",
        done=False,
        hidden=True,
        char_thought="He gave me a choice between jail and giving him my virginity. I chose him. He took me slowly at first, like he wanted me to feel every second of it. He came inside me and called me his wife. I lay there full of his cum and I couldn't even cry. Something in me had already accepted it.",
    )
    journal_event_add(
        "Dad",
        "Nightly Visits: Foot and Breeding",
        "After the first time, it became routine. He walks into my room while I sleep, touches me, repositions me... and I stopped being able to stop him. He shoves his foot on my face, forces his toes into my mouth, makes me lick every inch of his sweaty, unwashed foot. And while I'm gagging on the taste and smell of him — his foot buried in my mouth like I'm his personal foot rag — he enters me from below. He breeds me with his foot still in my mouth. Multiple times in a row. He makes me spread his cum across my own skin — my chest, my stomach, my face — while he watches and laughs. And each time he does it, some part of me breaks off and I can't get it back.",
        "If he has fucked my pussy even once, He can walk into my room anytime and do it to me again I cant even lock my door anymore. My room is not mine anymore. Every night I go to sleep knowing he might come in, and every morning I wake up knowing he already did.",
        "images/MaddHomeRoomscenes/foot on head/dad_madd_room_sleep_vag_dad_foot_inside_madd_vag_1.JPG",
        done=False,
        hidden=True,
        char_thought="He uses my mouth as a foot rag while he breeds me. He makes me smear his cum all over my own face with my own hands. And the worst part — every time he comes back, it takes a little less time for my body to stop fighting him. I'm being rewritten from the inside out, one night at a time.",
    )
    journal_event_add(
        "Dad",
        "Sleep With Dad: Vaginal Night",
        "I went to sleep next to him and he didn't wait. Immediately he put his dick inside me and started pounding me . It went on for so long I lost count of how many hours straight he fucked me . I slept with his dick still inside me , there is no way to go back to sleeping in my room alone when i can sleep next to him with his dick burried in me.",
        "Now that he's been inside me sleeping next to him at night will surely result in him putting it in me again. If I sleep next to him when his lust is high enough, he won't stop at touching — he'll take me completely, all night, and call it love.",
        "images/dadroomscenes/sleep vag/scene_sleep_next_to_dad_night_vaginal_clothes_off_21.JPG",
        done=False,
        hidden=True,
        char_thought="He came inside me and called me his wife and I lay there in the dark telling myself I had no choice. But my body had already answered for me, hours before he even finished. I woke up soaked and hollow and his arm was still around me like a lock.",
    )
    journal_event_add(
        "Brother",
        "Escape Night",
        "The night I finally ran. I needed his computer one last time to complete my cram school enrollment. He made me sit on his lap to use it. His hands were inside my shirt before the page even loaded. He pulled my hair back and spent what felt like forever licking every inch of my neck and face — his saliva coating my skin while I sat there clicking through payment fields. Then he yanked my shirt over my head. He buried his face between my bare breasts and sucked my nipples until they were raw, squeezing both with both hands, moaning into my chest like a starved animal. I sat there on his cock pressing through his pants, naked from the waist up, finishing my enrollment form while he devoured me. When he was finally done he helped me pull my shirt back on. I kissed his cheek. I put on his clothes — his oversized t-shirt, his cargo pants, his sweaty boxer shorts against my skin — and walked out of that house forever. His cum still coating the back of my throat from the day before. His spit still drying on my chest. I was wearing him as I escaped him.",
        "I know everything I need now — I already have the plan , I need to save money then i pay the money and escape. This is the night I stop surviving and start escaping. Brother will want payment for the computer one last time. Whatever he takes, I pay it and I leave. I can go to Brothers Room and pay the money required from his PC .",
        "images/BrotherScenes/scene_runaway_from_brother_room_sitting_on_brother_lap_facing_him_lift_shirt_madd_top_naked_first_lick_boobs_2.JPG",
        done=False,
        hidden=True,
        char_thought="He sucked my bare breasts while I typed in my credit card number. His tongue on my nipples while I clicked confirm payment. Two thousand dollars transferred and his spit running down my chest at the exact same moment. I finished the enrollment form half-naked on his lap and then I put on his clothes and walked out the front door. I've never felt more degraded and more free at the same time.",
    )
    journal_event_add(
        "Brother",
        "Morning Claim",
        "I woke up to find him standing over me, fury in his eyes. He'd been up all night obsessing over watching Dad pound me in the ass — and now he wanted his turn. Before I could say a word he was on top of me, yanking me against his chest, his lips attacking my neck and face. His saliva ran everywhere — down my throat, across my cheeks, soaking into my hair. He kissed me until I ran out of air, his tongue shoved so deep into my mouth I could barely breathe. Then he stripped my shorts off, reached behind me to spread me open, and pushed his cock into my ass — slow and deliberate, making sure I felt every inch. The pain melted into pleasure faster than I wanted to admit. I started pushing back against his thrusts. I started moaning his name. He talked the entire time — telling me I was made for this, that he'd fill me before Dad could, that I was his now. He came deep inside me — hot, thick spurts that didn't stop. He made me lie there afterward with his cum leaking out of me while the room filled with the smell of him. Then he just left. I stared at the ceiling wondering when I started wanting it.",
        "Now that brother has seen me get pounded by dad , he will demand that i let him do the same. I better not sleep in his room especially when his arousal is high",
        "images/BrotherScenes/madd_wake_up_brother_morning_tries_anal_brother_spooning_position_madd_naked_brother_naked_first_insertion.JPG",
        done=False,
        hidden=True,
        char_thought="He was inside me before I was fully awake. I felt every inch of him pushing in and I stopped pretending I didn't want it. My hips moved on their own to meet his thrusts. He came inside my ass and told me I was his — and the worst part is that lying there full of his cum, the sheets soaked, his smell all over me... I believed him.",
    )
    journal_event_add(
        "Brother",
        "Wake Up: Full Claim",
        "I woke up in his bed and he didn't waste a second. He started with his dirty foot shoved against my lips — forced me to lick every inch of his filthy soles until the taste stopped making me gag. Then he pulled me into his lap and kissed me until my mouth tasted like him. He made me clean his sweaty armpits with my tongue, drinking every drop of salt and musk while he watched me with those possessive eyes. Then he stripped my shorts off and slid his cock inside me for the first time — his own stepsister, on his lap, in the bed where I'd been sleeping. He used me slowly at first, then harder, then until I was screaming. I passed out after he came inside me. I woke up still leaking his cum, my face coated in his ass sweat from what he did while I was unconscious. He filled me. He marked me inside and out. And somewhere in the middle of all of it, my body stopped fighting him.",
        " Now that he's already put his dick in my butthole he might just try to put it in my pussy next. I know he always wanted to . I better not sleep in his room from now on. Especially when he's horny. ",
        "images/BrotherScenes/room_vag/madd_wake_up_brother_morning_brother_in_bed_maddie_lap_penetration_7.JPG",
        done=False,
        hidden=True,
        char_thought="He tasted me, licked me, kissed me, made me drink his sweat from his armpit, and then he fucked me until I blacked out. I woke up full of his cum with my face smelling like the inside of his ass. I don't know at what point I stopped crying and started moaning. I hate that I don't know.",
    )




# ---------------------------------------------------------------
# Persistent state variables
# ---------------------------------------------------------------
default journal_tab          = "Characters"   # "Characters" | "Events"
default journal_char_selected = None           # character name or None
default journal_detail_tab   = "Available"    # "Available" | "Done" (inside a char page)
default journal_events_tab   = "Available"    # "Available" | "Done" (Events section)

# Stores mutable journal state across saves/loads.
# Structure: {char_name: {event_name: {done, hidden, order}}, "_world": {event_name: {done}}}
default journal_save_state      = {}
default _journal_counter_store  = 0
# Tracks which events the player has already opened (key = "CharName::EventName", value = order at time of clear).
# An event shows the NEW badge when ev["order"] > journal_cleared_events.get(key, 0).
default journal_cleared_events  = {}
default journal_toast_queue     = []   # [(char_name, event_name), ...]


label after_load:
    python:
        # Restore counter from saved value
        _journal_order_counter[0] = _journal_counter_store
        # Re-apply all saved mutable state to the freshly init-built journal_characters
        for _jc_name, _jc_events in journal_save_state.items():
            if _jc_name == "_world":
                for _je_name, _je_state in _jc_events.items():
                    for _je in journal_events_list:
                        if _je["name"] == _je_name:
                            _je["done"] = _je_state.get("done", _je["done"])
                            break
            else:
                for _jchar in journal_characters:
                    if _jchar["name"] == _jc_name:
                        for _je_name, _je_state in _jc_events.items():
                            for _jev in _jchar["events"]:
                                if _jev["name"] == _je_name:
                                    _jev["done"]   = _je_state.get("done",   _jev["done"])
                                    _jev["hidden"] = _je_state.get("hidden", _jev["hidden"])
                                    _jev["order"]  = _je_state.get("order",  _jev["order"])
                                    # 'new' is NOT restored here — it is derived at render time
                                    # from ev["order"] vs journal_cleared_events
                                    break
                        break
        # Fix inconsistency from old saves: if an event is done=True but hidden=True,
        # just reveal it silently (no order bump, no NEW badge, no toast).
        for _jchar_fix in journal_characters:
            for _jev_fix in _jchar_fix.get("events", []):
                if _jev_fix.get("done", False) and _jev_fix.get("hidden", False):
                    _jev_fix["hidden"] = False
                    _journal_save_ev(_jchar_fix["name"], _jev_fix)
        # Rebuild each character's displayed description from their now-restored event states
        for _jchar_rb in journal_characters:
            _journal_rebuild_char_desc(_jchar_rb["name"])
    return


# ======================================================================
# Journal Screen
# ======================================================================
screen journal():
    tag menu

    add "gui/journal_paper_bg_2.png" xsize 1920 ysize 1080 xalign 0.5 yalign 0.5

    default lightbox_img = None
    default card_detail = None   # holds event dict when card popup is open

    # ------------------------------------------------------------------
    # Main frame
    # ------------------------------------------------------------------
    frame:
        xpos 190
        ypos 55
        xsize 1620
        ysize 970
        background None
        padding (40, 18, 60, 18)

        vbox:
            spacing 0

            # Title row -- back button on left when inside a character
            hbox:
                xfill True
                ysize 68

                if journal_char_selected is not None:
                    textbutton "< Back":
                        style "journal_back_btn"
                        action [
                            SetVariable("journal_char_selected", None),
                            SetVariable("journal_detail_tab", "Available"),
                        ]
                else:
                    null width 130

                text "~ My Journal ~" style "journal_title_text" xalign 0.5 yalign 0.5
                null width 130

            null height 12

            # ------------------------------------------------------------------
            # Top-level section tabs (Characters  |  Events)
            # Hidden while viewing a character detail page
            # ------------------------------------------------------------------
            if journal_char_selected is None:
                hbox:
                    xalign 0.5
                    spacing 6
                    for _stab in ["Characters", "Events"]:
                        $ _sa = (_stab == journal_tab)
                        textbutton "[_stab]":
                            style "journal_tab_btn"
                            background       ("#7a4e28e8" if _sa else "#c8a97ecc")
                            hover_background "#9b6238"
                            text_style       ("journal_tab_text_on" if _sa else "journal_tab_text_off")
                            action SetVariable("journal_tab", _stab)
                null height 16

            # ------------------------------------------------------------------
            # NEW JOURNAL ENTRY banner
            # ------------------------------------------------------------------
            if journal_any_new():
                frame at journal_new_entry_anim:
                    background "#8b4513cc"
                    padding (20, 8, 20, 8)
                    xfill True
                    hbox:
                        xalign 0.5
                        spacing 14
                        text "✶" style "journal_new_star_text"
                        text "NEW JOURNAL ENTRY" style "journal_new_banner_text"
                        text "✶" style "journal_new_star_text"
                null height 6

            # ==============================================================
            # VIEW A: CHARACTER DETAIL PAGE
            # ==============================================================
            if journal_char_selected is not None:

                $ _ch = next((c for c in journal_characters if c["name"] == journal_char_selected), None)

                if _ch is not None:

                    # Banner
                    frame:
                        style "journal_char_banner"
                        xfill True
                        ysize 195
                        hbox:
                            spacing 24
                            frame:
                                background "#3b2714ee"
                                padding (3, 3, 3, 3)
                                yalign 0.5
                                add Transform(_ch.get("portrait", "gui/journal_icon.png"), size=(480, 270))
                            vbox:
                                yalign 0.5
                                spacing 6
                                xsize 1272
                                text "[_ch['name']]" style "journal_char_banner_name"
                                frame:
                                    background "#8b5e3c66"
                                    xsize 240
                                    ysize 2
                                    padding (0, 0, 0, 0)
                                viewport:
                                    mousewheel True
                                    xsize 1272
                                    ysize 108
                                    text "[_ch['desc']]" style "journal_char_banner_desc"

                    null height 12

                    # Done / Available sub-tabs (green accent to distinguish from section tabs)
                    hbox:
                        xalign 0.5
                        spacing 6
                        for _dtab in ["Available", "Done"]:
                            $ _da = (_dtab == journal_detail_tab)
                            textbutton "[_dtab]":
                                style "journal_tab_btn"
                                background       ("#5c3318ee" if _da else "#c4a882cc")
                                hover_background "#7a4e28"
                                text_style       ("journal_tab_text_on" if _da else "journal_tab_text_off")
                                action SetVariable("journal_detail_tab", _dtab)

                    null height 12

                    $ _want_done = (journal_detail_tab == "Done")
                    $ _evf = sorted([e for e in _ch.get("events",[]) if bool(e.get("done",False)) == _want_done and not e.get("hidden", False)], key=lambda e: e.get("order",0), reverse=True)
                    $ _evrs = [_evf[_i:_i+3] for _i in range(0, len(_evf), 3)]

                    if _evf:
                        viewport:
                            mousewheel True
                            scrollbars ("vertical" if len(_evrs) > 1 else None)
                            draggable True
                            ysize 510
                            xsize 1488
                            vbox:
                                spacing 22
                                xfill True
                                for _erow in _evrs:
                                    hbox:
                                        xalign 0.5
                                        spacing 22
                                        for _ev in _erow:
                                            $ _ei  = _ev.get("image","") or _ch.get("portrait","gui/journal_icon.png")
                                            $ _en  = _ev.get("name","")
                                            $ _edd = _ev.get("desc","")
                                            $ _er  = _ev.get("req","")
                                            $ _ev_snap = _ev
                                            $ _ev_key = (journal_char_selected or "") + "::" + _en
                                            $ _ev_is_new = _ev.get("order", 0) > journal_cleared_events.get(_ev_key, 0)
                                            frame at (journal_card_new_anim if _ev_is_new else journal_no_anim):
                                                style "journal_card_frame"
                                                xsize 474
                                                vbox:
                                                    spacing 0
                                                    # Image — click to open detail popup
                                                    fixed:
                                                        xsize 474
                                                        ysize 267
                                                        button:
                                                            xsize 474
                                                            ysize 267
                                                            background       (Transform(_ei, xsize=474, ysize=267, blur=10.0, matrixcolor=SaturationMatrix(0)) if not _want_done else Transform(_ei, xsize=474, ysize=267))
                                                            hover_background (Transform(_ei, xsize=474, ysize=267, alpha=0.70, blur=10.0, matrixcolor=SaturationMatrix(0)) if not _want_done else Transform(_ei, xsize=474, ysize=267, alpha=0.70))
                                                            action [SetScreenVariable("card_detail", _ev_snap), Function(journal_event_clear_new, journal_char_selected, _en)]
                                                        # NEW ribbon overlaid on top-right of image
                                                        if _ev_is_new:
                                                            frame at journal_card_new_anim:
                                                                xalign 1.0
                                                                yalign 0.0
                                                                background "#c0390bdd"
                                                                padding (10, 4, 10, 4)
                                                                text "✶ NEW" size 14 color "#ffffff" bold True font "DejaVuSans-Bold.ttf"
                                                    # Title bar — click to open detail popup
                                                    button:
                                                        xfill True
                                                        background ("#fff0cc" if _ev_is_new else "#f5ead0ee")
                                                        hover_background ("#ffe8a0" if _ev_is_new else "#e8d4b0")
                                                        padding (14, 10, 14, 12)
                                                        action [SetScreenVariable("card_detail", _ev_snap), Function(journal_event_clear_new, journal_char_selected, _en)]
                                                        text ("[_en]  {size=13}{color=#b85c00}✶ NEW{/color}{/size}" if _ev_is_new else "[_en]") style "journal_card_title"
                                null height 22
                    else:
                        $ _emsg = ("No scenes completed yet." if _want_done else "No scenes available yet.")
                        text "[_emsg]" style "journal_scene_desc" xalign 0.5 yalign 0.5

            # ==============================================================
            # VIEW B: CHARACTERS LIST
            # ==============================================================
            elif journal_tab == "Characters":

                $ _crows = [journal_characters[_i:_i+3] for _i in range(0, len(journal_characters), 3)]

                if journal_characters:
                    viewport:
                        mousewheel True
                        scrollbars ("vertical" if len(_crows) > 1 else None)
                        draggable True
                        ysize 720
                        xsize 1488
                        vbox:
                            spacing 26
                            xfill True
                            for _crow in _crows:
                                hbox:
                                    xalign 0.5
                                    spacing 24
                                    for _char in _crow:
                                        $ _cn         = _char["name"]
                                        $ _cp         = _char.get("portrait", "gui/journal_icon.png") or "gui/journal_icon.png"
                                        $ _cn_has_new = journal_char_has_new(_cn)
                                        frame at (journal_char_new_anim if _cn_has_new else journal_no_anim):
                                            background ("#7a3a10ff" if _cn_has_new else "#3b2714ff")
                                            padding (3, 3, 3, 0)
                                            xsize 480
                                            vbox:
                                                spacing 0
                                                button:
                                                    xsize 474
                                                    ysize 455
                                                    background       Transform(_cp, xsize=474, ysize=455)
                                                    hover_background Transform(_cp, xsize=474, ysize=455, alpha=0.78)
                                                    action [
                                                        SetVariable("journal_char_selected", _cn),
                                                        SetVariable("journal_detail_tab", "Available"),
                                                    ]
                                                    if _cn_has_new:
                                                        frame:
                                                            xalign 1.0
                                                            yalign 0.0
                                                            background "#c0390bdd"
                                                            padding (10, 5, 10, 5)
                                                            text "\u2736 NEW" size 14 color "#ffffff" bold True font "DejaVuSans-Bold.ttf"
                                                frame:
                                                    background ("#8b3a0af0" if _cn_has_new else "#1e0f06f0")
                                                    padding (14, 14, 14, 14)
                                                    xsize 474
                                                    vbox:
                                                        spacing 4
                                                        xfill True
                                                        text _cn:
                                                            font "DejaVuSans-Bold.ttf"
                                                            size 26
                                                            color "#f5e8d0"
                                                            bold True
                                                            xalign 0.5
                                                        text "{size=13}{color=#9a8060}[[ tap to view ]{/color}{/size}":
                                                            font "DejaVuSans.ttf"
                                                            xalign 0.5
                            null height 22
                else:
                    text "No characters added yet." style "journal_scene_desc" xalign 0.5 yalign 0.5

            # ==============================================================
            # VIEW C: EVENTS SECTION
            # ==============================================================
            elif journal_tab == "Events":

                # Done / Available sub-tabs
                hbox:
                    xalign 0.5
                    spacing 6
                    for _wetab in ["Available", "Done"]:
                        $ _wea = (_wetab == journal_events_tab)
                        textbutton "[_wetab]":
                            style "journal_tab_btn"
                            background       ("#5c3318ee" if _wea else "#c4a882cc")
                            hover_background "#7a4e28"
                            text_style       ("journal_tab_text_on" if _wea else "journal_tab_text_off")
                            action SetVariable("journal_events_tab", _wetab)

                null height 14

                $ _ew_done = (journal_events_tab == "Done")
                $ _wef     = [e for e in journal_events_list if bool(e.get("done",False)) == _ew_done]
                $ _werows  = [_wef[_i:_i+3] for _i in range(0, len(_wef), 3)]

                if _wef:
                    viewport:
                        mousewheel True
                        scrollbars ("vertical" if len(_werows) > 2 else None)
                        draggable True
                        ysize 650
                        xsize 1488
                        vbox:
                            spacing 22
                            xfill True
                            for _werow in _werows:
                                hbox:
                                    xalign 0.5
                                    spacing 22
                                    for _wev in _werow:
                                        $ _wei  = _wev.get("image","")  or "gui/journal_icon.png"
                                        $ _wen  = _wev.get("name","")
                                        $ _wev_snap = _wev
                                        frame:
                                            style "journal_card_frame"
                                            xsize 474
                                            vbox:
                                                spacing 0
                                                # Image — click to open detail popup
                                                button:
                                                    xsize 474
                                                    ysize 267
                                                    background       (Transform(_wei, xsize=474, ysize=267, blur=10.0, matrixcolor=SaturationMatrix(0)) if not _ew_done else Transform(_wei, xsize=474, ysize=267))
                                                    hover_background (Transform(_wei, xsize=474, ysize=267, alpha=0.90, blur=10.0, matrixcolor=SaturationMatrix(0)) if not _ew_done else Transform(_wei, xsize=474, ysize=267, alpha=0.70))
                                                    action SetScreenVariable("card_detail", _wev_snap)
                                                # Title bar — click to open detail popup
                                                button:
                                                    xfill True
                                                    background "#f5ead0ee"
                                                    hover_background "#e8d4b0"
                                                    padding (14, 10, 14, 12)
                                                    action SetScreenVariable("card_detail", _wev_snap)
                                                    text "[_wen]" style "journal_card_title"
                            null height 22
                else:
                    $ _wempty = ("No events completed yet." if _ew_done else "No events available yet.")
                    text "[_wempty]" style "journal_scene_desc" xalign 0.5 yalign 0.5

    # ------------------------------------------------------------------
    # Close button
    # ------------------------------------------------------------------
    textbutton "x Close":
        xalign 0.95
        yalign 0.04
        text_size 28
        text_color "#8b5e3c"
        text_hover_color "#c0392b"
        text_font "DejaVuSans.ttf"
        action [
            SetVariable("journal_char_selected", None),
            SetVariable("journal_detail_tab", "Available"),
            Return(),
        ]

    # ------------------------------------------------------------------
    # Card detail popup overlay
    # ------------------------------------------------------------------
    if card_detail is not None:

        button:
            xfill True
            yfill True
            background "#000000bb"
            action SetScreenVariable("card_detail", None)

        # Outer card border (dark brown)
        frame:
            xsize 1060
            ysize 880
            xalign 0.5
            yalign 0.5
            background "#3b2714"
            padding (4, 4, 4, 4)

            # Inner card body
            frame:
                xfill True
                yfill True
                background "#f5ead0"
                padding (0, 0, 0, 0)

                vbox:
                    spacing 0

                    # Image banner
                    $ _cd_img = card_detail.get("image", "") or "gui/journal_icon.png"
                    $ _cd_done = card_detail.get("done", False)
                    frame:
                        xfill True
                        ysize 560
                        background "#1a0e06"
                        padding (0, 0, 0, 0)
                        add (Transform(_cd_img, xsize=1052, ysize=560, blur=10.0, matrixcolor=SaturationMatrix(0)) if not _cd_done else Transform(_cd_img, xsize=1052, ysize=560)) xalign 0.5 yalign 0.5

                    # Title bar
                    frame:
                        xfill True
                        background "#5c3318"
                        padding (20, 10, 20, 10)
                        text (card_detail.get("name", "")):
                            font "DejaVuSans.ttf"
                            size 24
                            color "#f5ead0"
                            bold True

                    # Description + requirements
                    frame:
                        background None
                        padding (24, 16, 24, 16)
                        xfill True
                        vbox:
                            spacing 10
                            if _cd_done:
                                # Scene completed — show full description
                                text (card_detail.get("desc", "")):
                                    font "DejaVuSans.ttf"
                                    size 17
                                    color "#5a4030"
                                    italic True
                            else:
                                # Scene not yet done — show only how to unlock it
                                text "How to unlock:":
                                    font "DejaVuSans.ttf"
                                    size 15
                                    color "#5a4030"
                                    bold True
                                $ _cd_req = card_detail.get("req", "") or "No requirements listed."
                                frame:
                                    background "#e8d4b0"
                                    padding (12, 10, 12, 10)
                                    xfill True
                                    text "[_cd_req]":
                                        font "DejaVuSans.ttf"
                                        size 16
                                        color "#8b2030"

            # Close button pinned top-right over the border
            textbutton "x":
                xalign 1.0
                yalign 0.0
                xpadding 12
                ypadding 6
                text_size 24
                text_color "#f5ead0"
                text_hover_color "#ff5555"
                background "#3b2714"
                hover_background "#5c1010"
                action SetScreenVariable("card_detail", None)

        key "K_ESCAPE" action SetScreenVariable("card_detail", None)

    # ------------------------------------------------------------------
    # Lightbox overlay
    # ------------------------------------------------------------------
    if lightbox_img is not None:

        button:
            xfill True
            yfill True
            background "#000000cc"
            action SetScreenVariable("lightbox_img", None)

        # Outer card border
        frame:
            xsize 984
            ysize 580
            xalign 0.5
            yalign 0.5
            background "#3b2714"
            padding (4, 4, 4, 4)

            # Inner card body
            frame:
                xfill True
                yfill True
                background "#1a0e06"
                padding (0, 0, 0, 0)

                vbox:
                    spacing 0

                    # Image
                    frame:
                        xfill True
                        ysize 546
                        background "#000000"
                        padding (0, 0, 0, 0)
                        add Transform(lightbox_img, maxsize=(976, 546)) xalign 0.5 yalign 0.5

                    # Bottom label bar
                    frame:
                        xfill True
                        background "#5c3318"
                        padding (20, 8, 20, 8)
                        text "Click outside or press Esc to close":
                            font "DejaVuSans.ttf"
                            size 14
                            color "#c4a882"
                            xalign 0.5

            # Close button
            textbutton "x":
                xalign 1.0
                yalign 0.0
                xpadding 12
                ypadding 6
                text_size 24
                text_color "#f5ead0"
                text_hover_color "#ff5555"
                background "#3b2714"
                hover_background "#5c1010"
                action SetScreenVariable("lightbox_img", None)

        key "K_ESCAPE" action SetScreenVariable("lightbox_img", None)


# ======================================================================
# Styles
# ======================================================================

style journal_title_text is default:
    font "DejaVuSans.ttf"
    size 48
    color "#3b2714"
    bold True

style journal_back_btn is default:
    xminimum 120
    xpadding 20
    ypadding 10
    background "#7a4e28cc"
    hover_background "#9b6238"

style journal_back_btn_text is default:
    font "DejaVuSans.ttf"
    size 20
    color "#ffffff"

style journal_tab_btn is default:
    xminimum 180
    xpadding 28
    ypadding 12

style journal_tab_text_on is default:
    font "DejaVuSans.ttf"
    size 22
    color "#ffffff"
    bold True

style journal_tab_text_off is default:
    font "DejaVuSans.ttf"
    size 22
    color "#3b2714"
    bold False

style journal_char_banner is default:
    background "#e8d8b0cc"
    padding (20, 10, 20, 10)

style journal_char_banner_name is default:
    font "DejaVuSans.ttf"
    size 34
    color "#3b2714"
    bold True

style journal_char_banner_desc is default:
    font "DejaVuSans.ttf"
    size 19
    color "#5a4030"
    italic True

style journal_card_frame is default:
    background "#f5ead0ee"
    xpadding 0
    ypadding 0

style journal_card_title is default:
    font "DejaVuSans.ttf"
    size 22
    color "#3b2714"
    bold True

style journal_card_desc is default:
    font "DejaVuSans.ttf"
    size 17
    color "#5a4030"
    italic True

style journal_card_req is default:
    font "DejaVuSans.ttf"
    size 14
    color "#8b2030"

# Legacy style names kept for any external references
style journal_scene_title is default:
    font "DejaVuSans.ttf"
    size 28
    color "#3b2714"
    bold True

style journal_scene_desc is default:
    font "DejaVuSans.ttf"
    size 22
    color "#5a4030"
    italic True

style journal_scene_req is default:
    font "DejaVuSans.ttf"
    size 19
    color "#8b2030"


# ======================================================================
# Journal: new-entry animations
# ======================================================================

transform journal_new_entry_anim:
    # Slides in from the left and gently pulses while visible
    on show:
        alpha 0.0
        xoffset -24
        linear 0.45 alpha 1.0 xoffset 0
    on idle:
        block:
            linear 1.8 alpha 0.82
            linear 1.8 alpha 1.0
            repeat
    on hide:
        linear 0.25 alpha 0.0

transform journal_card_new_anim:
    # Gentle fade-in then soft pulse for newly-completed event cards
    on show:
        alpha 0.0
        linear 0.35 alpha 1.0
    on idle:
        block:
            linear 1.2 alpha 0.80
            linear 1.2 alpha 1.0
            repeat

transform journal_char_new_anim:
    # Soft zoom pulse for character cards that have new entries
    on idle:
        block:
            linear 1.4 zoom 1.015
            linear 1.4 zoom 1.0
            repeat

transform journal_no_anim:
    # No-op transform used on non-new items
    alpha 1.0

transform journal_new_badge_anim:
    # Pops in then pulses the red NEW badge on the journal button
    on show:
        zoom 0.4
        alpha 0.0
        linear 0.25 zoom 1.15 alpha 1.0
        linear 0.12 zoom 1.0
    on idle:
        block:
            linear 0.9 zoom 1.08
            linear 0.9 zoom 1.0
            repeat

# ======================================================================
# Journal: new-entry styles
# ======================================================================

style journal_new_banner_text is default:
    font "DejaVuSans.ttf"
    size 24
    color "#ffffff"
    bold True

style journal_new_star_text is default:
    font "DejaVuSans.ttf"
    size 22
    color "#ffd700"
    bold True


# ======================================================================
# Journal Toast Notification
# Displays a styled on-screen popup whenever a new journal entry is added.
# ======================================================================

screen journal_toast(char_name="", event_name=""):
    zorder 200
    modal False

    frame at journal_toast_slide:
        xalign 0.97
        yalign 0.04
        xminimum 400
        xmaximum 500
        background "#1c0f07f0"
        padding (0, 0, 0, 0)

        vbox:
            spacing 0

            # Gold header strip
            frame:
                background "#8b4513ee"
                xfill True
                padding (12, 6, 12, 6)
                hbox:
                    xalign 0.5
                    spacing 10
                    text "{size=13}{color=#ffd700}✦{/color}{/size}" size 13
                    text "{size=13}{b}{color=#ffd700}NEW JOURNAL ENTRY{/color}{/b}{/size}" size 13
                    text "{size=13}{color=#ffd700}✦{/color}{/size}" size 13

            # Thin gold rule
            frame:
                background "#c8860099"
                xfill True
                ysize 2
                padding (0, 0, 0, 0)

            # Body
            frame:
                background "#2b1507ee"
                xfill True
                padding (16, 10, 16, 14)
                vbox:
                    spacing 5
                    hbox:
                        spacing 10
                        yalign 0.5
                        text "✒" size 26 color "#b8860b"
                        vbox:
                            yalign 0.5
                            spacing 3
                            if event_name:
                                text "[event_name]":
                                    font "DejaVuSans.ttf"
                                    size 15
                                    color "#f5e6c8"
                                    bold True
                                    italic True
                            if char_name:
                                text "— [char_name]":
                                    font "DejaVuSans.ttf"
                                    size 12
                                    color "#c8a97e"

    timer 4.5 action [Hide("journal_toast"), Show("journal_toast_delay")]


# Short gap between back-to-back toasts, then shows the next queued one.
screen journal_toast_delay():
    zorder 199
    timer 0.6 action [Hide("journal_toast_delay"), Function(_journal_toast_show_next)]


transform journal_toast_slide:
    on show:
        alpha 0.0
        xoffset 70
        linear 0.38 alpha 1.0 xoffset 0
    on idle:
        # very subtle pulse to draw the eye
        block:
            linear 2.0 alpha 0.88
            linear 2.0 alpha 1.0
            repeat
    on hide:
        linear 0.35 alpha 0.0 xoffset 50


