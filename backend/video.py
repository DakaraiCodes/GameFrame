import cv2

def open_video(video_path):
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        raise FileNotFoundError(f"Could not open video: {video_path}")
    
    print("Video opened successfully")

    return video

video_path = "../data/sample_game.mp4"

video = open_video(video_path)

video.release()

def get_first_frame(video):
    success, frame = video.read()

    if not success:
        raise RuntimeError("Could not read first frame.")
    
    print("First frame extracted")

    return frame

video_path = "../data/sample_game.mp4"

video = open_video(video_path)

frame = get_first_frame(video)

cv2.imwrite("../data/first_frame.jpg", frame)
cv2.imshow("First Frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

video.release()