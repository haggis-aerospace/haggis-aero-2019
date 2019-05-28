'''import cv2


def capture():
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1080, 720))
    while(True):
        #for _ in range(2):
            #cap.read()
        ret, frame = cap.read()
        if ret==True:
            cv2.imshow('Stream', frame)
            cv2.waitKey(1)
            #out.write(frame)

if __name__ == "__main__":
    capture()

'''

import cv2, queue, threading, time, imutils, os, os.path

# bufferless VideoCapture
class VideoCapture:

  def __init__(self, name):
    self.cap = cv2.VideoCapture(0)
    self.q = queue.Queue()
    t = threading.Thread(target=self._reader)
    t.daemon = True
    t.start()

  # read frames as soon as they are available, keeping only most recent one
  def _reader(self):
    while True:
      ret, frame = self.cap.read()
      if not ret:
        break
      if not self.q.empty():
        try:
          self.q.get_nowait()   # discard previous (unprocessed) frame
        except Queue.Empty:
          pass
      self.q.put(frame)

  def read(self):
    return self.q.get()

cap = VideoCapture(0)
#frame = cap.read()
#(w,h) = frame.shape[:2]
#(w,h) = (640, 480)
#name = "output"
#index = len([name for name in os.listdir('.') if os.path.isfile(name)])
#name = name + str(index) + ".avi"
#out = cv2.VideoWriter(name,cv2.VideoWriter_fourcc('X','V','I','D'), 24, (w,h))

def get_img(counter=0, save_directory):
  #start_time = time.time()
  frame = cap.read()
  frame = imutils.rotate(frame, 270)
  #print(frame.shape[:2])
 # out.write(frame)
  #time.sleep(.5)   # simulate long processing
  #(w,h) = frame.shape[:2]

  #M = cv2.getRotationMatrix2D((w/2,h/2),180,1)
  #frame = cv2.warpAffine(frame, M, (h, w))
  #cv2.flip(frame, frame, -1)
  #cv2.imshow("frame", frame)
  #end_time=time.time()
  #frame_rate=1/(end_time-start_time)
  #wait_time = 1/(30-frame_rate)
  #if wait_time < 0:
  #  wait_time=0
  #time.sleep(wait_time)
  threading.Thread(target=cv2.imwrite, args=('/media/pi/0677794046B427B7/CV/{}/frame{}.BMP'.format(save_directory, counter), frame))
  return 'frame{}.BMP'.format(counter)
  #end_time = time.time()
  #frame_rate = 1/(end_time-start_time)
  #print(frame_rate)
#  if chr(cv2.waitKey(1)&255) == 'q':
#    break
