from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import cv2
from twilio.rest import Client
import sqlite3
from pysine import sine
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


conn = sqlite3.connect('Test.db')
def eye_aspect_ratio(eye):
        A = distance.euclidean(eye[1], eye[5])
        B = distance.euclidean(eye[2], eye[4])
        C = distance.euclidean(eye[0], eye[3])
        ear = (A + B) / (2.0 * C)
        return ear
account_sid = 'Your twilio account_sid'
auth_token = 'Your twilio auth_token'
client = Client(account_sid, auth_token)
thresh = 0.25
frame_check = 20
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("Path of your shape predictor model file") # Dat file is the crux of the code

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
cap=cv2.VideoCapture(0)
flag=0
flag1=0

while True:
        ret, frame=cap.read()
        frame = imutils.resize(frame, width=450)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray1 = cv2.GaussianBlur(gray, (61,61), 0)
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray1)
        keyboard.press('w')
        if maxLoc[0]<375 and maxLoc[0]>100 and maxLoc[1]<240 and maxLoc[1]>117:
                flag1+=1
                print("Glare: ",flag1)
                if flag1>30:
                        cv2.circle(frame, maxLoc, 31, (255, 0, 0), 2)
                        keyboard.release('w')
        else:
                flag1=0
        subjects = detect(gray, 0)
        for subject in subjects:
                shape = predict(gray, subject)
                shape = face_utils.shape_to_np(shape)#converting to NumPy Array
                leftEye = shape[lStart:lEnd]
                rightEye = shape[rStart:rEnd]
                leftEAR = eye_aspect_ratio(leftEye)
                rightEAR = eye_aspect_ratio(rightEye)
                ear = (leftEAR + rightEAR) / 2.0
                leftEyeHull = cv2.convexHull(leftEye)
                rightEyeHull = cv2.convexHull(rightEye)
                cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
                cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
                if ear < thresh:
                        flag += 1
                        print("Drowsy: ",flag)
                        if flag >= frame_check:
                                keyboard.release('w')
                                call = client.calls.create(
                                                url='http://demo.twilio.com/docs/voice.xml',
                                                to='the customers mobile number',
                                                from_='your twilio phone number'
                                        )
                                print(call.sid)
                                conn.execute("UPDATE DATA set SLEPT = 1 where ID = 789")
                                conn.commit()
                                while True:
                                        ret, frame=cap.read()
                                        frame = imutils.resize(frame, width=450)
                                        cv2.putText(frame, "****************ALERT!****************", (10, 30),
                                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                                        cv2.putText(frame, "****************ALERT!****************", (10,325),
                                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                                        sine(frequency=3000.0, duration=0.1)
                                        cv2.imshow("Smart Car", frame)
                                        key = cv2.waitKey(1) & 0xFF
                                        if key == ord("q"):
                                                break
                else:
                        flag = 0
        cv2.imshow("Smart Car", frame)
        key1 = cv2.waitKey(1) & 0xFF
        if key1==ord("q"):
                break
cv2.destroyAllWindows()
