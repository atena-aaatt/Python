import cv2
import dlib
import numpy as np


tahminYolu= "shape_predictor_68_face_landmarks.dat"


detector = dlib.get_frontal_face_detector()
tahmin= dlib.shape_predictor(tahminYolu)


def tahmin_duygu(landmarks):
    
    agiz= (
        np.linalg.norm(landmarks[62] - landmarks[66]) /
        np.linalg.norm(landmarks[48] - landmarks[54])
    )
    
   
    if agiz > 0.1:
        return "Happy"
    elif agiz<= 0.2:
        return "Neutral"
  


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("hata kamera açılamadı")
    exit()

while True:
    T, frame = cap.read()
    if not T:
        print("hata frame bulunamadı")
        break

    
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    faces = detector(gri)
    for face in faces:
        nokta = tahmin(gri, face)

       
        points = []
        for i in range(68):
            x = nokta.part(i).x
            y = nokta.part(i).y
            points.append((x, y))
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        points = np.array(points)

       
        emotion =tahmin_duygu(points)

        
        x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

      
        cv2.putText(
            frame, emotion, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2
        )

   
    cv2.imshow("Duygu Tespiti", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
