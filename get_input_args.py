#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Derick visagie
# DATE CREATED:  24-3-2019                                 
# REVISED DATE: 
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
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

