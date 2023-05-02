# ITCS_6166_3DHumanModelling
# 1.Student Details in the Group:
Group 10 :
  •	Veda Samhitha Dyawanapally. 
  •	Vigneshwar Muriki.
  •	Mounika Kasaragadda.
  •	Deepthi Gade.

# 2.Introduction:
## 3D Human Modeling:
A physical body is represented by three-dimensional (3D) models using a network of points connected by various geometrical objects like triangles, lines, curved surfaces, etc. The process of creating three-dimensional representations of an object or surface is known as three-dimensional modeling. A detailed and accurate 3D model of a human body is what is intended by 3D human modeling. This model can then be used for a variety of applications, including animation, video games, virtual reality, and human-computer interaction.
The proposed model is deployed into a AWS, GCP or any other cloud service. Video data is transmitted and processed using WebRTC protocols.
And here is the model that we are going to use

https://github.com/Danial-Kord/DigiHuman


# 3.‘Client Server Application’ in 3D Human Modelling.
We will be using Client server architecture in this project. The backend part will be implemented using python/flask. We will be using WebRTC as the underlying communication between client and server.
# 4. Project plan based on two weeks iteration 
### Iteration 1:

•	Planned to conduct a meeting with team to review and understand project scope, objectives, and timeline.

•	Research and gather the necessary requirements. And also, will do the background study about the topic.

•	Create a basic client server functionality and conduct initial testing.

•	Create a WebRTC environment using the resources provided.

•	Initial testing of the web app connected via WebRTC.

### Iteration 2:

•	Make necessary changes to the algorithm after initial testing.

•	Integrate audio and video transmission functionality using WebRTC.

•	Implement video transmission into web browser

### Iteration 3:

•	Working on the issues discussed in the Flash talk by constantly setting up meetings with the professor to discuss the issues.

### Iteration 4:

•	Deploy the model into browser and integrate WebRTC to enable real time communication with the model.

•	Presentation on the final project.

•	Upload the final report as well as the code onto canvas.

# CHANGE OF PROJECT - SPEECH TO TEXT CONVERSION USING STREAMLIT
In the final iteration we have changed the project to Speech to Text conversion as there were some compilation errors in the previous project i.e., 3D Human Modeling. Since we had only 3 weeks of time for the final iteration, we have selected the project based on the time frame we had. We have created a basic speech to text conversion using streamlit with added additional features like highlighting text, editing transcription, sentiment analysis, exporting transcription.
### NOTE: In the 3D Human Modeling we faced multiple challenges to deploy the model into the browser. However, we have successfully implemented WebRTC protocols in the first iteration. We have approached Ayman Ali and scheduled meetings with him for a couple of times, but we couldn’t resolve those issues hence with the approval of Professor Pu Wang we have selected Speech to Text Project and as mentioned added additional features to the existing project.

### Instructions to run the app:
1. Extract and open the zip file in any IDE that supports python files.
2. Install all the necessary libraries SpeechRecognition, Textblob, PyAudio, streamlit, googletrans.
3. Run the app from the terminal by giving the command - "streamlit run filename.py"
4. App will run on localhost at port 8501 and the app opens in the browser.
