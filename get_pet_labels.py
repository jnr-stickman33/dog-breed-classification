#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py

# Imports python modules
from os import listdir
import os
# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create
#       with this function

def get_pet_labels(image_dir):

    filenames = listdir(image_dir)
    pet_labels = []
    name = ""
    for idx in range(0, len(filenames), 1):
        if filenames[idx] != ".":
            name = filenames[idx]
            name = name.lower()
            word_list = name.split("_")
            name = ""
            for word in word_list:
                if word.isalpha():
                    name += word + " "
            name = name.strip()
            pet_labels.append(name)
    results_dic = dict()
    for idx in range(0, len(filenames), 1):
        if filenames[idx] not in results_dic:
            results_dic[filenames[idx]] = [pet_labels[idx]]
        else:
            return("** Warning: Key = ", filenames[idx], " already exists in results_dic with value = ", results_dic[filename[idx]])


    return results_dic # Replace None with the results_dic dictionary that you created with this
