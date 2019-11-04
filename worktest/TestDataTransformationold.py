
import os
import fastavro
import csv
import schema,glob,reader
# from socket import socket
# from api_operations import get_operator_result, put_classifier_result, get_datasets
# from encryption import PyCrypt
# from spark_operations import spark_detect_columns, spark_persist_data, close_instance
# from app_config import Config
# from utility import copy_file
# from spark_connection import SparkConnection

class Fib(object):
    # //users.avro
    avro_path ="/home/jiayachong/avrome/util/datacreated/users.avro"
# def gen_cell_meta_valuetest(avro_path):
#     if os.path.isdir(avro_path):
#         path=avro_path+'/*.avro'
#         for filename in glob.glob(path):
#             avro_reader=reader(open(filename,"rb"))
#     else:
#         avro_reader=reader(open(avro_path,"rb"))
#     scan_result_list=[]
#     for scan_result in avro_reader:
#         print(scan_result)
#         scan_result_list.append(scan_result)
#
# gen_cell_meta_valuetest(path)

    def __call__(self, num, *args, **kwargs):
        n, m, lst = 0, 1, []

        for i in range(num):
            lst.append(n)
            n, m = m, n + m

        return lst

    if os.path.isdir(avro_path):
        path=avro_path+'/*.avro'
    for filename in glob.glob(avro_path):
        avro_reader=reader(open(filename,'rb'))
        # pass
    else:
        avro_reader=reader(open(avro_path,'rb'))
        scan_result_list=[]
        for scan_result in avro_reader:
            print(scan_result)

            scan_result_list.append(scan_result)

