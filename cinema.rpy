# ============================================
# Cinoche
# ============================================

label cinemaview:
    python:
        if game_time.is_morning():
            cinema = "cinemamor"
        elif game_time.is_afternoon():
            cinema = "cinemaaft"
        elif game_time.is_evening():
            cinema = "cinemaeve"
        else:  # night
            cinema = "cinemanig"


    scene expression cinema
    with fade
    if personnage_actuel == "Dave":
        show dave happy at left_small
    else:
        show madd violated at left_small
    with dissolve
    p "Aaah me voici dans le cinoche, que faire?"
    menu:
                "Regarder un film":
                    p "Un bon film pour passer le temps !"
                    call advance_time_and_check(minutes=60)
                    jump cinemaview
                
                "Regarder quelque chose de plus intéressant":
                    p "J'ai un large choix, enfin des heures."
                    menu:
                        "3D ou IA Blowjobs":
                            menu:
                                "1":
                                    p "Kiffe"
                                    $ renpy.movie_cutscene("images/LindsayBedroom/Emy1.webm")
                                    jump cinemaview
                            
                                "2":
                                    p "Kiffe"
                                    $ renpy.movie_cutscene("images/LindsayBedroom/Emy1.webm")
                                    jump cinemaview

                        "IRL Blowjobs":
                            menu:
                                "Streameuse":
                                    menu:
                                        "Arz":
                                            menu:
                                                "Arz 1":
                                                    p "Kiffe"
                                                    $ renpy.movie_cutscene("images/videos/Arz1.webm")
                                                    jump cinemaview

                                                "Arz 2":
                                                    p "Kiffe"
                                                    $ renpy.movie_cutscene("images/videos/Arz2.webm")
                                                    jump cinemaview

                                                "Arz 3":
                                                    p "Kiffe"
                                                    $ renpy.movie_cutscene("images/videos/Arz3.webm")
                                                    jump cinemaview

                                                "Arz 4":
                                                    p "Kiffe"
                                                    $ renpy.movie_cutscene("images/videos/Arz4.webm")
                                                    jump cinemaview
                  
                                "PornStar":
                                    menu:
                                        "Brea":
                                            menu:
                                                "Brea 1":
                                                    p "Kiffe"
                                                    $ renpy.movie_cutscene("images/videos/Brea1.webm")
                                                    jump cinemaview

                                                "Brea 2":
                                                    p "Kiffe"
                                                    $ renpy.movie_cutscene("images/videos/Arz2.webm")
                                                    jump cinemaview

                                                "Brea 3":
                                                    p "Kiffe"
                                                    $ renpy.movie_cutscene("images/videos/Arz3.webm")
                                                    jump cinemaview

                                                "Brea 4":
                                                    p "Kiffe"
                                                    $ renpy.movie_cutscene("images/videos/Arz4.webm")
                                                    jump cinemaview

                                        "Molly":
                                            menu:
                                                "Molly 1":
                                                    p "Kiffe"
                                                    $ renpy.movie_cutscene("images/videos/Molly1.webm")
                                                    jump cinemaview

                                                "Brea 2":
                                                    p "Kiffe"
                                                    $ renpy.movie_cutscene("images/videos/Arz2.webm")
                                                    jump cinemaview

                                                "Brea 3":
                                                    p "Kiffe"
                                                    $ renpy.movie_cutscene("images/videos/Arz3.webm")
                                                    jump cinemaview

                                                "Brea 4":
                                                    p "Kiffe"
                                                    $ renpy.movie_cutscene("images/videos/Arz4.webm")
                                                    jump cinemaview


                                          

                                "Molly":
                                    menu:
                                        "Molly 1":
                                            p "Kiffe"
                                            $ renpy.movie_cutscene("images/videos/Molly1.webm")
                                            jump cinemaview

                                        "Molly 2":
                                            p "Kiffe"
                                            $ renpy.movie_cutscene("images/LindsayBedroom/Emy1.webm")
                                            jump cinemaview
                             
                                

                        "Retour":
                            jump cinemaview

                    jump home_areas

                "Attendre ici":
                    show madd think at left_small
                    with dissolve
                    p "How long should I wait here?"
                    menu:
                        "1 minute":
                            call advance_time_and_check(minutes=1)
                            jump cinemaview
                        "5 minutes":
                            call advance_time_and_check(minutes=5)
                            jump cinemaview
                        "15 minutes":
                            call advance_time_and_check(minutes=15)
                            jump lindsaybedroom_door
                        "30 minutes":
                            call advance_time_and_check(minutes=30)
                            jump lindsaybedroom_door
                        "1 hour":
                            call advance_time_and_check(minutes=60)
                            jump lindsaybedroom_door
                        "3 hours":
                            call advance_time_and_check(minutes=180)
                            jump lindsaybedroom_door
                        "6 hours":
                            call advance_time_and_check(minutes=360)
                            jump lindsaybedroom_door
                        "12 hours":
                            call advance_time_and_check(minutes=720)
                            jump lindsaybedroom_door
                        "never mind":
                            jump lindsaybedroom_door
                        "Retourner au lobby":
                            jump home_areas
                "Lobby":
                    jump home_areas

return

