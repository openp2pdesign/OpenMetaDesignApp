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
from classes import *

temp = project()
temp.load("test2.meta")

for j,i in enumerate(temp.steps):
    print "---"
    print temp.steps[j].title
    for l,k in enumerate(temp.steps[j].flows):
        print temp.steps[j].flows[l].actor1
        print temp.steps[j].flows[l].actor2
        print temp.steps[j].flows[l].direction

surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, 1400, 1200)
ctx = cairo.Context (surface)

# paint background
ctx.set_source_rgb(1, 1, 1) # blue
ctx.rectangle(0, 0, 1400, 1200)
ctx.fill()

# Write a text
ctx.set_source_rgb(0, 0, 0)
ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
ctx.set_font_size(32)
ctx.move_to(10, 32)
ctx.show_text("System Map")

stepsize = 200
space = 40
barsize = 50
barsOriginX = 20
barsOriginY = 70
flowsOriginX = 40
flowsOriginY = barsOriginY + barsize + space


flowsCoord = {1:{"x":1,"y":1, "label":"flow"}}
coord = {}

# calculate coordinates for the rectangles
for i in range(5):
    coord[i] = {}
    coord[i]["x"] = barsOriginX
    if i == 0:
        coord[i]["y"] = barsOriginY
        coord[i]["x"] = barsOriginX
    else:
        coord[i]["y"] = coord[i-1]["y"] + barsize + space
        coord[i]["x"] = stepsize * i
    print "X:",coord[i]["x"]
    print "Y:",coord[i]["y"]
    print ""
    
# calculate coordinates for the flows
for i in range(5):
    flowsCoord[i] = {}
    flowsCoord[i]["x"] = flowsOriginX
    if i == 0:
        flowsCoord[i]["y"] = flowsOriginY
        flowsCoord[i]["x"] = flowsOriginX
    else:
        flowsCoord[i]["y"] = flowsCoord[i-1]["y"] + barsize + space
    print "X:",flowsCoord[i]["x"]
    print "Y:",flowsCoord[i]["y"]
    print ""
    
# Adding the labels
for i in range(5):
    flowsCoord[i]["label"] = "flow n."+str(i)

# Draw bars
for i in range(5):
    ctx.set_source_rgb(0.12, 0.6, 1) # blue
    ctx.rectangle(barsOriginX, coord[i]["y"], 
                  coord[i]["x"]-flowsOriginX, barsize)
    ctx.fill()

# Draw lines
for i in range(5):
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(4)
    ctx.set_dash([1.0])
    ctx.move_to(flowsCoord[i]["x"], flowsCoord[i]["y"]-space)
    ctx.line_to(flowsCoord[i]["x"], flowsCoord[i]["y"]) 
    ctx.stroke()

# Draw points
for i in range(5):
    ctx.set_line_width(2)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_dash([])
    ctx.translate(flowsCoord[i]["x"], flowsCoord[i]["y"])
    ctx.arc(0, 0, 2, 0, 2*math.pi)
    ctx.stroke_preserve()
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()
    # go back to origin
    ctx.translate(-flowsCoord[i]["x"], -flowsCoord[i]["y"])


# Draw flows labels
for i in range(5):
    ctx.set_source_rgba(0.95, 0.95, 0.95,0.9)
    ctx.rectangle(flowsCoord[i]["x"]-len(flowsCoord[i]["label"])*3, flowsCoord[i]["y"]-space/2-12, 
                  len(flowsCoord[i]["label"])*6, 18)
    ctx.fill()
    
    ctx.set_source_rgb(0, 0, 0)
    ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(12)
    ctx.move_to(flowsCoord[i]["x"]-len(flowsCoord[i]["label"])*2.5, flowsCoord[i]["y"]-space/2)
    ctx.show_text(flowsCoord[i]["label"])


surface.write_to_png ("test.png") # Output to PNG