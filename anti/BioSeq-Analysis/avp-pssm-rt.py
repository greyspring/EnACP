# coding: utf-8
import os

import glob
def extracts(file1,drec):
    fname,filename = os.path.split(file1)

    if (not os.path.exists(drec + filename + "feature-PSSM-RT.csv")):
        print("PSSM-RT")
        os.system(
            "python2 profile.pyc " + file1 + " PSSM-RT  -out " + drec + filename + "feature-PSSM-RT.csv -f csv -cpu 20")
    else:
        print(filename, "PSSM-RT method has existed")
    if (not os.path.exists(drec + filename + "feature-SS.csv")):
        print("SS")
        os.system(
            "python2 ps.pyc " + file1 + " SS  -out " + drec + filename + "feature-SS.csv -f csv -cpu 20")
    else:
        print(filename, "PSSM-RT method has existed")
    # os.system("python2 ps.pyc " + filename +" SS -out aq.csv -f csv")

    #os.system("sh /cu02_nfs/gespring/data/newdata/de.sh")
    #os.system("sh /cu02_nfs/gespring/data/newdata/method-feature/de.sh")



# CS  Failure IOError: [Errno 2] No such file or directory: 'D:\\wt_neg-test.a.3.1.1_67851/1_cs.txt'
# os.system("python2 profile.pyc "+ filename+" CS -out aqqqqqqqq.csv -f csv")
# ps.pyc 2 methods
# SS    Failure  The method is only support Unix......
# os.system("python2 ps.pyc " + filename +" SS -out aq.csv -f csv")
# SASA  Failure  The lack of documents   python: can't open file 'D:\light\BioSeq-Analysis/SPIDER2_local/misc/pred_pssm.py'
# os.system("python2 ps.pyc " +filename+ " SASA -out aq.csv -f csv")


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


def alter(file,old_str,new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w") as f:
        f.write(file_data)
def extractfeatures(files,path):
    a = path+"/method-feature/"
    b = path+"/features/"
    mkd(a)
    mkd(b)
    for i in files:
        fname, filename = os.path.split(i)
        if(os.path.exists(b+filename+".csv")):
            print(filename,"已经存在")
        else:
            print i
            extracts(i,a)
            #merges(filename,a,b)
            

def merges(filename,path1,path2): #combine features
    #outputfilename=(filename+"feature-DP.csv",filename+"feature-AC.csv",filename+"feature-CC.csv",filename+"feature-ACC.csv",filename+"feature-PDT.csv",filename+"feature-PC-PseAAC.csv",filename+"feature-SC-PseAAC.csv",filename+"feature-PC-PseAAC-General.csv",filename+"feature-SC-PseAAC-General.csv",filename+"feature-Top-n-gram.csv",filename+"feature-PDT-Profile.csv",filename+"feature-DT.csv",filename+"feature-AC-PSSM.csv",filename+"feature-CC-PSSM.csv",filename+"feature-ACC-PSSM.csv",filename+"feature-PSSM-DT.csv",filename+"feature-PSSM-RT.csv")
    # outputfilename=(path1+filename+"feature-DP.csv",path1+filename+"feature-AC.csv",path1+filename+"feature-CC.csv",path1+filename+"feature-ACC.csv",path1+filename+"feature-PDT.csv",path1+filename+"feature-PC-PseAAC.csv",path1+filename+"feature-SC-PseAAC.csv",path1+filename+"feature-PC-PseAAC-General.csv",path1+filename+"feature-SC-PseAAC-General.csv",
    #   path1+filename+"feature-AC-PSSM.csv",path1+filename+"feature-Top-n-gram.csv",path1+filename+"feature-PDT-Profile.csv",path1+filename+"feature-CC-PSSM.csv",path1+filename+"feature-ACC-PSSM.csv",path1+filename+"feature-PSSM-DT.csv",path1+filename+"feature-PSSM-RT.csv")
    outputfilename=(path1+filename+"feature-DP.csv",path1+filename+"feature-AC.csv",path1+filename+"feature-CC.csv",path1+filename+"feature-ACC.csv",path1+filename+"feature-PDT.csv",path1+filename+"feature-PC-PseAAC.csv",path1+filename+"feature-SC-PseAAC.csv",path1+filename+"feature-PC-PseAAC-General.csv",path1+filename+"feature-SC-PseAAC-General.csv")

    #testFile = "neg-test.a.1.1.2.fasta"
    #outputfilename=(filename+"feature-DP.csv",)
    temp = path2+filename+".csv"
    import pandas as pd
    df1 = pd.read_csv(path1+filename+"feature-kmer.csv", encoding='utf-8')#读取第一个文件
    df2 = pd.read_csv(path1+filename+"feature-DR.csv", encoding='utf-8')#读取第二个文件
    outfile = pd.merge(df1, df2,  left_index=True, right_index=True)#文件合并
    outfile.to_csv(temp, index=False,encoding='utf-8')#输出文件

    for i in outputfilename:
        df1 = pd.read_csv(r""+i+"", encoding='utf-8')  # 读取第一个文件
        df2 = pd.read_csv(r""+temp+"", encoding='utf-8')  # 读取第二个文件

        outfile = pd.merge(df1, df2, left_index=True, right_index=True)  # 文件合并
        outfile.to_csv(r""+temp+"", index=False, encoding='utf-8')  # 输出文件
#f = matchfiles("D:/light/newdata","fasta")
path = "/cu02_nfs/gespring/data/Tyagi_datasets"
#path = "/cu02_nfs/gespring/data/ACPP_2015supp"
#path = "/cu02_nfs/gespring/data/ACPP_2015supp"
#path = "/cu02_nfs/gespring/data/ACP_2018"
#path = "/cu02_nfs/gespring/data/ACPred_FL_2018"
path = "/cu02_nfs/gespring/data/Avp"
path = "/cu02_nfs/gespring/data/avp-pssm-rt"
f = matchfiles(path,"fasta")
print f
#os.system("sh /cu02_nfs/gespring/data/newdata/de.sh")
#os.system("sh /cu02_nfs/gespring/data/newdata/method-feature/de.sh")
#f = matchfiles("C:/Users/fanfan/Desktop/bishe/SCOP167-superfamily/","pos-test.c.2.1.3.fasta")
extractfeatures(f,path)

