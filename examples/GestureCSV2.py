from __future__ import print_function
import collections
import myo
import threading
import time
import numpy as np
import pandas as pd

class MyListener(myo.DeviceListener):

  def __init__(self, queue_size=8):
    self.lock = threading.Lock()
    self.emg_data_queue = collections.deque(maxlen=queue_size)
    self.orientation = []

  def on_connect(self, device, timestamp, firmware_version):
    device.set_stream_emg(myo.StreamEmg.enabled)

  def on_emg_data(self, device, timestamp, emg_data):
    with self.lock:
      self.emg_data_queue.append((timestamp, emg_data))

  def on_orientation_data(self, myo, timestamp, orientation):
    with self.lock:
      self.orientation = orientation

  def get_emg_data(self):
    with self.lock:
      return list(self.emg_data_queue)

  def get_orient_data(self):
    with self.lock:
      return list(self.orientation)

myo.init()
hub = myo.Hub()

data={'Myo':[],"Obs":[]}
path1="RevData/"

try:
  listener = MyListener()
  hub.run(200, listener)

  count = 0

  while True:
    
    if count < 5:
      data['Myo'].append(listener.get_emg_data())
      data['Obs'].append(listener.get_orient_data())
      count = count + 1
    else:
      print('10 words!')

      df = pd.DataFrame(data = data['Obs'])

      myoD = []

      for i in data['Myo']:
        #df2 = pd.DataFrame(data = data['Myo'])
        if(len(i) > 0):       
          for j in i:      
            myoD.append(j[1])



      print(myoD)
      df2 = pd.DataFrame(data = myoD)
      df2[df2.columns] = df2[df2.columns].astype(int)

      timestamp = time.time()
      #df.to_csv(path1+"ObsData%s"%timestamp, sep=',')
      #df2.to_csv(path1+"MyoData%s"%timestamp, sep=',')

      array = df.values
      array2 = df2.values.astype(int)


      np.savetxt(path1+"ObsData%s.csv"%timestamp, array, delimiter=",",  fmt='%d')
      np.savetxt(path1+"MyoData%s.csv"%timestamp, array2, delimiter=",",  fmt='%d')

      data={'Myo':[],"Obs":[]}
      count = 0
     
    time.sleep(1.0)
finally:
  hub.shutdown()
  
