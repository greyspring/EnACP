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
start python analysis.py %posfile% %negfile% RNA -method Kmer -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% RNA -method Mismatch -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% RNA -method Subsequence -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% RNA -method DAC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% RNA -method DCC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% RNA -method DACC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% RNA -method MAC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% RNA -method GAC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% RNA -method NMBAC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% RNA -method PC-PseDNC-General -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% RNA -method SC-PseDNC-General -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python extract_data.py RNA/%ml%
start python extract.py RNA/%ml%