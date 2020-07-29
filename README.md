# SystemArchitectureProject

This project is part of the study course 'System Architecture'. 

It is based on a video tutorial by Corey Schafer called "Full-Featured Web App" 
(Link: https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p).
This tutorial helped me lot to understand the basics of Django and it contains a large part of the functionality, 
I needed for the study project, like user accounts, admin dashboard, password 
encryption, password resetting with email and so on. I also liked that the website is responsive,
because Bootstrap was used. I kept the blog functionality in the app, because it might be useful someday. 

This the fuctionality I added:

  - <b>MQTT Client (mqtt_subscriber.py):</b> The app is able to connect to a MQTT broker, which runs on a computer in my 
  university. It can be accessed via VPN. The MQTT client can handle multiple topics, send data 
  directly to the frontend via websockets, post data (in JSON format) to the backend and write 
  data to JSON file in the project folder. During the project execution, the date was sent to me via MQTT from a 
  Raspberry Pi which was handled by a different group of students and contained sensor information. 
  It's also possible to use dummy data from my own publishing client (mqtt_publisher.py).
  
  - <b>Remote Login via RFID:</b> When an RFID transponder is held to the RFID reader, a message 
  is sent to the backend and the owner is assigned to a vehicle as a driver if a user with the correct RFID token is 
  found in the database. When the transponder is read again, the driver is removed.

  - <b>Real-Time Data Visualisation:</b> The use case of the project consisted of receiving sensor data from (imaginary) 
  vehicles and visualizing them in a web application. I decided to visualize the data on a dashboard for each vehicle 
  in real-time. To achieved that, I used websockets and the library Channels. The data received by the MQTT client is 
  first sent (as soon it is received) to a Channels consumer, where it is processed and forwarded to a JavaScript websocket client on the 
  frontend. For the visualisation charts I used the library Chart.js and some jQuery for the table visualisation. 
  
  - <b>RESTful API:</b> I used the Django REST Framework to create a RESTful API for the sensor data. The sensor data is 
  serialized into JSON and can be manipulated by other programs like Postman or the MQTT client via HTTP-Requests (GET, POST, PUT).
  
Although it's not quite finished, the app looks great and works very well. Especially the real-time data visualization works 
astonishingly well. I really enjoyed working on this app and I learned a lot. I would love to continue where I left off and develop 
even better and more complete apps with similar functionalities.
