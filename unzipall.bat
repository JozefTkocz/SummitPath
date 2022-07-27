FOR /D /r %%F in (".") DO (
pushd %CD%
cd %%F
FOR %%X in (*.rar *.zip) DO (
"C:\Program Files\7-Zip\7z" x "%%X"
)
popd
)