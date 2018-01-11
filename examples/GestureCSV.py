from __future__ import print_function
import collections
import myo
import threading
import time
import numpy as np
import pickle

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
      print('5 words!')
      #print(data['Myo'][0])
      print(data['Obs'])
      
      #timestamp=datetime.strftime(datetime.now(),"%Y%m%d%H%M%S") 
      timestamp = time.time()
      file=open(path1+"MyoData%s"%timestamp,'w')
      '''
      for i in np.arange(len(data['Obs'])):        
        #file.write("Myo: %d" % data['Myo'][i])
        file.write("Obs: ")
        for j in np.arange(len(data['Obs'][i])):
          file.write("%d" % data['Obs'][i][j])
        file.write("\n")
      '''
      pickle.dump(data['Myo'] ,file)
      pickle.dump(data['Obs'] ,file)
      data={'Myo':[],"Obs":[]}
      file.close()
      count = 0
     
    time.sleep(1.0)
finally:
  hub.shutdown()
  
