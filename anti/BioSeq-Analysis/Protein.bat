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
start python analysis.py %posfile% %negfile% Protein -method Kmer -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method DR -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method DP -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method AC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method CC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method ACC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method PDT -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method PC-PseAAC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method SC-PseAAC -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method PC-PseAAC-General -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method SC-PseAAC-General -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method Top-n-gram -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method PDT-Profile -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method DT -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method AC-PSSM -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method CC-PSSM -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method ACC-PSSM -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method SS -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method SASA -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method CS -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method PSSM-DT -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python analysis.py %posfile% %negfile% Protein -method PSSM-RT -ml %ml% -labels %poslabel% %neglabel% -model %model% -v %v% -opt %opt% -cpu %cpu% -bp 1
start python extract_data.py Protein/%ml%
start python extract.py Protein/%ml%