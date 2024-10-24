# -*- coding: utf-8 -*-
"""DINO Training.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16z8wL8JS5G-ZyxNnOZ_bN-m9FlYcv_Zv
"""
import os, sys
import torch, json
import numpy as np
from PIL import Image
import datasets.transforms as T
from main import build_model_main
from util.slconfig import SLConfig
from datasets import build_dataset
from util.visualizer import COCOVisualizer
from util import box_ops
# Commented out IPython magic to ensure Python compatibility.

!git clone https://github.com/IDEA-Research/DINO.git
% cd DINO

pip install -r requirements.txt

!cd models/dino/ops && python setup.py build install && python test.py && cd ../../..
!python test.py
!cd ../../..

!bash scripts/DINO_train.sh /content/drive/MyDrive/COCODIR --pretrain_model_path /path/to/a/pretrianed/resnet50

model_config_path = "content/DINO/DINO_4scale.py" 
model_checkpoint_path = "content/MyDrive/COCODIR/Weights/checkpoint0049.pth" 
args = SLConfig.fromfile(model_config_path) 
args.device = 'cuda' 
model, criterion, postprocessors = build_model_main(args)
checkpoint = torch.load(model_checkpoint_path, map_location='cpu')
model.load_state_dict(checkpoint['model'])
_ = model.eval()

with open('util/coco_id2name.json') as f:
    id2name = json.load(f)
    id2name = {int(k):v for k,v in id2name.items()}


args.dataset_file = 'coco'
args.coco_path = "/content/MyDrive/COCODIR/" # the path of coco
args.fix_size = False

dataset_val = build_dataset(image_set='val', args=args)  
image, targets = dataset_val[0]
box_label = [id2name[int(item)] for item in targets['labels']]
gt_dict = {
    'boxes': targets['boxes'],
    'image_id': targets['image_id'],
    'size': targets['size'],
    'box_label': box_label,
}
vslzr = COCOVisualizer()
vslzr.visualize(image, gt_dict, savedir=None) 
output = model.cuda()(image[None].cuda())
output = postprocessors['bbox'](output, torch.Tensor([[1.0, 1.0]]).cuda())[0]
thershold = 0.3 # set a thershold

scores = output['scores']
labels = output['labels']
boxes = box_ops.box_xyxy_to_cxcywh(output['boxes'])
select_mask = scores > thershold
box_label = [id2name[int(item)] for item in labels[select_mask]]
pred_dict = {
    'boxes': boxes[select_mask],
    'size': targets['size'],
    'box_label': box_label
}
vslzr.visualize(image, pred_dict, savedir=None)
from PIL import Image
import datasets.transforms as T
image = Image.open("./figs/idea.jpg").convert("RGB") 

transform = T.Compose([
    T.RandomResize([800], max_size=1333),
    T.ToTensor(),
    T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])
image, _ = transform(image, None)
output = model.cuda()(image[None].cuda())
output = postprocessors['bbox'](output, torch.Tensor([[1.0, 1.0]]).cuda())[0]

thershold = 0.5 

vslzr = COCOVisualizer()

scores = output['scores']
labels = output['labels']
boxes = box_ops.box_xyxy_to_cxcywh(output['boxes'])
select_mask = scores > thershold
box_label = [id2name[int(item)] for item in labels[select_mask]]
pred_dict = {
    'boxes': boxes[select_mask],
    'size': torch.Tensor([image.shape[1], image.shape[2]]),
    'box_label': box_label
}
vslzr.visualize(image, pred_dict, savedir=None, dpi=100)