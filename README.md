![Header](http://i.imgur.com/gp3BdlI.jpg)
# Asset Flinger
An addon for Blender for simple mesh importing/exporting via graphical menu. 
The Add-on also includes a drag-and-drop Thumbnail-renderer for the objects.

> Note that Asset Flinger is useful most probably only for the waiting period until the very comprehensive Blender's new Asset Browser is ready to be released from Blender Foundation's Developers. It's already in development. Keep following [Gooseberry blog](http://gooseberry.blender.org/) to stay up to date on how it's progressing.

## Demo :

#### Screenshot:
![Screenshot](http://i.imgur.com/sjnjRNl.jpg)
#### Video:
<a href="http://www.the_youtube_link_when_finished" target="_blank">![Video](http://i.imgur.com/BwRkfsY.jpg)</a>

## Usage :

* Add a mesh asset via shortcut: **Ctrl+Shift+Alt+A**
* Export your own mesh asset to the library via shortcut: **Ctrl+Shift+Alt+E**
* Supports subfolders
* Supports **.obj** file format and **.mtl** materials (object material slots are remembered)
* For generating the asset thumbnails, user can drag-and-drop **.obj** files to the provided Thumbnailer python file (New instance of Blender will render them in the background)

## Future development:

#### Feature ideas (easier to add):
* Installing the addon automatically adds a bookmark that points to the ‘assets' folder where the objects should be exported
* Easy GUI option to hide file names in the menu to make it more compact
* Easy GUI option choose the amount of columns for the menu to make it more compact (in the code there are already easy parameters for this)
* Providing 3 choices of the Addon. Tiny (32x32), small (64x64) and normal (128x128) thumbnails to make it more compact (in the code there are already easy parameters for this) - The Thumbnailer settings would be changed as well.

#### Feature ideas (harder to add):
* By pressing a up-folder-icon in the on-screen Asset Flinger menu user can go up one directory (to the parent directory)
* Wrapping of text for long file names
* Scrolling of the thumbnails via mouse wheel
* Automatic thumbnail creation through the on-screen Asset Flinger menu
* Automatic .obj export to the assets folder on user command. Displaying a confirm message
* Support for .blend objects and materials + their thumbnails


