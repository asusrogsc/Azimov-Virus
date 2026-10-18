# Phone UI System - Modern Smartphone Design
# ============================================================

# ── State Variables ──────────────────────────────────────────
default phone_owner = "Dave"
default phone_menu_open = False
default selected_contact = None
default phone_feature = "home"  # "home", "messages", "message_chat", "contacts", "stats", "inventory"
default phone_messages = {
    "Dave": {
        "LeVieux": [], "brother": [], "AZrocky": [], "Lindsay": [], "Mzelle": [], "unknown": []
    },
    "AZrocky": {
        "LeVieux": [], "brother": [], "Dave": [], "Lindsay": [], "Mzelle": [], "unknown": []
    }
}
default current_message_contact = None
default temp_message = ""
default contacts_met = {
    "Dave": ["LeVieux"], 
    "AZrocky": ["LeVieux", "Dave"]
}
default unread_messages = {
    "Dave": {
        "LeVieux": 0, "AZrocky": 0, "Lindsay": 0, "Mzelle": 0, "unknown": 0
    },
    "AZrocky": {
        "LeVieux": 0, "Dave": 0, "Lindsay": 0, "Mzelle": 0, "unknown": 0
    }
}
default message_replies = {}
default phone_msg_id_counter = 0
default phone_reply_target = {}
default unreplied_messages = {}  # {contact: [msg_id, msg_id, ...]} — received msgs player hasn't replied to
default phone_reply_panel_open = False  # True when player has clicked Reply on a message
default phone_anim_offset = 0
default phone_stat_view = "general"  # "general", "sex"

# ── Asset Paths (shorthand) ─────────────────────────────────
define PHONE_ASSET = "gui/phone/assets/"


init python:
    def augmenter_corruption_lindsay(valeur=1):
        """Augmente la corruption de Lindsay dans le fichier persistant de l'ordinateur."""
        # 1. Si la variable n'existe pas dans l'ordinateur, on l'initialise à 0
        if store.persistent.linds_corruption is None:
            store.persistent.linds_corruption = 0
            
        # 2. On augmente la valeur persistante
        store.persistent.linds_corruption += valeur
        
        # 3. On synchronise notre dictionnaire de statistiques pour l'affichage
        if "Lindsay" in store.character_relations:
            store.character_relations["Lindsay"]["corruption"] = store.persistent.linds_corruption
            
        renpy.restart_interaction()

# ── Transforms ───────────────────────────────────────────────
transform phone_slide_in:
    xoffset -440
    alpha 0.0
    easein 0.3 xoffset 0 alpha 1.0

transform phone_slide_out:
    xoffset 0
    alpha 1.0
    easeout 0.2 xoffset -440 alpha 0.0

transform phone_fade_in:
    alpha 0.0
    linear 0.15 alpha 1.0

transform phone_bounce_in:
    zoom 0.8 alpha 0.0
    easein 0.25 zoom 1.0 alpha 1.0

transform phone_msg_appear:
    xoffset 20 alpha 0.0
    easein 0.2 xoffset 0 alpha 1.0

transform phone_btn_pulse:
    ease 1.5 zoom 1.06
    ease 1.5 zoom 1.0
    repeat

transform avatar_online_pulse:
    alpha 0.6
    ease 1.0 alpha 1.0
    ease 1.0 alpha 0.6
    repeat

transform phone_dim_in:
    alpha 0.0
    linear 0.2 alpha 1.0

# ── Styles ───────────────────────────────────────────────────
style phone_text:
    font "DejaVuSans.ttf"
    color "#dde4f0"
    size 16
    antialias True

style phone_text_bold:
    font "DejaVuSans-Bold.ttf"
    color "#eef2fa"
    size 16

style phone_text_small:
    font "DejaVuSans.ttf"
    color "#8899bb"
    size 13

style phone_text_tiny:
    font "DejaVuSans.ttf"
    color "#667799"
    size 11

style phone_header_text:
    font "DejaVuSans-Bold.ttf"
    color "#eef2fa"
    size 22

style phone_contact_name:
    font "DejaVuSans-Bold.ttf"
    color "#dde4f0"
    size 17

style phone_msg_text:
    font "DejaVuSans.ttf"
    color "#eef2fa"
    size 14

style phone_msg_text_dark:
    font "DejaVuSans.ttf"
    color "#c8d4e8"
    size 14

style phone_reply_quote_sender:
    font "DejaVuSans-Bold.ttf"
    color "#5588cc"
    size 10

style phone_reply_quote_text:
    font "DejaVuSans.ttf"
    color "#8899bb"
    size 11

style phone_stat_label:
    font "DejaVuSans.ttf"
    color "#aabbdd"
    size 15

style phone_stat_value:
    font "DejaVuSans-Bold.ttf"
    color "#eef2fa"
    size 15

# ── Screens ──────────────────────────────────────────────────

# ┌──────────────────────────────────────────┐
# │  TIME DISPLAY (top-left corner overlay)  │
# └──────────────────────────────────────────┘
screen time_display():
    zorder 49
    vbox:
        spacing 4
        xpos 15
        ypos 15
        hbox:
            spacing 6
            text "📅" size 22 color "#a0b8e0"
            text "[game_time.get_date_string()] [get_day_of_week()]" size 18 color "#c8d8f0" font "DejaVuSans.ttf" yalign 0.5
        hbox:
            spacing 6
            text "[get_time_emoji()]" size 26 color "#a0b8e0"
            text "[game_time.get_time_string()]" size 22 color "#eef2fa" font "DejaVuSans-Bold.ttf" yalign 0.5


# ┌──────────────────────────────────────────┐
# │  FLOATING PHONE BUTTON                   │
# └──────────────────────────────────────────┘
transform hud_btn_fade:
    alpha 0.25
    on hover:
        linear 0.15 alpha 1.0
    on idle:
        linear 0.15 alpha 0.25

screen phone_button():
    zorder 50

    if not _windows_hidden and not phone_menu_open and not selected_contact:
        python:
            if phone_owner in unread_messages:
                total_unread = sum(unread_messages[phone_owner].values())
            else:
                total_unread = 0

        fixed:
            xpos 15
            ypos 105
            xysize (72, 72)
            at phone_btn_pulse

            button:
                at hud_btn_fade
                xysize (72, 72)
                background Frame(PHONE_ASSET + "phone_button.png", 8, 8)
                hover_background Frame(PHONE_ASSET + "phone_button_hover.png", 8, 8)
                text "📱" size 36 color "#b0c8f0" xalign 0.5 yalign 0.5
                action [SetVariable("phone_menu_open", True), SetVariable("phone_feature", "home")]

            # Unread badge
            if total_unread > 0:
                frame:
                    xysize (26, 26)
                    xpos 48
                    ypos -4
                    background Frame(PHONE_ASSET + "notification_badge.png", 4, 4)
                    text "[total_unread]" size 13 color "#ffffff" xalign 0.5 yalign 0.5 bold True font "DejaVuSans-Bold.ttf"

        # Journal button next to the phone button
        fixed:
            xpos 95
            ypos 105
            xysize (72, 72)
            at phone_btn_pulse

            button:
                at hud_btn_fade
                xysize (72, 72)
                background Frame(PHONE_ASSET + "phone_button.png", 8, 8)
                hover_background Frame(PHONE_ASSET + "phone_button_hover.png", 8, 8)
                text "📜" size 34 color "#d9c49a" xalign 0.5 yalign 0.5
                action ShowMenu("journal")

            # Journal NEW badge
            if journal_any_new():
                frame at journal_new_badge_anim:
                    xysize (36, 18)
                    xpos 38
                    ypos -4
                    background "#c0390b"
                    text "NEW" size 10 color "#ffffff" xalign 0.5 yalign 0.5 bold True font "DejaVuSans-Bold.ttf"


# ┌──────────────────────────────────────────┐
# │  MAIN PHONE INTERFACE                    │
# └──────────────────────────────────────────┘
screen phone_interface():
    zorder 100

    # ════════════════════════════════════════════
    #  MESSAGE CHAT VIEW
    # ════════════════════════════════════════════
    if phone_feature == "message_chat" and current_message_contact:
        modal True

        # Dim backdrop
        button:
            xysize (1920, 1080)
            background Solid("#00000088")
            action NullAction()
            at phone_dim_in

        python:
            _contact = current_message_contact
            _contact_display = "Unknown Number" if _contact == "unknown" else _contact.capitalize()
            
            # Sécurité notifications
            if phone_owner in unread_messages and _contact in unread_messages.get(phone_owner, {}):
                unread_messages[phone_owner][_contact] = 0

            # Sécurité extraction des messages
            _messages = [m for m in phone_messages.get(phone_owner, {}).get(_contact, []) if isinstance(m, dict)]

            # Cartographie des avatars
            _contact_image_map = {
                "dad": "images/dad/dad creepy.png",
                "brother": "images/brother/brother creepy.png",
                "Dave": "images/brother/brother creepy.png",
                "AZrocky": "images/brother/brother creepy.png",
                "Lindsay": "images/brother/brother creepy.png",
                "unknown": "images/ui/unknown_avatar.png",
            }
            _avatar_path = _contact_image_map.get(_contact, "images/{}/{}.png".format(_contact, _contact))

            # ── Système de réponses ──
            _raw_replies = message_replies.get(_contact, {})
            if isinstance(_raw_replies, list):
                _old = _raw_replies
                _raw_replies = {}
                for _rm in reversed(_messages):
                    if isinstance(_rm, dict) and _rm.get("sender") != "player" and "id" in _rm:
                        _raw_replies[_rm["id"]] = _old
                        break
                message_replies[_contact] = _raw_replies

            # Détermination de la cible de réponse active
            _reply_target_id = phone_reply_target.get(_contact, None)
            if _reply_target_id not in _raw_replies or not _raw_replies.get(_reply_target_id, []):
                if _raw_replies:
                    _reply_target_id = sorted(_raw_replies.keys())[-1]
                    phone_reply_target[_contact] = _reply_target_id
                else:
                    _reply_target_id = None

            _replies = _raw_replies.get(_reply_target_id, []) if _reply_target_id is not None else []

            # Récupération du texte cité
            _reply_target_text = ""
            _reply_target_sender = ""
            if _reply_target_id is not None:
                for _rm in _messages:
                    if isinstance(_rm, dict) and _rm.get("id") == _reply_target_id:
                        _reply_target_text = _rm.get("text", "")[:60]
                        _reply_target_sender = _rm.get("sender", "")
                        if not _reply_target_text and _rm.get("image"):
                            _reply_target_text = "📷 Photo"
                        break

            _msgs_with_replies = set(_raw_replies.keys()) if _raw_replies else set()

        # Phone body
        fixed:
            xysize (420, 780)
            xpos 40
            ypos 30
            at phone_slide_in

            # Background
            add PHONE_ASSET + "chat_bg.png" xysize (392, 752) xpos 14 ypos 14

            # Phone frame overlay
            add PHONE_ASSET + "phone_frame.png" xysize (420, 780)

            # ── Status bar ──
            frame:
                xysize (392, 28)
                xpos 14
                ypos 14
                background Solid("#0c0e16e8")
                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 8
                    text "[game_time.get_time_string()]" size 11 color "#8899bb" font "DejaVuSans.ttf"
                    text "•" size 11 color "#445577"
                    text "📶" size 10
                    text "🔋" size 10

            # ── Chat header ──
            frame:
                xysize (392, 60)
                xpos 14
                ypos 42
                background Frame(PHONE_ASSET + "header_bg.png", 4, 4)
                hbox:
                    spacing 12
                    yalign 0.5
                    xoffset 8

                    # Back button
                    button:
                        xysize (36, 36)
                        yalign 0.5
                        background Frame(PHONE_ASSET + "back_button.png", 4, 4)
                        hover_background Frame(PHONE_ASSET + "back_button_hover.png", 4, 4)
                        action [SetVariable("phone_feature", "messages"), SetVariable("current_message_contact", None), SetVariable("phone_reply_panel_open", False)]

                    # Avatar
                    fixed:
                        xysize (44, 44)
                        yalign 0.5
                        if _avatar_path:
                            add Transform(_avatar_path, xysize=(42, 42), fit="cover") xalign 0.5 yalign 0.5
                        else:
                            frame:
                                xysize (42, 42)
                                xalign 0.5
                                yalign 0.5
                                background Solid("#1a2040")
                                text "?" xalign 0.5 yalign 0.5 size 26 color "#445577" font "DejaVuSans-Bold.ttf"
                        # Online dot (hidden for unknown contacts)
                        if _avatar_path:
                            frame:
                                xysize (10, 10)
                                xpos 32
                                ypos 32
                                background Solid("#44dd66")
                                at avatar_online_pulse

                    vbox:
                        yalign 0.5
                        text _contact_display style "phone_contact_name"
                        if _contact == "unknown":
                            text "Not in contacts" size 11 color "#886655" font "DejaVuSans.ttf"
                        else:
                            text "online" size 11 color "#55cc77" font "DejaVuSans.ttf"

                    null width 40

                    # Close phone button
                    button:
                        xysize (36, 36)
                        yalign 0.5
                        xalign 1.0
                        background Frame(PHONE_ASSET + "close_button.png", 4, 4)
                        hover_background Frame(PHONE_ASSET + "close_button_hover.png", 4, 4)
                        action [SetVariable("phone_feature", "home"), SetVariable("current_message_contact", None), SetVariable("phone_menu_open", False), SetVariable("phone_reply_panel_open", False)]

            # ── Messages area ──
            viewport:
                xysize (374, 620)
                xpos 23
                ypos 110
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    spacing 10
                    xfill True
                    yminimum 620
                    null height 6

                    if len(_messages) == 0:
                        null height 120
                        text "No messages yet" xalign 0.5 style "phone_text_small"
                        text "Messages will appear here" xalign 0.5 style "phone_text_tiny"
                    else:
                        for _idx, _msg in enumerate(_messages):
                            if isinstance(_msg, dict):
                                python:
                                    _msg_has_image = _msg.get("image", None)
                                    _msg_has_text = bool(_msg.get("text", ""))
                                    _msg_is_player = (_msg["sender"] == "player")
                                    if _msg_has_image:
                                        _msg_image_d = resolve_phone_image(_msg["image"])
                                    else:
                                        _msg_image_d = None

                                    # ── Reply-to-specific-message data ──
                                    _msg_id = _msg.get("id", None)

                                    # Does this message have pending reply options?
                                    _msg_has_pending = (_msg_id in _msgs_with_replies) if _msg_id else False
                                    _msg_is_active_target = (_reply_target_id == _msg_id) if _msg_id else False

                                    # Is this message itself a reply to another message?
                                    _msg_reply_to = _msg.get("reply_to", None)
                                    _msg_rt_text = ""
                                    _msg_rt_sender = ""
                                    if _msg_reply_to:
                                        for _rm2 in _messages:
                                            if _rm2.get("id") == _msg_reply_to:
                                                _msg_rt_text = _rm2.get("text", "")[:50]
                                                _msg_rt_sender = _rm2.get("sender", "")
                                                if not _msg_rt_text and _rm2.get("image"):
                                                    _msg_rt_text = "📷 Photo"
                                                break

                                    # ── Timestamp display ──
                                    _msg_time_str = format_msg_time(_msg)
                                    _msg_date_str = format_msg_date(_msg)

                                    # ── Date separator logic ──
                                    # Show a date header when the day changes between messages
                                    _show_date_sep = False
                                    _msg_ts = _msg.get("timestamp", -1)
                                    _msg_day = _msg.get("time_day", None)
                                    _msg_month = _msg.get("time_month", None)
                                    if _idx == 0:
                                        _show_date_sep = True
                                    else:
                                        _prev = _messages[_idx - 1]
                                        _prev_day = _prev.get("time_day", None)
                                        _prev_month = _prev.get("time_month", None)
                                        _prev_ts = _prev.get("timestamp", -1)
                                        if _msg_day is not None and _prev_day is not None:
                                            if _msg_day != _prev_day or _msg_month != _prev_month:
                                                _show_date_sep = True
                                        elif _msg_ts != _prev_ts:
                                            _show_date_sep = True

                                    # ── Unreplied indicator ──
                                    _msg_unreplied = False
                                    if not _msg_is_player and _msg_id:
                                        _unr_list = unreplied_messages.get(_contact, [])
                                        _msg_unreplied = (_msg_id in _unr_list)

                            # ── Date separator ──
                            if _show_date_sep and _msg_date_str:
                                hbox:
                                    xfill True
                                    xalign 0.5
                                    null height 8
                                hbox:
                                    xfill True
                                    frame:
                                        xalign 0.5
                                        xpadding 14
                                        ypadding 4
                                        background Solid("#1a2040c0")
                                        text _msg_date_str size 10 color "#667799" font "DejaVuSans.ttf" xalign 0.5
                                hbox:
                                    xfill True
                                    xalign 0.5
                                    null height 6

                            if _msg_is_player:
                                # ── Sent message (right-aligned, blue) ──
                                hbox:
                                    xfill True
                                    null width 70
                                    frame:
                                        xalign 1.0
                                        xmaximum 280
                                        xminimum 60
                                        background Frame(PHONE_ASSET + "bubble_sent.png", 10, 10)
                                        xpadding 14
                                        ypadding 10
                                        vbox:
                                            spacing 6
                                            # ── Reply-to quote (WhatsApp style) ──
                                            if _msg_reply_to and _msg_rt_text:
                                                frame:
                                                    xmaximum 252
                                                    background Solid("#ffffff0e")
                                                    ypadding 4
                                                    right_padding 8
                                                    left_padding 2
                                                    hbox:
                                                        spacing 0
                                                        add Solid("#5599dd") xysize (3, 30) yalign 0.0
                                                        null width 6
                                                        vbox:
                                                            spacing 1
                                                            text _msg_rt_sender.capitalize() size 10 color "#7094cc" font "DejaVuSans-Bold.ttf"
                                                            text _msg_rt_text size 11 color "#8899bb" font "DejaVuSans.ttf"
                                            if _msg_image_d:
                                                button:
                                                    background None
                                                    action NullAction()
                                                    add Transform(_msg_image_d, xsize=240, fit="contain")
                                            if _msg_has_text:
                                                text _msg["text"] style "phone_msg_text"
                                            null height 3
                                            hbox:
                                                xalign 1.0
                                                spacing 6
                                                if _msg_time_str:
                                                    text _msg_time_str size 9 color "#6688aa" font "DejaVuSans.ttf"
                                                text "✓✓" size 10 color "#90b0e0"
                            else:
                                # ── Received message (left-aligned, dark) ──
                                vbox:
                                    spacing 2
                                    hbox:
                                        xfill True
                                        frame:
                                            xalign 0.0
                                            xmaximum 280
                                            xminimum 60
                                            if _msg_is_active_target:
                                                background Frame(PHONE_ASSET + "bubble_received.png", 10, 10)
                                            else:
                                                background Frame(PHONE_ASSET + "bubble_received.png", 10, 10)
                                            xpadding 14
                                            ypadding 10
                                            vbox:
                                                spacing 6
                                                # ── Reply-to quote (WhatsApp style) ──
                                                if _msg_reply_to and _msg_rt_text:
                                                    frame:
                                                        xmaximum 252
                                                        background Solid("#ffffff08")
                                                        ypadding 4
                                                        right_padding 8
                                                        left_padding 2
                                                        hbox:
                                                            spacing 0
                                                            add Solid("#4477aa") xysize (3, 30) yalign 0.0
                                                            null width 6
                                                            vbox:
                                                                spacing 1
                                                                text _msg_rt_sender.capitalize() size 10 color "#5580bb" font "DejaVuSans-Bold.ttf"
                                                                text _msg_rt_text size 11 color "#667799" font "DejaVuSans.ttf"
                                                if _msg_image_d:
                                                    button:
                                                        background None
                                                        action NullAction()
                                                        add Transform(_msg_image_d, xsize=240, fit="contain")
                                                if _msg_has_text:
                                                    text _msg["text"] style "phone_msg_text_dark"
                                                # ── Time + unreplied indicator ──
                                                hbox:
                                                    xalign 0.0
                                                    spacing 6
                                                    if _msg_time_str:
                                                        text _msg_time_str size 9 color "#556677" font "DejaVuSans.ttf"
                                                    if _msg_unreplied:
                                                        text "• unreplied" size 9 color "#aa6644" font "DejaVuSans.ttf"
                                        null width 70

                                    # ── Tap-to-reply indicator ──
                                    if _msg_has_pending:
                                        hbox:
                                            xoffset 14
                                            spacing 4
                                            button:
                                                yminimum 24
                                                xpadding 10
                                                ypadding 3
                                                if _msg_is_active_target and phone_reply_panel_open:
                                                    background Solid("#2244aa60")
                                                else:
                                                    background Solid("#1a204080")
                                                hover_background Solid("#2a306090")
                                                action [SetDict(phone_reply_target, _contact, _msg_id), SetVariable("phone_reply_panel_open", True)]
                                                hbox:
                                                    spacing 4
                                                    text "↩" size 11 color "#6688cc"
                                                    text "Reply" size 10 color "#6688cc" font "DejaVuSans.ttf" yalign 0.5
                                            if _msg_is_active_target and phone_reply_panel_open:
                                                text "◆" size 8 color "#4466aa" yalign 0.5

                    null height 10

            # ── Reply options area (only shown when player clicks Reply) ──
            if phone_reply_panel_open and len(_replies) > 0:
                frame:
                    xysize (374, 230)
                    xpos 23
                    ypos 500
                    background Solid("#141824f0")

                    vbox:
                        spacing 2
                        xfill True

                        # ── Close / dismiss bar ──
                        hbox:
                            xfill True
                            yoffset 2
                            # ── Quoted message header (WhatsApp-style) ──
                            if _reply_target_text:
                                frame:
                                    xsize 320
                                    xalign 0.0
                                    yminimum 34
                                    background Solid("#1c2444")
                                    left_padding 4
                                    right_padding 8
                                    top_padding 5
                                    bottom_padding 5
                                    hbox:
                                        spacing 0
                                        yalign 0.5
                                        add Solid("#4477cc") xysize (3, 26) yalign 0.5
                                        null width 8
                                        vbox:
                                            spacing 1
                                            text ("↩ Replying to " + _reply_target_sender.capitalize()) size 10 color "#5588bb" font "DejaVuSans-Bold.ttf"
                                            text _reply_target_text size 11 color "#7799bb" font "DejaVuSans.ttf"
                            else:
                                frame:
                                    xsize 320
                                    xalign 0.0
                                    yminimum 34
                                    background Solid("#00000000")
                                    ypadding 4
                                    text "  💬 Choose a reply:" size 12 color "#6688aa" font "DejaVuSans.ttf"

                            # Close button
                            button:
                                xysize (36, 34)
                                xalign 1.0
                                yalign 0.0
                                background Solid("#1a204080")
                                hover_background Solid("#2a306090")
                                action SetVariable("phone_reply_panel_open", False)
                                text "✕" size 14 color "#667799" xalign 0.5 yalign 0.5

                        null height 4

                        # ── Multiple-message indicator ──
                        if len(_msgs_with_replies) > 1:
                            hbox:
                                xfill True
                                xoffset 8
                                text "📨 [len(_msgs_with_replies)] messages — tap ↩ Reply on another to switch" size 10 color "#556688" font "DejaVuSans.ttf"
                            null height 2

                        viewport:
                            xysize (370, 120)
                            scrollbars "vertical"
                            mousewheel True
                            draggable True

                            vbox:
                                spacing 6
                                xfill True

                                for _reply in _replies:
                                    button:
                                        xsize 354
                                        yminimum 42
                                        xalign 0.5
                                        xpadding 14
                                        ypadding 10
                                        background Frame(PHONE_ASSET + "reply_button.png", 14, 14)
                                        hover_background Frame(PHONE_ASSET + "reply_button_hover.png", 14, 14)
                                        action [_reply["action"], Function(tag_last_sent_as_reply, _contact, _reply_target_id), Function(clear_message_replies, current_message_contact, _reply_target_id), SetVariable("phone_reply_panel_open", False)]
                                        text _reply["text"] style "phone_msg_text" xalign 0.0
            else:
                pass



    # ════════════════════════════════════════════
    #  PHONE MAIN SCREEN (home / messages list / contacts)
    # ════════════════════════════════════════════
    elif phone_menu_open and not selected_contact:
        modal True

        # Dim backdrop
        button:
            xysize (1920, 1080)
            background Solid("#00000088")
            action NullAction()
            at phone_dim_in

        python:
            if phone_owner in unread_messages:
                _total_unread = sum(unread_messages[phone_owner].values())
            else:
                _total_unread = 0

        fixed:
            xysize (420, 780)
            xpos 40
            ypos 30
            at phone_slide_in

            # Background
            add PHONE_ASSET + "phone_bg.png" xysize (392, 752) xpos 14 ypos 14

            # Phone frame overlay
            add PHONE_ASSET + "phone_frame.png" xysize (420, 780)

            # ── Status bar ──
            frame:
                xysize (392, 28)
                xpos 14
                ypos 14
                background Solid("#0c0e16e8")
                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 8
                    text "[game_time.get_time_string()]" size 11 color "#8899bb" font "DejaVuSans.ttf"
                    text "•" size 11 color "#445577"
                    text "📶" size 10
                    text "🔋" size 10

            # ── Header ──
            frame:
                xysize (392, 56)
                xpos 14
                ypos 42
                background Frame(PHONE_ASSET + "header_bg.png", 4, 4)
                hbox:
                    spacing 12
                    xoffset 14
                    yalign 0.5
                    if phone_feature == "home":
                        text "📱 Phone" style "phone_header_text"
                    elif phone_feature == "messages":
                        text "💬 Messages" style "phone_header_text"
                    elif phone_feature == "contacts":
                        text "👥 Contacts" style "phone_header_text"
                    elif phone_feature == "inventory":
                        text "💊 Inventory" style "phone_header_text"

                # Close button
                button:
                    xysize (36, 36)
                    xalign 1.0
                    yalign 0.5
                    xoffset -14
                    background Frame(PHONE_ASSET + "close_button.png", 4, 4)
                    hover_background Frame(PHONE_ASSET + "close_button_hover.png", 4, 4)
                    action [SetVariable("phone_feature", "home"), SetVariable("phone_menu_open", False)]
                button:
                    xysize (36, 36)
                    xalign 1.0
                    yalign 0.5
                    xoffset -12
                    background Frame(PHONE_ASSET + "close_button.png", 4, 4)
                    hover_background Frame(PHONE_ASSET + "close_button_hover.png", 4, 4)
                    action [SetVariable("phone_menu_open", False), SetVariable("phone_feature", "home")]

            # ── Navigation tabs ──
            frame:
                xysize (392, 50)
                xpos 14
                ypos 100
                background Solid("#0e1220d0")
                hbox:
                    spacing 4
                    xalign 0.5
                    yalign 0.5

                    # Messages tab
                    button:
                        xysize (75, 38)
                        if phone_feature == "messages":
                            background Frame(PHONE_ASSET + "tab_active.png", 18, 18)
                        else:
                            background Frame(PHONE_ASSET + "tab_inactive.png", 18, 18)
                            hover_background Frame(PHONE_ASSET + "tab_active.png", 18, 18)
                        action SetVariable("phone_feature", "messages")
                        hbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 4
                            text "💬" size 16
                            text "Chat" size 13 color "#dde4f0" font "DejaVuSans.ttf" yalign 0.5
                        # Badge on messages tab
                        if _total_unread > 0 and phone_feature != "messages":
                            frame:
                                xysize (20, 20)
                                xpos 55
                                ypos 2
                                background Frame(PHONE_ASSET + "notification_badge.png", 4, 4)
                                text "[_total_unread]" size 10 color "#fff" xalign 0.5 yalign 0.5 bold True

                    # Contacts tab
                    button:
                        xysize (75, 38)
                        if phone_feature == "contacts":
                            background Frame(PHONE_ASSET + "tab_active.png", 18, 18)
                        else:
                            background Frame(PHONE_ASSET + "tab_inactive.png", 18, 18)
                            hover_background Frame(PHONE_ASSET + "tab_active.png", 18, 18)
                        action SetVariable("phone_feature", "contacts")
                        hbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 4
                            text "👥" size 16
                            text "People" size 13 color "#dde4f0" font "DejaVuSans.ttf" yalign 0.5

                    # Home tab
                    button:
                        xysize (75, 38)
                        if phone_feature == "home":
                            background Frame(PHONE_ASSET + "tab_active.png", 18, 18)
                        else:
                            background Frame(PHONE_ASSET + "tab_inactive.png", 18, 18)
                            hover_background Frame(PHONE_ASSET + "tab_active.png", 18, 18)
                        action SetVariable("phone_feature", "home")
                        hbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 4
                            text "🏠" size 16
                            text "Home" size 13 color "#dde4f0" font "DejaVuSans.ttf" yalign 0.5

                    # My Stats tab
                    button:
                        xysize (75, 38)
                        if phone_feature == "stats":
                            background Frame(PHONE_ASSET + "tab_active.png", 18, 18)
                        else:
                            background Frame(PHONE_ASSET + "tab_inactive.png", 18, 18)
                            hover_background Frame(PHONE_ASSET + "tab_active.png", 18, 18)
                        action SetVariable("phone_feature", "stats")
                        hbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 4
                            text "📊" size 16
                            text "Stats" size 13 color "#dde4f0" font "DejaVuSans.ttf" yalign 0.5

                    # Inventory tab
                    button:
                        xysize (75, 38)
                        if phone_feature == "inventory":
                            background Frame(PHONE_ASSET + "tab_active.png", 18, 18)
                        else:
                            background Frame(PHONE_ASSET + "tab_inactive.png", 18, 18)
                            hover_background Frame(PHONE_ASSET + "tab_active.png", 18, 18)
                        action SetVariable("phone_feature", "inventory")
                        hbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 4
                            text "💊" size 16
                            text "Bag" size 13 color "#dde4f0" font "DejaVuSans.ttf" yalign 0.5

            # ── Content area ──
            # ──────────────────────────────────────
            #  HOME SCREEN
            # ──────────────────────────────────────
            if phone_feature == "home":
                frame:
                    xysize (374, 580)
                    xpos 23
                    ypos 158
                    background Solid("#00000000")

                    vbox:
                        spacing 20
                        xfill True
                        null height 30

                        # Big time display
                        vbox:
                            xalign 0.5
                            spacing 2
                            text "[game_time.get_time_string()]" xalign 0.5 size 52 color "#dde4f0" font "DejaVuSans-Bold.ttf"
                            text "[game_time.get_date_string()]  •  [get_day_of_week()]" xalign 0.5 size 16 color "#667799" font "DejaVuSans.ttf"

                        null height 20

                        # Quick access cards
                        hbox:
                            spacing 16
                            xalign 0.5

                            # Messages card
                            button:
                                xysize (105, 105)
                                background Frame(PHONE_ASSET + "app_messages.png", 14, 14)
                                hover_background Frame(PHONE_ASSET + "tab_active.png", 14, 14)
                                action SetVariable("phone_feature", "messages")
                                vbox:
                                    xalign 0.5
                                    yalign 0.5
                                    spacing 6
                                    text "💬" xalign 0.5 size 32
                                    text "Messages" xalign 0.5 size 12 color "#c8d8f0" font "DejaVuSans.ttf"
                                if _total_unread > 0:
                                    frame:
                                        xysize (22, 22)
                                        xpos 82
                                        ypos 2
                                        background Frame(PHONE_ASSET + "notification_badge.png", 4, 4)
                                        text "[_total_unread]" size 11 color "#fff" xalign 0.5 yalign 0.5 bold True

                            # Contacts card
                            button:
                                xysize (105, 105)
                                background Frame(PHONE_ASSET + "app_contacts.png", 14, 14)
                                hover_background Frame(PHONE_ASSET + "tab_active.png", 14, 14)
                                action SetVariable("phone_feature", "contacts")
                                vbox:
                                    xalign 0.5
                                    yalign 0.5
                                    spacing 6
                                    text "👥" xalign 0.5 size 32
                                    text "Contacts" xalign 0.5 size 12 color "#c8d8f0" font "DejaVuSans.ttf"

                            # Stats card
                            button:
                                xysize (105, 105)
                                background Frame(PHONE_ASSET + "app_stats.png", 14, 14)
                                hover_background Frame(PHONE_ASSET + "tab_active.png", 14, 14)
                                action SetVariable("phone_feature", "stats")
                                vbox:
                                    xalign 0.5
                                    yalign 0.5
                                    spacing 6
                                    text "📊" xalign 0.5 size 32
                                    text "My Stats" xalign 0.5 size 12 color "#c8d8f0" font "DejaVuSans.ttf"

                        # Second row — Inventory app
                        hbox:
                            spacing 16
                            xalign 0.5

                            # Inventory card
                            button:
                                xysize (105, 105)
                                background Frame(PHONE_ASSET + "app_contacts.png", 14, 14)
                                hover_background Frame(PHONE_ASSET + "tab_active.png", 14, 14)
                                action SetVariable("phone_feature", "inventory")
                                vbox:
                                    xalign 0.5
                                    yalign 0.5
                                    spacing 6
                                    text "💊" xalign 0.5 size 32
                                    text "Inventory" xalign 0.5 size 12 color "#c8d8f0" font "DejaVuSans.ttf"

                        null height 20

                        # Recent activity card
                        frame:
                            xsize 356
                            xalign 0.5
                            yminimum 80
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 18
                            ypadding 14

                            vbox:
                                spacing 8
                                text "📌 Recent" size 14 color "#8899bb" font "DejaVuSans-Bold.ttf"
                                add PHONE_ASSET + "divider.png" xsize 320

                                python:
                                    _recent_contact = None
                                    _recent_msg = None
                                    _max_id = -1
                                    
                                    if isinstance(contacts_met, dict):
                                        _liste_reelle = contacts_met.get(phone_owner, ["LeVieux"])
                                    else:
                                        _liste_reelle = contacts_met
                                    
                                    if phone_owner in phone_messages:
                                        for _rc in _liste_reelle:
                                            _rc_msgs = phone_messages[phone_owner].get(_rc, [])
                                            if len(_rc_msgs) > 0:
                                                _last_candidate = _rc_msgs[-1]
                                                if _last_candidate.get("id", 0) > _max_id:
                                                    _max_id = _last_candidate.get("id", 0)
                                                    _recent_contact = _rc
                                                    _recent_msg = _last_candidate

                                if _recent_msg:
                                    python:
                                        _recent_preview = _recent_msg.get("text", "")
                                        if _recent_msg.get("image", None) and not _recent_preview:
                                            _recent_preview = "📷 Photo"
                                        elif _recent_msg.get("image", None):
                                            _recent_preview = "📷 " + _recent_preview
                                        _recent_preview = _recent_preview[:50] + ("..." if len(_recent_preview) > 50 else "")
                                    hbox:
                                        spacing 10
                                        text _recent_contact.capitalize() size 14 color "#aabbdd" font "DejaVuSans-Bold.ttf" yalign 0.5
                                        text ":" size 14 color "#667799" yalign 0.5
                                        text _recent_preview size 13 color "#8899bb" font "DejaVuSans.ttf" yalign 0.5 substitute False
                                else:
                                    text "No recent messages" size 13 color "#556677" font "DejaVuSans.ttf"
            # ──────────────────────────────────────
            #  CONTACTS SCREEN (Placé ici, au bon niveau !)
            # ──────────────────────────────────────
            elif phone_feature == "contacts":
                frame:
                    xysize (374, 580)
                    xpos 23
                    ypos 158
                    background Solid("#00000000")

                    viewport:
                        xysize (374, 560)
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        vbox:
                            spacing 10
                            xfill True
                            null height 5

                            python:
                                if isinstance(contacts_met, dict):
                                    _liste_reelle = contacts_met.get(phone_owner, ["LeVieux"])
                                else:
                                    _liste_reelle = contacts_met

                            for _ct in _liste_reelle:
                                if _ct != phone_owner: 
                                    python:
                                        _stat_contact_images = {
                                            "dad": "images/dad/dad creepy.png",
                                            "brother": "images/brother/brother creepy.png",
                                            "AZrocky": "images/brother/brother creepy.png",
                                            "Lindsay": "images/lindsay/lindsay_profile.png",
                                            "unknown": "images/ui/unknown_avatar.png",
                                        }
                                        _ct_img = _stat_contact_images.get(_ct, "images/{}/{}.png".format(_ct, _ct))

                                    button:
                                        xsize 340
                                        xalign 0.5
                                        yminimum 70
                                        background Frame(PHONE_ASSET + "contact_idle.png", 8, 8)
                                        hover_background Frame(PHONE_ASSET + "contact_hover.png", 8, 8)
                                        action SetVariable("selected_contact", _ct)
                                        
                                        hbox:
                                            spacing 15
                                            yalign 0.5
                                            xoffset 12
                                            text _ct.capitalize() style "phone_contact_name"

            # ──────────────────────────────────────
            #  MESSAGES APP (Fermeture et réalignement parfaits)
            # ──────────────────────────────────────
            elif phone_feature == "messages":
                frame:
                    xysize (374, 580)
                    xpos 23
                    ypos 158
                    background Solid("#00000000")

                    viewport:
                        xysize (374, 560)
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        vbox:
                            spacing 10
                            xfill True

                            python:
                                if isinstance(contacts_met, dict):
                                    _liste_reelle = contacts_met.get(phone_owner, ["LeVieux"])
                                else:
                                    _liste_reelle = contacts_met

                            for _ct in _liste_reelle:
                                python:
                                    # SÉCURITÉ COMPLÈTE : On utilise .get() partout pour éviter les KeyError
                                    _ct_msgs = phone_messages.get(phone_owner, {}).get(_ct, [])
                                    _ct_unread = unread_messages.get(phone_owner, {}).get(_ct, 0)
                            
                                    _ct_last_msg = None
                                    _ct_preview = "Pas de message"
                                    _ct_img = None
                                    _ct_time_str = ""
                            
                                    if len(_ct_msgs) > 0:
                                        _ct_last_msg = _ct_msgs[-1]
                                        _ct_preview = _ct_last_msg.get("text", "")
                                        _ct_img = _ct_last_msg.get("image", None)
                                  
                                        if _ct_img and not _ct_preview:
                                            _ct_preview = "📷 Photo"
                                        elif _ct_img:
                                            _ct_preview = "📷 " + _ct_preview
                                      
                                        _h = _ct_last_msg.get("time_hour", 0)
                                        _m = _ct_last_msg.get("time_minute", 0)
                                        _ct_time_str = "{:02d}:{:02d}".format(_h, _m)
                                 
                                    _ct_preview = _ct_preview[:30] + ("..." if len(_ct_preview) > 30 else "")
                                    _ct_last = _ct_preview
  
                                button:
                                    xsize 350
                                    yminimum 70
                                    background Frame(PHONE_ASSET + "contact_idle.png", 8, 8)
                                    hover_background Frame(PHONE_ASSET + "contact_hover.png", 8, 8)
                                    action [SetVariable("current_message_contact", _ct), SetVariable("phone_feature", "message_chat")]
                                    
                                    # Contenu basique du bouton (Ajustable selon vos préférences)
                                    hbox:
                                        spacing 10
                                        yalign 0.5
                                        xoffset 10
                                        text _ct.capitalize() style "phone_contact_name"
                                        text _ct_last size 13 color "#8899bb" yalign 0.5

            # ──────────────────────────────────────
            #  CONTACTS / STATS LIST
            # ──────────────────────────────────────
            elif phone_feature == "contacts":
                frame:
                    xysize (374, 580)
                    xpos 23
                    ypos 158
                    background Solid("#00000000") # Fond transparent pour voir votre chat_bg

                vbox:
                    spacing 10
                    xfill True
                    null height 5

                    python:
                    # 1. Récupération sécurisée du répertoire
                        if isinstance(contacts_met, dict):
                            _liste_reelle = contacts_met.get(phone_owner, ["LeVieux"])
                        else:
                            _liste_reelle = contacts_met

                # 2. Une SEULE boucle propre pour lister les contacts
                for _ct in _liste_reelle:
                    if _ct != phone_owner: 
                        python:
                            _stat_contact_images = {
                                "dad": "images/dad/dad creepy.png",
                                    "brother": "images/brother/brother creepy.png",
                                    "AZrocky": "images/brother/brother creepy.png",
                                    "Lindsay": "images/lindsay/lindsay_profile.png",
                                    "unknown": "images/ui/unknown_avatar.png",
                            }
                            _ct_img = _stat_contact_images.get(_ct, "images/{}/{}.png".format(_ct, _ct))

                        # 3. Le bouton de la fiche contact, parfaitement dimensionné pour l'écran
                        button:
                            xsize 340 # Légèrement plus étroit pour ne pas toucher la barre de défilement
                            xalign 0.5
                            yminimum 70
                            background Frame(PHONE_ASSET + "contact_idle.png", 8, 8)
                            hover_background Frame(PHONE_ASSET + "contact_hover.png", 8, 8)
                            action SetVariable("selected_contact", _ct)
                                
                            hbox:
                                spacing 15
                                yalign 0.5
                                xoffset 12
                                text _ct.capitalize() style "phone_contact_name"

                                # Emplacement pour l'image de profil
                                fixed:
                                    xysize (44, 44)
                                    yalign 0.5
                                    $ _resolved_avatar = resolve_phone_image(_ct_img)
                                    if _resolved_avatar:
                                        add Transform(_resolved_avatar, xysize=(42, 42), fit="cover") xalign 0.5 yalign 0.5
                                    else:
                                        frame:
                                            xysize (42, 42)
                                            background Solid("#1a2040")
                                            text "?" xalign 0.5 yalign 0.5 size 20 color "#445577"

                                # Texte du nom du contact
                                vbox:
                                    yalign 0.5
                                    text _ct.capitalize() style "phone_contact_name"

                        # 4. Boucle secondaire de configuration des profils
                        for _sc in _liste_reelle:
                            if _sc != phone_owner:
                                python:
                                    # Déclaration du dictionnaire indispensable pour éviter le NameError
                                    _stat_contact_images = {
                                        "dad": "images/dad/dad creepy.png",
                                        "brother": "images/brother/brother creepy.png",
                                        "AZrocky": "images/brother/brother creepy.png",
                                        "Lindsay": "images/lindsay/lindsay_profile.png",
                                        "unknown": "images/ui/unknown_avatar.png",
                                    }
                                    # Récupération sécurisée de l'image de profil
                                    _sc_img = _stat_contact_images.get(_sc, "images/{}/{}.png".format(_sc, _sc))

                            button:
                                xsize 362
                                yminimum 72
                                xalign 0.5
                                xpadding 10
                                ypadding 10
                                background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                                hover_background Frame(PHONE_ASSET + "contact_hover.png", 16, 16)
                                action SetVariable("selected_contact", _sc)

                                hbox:
                                    spacing 12
                                    yalign 0.5

                                    fixed:
                                        xysize (48, 48)
                                        yalign 0.5
                                        add Transform(_sc_img, xysize=(46, 46), fit="cover") xalign 0.5 yalign 0.5

                                    vbox:
                                        yalign 0.5
                                        spacing 3
                                        text _sc.capitalize() style "phone_contact_name"
                                        text "View stats & info" style "phone_text_tiny"

                        null height 20

            # ──────────────────────────────────────
            #  INVENTORY SCREEN
            # ──────────────────────────────────────
            elif phone_feature == "inventory":
                viewport:
                    xysize (374, 580)
                    xpos 23
                    ypos 158
                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    vbox:
                        spacing 12
                        xfill True
                        null height 10

                        text "Your Items" xalign 0.5 size 18 color "#c8d8f0" font "DejaVuSans-Bold.ttf"
                        add PHONE_ASSET + "divider.png" xsize 340 xalign 0.5
                        null height 6

                        # ── Aphrodisiac ──
                        frame:
                            xsize 350
                            xalign 0.5
                            yminimum 72
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 14
                            ypadding 12
                            hbox:
                                spacing 14
                                yalign 0.5
                                # Icon
                                frame:
                                    xysize (48, 48)
                                    background Solid("#7a1030")
                                    yalign 0.5
                                    text "♥" xalign 0.5 yalign 0.5 size 26 color "#ff6090" font "DejaVuSans.ttf"
                                vbox:
                                    yalign 0.5
                                    spacing 4
                                    text "Aphrodisiac" size 16 color "#dde4f0" font "DejaVuSans-Bold.ttf"
                                    text "Raises someone's lust" size 12 color "#667799" font "DejaVuSans.ttf"
                                frame:
                                    xalign 1.0
                                    yalign 0.5
                                    xpadding 12
                                    ypadding 6
                                    background Solid("#1a0a1a")
                                    text "x [inv_aphrodisiac]" size 18 color "#ff6090" font "DejaVuSans-Bold.ttf" xalign 0.5 yalign 0.5

                        # ── Stress Pills ──
                        frame:
                            xsize 350
                            xalign 0.5
                            yminimum 72
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 14
                            ypadding 12
                            hbox:
                                spacing 14
                                yalign 0.5
                                # Icon
                                frame:
                                    xysize (48, 48)
                                    background Solid("#163a6b")
                                    yalign 0.5
                                    text "★" xalign 0.5 yalign 0.5 size 26 color "#80c0ff" font "DejaVuSans.ttf"
                                vbox:
                                    yalign 0.5
                                    spacing 4
                                    text "Stress Pills" size 16 color "#dde4f0" font "DejaVuSans-Bold.ttf"
                                    text "Reduces your stress" size 12 color "#667799" font "DejaVuSans.ttf"
                                frame:
                                    xalign 1.0
                                    yalign 0.5
                                    xpadding 12
                                    ypadding 6
                                    background Solid("#0a101a")
                                    text "x [inv_stress_pills]" size 18 color "#80c0ff" font "DejaVuSans-Bold.ttf" xalign 0.5 yalign 0.5

                        # ── Sleeping Pills ──
                        frame:
                            xsize 350
                            xalign 0.5
                            yminimum 72
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 14
                            ypadding 12
                            hbox:
                                spacing 14
                                yalign 0.5
                                # Icon
                                frame:
                                    xysize (48, 48)
                                    background Solid("#231550")
                                    yalign 0.5
                                    text "☽" xalign 0.5 yalign 0.5 size 26 color "#c0a0ff" font "DejaVuSans.ttf"
                                vbox:
                                    yalign 0.5
                                    spacing 4
                                    text "Sleeping Pills" size 16 color "#dde4f0" font "DejaVuSans-Bold.ttf"
                                    text "Puts someone to sleep" size 12 color "#667799" font "DejaVuSans.ttf"
                                frame:
                                    xalign 1.0
                                    yalign 0.5
                                    xpadding 12
                                    ypadding 6
                                    background Solid("#100a1a")
                                    text "x [inv_sleeping_pills]" size 18 color "#c0a0ff" font "DejaVuSans-Bold.ttf" xalign 0.5 yalign 0.5

                        # ── Testosterone Pills ──
                        frame:
                            xsize 350
                            xalign 0.5
                            yminimum 72
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 14
                            ypadding 12
                            hbox:
                                spacing 14
                                yalign 0.5
                                # Icon
                                frame:
                                    xysize (48, 48)
                                    background Solid("#5a1a00")
                                    yalign 0.5
                                    text "\u26a1" xalign 0.5 yalign 0.5 size 26 color "#ff8800" font "DejaVuSans.ttf"
                                vbox:
                                    yalign 0.5
                                    spacing 4
                                    text "Testosterone Pills" size 16 color "#dde4f0" font "DejaVuSans-Bold.ttf"
                                    text "Raises anger & aggression" size 12 color "#667799" font "DejaVuSans.ttf"
                                frame:
                                    xalign 1.0
                                    yalign 0.5
                                    xpadding 12
                                    ypadding 6
                                    background Solid("#1a0800")
                                    text "x [inv_testosterone]" size 18 color "#ff8800" font "DejaVuSans-Bold.ttf" xalign 0.5 yalign 0.5

                        null height 20

                        # Empty state
                        if inv_aphrodisiac == 0 and inv_stress_pills == 0 and inv_sleeping_pills == 0 and inv_testosterone == 0:
                            text "Your bag is empty.\nVisit the pharmacy to buy items." xalign 0.5 size 13 color "#445566" font "DejaVuSans.ttf" text_align 0.5

                        null height 20

            # ──────────────────────────────────────
            #  MY STATS SCREEN
            # ──────────────────────────────────────
            elif phone_feature == "stats":
                viewport:
                    xysize (374, 580)
                    xpos 23
                    ypos 158
                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    vbox:
                        spacing 12
                        xfill True
                        null height 10

                        text "My Stats" xalign 0.5 size 18 color "#c8d8f0" font "DejaVuSans-Bold.ttf"
                        add PHONE_ASSET + "divider.png" xsize 340 xalign 0.5
                        null height 6

                        # ── Money ──
                        frame:
                            xsize 350
                            xalign 0.5
                            yminimum 62
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 14
                            ypadding 12
                            hbox:
                                spacing 14
                                yalign 0.5
                                frame:
                                    xysize (48, 48)
                                    background Solid("#2a1a00")
                                    yalign 0.5
                                    text "💰" xalign 0.5 yalign 0.5 size 26 font "DejaVuSans.ttf"
                                vbox:
                                    yalign 0.5
                                    spacing 4
                                    text "Money" size 16 color "#dde4f0" font "DejaVuSans-Bold.ttf"
                                    text "Your current funds" size 12 color "#667799" font "DejaVuSans.ttf"
                                frame:
                                    xalign 1.0
                                    yalign 0.5
                                    xpadding 12
                                    ypadding 6
                                    background Solid("#1a1000")
                                    text "[madd_money]" size 18 color "#FFD700" font "DejaVuSans-Bold.ttf" xalign 0.5 yalign 0.5

                        # ── Grades ──
                        frame:
                            xsize 350
                            xalign 0.5
                            yminimum 62
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 14
                            ypadding 12
                            hbox:
                                spacing 14
                                yalign 0.5
                                frame:
                                    xysize (48, 48)
                                    background Solid("#1a0a3a")
                                    yalign 0.5
                                    text "🎓" xalign 0.5 yalign 0.5 size 26 font "DejaVuSans.ttf"
                                vbox:
                                    yalign 0.5
                                    spacing 4
                                    text "Grades" size 16 color "#dde4f0" font "DejaVuSans-Bold.ttf"
                                    text "Academic performance" size 12 color "#667799" font "DejaVuSans.ttf"
                                frame:
                                    xalign 1.0
                                    yalign 0.5
                                    xpadding 12
                                    ypadding 6
                                    background Solid("#0a0820")
                                    text "[grades]" size 18 color "#6C5CE7" font "DejaVuSans-Bold.ttf" xalign 0.5 yalign 0.5

                        # ── Secret Identity ──
                        frame:
                            xsize 350
                            xalign 0.5
                            yminimum 62
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 14
                            ypadding 12
                            hbox:
                                spacing 14
                                yalign 0.5
                                frame:
                                    xysize (48, 48)
                                    background Solid("#3a0a0a")
                                    yalign 0.5
                                    text "🆔" xalign 0.5 yalign 0.5 size 26 font "DejaVuSans.ttf"
                                vbox:
                                    yalign 0.5
                                    spacing 4
                                    text "Secret Identity" size 16 color "#dde4f0" font "DejaVuSans-Bold.ttf"
                                    text "How hidden you remain" size 12 color "#667799" font "DejaVuSans.ttf"
                                frame:
                                    xalign 1.0
                                    yalign 0.5
                                    xpadding 12
                                    ypadding 6
                                    background Solid("#1a0000")
                                    text "{:.1f}%".format(secret_identity) size 18 color "#E74C3C" font "DejaVuSans-Bold.ttf" xalign 0.5 yalign 0.5
                        
                        # ── Corruption ──
                        frame:
                            xsize 350
                            xalign 0.5
                            yminimum 62
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 14
                            ypadding 12
                            hbox:
                                spacing 14
                                yalign 0.5
                                frame:
                                    xysize (48, 48)
                                    background Solid("#2a0000")
                                    yalign 0.5
                                    text "😈" xalign 0.5 yalign 0.5 size 26 font "DejaVuSans.ttf"
                                vbox:
                                    yalign 0.5
                                    spacing 4
                                    text "Corruption" size 16 color "#dde4f0" font "DejaVuSans-Bold.ttf"
                                    text "How far you've fallen" size 12 color "#667799" font "DejaVuSans.ttf"
                                frame:
                                    xalign 1.0
                                    yalign 0.5
                                    xpadding 12
                                    ypadding 6
                                    background Solid("#150000")
                                    text "[corruption]" size 18 color "#C0392B" font "DejaVuSans-Bold.ttf" xalign 0.5 yalign 0.5

                        # ── Lust ──
                        frame:
                            xsize 350
                            xalign 0.5
                            yminimum 62
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 14
                            ypadding 12
                            hbox:
                                spacing 14
                                yalign 0.5
                                frame:
                                    xysize (48, 48)
                                    background Solid("#2a1000")
                                    yalign 0.5
                                    text "🔥" xalign 0.5 yalign 0.5 size 26 font "DejaVuSans.ttf"
                                vbox:
                                    yalign 0.5
                                    spacing 4
                                    text "Lust" size 16 color "#dde4f0" font "DejaVuSans-Bold.ttf"
                                    text "Tes hot ou pas ?" size 12 color "#667799" font "DejaVuSans.ttf"
                                frame:
                                    xalign 1.0
                                    yalign 0.5
                                    xpadding 12
                                    ypadding 6
                                    background Solid("#1a0800")
                                    text "[_sel_lust:.0f]" size 18 color "#F39C12" font "DejaVuSans-Bold.ttf" xalign 0.5 yalign 0.5


                        # ── Informations ──
                        frame:
                            xsize 350
                            xalign 0.5
                            yminimum 62
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 14
                            ypadding 12
                            hbox:
                                spacing 14
                                yalign 0.5
                                frame:
                                    xysize (48, 48)
                                    background Solid("#2a1000")
                                    yalign 0.5
                                    text "🔥" xalign 0.5 yalign 0.5 size 26 font "DejaVuSans.ttf"
                                vbox:
                                    yalign 0.5
                                    spacing 4
                                    text "Informations" size 16 color "#dde4f0" font "DejaVuSans-Bold.ttf"
                                    text "Infos prise à la tv" size 12 color "#667799" font "DejaVuSans.ttf"
                                frame:
                                    xalign 1.0
                                    yalign 0.5
                                    xpadding 12
                                    ypadding 6
                                    background Solid("#1a0800")
                                    text "[checkinfos]" size 18 color "#F39C12" font "DejaVuSans-Bold.ttf" xalign 0.5 yalign 0.5

                        # ── Rocky ──
                        frame:
                            xsize 350
                            xalign 0.5
                            yminimum 62
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 14
                            ypadding 12
                            hbox:
                                spacing 14
                                yalign 0.5
                                frame:
                                    xysize (48, 48)
                                    background Solid("#2a1000")
                                    yalign 0.5
                                    text "🔥" xalign 0.5 yalign 0.5 size 26 font "DejaVuSans.ttf"
                                vbox:
                                    yalign 0.5
                                    spacing 4
                                    text "Rocky Tier" size 16 color "#dde4f0" font "DejaVuSans-Bold.ttf"
                                    text "Tier" size 12 color "#667799" font "DejaVuSans.ttf"
                                frame:
                                    xalign 1.0
                                    yalign 0.5
                                    xpadding 12
                                    ypadding 6
                                    background Solid("#1a0800")
                                    text "[convrocky]" size 18 color "#F39C12" font "DejaVuSans-Bold.ttf" xalign 0.5 yalign 0.5

                        null height 20


    # ════════════════════════════════════════════
    #  CONTACT STATS DETAIL VIEW
    # ════════════════════════════════════════════
   

    elif selected_contact:
        modal True

        python:
            if selected_contact == "Lindsay":
            
                _sel_corruption = _sel_data.get("corruption", 0)
            _sel_name = selected_contact.capitalize()
            _sel_data = character_relations.get(selected_contact, {})
            _sel_intimacy = _sel_data.get("intimacy", 0)
            _sel_lust = _sel_data.get("lust", 0)
            _sel_anger = _sel_data.get("anger", 0)
            _sel_dominance = _sel_data.get("dominance", 0)
            _sel_friend = _sel_data.get("friend", 0)
            _sel_identity = _sel_data.get("identity", 100)
                       

            # Sex-related stat counts
            _sel_kissed = _sel_data.get("kissed", 0)
            _sel_oral_sex = _sel_data.get("oral_sex", 0)
            _sel_vaginal_sex = _sel_data.get("vaginal_sex", 0)
            _sel_anal_sex = _sel_data.get("anal_sex", 0)
            _sel_touched = _sel_data.get("touched_madd", 0)
            _sel_groped = _sel_data.get("groped_madd", 0)
            _sel_undressed = _sel_data.get("undressed_madd", 0)
            _sel_vaginal_creampie = _sel_data.get("vaginal_creampie", 0)
            _sel_anal_creampie = _sel_data.get("anal_creampie", 0)
            _sel_pissed_on = _sel_data.get("pissed_on_her", 0)
            _sel_pissed_mouth = _sel_data.get("pissed_in_mouth", 0)
            _sel_came_on = _sel_data.get("came_on_madd", 0)
            

            _sel_img_map = {
                "AZrocky": "images/brother/brother creepy.png",
                "Dave": "images/brother/brother creepy.png",
                "Lindsay": "images/brother/brother creepy.png",
                "Mzelle": "images/brother/brother creepy.png",
            }
            _sel_avatar = _sel_img_map.get(selected_contact, "images/{}/{}.png".format(selected_contact, selected_contact))

        # Dim backdrop
        button:
            xysize (1920, 1080)
            background Solid("#00000088")
            action NullAction()
            at phone_dim_in

        fixed:
            xysize (420, 780)
            xpos 40
            ypos 30
            at phone_slide_in

            # Background
            add PHONE_ASSET + "phone_bg.png" xysize (392, 752) xpos 14 ypos 14

            # Phone frame overlay
            add PHONE_ASSET + "phone_frame.png" xysize (420, 780)

            # ── Status bar ──
            frame:
                xysize (392, 28)
                xpos 14
                ypos 14
                background Solid("#0c0e16e8")
                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 8
                    text "[game_time.get_time_string()]" size 11 color "#8899bb" font "DejaVuSans.ttf"
                    text "•" size 11 color "#445577"
                    text "📶" size 10
                    text "🔋" size 10

            # ── Header ──
            frame:
                xysize (392, 56)
                xpos 14
                ypos 42
                background Frame(PHONE_ASSET + "header_bg.png", 4, 4)
                hbox:
                    spacing 10
                    xoffset 10
                    yalign 0.5

                    button:
                        xysize (36, 36)
                        yalign 0.5
                        background Frame(PHONE_ASSET + "back_button.png", 4, 4)
                        hover_background Frame(PHONE_ASSET + "back_button_hover.png", 4, 4)
                        action [SetVariable("selected_contact", None), SetVariable("phone_stat_view", "general")]

                    text _sel_name style "phone_header_text"

                button:
                    xysize (36, 36)
                    xalign 1.0
                    yalign 0.5
                    xoffset -12
                    background Frame(PHONE_ASSET + "close_button.png", 4, 4)
                    hover_background Frame(PHONE_ASSET + "close_button_hover.png", 4, 4)
                    action [SetVariable("selected_contact", None), SetVariable("phone_menu_open", False), SetVariable("phone_feature", "home"), SetVariable("phone_stat_view", "general")]

            # ── Stats content ──
            viewport:
                xysize (374, 590)
                xpos 23
                ypos 105
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    spacing 14
                    xfill True
                    null height 10

                    # Large avatar
                    fixed:
                        xysize (374, 110)
                        xalign 0.5
                        add Transform(_sel_avatar, xysize=(100, 100), fit="cover") xalign 0.5 yalign 0.5

                    text _sel_name xalign 0.5 size 24 color "#dde4f0" font "DejaVuSans-Bold.ttf"

                    add PHONE_ASSET + "divider.png" xalign 0.5

                    # ── Stat view tabs ──
                    hbox:
                        spacing 8
                        xalign 0.5

                        button:
                            xysize (164, 36)
                            if phone_stat_view == "general":
                                background Frame(PHONE_ASSET + "tab_active.png", 18, 18)
                            else:
                                background Frame(PHONE_ASSET + "tab_inactive.png", 18, 18)
                                hover_background Frame(PHONE_ASSET + "tab_active.png", 18, 18)
                            action SetVariable("phone_stat_view", "general")
                            hbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 4
                                text "📊" size 15
                                text "General" size 13 color "#dde4f0" font "DejaVuSans.ttf" yalign 0.5

                        button:
                            xysize (164, 36)
                            if phone_stat_view == "sex":
                                background Frame(PHONE_ASSET + "tab_active.png", 18, 18)
                            else:
                                background Frame(PHONE_ASSET + "tab_inactive.png", 18, 18)
                                hover_background Frame(PHONE_ASSET + "tab_active.png", 18, 18)
                            action SetVariable("phone_stat_view", "sex")
                            hbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 4
                                text "🔞" size 15
                                text "Sex Stats" size 13 color "#dde4f0" font "DejaVuSans.ttf" yalign 0.5

                    null height 4

                    # ══════════════════════════════════════
                    #  GENERAL STATS (relationship bars)
                    # ══════════════════════════════════════
                    if phone_stat_view == "general":
                        # Intimacy
                        frame:
                            xsize 356
                            xalign 0.5
                            yminimum 54
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 14
                            ypadding 10
                            hbox:
                                yalign 0.5
                                spacing 10
                                text "❤️" size 22
                                vbox:
                                    spacing 3
                                    text "Intimacy" style "phone_stat_label"
                                    hbox:
                                        spacing 10
                                        bar:
                                            xysize (200, 10)
                                            range 100
                                            value _sel_intimacy
                                            left_bar Frame(PHONE_ASSET + "stat_bar_intimacy_fill.png", 6, 6)
                                            right_bar Frame(PHONE_ASSET + "stat_bar_intimacy_bg.png", 6, 6)
                                            thumb None
                                        text "[_sel_intimacy:.0f]" style "phone_stat_value" color "#ff5a5a"

                        # Lust
                        frame:
                            xsize 356
                            xalign 0.5
                            yminimum 54
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 14
                            ypadding 10
                            hbox:
                                yalign 0.5
                                spacing 10
                                text "🔥" size 22
                                vbox:
                                    spacing 3
                                    text "Lust" style "phone_stat_label"
                                    hbox:
                                        spacing 10
                                        bar:
                                            xysize (200, 10)
                                            range 100
                                            value _sel_lust
                                            left_bar Frame(PHONE_ASSET + "stat_bar_lust_fill.png", 6, 6)
                                            right_bar Frame(PHONE_ASSET + "stat_bar_lust_bg.png", 6, 6)
                                            thumb None
                                        text "[_sel_lust:.0f]" style "phone_stat_value" color "#ff8c32"

                        # Anger
                        frame:
                            xsize 356
                            xalign 0.5
                            yminimum 54
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 14
                            ypadding 10
                            hbox:
                                yalign 0.5
                                spacing 10
                                text "😠" size 22
                                vbox:
                                    spacing 3
                                    text "Anger" style "phone_stat_label"
                                    hbox:
                                        spacing 10
                                        bar:
                                            xysize (200, 10)
                                            range 100
                                            value _sel_anger
                                            left_bar Frame(PHONE_ASSET + "stat_bar_anger_fill.png", 6, 6)
                                            right_bar Frame(PHONE_ASSET + "stat_bar_anger_bg.png", 6, 6)
                                            thumb None
                                        text "[_sel_anger:.0f]" style "phone_stat_value" color "#dd2828"

                        # Dominance
                        frame:
                            xsize 356
                            xalign 0.5
                            yminimum 54
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 14
                            ypadding 10
                            hbox:
                                yalign 0.5
                                spacing 10
                                text "👑" size 22
                                vbox:
                                    spacing 3
                                    text "Dominance" style "phone_stat_label"
                                    hbox:
                                        spacing 10
                                        bar:
                                            xysize (200, 10)
                                            range 100
                                            value _sel_dominance
                                            left_bar Frame(PHONE_ASSET + "stat_bar_dominance_fill.png", 6, 6)
                                            right_bar Frame(PHONE_ASSET + "stat_bar_dominance_bg.png", 6, 6)
                                            thumb None
                                        text "[_sel_dominance:.0f]" style "phone_stat_value" color "#888ca0"

                        # Friendship
                        frame:
                            xsize 356
                            xalign 0.5
                            yminimum 54
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 14
                            ypadding 10
                            hbox:
                                yalign 0.5
                                spacing 10
                                text "🤝" size 22
                                vbox:
                                    spacing 3
                                    text "Friendship" style "phone_stat_label"
                                    hbox:
                                        spacing 10
                                        bar:
                                            xysize (200, 10)
                                            range 100
                                            value _sel_friend
                                            left_bar Frame(PHONE_ASSET + "stat_bar_friend_fill.png", 6, 6)
                                            right_bar Frame(PHONE_ASSET + "stat_bar_friend_bg.png", 6, 6)
                                            thumb None
                                        text "[_sel_friend:.0f]" style "phone_stat_value" color "#64b4f0"

                        # Identity
                        frame:
                            xsize 356
                            xalign 0.5
                            yminimum 54
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 14
                            ypadding 10
                            hbox:
                                yalign 0.5
                                spacing 10
                                text "🧠" size 22
                                vbox:
                                    spacing 3
                                    text "Identity" style "phone_stat_label"
                                    hbox:
                                        spacing 10
                                        bar:
                                            xysize (200, 10)
                                            range 100
                                            value _sel_identity
                                            left_bar Frame(PHONE_ASSET + "stat_bar_identity_fill.png", 6, 6)
                                            right_bar Frame(PHONE_ASSET + "stat_bar_identity_bg.png", 6, 6)
                                            thumb None
                                        text "[_sel_identity:.0f]" style "phone_stat_value" color "#dcbe3c"

                          # Corruption Lindsay
                    if selected_contact == "Lindsay":
                        frame:
                            xsize 356
                            xalign 0.5
                            yminimum 54
                            background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                            xpadding 14
                            ypadding 10
                            hbox:
                                yalign 0.5
                                spacing 10
                                text "😈" size 22
                                
                                vbox:
                                    spacing 4
                                    # 1. On récupère proprement la valeur (0 par défaut si non définie)
                                    $ linds_corr = getattr(persistent, 'linds_corruption', 0)
                                hbox:
                                        spacing 10
                                        # 2. On affiche directement la variable locale de l'écran
                                        text "Corruption: [linds_corr]/100" size 14 color "#ffaa66" font "DejaVuSans.ttf"
                                    
                                bar:
                                    value StaticValue(linds_corr, 100)
                                    xsize 250
                                    ysize 8
                                    left_bar Solid("#ffaa66")
                                    right_bar Solid("#222b45")
                                    
                                text "[linds_corr]" style "phone_stat_value" color "#888ca0"

                    # ══════════════════════════════════════
                    #  SEX STATS (count-based cards)
                    # ══════════════════════════════════════
                    if phone_stat_view == "sex":

                        # Section header
                        text "Sexual Encounters" xalign 0.5 size 14 color "#667799" font "DejaVuSans.ttf"
                        null height 2

                        # Row 1: Kissed / Oral Sex
                        hbox:
                            spacing 8
                            xalign 0.5
                            frame:
                                xysize (172, 58)
                                background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                                xpadding 10
                                ypadding 8
                                hbox:
                                    yalign 0.5
                                    spacing 8
                                    text "💋" size 24
                                    vbox:
                                        spacing 1
                                        text "Kissed" size 12 color "#aabbdd" font "DejaVuSans.ttf"
                                        text "[_sel_kissed]" size 18 color "#ff6b9d" font "DejaVuSans-Bold.ttf"
                            frame:
                                xysize (172, 58)
                                background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                                xpadding 10
                                ypadding 8
                                hbox:
                                    yalign 0.5
                                    spacing 8
                                    text "👄" size 24
                                    vbox:
                                        spacing 1
                                        text "Oral Sex" size 12 color "#aabbdd" font "DejaVuSans.ttf"
                                        text "[_sel_oral_sex]" size 18 color "#ff5a82" font "DejaVuSans-Bold.ttf"

                        # Row 2: Vaginal Sex / Anal Sex
                        hbox:
                            spacing 8
                            xalign 0.5
                            frame:
                                xysize (172, 58)
                                background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                                xpadding 10
                                ypadding 8
                                hbox:
                                    yalign 0.5
                                    spacing 8
                                    text "🌸" size 24
                                    vbox:
                                        spacing 1
                                        text "Vaginal Sex" size 12 color "#aabbdd" font "DejaVuSans.ttf"
                                        text "[_sel_vaginal_sex]" size 18 color "#e84590" font "DejaVuSans-Bold.ttf"
                            frame:
                                xysize (172, 58)
                                background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                                xpadding 10
                                ypadding 8
                                hbox:
                                    yalign 0.5
                                    spacing 8
                                    text "🍑" size 24
                                    vbox:
                                        spacing 1
                                        text "Anal Sex" size 12 color "#aabbdd" font "DejaVuSans.ttf"
                                        text "[_sel_anal_sex]" size 18 color "#e06040" font "DejaVuSans-Bold.ttf"

                        # Row 3: Touched / Groped
                        hbox:
                            spacing 8
                            xalign 0.5
                            frame:
                                xysize (172, 58)
                                background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                                xpadding 10
                                ypadding 8
                                hbox:
                                    yalign 0.5
                                    spacing 8
                                    text "👋" size 24
                                    vbox:
                                        spacing 1
                                        text "Touched" size 12 color "#aabbdd" font "DejaVuSans.ttf"
                                        text "[_sel_touched]" size 18 color "#c088dd" font "DejaVuSans-Bold.ttf"
                            frame:
                                xysize (172, 58)
                                background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                                xpadding 10
                                ypadding 8
                                hbox:
                                    yalign 0.5
                                    spacing 8
                                    text "✊" size 24
                                    vbox:
                                        spacing 1
                                        text "Groped" size 12 color "#aabbdd" font "DejaVuSans.ttf"
                                        text "[_sel_groped]" size 18 color "#b070cc" font "DejaVuSans-Bold.ttf"

                        # Row 4: Undressed / V. Creampie
                        hbox:
                            spacing 8
                            xalign 0.5
                            frame:
                                xysize (172, 58)
                                background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                                xpadding 10
                                ypadding 8
                                hbox:
                                    yalign 0.5
                                    spacing 8
                                    text "👙" size 24
                                    vbox:
                                        spacing 1
                                        text "Undressed" size 12 color "#aabbdd" font "DejaVuSans.ttf"
                                        text "[_sel_undressed]" size 18 color "#dd7788" font "DejaVuSans-Bold.ttf"
                            frame:
                                xysize (172, 58)
                                background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                                xpadding 10
                                ypadding 8
                                hbox:
                                    yalign 0.5
                                    spacing 8
                                    text "💧" size 24
                                    vbox:
                                        spacing 1
                                        text "V. Creampie" size 12 color "#aabbdd" font "DejaVuSans.ttf"
                                        text "[_sel_vaginal_creampie]" size 18 color "#ff8866" font "DejaVuSans-Bold.ttf"

                        # Row 5: A. Creampie / Pissed On
                        hbox:
                            spacing 8
                            xalign 0.5
                            frame:
                                xysize (172, 58)
                                background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                                xpadding 10
                                ypadding 8
                                hbox:
                                    yalign 0.5
                                    spacing 8
                                    text "💦" size 24
                                    vbox:
                                        spacing 1
                                        text "A. Creampie" size 12 color "#aabbdd" font "DejaVuSans.ttf"
                                        text "[_sel_anal_creampie]" size 18 color "#ff6644" font "DejaVuSans-Bold.ttf"
                            frame:
                                xysize (172, 58)
                                background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                                xpadding 10
                                ypadding 8
                                hbox:
                                    yalign 0.5
                                    spacing 8
                                    text "🚿" size 24
                                    vbox:
                                        spacing 1
                                        text "Pissed On" size 12 color "#aabbdd" font "DejaVuSans.ttf"
                                        text "[_sel_pissed_on]" size 18 color "#ccaa44" font "DejaVuSans-Bold.ttf"

                        # Row 6: Pissed In Mouth / Came On
                        hbox:
                            spacing 8
                            xalign 0.5
                            frame:
                                xysize (172, 58)
                                background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                                xpadding 10
                                ypadding 8
                                hbox:
                                    yalign 0.5
                                    spacing 8
                                    text "😮" size 24
                                    vbox:
                                        spacing 1
                                        text "Pissed Mouth" size 12 color "#aabbdd" font "DejaVuSans.ttf"
                                        text "[_sel_pissed_mouth]" size 18 color "#bbaa33" font "DejaVuSans-Bold.ttf"
                            frame:
                                xysize (172, 58)
                                background Frame(PHONE_ASSET + "contact_idle.png", 16, 16)
                                xpadding 10
                                ypadding 8
                                hbox:
                                    yalign 0.5
                                    spacing 8
                                    text "💦" size 24
                                    vbox:
                                        spacing 1
                                        text "Came On" size 12 color "#aabbdd" font "DejaVuSans.ttf"
                                        text "[_sel_came_on]" size 18 color "#88ccff" font "DejaVuSans-Bold.ttf"

                    null height 6
                    add PHONE_ASSET + "divider.png" xalign 0.5
                    null height 6

                    # Message shortcut
                    button:
                        xsize 280
                        yminimum 44
                        xalign 0.5
                        xpadding 16
                        ypadding 10
                        background Frame(PHONE_ASSET + "reply_button.png", 14, 14)
                        hover_background Frame(PHONE_ASSET + "reply_button_hover.png", 14, 14)
                        action [SetVariable("current_message_contact", selected_contact), SetVariable("selected_contact", None), SetVariable("phone_feature", "message_chat"), SetVariable("phone_stat_view", "general")]
                        hbox:
                            xalign 0.5
                            spacing 8
                            text "💬" size 18 yalign 0.5
                            text "Send Message" size 15 color "#c8d8f0" font "DejaVuSans.ttf" yalign 0.5

                    null height 20


# ── Register overlays ────────────────────────────────────────
init python:
    config.overlay_screens.append("time_display")
    config.overlay_screens.append("phone_button")
    config.overlay_screens.append("phone_interface")

# ── Helper Functions ─────────────────────────────────────────
init python:
    def resolve_phone_image(img):
        """Resolve an image reference to a displayable.
        
        Accepts:
            - A file path string:   "images/dad/dad creepy.png"
            - A declared image name: "shower naked", "madd r1", "family new"
            - An existing displayable object (Transform, etc.)
        
        Returns a Ren'Py displayable that can be used with `add`.
        """
        if img is None:
            return None
        # Already a displayable object (Transform, Composite, etc.)
        if not isinstance(img, str):
            return img
        # Check if it's a registered image name (e.g. "shower naked")
        if renpy.has_image(img):
            return renpy.displayable(img)
        # Also try with spaces replaced by underscores and vice versa
        alt = img.replace("_", " ")
        if alt != img and renpy.has_image(alt):
            return renpy.displayable(alt)
        alt2 = img.replace(" ", "_")
        if alt2 != img and renpy.has_image(alt2):
            return renpy.displayable(alt2)
        # Assume it's a file path
        return img

    def send_message(contact, message_text, image=None, reply_to=None):
        """Send a message to a contact (from the player).
        
        S'adapte automatiquement sur le téléphone de l'utilisateur actif (phone_owner).
        """
        store.phone_msg_id_counter += 1
        msg = {
            "id": store.phone_msg_id_counter,
            "sender": "player",
            "text": message_text.strip() if message_text else "",
            "timestamp": days_passed,
            "time_hour": game_time.hour,
            "time_minute": game_time.minute,
            "time_day": game_time.day,
            "time_month": game_time.month,
            "time_year": game_time.year,
        }
        if image:
            msg["image"] = image
        if reply_to is not None:
            msg["reply_to"] = reply_to
            
        if msg["text"] or image:
            # SÉCURITÉ CENTRALISÉE : On injecte dans le répertoire du BON propriétaire actif
            if phone_owner in phone_messages and contact in phone_messages[phone_owner]:
                phone_messages[phone_owner][contact].append(msg)
                
                # Marquer le message d'origine comme répondu
                if reply_to is not None and contact in unreplied_messages:
                    if reply_to in unreplied_messages[contact]:
                        unreplied_messages[contact].remove(reply_to)
                        
        renpy.restart_interaction()

    def receive_message(target, contact, message_text, image=None):
        """Receive a message from a contact (NPC sends to player).
        
        Args:
            contact: String key like "dad", "brother", etc.
            message_text: The text content (can be "" if sending only an image).
            image: File path ("images/dad/dad creepy.png") OR
                declared image name ("shower naked", "madd r1").
        
        Examples:
            # Text only
            $ receive_message("dad", "Hello daughter")
            
            # Image only (file path)
            $ receive_message("dad", "", image="images/dad/dad creepy.png")
            
            # Image only (declared image name)
            $ receive_message("dad", "", image="shower naked")
            $ receive_message("brother", "", image="madd r1")
            
            # Text + declared image
            $ receive_message("brother", "Remember this?", image="family new")
        """
        store.phone_msg_id_counter += 1
        msg = {
            "id": store.phone_msg_id_counter,
            "sender": contact,
            "text": message_text.strip() if message_text else "",
            "timestamp": days_passed,
            "time_hour": game_time.hour,
            "time_minute": game_time.minute,
            "time_day": game_time.day,
            "time_month": game_time.month,
            "time_year": game_time.year,
        }
        if image:
            msg["image"] = image
            
        if msg["text"] or image:
            # On injecte le message dans le dictionnaire du bon propriétaire (target)
            if target in phone_messages and contact in phone_messages[target]:
                phone_messages[target][contact].append(msg)
                unread_messages[target][contact] += 1
                
            # Tracking des messages sans réponse
                if contact not in unreplied_messages:
                    unreplied_messages[contact] = []
                unreplied_messages[contact].append(store.phone_msg_id_counter)
                
        renpy.restart_interaction()

    def mark_as_read(contact):
        """Mark all messages from a contact as read based on active phone owner.
        
        Conserves the anonymous bank transfer event for the unknown contact.
        """
        # 1. Remise à zéro sécurisée du compteur du BON propriétaire de téléphone
        if phone_owner in unread_messages and contact in unread_messages[phone_owner]:
            unread_messages[phone_owner][contact] = 0
            
        # 2. Conservation de votre événement de virement anonyme original
        if contact == "unknown" and not store.brother_anonymous_transfer_claimed:
            store.madd_money += 3000
            store.brother_anonymous_transfer_claimed = True
            
        renpy.restart_interaction()

    def get_unread_count():
        """Get total unread message count"""
        return sum(unread_messages.values())

    def get_contact_image(contact):
        """Get the image path for a contact"""
        contact_lower = contact.lower()
        return "images/{}/{} creepy.png".format(contact_lower, contact_lower)

    def get_message_display(contact):
        """Get formatted messages for display"""
        return phone_messages.get(contact, [])

    def set_message_replies(contact, replies_list, reply_to=None):
        """Set reply options for a contact, optionally tied to a specific message.
        
        Each reply is a dict with:
            - "text": Display text for the reply button
            - "action": A Ren'Py action or list of actions to execute
        
        If reply_to is None (default / backward-compatible), the replies are
        automatically tied to the most recent received message from that contact.
        
        If reply_to is an integer message ID, the replies target that exact message.
        
        Multiple calls accumulate — you can have reply options on several messages
        at once. The player taps a message's "Reply" button to select it, then
        picks from the options shown at the bottom.
        
        Examples:
            # Auto-target the last received message (backward compatible)
            $ set_message_replies("dad", [
                {"text": "Yes dad", "action": Function(send_message, "dad", "Yes dad")},
                {"text": "No way!", "action": Function(send_message, "dad", "No way!")},
            ])
            
            # Target a specific message by ID
            $ set_message_replies("dad", [
                {"text": "Got it", "action": Function(send_message, "dad", "Got it")},
            ], reply_to=5)
        """
        if reply_to is None:
            # Auto-target the last received message from this contact
            if phone_owner in phone_messages:
                msgs = phone_messages[phone_owner].get(contact, [])
            else:
                msgs = []
            for m in reversed(msgs):
                if m.get("sender") != "player" and "id" in m:
                    reply_to = m["id"]
                    break
        # Ensure dict structure exists
        if contact not in message_replies or not isinstance(message_replies.get(contact), dict):
            message_replies[contact] = {}
        if reply_to is not None:
            message_replies[contact][reply_to] = replies_list
            # Auto-select as reply target
            phone_reply_target[contact] = reply_to
        else:
            # Fallback: store under key 0 (no specific target)
            message_replies[contact][0] = replies_list
            phone_reply_target[contact] = 0

    def clear_message_replies(contact, msg_id=None):
        """Clear reply options for a contact.
        
        If msg_id is given, only clears replies for that specific message.
        If msg_id is None, clears ALL replies for the contact.
        """
        if msg_id is not None:
            if contact in message_replies and isinstance(message_replies[contact], dict):
                if msg_id in message_replies[contact]:
                    del message_replies[contact][msg_id]
            # Mark this specific message as replied in unreplied tracking
            if contact in unreplied_messages and msg_id in unreplied_messages[contact]:
                unreplied_messages[contact].remove(msg_id)
        else:
            message_replies[contact] = {}
        # Update reply target — pick next available or clear
        remaining = message_replies.get(contact, {})
        if isinstance(remaining, dict) and remaining:
            phone_reply_target[contact] = sorted(remaining.keys())[-1]
        else:
            if contact in phone_reply_target:
                phone_reply_target[contact] = None

    def tag_last_sent_as_reply(contact, reply_to_id):
        """Associe le dernier message envoyé par le joueur à l'ID du message auquel il répond.
        
        Cherche automatiquement dans la boîte du propriétaire de téléphone actif.
        """
        if phone_owner in phone_messages:
            _messages = phone_messages[phone_owner].get(contact, [])
        else:
            _messages = []
            
        # On parcourt à l'envers pour trouver le VRAI dernier dictionnaire valide envoyé par le joueur
        for m in reversed(_messages):
            if isinstance(m, dict) and m.get("sender") == "player":
                m["reply_to"] = reply_to_id
                break
                
        renpy.restart_interaction()

    def get_unreplied_messages(contact):
        """Get list of unreplied message IDs for a contact.
        
        Returns a list of message IDs (ints) that the player hasn't replied to.
        
        Examples:
            $ unreplied = get_unreplied_messages("dad")
            if len(unreplied) > 0:
                "Dad is still waiting for your reply..."
        """
        return list(unreplied_messages.get(contact, []))

    def get_unreplied_message_texts(contact):
        """Get the actual text content of unreplied messages for a contact.
        
        Returns a list of dicts: [{"id": int, "text": str, "timestamp": int, "time": "HH:MM"}, ...]
        Useful for checking WHAT was said and building contextual responses.
        
        Examples:
            $ unreplied = get_unreplied_message_texts("dad")
            # unreplied[0]["text"] -> "Come downstairs now."
            # unreplied[0]["time"] -> "14:30"
        """
        ids = unreplied_messages.get(contact, [])
        if not ids:
            return []
        msgs = phone_messages.get(contact, [])
        result = []
        for m in msgs:
            if m.get("id") in ids:
                result.append({
                    "id": m["id"],
                    "text": m.get("text", ""),
                    "timestamp": m.get("timestamp", 0),
                    "time": "{:02d}:{:02d}".format(m.get("time_hour", 0), m.get("time_minute", 0)),
                })
        return result

    def get_total_unreplied(contact=None):
        """Get count of unreplied messages.
        
        If contact is given, returns count for that contact.
        If contact is None, returns total across ALL contacts.
        
        Examples:
            $ total = get_total_unreplied()           # all contacts
            $ dad_unreplied = get_total_unreplied("dad")  # just dad
        """
        if contact:
            return len(unreplied_messages.get(contact, []))
        return sum(len(v) for v in unreplied_messages.values())

    def has_unreplied(contact):
        """Check if a contact has any unreplied messages.
        
        Example:
            if has_unreplied("dad"):
                "Dad sent messages you never answered..."
        """
        return len(unreplied_messages.get(contact, [])) > 0

    def format_msg_time(msg):
        """Format a message's timestamp for display.
        Returns "HH:MM" or "" if no time data."""
        h = msg.get("time_hour", None)
        m = msg.get("time_minute", None)
        if h is not None and m is not None:
            return "{:02d}:{:02d}".format(h, m)
        return ""

    def format_msg_date(msg):
        """Format a message's date for display.
        Returns e.g. 'Day 1', 'Day 2', etc. based on the timestamp (days_passed),
        or 'DD/MM' if full date data is present."""
        d = msg.get("time_day", None)
        mo = msg.get("time_month", None)
        if d is not None and mo is not None:
            month_names = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            mn = month_names[mo] if 1 <= mo <= 12 else str(mo)
            return "{} {}".format(mn, d)
        ts = msg.get("timestamp", None)
        if ts is not None:
            return "Day {}".format(ts + 1)
        return ""

    def add_contact(contact):
        """Add a new contact to the met list"""
        if contact not in contacts_met:
            contacts_met.append(contact)
        if contact not in phone_messages:
            phone_messages[contact] = []
        if contact not in unread_messages:
            unread_messages[contact] = 0

    def send_notification(contact, message_text, image=None):
        """Send a message and briefly show the phone notification.
        
        Args:
            contact: String key like "dad", "brother", etc.
            message_text: The text (can be "" if image-only).
            image: Optional image path string.
        
        Examples:
            $ send_notification("dad", "Come downstairs now.")
            $ send_notification("brother", "", image="images/brother/brother creepy.png")
        """
        receive_message(contact, message_text, image=image)
        if image and not message_text:
            renpy.notify("📱 {} sent a photo".format(contact.capitalize()))
        else:
            renpy.notify("📱 New message from {}".format(contact.capitalize()))

    def open_phone_to_chat(contact):
        """Open the phone directly to a specific chat"""
        store.phone_menu_open = True
        store.current_message_contact = contact
        store.phone_feature = "message_chat"

    def close_phone():
        """Close the phone completely"""
        store.phone_menu_open = False
        store.selected_contact = None
        store.current_message_contact = None
        store.phone_feature = "home"
