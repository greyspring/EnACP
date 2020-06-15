@echo off
set posfile=%1%
set negfile=%2%
set ml=%3%
set poslabel=%4%
set neglabel=%5%
set model=%6%
set v=%7%
set opt=%8%
set cpu=%9%
start python analysis.py %posfile% %negfile% DNA -method Kmer -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
#python analysis.py %posfile% %negfile% DNA -method Kmer -r 1 -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% DNA -method Mismatch -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% DNA -method Subsequence -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% DNA -method DAC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% DNA -method DCC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% DNA -method DACC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% DNA -method TAC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% DNA -method TCC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% DNA -method TACC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% DNA -method MAC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% DNA -method GAC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% DNA -method NMBAC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% DNA -method PseDNC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% DNA -method PseKNC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% DNA -method PC-PseDNC-General -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% DNA -method PC-PseTNC-General -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% DNA -method SC-PseDNC-General -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% DNA -method SC-PseTNC-General -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python extract_data.py DNA/%ml%
start python extract.py DNA/%ml%