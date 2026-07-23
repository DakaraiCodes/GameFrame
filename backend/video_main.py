import cv2
from video import open_video, get_frames_every_second
from vision import analyze_scoreboard
from ocr import extract_text
from models import build_game_data
from io_utils import save_game_data
from events import detect_scoring_events, detect_lead_changes
from runs import detect_scoring_runs
from teams import get_team_name
from summary import build_game_summary 
from report import print_game_summary 
from stats import get_largest_lead, get_largest_run


team_names = {
    "left": "Knicks",
    "right": "Nets",
}

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

scoring_events = detect_scoring_events(timeline)

largest_lead = get_largest_lead(timeline)

print("\nLargest lead:")
print(largest_lead)


for event in scoring_events:
    team_name = get_team_name(
        event["team"],
        team_names
    )

    display_event = {
        **event,
        "team": team_name,
    }

    print(display_event)

lead_changes = detect_lead_changes(scoring_events)

print("\nLead changes:")

for change in lead_changes:
    print(change)

scoring_events = detect_scoring_events(timeline)

print("\nScorng events:")

team_name = get_team_name(
    event["team"],
    team_names
)

print({
    **event,
    "team": team_name,
})

scoring_runs = detect_scoring_runs(scoring_events)

largest_run = get_largest_run(scoring_runs)

print("\nLargest run:")
print(largest_run)

print("\nScoring runs:")

for run in scoring_runs:
    print(run)

game_summary = build_game_summary(
    timeline,
    scoring_events,
    lead_changes,
    scoring_runs,
    largest_lead,
    largest_run,
)

print_game_summary(
    game_summary,
    team_names
)

video.release()