#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py

# Imports classifier function for using CNN to classify images
from classifier import classifier

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function.
#       Notice that this function doesn't return anything because the
#       results_dic dictionary that is passed into the function is a mutable
#       data type so no return is needed.
#
def classify_images(images_dir, results_dic, model):

    for key in results_dic: #TODO 3a
        model_label = classifier(images_dir + key, model)
        model_label = model_label.lower().strip()
        truth = results_dic[key][0] #Image Label

        if truth in model_label:
            results_dic[key].extend((model_label, 1)) #TODO 3c
        else:
            results_dic[key].extend((model_label, 0)) #TODO 3d
