# Development of cost effective applications using eye gaze and facial features to access the pc/laptop by the person with SCI

# Description
Developing assistive software for spinal cord injury patients, enabling computer use through eye and facial movements via webcam integration. This entails designing an intuitive user interface, incorporating eye tracking and facial recognition technology, ensuring accessibility features, employing machine learning for accuracy, conducting extensive user testing, prioritizing privacy and security, providing comprehensive support, and complying with relevant regulations.We're developing a free solution utilizing machine learning and the OpenCV2 package to enable spinal cord injury patients to control computers using only eye and facial movements via webcam integration. This solution aims to provide an affordable alternative to existing options like the head mouse, which typically costs between Inr 15,000 to Inr 20,000. Our approach leverages advanced algorithms for eye tracking and facial recognition, ensuring accurate and responsive control. By utilizing open-source tools and technologies, we're committed to making computer access more accessible and affordable for individuals with spinal cord injuries, thereby enhancing their independence and quality of life.

# Team member details
Team number VH100
Gembali Keerthivardhan-Team Leader
Gadde Ashok
Kotaru Pavan Kalyan
Unnam Venkateswara Prasad

# The problem it solves

Every day, approximately 100 individuals suffer from spinal cord injuries (SCI), with 40 of them experiencing the devastating loss of motor function below the neck. Many of these individuals were previously active computer users, relying on PCs for work and daily tasks. However, their injuries have abruptly severed this vital connection to technology, severely limiting their ability to communicate, work, and engage with the world.To address this pressing issue, we are developing a solution that leverages machine learning and the OpenCV2 package. By harnessing the power of eye and facial movements captured through a webcam, we aim to empower SCI patients to regain control over their computers, enabling them to navigate interfaces, type messages, and access vital resources independently. This initiative is crucial as it not only restores a sense of autonomy and productivity to those affected by SCI but also provides a cost-effective alternative to existing solutions, such as the prohibitively expensive head mouse.Through our commitment to accessibility and innovation, we strive to bridge the technological gap caused by spinal cord injuries, ensuring that individuals can continue to participate fully in both professional and personal spheres despite their physical limitations. By providing a free solution to this pressing problem, we aim to make meaningful contributions to the lives of SCI patients, fostering greater inclusion and opportunity in the digital age.

# Use Cases

1. Communication and Social Interaction: Enable SCI patients to communicate with friends, family, and colleagues through text-based platforms and social media by typing messages using eye and facial movements.

2. Work and Productivity: Facilitate access to productivity tools such as word processors, spreadsheets, and email clients, allowing users to continue working remotely or engaging in educational activities.

3. Internet Browsing and Information Access: Empower users to browse the internet, conduct research, and access online resources independently, enhancing their ability to stay informed and connected with the world.

4. Entertainment and Leisure: Provide access to entertainment content such as movies, music, and games, allowing users to enjoy leisure activities and relax during their downtime.

5. Assistive Device Control : Integrate with smart home devices and assistive technologies to control lights, temperature, and other environmental factors, enhancing accessibility and comfort within the home environment.

6. Health Monitoring and Rehabilitation : Incorporate features for health monitoring and rehabilitation exercises, enabling users to track their progress and adhere to treatment plans prescribed by healthcare professionals.

7. Educational Opportunities: Support access to online learning platforms and educational resources, empowering users to continue their education and pursue personal development goals.

8. Remote Healthcare Services: Enable users to participate in telehealth appointments and access remote healthcare services, facilitating communication with healthcare providers and improving overall healthcare outcomes.

9. Community Engagement and Support: Foster connections within the SCI community by providing access to online forums, support groups, and peer-to-peer networks, promoting mutual support and sharing of experiences.

10. Customizable Interfaces: Offer customizable interfaces and settings to accommodate individual preferences and unique user needs, ensuring a personalized and intuitive user experience.

# Challenges we ran into

1. Interference from Other People : One significant challenge is dealing with interference from other people entering the camera frame. The software may inadvertently focus on their eyes instead of the intended user's eyes, disrupting the user's control over the system. To address this, you implemented a locked gaze feature to prioritize the user's eyes. However, ensuring reliable detection and differentiation between multiple individuals in the frame remains a challenge, particularly in crowded or dynamic environments.

2. Accuracy of Eye and Facial Movement Detection: Another critical challenge is ensuring the accuracy of eye and facial movement detection. Variability in lighting conditions, camera quality, and user positioning can affect the precision of tracking algorithms, leading to errors in interpreting user inputs. Achieving consistent and reliable tracking across different users and environments requires sophisticated machine learning models and robust calibration techniques.

3. Adaptation to User Variability: Users with spinal cord injuries may exhibit a wide range of eye and facial movement capabilities, requiring the software to adapt to individual variability. Developing algorithms that can accommodate diverse movement patterns and user preferences while maintaining accuracy poses a significant technical challenge. Additionally, providing customizable settings and calibration options to tailor the software to each user's specific needs adds complexity to the development process.

4. Real-time Performance and Responsiveness: Ensuring real-time performance and responsiveness of the software is crucial for a seamless user experience. Processing eye and facial movement data, interpreting inputs, and generating corresponding actions must occur with minimal latency to provide fluid interaction. Optimizing algorithm efficiency and leveraging hardware acceleration techniques are essential for meeting performance requirements, particularly on resource-constrained devices such as laptops.

5. User Training and Adaptation: Effective user training and adaptation are critical for maximizing the usability of the software. Teaching users how to use the system effectively, providing feedback on their movements, and incorporating mechanisms for user feedback and adjustments are essential for facilitating a smooth learning curve and improving overall user satisfaction.

Addressing these challenges requires a multidisciplinary approach combining expertise in computer vision, machine learning, human-computer interaction, and assistive technology. By iteratively refining algorithms, conducting rigorous testing, and incorporating user feedback, you can overcome these challenges and develop a robust and user-friendly solution for spinal cord injury patients.






# Demo Video

https://youtu.be/CA3Ka7HejZY

# Exact Steps to Run the project

1)First the open the repository in Vs Code
2)Then Open the Iriscontrol.py
3)Then Run in the python interpreter installed in the lap/pc
4)Then the video output pops up and it detects the eyes
5)There are two pointers yellow(2 dots) and Green(4 dots)
6)When ever you close right eye yellow dots meet and it act as click
7) Left eye can be used as mouse

# Technologies used

Python
Open Cv
Media pipe
Py autogui
Tensor flow


