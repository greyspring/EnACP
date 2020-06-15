import os
def extracts(filename):

    #profile.pyc 9 methods
    print("AC-PSSM ")
    os.system("python2 profile.pyc " + filename +" AC-PSSM -out "+filename+"feature-AC-PSSM.csv -f csv -cpu 20 ")

# CS  Failure IOError: [Errno 2] No such file or directory: 'D:\\wt_neg-test.a.3.1.1_67851/1_cs.txt'
#os.system("python2 profile.pyc "+ filename+" CS -out aqqqqqqqq.csv -f csv")
# ps.pyc 2 methods
# SS    Failure  The method is only support Unix......
# os.system("python2 ps.pyc " + filename +" SS -out aq.csv -f csv")
# SASA  Failure  The lack of documents   python: can't open file 'D:\light\BioSeq-Analysis/SPIDER2_local/misc/pred_pssm.py'
# os.system("python2 ps.pyc " +filename+ " SASA -out aq.csv -f csv")

extracts("pos-trains.txt")

