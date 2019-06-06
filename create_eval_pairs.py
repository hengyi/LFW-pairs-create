# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:13:28 2019

@author: yiheng
"""

import os
import random

#BASE_DIR='/home/share/test_pair'
#BASE_DIR='/home/share/train_data/64_CASIA-FaceV5/CASIA-FaceV5'
SAMPLE_NUM=2
CMP_EQUAL_NUM=300
CMP_RETRY_TIME=10
PWD = os.path.dirname(os.path.abspath(__file__))
print(PWD)
BASE_DIR = PWD
print(__file__)
PAIRS_FILE_PATH=os.path.join(PWD, 'ch_pairs.txt')
print(PAIRS_FILE_PATH)

def rand_300_equal(f, pic_dir):
    index = 0
    for d in pic_dir:
        index += 1         
        files_pic = os.listdir(os.path.join(BASE_DIR, d))
        if len(files_pic) == 1:
            continue
        
        print(files_pic)
        sl_2 = random.sample(files_pic, SAMPLE_NUM)
        print(sl_2)
        rint0 = files_pic.index(sl_2[0])
        rint1= files_pic.index(sl_2[1])
                     
        new_line = d + '	' + str(rint0) + '	' +  str(rint1) + '\n'
        print(new_line)
        f.write(new_line)
        
        if index == CMP_EQUAL_NUM:
            break
    
def rand_300_unequal(f, pic_dir):
    index = 0
    while True:
        index += 1         
        rd_dir = random.sample(pic_dir, 2)
        files_pic_1 = os.listdir(os.path.join(BASE_DIR, rd_dir[0]))
        files_pic_2 = os.listdir(os.path.join(BASE_DIR, rd_dir[1]))
        
        print(files_pic_1)
        print(files_pic_2)
        
        sl_1 = random.choice(files_pic_1)
        sl_2 = random.choice(files_pic_2)
        print(sl_1)
        print(sl_2)
        rint0 = files_pic_1.index(sl_1)
        rint1= files_pic_2.index(sl_2)
                     
        new_line = rd_dir[0] + '	' + str(rint0) + '	' +  rd_dir[1]  + '	'  + str(rint1) + '\n'
        print(new_line)
        f.write(new_line)
        
        if index == CMP_EQUAL_NUM:
            break

if __name__ == '__main__':
    files_tmp = os.listdir(BASE_DIR)
    print(files_tmp)
    
    pic_dir = [file for file in files_tmp if os.path.isdir(file)]
    print(pic_dir)
    
    pairs_head = str(CMP_RETRY_TIME) + '  ' + str(CMP_EQUAL_NUM) + '\n'
    with open(PAIRS_FILE_PATH, 'w+') as f:
#        f.write('10	300\n')
        f.write(pairs_head)
        for _ in range(CMP_RETRY_TIME):
            rand_300_equal(f, pic_dir)
            rand_300_unequal(f, pic_dir)
            

    
            
