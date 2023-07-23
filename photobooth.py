import numpy as np
from PIL import Image, ImageDraw, ImageFont
from picamera2 import Picamera2, Preview
import time
from datetime import datetime
from gpiozero import Button
from signal import pause
import cv2

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
bg1 = Image.open('/home/pi/cv2_test1/PicsArt.jpg')
ft1 = Image.open('/home/pi/cv2_test1/kisspng.png')
frontImage = Image.open('/home/pi/cv2_test1/Pngtree.png')
bg1 = bg1.convert("RGBA")
ft1 = ft1.convert("RGBA")
frontImage = frontImage.convert("RGBA")
font = ImageFont.truetype("/home/pi/cv2_test1/Conquest-8MxyM.ttf", 100)

picam2 = Picamera2()
button = Button(17)
#count = 2
camera_config = picam2.create_still_configuration(main={"size": (1047, 1256)}, lores={"size": (534, 640), "format": "YUV420"}, display="lores")
picam2.configure(camera_config)

picam2.start_preview(Preview.QTGL)
picam2.start()
def capture():
    timestamp = datetime.now().isoformat()
    path = '/home/pi/Pictures/%s.jpg' % timestamp
    picam2.capture_file(path)
    picam2.stop()
    picam2.stop_preview()

    #
    background = Image.open(path)
    background = background.convert("RGBA")

    #
    bg1.paste(background, (461,207), background )

    img_background = np.array(bg1)
    grey = cv2.cvtColor(img_background, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(grey, scaleFactor=1.3, minNeighbors=5)
    #
    for (x, y, w, h) in faces:
        #cv2.rectangle(img_background, (x, y), (x + w, y + h), (0, 255, 0))
        print("("+str(x)+","+str(y)+")"+"("+str(w)+","+str(h)+")")
        ft_rs = ft1.resize((w, int(221*(w/607))))
        bg1.paste(ft_rs,(x,y-int(221*(w/607))),ft_rs)

    #
    bg1.paste(frontImage, (0,0), frontImage)
    
    # Save this image
    draw = ImageDraw.Draw(bg1)
    text = "#Thanh Thanh"
    x, y = 812, 1524

# Draw the text on the image
    draw.text((x, y), text, font=font, fill=(56, 24, 6))
    bg1.save('/home/pi/Pictures/%s.PNG' % timestamp, format="png")
    cv2.imshow('cute-chua-ne:))',cv2.imread('/home/pi/Pictures/%s.PNG' % timestamp,  cv2.IMREAD_UNCHANGED))
button.when_pressed = capture
pause()





