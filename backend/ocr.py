import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text(regions):
    # Left score preprocessing

    left_score_gray = cv2.cvtColor(
        regions["left_score"],
        cv2.COLOR_BGR2GRAY
    )

    _, left_score_binary = cv2.threshold(
        left_score_gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    left_score_large = cv2.resize(
        left_score_binary,
        None,
        fx=6,
        fy=6,
        interpolation=cv2.INTER_NEAREST
    )

    left_score_padded = cv2.copyMakeBorder(
        left_score_large,
        40,
        40,
        40,
        40,
        cv2.BORDER_CONSTANT,
        value=255
    )

    left_score_text = pytesseract.image_to_string(
        left_score_padded,
        config="--psm 10 -c tessedit_char_whitelist=0123456789O"
    ).strip()
    
    print("Raw left score OCR:", repr(left_score_text))
    left_score_text = left_score_text.replace("O", "0")

    # Right score preprocessing

    right_score_gray = cv2.cvtColor(
        regions["right_score"],
        cv2.COLOR_BGR2GRAY
    )

    _, right_score_binary = cv2.threshold(
        right_score_gray,
        0,
        255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    right_score_large = cv2.resize(
        right_score_binary,
        None,
        fx=6,
        fy=6,
        interpolation=cv2.INTER_NEAREST
    )

    right_score_padded = cv2.copyMakeBorder(
        right_score_large,
        40,
        40,
        40,
        40,
        cv2.BORDER_CONSTANT,
        value=255
    )

    right_score_text = pytesseract.image_to_string(
        right_score_padded,
        config="--psm 10 -c tessedit_char_whitelist=0123456789O"
    ).strip()

    print("Raw right score OCR:", repr(right_score_text))

    right_score_text = right_score_text.replace("O", "0")

    # Game clock preprocessing

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

    # ---------------------
    # Quarter preprocessing
    # ---------------------
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

    # ------------------------
    # Shot clock preprocessing
    # ------------------------
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

    # Save processed score images for debugging
    cv2.imwrite(
        "../data/left_score_padded.jpg",
        left_score_padded
    )

    cv2.imwrite(
        "../data/right_score_padded.jpg",
        right_score_padded
    )

    return {
        "left_score_text": left_score_text,
        "right_score_text": right_score_text,
        "game_clock_text": game_clock_text,
        "quarter_text": quarter_text,
        "shot_clock_text": shot_clock_text,
    }