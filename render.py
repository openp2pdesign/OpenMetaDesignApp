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

# Load data
temp = project()
temp.load("test2.meta")

# Calculate total actors
totalActors = []
for j in range(len(temp.steps)):
    for k in temp.steps[j].actors:
        if k not in totalActors:
            totalActors.append(k)

whiteBorder = 10
stepSize = 400
actorSize = 200
canvasX = (whiteBorder*2)+len(temp.steps)*stepSize
canvasY = 50+len(totalActors)*actorSize

surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, canvasX, canvasY+whiteBorder)
ctx = cairo.Context (surface)

# Paint background
ctx.set_source_rgb(1, 1, 1) # blue
ctx.rectangle(0, 0, canvasX, canvasY+whiteBorder)
ctx.fill()

# Write the canvas title
ctx.set_source_rgb(0, 0, 0)
ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
ctx.set_font_size(32)
ctx.move_to(10, 32)
ctx.show_text("System Map")

# Draw the borders of the areas for the steps
for j in range(len(temp.steps)):    
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(2)
    ctx.set_dash([1.0])
    ctx.move_to(10+j*400, 50)
    ctx.line_to(10+j*400, canvasY) 
    ctx.stroke()
# Draw last border
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(2)
ctx.set_dash([1.0])
final = len(temp.steps)
ctx.move_to(10+final*400, 50)
ctx.line_to(10+final*400, 50+len(totalActors)*200) 
ctx.stroke()


barsize = 50

# Draw bars for actors in each step when they are present
for j in range(len(temp.steps)):     
    print temp.steps[j].title
    print "---"
    for g in totalActors:
        if g in temp.steps[j].actors:
            ctx.set_source_rgb(0.12, 0.6, 1)
            ctx.rectangle((whiteBorder)+j*stepSize, 
                          200+j*100, 
                          stepSize, 
                          barsize)
            ctx.fill()
   


for j in range(len(temp.steps)):
    print "---"        
    print temp.steps[j].title
    for l,k in enumerate(temp.steps[j].flows):
        print temp.steps[j].flows[l].actor1
        print temp.steps[j].flows[l].actor2
        print temp.steps[j].flows[l].direction



surface.write_to_png ("test.png") # Output to PNG