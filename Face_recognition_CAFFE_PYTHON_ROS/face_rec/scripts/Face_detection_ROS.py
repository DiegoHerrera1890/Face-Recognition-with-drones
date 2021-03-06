#!/usr/bin/env python
import numpy as np
import cv2
import rospy
#from std_msgs.msg import String
import sys
from face_rec.msg import coordinates

def cam_test():                         
  face_cascade = cv2.CascadeClassifier('/home/jetson/catkin_ws/src/face_rec/Scripts/haarcascade_frontalface_default.xml')
  cap = cv2.VideoCapture(0)
  pub = rospy.Publisher('chatter', coordinates, queue_size=10)
  rospy.init_node('talker', anonymous=True)
  rate = rospy.Rate(10)
  msg = coordinates()
  while True:
      ret, img = cap.read()
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray, 1.3, 5)
      #width = cap.get(3)
      #height = cap.get(4)
      #print('Ancho y Alto:',width,height)
      cv2.circle(img,(320,240),15,(0,0,255),2)
      for (x,y,w,h) in faces:
          cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
          c1 =x+(w/2)
          c2 =y+(h/2)
          cv2.circle(img,(c1,c2),15,(0,255,0),2)
          roi_gray = gray[y:y+h, x:x+w]
          roi_color = img[y:y+h, x:x+w]
          #print(x)
          msg.A = x+(w/2)
          msg.B = y+(h/2)
      #hello_str = "hello world %s" % rospy.get_time()
      #rospy.loginfo(hello_str)
      
      #msg.A = 5
      #msg.B = 6
      rospy.loginfo(msg)
      pub.publish(msg)
      rate.sleep()
      cv2.imshow('img',img)
      k = cv2.waitKey(30) & 0xff
      if k == 27:
          break

  cap.release()
  cv2.destroyAllWindows()


if __name__ == '__main__':
       try:
           cam_test()
       except rospy.ROSInterruptException:
           pass
