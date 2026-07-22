import cv2


def analyze_scoreboard(image):
    image_height, image_width = image.shape[:2]

    scoreboard = image[
        int(image_height * 0.94):int(image_height * 1.00),
        int(image_width * 0.247):int(image_width * 0.752)
    ]

    scoreboard_height, scoreboard_width = scoreboard.shape[:2]
    left_score = scoreboard[
        int(scoreboard_height * 0.05):int(scoreboard_height * 0.90),
        int(scoreboard_width * 0.31):int(scoreboard_width * 0.40)
    ]

    right_score = scoreboard[
        int(scoreboard_height * 0.05):int(scoreboard_height * 0.90),
        int(scoreboard_width * 0.58):int(scoreboard_width * 0.67)
    ]

    quarter = scoreboard[
        int(scoreboard_height * 0.05):int(scoreboard_height * 0.90),
        int(scoreboard_width * 0.67):int(scoreboard_width * 0.76)
    ]

    game_clock = scoreboard[
        int(scoreboard_height * 0.05):int(scoreboard_height * 0.90),
        int(scoreboard_width * 0.76):int(scoreboard_width * 0.94)
    ]

    shot_clock = scoreboard[
        int(scoreboard_height * 0.05):int(scoreboard_height * 0.90),
        int(scoreboard_width * 0.94):int(scoreboard_width * 1.00)
    ]
    
    print("Image received succesfully")


    left_score = scoreboard[
        int(scoreboard_height * 0.07):int(scoreboard_height * 0.88),
        int(scoreboard_width * 0.31):int(scoreboard_width * 0.40)
    ]
    
    return {
        "scoreboard": scoreboard,
        "left_score":left_score,
        "right_score":right_score,
        "game_clock":game_clock,
        "quarter":quarter,
        "shot_clock":shot_clock,
    }