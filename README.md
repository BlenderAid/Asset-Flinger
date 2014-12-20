![alt header](http://i.imgur.com/gp3BdlI.jpg)
# Asset Flinger
An addon for Blender for simple mesh importing/exporting via graphical menu. 
The Add-on also includes a drag-and-drop Thumbnail-renderer for the objects.

**Demo** : 
[http://www.the_youtube_link_when_finished](http://www.)

![alt using Asset Flinger](http://i.imgur.com/sjnjRNl.jpg)

## Usage :

* Add a mesh asset via shortcut: **Ctrl+Shift+Alt+A**
* Export your own mesh asset to the library via shortcut: **Ctrl+Shift+Alt+E**
* Supports subfolders
* Supports **.obj** file format and **.mtl** materials (object material slots are remembered)
* For generating the asset thumbnails, user can drag-and-drop **.obj** files to the provided Thumbnailer python file (New instance of Blender will render them in the background)

## Feature Ideas :

#### Easier to add :
* Installing the addon automatically adds a bookmark that points to the ‘assets' folder where the objects should be exported
* By pressing a up-folder-icon in the on-screen Asset Flinger menu user can go up one directory (to the parent directory)
* Wrapping of text for long file names

#### Harder to add :
* Scrolling of the thumbnails via mouse wheel
* Automatic thumbnail creation through the on-screen Asset Flinger menu
* Automatic .obj export to the assets folder on user command. Displaying a confirm message
* Support for .blend objects and materials + their thumbnails


