# EnACP
 
EnACP is a method to identify anticancer peptides using diversified feature representations and ensemble learning.

1. pre-Installation

===========

The BioSeq-Analysis package need to be pre-installed. The full package and documents of BioSeq-Analysis are available at http://bioinformatics.hitsz.edu.cn/BioSeq-Analysis/download. 
Before using BioSeq-Analysis, the Python software should be first installed and configured. Python 2.7 64-bit is recommended, which can be downloaded from https://www.python.org. 

If you clone this git repository, you dont need install BioSeq-Analysis package but need copy two files nrdb90.phr and nrdb90.psq in BioSeq-Analysis package into directory /anti/BioSeq-Analysis/psiblast/nrdb90/.
or install BioSeq-Analysis package referring the file: /anti/BioSeq-Analysis/README.



2. Usage 

===========

  1).Test fasta sequences: 
  
     Create a new directory for the test fasta format file in the directory /anti/Input_data/Input_data_fasta/test/

  2).Feature_repretation: 
  
     python Feature_repretation.py  EnACP/anti/Input_data/Input_fasta/test
     Features are stored in directory EnACP/anti/Input_data/Input_data_feature/.

  3).Prediction:  
  
     python  predict.py EnACP/anti/Input_data/Input_feature/test


3. Reference and Feedback

===========

  Ruiquan Ge, Guanwen Feng, Xiaoyang Jing, Renfeng Zhang, Pu Wang and Qing Wu. EnACP: An Ensemble Learning Model for Identification of     Anticancer Peptides. Submitted,2020.
 
  Please contact the development team at: gespring@hdu.edu.cn or fgw.98@qq.com to submit questions or feedback for us.
