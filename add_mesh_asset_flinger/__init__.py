# ##### BEGIN GPL LICENSE BLOCK #####
#
#  Copyright (C) 2014 Blender Aid
#  http://www.blendearaid.com
#  blenderaid@gmail.com

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
        "name": "Asset Flinger",
        "version": (0, 2),
        "blender": (2, 70, 0),
        "location": "View3D > Add > Mesh > Asset Flinger",
        "description": "Simple Mesh Importer",
        "category": "Add Mesh"}

import bpy
import bgl
import blf
import os
import pprint

from bpy.types import AddonPreferences
from bpy.props import (BoolProperty, EnumProperty,
                       FloatProperty, FloatVectorProperty,
                       IntProperty, StringProperty)

class AssetFlingerPreferences(AddonPreferences):
    bl_idname = __name__
    custom_library_path = StringProperty(
            name="Your Library",
            subtype='FILE_PATH',
            )

    def draw(self, context):
            layout = self.layout

            split = layout.split(percentage=1)

            col = split.column()
            sub = col.column(align=True)
            sub.prop(self, "custom_library_path")

            sub.separator()


iconWidth = 128
iconHeight = 128
targetItemWidth = 400
targetItemHeight = 128

# Full path to "\addons\add_mesh_asset_flinger\" -directory
paths = bpy.utils.script_paths("addons")

libraryPath = 'assets'
for path in paths:
    libraryPath = os.path.join(path, "add_mesh_asset_flinger")
    if os.path.exists(libraryPath):
        break

if not os.path.exists(libraryPath):
    raise NameError('Did not find assets path from ' + libraryPath)
libraryIconsPath = os.path.join(libraryPath, "icons")
libraryDefaultModelsPath = os.path.join(libraryPath, "assets")

def drawMenuItem(item, x, y, width, height):
    global iconWidth
    global iconHeight

    iconMarginX = 4
    iconMarginY = 4
    textMarginX = 6

    textHeight = 16
    textWidth = 72

    bgl.glEnable(bgl.GL_BLEND)
    if item['highlighted']:
        bgl.glColor4f(0.555, 0.555, 0.555, 0.8)
    else:
        bgl.glColor4f(0.447, 0.447, 0.447, 0.8)

    bgl.glRectf(x, y, x + width, y + height)

    texture = item['icon']
    texture.gl_load()
    bgl.glColor4f(0.0, 0.0, 1.0, 0.5)
    #bgl.glLineWidth(1.5)

    #------ TEXTURE ---------#
    bgl.glEnable(bgl.GL_BLEND)
    bgl.glBindTexture(bgl.GL_TEXTURE_2D, texture.bindcode[0])
    bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MIN_FILTER, bgl.GL_NEAREST)
    bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MAG_FILTER, bgl.GL_NEAREST) #GL_LINEAR seems to be used in Blender for background images
    bgl.glEnable(bgl.GL_TEXTURE_2D)
    bgl.glBlendFunc(bgl.GL_SRC_ALPHA, bgl.GL_ONE_MINUS_SRC_ALPHA)

    bgl.glColor4f(1,1,1,1)
    bgl.glBegin(bgl.GL_QUADS)
    bgl.glTexCoord2d(0,0)
    bgl.glVertex2d(x + iconMarginX, y)
    bgl.glTexCoord2d(0,1)
    bgl.glVertex2d(x + iconMarginX, y + iconHeight)
    bgl.glTexCoord2d(1,1)
    bgl.glVertex2d(x + iconMarginX + iconWidth, y + iconHeight)
    bgl.glTexCoord2d(1,0)
    bgl.glVertex2d(x + iconMarginX + iconWidth , y)
    bgl.glEnd()

    texture.gl_free()

    # draw some text
    font_id = 0
    blf.position(font_id, x + iconMarginX + iconWidth + textMarginX, y + iconHeight * 0.5 - 0.25 * textHeight, 0)
    blf.size(font_id, textHeight, textWidth)
    blf.draw(font_id, item['text'])

def drawCallbackMenu(self, context):

    global targetItemWidth
    global targetItemHeight

    marginX = 20
    marginY = 5
    paddingX = 5


    bgl.glEnable(bgl.GL_BLEND)
    bgl.glColor4f(0.0, 0.0, 0.0, 0.6)
    bgl.glRectf(0,0,context.area.regions[4].width,context.area.regions[4].height)

    contentWidth = context.area.regions[4].width - marginX * 2
    contentHeight = context.area.regions[4].height - marginY * 2

    contentX = marginX
    contentY = context.area.height - marginY - targetItemHeight - 50

    colCount = int(contentWidth / targetItemWidth)

    itemWidth = (contentWidth - (colCount * paddingX)) / (colCount + 1)
    itemHeight = targetItemHeight

    col = 0
    row = 0
    x = contentX
    y = contentY

    if len(self.current_dir_content ) == 0:
        font_id = 0
        text = "Folder doesn't contain any assets!"
        bgl.glColor4f(1.0, 1.0, 1.0, 1.0)
        blf.size(font_id, 20, 72)
        textWidth, textHeight = blf.dimensions(font_id, text)
        blf.position(font_id, contentX + contentWidth * 0.5 - textWidth * 0.5, contentY - contentHeight * 0.5 + textHeight * 0.5, 0)
        blf.draw(font_id, text)
    else:
        for item in self.current_dir_content:
            if self.mouseX > x and self.mouseX < x + itemWidth and self.mouseY > y and self.mouseY < y + itemHeight:
                item['highlighted'] = True
            else:
                item['highlighted'] = False

            drawMenuItem(item, x, y, itemWidth, itemHeight)
            x = x + itemWidth + paddingX
            col += 1

            if col > colCount:
                col = 0
                x = contentX
                y = y - itemHeight - marginY
                row += 1

    bgl.glDisable(bgl.GL_BLEND)
    bgl.glDisable(bgl.GL_TEXTURE_2D)
    #bgl.glColor4f(0.0, 0.0, 0.0, 1.0)

def getClicked(self, context):


    global targetItemWidth
    global targetItemHeight

    marginX = 20
    marginY = 5
    paddingX = 5

    contentWidth = context.area.regions[4].width - marginX * 2
    contentHeight = context.area.regions[4].height - marginY * 2

    contentX = marginX
    contentY = context.area.height - marginY - targetItemHeight - 50

    colCount = int(contentWidth / targetItemWidth)

    itemWidth = (contentWidth - (colCount * paddingX)) / (colCount + 1)
    itemHeight = targetItemHeight

    col = 0
    row = 0
    x = contentX
    y = contentY

    for item in self.current_dir_content:
        if self.mouseX > x and self.mouseX < x + itemWidth and self.mouseY > y and self.mouseY < y + itemHeight:
            return item

        x = x + itemWidth + paddingX
        col += 1
        if col > colCount:
            col = 0
            x = contentX
            y = y - itemHeight - marginY
            row += 1
    return None

class AssetFlingerMenu(bpy.types.Operator):

    bl_idname = "view3d.asset_flinger"
    bl_label = "Asset Flinger"
    tree_index = ''
    current_dir_content = []

    def clearImages(self):
        # Cleaner for Images
        # print ("here")
        for image in bpy.data.images:
            if image.filepath_raw in self.imageList:
                # print (image.filepath_raw)
                image.user_clear()
                bpy.data.images.remove(image)

        # print ("images " + str(len(bpy.data.images)))

        self.imageList.clear()

    def modal(self, context, event):
        context.area.tag_redraw()
        if event.type == 'MOUSEMOVE':
            self.mouseX = event.mouse_region_x
            self.mouseY = event.mouse_region_y

        elif event.type == 'LEFTMOUSE' and event.value == 'RELEASE':
            self.mouseX = event.mouse_region_x
            self.mouseY = event.mouse_region_y
            selected = getClicked(self, context)

            if selected == None:
                bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
                return {'FINISHED'}

            if selected['isFolder'] == True:

                self.tree_index = os.path.normpath(os.path.join(self.tree_index, selected['text']))
                self.browse_assets(self.tree_index)

            else:
                bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
                bpy.ops.import_scene.obj(filepath=selected['filename'])
                bpy.ops.view3d.snap_selected_to_cursor()
                bpy.context.scene.objects.active = bpy.context.selected_objects[0]

                return {'FINISHED'}

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')

            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def buildAssetTree(self, parentItem, path):
        parentItem['subItems'] = []

        up_folder = {}
        iconFile = os.path.join(libraryIconsPath, "folder.png")
        up_folder['icon'] = bpy.data.images.load(filepath = iconFile)
        self.imageList.append(up_folder['icon'].filepath_raw)
        up_folder['text'] = '..'
        up_folder['isFolder'] = True
        up_folder['subItems'] = []
        #up_folder['index'] = self.tree_index
        parentItem['subItems'].append(up_folder)



        file_list = [f for f in os.listdir(path) if not f.startswith('.')]
        file_list.sort()
        for name in file_list:
            if os.path.isdir(os.path.join(path, name)):
                menuItem = {}
                iconFile = os.path.join(libraryIconsPath, "folder.png")
                menuItem['icon'] = bpy.data.images.load(filepath = iconFile)
                self.imageList.append(menuItem['icon'].filepath_raw)
                menuItem['text'] = name
                menuItem['isFolder'] = True
                menuItem['subItems'] = []
                parentItem['subItems'].append(menuItem)

                #self.tree_index += 1

                self.buildAssetTree(menuItem, os.path.join(path, name))



        obj_list = [item for item in file_list if item[-3:] == 'obj']

        for name in obj_list:
            objItem = {}

            iconFile = os.path.join(path, name.replace('obj','png'))
            if not os.path.exists(iconFile):
                iconFile = os.path.join(libraryIconsPath, "nothumbnail.png")

            objItem['icon'] = bpy.data.images.load(filepath = iconFile)
            self.imageList.append(objItem['icon'].filepath_raw)
            text = os.path.splitext(name)[0]
            objItem['text'] = text
            objItem['isFolder'] = False
            objItem['filename'] = os.path.join(path, name)
            parentItem['subItems'].append(objItem)

        #pprint.pprint(parentItem)

    def browse_assets(self, path):

        def up_folder(self):
            # Create 'up' directory to go to previus dir (if we are not in the)
            menuItem = {}
            iconFile = os.path.join(libraryIconsPath, "folder.png")
            menuItem['icon'] = bpy.data.images.load(filepath = iconFile)
            self.imageList.append(menuItem['icon'].filepath_raw)
            menuItem['text'] = '..'
            menuItem['isFolder'] = True
            self.current_dir_content.append(menuItem)


        user_preferences = bpy.context.user_preferences
        addon_prefs = user_preferences.addons[__name__].preferences

        file_list = [f for f in os.listdir(path) if not f.startswith('.')]
        file_list.sort()
        self.current_dir_content = []

        if path != libraryDefaultModelsPath:
            if addon_prefs.custom_library_path:
                if addon_prefs.custom_library_path != os.path.join(path, ''):
                    up_folder(self)
            else:
                up_folder(self)
        else:
            if addon_prefs.custom_library_path:
                menuItem = {}
                iconFile = os.path.join(libraryIconsPath, "folder.png")
                menuItem['icon'] = bpy.data.images.load(filepath = iconFile)
                self.imageList.append(menuItem['icon'].filepath_raw)
                menuItem['text'] = addon_prefs.custom_library_path
                menuItem['isFolder'] = True
                self.current_dir_content.append(menuItem)

        for name in file_list:
            if os.path.isdir(os.path.join(path, name)):
                menuItem = {}
                iconFile = os.path.join(libraryIconsPath, "folder.png")
                menuItem['icon'] = bpy.data.images.load(filepath = iconFile)
                self.imageList.append(menuItem['icon'].filepath_raw)
                menuItem['text'] = name
                menuItem['isFolder'] = True
                self.current_dir_content.append(menuItem)
                self.tree_index = path

        obj_list = [item for item in file_list if item[-3:] == 'obj']

        for name in obj_list:
            objItem = {}

            iconFile = os.path.join(path, name.replace('obj','png'))
            if not os.path.exists(iconFile):
                iconFile = os.path.join(libraryIconsPath, "nothumbnail.png")

            objItem['icon'] = bpy.data.images.load(filepath = iconFile)
            self.imageList.append(objItem['icon'].filepath_raw)
            text = os.path.splitext(name)[0]
            objItem['text'] = text
            objItem['isFolder'] = False
            objItem['filename'] = os.path.join(path, name)
            self.current_dir_content.append(objItem)


    def __del__(self):
        # print("End")
        self.clearImages()

    def invoke(self, context, event):
        if context.area.type == 'VIEW_3D':


            self.mouseX = event.mouse_region_x
            self.mouseY = event.mouse_region_y

            self.mainItem = {}
            self.current_dir_content = []
            self.imageList = []
            self.buildAssetTree(self.mainItem, libraryDefaultModelsPath)
            self.browse_assets(libraryDefaultModelsPath)

            self.activeItem = self.mainItem

            # the arguments we pass the the callback
            args = (self, context)
            # Add the region OpenGL drawing callback
            # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
            self._handle = bpy.types.SpaceView3D.draw_handler_add(drawCallbackMenu, args, 'WINDOW', 'POST_PIXEL')

            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "View3D not found, cannot show asset flinger")
            return {'CANCELLED'}

# store keymaps here to access after registration
addon_keymaps = []

def menu_draw(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(AssetFlingerMenu.bl_idname, icon='MOD_SCREW')

def register():
    bpy.utils.register_class(AssetFlingerMenu)
    bpy.types.INFO_MT_mesh_add.append(menu_draw)
    bpy.utils.register_class(AssetFlingerPreferences)

    # handle the keymap
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new('view3d.asset_flinger', 'A', 'PRESS', ctrl=True, shift=True, alt=True)
        kmi = km.keymap_items.new('export_scene.obj', 'E', 'PRESS', ctrl=True, shift=True, alt=True)
        kmi.properties.use_selection = True
        kmi.properties.use_mesh_modifiers = False



        '''
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Asset Flinger', space_type='EMPTY')

    kmi = km.keymap_items.new('view3d.asset_flinger', 'A', 'PRESS', ctrl=True, shift=True, alt=True)
    kmi = km.keymap_items.new('export_scene.obj', 'E', 'PRESS', ctrl=True, shift=True, alt=True)
    kmi.properties.use_selection = True
    kmi.properties.use_mesh_modifiers = False
    '''

    addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(AssetFlingerMenu)
    bpy.utils.unregister_class(AssetFlingerPreferences)

    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
