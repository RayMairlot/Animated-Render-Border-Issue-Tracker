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
    "version": (1, 1),
    "blender": (2, 74, 0),
    "location": "Properties> Render> Animated Render Border",
    "category": "Render"}

import bpy
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
from bpy.app.handlers import persistent

trackableObjectTypes = ["MESH", "FONT", "CURVE", "SURFACE", "META", "LATTICE", "EMPTY", "SPEAKER", "CAMERA", "LAMP"]
noVertexObjectTypes = ["FONT", "META", "EMPTY", "SPEAKER", "CAMERA", "LAMP"]

#######Update functions########################################################


def updateFrame(self,context):
    
    bpy.context.scene.frame_set(bpy.context.scene.frame_current)       
     
   
   
def refreshTracking(self,context):
       
    border = context.scene.animated_render_border
   
    if border.type == "Object":
       
        if bpy.data.objects[border.object].type in noVertexObjectTypes: #Objects that don't have vertices
           
            border.use_bounding_box = True         
   
    bpy.context.scene.frame_set(bpy.context.scene.frame_current)    
    
    updateBoundingBox(self,context)       
                   


def updateBoundingBox(self,context):
        
    border = context.scene.animated_render_border
        
    if border.type == "Object" and border.object != "" and border.object in bpy.data.objects:  #If object is chosen as object but renamed, it can't be tracked.

        bpy.data.objects[border.object].show_bounds = border.draw_bounding_box
        
    elif border.type == "Group" and border.group != "" and border.group in bpy.data.groups:
        
        for object in bpy.data.groups[border.group].objects:
            
            if object.type in trackableObjectTypes: #Types of object that can be tracked
               
                object.show_bounds = border.draw_bounding_box
                                            


def toggleTracking(self,context):
    
    border = context.scene.animated_render_border
    
    if border.enable and not context.scene.render.use_border:
        context.scene.render.use_border = True

    if border.enable:      
        updateObjectList(self)
        
    updateFrame(self,context)



def updateBorderWithMinX(self,context):

    border = bpy.context.scene.animated_render_border     
    context.scene.render.border_min_x = border.border_min_x
     
def updateBorderWithMaxX(self,context):

    border = bpy.context.scene.animated_render_border     
    context.scene.render.border_max_x = border.border_max_x
    
def updateBorderWithMinY(self,context):

    border = bpy.context.scene.animated_render_border     
    context.scene.render.border_min_y = border.border_min_y
    
def updateBorderWithMaxY(self,context):

    border = bpy.context.scene.animated_render_border     
    context.scene.render.border_max_y = border.border_max_y            

          
          
@persistent          
def updateObjectList(scene):
            
    border = bpy.context.scene.animated_render_border     
    
    if border.enable:        
        border.mesh_objects.clear()
        for object in bpy.context.scene.objects:
            if object.type in trackableObjectTypes: #Types of object that can be tracked
                meshAdd = border.mesh_objects.add()
                meshAdd.name = object.name                                          


#########Properties###########################################################


class animatedBorderRenderProperties(bpy.types.PropertyGroup):
    
    mesh_objects = bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)

    object = bpy.props.StringProperty(description = "The object to track", update=refreshTracking)

    group = bpy.props.StringProperty(description = "The group to track", update=refreshTracking)

    type = bpy.props.EnumProperty(description = "The type of tracking to do, objects or groups", items=[
                                                                                                        ("Object","Object","Object"),
                                                                                                        ("Group","Group","Group"),
                                                                                                        ("Keyframe","Keyframe","Keyframe")], update=refreshTracking)

    use_bounding_box = bpy.props.BoolProperty(default=True, description="Use object's bounding box (less reliable, quicker) or object's vertices for boundary checks", update=updateFrame)

    margin = bpy.props.IntProperty(default=3, description="Add a margin around the object's bounds", update=updateFrame)

    draw_bounding_box = bpy.props.BoolProperty(default=False, description="Draw the bounding boxes of the objects being tracked", update=updateBoundingBox)

    enable = bpy.props.BoolProperty(default=False, description="Animated Render Border", update=toggleTracking)
    
    border_min_x = bpy.props.FloatProperty(description="Minimum X value for the render border", min=0, max=1, update=updateBorderWithMinX)
    
    border_max_x = bpy.props.FloatProperty(description="Maximum X value for the render border", min=0, max=1, update=updateBorderWithMaxX)

    border_min_y = bpy.props.FloatProperty(description="Minimum Y value for the render border", min=0, max=1, update=updateBorderWithMinY)

    border_max_y = bpy.props.FloatProperty(description="Maximum Y value for the render border", min=0, max=1, update=updateBorderWithMaxY)    


bpy.utils.register_class(animatedBorderRenderProperties)


bpy.types.Scene.animated_render_border = bpy.props.PointerProperty(type=animatedBorderRenderProperties)


#########Frame Handler########################################################

bpy.app.handlers.frame_change_post.clear()
bpy.app.handlers.scene_update_post.clear()

@persistent
def animate_render_border(scene):
        
    scene = bpy.context.scene
    camera = scene.camera
    border = scene.animated_render_border
    
    cameraExists = False
    
    if camera:
        if camera.type == "CAMERA":
            cameraExists = True
    
    if border.enable and cameraExists:
        #If object is chosen but consequently renamed, it can't be tracked.
        if border.type == "Object" and border.object != "" and border.object in bpy.data.objects or \
           border.type == "Group" and border.group != "" and border.group in bpy.data.groups: 
        
            objs = [] 
            if border.type == "Object":  
                objs = [border.object]
            elif border.type == "Group":
                objs = (object.name for object in bpy.data.groups[border.group].objects if object.type in trackableObjectTypes) #Type of objects that can be tracked
            
            coords_2d = []
            for obj in objs:
                
                verts = []
                if border.use_bounding_box or bpy.data.objects[obj].type in noVertexObjectTypes: #Objects that have no vertices
                
                    verts = (Vector(corner) for corner in bpy.data.objects[obj].bound_box)
                
                elif bpy.data.objects[obj].type == "MESH":
                
                    verts = (vert.co for vert in bpy.data.objects[obj].data.vertices)
                
                elif bpy.data.objects[obj].type == "CURVE":
                    
                    verts = (vert.co for spline in bpy.data.objects[obj].data.splines for vert in spline.bezier_points)
                
                elif bpy.data.objects[obj].type == "SURFACE":
                    
                    verts = (vert.co for spline in bpy.data.objects[obj].data.splines for vert in spline.points)
                    
                elif bpy.data.objects[obj].type == "LATTICE":
                
                    verts = (vert.co for vert in bpy.data.objects[obj].data.points)
                        
                wm = bpy.data.objects[obj].matrix_world     #Vertices will be in local space unless multiplied by the world matrix
                for coord in verts:
                    coords_2d.append(world_to_camera_view(scene, camera, wm*coord))

            minX = 1
            maxX = 0
            minY = 1
            maxY = 0
            
            for x, y, distance_to_lens in coords_2d:
                                
                #Points behind camera will have negative coordinates, this makes them positive                
                if distance_to_lens<0:
                    y = y *-1
                    x = x *-1               
                
                if x<minX:
                    minX = x
                if x>maxX:
                    maxX = x
                if y<minY:
                    minY = y
                if y>maxY:
                    maxY = y
                                        
            margin = border.margin/100
                
            scene.render.border_min_x = minX - margin
            scene.render.border_max_x = maxX + margin
            scene.render.border_min_y = minY - margin
            scene.render.border_max_y = maxY + margin
            
        elif border.type == "Keyframe":
            
            scene.render.border_min_x = border.border_min_x
            scene.render.border_max_x = border.border_max_x
            scene.render.border_min_y = border.border_min_y
            scene.render.border_max_y = border.border_max_y
          
           

###########Operators############################################################


def mainRender(context):
                
    oldStart = context.scene.frame_start
    oldEnd = context.scene.frame_end
    oldCurrent = context.scene.frame_current
    
    context.window_manager.progress_begin(0,oldEnd)
    
    for i in range(oldStart, oldEnd+1):
    
        context.window_manager.progress_update(i)
                
        context.scene.frame_set(i)
        animate_render_border(context.scene)
        
        context.scene.frame_start = i
        context.scene.frame_end = i
         
        bpy.ops.render.render(animation=True)
    
    context.window_manager.progress_end()
    
    context.scene.frame_current = oldCurrent    
    context.scene.frame_start = oldStart
    context.scene.frame_end = oldEnd
    
    
def mainFix(context):
                
    context.scene.render.use_border = True
    
    
def insertKeyframe(context):
    
    border = context.scene.animated_render_border
    
    border.border_min_x = context.scene.render.border_min_x
    border.border_min_y = context.scene.render.border_min_y
    border.border_max_x = context.scene.render.border_max_x
    border.border_min_y = context.scene.render.border_min_y
    border.border_max_y = context.scene.render.border_max_y            
    
    context.scene.keyframe_insert(data_path="animated_render_border.border_min_x")  
    context.scene.keyframe_insert(data_path="animated_render_border.border_max_x")  
    context.scene.keyframe_insert(data_path="animated_render_border.border_min_y")  
    context.scene.keyframe_insert(data_path="animated_render_border.border_max_y")    
    
    
def deleteKeyframe(context):

    context.scene.keyframe_delete(data_path="animated_render_border.border_min_x")  
    context.scene.keyframe_delete(data_path="animated_render_border.border_max_x")  
    context.scene.keyframe_delete(data_path="animated_render_border.border_min_y")  
    context.scene.keyframe_delete(data_path="animated_render_border.border_max_y")   
    


###########UI################################################################


class RENDER_PT_animated_render_border(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Animated Render Border"
    bl_idname = "RENDER_PT_animated_render_border"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"


    def draw_header(self, context):

        self.layout.prop(context.scene.animated_render_border, "enable", text="")


    def draw(self, context):
                        
        layout = self.layout
        scene = context.scene
        border = context.scene.animated_render_border
        
        layout.active = scene.animated_render_border.enable
        
        if not context.scene.render.use_border and border.enable:
            row = layout.row()
            split = row.split(0.7)
            
            column = split.column()
            column.label(text="'Border' is disabled in", icon="ERROR")
            column.label(text="'Dimensions' panel.", icon="SCULPT_DYNTOPO")
            
            column = split.column()         
            column.operator("render.animated_render_border_fix", text="Fix")
        
        if scene.camera:    
            if scene.camera.type != "CAMERA":
                row = layout.row()
                row.label(text="Active camera must be a Camera", icon="ERROR")
                row = layout.row()
                row.label(text="object, not '"+scene.camera.type.lower().capitalize()+"'.", icon="SCULPT_DYNTOPO")
        
        column = layout.column()
        row = column.row()
        row.prop(scene.animated_render_border, "type",expand=True)
        row = column.row()
        
        
        if border.type == "Keyframe":
        
            column = layout.column()
            column.active = context.scene.render.use_border and border.enable
            
            col = column.column(align=True)
            col.operator("render.animated_render_border_insert_keyframe", text="Insert Keyframe", icon="KEY_HLT")
            col.operator("render.animated_render_border_delete_keyframe", text="Delete Keyframe", icon="KEY_DEHLT")    
            col.label(text="Border Vales:")          
            row = column.row()
            row.label(text="")
            row.prop(scene.animated_render_border, "border_max_y", text="Max Y")  
            row.label(text="")
            row = column.row(align=True)
            row.prop(scene.animated_render_border, "border_min_x", text="Min X")  
            row.label(text="")
            row.prop(scene.animated_render_border, "border_max_x", text="Max X")  
            row = column.row()
            row.label(text="")
            row.prop(scene.animated_render_border, "border_min_y", text="Min Y")        
            row.label(text="")                           
            
        else:
            
            if border.type == "Object":
                row.label(text="Mesh object to track:")
                row = column.row()
                
                objectIcon = "OBJECT_DATA"
                if border.object != "" and border.object in bpy.data.objects:
                    objectIcon = bpy.data.objects[border.object].type+"_DATA"
                    
                    if bpy.data.objects[border.object].type == "SPEAKER":   
                        objectIcon = "SPEAKER" #Speaker doesn't have it's own icon like other objects
                    
                row.prop_search(scene.animated_render_border, "object", scene.animated_render_border, "mesh_objects", text="", icon=objectIcon) #Where my property is, name of property, where list I want is, name of list
            else:
                row.label(text="Group to track:")
                row = column.row()
                row.prop_search(scene.animated_render_border, "group", bpy.data, "groups", text="")
            
            
            if border.type == "Object" and border.object == "" or \
               border.type == "Group" and border.group == "":
                                
                enabled = False
            else:
                enabled = True
            
            #New column is to separate it from previous row, it needs to be able to be disabled.
            columnMargin = row.column()
            columnMargin.enabled = enabled    
            columnMargin.prop(scene.animated_render_border, "margin", text="Margin")    
            
            row = column.row()
            
            noVertices = False
            
            if border.type == "Object" and border.object != "" and border.object in bpy.data.objects:
                
                if bpy.data.objects[border.object].type in noVertexObjectTypes: #Objects without vertices
                    
                    noVertices = True
                                            
            if noVertices:    
                row.enabled = False
            else:
                row.enabled = True   
            row.prop(scene.animated_render_border, "use_bounding_box", text="Use Bounding Box")
            
            row = column.row()
            row.enabled = enabled           
            row.prop(scene.animated_render_border, "draw_bounding_box", text="Draw Bounding Box")
                
            row = column.row()     
            row.enabled = enabled      
            row.operator("render.animated_render_border_render", text="Render Animation", icon="RENDER_ANIMATION")
        
       

class RENDER_OT_animated_render_border_render(bpy.types.Operator):
    """Render the sequence using the animated render border"""
    bl_idname = "render.animated_render_border_render"
    bl_label = "Render Animation"

    def invoke(self, context, event):
        
        return context.window_manager.invoke_props_dialog(self, width=340, height = 300)


    def draw(self, context):
        layout = self.layout

        if bpy.context.scene.camera:               
            row = layout.row()
            row.label("Once the render has started it cannot be easily stopped unless", icon="INFO")
            row = layout.row()
            row.label("you close Blender. Make sure your work is saved if necessary.")  
            row = layout.row()
                
            row.label("Press 'OK' to render or press the 'Esc' key on the keyboard")
            row = layout.row()
            row.label("to cancel.")  
        else:
            row = layout.row()
            row.label("No active camera to render from", icon="ERROR")        


    def execute(self, context):
        
        if bpy.context.scene.camera:
            mainRender(context)
        else:
            pass
            
        return {'FINISHED'}
    
        
class RENDER_OT_animated_render_border_fix(bpy.types.Operator):
    """Fix the render border by turning on 'Border' rendering"""
    bl_idname = "render.animated_render_border_fix"
    bl_label = "Render Border Fix"

    def execute(self, context):
 
        mainFix(context)
            
        return {'FINISHED'}    
    
    
class RENDER_OT_animated_render_border_insert_keyframe(bpy.types.Operator):
    """Insert a keyframe for all the render border values"""
    bl_idname = "render.animated_render_border_insert_keyframe"
    bl_label = "Insert Animated Render Border Keyframe"

    def execute(self, context):
     
        insertKeyframe(context)
            
        return {'FINISHED'}  
    
    
class RENDER_OT_animated_render_border_delete_keyframe(bpy.types.Operator):
    """Delete a keyframe for all the render border values"""
    bl_idname = "render.animated_render_border_delete_keyframe"
    bl_label = "Delete Animated Render Border Keyframe"

    def execute(self, context):
     
        deleteKeyframe(context)
            
        return {'FINISHED'}       
            


def register():
    
    bpy.app.handlers.frame_change_post.append(animate_render_border)
    bpy.app.handlers.scene_update_post.append(updateObjectList)
    
    bpy.utils.register_class(RENDER_PT_animated_render_border)
    bpy.utils.register_class(RENDER_OT_animated_render_border_render)
    bpy.utils.register_class(RENDER_OT_animated_render_border_fix)
    bpy.utils.register_class(RENDER_OT_animated_render_border_insert_keyframe)   
    bpy.utils.register_class(RENDER_OT_animated_render_border_delete_keyframe)        
    
    
def unregister():
    
    bpy.app.handlers.frame_change_post.remove(animate_render_border)        
    bpy.app.handlers.scene_update_post.remove(updateObjectList)
    
    bpy.utils.unregister_class(RENDER_PT_animated_render_border)
    bpy.utils.unregister_class(RENDER_OT_animated_render_border_render)
    bpy.utils.unregister_class(RENDER_OT_animated_render_border_fix)
    bpy.utils.unregister_class(RENDER_OT_animated_render_border_insert_keyframe)    
    bpy.utils.unregister_class(RENDER_OT_animated_render_border_delete_keyframe)        
    bpy.utils.unregister_class(animatedBorderRenderProperties)
    
    del bpy.types.Scene.animated_render_border
    

if __name__ == "__main__":
    register()