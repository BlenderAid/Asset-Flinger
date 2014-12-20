![alt header](http://i.imgur.com/gp3BdlI.jpg)
=============
# Asset Flinger
=============
An addon for Blender to use quick shortcuts to easily import and export ready-made or user's own .OBJ mesh objects into Blender via graphical menu. The Add-on also includes a drag-and-drop Thumbnail-renderer for the objects.

**Demo** : [http://www.theyoutubelinkwillgohere](http://www.)

## Features :

* Auto resize picture to jpg optimised and sharp, and cache thumbnail in tmp folder of your server ( thx Timthumb )
* Keep high-res on disk to download, so you can list a lot of hi-res PNG easily
* link (auto scroll in the page ) to the picture available.
* Display date, file weight, image size
* Generate page title and title for the files automatically.
* Responsive, image are resized for smartphone, and tablet with smaller screens. 
* Don't get listed by search engine to keep project private ( anyone with link can access )
* Subfolder works, and has mini thumbnails

## Usage :

Just drop the index.php file into a FTP folder with the "lib" subfolder.
Your folder is now ready to list images and files. 

## To know :

#### List of picture format to be display :

jpg,gif,png,jpeg
 
#### List of downloadable files : 

zip,txt,psd,pdf,avi,mpeg,tar,7z,odt,doc,docx,ppt,ora

#### Privacy :

Possibility to make the page private, via a secret path name, and uncommenting line 49, to block access of search engine and bots. 

#### Listing order :

Files are listed depending alphabetical order, first pictures then files ( to download, etc ). you can use number prefix to sort them manually ( eg: 01-file.jpg, 02-file.jpg etc... or 20140815-wip.png, 20140920-wip.png ). Number are removed automatically to make a clean title to the picture. 

## Troubles/Issues :

Most of the issues can come from *Timthumb*, the library I use for generating the thumbnails.

I ship a modified version of timthumb ( configuration changed only ) to use the /tmp/ folder of the Linux server as a place to cache images. With this method, I avoid having to download a cache folder when I backup my server ; but If this method doesn't work on your server ; you probably will prefer to setup manually a cache folder (l.40 on lib/timthumb.php ). You can see how the default timthumb last SVN file is setup here : [https://code.google.com/p/timthumb/source/browse/trunk/timthumb.php](https://code.google.com/p/timthumb/source/browse/trunk/timthumb.php) ; using './cache' . If you decide to use a cache folder, be sure to apply a 777 permission to it ( or 755 should be suffisent too ). Other modifications I made on the version I ship : max imagesize, max imageweight and a better sharpening filter in my opinion.

Read more info about installation recommendation here : [http://www.binarymoon.co.uk/2010/11/timthumb-hints-tips/](http://www.binarymoon.co.uk/2010/11/timthumb-hints-tips/)








The Contours Retopology tool is an addon for Blender that provides quick and easy ways retopologize cylindrical forms. Use cases include organic forms, such as arms, legs, tentacles, tails, horns, etc.

The tool works by drawing strokes perpendicular to the form to define the contour of the shape. Immediately upon drawing the first stroke, a preview mesh is generated, showing you exactly what you’ll get. You can draw as many strokes as you like, in any order, from any direction.

The add-on is available for purchase from the Blender Market: http://cgcookiemarkets.com/blender/all-products/contours-retopology-tool/

Documentation: http://cgcookiemarkets.com/blender/all-products/contours-retopology-tool/?view=docs

Support Forums: http://cgcookiemarkets.com/blender/all-products/contours-retopology-tool/?view=support
