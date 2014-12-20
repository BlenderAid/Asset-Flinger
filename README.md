![Header](http://i.imgur.com/gp3BdlI.jpg)
# Asset Flinger
A Blender Add-on for simple mesh importing/exporting via graphical menu. 
The Add-on also includes a drag-and-drop thumbnail renderer for .obj files (works on Windows, Mac and Linux).

> Note that there's in development **a *new* very comprehensive Asset Browser for Blender by the Developers of the Blender Foundation**. Keep following the **<a href="http://gooseberry.blender.org" target="_blank">![Gooseberry blog](Gooseberry blog)</a>** and other Blender Development related channels in order to stay up to date on how it's progressing. That being said, Asset Flinger will probably eventually become unneeded. However, until that happens it sure can be fun and useful for some people.

##Download :
Here you can download the easily installable Add-on with ready-made CC0/Public Domain objects, the Python files in correct directories and some .blend templates for the thumbnailer. All in one package: **[Blender Aid Asset Flinger Add-on v0.1](http://files.manujarvinen.com/Blender_Aid/Blender_Aid_Asset_Flinger_Add-on_v0.1.zip)**

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
* For generating the asset thumbnails, user can drag-and-drop **.obj** files to the provided Thumbnailer python file. New instance of Blender will render them in the background.

## Installation :
#### Installing the Add-on :
1. Download the package
2. Open Blender
3. Go to user preferences -> Add-ons -> Install from File...
4. Navigate to the downloaded .zip file, click Install from File...
5. enable the Asset Flinger Add-on from the checkbox
6. Save User Settings
4. Try it out :) **Ctrl+Shift+Alt+A** opens the Asset Flinger menu in the 3D View

#### Setting up a Blender bookmark :
1. Make a simple object in Blender
2. Open the Python Console (**Shift+F4**), paste the following command and press Enter: `bpy.utils.user_resource('SCRIPTS', "addons")`
3. In the console, you should see the path to the Blender Add-ons folder for your system, copy  (**Ctrl+C**) that to clipboard (without the ' marks)
4. Export your object by pressing **Ctrl+Shift+Alt+E**
5. In the Export panel, press **Ctrl+V** to paste the 'Add-ons' folder location to the *File Path* bar, then go to the folder `/add_mesh_asset_flinger/assets/`
5. Add that as a bookmark
6. Export your object there

####Preparing Asset Flinger Thumbnailer
1. Check if you have Python installed by opening up the Terminal 
 * *Windows*: **Win-button+R** and type: `cmd`
 * *Mac*: **Command+space** and type: `terminal`
 * *Linux*: **Ctrl+Alt+T**
2. Type: `python`
3. If it says: `Python [version number]` and a couple of lines of text, then you have Python installed
4. If not, download **[Python 2.7.9](http://www.python.org)** and install it
5. Open your operating system's file browser and press
 * *Windows*: **Ctrl+L**
 * *Mac*: **Command+Shift+G**
 * *Linux*: **Ctrl+L**
6. Paste (**Ctrl+V**) the path to the addons folder and press Enter
7. Go to folder `/add_mesh_asset_flinger/assets/` and save it to favorites, name it as *"Asset Flinger Objects"*
8. Go back one folder and then go to folder `/thumbnailer/` and save it to favorites, name it as *"Asset Flinger Thumbnailer"*

##### Changing the path to Thumbnailer :
> INFO: for the Thumbnailer, default Blender paths are used:
> * *Windows*: `C:\\Program Files\\Blender Foundation\\Blender\\blender.exe` (Python requires double-backslashes)
> * *Mac*: `/Applications/Blender/blender.app/Contents/MacOS/blender`
> * *Linux*: `/usr/bin/blender`
    
If you need to change the Blender path, navigate to the following file in the addon's folder and open it into a text editor, make the change and save:
 * *Windows*: `thumbnailer\Windows\Thumbnailer.py`
 * *Mac*: `thumbnailer/Mac/Thumbnailer.app (right-click>Show Package Contents) /Contents/Resources/thumbnail_maker/config`
 * *Linux*: `thumbnailer/Linux/Thumbnailer.py`

> Note to *Windows* and *Linux* users, if you want to move the Thumbnailer to a different location, move the whole folder because it contains required hidden files. *Mac* users are free to move their single Thumbnailer wherever they want.

#### Finishing up :
1. Try to drag your .obj from *'Assets'* to the Thumbnailer like shown in the video
2. Done, everything should work nicely! If not, feel free to contact the Vendor for help :)

Asset Flinger has been tested and proved to work on :
* Blender 2.70 (Windows 7, MacOS X 10.10 Yosemite, Ubuntu 14.10, Xubuntu 14.10)
* Blender 2.72 (Windows 7, MacOS X 10.10 Yosemite, Ubuntu 14.10, Xubuntu 14.10) 

## Highly Hypothetical Future Development:

#### Feature Ideas (easier to add):
* Installing the addon automatically adds a bookmark that points to the ‘assets' folder where the objects should be exported
* Easy GUI option to hide file names in the menu to make it more compact
* Easy GUI option to choose the amount of columns for the menu to make it more compact (in the code there are already easy parameters for this)
* Providing 2 choices of the Addon. Small (64x64) and the current Normal (128x128) thumbnails to make it more compact (in the code there are already easy parameters for this) - The Thumbnailer settings would be changed as well.

#### Feature Ideas (harder to add):
* By pressing an up-folder-icon in the GUI user can go up one directory (to the parent directory)
* Wrapping of text for long file names
* Scrolling of the thumbnails via mouse wheel
* Automatic thumbnail creation through the on-screen Asset Flinger menu
* Automatic .obj export to the 'assets' folder on user command. Displaying a confirm message
* Support for .blend objects and materials + their thumbnails


