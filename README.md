<h4>Summary</h4>

In essence, this addon allows the 'border render' feature of blender to be animated by tracking a selected object or group. So, if you have an animation that has an object animating across the screen the border render will update every frame so that the object (or group of objects) is always encompassed. 

There are a few reasons why you might want to animate the border render. You might want to render a preview of an animated object but don't want to waste processing time on background objects. Or, a portion of the image has a transparent background and you want to skip rendering the transparent areas (which, despite being empty still take time to process) and focus all processing power on the selected object.

The tracking of an object/group is either done by looking at the bounding box of each object or, the slower, but more precise method of looking at each vertex of the object and calculating how large the border render will need to be to cover the object/group.

<h4>Advantages</h4>

• Blank space will not be rendered.

• Preview or final quality renders can be focused to specific objects/groups.

<h4>Limitations</h4>

• Currently only mesh objects can be tracked. This will hopefully improved in future. The current workaround would be to animate a plane which covers the object when viewed from the camera and track that.

• Because a custom render operator is needed to allow the border box to update each frame the render cannot be cancelled like normal renders can. The render can only be cancelled by closing Blender. Because of this, a warning pop-up will appear to notifiy the user to warn them of this (not currently coded).

<h4>Options</h4>

• Either 'Object' tracking, for a single object, or 'Group' tracking, for multiple objects can be selected.

• The object or group to be tracked is selected from a drop down box.

• Tracking can be set to use the object's/group's bounding box for tracking (can be imprecise, but faster) or the object's/group's vertices (very precise, but slower, particualrly with groups).

• A 'Margin' property to expand or contract the border (useful when using the less precise bounding box tracking) can be set (default 3).

• An option to draw the bounding box of each object (or each object in the group). This can be useful to determine which tracking option (bounding box/vertex) might be more suitable.
