Rem Create the QT5_DIR environment variable if it does not exist already.

IF NOT DEFINED QT5_DIR (
	ECHO QT5_DIR is NOT defined
)
ELSE (
	ECHO. && ECHO QT5_DIR environment variable exists already! && ECHO QT5_DIR = %QT5_DIR% && ECHO. && SET /p userinput=Type YES if you want to set the environment variable nonetheless or NO to exit batch file: 
	
	IF %userinput%==YES (
		setx QT5_DIR %HOMEDRIVE%\Qt\Qt5.6.0\5.6\
		ECHO The following environment variable has been set && ECHO. && ECHO QT5_DIR = %QT5_DIR% && ECHO.
		PAUSE
	)
	EXIT /B 1
)

SET /p userinput=Type YES if you want to create the environment variable or NO to exit batch file: 
ECHO %userinput%

IF %userinput%==YES (
	setx QT5_DIR %HOMEDRIVE%\Qt\Qt5.6.0\5.6\
	ECHO Created and set the user variable QT5_DIR = %HOMEDRIVE%\Qt\Qt5.6.0\5.6\
)

PAUSE
EXIT /B 1