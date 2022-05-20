import time
import tqdm

for outer in tqdm.tqdm([10, 20, 30, 40, 50], desc=" outer", position=0):
    for inner in tqdm.tqdm(range(outer), desc=" inner loop", position=1, leave=False):
        time.sleep(0.05)
print("done!")