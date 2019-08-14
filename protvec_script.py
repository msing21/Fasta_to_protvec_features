#!/usr/bin/env python3

import biovec
import os,sys,argparse
import pandas as pd
import time

pv2 = biovec.models.load_protvec('/home/manali/mymolecules/Drug-Bank-data/FASTA-Training/biovec-master/trained_models/swissprot-reviewed.model')

def fastaflat_to_features(filename):
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                f1 = word
                pv3 = pv2.to_vecs(f1)
                new_series = pd.DataFrame(pv3)
                new_series.to_csv('test_m.csv', index=None)
                

def getArgs():
    parser = argparse.ArgumentParser('python')
    parser.add_argument('-infile', required=True)
    return parser.parse_args()

if __name__ == "__main__":
    args = getArgs()
    filename = fastaflat_to_features(args.infile)
    start = time.time()
    end = time.time()
    print ('time elapsed:' + str(end - start))
    
