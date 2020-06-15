#!/bin/bash
input1=$1
input2=$2
type=$3
label1=$4
label2=$5
model=$6
fold=$7
opt=$8
cpu=$9
python analysis.py ${input1} ${input2} Protein -method Kmer -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method DR -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method DP -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method AC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method CC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method ACC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method PDT -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method PC-PseAAC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method SC-PseAAC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method PC-PseAAC-General -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method SC-PseAAC-General -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method Top-n-gram -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method PDT-Profile -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method DT -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method AC-PSSM -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method CC-PSSM -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method ACC-PSSM -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method SS -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method SASA -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method CS -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method PSSM-DT -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} Protein -method PSSM-RT -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python extract_data.py Protein/${type}
python extract.py Protein/${type}
