# UCI-ICS33
Final Project done in University of California, Irvine, ICS33 class
# Inheritance and Animation
There are different types of objects(listed on the top). Each object supports different functionality:
1. Ball(blue): small balls which move in straight lines and with constant speed, bouncing around in the display window.
2. Floater(red): small balls moving in strage way(basically straight line but with fluctuations), with same constant speed as 'ball', bouncing around in the display window.
3. Black hole(black): when balls or floaters pass the black hole(overlap with the black hole), black hole will 'eat' the passing object.
4. Plusator(black): Similar as Black hole but will change size. It will shrink as time passes unless it eats. It will eventually disappear on the window if it doesn't eat.
5. Hunter(black): Similar as Plusator but will move in straight line and constant speed, bouncing around in the window.
6. Special(green): Special object that will follow user's command to move. User can use "WASD" to control the ball move upward, leftward, downward and rightward with default constant speed. It will shrink and eat any balls or floaters as a hunter. When it hit the edge of the display window, it will 'die' with a popup window asking the user whether or not to restart the game. It restart, the display window will clean up. 

Other Buttons:
1. Reset: The display window will clean up all the objects and the ball/cycle information will reset as 0. 
2. Start: After hit, the animation will start.
3. Stop: The animial will stop.
4. Step: The animial will stop and if hit the button again, the animation will go one cycle and stop.(Step by step animation)
5. Remove: Hit the button and select an object on the display window, the selected object will be removed.

Ball cycle information:
The number of objects and the number of cycles will be displayed at the upper right. 

<img width="1068" alt="Screen Shot 2022-04-30 at 12 56 40 PM" src="https://user-images.githubusercontent.com/62400474/166120907-4c5c30fa-32ec-43a4-bcc2-9e2160cc94b8.png">

<img width="1073" alt="Screen Shot 2022-04-30 at 12 55 35 PM" src="https://user-images.githubusercontent.com/62400474/166120903-42d661c2-3fea-4edf-be97-1223eca06b21.png">

<img width="1070" alt="Screen Shot 2022-04-30 at 12 55 46 PM" src="https://user-images.githubusercontent.com/62400474/166120902-19d0cff8-1042-4a33-9e54-a33b82fa5714.png">

<img width="1069" alt="Screen Shot 2022-04-30 at 12 55 57 PM" src="https://user-images.githubusercontent.com/62400474/166120900-a035ddfc-94c5-4fd3-9bfd-b21ef82b2373.png">

<img width="1070" alt="Screen Shot 2022-04-30 at 12 56 15 PM" src="https://user-images.githubusercontent.com/62400474/166120899-edb261d5-9388-4b41-aa7a-7c0cf7ec1d1e.png">

<img width="1069" alt="Screen Shot 2022-04-30 at 12 56 31 PM" src="https://user-images.githubusercontent.com/62400474/166120897-a4ebabb5-3e31-4ee5-92c7-011a76f82b4c.png">

<img width="1067" alt="Screen Shot 2022-04-30 at 12 55 21 PM" src="https://user-images.githubusercontent.com/62400474/166120904-707b9024-e3d5-4ba9-8e6c-f95c04c92bdb.png">


Instruction on running the code:
Code for each object is writing in separate '.py' files. When running the animation, run the scrip.py file. 
