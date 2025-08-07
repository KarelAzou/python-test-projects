This is my python test project

::-----------------------------------------------------
::-- DO ONCE as setup
::-----------------------------------------------------

::To initially setup a vitual environment run in terminal
::first make sure you're in the root dir of your project
python -m venv .venv

::-----------------------------------------------------
::-- Do this when downloading this project
::-----------------------------------------------------
::In VS Code Press Ctrl+Shift+P to open the Command Palette.
::Type: Python: Select Interpreter
::Choose the one that looks like:
::    .\.venv\Scripts\python.exe 

::once that was set up
:: activate your venv 
.venv/Scripts/activate
::simply install the requirements to this venv
pip install -r requirements.txt