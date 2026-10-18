# ============================================
# Sauvetage Harem
# ============================================

label lindsay_save:

    scene scene_home_lobby_area_morning

"C'est commme ça que le plus gros de l'histoire commence, chercher des personnes dans le besoin et proposer notre maison et notre aide."

with fade
show dave happy at left_small
with dissolve
p "Hey, une fois ici je vais où ?"
menu:
    "Lindsay":
        python:
            if "Lindsay" not in contacts_met["Dave"]:
                contacts_met["Dave"].append("Lindsay")
            "Vous avez ajouté Lindsay à vos contacts."
        $savelindsay += 1
        $ nom_chambre_1 = "Chambre de Lindsay"
        call lindsayaftersave from _call_lindsayaftersave
        jump lindsaybedroom_door
        

return

label mzelle_save:

    scene scene_home_lobby_area_morning

"Doucement mais surement, on tombe dans le piège, on vit avec le moment présent, que vas t'il se passer ensuite ?"

with fade
show dave happy at left_small
with dissolve
p "Hey, une fois ici je vais où ?"
menu:
    "Mzelle":
        python:
            if "Mzelle" not in contacts_met["Dave"]:
                contacts_met["Dave"].append("Mzelle")
            "Vous avez ajouté Mzelle à vos contacts."
        $savemzelle += 1
        $ nom_chambre_2 = "Chambre de Mzelle"
        call mzelleaftersave from _call_mzelleaftersave
        jump mzellebedroom_door
        

return

label sisters_save:

    scene scene_home_lobby_area_morning

"Doucement mais surement, on tombe dans le piège, on vit avec le moment présent, que vas t'il se passer ensuite ?"

with fade
show dave happy at left_small
with dissolve
p "Hey, une fois ici je vais où ?"
menu:
    "Sisters":
        python:
            if "Prisci" not in contacts_met["Dave"]:
                contacts_met["Dave"].append("Prisci")
            "Vous avez ajouté Prisci à vos contacts."
        $savesisters += 1
        $ nom_chambre_3 = "Chambre des soeurs"
        call sistersaftersave from _call_sistersaftersave
        jump sistersbedroom_door
        

return
