#
# Open MetaDesign 0.1
#
# Author: Massimo Menichinelli
# Website:
# http://openmetadesign.org
# http://openp2pdesign.org
#
# License: GPL v.3
#

import cairo
import math

surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, 1400, 1200)
ctx = cairo.Context (surface)

# paint background
ctx.set_source_rgb(1, 1, 1) # blue
ctx.rectangle(0, 0, 1400, 1200)
ctx.fill()

# Write a text
ctx.set_source_rgb(0, 0, 0)
ctx.select_font_face("Anivers", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
ctx.set_font_size(32)
ctx.move_to(10, 32)
ctx.show_text("System Map")

originX = 10
originY = 50
space = 20
barsize = 40

coord = {1:{"x":1,"y":1}}

# calculate coordinates for the rectangles
for i in range(5):
    coord[i] = {}
    coord[i]["x"] = originX
    if i == 0:
        coord[i]["y"] = originY
    else:
        coord[i]["y"] = coord[i-1]["y"] + barsize + space
    print "X:",coord[i]["x"]
    print "Y:",coord[i]["y"]
    print ""

# Draw bars
for i in range(5):
    ctx.set_source_rgb(0.12, 0.6, 1) # blue
    ctx.rectangle(coord[i]["x"], coord[i]["y"], 
                  300, barsize)
    ctx.fill()

# Draw lines
for i in range(5):
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(4)
    ctx.set_dash([1.0])
    ctx.move_to(coord[i]["x"], coord[i]["y"]-space)
    ctx.line_to(coord[i]["x"], coord[i]["y"]) 
    ctx.stroke()

# Draw points
for i in range(5):
    ctx.set_line_width(2)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_dash([])
    ctx.translate(coord[i]["x"], coord[i]["y"])
    ctx.arc(0, 0, 2, 0, 2*math.pi)
    ctx.stroke_preserve()
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()
    # go back to origin
    ctx.translate(-coord[i]["x"], -coord[i]["y"])



surface.write_to_png ("test.png") # Output to PNG