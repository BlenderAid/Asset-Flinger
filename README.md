![alt header](http://i.imgur.com/gp3BdlI.jpg)

# Asset Flinger
An addon for Blender to use quick shortcuts to easily import and export ready-made or user's own .OBJ mesh objects into Blender via graphical menu. The Add-on also includes a drag-and-drop Thumbnail-renderer for the objects.

**Demo** : 
[http://www.the_youtube_link_when_finished](http://www.)

![alt using Asset Flinger](http://i.imgur.com/sjnjRNl.jpg)

## Usage :

* Add a mesh asset via shortcut: **Ctrl+Shift+Alt+A**
* Export your own mesh asset to the library via shortcut: **Ctrl+Shift+Alt+E**
* Supports subfolders
* Supports **.obj** file format and **.mtl** materials (asset material slots are remembered)
* For generating the asset thumbnails, user can drag-and-drop **.obj** files to the provided Thumbnailer python file (New instance of Blender will render them in the background)

## Feature Ideas :

#### Easier to add :
* backspace goes up one directory (to the parent directory)
* installing the addon automatically adds one bookmark that points to the ‘assets' folder where objects are exported
* wrapping of text for long file names

#### Harder to add :
* less effort to install the THUMBNAILER regardless of operating system 
* (best would be no effort required at all. However, somehow Python 2.7 needs to be installed anyway)
* support for .blend objects and materials and their thumbnails
* scrolling of the thumbnails via mouse wheel
* by user command, objects could automatically get exported to the assets folder and a confirm message displayed
* automatic thumbnail creation could be launched through the on-screen Asset Flinger menu
