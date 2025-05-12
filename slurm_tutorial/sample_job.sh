#!/bin/bash
#SBATCH --job-name=sample
#SBATCH --output=output.log
#SBATCH --ntasks=1
#SBATCH --time=01:00:00
#SBATCH --mem=8G

python sample.py