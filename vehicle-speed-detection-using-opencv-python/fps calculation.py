import cv2

# Load the video
video = cv2.VideoCapture("carsVideo.mp4")

# Get the frames per second (FPS) of the video
fps = video.get(cv2.CAP_PROP_FPS)

print(f"FPS of the video: {fps}")

# Don't forget to release the video capture object when done
video.release()
