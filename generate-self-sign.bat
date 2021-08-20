set SIGNTOOL="C:\Program Files (x86)\Windows Kits\10\bin\10.0.19041.0\x64\signtool.exe"
set TIMESTAMP_SERVICE="http://timestamp.digicert.com"
echo "Test signing snapcraft.exe..."
powershell.exe .\generate-self-sign.ps1
echo "cx_freeze to produce exe from py..."
START /WAIT stltodae.bat
echo "sign stltodae.exe with self-signed cert..."
%SIGNTOOL% sign /fd SHA256 /td SHA256 /tr %TIMESTAMP_SERVICE% /f test-signing.pfx /p Password1234 cxfreeze\stltodae.exe
echo "create installer.exe"
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" stltodae.iss
echo "sign installer.exe with self-signed cert..."
%SIGNTOOL% sign /fd SHA256 /td SHA256 /tr %TIMESTAMP_SERVICE% /f test-signing.pfx /p Password1234 output\STLtoSketchup-Installx64.exe