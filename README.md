![Header](http://i.imgur.com/gp3BdlI.jpg)

# About Blender 2.8

*"Addon Compatibility
When we switch to the OpenGL 3.3 core profile in Blender 2.8, addons that do OpenGL drawing will no longer be able to use deprecated functions. Old functions have already been removed from bpy.*

*We will give addon writers a way to draw into editors, but the exact API needs to be designed."*

So, Asset Flinger for Blender 2.8 will be on hold for the moment :/ Let's see how things turn out for the future.

# Download

**[Asset_Flinger_Add-on_v0.3.zip](https://github.com/black-h0bB1T/Asset-Flinger/blob/master/releases/Asset_Flinger_Add-on_v0.3.zip?raw=true)** (Blender 2.78c)

**[Asset_Pack_v0.1.zip (CC-0, Public Domain)](http://files.manujarvinen.com/asset_pack_v0.1.zip)**

**[Asset_Flinger_Add-on_v0.2.zip](http://files.manujarvinen.com/Asset_Flinger/Asset_Flinger_Add-on_v0.2.zip)** (Blender 2.77)

**[Asset_Flinger_Add-on_v0.1.zip](http://files.manujarvinen.com/Asset_Flinger/Asset_Flinger_Add-on_v0.1.zip)** (Blender 2.76 or lower)

- **[Installation instructions](https://github.com/BlenderAid/Asset-Flinger#installation)**

# Usage (IMPORTANT! READ THESE BEFORE USING!)

* Define your asset folder from the Add-on's settings, the path **CAN'T CONTAIN ANY SPACES** or it doesn't work.
* Export your own mesh asset to the library via shortcut: **Ctrl+Shift+Alt+E** - By this method you **AUTOMATICALLY render a thumbnail** for the object.
* Add a mesh asset via shortcut: **Ctrl+Shift+Alt+A**
* Supports subfolders
* If you want, **download the Asset Pack and unzip it** to the asset folder to have a nice collection of ***CC-0 / Public Domain / 100%-free-for-commercial-use*** useful assets, like nuts and bolts and many others. They can be downloaded from **[here](http://blenderaid.com/asset_library)** as well.
* If you have 100s of .obj files without thumbnails, you can download the 0.2 version of Asset Flinger, navigate to the thumbnailer folder and drag'n'drop the .obj files over the .py or .bat files in order to render thumbnails for them. You may need to edit the .py or .bat files to put your Blender's install location into them. The Mac Thumbnailer didn't seem to work, unfortunately :(

For example you might want to convert [this](https://gumroad.com/l/HTJJk) free 400-piece kitbashing set for Asset Flinger.

# Demo

Note: This video shows Asset Flinger 0.1/0.2. The current version has a bit more enhanced UI.

#### Video:
<a href="http://youtu.be/qYYoSTjIOTY" target="_blank">![Video](http://i.imgur.com/BwRkfsY.jpg)</a>
#### Screenshot:
![Screenshot](http://i.imgur.com/sjnjRNl.jpg)

# Asset Flinger

Note: Since version 0.3 Asset Flinger has had a new fork and a new maintainer here: [Asset Flinger New Maintainer](https://github.com/black-h0bB1T/Asset-Flinger).

Asset Flinger is a **Free Blender Add-on for simple mesh importing via graphical menu**.
It's aimed at 3D modellers who constantly import pre-made 3D assets from their libraries for building their highly detailed creations.

This Add-on also generates thumbnails for the assets you export.

> **Some history:**

> This add-on was made possible by the efforts of a 3D modeler and 3 anonymous programmers on their personal free time. The project started a long time ago **[back in 2013](http://blenderartists.org/forum/showthread.php?293731-OBJ-Asset-Library-Addon)** and was active only partly over time. There was some inspiration to develop it for the **[Blender Market's Add-on Contest](http://community.cgcookie.com/t/blender-add-on-contest-winners-announced/392)**. Thanks to Blender Market for the ***Honorable Mention for Asset Flinger!*** One idea was to actually put it on sale to there. - However, the add-on never got finished and so it's not polished enough in order to be put on sale. Also, **[the new awesome and extensive asset management system for Blender](https://mont29.wordpress.com/2015/01/14/assets-filebrowser-preliminary-work-experimental-build-i/)** is slowly coming and **[going to](http://wiki.blender.org/index.php/User:Brita/Proposals/UIPreviews)** render this add-on useless, so there's no sense to keep this behind curtains any longer anyway.

It is now released as a free add-on. Feel free to fork it if you like. 

> — Manu Järvinen, ([manu.jarvinen@gmail.com](mailto:manu.jarvinen@gmail.com))

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

# Tested
Asset Flinger has been tested and proved to work on :
* Blender 2.70 (Windows 7, MacOS X 10.10 Yosemite (except Thumbnailer), Ubuntu 14.10, Xubuntu 14.10)
* Blender 2.72 (Windows 7, MacOS X 10.10 Yosemite (except Thumbnailer), Ubuntu 14.10, Xubuntu 14.10)

# Known Bugs / Issues
* Spaces not supported in the 'Asset library path'
* Doesn't work in Local View (isolation mode)
* When Tool Shelf (T) or Properties (N) panel is open in 3D view, you can't toggle them off after you've launched the Asset Flinger menu
* While using Asset Flinger in quad view or other types of layouts that have multiple smaller 3D views, the menu appears to all of them.

# Feature Ideas

* Wrapping of text for long file names
* Remembering the last used asset folder where the user picked the asset last time
* Easy Add-on preferences checkbox for the above 'Remember last used asset folder'
* Easy Add-on preferences checkbox for hiding the asset file names in the asset menu to make it more compact
* Easy Add-on preferences setting to choose the amount of columns for the asset menu to make it more compact. (In the code there are already easy parameters for this)



