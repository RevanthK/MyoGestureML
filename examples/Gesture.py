from __future__ import print_function
import collections
import myo
import threading
import time

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

try:
  listener = MyListener()
  hub.run(200, listener)

  while True:

    print(listener.get_emg_data())
    print(listener.get_orient_data())
      
    time.sleep(1.0)
finally:
  hub.shutdown()
  
