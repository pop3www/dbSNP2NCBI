#!/bin/bash

echo "install dbSNP_NCBI_env"
conda remove --name dbSNP_NCBI --all -y
conda env create -f environment.yml -y
source activate dbSNP_NCBI
conda list
