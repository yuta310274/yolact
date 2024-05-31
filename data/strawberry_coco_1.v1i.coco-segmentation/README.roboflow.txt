
strawberry_coco_1 - v1 2022-09-24 7:58pm
==============================

This dataset was exported via roboflow.com on September 24, 2022 at 10:58 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

It includes 1058 images.
Strawberry are annotated in COCO Segmentation format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise
* Random rotation of between -15 and +15 degrees
* Random brigthness adjustment of between -25 and +25 percent


