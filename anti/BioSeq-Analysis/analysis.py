if __name__ == '__main__':
    import sys
    sys.dont_write_bytecode = True
    import argparse
    import subprocess
    from argparse import RawTextHelpFormatter
    parse = argparse.ArgumentParser(description="The analysis module for training a best classifier",
                                    formatter_class=RawTextHelpFormatter)
    parse.add_argument('inputfiles', nargs='*',
                       help="The input files in FASTA format.More than one file could be input.")
    parse.add_argument('-out', nargs='*',
                       help="The output files used for storing results. The number of output files should be the "
                            "same as that of input files.")
    parse.add_argument('alphabet', choices=['DNA', 'RNA', 'Protein'],
                       help="The alphabet of sequences.")
    parse.add_argument('-method', type=str, nargs='*',
                       help="The method names. You can input several methods. The vector of each method implements "
                            "linear merging. Up to 3 methods.")
    parse.add_argument('-n', type=int, nargs='*',
                       help="The maximum distance between structure statuses, (default is from 1 to 4). "
                            "It works with PseDPC method. Or for Top-n-gram, PDT-Profile methods. The value of "
                            "top-n-gram (default is from 1 to 2).If there are several methods, enter the ranges "
                            "in turn.")
    parse.add_argument('-lag', type=int, nargs='*',
                       help="The value of lag. For ACC-PSSM, AC-PSSM and CC-PSSM methods. The value of lag "
                            "(default is from 1 to 7). If there are several methods, enter the ranges in turn.")
    parse.add_argument('-oli', type=int, choices=[0, 1], nargs='*',
                       help="Choose one kind of Oligonucleotide: 0 represents dinucleotide, default;1 represents "
                            "trinucleotide.For DAC, DCC, DACC, TAC, TCC, TACC, MAC, GAC, NMBAC, AC, CC, ACC methods.")
    parse.add_argument('-lamada', type=int, nargs='*',
                       help="The value of lamada. For PseDNC, PseKNC, PC-PseDNC-General, PC-PseTNC-General, "
                            "SC-PseDNC-General, SC-PseTNC-General, PC-PseAAC-General, SC-PseAAC-General, PC-PseAAC, "
                            "SC-PseAAC, MAC, PDT, PDT-Profile, GAC, NMBAC methods (default is from 1 to 7). "
                            "If there are several methods, enter the ranges in turn.")
    parse.add_argument('-w', type=float, nargs='*',
                       help="The weight factor used to adjust the effect of the correlation factors. For PseSSC, "
                            "PseDNC, PseKNC, PC-PseDNC-General, PC-PseTNC-General, SC-PseDNC-General, "
                            "SC-PseTNC-General, PC-PseAAC-General, SC-PseAAC-General, PC-PseAAC, "
                            "SC-PseAAC methods (default is from 0.1 to 0.8). If there are several methods, "
                            "enter the ranges in turn.")
    parse.add_argument('-k', type=int, nargs='*',
                       help="The number of k adjacent structure statuses. (For PseKNC and Mismatch, default is from 1 "
                            "to 4. For Kmer, RevKmer, IDKmer, PseSSC and Subsequence, default is from 1 to 3.). "
                            "If there are several methods, enter the ranges in turn.")
    parse.add_argument('-m', type=int, nargs='*',
                       help="For Mismatch. The max value inexact matching. (m<k) (default is from 1 to 4). "
                            "If there are several methods, enter the ranges in turn.")
    parse.add_argument('-delta', type=float, nargs='*',
                       help="For subsequence method. The value of penalized factor. (0<=delta<=1) "
                            "(default is from 0 to 0.8). If there are several methods, enter the ranges in turn.")
    parse.add_argument('-ps', nargs='*',
                       help="The input positive source file in FASTA format for IDKmer.")
    parse.add_argument('-ns', nargs='*',
                       help="The input negative source file in FASTA format for IDKmer.")
    parse.add_argument('-max_dis', type=int, nargs='*',
                       help="The max distance value of DR, DT, Distance Pair. Only for DR, DT and Distance Pair "
                            "methods(default is from 1 to 4). If there are several methods, enter the ranges in turn.")
    parse.add_argument('-cp', choices=['cp_13', 'cp_14', 'cp_19', 'cp_20'], nargs='*',
                       help="For Distance Pair method. The reduced alphabet scheme. Choose one of the four:\n"
                            "cp_13, cp_14, cp_19, cp_20 ,default=cp_14")
    parse.add_argument('-r', type=int, nargs='*',
                       help="Whether consider the reverse complement or not. 1 means True, 0 means False. For Kmer "
                            "method. (default=0).Or the value of lambda, represents the highest counted rank (or tier) "
                            "of the structural correlation along a RNA chain. For PseSSC, PseDPC methods. "
                            "(default is from 1 to 7). If there are several methods, enter the ranges in turn.")
    parse.add_argument('-i',
                       help="The indices file user choose.\n"
                            "Default indices:\n"
                            "DNA dinucleotide: Rise, Roll, Shift, Slide, Tilt, Twist.\n"
                            "DNA trinucleotide: Dnase I, Bendability (DNAse).\n"
                            "RNA: Rise, Roll, Shift, Slide, Tilt, Twist.\n"
                            "Protein: Hydrophobicity, Hydrophilicity, Mass.")
    parse.add_argument('-e', help="The user-defined indices file.\n")
    # there has a problem
    parse.add_argument('-a', type=bool, nargs='*', help="Choose or do not choose all physicochemical indices, \n"
                                                        "default=False")
    parse.add_argument('-f', default='tab', choices=['tab', 'svm', 'csv'],
                       help="The output format (default = tab).\n"
                            "tab -- Simple format, delimited by TAB.\n"
                            "svm -- The libSVM training data format.\n"
                            "csv -- The format that can be loaded into a spreadsheet program.")
    parse.add_argument('-labels', nargs='*',
                       help="The labels of the input files.\n"
                            "For binary classification problem, the labels can only be '+1' or '-1'.\n"
                            "For multiclass classification problem, the labels can be set as a list of integers.")
    parse.add_argument('-cpu', type=int, nargs='*',
                       help="The maximum number of CPU cores used for multiprocessing in generating frequency profile. "
                            "(default=1).For Top-n-gram, PDT-Profile, DT, AC-PSSM, CC-PSSM, ACC-PSSM, PDT methods and "
                            "the number of CPU cores used for multiprocessing during parameter selection process. "
                            "(default=1).")
    # Parameters of SVM as follows:
    parse.add_argument('-p', default='ACC', choices=['ACC', 'MCC', 'AUC'],
                       help="The performance metric used for parameter selection.\n"
                            "Default value is ACC.")
    parse.add_argument('-model',
                       help="The name of the trained model.")

    parse.add_argument('-opt', default='0', choices=['0', '1'],
                       help="Set the range of parameters to be optimized.\n"
                            "0: small range set c from -5 to 10, step is 2; g from -10 to 5, step is 2.\n"
                            "1: large range set c from -5 to 10, step is 1; g from -10 to 5, step is 1.\n"
                            "Default value is 0.")

    parse.add_argument('-b', default='0', choices=['0', '1'],
                       help="whether to train a SVC or SVR model for probability\n"
                            "estimates, 0 or 1. Default value is 0.")
    parse.add_argument('-v', default='5',
                       help="The cross validation mode.\n"
                            "n: (an integer larger than 0) n-fold cross validation.\n"
                            "j: (character 'j') jackknife cross validation.\n"
                            "i: (character 'i') independent test set method.")
    parse.add_argument('-i_files', nargs='+',
                       help="The independent test dataset.\n"
                            "If the parameter '-v' is specified as 'i', one or more\n"
                            " independent test dataset files should be\n"
                            "included.\n"
                            "e.g. '-i_files test1.txt test2.txt'.")
    parse.add_argument('-o',
                       help="The output file name listing the predicted labels.\n"
                            "The default name is 'output_labels.txt'.")
    parse.add_argument('-ind',
                       help="The independent test dataset, The input files in FASTA format.")
    parse.add_argument('-rl',
                       help="The real label file. Optional.")
    parse.add_argument('-ml', default='svm', choices=['svm', 'rf', 'oet_knn', 'cda'],
                       help="The method of machine learning,\n"
                            "rf is random forest. Default is svm.")
    parse.add_argument('-sp', type=str, default='none', choices=['over', 'under', 'none'],
                       help="Balance the unbalanced data, default value is none.")
    parse.add_argument('-bp', default='0', choices=['0', '1'],
                       help="The option of batch processing. 1 is run batch processing, 0 is not.")
    parse.add_argument('-cw', type=int, default=0, choices=[0, 1],
                       help="Please choose whether you use the function")
    parse.add_argument('-size', type=int, default=5,
                       help="Please set the size of the window.")
    args = parse.parse_args()

    cmder = ' '.join(sys.argv[1:])
    cmd = 'python analysiss.pyc' + ' ' + cmder
    subprocess.call(cmd, shell=True)
