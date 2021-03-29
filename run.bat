@REM start "" chromedriver.exe

@REM install modul
pip install pipreqs
pipreqs .
pip install - r requirements.txt

pythonw script_api.py