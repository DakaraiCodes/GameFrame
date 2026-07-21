import cv2
import pytesseract

def extract_text(regions):
    left_score_text = pytesseract.image_to_string(
        regions["left_score"],
        config="--psm 7 -c tessedit_char_whitelist=0123456789"
    ).strip()

    right_score_text = pytesseract.image_to_string(
        regions["right_score"],
        config="--psm 7 -c tessedit_char_whitelist=0123456789"
    ).strip()

    game_clock_gray = cv2.cvtColor(
        regions["game_clock"],
        cv2.COLOR_BGR2GRAY
    )

    game_clock_large = cv2.resize(
        game_clock_gray,
        None,
        fx=4,
        fy=4,
        interpolation=cv2.INTER_CUBIC
    )

    game_clock_text = pytesseract.image_to_string(
        game_clock_large,
        config="--psm 10 -c tessedit_char_whitelist=0123456789"
    ).strip()

    quarter_large = cv2.resize(
        regions["quarter"],
        None,
        fx=4,
        fy=4,
        interpolation=cv2.INTER_CUBIC
    )

    quarter_text = pytesseract.image_to_string(
        quarter_large,
        config="--psm 8 -c tessedit_char_whitelist=STNDRH"
    ).strip()

    shot_clock_gray = cv2.cvtColor(
        regions["shot_clock"],
        cv2.COLOR_BGR2GRAY
    )

    _, shot_clock_binary = cv2.threshold(
        shot_clock_gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    
    shot_clock_large = cv2.resize(
        shot_clock_binary,
        None,
        fx=6,
        fy=6,
        interpolation=cv2.INTER_NEAREST
    )

    shot_clock_text = pytesseract.image_to_string(
        shot_clock_large,
        config="--psm 10 -c tessedit_char_whitelist=0123456789"
    ).strip()

    return {
    "left_score_text": left_score_text,
    "right_score_text": right_score_text,
    "game_clock_text": game_clock_text,
    "quarter_text": quarter_text,
    "shot_clock_text": shot_clock_text,
}