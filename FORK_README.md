# Preliminary Project Report

This repository is a fork from [https://github.com/bupt-ai-cz/LLVIP]. 

This project is for UofT CSC490 Capstone. 









TODO list DELETE LATER:

Group name
Team member names
Distribution of responsibilities in the group
Machine-vision problem you are addressing
Name and location of dataset you plan to use
How you plan to measure the accuracy of your system
Paper references(s)
Reasons, why you decided on this specific problem and dataset (longest section/paragraph of this report, one or two figures will be helpful).  For instance, the problem might
    represent an interesting or useful application. 
    present interesting technical challenges.
    involve an area of machine learning that you would like to gain more experience with.
    be on the cutting edge of what is possible.
    excite you for some other reason.
Who has started to access (download) the dataset?
Who is setting up the source code repository?
Distribution of tasks for this report
A link to your source code repository














Group Name: **UofT CSC490 LLVIP**
- [Amr Alomari](https://github.com/T3CHW1ZRD)
  Machine Learning 4th Y Undergrad@UofT
  Role / Responsibility
  - Machine Vision Engineer (Student)

- [Charles Cheung](https://github.com/charlescheung22)
  Machine Learning 4th Y Undergrad@UofT
  Role / Responsibility
  - Machine Vision Engineer (Student)


The goal of our project is perform object detection (on pedestrians), given pairs of pictures, in Visible and Infrared (VIR) light. 
- The dataset to be used is [LLVIP](https://github.com/bupt-ai-cz/LLVIP).
- System accuracy can be tested by splitting into the classing Train Verify Test data splits or just Train Test data splits. 
  
  $Recall = \frac{\text{True Positive}}{\text{True Positive} + \text{False Negative}}$ can also be tested. Mean Average Precision (mAP), Average Precision[small] (AP_small) can be attempted if there is additional time as these aren't vital.

Reference:
```
@inproceedings{jia2021llvip,
  title={LLVIP: A visible-infrared paired dataset for low-light vision},
  author={Jia, Xinyu and Zhu, Chuang and Li, Minzhen and Tang, Wenqi and Zhou, Wenli},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  pages={3496--3504},
  year={2021}
}
```


TODO REASONS

- Charles has accessed the dataset.
- Both are setting up source code.
- In general, TODO HERE
- Please find the repository at [this location](https://github.com/charlescheung22/LLVIP).







General TODO List:
- Get a Yolo v8 up and running



