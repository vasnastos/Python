import time
import glob
import tqdm

pbar = tqdm.tqdm(glob.glob("dummy_text/*.txt"))
for file in pbar:
    pbar.set_description(file)
    time.sleep(0.5)
