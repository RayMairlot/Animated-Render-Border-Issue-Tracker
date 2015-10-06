###Changelog:
---

####V2.0

#####Changes:

+ Renders can now be cancelled by pressing the 'Esc' key during a render. However, the frame currently being rendered has to finish before the rendering will stop.

+ Now FONT, CURVE, SURFACE, META, LATTICE and ARMATURE objects can be tracked in addition to MESH objects. Font and META objects can only be tracked via their bounding boxes, other objects can use bounding box or 'inner points' (vertices, lattice points, curve points etc.). Lattice and Armature objects require Blender 2.76 or later to be able to use 'bounding box' method, otherwise they will fall back to 'inner points'.

+ As an alternative to 'tracking' objects, the border and it's invidividual values can now be keyframed in the new 'Keyframe' mode.

+ A border dimensions label can be turned on in the add-on's user preferences which will display the size of the border in pixels, below the 'Render Animation' button.

+ New warnings for: Object to track not existing, group to track not existing and the selected group being empty. 

+ Most warnings now stop the render from being started until they have been fixed apart from warnings about using version of Blender previous to version 2.76 (see User Guide> Warnings for more information).

+ Exceptions are now raised when calling `bpy.ops.render.animated_render_border_render()` from a script for any warning that would normally be displayed via the UI.

+ Camera's 'Shift X' and 'Shift Y' properties are now taken into account when calculating the render border.

+ 'Frame Step' and 'Aspect ratio' properties in the Render> Dimensions panel are taken into account when calculating the render border.
	
+ Bounding boxes are now disable or enabled when changing tracking modes, the selected object or the  selected group so you won't be left with lots of objects with their bounding boxes visible.
	
+ The 'User guide' document now includes the Python api commands to manipulate all the 'Animated Render Border' properties/tools via a script.

+ Updated the 'User Guide' to take into account all changes, with explanations for new features and workflows.

#####Fixes:

+ Fixed a bug where points behind camera were incorrectly calculated.
