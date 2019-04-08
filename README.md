:information_source: *While the source code for this add-on is available here for free, if this add-on has helped you please do consider supporting me by buying it on the blender market: https://blendermarket.com/products/animated-render-border/*

:information_source: **Updating the Add-on for Blender 2.8**: A mostly working version is available on the branch [here](https://github.com/RayMairlot/Animated-Render-Border/tree/2.8-Update), though I have found tracking to be slightly inconsistent when rendering sometimes. Feel free to report problems about using the add-on with 2.8 (or regarding other issues) on the [issues](https://github.com/RayMairlot/Animated-Render-Border/issues) page.

---

## About Animated Render Border

In essence, this addon allows the 'border render' feature of blender to be animated by tracking a selected object or group. So, if you have an animation that has an object animating across the screen the border render will update every frame so that the object (or group of objects) is always encompassed. 

There are a few reasons why you might want to animate the border render. You might want to render a preview of an animated object but don't want to waste processing time on background objects. Or, apart from the tracked objects the image has a transparent background and you want to skip rendering the transparent areas (which, despite being empty still take time to process) and focus all processing power on the selected object.

The tracking of an object/group is either done by looking at the bounding box of each object or, the slower, but more precise method of looking at the 'inner points' of the object (e.g. vertices, lattice points or curve points, depending on object type) and calculate how large the border render will need to be to cover the object/group.

<h4>Advantages</h4>

• Blank space will not be rendered.

• Preview or final quality renders can be focused to specific objects/groups.

<h4>Limitations</h4>

• Because a custom render operator is needed to allow the border box to update each frame the render cannot be cancelled like normal renders can. Once the render is cancelled with the 'Esc' key the script will finish rendering the current frame and *then* cancel.

<h4>Options</h4>

• Either 'Object' tracking for a single object, 'Group' tracking for multiple objects or 'Keyframe' mode for animating the render border by hand.

• The object or group to be tracked is selected from a drop down box.

• Tracking can be set to use the object's/group's bounding box for tracking (can be imprecise, but faster) or the object's/group's 'inner points' (very precise, but slower, particualrly with groups).

• A 'Margin' property to expand or contract the border (useful when using the less precise bounding box tracking) can be set (default 3).

• An option to draw the bounding box of each object (or each object in the group). This can be useful to determine which tracking option (bounding box/vertex) might be more suitable.
