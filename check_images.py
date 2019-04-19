#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py

# Imports python modules
from time import time, sleep
import time

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():

    start_time = time.time()

    in_arg = get_input_args()

    # Function that checks command line arguments using in_arg
    check_command_line_arguments(in_arg)
###############################################################################


    results = get_pet_labels(in_arg.dir)

    # Function that checks Pet Images in the results Dictionary using results
    check_creating_pet_image_labels(results)
################################################################################


    classify_images(in_arg.dir, results, in_arg.arch)

    # Function that checks Results Dictionary using results
    check_classifying_images(results)
################################################################################


    adjust_results4_isadog(results, in_arg.dogfile)

    # Function that checks Results Dictionary for is-a-dog adjustment using results
    check_classifying_labels_as_dogs(results)
################################################################################


    results_stats = calculates_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    check_calculating_results(results, results_stats)
################################################################################


    print_results(results, results_stats, in_arg.arch, True, True)

    end_time = time.time()


    tot_time = (end_time - start_time)#calculate difference between end time and start time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )


# Call to main function to run the program
if __name__ == "__main__":
    main()
