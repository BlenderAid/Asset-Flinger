@for %%i in (%*) do "C:\Program Files\Blender\blender-app.exe" -b "%~dp0/.thumbnailer_METAL/Thumbnailer.blend" --python-text ThumbScript --objFiles %%i
