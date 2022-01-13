from pathlib import Path
import os
from glob import glob
import shutil

if __name__ == '__main__':
    dataset_path = Path("./datasets/endoscopy")
    train_a_path = dataset_path / "trainA"
    train_b_path = dataset_path / "trainB"
    train_a_path.mkdir(parents=True,exist_ok=True)
    train_b_path.mkdir(parents=True,exist_ok=True)
    gan_data_path = Path("../BladderDepthEstimation/datasets/gan_data")
    synth_data_path = Path("../BladderDepthEstimation/datasets/depth_data")
    max_imgs = 10000
    for idx,file in enumerate(synth_data_path.rglob("./*/*.png")):
        shutil.copy(file,train_a_path/("synth-"+str(idx)+".png"))
        if idx >max_imgs:
            break
    for idx,file in enumerate(gan_data_path.rglob("./train/*.png")):
        shutil.copy(file,train_b_path/("gan-"+str(idx)+".png"))
        if idx >max_imgs:
            break
    
        
    