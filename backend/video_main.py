import cv2
from video import open_video, get_first_frame
from vision import analyze_scoreboard
from ocr import extract_text
from models import build_game_data

video_path = "../data/sample_game.mp4"

video = open_video(video_path)

frame = get_first_frame(video)
#scoreboard_box = cv2.selectROI(
#    "Select Video Scoreboard",
#    frame,
#    showCrosshair=True,
#    fromCenter = False
#)

#print("Video scoreboard box:", scoreboard_box)

#cv2.destroyAllWindows()
#ideo.release()


#print("Video frame shape:", frame.shape)

regions = analyze_scoreboard(frame)
ocr_data = extract_text(regions)

print("OCR data:", ocr_data)

#game_data = build_game_data(ocr_data)

print("OCR data:", ocr_data)
#print("Game data:", game_data)

#cv2.imwrite("../data/video_scoreboard.jpg", regions["scoreboard"])
#left_score_box = cv2.selectROI(
#   "Select Only Left Score Number",
#    regions["scoreboard"],
#    showCrosshair=True,
#    fromCenter=False
#)

#print("Left score box:", left_score_box)
#print("Scoreboard shape:", regions["scoreboard"].shape)

#cv2.imshow("Shot Clock", regions["shot_clock"])
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#ocr_data = extract_text(regions)

#game_data = build_game_data(ocr_data)

#print(game_data)

video.release()