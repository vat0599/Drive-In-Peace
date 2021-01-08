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
The code works on two parts:- First being the ability for the system to figure out whether a person is sleeping or not. Second being able to detect glare from the outside environment.

In the first case, we use the concept of EAR (Eye Aspect Ratio) in determining whether a person's eye is closed or not.

As you can see in the below image, we have 6 data points which signifies the posture of the eye. The summation of the distance between the top and bottom points is divided by the farthest left and right points to give us a ratio. This ratio is then used to figure the eye position as open or closed. If the ratio drops below the minimum threshold of 0.15, then it is deemed that the eye is closed.

<img src="https://user-images.githubusercontent.com/41820878/104048983-2642e180-520a-11eb-820e-48c4527f787c.png">

<img src="https://user-images.githubusercontent.com/41820878/104019598-d6502480-51e1-11eb-8ff4-ac13b8b4fb84.png">

Now the problem is that the program will end up counting blinking of eye as sleeping. To ensure this doesnt happen, we have another threshold counter for how much time the eyes remain closed. Studies shows that eye blinking process is fairly instantaneous, so any time above 2 sec (which is captured as 20 frames in the code) is considered sleeping. Thus with this premise we work on the code.

To address the second problem of glare detection, we use gaussian blur to find out the brightest point in a given frame, and if this frame has brightness above the threshold and is within the driving view, then it is considered a glare and the vehicle speed is appropriately reduced. We automatically put a circle which points to the glare region.

## Some output screenshots while running the code
Now looking at the outputs, we see that both the eyes are continuosly monitored and the car is moving smoothly over the road.

<img src="https://user-images.githubusercontent.com/41820878/104029372-ea028780-51ef-11eb-975e-7e7d8b93e447.png">

And when the eyes are closed there is a clear alert message in the screen with a loud sound to wake up the driver. Along with this we can notice that the speed of the car is also decreased and will stop smoothly. And finally the passenger travelling behind will also recieve a distress call which can be helpful at these dire situations.

<img src="https://user-images.githubusercontent.com/41820878/104029732-5a110d80-51f0-11eb-8bed-91d895456ed9.png">

In this output below, we see that when a shiny object gets in the view of road, the program automatically localises the place of blur by encircling it and the speed of the vehicle is also reduced so as to avoid any accidents at high speeds.

<img src="https://user-images.githubusercontent.com/41820878/104029690-4b2a5b00-51f0-11eb-810a-edc9b15435d8.png">

The final image below is just a small database of the drivers of the companies, and also shows whether anyone slept during their journey. This can be helpful in monitoring their employees and can also improve the quality and safety of the trips.

<img src="https://user-images.githubusercontent.com/41820878/104029791-6dbc7400-51f0-11eb-8736-5c54e9157bd8.png">

## Contributions
Do not hesitate to contribute by [filling an issue](https://github.com/vat0599/Drive-In-Peace/issues) or [a PR](https://github.com/vat0599/Drive-In-Peace/pulls) !
