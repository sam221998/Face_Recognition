import os
import facerec
import cv2
import mysql.connector
import wikip
import webbrowser







                                  
#connect to sam database in mysql  where store the my images
mydb = mysql.connector.connect(
  host="localhost",
  user="sameer",
  passwd="Sameer123@",
  database='sam'
)

mycursor = mydb.cursor()


'''filename = '/home/sameer/project/sem2/helloworld1.html'
webbrowser.open_new_tab(filename)'''



img=str(input("Enter the Path of image or Image name"))


j=cv2.imread(str(img))
cv2.imshow("Compare/INPUT Image",j)
cv2.waitKey(0)
cv2.destroyAllWindows()



image1 =facerec.load_image_file(str(img))


image1encode=facerec.face_encodings(image1)[0]


myimg=os.listdir('images')

for image in myimg:


    cimage = facerec.load_image_file("images/"+image)
    cimagenc = facerec.face_encodings(cimage)[0]
    result = facerec.compare_faces([image1encode],cimagenc)
    

    
    if result[0] == True:
        print "match: "+image
        sentimg=image
        sql="select name from info where image = %s"
        adr = (image, )
        mycursor.execute(sql, adr)
        myresult = mycursor.fetchall()
        for x in myresult:
            print x
            webbrowser.open_new_tab('/home/sameer/project/sem2/helloworld1.html')
        break
    
