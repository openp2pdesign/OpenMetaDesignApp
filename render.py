# -*- coding: utf-8 -*-
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


def system_map_render(temp, filename):    
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
    
    originY = 70
    originAreaY = 130
    whiteBorder = 10
    stepSize = 400
    actorSize = 150
    barSize = 70
    canvasX = (whiteBorder*2)+len(temp.steps)*stepSize
    canvasY = originAreaY+len(totalActors)*actorSize
    
    # Initialize canvas
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
        ctx.move_to(10+j*400, originY)
        ctx.line_to(10+j*400, canvasY) 
        ctx.stroke()
    # Draw last border
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(2)
    ctx.set_dash([1.0])
    final = len(temp.steps)
    ctx.move_to(10+final*400, originY)
    ctx.line_to(10+final*400, originY+len(totalActors)*200) 
    ctx.stroke()
    
    # Draw the titles of the steps
    ctx.set_source_rgb(0, 0, 0)
    ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(24)
    for j in range(len(temp.steps)):
        ctx.move_to(whiteBorder + stepSize/2-len(temp.steps[j].title)*6 + j*stepSize, originY+24)
        ctx.show_text(temp.steps[j].title)
    
    
    # Draw bars for actors in each step when they are present
    for j in range(len(temp.steps)):
        for y,g in enumerate(sorted(totalActors)):
            if g in temp.steps[j].actors:
                ctx.set_source_rgb(0.7,0.7,0.7)
                ctx.rectangle((whiteBorder)+j*stepSize, 
                              originAreaY+y*150, 
                              stepSize, 
                              barSize)
                ctx.fill()
    
    # Position the name of each actor
    for j in range(len(temp.steps)):
        for y,g in enumerate(sorted(totalActors)):
            if g in temp.steps[j].actors:
                ctx.set_source_rgb(0,0,0)
                ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                ctx.set_font_size(16)
                ctx.move_to(whiteBorder+(stepSize/2)-32+j*stepSize, originAreaY+39+y*150)
                ctx.show_text(g)
    
    
    for j in range(len(temp.steps)):       
        for l,k in enumerate(temp.steps[j].flows):
            # Connect the actors with a line, here we start
            ctx.set_source_rgb(0, 0, 0)
            ctx.set_line_width(2)
            
            # Set the type of flow as a line style
            if temp.steps[j].flows[l].type == "Information flow":
                ctx.set_dash([2.0])
            elif temp.steps[j].flows[l].type == "Financial flow":
                ctx.set_dash([6.0])
            elif temp.steps[j].flows[l].type == "Physical resources flow":
                ctx.set_dash([1.0,0.2,0.4])
            
            # Draw the flow lines, add the barSize according to the order of the actors
            if totalActors[temp.steps[j].flows[l].actor1]["order"] > totalActors[temp.steps[j].flows[l].actor2]["order"]:
                # First actor has a greater ordering number
                coordX = whiteBorder+20+j*400+l*50
                coordY1 = originAreaY+(totalActors[temp.steps[j].flows[l].actor1]["order"])*150
                coordY2 = originAreaY+barSize+(totalActors[temp.steps[j].flows[l].actor2]["order"])*150
                ctx.move_to(coordX, coordY1)
                ctx.line_to(coordX, coordY2)
                ctx.stroke()
                if temp.steps[j].flows[l].direction == "From the first actor to the second one":
                    # Arrow must be drawn on the second actor
                    ctx.translate(coordX, coordY1)
                    ctx.arc(0, 0, 4, 0, 3*pi)
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.fill()
                    # go back to origin
                    ctx.translate(-coordX, -coordY1)
                    
                    # Draw label box
                    ctx.set_source_rgba(0.95, 0.95, 0.95,0.9)
                    ctx.rectangle(coordX-len(temp.steps[j].flows[l].what)*4, coordY1-33, 
                                  len(temp.steps[j].flows[l].what)*8, 18)
                    ctx.fill()
                    # Draw label
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                    ctx.set_font_size(12)
                    ctx.move_to(coordX-len(temp.steps[j].flows[l].what)*2.5, coordY1-20)
                    ctx.show_text(temp.steps[j].flows[l].what)
                    
                elif temp.steps[j].flows[l].direction == "From the second actor to the first one":
                    # Arrow must be drawn on the first actor
                    ctx.translate(coordX, coordY2)
                    ctx.arc(0, 0, 4, 0, 3*pi)
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.fill()
                    # go back to origin
                    ctx.translate(-coordX, -coordY2)
                    
                    # Draw label box
                    ctx.set_source_rgba(0.95, 0.95, 0.95,0.9)
                    ctx.rectangle(coordX-len(temp.steps[j].flows[l].what)*4, coordY2+8, 
                                  len(temp.steps[j].flows[l].what)*8, 18)
                    ctx.fill()
                    # Draw label
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                    ctx.set_font_size(12)
                    ctx.move_to(coordX-len(temp.steps[j].flows[l].what)*2.5, coordY2+20)
                    ctx.show_text(temp.steps[j].flows[l].what)
                    
                elif temp.steps[j].flows[l].direction == "Both directions":
                    ctx.translate(coordX, coordY2)
                    ctx.arc(0, 0, 4, 0, 3*pi)
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.fill()
                    # go back to origin
                    ctx.translate(-coordX, -coordY2)
                    ctx.translate(coordX, coordY1)
                    ctx.arc(0, 0, 4, 0, 3*pi)
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.fill()
                    # go back to origin
                    ctx.translate(-coordX, -coordY1)
                    
                    # Draw label box
                    ctx.set_source_rgba(0.95, 0.95, 0.95,0.9)
                    ctx.rectangle(coordX-len(temp.steps[j].flows[l].what)*4, coordY1-33, 
                                  len(temp.steps[j].flows[l].what)*8, 18)
                    ctx.fill()
                    # Draw label
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                    ctx.set_font_size(12)
                    ctx.move_to(coordX-len(temp.steps[j].flows[l].what)*2.5, coordY1-20)
                    ctx.show_text(temp.steps[j].flows[l].what)
            
            else:
                # First actor has a smaller ordering number
                coordX = whiteBorder+20+j*400+l*50
                coordY1 = originAreaY+barSize+(totalActors[temp.steps[j].flows[l].actor1]["order"])*150
                coordY2 = originAreaY+(totalActors[temp.steps[j].flows[l].actor2]["order"])*150
                ctx.move_to(coordX, coordY1)
                ctx.line_to(coordX, coordY2)
                ctx.stroke()
                if temp.steps[j].flows[l].direction == "From the first actor to the second one":
                    # Arrow must be drawn on the second actor
                    ctx.translate(coordX, coordY1)
                    ctx.arc(0, 0, 4, 0, 3*pi)
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.fill()
                    # go back to origin
                    ctx.translate(-coordX, -coordY1)
                    
                    # Draw label box
                    ctx.set_source_rgba(0.95, 0.95, 0.95,0.9)
                    ctx.rectangle(coordX-len(temp.steps[j].flows[l].what)*4, coordY1+8, 
                                  len(temp.steps[j].flows[l].what)*8, 18)
                    ctx.fill()
                    # Draw label
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                    ctx.set_font_size(12)
                    ctx.move_to(coordX-len(temp.steps[j].flows[l].what)*2.5, coordY1+20)
                    ctx.show_text(temp.steps[j].flows[l].what)
                    
                elif temp.steps[j].flows[l].direction == "From the second actor to the first one":
                    # Arrow must be drawn on the first actor
                    ctx.translate(coordX, coordY2)
                    ctx.arc(0, 0, 4, 0, 3*pi)
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.fill()
                    # go back to origin
                    ctx.translate(-coordX, -coordY2)
                    
                    # Draw label box
                    ctx.set_source_rgba(0.95, 0.95, 0.95,0.9)
                    ctx.rectangle(coordX-len(temp.steps[j].flows[l].what)*4, coordY2-33, 
                                  len(temp.steps[j].flows[l].what)*8, 18)
                    ctx.fill()
                    # Draw label
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                    ctx.set_font_size(12)
                    ctx.move_to(coordX-len(temp.steps[j].flows[l].what)*2.5, coordY2-20)
                    ctx.show_text(temp.steps[j].flows[l].what)
                    
                elif temp.steps[j].flows[l].direction == "Both directions":
                    ctx.translate(coordX, coordY2)
                    ctx.arc(0, 0, 4, 0, 3*pi)
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.fill()
                    # go back to origin
                    ctx.translate(-coordX, -coordY2)
                    ctx.translate(coordX, coordY1)
                    ctx.arc(0, 0, 4, 0, 3*pi)
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.fill()
                    # go back to origin
                    ctx.translate(-coordX, -coordY1)
                    
                    # Draw label box
                    ctx.set_source_rgba(0.95, 0.95, 0.95,0.9)
                    ctx.rectangle(coordX-len(temp.steps[j].flows[l].what)*4, coordY1+8, 
                                  len(temp.steps[j].flows[l].what)*8, 18)
                    ctx.fill()
                    # Draw label
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                    ctx.set_font_size(12)
                    ctx.move_to(coordX-len(temp.steps[j].flows[l].what)*2.5, coordY1+20)
                    ctx.show_text(temp.steps[j].flows[l].what)
            
            
    surface.write_to_png(filename) # Output to PNG
    
    
if __name__ == "__main__":
    p = project()
    p.load("test2.meta")
    system_map_render(p,"test.png")