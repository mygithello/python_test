import sys
import logging
import json
import os
import glob
import re
import pathlib

import  reader, schema
import writer
import fastavro

path_avro_file='C:\\Users\\yacjia\\soft\\data\\classifier\\result-new-type'
files = os.listdir(path_avro_file)
scan_result_lst = []
for file in files:
    file_name = os.path.splitext(file)[0]
    if file_name.count('cell_decision') > 0:
        avro_reader = reader(open(file_name, "rb"))
    else:
        avro_reader = None
    print(os.path.splitext(file)[0])
    # for scan_result in avro_reader:
    #     print(scan_result)
    #     scan_result_lst.append(scan_result)

    # if os.path.isfile(file):
    #     file_name = os.path.splitext(file)[0]
    #
    #

    # if os.path.isdir(path_avro_file):
    #     path = path_avro_file + '/*.avro'
    #     for filename in glob.glob(path):
    #         avro_reader = reader(open(filename, "rb"))
    # else:
    #     avro_reader = reader(open(path_avro_file, "rb"))
    # scan_result_lst = []
    # for scan_result in avro_reader:
    #     scan_result_lst.append(scan_result)


    print("--------------------new----------------------")

    scan_result_lst = []
    print('----path_avro_file:-------')
    print(path_avro_file)
    if os.path.isdir(path_avro_file):
        files = os.listdir(path_avro_file)
        for eachfile in files:
            path = path_avro_file + '/*cell_decision.avro'
            for filename in glob.glob(path):
                print("--filename--: " + filename)
                avro_reader = reader(open(filename, "rb"))
                for scan_result in avro_reader:
                    scan_result_lst.append(scan_result)
                print(len(scan_result_lst))
    else:
        avro_reader = reader(open(path_avro_file, "rb"))
        for scan_result in avro_reader:
            scan_result_lst.append(scan_result)