![Header](http://i.imgur.com/gp3BdlI.jpg)
# Asset Flinger
A Blender Add-on for simple mesh importing via graphical menu. 
The Add-on also includes a drag-and-drop thumbnail generator for .obj files. (Works on Windows, Mac and Linux - However, the Thumbnailer For Mac doesn't work yet :/ But soon it will.)

> This addon is made as a hobby on free time and mainly intended for the excruciating waiting period until the **new very comprehensive Asset Browser for Blender** is released from the **Developers of the Blender Foundation** as mentioned **[here](http://www.blender.org/press/18-anticipated-blender-development-projects-of-2015/)**. Keep following the **[Gooseberry blog](http://gooseberry.blender.org)** and other Blender Development related channels in order to stay up to date on how it's progressing. That being said, Asset Flinger will probably eventually become unneeded. However, until that happens it sure can be fun and useful for some people.

##Download :
Here you can download the easily installable Add-on with ready-made ***CC0 / Public Domain / 100%-free-for-commercial-use*** objects, the Python files in correct directories and some .blend templates for the thumbnailer. All in one package: **[Blender Aid Asset Flinger Add-on v0.1](http://files.manujarvinen.com/Blender_Aid/Blender_Aid_Asset_Flinger_Add-on_v0.1.zip)**

## Demo :

#### Screenshot:
![Screenshot](http://i.imgur.com/sjnjRNl.jpg)
#### Video:
<a href="https://www.youtube.com/watch?v=FhpIx_CqWIo" target="_blank">![Video](http://i.imgur.com/BwRkfsY.jpg)</a>

## New Features:
**User library:**
![User library](http://i.imgur.com/mNprfnZ.png)

**'Go to parent folder' icon**
![Parent folder](http://i.imgur.com/IqbiM0D.png)

## Usage :

* Add a mesh asset via shortcut: **Ctrl+Shift+Alt+A**
* Export your own mesh asset to the library via shortcut: **Ctrl+Shift+Alt+E**
* Supports subfolders
* Supports **.obj** file format and **.mtl** materials (object material slots are remembered)
* For generating the asset thumbnails, user can drag-and-drop **.obj** files to the provided Thumbnailer python or bat file. New instance of Blender will render them in the background.

## Installation :
#### Installing the Add-on :
1. Download the package
2. Open Blender
3. Go to user preferences > Add-ons > Install from File...
4. Navigate to the downloaded .zip file, click Install from File...
5. Enable the Asset Flinger Add-on from the checkbox
6. Save User Settings
7. Try it out :) **Ctrl+Shift+Alt+A** opens the Asset Flinger menu in the 3D View

#### Setting up :
1. In the Addon panel in Blender's User Preferences, put your own Asset Library location to Asset Flinger Addon's preferences
2. Next time you export objects with **Ctrl+Shift+Alt+E**, make that location as a bookmark for your convenience

> #### Installing Python (probably not needed)
1. Check if you have Python installed by opening up the Terminal 
 * *Windows*: **Win-button+R** and type: `cmd`
 * *Mac*: **Command+space** and type: `terminal`
 * *Linux*: **Ctrl+Alt+T**
2. Type: `python`
3. If it says: `Python [version number]` and a couple of lines of text, then you have Python installed
4. If not, download **[Python 2.7.9](http://www.python.org)** and install it

#### Preparing Asset Flinger Thumbnailer
1. Find the Thumbnailer for your system by unzipping the Asset Flinger Add-on's .zip file

##### Changing the path to Thumbnailer (If you haven't installed Blender to default location) :
> INFO: these are the default paths for the Thumbnailer:
> * *Windows*: `C:\Program Files\Blender Foundation\Blender\blender-app.exe`
> * *Mac*: `/Applications/Blender/blender.app/Contents/MacOS/blender`
> * *Linux*: `/usr/bin/blender`
    
If you need to change the Blender path, navigate to the following file in the thumbnailer and open it into a text editor (in Windows Wordpad is recommended), make the change and save:
 * *Windows*: `thumbnailer\Windows\Thumbnailer.bat`
 * *Mac*: `thumbnailer/Mac/Thumbnailer.app (right-click>Show Package Contents) /Contents/Resources/thumbnail_maker/config`
 * *Linux*: `thumbnailer/Linux/Thumbnailer.py`

> Note to *Windows* and *Linux* users, if you want to move the Thumbnailer to a different location, move the whole folder because it contains required hidden files. *Mac* users are free to move their single Thumbnailer wherever they want.

#### Finishing up :
1. Try to drag your .obj from Your Asset Library to the Thumbnailer like shown in the video
2. Done, everything should work nicely! If not, feel free to contact the Vendor for help :)

Asset Flinger has been tested and proved to work on :
* Blender 2.70 (Windows 7, MacOS X 10.10 Yosemite (except Thumbnailer), Ubuntu 14.10, Xubuntu 14.10)
* Blender 2.72 (Windows 7, MacOS X 10.10 Yosemite (except Thumbnailer), Ubuntu 14.10, Xubuntu 14.10) 

## Highly Hypothetical Future Development:

#### Feature Ideas (easier to add):
* Remembering the folder where the user picked the object last time
* Easy Addon checkbox for the above 'Remember last used asset folder'
* Easy Addon setting to hide file names in the menu to make it more compact
* Easy Addon setting to choose the amount of columns for the menu to make it more compact. (In the code there are already easy parameters for this)
* Easy Addon setting to choose between the current Normal (128x128) and Small (64x63) sized thumbnails to allow for more compact view. (In the code there are already easy parameters for this) - OR - if this appears to be hard to realize, then simply providing 2 choices of the Addon with the different sized thumbnails and thumbnail-generation settings

#### Feature Ideas (harder to add):
* Wrapping of text for long file names
* Scrolling of the thumbnails via mouse wheel
* Instant and Automatic thumbnail rendering for exported objects (no need to leave Blender or setting up the Thumbnailer at all)
* Support for .blend objects and materials + their thumbnails

## Known Bugs:
* When using Your Library, the Asset Flinger menu displays the whole path to your library. Should be only the folder's name
* While in the Asset Flinger menu and doing an Alt-Tab to switch programs, and then coming back to Blender, the menu appears to all 3D views. Very annoying.
