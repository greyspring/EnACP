import os
import sys
sys.path.append("/home/gespring/venv/Lib/site-packages")
def extracts(filename):
    #nac.pyc 3 methods
    print("Kmer method")
    os.system("python2 nac.pyc " + filename +" Protein Kmer -out "+filename+"feature-kmer.csv -f csv")
filename = 'pos-trains.txt'
extracts(filename)