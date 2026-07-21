import cv2
import pytesseract
import json

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

x = 465
y = 953
width = 994
height = 66


def analyze_scoreboard(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")

    print("Image loaded successfully")

    scoreboard = image[y:y + height, x:x + width]

    left_score = scoreboard[:, 300:400]
    right_score = scoreboard[:, 560:660]
    game_clock = scoreboard[:, 735:915]
    quarter = scoreboard[0:50, 660:735]
    quarter_number = quarter[:, 0:35]
    shot_clock = scoreboard[:, 915:994]

    return {
        "scoreboard": scoreboard,
        "left_score":left_score,
        "right_score":right_score,
        "game_clock":game_clock,
        "quarter":quarter,
        "quarter_number":quarter_number,
        "shot_clock":shot_clock,
    }

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



image_path = "../data/sample_game_2.jpg"

regions = analyze_scoreboard(image_path)
ocr_data = extract_text(regions)
game_data = build_game_data(ocr_data)

print(ocr_data)
print(game_data)

with open("../data/sample_game_data.json", "w") as file:
    json.dump(game_data, file, indent=4)



