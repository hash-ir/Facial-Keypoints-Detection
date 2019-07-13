from torch.utils.data import Dataset, DataLoader
import matplotlib.image as mpimg
import pandas as pd
import os
import numpy as np

class FacialKeypointsDataset(Dataset):
    """Face Landmarks dataset."""

    def __init__(self, csv_file, transform=None):
        self.key_pts_frame = pd.read_csv(csv_file)
        self.key_pts_frame.dropna(inplace=True)
        self.key_pts_frame.reset_index(drop=True, inplace=True)
        self.transform = transform

    def __len__(self):
        return len(self.key_pts_frame)

    def __getitem__(self, idx):
        image_string = self.key_pts_frame.loc[idx]['Image']
        image_array = np.array([int(item) for item in image_string.split()]).reshape(-1, 96, 96).astype(np.float32)
#         print(image_array.shape)
        sample = {}
        sample['image'] = image_array
        sample['keypoints'] = self.key_pts_frame.loc[idx].values[:-1].reshape(15, 2).astype(np.float32)

        if self.transform:
            sample = self.transform(sample)

        return sample

