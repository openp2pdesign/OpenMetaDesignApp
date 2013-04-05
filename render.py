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
from math import pi
from classes import *

# Load data
temp = project()
temp.load("test2.meta")

# Calculate total actors
totalActors_pre = []
totalActors = {}
for j in range(len(temp.steps)):
    for k in temp.steps[j].actors:
        if k not in totalActors_pre:
            totalActors_pre.append(k)
 
# Order the dict of actors            
for p,l in enumerate(sorted(totalActors_pre)):
    totalActors[l] = {"order":p}
    
for k in totalActors:
    print k,"-",totalActors[k]["order"]


whiteBorder = 10
stepSize = 400
actorSize = 150
barsize = 70
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

# Draw bars for actors in each step when they are present
for j in range(len(temp.steps)):
    for y,g in enumerate(sorted(totalActors)):
        if g in temp.steps[j].actors:
            ctx.set_source_rgb(0.7,0.7,0.7)
            ctx.rectangle((whiteBorder)+j*stepSize, 
                          50+y*150, 
                          stepSize, 
                          barsize)
            ctx.fill()

# Position the name of each actor
for j in range(len(temp.steps)):
    for y,g in enumerate(sorted(totalActors)):
        if g in temp.steps[j].actors:
            ctx.set_source_rgb(0,0,0)
            ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            ctx.set_font_size(16)
            ctx.move_to((whiteBorder)+20, 50+39+y*150)
            ctx.show_text(g)


for j in range(len(temp.steps)):       
    for l,k in enumerate(temp.steps[j].flows):
        print "---"
        print k
        print temp.steps[j].flows[l].actor1, totalActors[temp.steps[j].flows[l].actor1]["order"]
        print temp.steps[j].flows[l].actor2, totalActors[temp.steps[j].flows[l].actor2]["order"]
        print temp.steps[j].flows[l].direction
        if temp.steps[j].flows[l].direction == "From the first actor to the second one":
            pass
        elif temp.steps[j].flows[l].direction == "From the second actor to the first one":
            pass
        elif temp.steps[j].flows[l].direction == "Both directions":
            pass
        
        # Connect the actors with a line
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(4)
        ctx.set_dash([1.0,0.2,0.4])
        ctx.move_to(whiteBorder+j*450, 50+totalActors[temp.steps[j].flows[l].actor1]["order"]*100)
        ctx.line_to(whiteBorder+j*450, 50+totalActors[temp.steps[j].flows[l].actor2]["order"]*100) 
        ctx.stroke()
        



surface.write_to_png ("test.png") # Output to PNG