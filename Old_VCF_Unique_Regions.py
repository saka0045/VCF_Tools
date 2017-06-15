#!/usr/local/biotools/python/2.7.3/bin/python

import sys, os, argparse, re
from os.path import basename

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--oldvcf",
                        dest='old_vcf',
                        required=True,
                        help="Old VCF File")
    #parser.add_argument("-c", "--cavavcf",
                        dest='cava_vcf',
                        required=True,
                        help="CAVA VCF File")
    args = parser.parse_args()

def parse_old_vcf(old_vcf):
    old_vcf_dict = {}
    old_vcf_file = (open(old_vcf, 'r').readline()[2:])
    for eachline in old_vcf_file:
        row = eachline.split('\t')
        chr = row[0]
        position = row[1]
        old_vcf_dict[chr] = position
    return old_vcf_dict

if __name__ == '__main__':
    main()
    parse_old_vcf()
    print(old_vcf_dict)
