@for %%i in (%*) do "C:\Program Files\Blender Foundation\Blender\blender-app.exe" -b "%~dp0/.thumbnailer_MTL/Thumbnailer.blend" --python-text ThumbScript --objFiles %%i
