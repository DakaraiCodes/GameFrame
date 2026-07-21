import cv2

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