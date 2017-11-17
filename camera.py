
import crop_face
import cv2

camera_port = 0

ramp_frames = 30

camera = cv2.VideoCapture(camera_port)



def get_image():



  while True :

    retval, im = camera.read()

    cv2.imshow("face",im)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break


    resized_image = cv2.resize(im, (64, 64))

    return resized_image
  



