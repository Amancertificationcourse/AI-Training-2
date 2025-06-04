import cv2
from deepface import DeepFace
import pyttsx3

voice = pyttsx3.init();
voice.setProperty('rate',200)
cap=cv2.VideoCapture(0)
fc=0
last=""
emotion="Detecting...."
while True:
    ret, frame=cap.read()
    if not ret:
        break

    small_frame=cv2.resize(frame,(640, 480))
    if fc%10==0:
        try:
            results=DeepFace.analyze(frame,actions=['emotion'],enforce_detection=False)
            emotion=results[0]['dominant_emotion']

            if emotion!=last:
                voice.say(f"You look {emotion}")
                voice.runAndWait()
                last=emotion

        except Exception as e:
            emotion="Error"

    cv2.putText(frame,f'Emotion: {emotion}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    cv2.imshow("Emotion Recognition",frame)
    fc+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
