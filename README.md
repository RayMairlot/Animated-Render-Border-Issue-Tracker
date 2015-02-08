Intro
------------------------

The ‘Border render’ feature of blender is a great tool to quickly preview a portion of the image, saving time, as the whole image isn’t being rendered, allowing you to focus render power on specific areas. However, the default border render is fixed in position, so if you are rendering an animation with a moving object you can no longer focus all render power on that object. Or, you can, but you would have to make the border render area large enough that it encompasses any part of the image that the object moves to.

This script (soon to be addon) aims to remove that limitation by allowing the border render to track an object or group for the duration of the render.

Advantages
------------------------

•	Preview renders of specific objects only:

Having a border render that tracks an object means you can now render an entire image sequence, presumably for the purposes of testing, with no render power being wasted on other details in the scene. 

•	Blank space will not be rendered:

The second advantage is that blank space will no longer be rendered. While blank space in a render (found when separating objects onto their own render layers, with a transparent background enabled) renders quickly, it does take some time to process that space. Even though we may know it’s going to be blank, the renderer won’t know until it has attempted to render it. We help the render out by using border render, meaning anything outside the border render area will be ignored.

Limitations
------------------------

Ideally, you would be able to have different render borders for each render layer, allowing you to render all render layers at once, with each layer isolating the correct objects. I’m not entirely sure that it’s possible to detect which render layer the renderer is currently rendering, only that it is rendering at all. So, you can either use this animated render border script for testing purposes, draft renders and so on, or, you could render the entire render layer out as an image sequence, using the addon, and then import the rendered sequence back into the compositor to combine with your other rendered layers.

Another limitation is that only mesh objects will currently be tracked. Meshes have the option to be tracked via checking vertices or the bounding box of the object, and while objects that don’t have vertices, such as empties do have a bounding box, I have found that they don’t quite track properly compared to meshes. 
