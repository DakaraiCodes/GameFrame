import cv2
from video import open_video, get_frames_every_second
from vision import analyze_scoreboard
from ocr import extract_text
from models import build_game_data
from io_utils import save_game_data

video_path = "../data/sample_game.mp4"

video = open_video(video_path)

frames = get_frames_every_second(video)

first_sampled_frame = frames[0]

last_valid_game_data = {
    "left_score": None,
    "right_score": None,
    "quarter": None,
}

timeline = []

for index, frame in enumerate(frames):
    print(f"\nFrame {index + 1}")
    regions = analyze_scoreboard(frame)
    ocr_data = extract_text(regions)
    game_data = build_game_data(ocr_data)

    carry_forward_keys = [
        "left_score",
        "right_score",
        "quarter",
    ]

    for key in carry_forward_keys:
        if game_data[key] is None:
            game_data[key] = last_valid_game_data[key]
        else:
            last_valid_game_data[key] = game_data[key]

    timeline.append(game_data.copy())

    print("Game data:", game_data)

print("\nTimeline length:", len(timeline))
save_game_data (
    timeline,
    "../data/video_timeline.json"
)

video.release()