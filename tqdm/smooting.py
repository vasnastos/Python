import time
import tqdm

for t in tqdm.tqdm([50]*10 + [10]*50, smoothing=0.1):
    time.sleep(t*0.01)

for t in tqdm.tqdm([50]*10 + [10]*50, smoothing=0.9):
    time.sleep(t*0.01)
