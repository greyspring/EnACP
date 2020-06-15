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
python analysis.py ${input1} ${input2} DNA -method Kmer -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
#python analysis.py ${input1} ${input2} DNA -method Kmer -r 1 -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} DNA -method Mismatch -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} DNA -method Subsequence -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} DNA -method DAC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} DNA -method DCC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} DNA -method DACC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} DNA -method TAC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} DNA -method TCC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} DNA -method TACC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} DNA -method MAC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} DNA -method GAC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} DNA -method NMBAC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} DNA -method PseDNC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} DNA -method PseKNC -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} DNA -method PC-PseDNC-General -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} DNA -method PC-PseTNC-General -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} DNA -method SC-PseDNC-General -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python analysis.py ${input1} ${input2} DNA -method SC-PseTNC-General -ml ${type} -labels ${label1} ${label2} -model ${model} -v ${fold} -opt ${opt} -cpu ${cpu} -bp 1
python extract_data.py DNA/${type}
python extract.py DNA/${type}
