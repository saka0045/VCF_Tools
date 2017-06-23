#!/usr/local/biotools/python/2.7.3/bin/python

import sys, os, argparse, re
from os.path import basename

def main():
    #argparser
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--oldvcf",
                        dest='old_vcf',
                        required=True,
                        help="Old VCF File")
    parser.add_argument("-c", "--cavavcf",
                        dest='cava_vcf',
                        required=True,
                        help="CAVA VCF File")

    args = parser.parse_args()

    #setting up the programs
    old_vcf_dict = parse_old_vcf(args.old_vcf)
    cava_vcf_dict = parse_cava_vcf(args.cava_vcf)
    old_unique_region_file = "./Old_Unique_Regions"
    compare_vcf(old_vcf_dict, cava_vcf_dict, old_unique_region_file)

def parse_old_vcf(old_vcf):
    #parse the old_vcf file and store chr number and genomic coordinates
    old_vcf_dict = {}
    old_vcf_file = (open(old_vcf, 'r')).readlines()[8:]
    for eachline in old_vcf_file:
        row = eachline.split('\t')
        chr = row[0]
        position = row[1]
        old_vcf_dict[position] = chr

    return old_vcf_dict

def parse_cava_vcf(cava_vcf):
    #parse the CAVA vcf and store chr number and genomic coordinates
    cava_vcf_dict = {}
    cava_vcf_file = (open(cava_vcf, 'r')).readlines()[8:]
    for eachline in cava_vcf_file:
        row = eachline.split('\t')
        chr = row[0]
        position = row[1]
        cava_vcf_dict[position] = chr

    return cava_vcf_dict

def compare_vcf(old_vcf_dict, cava_vcf_dict, old_unique_region_file):
    #Compare the two VCFs and report out regions only showing in the old vcf
    old_vcf_region = set(old_vcf_dict.keys())
    cava_vcf_region = set(cava_vcf_dict.keys())
    different_region = old_vcf_region.difference(cava_vcf_region)
    sorted_different_region = sorted(different_region, key=lambda region: float(region))
    outputfile = open(old_unique_region_file, 'w')
    
    for region in sorted_different_region:
        outputfile.write(old_vcf_dict[region])
        outputfile.write("\t")
        outputfile.write(region)
        outputfile.write("\n")
    outputfile.close()

    print("Done Comparing. File saved as Old_Unique_Regions")


main()
