@SETLOCAL ENABLEDELAYEDEXPANSION & python -x "%~f0" %* & EXIT /B !ERRORLEVEL!

import os
currentFolder = os.path.dirname(os.path.realpath(__file__))

path = currentFolder+"\pythonExec.py"
exec(open(path).read())
