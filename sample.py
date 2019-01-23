import vpython

# GlowScript 2.7 VPython

vpython.scene.range = 1
vpython.scene.forward = vpython.vector(-1,-.5,-1)
vpython.box(pos=vpython.vector(1,1,1),
            texture="https://s3.amazonaws.com/glowscript/textures/flower_texture.jpg")

redbox=vpython.box(pos=vpython.vector(4,2,3),
                   size=vpython.vector(8,4,6),
                   color=vpython.color.red)
ball=vpython.sphere(pos=vpython.vector(4,7,3),
                    radius=2,
                    color=vpython.color.green)


s = 'This illustrates the use of an image from another web site as a texture.\n'
s += 'This is an example of CORS, "Cross-Origin Resource Sharing".\n'
vpython.scene.caption = s

vpython.scene.append_to_caption("""
Right button drag or Ctrl-drag to rotate "camera" to view scene.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
Shift-drag to pan left/right and up/down.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate.""")


