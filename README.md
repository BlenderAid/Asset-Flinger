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
* Supports **.obj** file format and **.mtl** materials (asset material slots are remembered)
* For generating the asset thumbnails, user can drag-and-drop **.obj** files to the provided Thumbnailer python file (New instance of Blender will render them in the background)

## Feature Ideas :

#### Easier to add :
* installing the addon automatically adds one bookmark that points to the ‘assets' folder where objects are exported
* by pressing a up-folder-icon user can go up one directory (to the parent directory)
* wrapping of text for long file names

#### Harder to add :
* scrolling of the thumbnails via mouse wheel
* automatic thumbnail creation through the on-screen Asset Flinger menu
* automatic .obj export to the assets folder on user command. Displaying a confirm message
* support for .blend objects and materials + their thumbnails


