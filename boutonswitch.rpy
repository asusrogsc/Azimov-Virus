# ============================================
# Switch Character
# ============================================

screen bouton_switch_perso():
    frame:
        xalign 0.95
        yalign 0.05
        background "#2c3e50"
        padding (10, 10)

        if personnage_actuel == "Dave":
            # 1. On prépare la variable globale, puis on saute vers le label de traitement
            textbutton "Incarner Rocky" action [SetVariable("prochain_perso", "Rocky"), Jump("action_switch_vers")]
        else:
            textbutton "Incarner Dave" action [SetVariable("prochain_perso", "Dave"), Jump("action_switch_vers")]

# Le label adapté :
label action_switch_vers:
    # On récupère la valeur stockée par le bouton
    $ personnage_actuel = prochain_perso
    
    if personnage_actuel == "Dave":
        $ phone_owner = "Dave"
        $ nom_pc_actuel = "Dave"
        "Changement de personnage... Vous incarnez désormais Dave."
    else:
        $ nom_pc_actuel = "Rocky"
        $ phone_owner = "AZrocky"
        "Changement de personnage... Vous incarnez désormais Rocky."
        
    jump home_areas