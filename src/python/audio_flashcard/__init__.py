import os
from pysideuic import compileUi

dir_path = os.path.abspath(os.path.join(__file__, os.path.pardir))
ui = os.path.join(dir_path, 'audioFlashcard.ui')
out = os.path.join(dir_path, 'ui_audioFlashcard.py')
pyfile = open(out, 'w')
compileUi(ui, pyfile, False, 4, False)
pyfile.close()
