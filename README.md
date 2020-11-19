# hw2 -- Object Detection
## data
- dataset: Street View House Numbers
  
- link: http://ufldl.stanford.edu/housenumbers/

- data preprocessing

  Move you data into `data/custom/train`, if you have validation data, move it to `data/custom/valid`.
  Create a file to `data/custom/train.txt` that contain the training image path, if you have validation data, also create a file named `valid.txt`.
  The annotations are save in .h5 file, run `python3 datapreprocessing.py` and you can turn it to txt files.
  One image corresponds to one txt file, each txt files row contain `label_idx x_center y_center width height`
  The coordinates should be scaled [0, 1], and the label_idx should be zero-indexed and correspond to the row number of the class name in data/custom/classes.names.
  
 - class
   Add class names to data/custom/classes.names. This file should have one row per class name.

## model
- create custom model

  Install the requirements from the link https://github.com/eriklindernoren/PyTorch-YOLOv3
  
  Run the commands below to create a custom model definition, replacing <num-classes> with the number of classes in your dataset. In this project <num-classes>=10
  
   ` $ cd config/`
   
   ` $ bash create_custom_model.sh <num-classes>`
   
   then you will get  `config/yolov3-custom.cfg` and `config/custom.data`
   
 
## train
- run `$ python3 train.py` 

  you can change epoch, weight, model...

  In this project, model_def = "config/yolov3-custom.cfg", data_config = "config/custom.data"

- tensorboard

  Training history is in  `logs/` , run the command below.

  `$ tensorboard --logdir='logs' --port=6006`
  
 - checkpoints
 
   In checkpoints folder, it contains each epoch training weight.
   
  
## detect
- detect object from the test images

  put test images to `data/samples/images`, after running `$ python3 detect.py`, in output folder it contains images with bounding box and predict.json.

  you can choose weight from checkpoint floder, or conf_thrs and nms_thrs to get the result more accurate.
  
- example:

  ![image](https://github.com/shenhsinyu/hw2/blob/main/output/1.png)
 
  
