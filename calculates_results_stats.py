#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py

def calculates_results_stats(results_dic):

    results_stats_dic = dict()      # Creates empty dictionary for results_stats_dic

    results_stats_dic["n_dogs_img"] = 0        #Sets all counters to initial values of zero so that they can
    results_stats_dic["n_match"] = 0           # be incremented while processing through the images in results_dic
    results_stats_dic["n_correct_dogs"] = 0
    results_stats_dic["n_correct_notdogs"] = 0
    results_stats_dic["n_correct_breed"] = 0

    for key in results_dic:

        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

        if results_dic[key][2] == 1 and results_dic[key][3] == 1:
            results_stats_dic['n_correct_breed'] += 1

        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1

            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1

        else:
            results_stats_dic['n_correct_notdogs'] += 1


    results_stats_dic['n_images'] = len(results_dic)

    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] - results_stats_dic['n_dogs_img'])

    if results_stats_dic['n_images'] != 0:
        results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100.0
    else:
        results_stats_dic['pct_match'] = 0.0

    if results_stats_dic['n_dogs_img'] != 0:
        results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_dogs'] = 0.0

    if results_stats_dic['n_dogs_img'] != 0:
        results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_breed'] = 0.0

    if results_stats_dic['n_notdogs_img'] != 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0


    return results_stats_dic
