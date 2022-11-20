import cv2
import numpy as np

def load_capture():
    capture = cv2.VideoCapture("rtsp://192.168.0.98/live0")
    return capture

# Sekunden pro Frame
sPF = 1
calcedFPS = 1/sPF

# Um Framenummer zu loggen
total_frames = 0

while True:
    # Bild (Video) (eig sogar einzelnes Frame) laden
    capture = load_capture()
    ret, img = capture.read()

    # Falls kein Bild mehr kommt --> Abbruch
    if img is None:
        print("End of stream")
        break

    # Bild in neuem Fenster namens "Videostream" anzeigen
    cv2.imshow("Videostream", img)

    # Gesamtanzahl an Frames erhöhen
    total_frames += 1

    # Bild nicht mehr speichern
    capture.release()

    # waitKey = Abbruch durch Tasteneingabe
    # 1000ms = 1s --> wartet also 1s
    # 1s --> damit fps runter geht --> geringere CPU Auslastung (alter Laptop von 90% auf 30%)
    if cv2.waitKey(sPF*1000) > -1:
        print("-----")
        print("Script durch Tasteneingabe beendet")
        break

    # Framenummer loggen
    print("Frame #" + str(total_frames))