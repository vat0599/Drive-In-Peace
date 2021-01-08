# Drive In Peace aka D.I.P
A smart vehicle assistance system which has drowsiness detection, glare detection for four wheeler along with distress call alert.

This was designed for Uber, Ola and other ridesharing organizations to enhance customer experience by ensuring they have a safe ride.
During long rides, its likely that the driver gets tired and in some rare case might fall asleep during the ride. This can cause fatal damage to both the driver as well as the customer travelling behind. Thus to ensure this never happens, a camera will be attached to the car and will monitor the eye movements (clearly undrerstands the difference between eye blinking and sleeping) of the driver and when the driver nods off, it will perform a distress call to the customer to wake the driver up along with storing the driver details in the database with the timestamp. The car will immediately slow down and will come down to an halt with sirens wailing inside the car to attract the most attention. Then after the driver is fully conscious, he/she can resume the ride by clicking a trigger button.

Similary, it is possible that while driving some shiny objects might block the view and this even though looks simple, might cause the driver to loose focus and hit somewhere. Thus, a camera is fitted in front and monitors the road continously and during such unfortunate occasions, it automatically reduces its speed in a smooth manner and moves past the danger. These intelligent systems ensure that the driver gets atmost safety and secure feeling during his/her ride and also increases the trust towards the company. The company also has an understanding towards their drivers performances and can take appropriate action for their wellbeing.

## Steps to implement the code:
- Clone the repo.
- In that folder add the shape predictor model file by clicking on the link given: https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2
- Now we should create a twilio account in order to have a phone number for the laptop or pc you are using. In order to do that follow this link https://www.twilio.com/ and create a free account. You'll receive a account_sid and auth_token along with a phone number for your laptop. These should now be edited to your drowsiness_detection.py.
- Now finally you need to install unreal engine to create a simulation to test your code performance in the simulated car. You can find a folder named "MRT 4.23", this is the folder which has the simulation of a car moving in an environment. Now you should open the unreal engine emulator, go the MRT 4.23 folder and open the file MRT.uproject. You'll be able to see a car in a highway. This is your environment. The car and your web cam feed is simultaneously monitored and appropriate action will be taken.
- Now that your setup is ready, you can finally run the drowsiness_detection.py code and switch to the simulation window. A web cam feed along with the car movement can be seen and when you sleep or bring in flashlights nearby, you can see the effect of it in the car's speed along with the alert window.

## How this works?
- The code
<img src="https://user-images.githubusercontent.com/41820878/104019598-d6502480-51e1-11eb-8ff4-ac13b8b4fb84.png">

## Some output screenshots while running the code:
<img src="https://user-images.githubusercontent.com/41820878/104029372-ea028780-51ef-11eb-975e-7e7d8b93e447.png">

<img src="https://user-images.githubusercontent.com/41820878/104029690-4b2a5b00-51f0-11eb-810a-edc9b15435d8.png">

<img src="https://user-images.githubusercontent.com/41820878/104029732-5a110d80-51f0-11eb-8bed-91d895456ed9.png">

<img src="https://user-images.githubusercontent.com/41820878/104029791-6dbc7400-51f0-11eb-8736-5c54e9157bd8.png">
