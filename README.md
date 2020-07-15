# Face_Recognition
This Project is about Matching the Faces of persons and display the information of that matched person.In this Project First We take image as input thenwe have make dataset of the images then given input image is search in the images directory if the given image matched with our directory of images then we fetch the name of that matched person from database.now fetched name of that person is stored in global varible and pass as parameter to function and fetched name concatinate with that wikipedia url and display the information and matched imageon terminal.In this project we used face recognition library.This library uses to compare a digital image to the stored faceprint in order to verify an individual's identity.To identify the given face  from our dataset we match the image onfollowing criteria:
1)Color of the face
2)Width of other parts of the face like lips, nose, etc.
3)Height/width of the face.
In this we use feature vector technique.feature vector is numerical representation of "Face".Vector can have (height of face(in cm), width of face(in cm),height of nose(in cm),color of face(R,G,B)).
Code Explaination
i)use two libraries os,face_recognition.
ii)we make a list of all the present images.
iii)now we load the input image to compare all other images.
iv)we encoded the loaded image into a feature vector.
v)now looping over each image we load and encode each image and compare with input encoded image and check image is matched or not
vi)if image is matched  then access the information of that matched person image
Run the file:python2 facematch2.py and give input image name in single quotes
