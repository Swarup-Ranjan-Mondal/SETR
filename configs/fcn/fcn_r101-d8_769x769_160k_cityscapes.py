_base_ = './fcn_r50-d8_769x769_160k_cityscapes.py'
model = dict(pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101))
