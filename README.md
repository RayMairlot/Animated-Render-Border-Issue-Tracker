# Animated Render Border

:information_source: *While the source code for this add-on is available here for free, if this add-on has helped you please do consider supporting me by buying it on the blender market: https://blendermarket.com/products/animated-render-border/*

:information_source: **Updating the Add-on for Blender 2.8**: See the ['Add-on Versions and Blender Compatibility'](#AddOnVersionsAndBlenderCompatability) section for information about 2.8.

![ARB Featured Image](/README%20images/ARB%20Github%20Featured%20Product%20image.png)

## :notebook: Contents
  
 - [About](#About)
 - [Add-on Versions and Blender Compatability](#AddOnVersionsAndBlenderCompatability)
   - [Compatibility](#Compatibility)
   - [Changelog](#Changelog)
 - [Installation](#Installation)
 - [Usage](#Usage)
   - [Steps to start using ‘Object’ or 'Collection’ tracking](#StepsToStartUsingObjectOrCollectionTracking)
   - [Steps to start using ‘Keyframe’ mode](#StepsToStartUsingKeyframeMode)
   - [Command Line Rendering](#CommandLineRendering)
 - [Options](#Options)
   - [Options for all 3 tracking modes](#OptionsForAll3TrackingModes)
   - [‘Object’ and ‘Collection’ tracking](#ObjectAndCollectionTracking)
   - ['Keyframe’ tracking](#KeyframeTracking)
 - [Warnings](#Warnings)
 - [User Preferences](#UserPreferences)
 - [Limitations](#Limitations)
   - [Object types which can't be tracked](#ObjectTypesWhichCantBeTracked)
   - [Different render borders for different render layers](#DifferentRenderBordersForDifferentRenderLayers)
   - ['Panoramic' lens types for cameras, e.g. Equirectangular, Mirror Ball etc.](#PanoramicLensTypesForCamerasEgEquirectangularMirrorBallEtc)
 
<br>

## <a name="About"></a>:information_source: About

This add-on makes the ‘render border’ feature in Blender adaptive so that the border updates its location and size every frame to always surround the selected object or collection of objects*, focusing your render power on just those specific parts of the image. You can scroll in the timeline to see the border update automatically and render when ready.

There is also a ‘Keyframe’ mode, to allow you to manually place and keyframe the position of the render border instead of tracking an object or collection.

The add-on looks at the bounding box of the object(s) selected to be tracked and will adjust the render border accordingly. Alternatively, objects can be tracked by analysing the ‘inner points’ of the object (vertices, lattice points, curve points etc.), which can be slower with complex objects, but very precise.

You can also always use the ‘margin’ feature of the add-on to make sure you’ve always got a ‘safe’ area around your tracked objects.

\**Tracking is enabled for the following object types: **Meshes, Text (Font) objects, Curves, Surfaces, Meta objects, Lattices and Armatures**.*

### Animated Render Border Panel:

|Object Mode|Collection Mode|Keyframe Mode|
|---|---|---|
|![Object Mode](/README%20images/Object%20Mode.png)|![Collection Mode](/README%20images/Collection%20Mode.png)|![Keyframe Mode](/README%20images/Keyframe%20Mode.png)|

<br>

## <a name="AddOnVersionsAndBlenderCompatability"></a>:heavy_check_mark: Add-on Versions and Blender Compatibility 

The add-on is currently being updated to be compatible with Blender 2.80, with further testing to be carried out when 2.80 has been released. The work is mostly done and is currently downloadable from the [2.80-Update branch](https://github.com/RayMairlot/Animated-Render-Border/tree/2.8-Update). This will be purely a compatability update and contains no new features. It will contain a few bug fixes which will also be applied to the 2.79 compatible version (possibly as 2.1.1).

### <a name="Compatibility"></a>Compatibility

While the table below describes the add-on in terms of Blender 2.79b and 2.80, versions 2.1 and lower *are* compatible with versions of Blender prior to 2.79b. Versions 1.0 and 1.1 were originally released as having been tested with Blender 2.74 and versions 2.0 and 2.1 were tested with 2.76, and, while *untested*, they should also be compatible with versions of Blender earlier than those. 

| Add-on Version | Blender 2.79b | Blender 2.80+ |
|:---:|:---:|:---:|
| 3.0* | :x: | :heavy_check_mark: |
| [2.1](https://github.com/RayMairlot/Animated-Render-Border/releases/tag/v1.1) | :heavy_check_mark: | :x: |
| [2.0](https://github.com/RayMairlot/Animated-Render-Border/releases/tag/v1.1) | :heavy_check_mark: | :x: |
| [1.1](https://github.com/RayMairlot/Animated-Render-Border/releases/tag/v1.1) | :heavy_check_mark: | :x: |
| [1.0](https://github.com/RayMairlot/Animated-Render-Border/releases/tag/v1.0) | :heavy_check_mark: | :x: |

**Not yet released.*

### <a name="Changelog"></a>Changelog

#### V2.1
 - Bug fixes
#### V2.0
 - Renders can now be properly cancelled.
 - Text (Font) objects, Curves, Surfaces, Meta objects, Lattices and Armatures can now be tracked, in addition to Mesh objects.
 - Render border can now be manually keyframed instead of tracking an object
 - Bug fixes
#### V1.1
 - Bug fixes
#### V1.0
 - Initial Release

<br>

Full Changelog available [here](Changelog.md).

<br>

## <a name="Installation"></a>:computer: Installation

For those familar with installing Blender add-ons, this add-on is no different (but make sure to install the .py file and not the Github .zip file). 

For those less familar, the steps to intsall it are below:

1. If you've downloaded one of the Github releases, unzip it and find the 'animatedRenderborder.py' file. If you already have the .py file, proceed to step 2.

2. Open Blender and open its *User Preferences* by going to *File> User Preferences* and navigate to the *Add-ons* tab.

3. Press the *Install from file* button and browse to and select the 'animatedRenderborder.py' file.

4. The add-on should then automatically appear, which you can then enable by clicking the checkbox next to it. Once enabled, the ‘Animated Render Border’ panel will appear at the bottom of the ‘Render’ tab of the ‘Properties’ area, where all the other render settings are.

<br>
  
## <a name="Usage"></a>:books: Usage

### <a name="StepsToStartUsingObjectOrCollectionTracking"></a>Steps to start using ‘Object’ or ‘Collection’ tracking

1. Enable tracking by clicking the checkbox next to the panel title.

2. If you are tracking a single object you can leave the tracking type on its default, otherwise change to ‘Collection’ tracking.

3. Choose the object (or collection) you wish to track by selecting it from the dropdown box. If this box is blank it means there are no trackable objects (or collections) in the scene.

4. Press <kbd>Numpad </kbd>' to look through the active camera.

You can now scroll in the timeline and, whether your object is animated or still, the render border will move to match the object’s position. You may wish to refine the tracking using the ‘Margin’ and ‘Use Bounding Box’ options. 

If you wish, your object can now be rendered (using the ‘Animated Render Border’ custom ‘Render Animation’ button) and the render border will update accordingly for each rendered frame.   

If you want to turn off tracking either temporarily or permanently you can click the checkbox next to the panel name.

### <a name="StepsToStartUsingKeyframeMode"></a>Steps to start using ‘Keyframe’ mode

1. Enable tracking by clicking the checkbox next to the panel title.

2. Change to ‘Keyframe’ tracking mode.

3. Press <kbd>Numpad 0</kbd> to look through the active camera.

4. Move to the frame in the timeline that you want to place the first keyframe for the render border on.

5. Either manipulate the ‘Min X’, ‘Max X’, ‘Min Y’ or ‘Max Y’ UI values or draw the border in the viewport using the regular <kbd>Ctrl</kbd>+<kbd>B</kbd> shortcut to define the size and position of the border.

    If you manually draw the border in the viewport the min/max values in the panel will not immediately update, instead, a ‘Refresh to synchronise border values’ button will appear, which, when pressed will update the values. Refreshing is only necessary if you wish to tweak the border values after manually drawing a border, otherwise you can insert a keyframe, shown in the next step, as normal.

6. Once you are happy with the size and position of the render border press the ‘Insert Keyframe’ button to insert a keyframe for all 4 border values. You can alternatively, right-click on an individual border value and choose ‘Insert Keyframe’ or simply press <kbd>I</kbd> while the cursor is over the value to insert a keyframe for just that value.

7. Repeat steps 4, 5 and 6 to insert keyframes for a different sized border on a different frame.

You can now scroll in the timeline and the border will move depending on the keyframes you have set. To remove a keyframe you can either do so via the ‘Dope Sheet’ editor, or by right-clicking on the keyframed value and choosing ‘Delete Keyframe’ or alternatively, you can use the ‘Delete Keyframe’ button in the panel, which will delete keyframes for all 4 values at once.

If you wish, your object can now be rendered (using the ‘Animated Render Border’ custom ‘Render Animation’ button) and the render border will update accordingly for each rendered frame.   

If you want to turn off tracking either temporarily or permanently you can click the checkbox next to the panel name.
  
### <a name="CommandLineRendering"></a>Command line rendering

In a normal command line render you would use `-a` at the end of the command to indicate to blender that you are rendering an animation, but this would use the default render command, not the Animated Render Border Render command.

To fix this, instead of using `-a` we use `—python-expr` (Python Expression) which allows us to specify a specific python command to run. In this case, specifying that we want to run the `bpy.ops.render.animated_render_border_render()` command is not enough to get the render to work and will result in an error, probably saying that `bpy` is not defined. This is exactly the same as if we were running a Python command in blender; only after importing `bpy` will `bpy` commands be available. So the Python expression we need to add to the end of the command is:

`--python-expr "import bpy; bpy.ops.render.animated_render_border_render()"`
 
The semicolon between the two commands tells Blender they are separate and the quotes around the entire command allows for the space between `import` and `bpy`. For more complex commands you could just reference a python file using one of the alternative python arguments.

The full command (when in the blender directory, minus my paths) is:

`blender -b "path to blend" --python-expr "import bpy; bpy.ops.render.animated_render_border_render()"`

If you need to add extra arguments to the command, such as setting the format or the output path these arguments should go before the `—python-expr` command, otherwise the render will happen before they are set (because the command line arguments are executed in the order they are written).

<br>

## <a name="Options"></a>:wrench: Options

### <a name="OptionsForAll3TrackingModes"></a>Options for all 3 tracking modes

 - **Enable/Disable** 

    This is the checkbox that appears next to the panel name and allows you to easily turn on or off the tracking without having to remove the tracking object or collection (which, if blank, would also disable tracking) or keyframes. When turning this on it will turn on the render border option in the Render> Dimensions panel if it isn’t already on. It won’t, however, turn off the render border when disabling it.

    |||
    |---|---|
    |Python|`scene.animated_render_border.enable`|
    |Type|`Bool`|
    |Default|`False`|

 - **Type**
 
    The type of tracking to perform: either track a single object, a collection of objects or manually keyframe the border values. The exact object or collection to track is specified later on.

    |||
    |---|---|
    |Python|`scene.animated_render_border.type`|
    |Type|`Enum in [‘Object’, ‘Collection’, ‘Keyframe’]`|
    |Default|`‘Object’`|

 - **Render Animation**
 
    The default ‘Render Animation’ button in Blender does not allow the render border to update each frame, so a custom ‘Render Animation’ button is needed. Once pressed, the mouse cursor will turn into a percentage counter and will update as the render progresses.
    
    This does not affect still frames, which can be rendered using the normal ‘Render’ button.

    The render can be cancelled by pressing the ‘Esc’ key on the keyboard. This doesn’t immediately cancel the render though, as the current frame has to finish rendering before it will stop.

    The ‘Render Animation’ button will appear disabled and display a ‘Fix errors to render’ message if there are any issues which would stop the render from operating correctly. These various issues are covered in the ‘Warnings’ section later on. The button will also be disabled if nothing is selected to be tracked when in ‘Object’ or ‘Collection’ tracking mode.

    |||
    |---|---|
    |Python|`bpy.ops.render.animated_render_border_render()`|

 - **Fix**
 
    This button appears when the render border has been turned off and is accompanied by a warning. It simply turns the render border back on and updates the render border by refreshing the current frame.
    
    |||
    |---|---|
    |Python|`bpy.ops.render.animated_render_border_fix()`|
 
<br>

### <a name="ObjectAndCollectionTracking"></a>‘Object’ and ‘Collection’ tracking

 - **Object to track**
 
    When ‘Object’ tracking has been selected you can select your chosen object from the dropdown box. If this dropdown box is blank it means there are no trackable objects in the scene.
    
    The types of object that can be tracked are: Meshes, Text objects, Curves, Surfaces, Meta objects, Lattices and Armatures.

    |||
    |---|---|
    |Python|`scene.animated_render_border.object`|
    |Type|`String`|
    |Default|`""`|
    |Note|Cannot be blank when tracking type is ‘Object’.|

 - **Collection to track**
 
    When ‘Collection’ tracking has been selected you can select your chosen collection from the dropdown box. If this dropdown box is blank it means there are no trackable collections in the scene.
    
    The types of objects that can be tracked in a collection are: Meshes, Text objects, Curves, Surfaces, Meta objects, Lattices and Armatures. If the chosen collection contains object types that are not in this list then they will not be taken into account when doing the tracking.

    |||
    |---|---|
    |Python|`scene.animated_render_border.collection`|
    |Type|`String`|
    |Default|`""`|
    |Note|Cannot be blank when tracking type is ‘Collection’.|

 - **Bone**
 
    If you have selected ‘Object’ tracking mode and have chosen to track an armature, this optional property appears. This drop-down box allows you to select a specific bone to track; if this is left blank all the bones in the armature will be tracked.

    |||
    |---|---|
    |Python|`scene.animated_render_border.bone`|
    |Type|`String`|
    |Default|`""`|
    |Note|Optional - only appears for ‘Object’ tracking when the chosen object is an armature.|

 - **Margin**
 
    This allows you to increase or decrease the border around the tracked object(s).

    |||
    |---|---|
    |Python|`scene.animated_render_border.margin`|
    |Type|`Int`|
    |Default|`3`|

 - **Use Bounding Box**
 
    By default, the tracking will calculate where the render border has to be by looking at the bounding box of the object. This is relatively quick as there are only 8 points of the bounding box (the corners) to analyse, but can appear slightly inaccurate depending on the orientation of the object.
    
    Turning this option off switches to a slower, more precise method, which analyses the ‘inner points’ of the object i.e. vertices if it’s a mesh, the lattice points for lattices, bones for armatures and so on, depending on the object type. Out of the types of objects that can be tracked, the following object types do not have any ‘inner points’ and so can’t use this precise method: Text objects and Meta objects. When one of these objects is tracked, the ‘Bounding Box’ option will be turned on and cannot be turned off. If you are using ‘Collection’ tracking and have ‘Bounding Box’ turned off, then ‘inner points’ will be used on any objects in the collection that support that; ones that don’t will fall back to the bounding box method.

    While this ‘inner points’ method is more precise, it is slower than the bounding box method as it has to compare every ‘inner point’ of the object, but results in a very precise calculation, creating a very tight, accurate border around the object. However, this could get very slow for objects with many inner points (e.g. high resolution meshes) or a collection of many objects.
    
    The exception to the precision ‘inner points’ offers is with ‘Surface’ type objects as often their ‘inner points’ are far larger in area than the displayed surface. In this case, ‘Use Bounding Box’ will probably be preferable.

    ‘Inner points’ will also be the preferable option if your object(s) has geometry generated by a modifier as the bounding box will stretch to contain all of the object whereas the ‘inner points’ will remain in their pre-modifier positions.

    |||
    |---|---|
    |Python|`scene.animated_render_border.use_bounding_box`|
    |Type|`Bool`|
    |Default|`True`|

 - **Draw Bounding Box**
 
    Enabling this option will turn on the bounding box option which is a feature of Blender found on the ‘Object’ tab of the selected object. This displays the box that Blender has calculated as the ‘bounds’ of the object and can be helpful when deciding whether ‘bounding box’ tracking or ‘precision’ tracking will be more suitable for your object(s). 

    |||
    |---|---|
    |Python|`scene.animated_render_border.draw_bounding_box`|
    |Type|`Bool`|
    |Default|`False`|

<br>

### <a name="KeyframeTracking"></a>'Keyframe’ tracking
 
 - **Insert Keyframe**
 
	This button inserts a keyframe for all 4 bounding box values on the current frame.

    |||
    |---|---|
    |Python|`bpy.ops.render.animated_render_border_insert_keyframe()`|

 - **Delete Keyframe**
 
	This button deletes a keyframe for all 4 bounding box values on the current frame.

    |||
    |---|---|
    |Python|`bpy.ops.render.animated_render_border_delete_keyframe()`|

 - **Min X, Max X, Min Y, Max Y**

    These are the values that represent the left, right, bottom and top edges of the render border box. Because a render border cannot have ‘0’ width or ‘0’ height, the minimum and maximum values on a single axis (x or y) cannot be the same. To adjust for this, if the min value is set to the same as the max value for either the x or y axis, 0.01 will be added to the max value. In the same manner, if the max value is set to the same as the min value, 0.01 will be subtracted from the min value.

    The minimum values also cannot be more than the maximum values, nor the maximums less than the minimums. If a value tries to go beyond these limits the other value will adjust to compensate. For example, increasing the minimum value up to and beyond the maximum value will cause the maximum value to increase so it is always at least 0.01 units more than the minimum.

    |||
    |---|---|
    |Python|`scene.animated_render_border.border_min_x`|
    |Type|`Float`|
    |Default|`0`|
    
    |||
    |---|---|
    |Python|`scene.animated_render_border.border_max_x`|
    |Type|`Float`|
    |Default|`1`|
    
    |||
    |---|---|
    |Python|`scene.animated_render_border.border_min_y`|
    |Type|`Float`|
    |Default|`0`|
    
    |||
    |---|---|
    |Python|`scene.animated_render_border.border_max_y`|
    |Type|`Float`|
    |Default|`1`|

 - **Refresh to synchronise border values**
 
    This button appears when the UI values representing the minimum and maximum of the render border have got out of sync with the actual values. This happens when the render border is drawn manually in the viewport. Pressing the button will update all the UI values to the values of the actual render border. This is useful if you wish to tweak the render border values after manually drawing it. If you don’t need to tweak the values and just wish to insert a keyframe then you don’t need to refresh them.

    |||
    |---|---|
    |Python|`bpy.ops.render.animated_render_border_refresh_values()`|

<br>

## <a name="Warnings"></a>:warning: Warnings

There are various warnings that will appear so as to alert you to things that will stop the render from rendering correctly. These need to be fixed before a render can be started, or in the case of rendering using Python, will cause an error to be thrown.

 - **‘Border’ is disabled in ‘Dimensions’ panel**
 
    If the Animated Render Border panel is enabled but the ‘border’ option has been turned off, either with a shortcut or via the Render> Dimensions panel, this warning will appear. This warning is accompanied by a ‘Fix’ button, which, when pressed will turn the border option back on.

 - **Active camera must be a Camera object, not [object type]**

    Via the ‘Set Active Object as Camera’ Blender command it is possible to set an object which is not a camera as the active scene camera. Obviously, a render cannot be started if the scene camera is anything other than a camera type object. Change the camera object in the ‘Scene’ properties to a camera object to remove this error.

 - **No camera is set in the scene properties**
 
    This error deals with a situation where this is no camera set to be rendered from. Similar to the previous error, this can be fixed by going to the ‘Scene’ properties and selecting a camera from the drop-down list. If no cameras are in this list, then one must be added to the scene.
    
 - **The object selected to be tracked does not exist**
 
    If an object is selected to be tracked, but that object is subsequently renamed, the add-on will no longer be able to detect or track that object. To correct this error re-select the object to be tracked from the object drop down list. This error will also appear when the selected object has been deleted.
    
 - **The collection selected to be tracked does not exist**
 
    If a collection is selected to be tracked, but that collection is subsequently renamed, the add-on will no longer be able to detect or track that collection. To correct this error re-select the collection to be tracked from the collection drop down list. This error will also appear when the selected collection has been deleted.
    
 - **The selected collection has no trackable objects**
 
    If the collection to be tracked is empty or none of the objects can be tracked, this error appears. The collection must contain one of the following types of object for tracking to be possible: Meshes, Text objects, Curves, Surfaces, Meta objects, Lattices, Lamps or Armatures.

 - **“Armatures objects can only use bounding box tracking in Blender 2.76 and later.”**
    **“Lattice objects can only use bounding box tracking in Blender 2.76 and later.”**
    **“Armature or Lattice objects in this collection can only use bounding box tracking in Blender 2.76 and later.”**
    
    These 3 separate error messages are related to users using a version of Blender prior to version 2.76. Blender 2.76 has a specific change in its code which allows access to the bounding boxes of Armature and Lattice objects. Previous versions of Blender do not have this and so the add-on will automatically turn off and disable the ‘Use Bounding Box’ option when an Armature, Lattice, or collection containing either of those object types is selected when the add-on detects Blender 2.75 or earlier is being used. This doesn’t stop the object being tracked, it just means you can’t use the bounding box to track it. Instead, it will resort to the ‘inner points’ method described in the “Options for ‘Object’ and ‘Collection’ tracking” > “Use Bounding Box” section of this user guide document.
    
    These are the only warnings which will not stop the user from being able to render. If you are using Blender 2.76 or later you will not see these warnings as Armatures and Lattices can be tracked like any of the other trackable objects.

<br>

## <a name="UserPreferences"></a>:gear: User Preferences

The add-on’s user preferences appear below the panel in Blender’s user preferences where you enable the add-on. Once the add-on is enabled the add-on’s user preferences box will appear below it.

 - **Display border dimensions**
 
    This user preference, which is off by default, turns on a label whose only function is to display in pixels the size of the bounding box. The label appears below the ‘Render Animation’ button for all 3 tracking types when turned on.

    |||
    |---|---|
    |Python|`bpy.context.user_preferences.addons[‘animatedRenderborder’].preferences.display_border_dimensions`|
    |Type|`Bool`|
    |Default|`False`|
    |Note|The value passed to `bpy.context.user_preferences.addons` is dependent on the version number.|

<br>

## <a name="Limitations"></a>:no_entry_sign: Limitations

### <a name="ObjectTypesWhichCantBeTracked"></a>Object types which can't be tracked

Ideally, all objects would be trackable, but this currently isn’t possible. This means that you can’t currently track camera objects, empties and a few other object types and they won’t appear in the object drop down list and will be ignored if they are present in the chosen tracking collection.   

In the future, hopefully all objects will be supported for tracking, but for now there is a useable workaround. If you wanted to track an empty you would simply have to make a cube and scale it so that the empty is contained within the cube. You can then parent the cube to the empty and track the cube object instead. The cube doesn’t have to be visible, visible in the render or even on the same layer, so it should be relatively unobtrusive.  

### <a name="DifferentRenderBordersForDifferentRenderLayers"></a>Different render borders for different render layers

This can't currently be done. At the minute the render border is set at the beginning of the render and it is only possible to update it when the rendering of the next frame starts, so whatever render border is set at the beginning of the render will be set for all render layers.

The only solution at the minute is to render out the render layers separately, setting a different render border between each render and then combining the render layers later in the compositor.

This is a question I get asked a lot so I will continue to look for a solution to this.

(Last updated: 13/09/17)

### <a name="PanoramicLensTypesForCamerasEgEquirectangularMirrorBallEtc"></a>'Panoramic' lens types for cameras, e.g. Equirectangular, Mirror Ball etc.

The add-on can only track the actual position of the object in the 3D View. If the camera has settings that changes/warps the position of the object in Rendered shading view (as is the case for Panoramic camera types), then the add-on unfortunately cannot track its rendered location. 

The only solution to this at the minute is to manually animate the render border by using the 'Keyframe' mode of the add-on, while in rendered shading mode.

I will look into whether this can be improved.
