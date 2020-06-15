# coding: utf-8
import os
import pandas as pd
import glob
import sys
def extracts(file1,drec):
    fname,filename = os.path.split(file1)

    # nac.pyc 3 methods
    if (not os.path.exists(drec + filename + "feature-kmer.csv")):
        print("Kmer method")
        os.system("python2       nac.pyc " + file1 + " Protein Kmer -out " + drec + filename + "feature-kmer.csv -f csv")
    else:
        pass

    if (not os.path.exists(drec + filename + "feature-DR.csv")):
        print("DR method")
        os.system("python2       nac.pyc " + file1 + " Protein DR -out " + drec + filename + "feature-DR.csv -f csv")
    else:
        pass

    if (not os.path.exists(drec + filename + "feature-DP.csv")):
        print("DP method")
        os.system("python2       nac.pyc " + file1 + " Protein DP  -out " + drec + filename + "feature-DP.csv -f csv")
    else:
        pass

    # acc.pyc 8 methods
    if (not os.path.exists(drec + filename + "feature-AC.csv")):
        print("AC")
        os.system("python2       acc.pyc " + file1 + " Protein AC -out " + drec + filename + "feature-AC.csv -f csv")
    else:
        pass

    if (not os.path.exists(drec + filename + "feature-CC.csv")):
        print("CC")
        os.system("python2       acc.pyc " + file1 + " Protein CC -out " + drec + filename + "feature-CC.csv -f csv")
    else:
        pass

    if (not os.path.exists(drec + filename + "feature-ACC.csv")):

        print("ACC")
        os.system("python2       acc.pyc " + file1 + " Protein ACC -out " + drec + filename + "feature-ACC.csv -f csv")
    else:
        pass

    if (not os.path.exists(drec + filename + "feature-PDT.csv")):

        print("PDT")
        os.system("python2       acc.pyc " + file1 + " Protein PDT -out " + drec + filename + "feature-PDT.csv -f csv")
    else:
        pass

    if (not os.path.exists(drec + filename + "feature-PC-PseAAC.csv")):

        print("PC-PseAAC")
        os.system(
            "python2       pse.pyc " + file1 + " Protein PC-PseAAC -out " + drec + filename + "feature-PC-PseAAC.csv -f csv")
    else:
        pass

    if (not os.path.exists(drec + filename + "feature-SC-PseAAC.csv")):

        print("SC-PseAAC")
        os.system(
            "python2       pse.pyc " + file1 + " Protein SC-PseAAC -out " + drec + filename + "feature-SC-PseAAC.csv -f csv")
    else:
        pass

    if (not os.path.exists(drec + filename + "feature-PC-PseAAC-General.csv")):

        print("PC-PseAAC-General")
        os.system(
            "python2       pse.pyc " + file1 + " Protein PC-PseAAC-General -out " + drec + filename + "feature-PC-PseAAC-General.csv -f csv")
    else:
        pass

    if (not os.path.exists(drec + filename + "feature-SC-PseAAC-General.csv")):

        print("SC-PseAAC-General")
        os.system(
            "python2       pse.pyc " + file1 + " Protein SC-PseAAC-General -out " + drec + filename + "feature-SC-PseAAC-General.csv -f csv")
    else:
        pass
    #profile.pyc 9 methods

    if (not os.path.exists(drec + filename + "feature-AC-PSSM.csv")):
        print("AC-PSSM ")
        os.system(
            "python2       profile.pyc " + file1 + " AC-PSSM -out " + drec + filename + "feature-AC-PSSM.csv -f csv -cpu 20")
    else:
        pass
        #print(filename, "AC-PSSM method has existed")

    if (not os.path.exists(drec + filename + "feature-Top-n-gram.csv")):
        print("Top-n-gram")
        os.system(
            "python2 profile.pyc  " + file1 + " Top-n-gram -out " + drec + filename + "feature-Top-n-gram.csv -f csv -n 2 -cpu 20")
    else:
        pass
        #print(filename, "Top-n-gram method has existed")

    if (not os.path.exists(drec + filename + "feature-PDT-Profile.csv")):
        print("PDT-Profile")
        os.system(
            "python2 profile.pyc " + file1 + " PDT-Profile -out " + drec + filename + "feature-PDT-Profile.csv -f csv -n 2 -cpu 20")
    else:
        pass
        #print(filename, "PDT-Pofile method has existed")

    if (not os.path.exists(drec + filename + "feature-CC-PSSM.csv")):

        print("CC-PSSM")
        os.system(
            "python2 profile.pyc " + file1 + " CC-PSSM -out " + drec + filename + "feature-CC-PSSM.csv -f csv -cpu 20")
    else:
        pass
        #print(filename, "CC-PSSM method has existed")

    if (not os.path.exists(drec + filename + "feature-ACC-PSSM.csv")):
        print("ACC-PSSM")
        os.system(
            "python2 profile.pyc " + file1 + " ACC-PSSM -out " + drec + filename + "feature-ACC-PSSM.csv -f csv -cpu 20")
    else:
        pass
        #print(filename, "ACC-PSSM method has existed")

    if (not os.path.exists(drec + filename + "feature-PSSM-DT.csv")):
        print("PSSM-DT")
        os.system(
            "python2 profile.pyc " + file1 + " PSSM-DT -out " + drec + filename + "feature-PSSM-DT.csv -f csv -cpu 20")
    else:
        pass
        #print(filename, "PSSM-DT method has existed")

    if (not os.path.exists(drec + filename + "feature-PSSM-RT.csv")):
        print("PSSM-RT")
        os.system(
            "python2 profile.pyc " + file1 + " PSSM-RT  -out " + drec + filename + "feature-PSSM-RT.csv -f csv -cpu 20")
    else:
        pass
        #print(filename, "PSSM-RT method has existed")

    if (not os.path.exists(drec + filename + "feature-DT.csv")):
        print("DT")
        os.system("python2 profile.pyc " + file1 + " DT -out " + drec + filename + "feature-DT.csv -f csv -cpu 20")
    else:
        pass

def matchfiles(tmpdir,suffix):  # 读取文件路径
    ###windows os
    # f = glob.glob(tmpdir + '\\*.' + suffix)
    ###linux os
    fi = []
    filenames = []
    #f = glob.glob(tmpdir + suffix)
    f = glob.glob(tmpdir + '/*.' + suffix)
    return f
    # fileout = open(dir + '\\' + suffix + '.txt','wt')
    #
    # for tmpfile in f:
    #     fname, modfasta_filename = os.path.split(tmpfile)
    #     print modfasta_filename
    #     filenames.append(modfasta_filename)
    # fi.append(filenames)
    # return fi
def mkd(x):
    if(os.path.exists(x)):
        pass
    else:
        os.makedirs(x)
def extractfeatures(files,path):
    path_,filename = os.path.split(path)
    # a = path+"/method-feature/"
    b = "../Input_data/Input_data_feature"+"/"+filename+"/"
    # mkd(a)
    mkd(b)
    for i in files:
        extracts(i,b)

def main(argv):
    path = argv[1]
    f = matchfiles(path,"fasta")
    extractfeatures(f,path)

if __name__ == '__main__':
	main(sys.argv)

#f = matchfiles("C:/Users/fanfan/Desktop/bishe/SCOP167-superfamily/","pos-test.c.2.1.3.fasta")

