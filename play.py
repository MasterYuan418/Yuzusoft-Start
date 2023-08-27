import cv2
import threading
import top
import time
import pygame

def video():

    cap = cv2.VideoCapture("yuzu.mp4")
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    while (True):
        ret, frame = cap.read()
        cv2.namedWindow("video", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("video", frame)
        top.run()
        if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
            break

    cap.release()

    cv2.destroyAllWindows()


def run():
    pygame.mixer.init()
    song_1 = pygame.mixer.Sound('bgm.mp3')
    song_2 = pygame.mixer.Sound('yuzu.ogg')
    vd = threading.Thread(target=video)
    #mc = threading.Thread(target=music)
    vd.start()
    song_1.play()
    pygame.time.delay(700)
    #mc.start()
    song_2.play()
