![Header](http://i.imgur.com/gp3BdlI.jpg)

# Download

**[Asset_Flinger_Add-on_v0.1.zip](http://files.manujarvinen.com/Asset_Flinger/Asset_Flinger_Add-on_v0.1.zip)**

- **[Installation instructions](https://github.com/BlenderAid/Asset-Flinger#installation)**
- Includes some nice ready-made ***CC-0 / Public Domain / 100%-free-for-commercial-use*** assets. They can be downloaded from **[here](http://blenderaid.com/asset_library)** as well.

# Demo

#### Video:
<a href="http://youtu.be/qYYoSTjIOTY" target="_blank">![Video](http://i.imgur.com/BwRkfsY.jpg)</a>
#### Screenshot:
![Screenshot](http://i.imgur.com/sjnjRNl.jpg)

#### GIF animation about using the Thumbnailer (Windows):
<a href="http://i.imgur.com/cbulKFh.gif" target="_blank">![Gif](http://i.imgur.com/cbulKFh.gif)</a>

# Asset Flinger
Asset Flinger is a work-in-progress **Free Blender Add-on for simple mesh importing via graphical menu**.
It's aimed at 3D modellers who constantly import pre-made 3D assets from their libraries for building their highly detailed creations.

The Add-on also includes a drag-and-drop thumbnail generator for .obj files for Windows and Linux. (Although it should be eventually quite easy to generate the thumbnails inside Blender) **[Find here](http://files.manujarvinen.com/Asset_Flinger/)** the development files for Mac OS X that almost worked)

> **Some history:**

> This add-on was made possible by the efforts of a 3D modeler and 3 anonymous programmers on their personal free time. The project started a long time ago **[back in 2013](http://blenderartists.org/forum/showthread.php?293731-OBJ-Asset-Library-Addon)** and was active only partly over time. There was some inspiration to develop it for the **[Blender Market's Add-on Contest](http://community.cgcookie.com/t/blender-add-on-contest-winners-announced/392)**. Thanks to Blender Market for the ***Honorable Mention for Asset Flinger!*** One idea was to actually put it on sale to there. - However, the add-on never got finished and so it's not polished enough in order to be put on sale. Also, **[the new awesome and extensive asset management system for Blender](https://mont29.wordpress.com/2015/01/14/assets-filebrowser-preliminary-work-experimental-build-i/)** is slowly coming and **[going to](http://wiki.blender.org/index.php/User:Brita/Proposals/UIPreviews)** render this add-on useless, so there's no sense to keep this behind curtains any longer anyway.

It is now released as a free add-on. Feel free to fork it if you like. 
Although, **contributions as pull requests** to the project would be highly appreciated :) 

> Also CC-0 licenced .obj assets would be gladly accepted as contributions, and I plan on making and adding more of them - I'm very picky about their quality, though. Personally I like to use Asset Flinger for my daily modeling, regardless of its shortcomings :) 

> — Manu Järvinen

# Usage

* Add a mesh asset via shortcut: **Ctrl+Shift+Alt+A**
* Export your own mesh asset to the library via shortcut: **Ctrl+Shift+Alt+E**
* Supports subfolders
* Supports **.obj** file format and **.mtl** materials (object material slots are remembered)
* For generating the asset thumbnails (doesn't work in Mac OS X yet), user can drag-and-drop **.obj** files to the provided Thumbnailer python or bat file. New instance of Blender will render them in the background.

# Installation
#### Installing the Add-on :
1. Download the package
2. Open Blender
3. Go to user preferences > Add-ons > Install from File...
4. Navigate to the downloaded .zip file, click Install from File...
5. Enable the Asset Flinger Add-on from the checkbox
6. Save User Settings
7. Try it out :) **Ctrl+Shift+Alt+A** opens the Asset Flinger menu in the 3D View

#### Setting up library location for your own assets:
1. In the Add-ons panel in Blender's User Preferences, put your own Asset Library location to Asset Flinger Add-on's preferences
2. Export your 3D models to the library with **Ctrl+Shift+Alt+E**
3. Make that location as a bookmark for your convenience

#### Preparing Asset Flinger Thumbnailer (sadly, quite loborious :/ - Also, doesn't work in Mac OS X yet)
1 . Unzip the Asset Flinger Add-on's .zip file and find the Thumbnailer folder for your system

2 . If you have installed Blender to default location, skip to step 5
> INFO: these are the usual default installation locations for Blender:
> * *Windows*: `C:\Program Files\Blender Foundation\Blender\blender-app.exe`
> * *Mac*: `/Applications/Blender/blender.app/Contents/MacOS/blender`
> * *Linux*: `/usr/bin/blender`

3 . Navigate to the following file and open it into a text editor (in Windows Wordpad is recommended), make the change and save:
 * *Windows*: `thumbnailer\Windows\Thumbnailer.bat`
 * *Mac*: `thumbnailer/Mac/Thumbnailer.app (right-click>Show Package Contents) /Contents/Resources/thumbnail_maker/config`
 * *Linux*: `thumbnailer/Linux/Thumbnailer.py`

4 . In the Thumbnailer file, change the path to where your Blender is located, save and close

> Note to *Windows* and *Linux* users, if you want to move the Thumbnailer to a different location, move the whole folder because it contains required hidden files. *Mac* users are free to move their single Thumbnailer wherever they want.

5 . Try to drag your .obj from Your Asset Library to the Thumbnailer like shown in the video. A nice thumbnail should be rendered.

> In Linux, at least Thunar file manager supports Drag&Drop, you may need to install it. Also, you might need to right-click the .py-file and make it executable in order to allow Drag&Drop

6 . Done, everything should work nicely!

# Tested
Asset Flinger has been tested and proved to work on :
* Blender 2.70 (Windows 7, MacOS X 10.10 Yosemite (except Thumbnailer), Ubuntu 14.10, Xubuntu 14.10)
* Blender 2.72 (Windows 7, MacOS X 10.10 Yosemite (except Thumbnailer), Ubuntu 14.10, Xubuntu 14.10)

# Known Bugs / Issues
* Doesn't work in Local View (isolation mode)
* When using *Your Library*, the Asset Flinger menu displays the whole path to your library. Should be only the folder's name
* When Tool Shelf (T) or Properties (N) panel is open in 3D view, you can't toggle them off after you've launched the Asset Flinger menu
* When you set up a wrong path for *Your Library* in the add-on's Preferences, you get an error message when using the custom path in the add-on in 3D view. Also, the 3D view goes a little darker and doesn't go away until you restart whole Blender
* While in the Asset Flinger menu and doing an Alt-Tab to switch programs, and then coming back to Blender, the menu appears to all open 3D views. Very annoying.
* While using Asset Flinger in quad view or other types of layouts that have multiple smaller 3D views, the menu appears to all of them.

# Feature Ideas

#### Easier to add:
* Remembering the last used asset folder where the user picked the asset last time
* Easy Add-on preferences checkbox for the above 'Remember last used asset folder'
* Easy Add-on preferences checkbox for hiding the asset file names in the asset menu to make it more compact
* Easy Add-on preferences setting to choose the amount of columns for the asset menu to make it more compact. (In the code there are already easy parameters for this)
* Easy Add-on preferences setting to choose between the current Normal (128x128) and Small (64x64) sized thumbnails to allow for more compact view. (In the code there are already easy parameters for this) - OR - if this appears to be hard to realize, then simply providing 2 choices of the Add-on with the different sized thumbnails and thumbnail-generation settings

#### Harder to add:
* **Instant and Automatic thumbnail rendering for exported objects (no need to leave Blender or setting up the Thumbnailer at all)**
* Wrapping of text for long file names
* Scrolling of the thumbnails via mouse wheel
* Support for .blend objects and materials + their thumbnails
