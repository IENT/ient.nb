# IENT TikZ Magic

## Introduction

Welcome! `ient_tikz_magic.py` enables you to compile your TikZ-figures in Jupyter notebooks! 

For an example, take a look at `Tikz Demo.ipynb`.

## Installation

Several commands are needed for `ient_tikzmagic` to work properly:

- `pdflatex` compiles your `tikz` code in the notebook to a pdf file (should be installed at all IENT computers)
- While compiling with `pdflatex` (or right at the end of the call), the latex `standalone` package calls imagemagick to convert the pdf to png (imagemagick should also be installed at IENT linux computers)
  - If you use linux: The newer versions of imagemagick prohibit converting pdf to other formats. You can force them to do so anyway by `sudo vim /etc/ImageMagick-6/policy.xml` and replacing `<policy domain="coder" rights="none" pattern="PDF" />` with `<policy domain="coder" rights="read|write" pattern="PDF" />`. Note that on newer systems, the `6` in `ImageMagick-6` should be replaced by higher numbers than six :)
  - If you use windows: replace `convertexe={convert}` with `convertexe={magick}` on line 293 of `ient_tikzmagic.py`
- Troubleshooting: You can enable `ient_tikzmagic` to forward the pdflatex log file to the notebook output by replacing `ret_log = False` with `ret_log = True` on line 106. If you then comment out line 354 to prevent deletion of the temporary folder (including the tex, log and pdf files) and adding a line with `print(plot_dir)` after line 250, you get access to said temporary folder for debugging.
