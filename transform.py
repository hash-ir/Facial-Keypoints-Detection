import torch
import torch.functional as F
import random

class Normalize(object):
    def __call__    (self, sample):
        image, key_pts = sample['image'], sample['keypoints']
        image /= 255.
        key_pts = key_pts - 48
        key_pts = key_pts.reshape(-1, 2)/48.

        return {'image': image, 'keypoints': key_pts}

class ToTensor(object):
    def __call__(self, sample):
        image, key_pts = sample['image'], sample['keypoints']
        
        return {'image': torch.from_numpy(image).float(),
                'keypoints': torch.from_numpy(key_pts).float()}