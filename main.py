import cv2
import numpy as np

width = 100
height = 100
fps = 60
duration = 3
text = "Privet Sveta"

fourcc = cv2.VideoWriter_fourcc(*'avc1')  # Кодек для мака
video = cv2.VideoWriter('running_text.mov', fourcc, fps, (width, height))

color = (255, 255, 255)  # белый
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.5
thickness = 2
text_width, _ = cv2.getTextSize(text, font, font_scale, thickness)[0]
frames = int(duration * fps)
speed = text_width / frames

# Цикл по кадрам
for i in range(frames):
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    x = int(width / 2 - text_width / 2 + 100 - speed * i)

    if x < -text_width:
        x = width

    cv2.putText(frame, text, (x, int(height / 2)), font, font_scale, color, thickness, cv2.LINE_AA)
    video.write(frame)

video.release()