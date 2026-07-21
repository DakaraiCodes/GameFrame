def build_game_data(ocr_data):
    game_clock_text = ocr_data["game_clock_text"]

    if len(game_clock_text) == 4 and game_clock_text.isdigit():
        game_clock_text = game_clock_text[0] + ":" + game_clock_text[2:]
    elif len(game_clock_text) == 3 and game_clock_text.isdigit():
        game_clock_text = game_clock_text[0] + ":" + game_clock_text[1:]

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

    shot_clock_text = ocr_data["shot_clock_text"]

    shot_clock_value = (
        int(shot_clock_text)
        if shot_clock_text.isdigit()
        else None
    )

    return {
        "left_score": int(ocr_data["left_score_text"]),
        "right_score": int(ocr_data["right_score_text"]),
        "quarter": quarter_value,
        "game_clock": game_clock_text,
        "shot_clock": shot_clock_value,
    }