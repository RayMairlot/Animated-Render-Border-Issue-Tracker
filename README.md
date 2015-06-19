<h4>Summary<h4>

Rendering an image that has a transparent background means both Cycles and the Blender Internal renderer will spend some time rendering those transparent areas. _We_ know the area is transparent and doesn't need to be rendered, but the renderer only knows that after doing some processing. We can help the renderer along by using the 'Border Render' feature of Blender to isolate our object and skip the rendering of uneccessary parts of the image. While this works for static objects, an animated object cannot benefit from this optimisation as much because the border render area would have to be large enough to encompass the object for the duration of the render.

This addon aims to remove that limitation by allowing the border render to track an object or group for the duration of the render by adjusting the border render for every frame of the animation. It does this either by looking at the bounding box of each object or the slower, but more precise method of looking at each vertex of the object and calculating how large the border render will need to be to cover the object/group.   

<h4>Advantages<h4>

• Blank space will not be rendered.

• Preview or final quality renders can be focused to specific objects/groups.

<h4>Limitations<h4>

• Currently only mesh objects can be tracked. This will hopefully improved in future. The current workaround would be to animate a plane which covers the object when viewed from the camera and track that.

• To adjust the border render per frame seems to require a custom render function. This, unfotunately, means the render cannot be cancelled once started without closing blender.
