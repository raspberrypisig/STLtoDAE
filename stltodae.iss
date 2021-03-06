; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "STLtoSketchup"
#define MyAppVersion "0.1.0"
#define MyAppPublisher "Mohan Gupta"
#define MyAppURL "https://github.com/raspberrypisig/STLtoDAE"
#define MyAppExeName "stltodae.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{269B560E-F32C-4A96-8B34-DA0F90C2E7DD}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=C:\Users\Mohan\Developer\stltodae\cxfreeze\output
OutputBaseFilename=STLtoSketchup-Installx64
SetupIconFile=C:\Users\Mohan\Developer\stltodae\cxfreeze\geometric_figures_icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Mohan\Developer\stltodae\cxfreeze\stltodae\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mohan\Developer\stltodae\cxfreeze\stltodae\python3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mohan\Developer\stltodae\cxfreeze\stltodae\python39.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Mohan\Developer\stltodae\cxfreeze\stltodae\lib\*"; DestDir: "{app}\lib"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

