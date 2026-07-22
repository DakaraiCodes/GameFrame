import cv2

def open_video(video_path):
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        raise FileNotFoundError(f"Could not open video: {video_path}")
    
    print("Video opened successfully")
    return video


def get_first_frame(video):
    success, frame = video.read()

    if not success:
        raise RuntimeError("Could not read first frame.")
    
    print("First frame extracted")

    return frame

if __name__ == "__main__":
    video_path = "../data/sample_game.mp4"

    video = open_video(video_path)

    frame = get_first_frame(video)

    video.release()

