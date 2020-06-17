# Facial Keypoints Detection

A real-time implementation of facial keypoints detection made with `PyTorch` and `OpenCV`. Visit [here](https://www.kaggle.com/c/facial-keypoints-detection/) for more details about the dataset used for the training. 

## Quick Start
### Install
1. Clone the repository
```bash
git clone https://github.com/hash-ir/Facial-Keypoints-Detection.git
cd Facial-Keypoints-Detection
```
2. For running the IPython notebook `Facial Keypoints.ipynb` the following tools are required:
* [PyTorch](https://pytorch.org/get-started/locally/)
* [Open CV](https://pypi.org/project/opencv-python/)
* [Pandas](https://pandas.pydata.org/pandas-docs/stable/install.html)

An alternate is to make a conda environment from the `environment.yaml` file included in the repository:
```bash
conda env create -f environment.yaml
```
3. Once the dependencies are installed, replace the path of `haarcascade_frontalface_default.xml` with your path:
```bash
/home/<username>/anaconda3/lib/python3.x/site-packages/cv2/data/haarcascade_frontalface_default.xml # linux
```
```bash
C:\Users\<username>\Anaconda3\envs\<envname>\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml # windows
```


### Usage
1. For training, download the dataset from [here](https://www.kaggle.com/c/facial-keypoints-detection/data), extract and put `training.csv` and `test.csv` in the root directory.
2. For testing, execute the first cell, network architecture code cell and last two code cells. Real-time testing requires webcam!

## Demo
A real-time demo of me testing it out is [here](https://drive.google.com/open?id=1gb2E10oJCGY6gujHmmworcl8Pqvfor2k)

I have used a fairly simple model and a small dataset (around 1500 samples). Next steps are to incorporate a bigger model and use a bigger dataset and/or data augmentation

## Author(s)
* **Hashir Ahmad** - *full project* - [GitHub](https://github.com/hash-ir)

## License
This work is licensed under the [MIT License](https://github.com/hash-ir/Facial-Keypoints-Detection/blob/master/LICENSE).
