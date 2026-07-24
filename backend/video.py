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

def get_video_fps(video):
    fps = video.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        raise RuntimeError("Could not determine video FPS.")

    return fps

def stream_frames_every_second(video):
    fps = get_video_fps(video)
    frame_interval = int(fps)

    frame_number = 0

    while True:
        success, frame = video.read()

        if not success:
            break

        if frame_number % frame_interval == 0:
            yield frame

        frame_number += 1

if __name__ == "__main__":
    video_path = "../data/sample_game.mp4"

    video = open_video(video_path)

    frame_count = 0

    for frame in stream_frames_every_second(video):
        frame_count += 1

    print("Frames extracted", frame_count)

    video.release()

