
import os
import fastavro
import reader,schema

path ="/home/jiayachong/avrome/util/datacreated/users.avro"
def gen_cell_meta_valuetest(path):
    scan_result_list=[]
    files=os.listdir(path)
    for file in  files:
        file_name=os.path.splitext(file)[0]
        print(file_name)
        if file_name.count('cell_decision')>0:
            avro_reader=reader(open(file_name,"rb"))
        else:
            avro_reader=None
        for scan_result in avro_reader:
            scan_result_list.append(scan_result)
