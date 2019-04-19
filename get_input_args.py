#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py

# Imports python modules
import argparse


def get_input_args():  #TODO 1

    parser = argparse.ArgumentParser() # Create Parse using ArgumentParser
    # Create 3 command line arguments as mentioned above using add_argument() from ArguementParser method
    parser.add_argument("--dir", type = str, default = "pet_images/", help = "Requires path to image folder!")
    parser.add_argument("--arch", type = str, default = "vgg" , help = "Convolutional Neutral Network Architecture")
    parser.add_argument("--dogfile", type = str, default = "dognames.txt", help = "Needs path to the File containing dognames")

    # Replace None with parser.parse_args() parsed argument collection that
    # you created with this function
    return parser.parse_args()
