
def safe_int(value):
    if value.isdigit():
        return int(value)

    return None

def build_game_data(ocr_data):
    game_clock_text = ocr_data["game_clock_text"]

    if game_clock_text.isdigit():
        if len(game_clock_text) == 4:
            minutes = int(game_clock_text[:2])
            seconds = int(game_clock_text[2:])

            if minutes <= 12 and seconds <= 59:
                game_clock_text = f"{minutes}:{seconds:02d}"
            else:
                game_clock_text = None

        elif len(game_clock_text) == 3:
            minutes = int(game_clock_text[0])
            seconds = int(game_clock_text[1:])

            if minutes <= 9 and seconds <= 59:
                game_clock_text = f"{minutes}: {seconds:02d}"
            else:
                game_clock_text = None
        else:
            game_clock_text = None
    else:
        game_clock_text = None

    #Quarter 
    quarter_text = ocr_data["quarter_text"]

    if "ST" in quarter_text:
        quarter_value = 1
    elif "ND" in quarter_text:
        quarter_value = 2
    elif "RD" in quarter_text:
        quarter_value = 3
    elif "TH" in quarter_text:
        quarter_value = 4
    else:
        quarter_value = None

    #shot clock
    shot_clock_text = ocr_data["shot_clock_text"]
    shot_clock_value = safe_int(shot_clock_text)


    return {
        "left_score": safe_int(ocr_data["left_score_text"]),
        "right_score": safe_int(ocr_data["right_score_text"]),
        "quarter": quarter_value,
        "game_clock": game_clock_text,
        "shot_clock": shot_clock_value,
    }