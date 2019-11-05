import sys
import logging
import json
import os
import glob
import re
import pathlib
from fastavro import writer, reader, schema

# path_avro_file='C:\\Users\\yacjia\\soft\\data\\classifier\\result-new-type'

# files = os.listdir(path_avro_file)
# scan_result_lst = []
# for file in files:
#     file_name = os.path.splitext(file)[0]
#     if file_name.count('cell_decision') > 0:
#         avro_reader = reader(open(file_name, "rb"))
#     else:
#         avro_reader = None
#     print(os.path.splitext(file)[0])
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
    path_avro_file='/home/jiayachong/avrome/work/parsing-cell-path'

    scan_result_lst = []
    print('----cell_avro_path:-------')
    print(path_avro_file)
    if os.path.isdir(path_avro_file):
        files = os.listdir(path_avro_file)
        path = path_avro_file + '/*cell_decision.avro'
        for filename in glob.glob(path):
            print("--file_full_path--: " + filename)
            avro_reader = reader(open(filename, "rb"))
            for scan_result in avro_reader:
                scan_result_lst.append(scan_result)
    else:
        avro_reader = reader(open(path_avro_file, "rb"))
        for scan_result in avro_reader:
            scan_result_lst.append(scan_result)


    print('-----------------------------------------------------------------')
    for record in scan_result_lst:
        print(record)
    print(len(scan_result_lst))

#     print("""
#
# 72.acct_id.cell_decision.avro        72.countryCode.post_decision.avro  72.ip_addr.post_decision.avro
# 72.acct_id.post_decision.avro        72.countryCode.pre_decision.avro   72.ip_addr.pre_decision.avro
# 72.acct_id.pre_decision.avro         72.country.post_decision.avro      72.key_info.cell_decision.avro
# 72.age_info.cell_decision.avro       72.country.pre_decision.avro       72.key_info.post_decision.avro
# 72.age_info.post_decision.avro       72.data_info.cell_decision.avro    72.key_info.pre_decision.avro
# 72.age_info.pre_decision.avro        72.data_info.post_decision.avro    72.name_info.cell_decision.avro
# 72.birthday.cell_decision.avro       72.data_info.pre_decision.avro     72.name_info.post_decision.avro
# 72.birthday.post_decision.avro       72.email.cell_decision.avro        72.name_info.pre_decision.avro
# 72.birthday.pre_decision.avro        72.email_info.cell_decision.avro   72.phone.cell_decision.avro
# 72.car_number.cell_decision.avro     72.email_info.post_decision.avro   72.phone_info.cell_decision.avro
# 72.car_number.post_decision.avro     72.email_info.pre_decision.avro    72.phone_info.post_decision.avro
# 72.car_number.pre_decision.avro      72.email.post_decision.avro        72.phone_info.pre_decision.avro
# 72.company_addr.cell_decision.avro   72.email.pre_decision.avro         72.phone.post_decision.avro
# 72.company_addr.post_decision.avro   72.family_addr.cell_decision.avro  72.phone.pre_decision.avro
# 72.company_addr.pre_decision.avro    72.family_addr.post_decision.avro  72.product_info.cell_decision.avro
# 72.company.cell_decision.avro        72.family_addr.pre_decision.avro   72.product_info.post_decision.avro
# 72.company_name.cell_decision.avro   72.family_name.cell_decision.avro  72.product_info.pre_decision.avro
# 72.company_name.post_decision.avro   72.family_name.post_decision.avro  72.runoob_author.cell_decision.avro
# 72.company_name.pre_decision.avro    72.family_name.pre_decision.avro   72.runoob_author.post_decision.avro
# 72.company_phone.cell_decision.avro  72.full_name.cell_decision.avro    72.runoob_author.pre_decision.avro
# 72.company_phone.post_decision.avro  72.full_name.post_decision.avro    72.runoob_title.cell_decision.avro
# 72.company_phone.pre_decision.avro   72.full_name.pre_decision.avro     72.runoob_title.post_decision.avro
# 72.company.post_decision.avro        72.gender.cell_decision.avro       72.runoob_title.pre_decision.avro
# 72.company.pre_decision.avro         72.gender.post_decision.avro       configFile
# 72.country.cell_decision.avro        72.gender.pre_decision.avro        input.avro
# 72.countryCode.cell_decision.avro    72.ip_addr.cell_decision.avro      _SUCCESS
#
#     """)