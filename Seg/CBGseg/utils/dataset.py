#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: muyeby
@contact: bxf_hit@163.com
@site: http://muyeby.github.io
@software: PyCharm
@file: dataset.py
@time: 16-7-30 上午7:38
"""

from __future__ import print_function
import sys
import os
DATA_DIR = os.getcwd()+'/../train/'
TRAIN_FILE = DATA_DIR + 'data/hit_train.txt'
TRAIN_PLACE = DATA_DIR + 'train/placecontext.txt'
DATA_DICT = DATA_DIR + 'train/hit_training_words.txt'
DATA_DICT2 = DATA_DIR + 'train/pku_training_words.utf8'
DATA_DICT3 = DATA_DIR + 'train/vocab.utf8'
def read_dataset(filename=TRAIN_FILE):
    try:
        f2 =DATA_DIR+'test/HIT_test2.txt'
        fp = open(filename, 'r')
        # f = open(f2,'wb')
    except:
        print("Failed to open file.", file=sys.stderr)
        return

    dataset = []
    # i =0
    for line in fp:
        if sys.version < '3.0':
            if not (type(line) is unicode):
                try:
                    line = line.decode('utf-8')
                except:
                    line = line.decode('gbk', 'ignore')
        tokens = line.strip().split()
        tmp = (' '.join([t.rsplit('/', 1)[0] for t in tokens]))
        # if tmp:
        #     tt = ''.join([t.rsplit('/', 1)[0] for t in tokens])
        #     # f.write(tt.encode('utf-8')+"\n")
        if tmp:
            dataset.append(' '.join([t.rsplit('/', 1)[0] for t in tokens]))
    return dataset
def read_dataset2(filename = TRAIN_FILE):
    try:
        # f2 = DATA_DIR + 'HIT_test.txt'
        fp = open(filename, 'r')
        # f = open(f2,'wb')
    except:
        print("Failed to open file.", file=sys.stderr)
        return

    dataset = []
    # i =0
    for line in fp:
        if sys.version < '3.0':
            if not (type(line) is unicode):
                try:
                    line = line.decode('utf-8')
                except:
                    line = line.decode('gbk', 'ignore')
        tokens = line.strip().split()
        if tokens:
            dataset.append(' '.join(tokens))
            # print(tokens)
    return dataset
def read_dict():
    try:
        # f2 = DATA_DIR + 'HIT_test.txt'
        fp = open(DATA_DICT, 'r')
        f2 = open(DATA_DICT2,'r')
        f3 = open(DATA_DICT3,'r')
    except:
        print("Failed to open file.", file=sys.stderr)
        return
    dict_list = [fp,f2]
    idict ={}
    for fs in dict_list:
        for line in fs:
            if sys.version < '3.0':
                if not (type(line) is unicode):
                    try:
                        line = line.decode('utf-8')
                    except:
                        line = line.decode('gbk', 'ignore')
            word = line.strip().split('\t')[0].split(' ')[0]
            if(len(word)>1):
                idict[word] = 1

    fp.close()
    f2.close()
    f3.close()
    return idict

def get_pcon(filename = TRAIN_PLACE):
    tmpdict = {}
    try:
        f = open(filename,'rb')
    except:
        print("Failed to open file.", file=sys.stderr)
        return
    for line in f:
        if sys.version < '3.0':
            if not (type(line) is unicode):
                try:
                    line = line.decode('utf-8')
                except:
                    line = line.decode('gbk', 'ignore')
        word = line.strip()
        tmpdict[word] = 1
    return tmpdict