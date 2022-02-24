#! /bin/sh
chmod +x ./bedGraphToBigWig

python3 script.py

sort -k1,1 -k2,2n 100_bin_corr.bed > 100_bin_corr_sorted.bed
sort -k1,1 -k2,2n 1000_bin_corr.bed > 1000_bin_corr_sorted.bed
sort -k1,1 -k2,2n 10000_bin_corr.bed > 10000_bin_corr_sorted.bed
sort -k1,1 -k2,2n 100000_bin_corr.bed > 100000_bin_corr_sorted.bed
sort -k1,1 -k2,2n 1000000_bin_corr.bed > 1000000_bin_corr_sorted.bed

./bedGraphToBigWig 100_bin_corr_sorted.bed hg19.chrom.sizes 100_bin_BigWig.bw
./bedGraphToBigWig 1000_bin_corr_sorted.bed hg19.chrom.sizes 1000_bin_BigWig.bw
./bedGraphToBigWig 10000_bin_corr_sorted.bed hg19.chrom.sizes 10000_bin_BigWig.bw
./bedGraphToBigWig 100000_bin_corr_sorted.bed hg19.chrom.sizes 100000_bin_BigWig.bw
./bedGraphToBigWig 1000000_bin_corr_sorted.bed hg19.chrom.sizes 1000000_bin_BigWig.bw
