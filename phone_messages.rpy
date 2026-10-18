# ============================================================
# FONCTION DE SYNCHRONISATION EN TÂCHE DE FOND
# ============================================================
init python:
    def sync_rocky_messages(choix_id):
        """Ajoute les messages de manière invisible dans le téléphone de Rocky et de Dave."""
        # On s'assure que les structures de base existent
        if "Dave" in phone_messages and "AZrocky" in phone_messages:
            
            # --- CHOIX 1 ---
            if choix_id == 1:
                phone_messages["Dave"]["AZrocky"].append({"id": store.phone_msg_id_counter, "sender": "AZrocky", "text": "Super", "timestamp": days_passed, "time_hour": game_time.hour, "time_minute": game_time.minute})
                store.phone_msg_id_counter += 1
                phone_messages["AZrocky"]["Dave"].append({"id": store.phone_msg_id_counter, "sender": "Dave", "text": "Bien, c'est vrai qu'on se fait chier...", "timestamp": days_passed, "time_hour": game_time.hour, "time_minute": game_time.minute})
                store.phone_msg_id_counter += 1
                phone_messages["AZrocky"]["Dave"].append({"id": store.phone_msg_id_counter, "sender": "player", "text": "Super", "timestamp": days_passed, "time_hour": game_time.hour, "time_minute": game_time.minute})
                store.phone_msg_id_counter += 1
                
            # --- CHOIX 2 ---
            elif choix_id == 2:
                phone_messages["Dave"]["AZrocky"].append({"id": store.phone_msg_id_counter, "sender": "AZrocky", "text": "Réfléchis y stp", "timestamp": days_passed, "time_hour": game_time.hour, "time_minute": game_time.minute})
                store.phone_msg_id_counter += 1
                phone_messages["AZrocky"]["Dave"].append({"id": store.phone_msg_id_counter, "sender": "Dave", "text": "On est bien comme ça...", "timestamp": days_passed, "time_hour": game_time.hour, "time_minute": game_time.minute})
                store.phone_msg_id_counter += 1
                phone_messages["AZrocky"]["Dave"].append({"id": store.phone_msg_id_counter, "sender": "player", "text": "Réfléchis y stp", "timestamp": days_passed, "time_hour": game_time.hour, "time_minute": game_time.minute})
                store.phone_msg_id_counter += 1
                
            # --- CHOIX 3 ---
            elif choix_id == 3:
                phone_messages["Dave"]["AZrocky"].append({"id": store.phone_msg_id_counter, "sender": "AZrocky", "text": "Ok, même heure, même endroit.", "timestamp": days_passed, "time_hour": game_time.hour, "time_minute": game_time.minute})
                store.phone_msg_id_counter += 1
                phone_messages["AZrocky"]["Dave"].append({"id": store.phone_msg_id_counter, "sender": "Dave", "text": "Plus tard...", "timestamp": days_passed, "time_hour": game_time.hour, "time_minute": game_time.minute})
                store.phone_msg_id_counter += 1
                phone_messages["AZrocky"]["Dave"].append({"id": store.phone_msg_id_counter, "sender": "player", "text": "Ok, même heure, même endroit.", "timestamp": days_passed, "time_hour": game_time.hour, "time_minute": game_time.minute})
                store.phone_msg_id_counter += 1
                
            # --- CHOIX 4 (Intro 2) ---
            elif choix_id == 4:
                phone_messages["Dave"]["AZrocky"].append({"id": store.phone_msg_id_counter, "sender": "AZrocky", "text": ":D", "timestamp": days_passed, "time_hour": game_time.hour, "time_minute": game_time.minute})
                store.phone_msg_id_counter += 1
                phone_messages["AZrocky"]["Dave"].append({"id": store.phone_msg_id_counter, "sender": "Dave", "text": "De rien", "timestamp": days_passed, "time_hour": game_time.hour, "time_minute": game_time.minute})
                store.phone_msg_id_counter += 1
                phone_messages["AZrocky"]["Dave"].append({"id": store.phone_msg_id_counter, "sender": "player", "text": ":D", "timestamp": days_passed, "time_hour": game_time.hour, "time_minute": game_time.minute})
                store.phone_msg_id_counter += 1
                
            # --- CHOIX 5 (Intro 2) ---
            elif choix_id == 5:
                phone_messages["Dave"]["AZrocky"].append({"id": store.phone_msg_id_counter, "sender": "AZrocky", "text": "Pour lancer ta mission va sur le pc !", "timestamp": days_passed, "time_hour": game_time.hour, "time_minute": game_time.minute})
                store.phone_msg_id_counter += 1
                phone_messages["AZrocky"]["Dave"].append({"id": store.phone_msg_id_counter, "sender": "Dave", "text": "Ok, je fais ça", "timestamp": days_passed, "time_hour": game_time.hour, "time_minute": game_time.minute})
                store.phone_msg_id_counter += 1
                phone_messages["AZrocky"]["Dave"].append({"id": store.phone_msg_id_counter, "sender": "player", "text": "Pour lancer ta mission va sur le pc !", "timestamp": days_passed, "time_hour": game_time.hour, "time_minute": game_time.minute})
                store.phone_msg_id_counter += 1
                
        renpy.restart_interaction()

# ============================================================
# SCENARIOS DES MESSAGES
# ============================================================

label rocky_phone_intro:
    "Vous avez reçu un message"
    python:
        receive_message("Dave", "AZrocky", "Hey, mardi vers 15h00, je serai au park, possible qu'on discute... marre qu'on soit seul, enfin bref viens.")
        
        if "AZrocky" in phone_messages and "Dave" in phone_messages["AZrocky"]:
            phone_messages["AZrocky"]["Dave"].append({
                "id": store.phone_msg_id_counter, "sender": "player", 
                "text": "Hey, mardi vers 15h00, je serai au park, possible qu'on discute... marre qu'on soit seul, enfin bref viens."
            })
            store.phone_msg_id_counter += 1

        set_message_replies("AZrocky", [
                {"text": "Bien, c'est vrai qu'on se fait chier...", "action": [Function(send_message, "AZrocky", "Bien, c'est vrai qu'on se fait chier..."), Function(sync_rocky_messages, 1)]},
                {"text": "On est bien comme ça...", "action": [Function(send_message, "AZrocky", "On est bien comme ça..."), Function(sync_rocky_messages, 2)]},
                {"text": "Plus tard...", "action": [Function(send_message, "AZrocky", "Plus tard..."), Function(sync_rocky_messages, 3)]},
            ])
    return

label rocky_phone_intro2:
    "Vous avez reçu un message"
    python:
        receive_message("Dave", "AZrocky", "Merci d'être passer, je compte sur toi pour nous trouver des gens. n'hésite pas à regarder les infos !")
        
        if "AZrocky" in phone_messages and "Dave" in phone_messages["AZrocky"]:
            phone_messages["AZrocky"]["Dave"].append({
                "id": store.phone_msg_id_counter, "sender": "player", 
                "text": "Merci d'être passer, je compte sur toi pour nous trouver des gens. n'hésite pas à regarder les infos !"
            })
            store.phone_msg_id_counter += 1

        set_message_replies("AZrocky", [
                {"text": "De rien", "action": [Function(send_message, "AZrocky", "De rien"), Function(sync_rocky_messages, 4)]},
                {"text": "Ok, je fais ça", "action": [Function(send_message, "AZrocky", "Ok, je fais ça"), Function(sync_rocky_messages, 5)]},
            ])
    return
label rocky_phone_save2:
    "Vous avez reçu un message"
    python:
        receive_message("Dave", "AZrocky", "Merci d'être passer, je compte sur toi pour trouver une autre personne. n'hésite pas à regarder les infos !")
        
        if "AZrocky" in phone_messages and "Dave" in phone_messages["AZrocky"]:
            phone_messages["AZrocky"]["Dave"].append({
                "id": store.phone_msg_id_counter, "sender": "player", 
                "text": "Merci d'être passer, je compte sur toi pour trouver une autre personne. n'hésite pas à regarder les infos !"
            })
            store.phone_msg_id_counter += 1

        set_message_replies("AZrocky", [
                {"text": "De rien", "action": [Function(send_message, "AZrocky", "De rien"), Function(sync_rocky_messages, 4)]},
                {"text": "Ok, je fais ça", "action": [Function(send_message, "AZrocky", "Ok, je fais ça"), Function(sync_rocky_messages, 5)]},
            ])
    return

label lindsayaftersave:
    "Vous avez reçu un message"
    python:
        # 1. On précise "Dave" comme premier argument
        receive_message("Dave", "Lindsay", "Merci pour tout, enfin un endroit où me poser ! en sécurité...")
        
        # 2. On adapte les réponses automatiques
        set_message_replies("Lindsay", [
                {"text": "Oui tu es en sécurité maintenant!", "action": [Function(send_message, "Lindsay", "Oui tu es en sécurité maintenant!"), Function(receive_message, "Dave", "Lindsay", "Hihi")]},
                {"text": "Je l'espère...", "action": [Function(send_message, "Lindsay", "Je l'espère..."), Function(receive_message, "Dave", "Lindsay", "Comment ça ?")]},
            ])
    return

label mzelleaftersave:
    "Vous avez reçu un message"
    python:
        # 1. On précise "Dave" comme premier argument
        receive_message("Dave", "Mzelle", "Merci pour tout, enfin un endroit où me poser ! en sécurité...")
        
        # 2. On adapte les réponses automatiques
        set_message_replies("Lindsay", [
                {"text": "Oui tu es en sécurité maintenant!", "action": [Function(send_message, "Mzelle", "Oui tu es en sécurité maintenant!"), Function(receive_message, "Dave", "Mzelle", "Hihi")]},
                {"text": "Je l'espère...", "action": [Function(send_message, "Mzelle", "Je l'espère..."), Function(receive_message, "Dave", "Mzelle", "Comment ça ?")]},
            ])
    return

label dad_after_sleep_message:
    if not dad_after_sleep_message_sent:
        "You received a message"
        python:
            receive_message("dad", "I loved feeling your body around my cock... The way you submitted to me, the way your body responded even when your mind was trying to resist... God, you drive me crazy. I want more of that. Keep sleeping with me, and I'll unlock your room. You'll have your freedom... sort of.")
            set_message_replies("dad", [
                {"text": "Okay daddy", "action": [Function(send_message, "dad", "Okay daddy"), Function(receive_message, "dad", "You're gonna be my wife soon enough. Just keep being a good girl for me.")]},
                {"text": "Fuck no old man", "action": [Function(send_message, "dad", "Fuck no old man"), Function(receive_message, "dad", "You better watch your tone with me. I'm getting real tired of your attitude. Keep this up and you'll regret it.")]},
            ])
            dad_after_sleep_message_sent = True
    
    return


label dad_saw_brother_madd_message:
    if dad_sees_brother_madd_together and not dad_saw_brother_madd_message_sent:
        "You received a message"
        python:
            receive_message("dad", "I know what your hoe ass is doing in the living room . I would be careful if i were you")
            dad_saw_brother_madd_message_sent = True
    return


label check_family_messages:
    # ════════════════════════════════════════════════════════════
    #  SCENE HINT MESSAGES — one hint per day-change, probability-gated
    #  Tone & content scale with BOTH lust AND intimacy
    #    intimacy low  (<20) = cold, distant, matter-of-fact
    #    intimacy mid  (20-45) = familiar, suggestive, probing
    #    intimacy high (46+) = possessive, demanding, explicit
    # ════════════════════════════════════════════════════════════

# ╔═══════════════════════════════════════════════════════════════╗
# ║                BROTHER HINT MESSAGES                          ║
# ╚═══════════════════════════════════════════════════════════════╝

label dad_phone_bathroom_warning:
    if not dad_bathroom_warning_sent:
        "Vous avez reçu un message"
        python:
            receive_message("Dave", "dad", "Do not go to the bathroom between 5 and 6. It's my lone time. If you come you will...")
            set_message_replies("dad", [
                {"text": "Got it dad", "action": [Function(send_message, "Dave", "dad", "Got it dad"), Function(receive_message, "Dave", "dad", "Good girl")]},
                {"text": "Like I would ever listen to you", "action": [Function(send_message, "Dave", "dad", "Like I would ever listen to you"), Function(receive_message, "Dave", "dad", "Go ahead and try it then bitch")]},
                {"text": "Okay", "action": [Function(send_message, "Dave", "dad", "Okay"), Function(receive_message, "Dave", "dad", "Good you know your place")]},
            ])
            dad_bathroom_warning_sent = True
    
    return

