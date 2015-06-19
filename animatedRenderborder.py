# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Animated Render Border",
    "description": "Track objects or groups with the border render",
    "author": "Ray Mairlot",
    "version": (1, 0),
    "blender": (2, 74, 0),
    "location": "Properties> Render> Animated Render Border",
    "category": "Render"}

import bpy
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view


#######Update functions########################################################



def fakeUpdate(self,context):
    
    bpy.context.scene.frame_set(bpy.context.scene.frame_current)    
    
    

def trackUpdate(self,context):
    
    scene = bpy.context.scene
        
    if scene.animated_render_border_type == "Group":
        if scene.animated_render_border_group == "":
            scene.render.use_border = False
        else:
            scene.render.use_border = True
            scene.frame_set(bpy.context.scene.frame_current)
    else:
        if scene.animated_render_border_object == "":
            scene.render.use_border = False
        else:
            scene.render.use_border = True
            scene.frame_set(bpy.context.scene.frame_current)        
            
            

def updateBoundingBox(self,context):
    
    scene = bpy.context.scene
        
    if scene.animated_render_border_type == "Object":
        
        bpy.data.objects[scene.animated_render_border_object].show_bounds = scene.animated_render_border_draw_bounding_box
        
    else:
        
        for object in bpy.data.groups[scene.animated_render_border_group].objects:
            
            object.show_bounds = scene.animated_render_border_draw_bounding_box
                            


def updateObjectList(self,context):
    
    updateObjectListMain()
    
    
def updateObjectListMain(scene):
        
    bpy.context.scene.animated_render_border_mesh_objects.clear()
    for object in bpy.context.scene.objects:
        if object.type == "MESH":
            meshAdd = bpy.context.scene.animated_render_border_mesh_objects.add()
            meshAdd.name = object.name                                          


#########Properties###########################################################

bpy.types.Scene.animated_render_border_mesh_objects = bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)

bpy.types.Scene.animated_render_border_object = bpy.props.StringProperty(description = "The object to track", update=trackUpdate)

bpy.types.Scene.animated_render_border_group = bpy.props.StringProperty(description = "The group to track", update=trackUpdate)

bpy.types.Scene.animated_render_border_type = bpy.props.EnumProperty(description = "The type of tracking to do, objects or groups", items=[("Object","Object","Object"),("Group","Group","Group")], update=trackUpdate)

bpy.types.Scene.animated_render_border_use_bounding_box = bpy.props.BoolProperty(default=True, description="Use object's bounding box (less reliable, quicker)or object's vertices for boundary checks", update=fakeUpdate)

bpy.types.Scene.animated_render_border_margin = bpy.props.IntProperty(default=3, description="Add a margin around the object's bounds", update=fakeUpdate)

bpy.types.Scene.animated_render_border_draw_bounding_box = bpy.props.BoolProperty(default=False, description="Draw the bounding boxes of the objects being tracked", update=updateBoundingBox)

bpy.types.Scene.animated_render_border_enable = bpy.props.BoolProperty(default=False, description="Animated Render Border", update=updateObjectList)


#########Frame Handler########################################################


def animate_render_border(scene):
    
    scene = bpy.context.scene
    camera = bpy.data.objects['Camera']
    
    if scene.animated_render_border_type == "Object" and scene.animated_render_border_object != "" or \
       scene.animated_render_border_type == "Group" and scene.animated_render_border_group != "":
    
        objs = [] 
        if scene.animated_render_border_type == "Object": 
            objs = [scene.animated_render_border_object]
        else:
            objs = (object.name for object in bpy.data.groups[scene.animated_render_border_group].objects if object.type =="MESH")
        
        
        coords_2d = []
        for obj in objs:
            
            verts = []
            if scene.animated_render_border_use_bounding_box:
                verts = (Vector(corner) for corner in bpy.data.objects[obj].bound_box)
            else:
                verts = (vert.co for vert in bpy.data.objects[obj].data.vertices)
                    
            wm = bpy.data.objects[obj].matrix_world     #Vertices will be in local space unless multiplied by the world matrix
            for coord in verts:
                coords_2d.append(world_to_camera_view(scene, camera, wm*coord))

        minX = 1
        maxX = 0
        minY = 1
        maxY = 0

        for x, y, distance_to_lens in coords_2d:
            
            if x<minX:
                minX = x
            if x>maxX:
                maxX = x
            if y<minY:
                minY = y
            if y>maxY:
                maxY = y                 
                
        margin = bpy.context.scene.animated_render_border_margin
            
        scene.render.border_min_x = minX - (margin/100)
        scene.render.border_max_x = maxX + (margin/100)
        scene.render.border_min_y = minY - (margin/100)
        scene.render.border_max_y = maxY + (margin/100)  
    
    

###########RENDER############################################################


def main(context):
    
    oldStart = bpy.context.scene.frame_start
    oldEnd = bpy.context.scene.frame_end
    
    for i in range(1, oldEnd+1):
        
        bpy.context.scene.frame_set(i)
        animate_render_border(context.scene)
        
        bpy.context.scene.frame_start = i
        bpy.context.scene.frame_end = i
         
        bpy.ops.render.render(animation=True)
        
    bpy.context.scene.frame_start = oldStart
    bpy.context.scene.frame_end = oldEnd


###########UI################################################################



class AnimatedRenderBorderPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Animated Render Border"
    bl_idname = "RENDER_PT_animated_render_border"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"


    def draw_header(self, context):

        self.layout.prop(context.scene, "animated_render_border_enable", text="")


    def draw(self, context):
                
        layout = self.layout
        scene = context.scene
        
        layout.active = scene.animated_render_border_enable
        
        row = layout.row()
        row.prop(scene, "animated_render_border_type",expand=True)
        row = layout.row()
        
        if scene.animated_render_border_type == "Object":
            row.label(text="Mesh object to track:")
            row = layout.row()
            row.prop_search(scene, "animated_render_border_object", scene, "animated_render_border_mesh_objects", text="", icon="OBJECT_DATA") #Where my property is, name of property, where list I want is, name of list
        else:
            row.label(text="Group to track:")
            row = layout.row()
            row.prop_search(scene, "animated_render_border_group", bpy.data, "groups", text="")
        
        
        if scene.animated_render_border_type == "Object" and scene.animated_render_border_object == "" or \
           scene.animated_render_border_type == "Group" and scene.animated_render_border_group == "":
            
            enabled = False
            
        else:
            
            enabled = True
            
        column = row.column()      
        column.enabled = enabled
        column.prop(scene, "animated_render_border_margin", text="Margin")    
        
        row = layout.row()
        row.enabled = enabled       
        row.prop(scene, "animated_render_border_use_bounding_box", text="Use Bounding Box")
        
        row = layout.row()
        row.enabled = enabled           
        row.prop(scene, "animated_render_border_draw_bounding_box", text="Draw Bounding Box")
            
        row = layout.row()     
        row.enabled = enabled      
        row.operator("render.render_animated_render_border", text="Render", icon="RENDER_STILL")
        



class RenderAnimatedRenderBorder(bpy.types.Operator):
    """Render the sequence using the animated render border"""
    bl_idname = "render.render_animated_render_border"
    bl_label = "Render"

    def execute(self, context):
        main(context)
        return {'FINISHED'}



def register():
    bpy.utils.register_class(AnimatedRenderBorderPanel)
    bpy.utils.register_class(RenderAnimatedRenderBorder)
    
    bpy.app.handlers.frame_change_pre.append(animate_render_border)
    bpy.app.handlers.scene_update_post.append(updateObjectListMain)
    
    

def unregister():
    bpy.utils.unregister_class(AnimatedRenderBorderPanel)
    bpy.utils.unregister_class(RenderAnimatedRenderBorder)
    
    bpy.app.handlers.frame_change_pre.remove(animate_render_border)        
    bpy.app.handlers.scene_update_post.remove(updateObjectListMain)


if __name__ == "__main__":
    register()