import subprocess
import time

start_time = time.time()
for i in range(100):
    p = subprocess.Popen(["python","/workspace/cortx-s3server/testauth1.py","100"])
print("to main thread")
#for i in range(10):
p.wait()
sending_time = time.time() - start_time
print(sending_time)
