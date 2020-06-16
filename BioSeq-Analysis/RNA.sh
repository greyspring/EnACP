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
python analysis.py ${input1} ${input2} RNA -method Kmer -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} RNA -method Mismatch -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} RNA -method Subsequence -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} RNA -method DAC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} RNA -method DCC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} RNA -method DACC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} RNA -method MAC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} RNA -method GAC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} RNA -method NMBAC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
#python analysis.py ${input1} ${input2} RNA -method PseSSC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
#python analysis.py ${input1} ${input2} RNA -method PseDPC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} RNA -method PC-PseDNC-General -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
#python analysis.py ${input1} ${input2} RNA -method Triplet -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} RNA -method SC-PseDNC-General -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python extract_data.py RNA/${type}
python extract.py RNA/${type}
