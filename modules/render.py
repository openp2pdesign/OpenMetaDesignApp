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
import pango
import pangocairo
from math import pi
from modules.classes import *


def actors_flows_system_render(temp, filename):    
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
    ctx.show_text("Actors and flows in the Open Design process")
    
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
            print "L:",l
            print "K:",k
            # Connect the actors with a line, here we start
            ctx.set_source_rgb(0, 0, 0)
            ctx.set_line_width(2)
            
            # Set the type of flow as a line style
            if temp.steps[j].flows[k].type == "Information flow":
                ctx.set_dash([2.0])
            elif temp.steps[j].flows[k].type == "Financial flow":
                ctx.set_dash([6.0])
            elif temp.steps[j].flows[k].type == "Physical resources flow":
                ctx.set_dash([1.0,0.2,0.4])
            
            # Draw the flow lines, add the barSize according to the order of the actors
            if totalActors[temp.steps[j].flows[k].actor1]["order"] > totalActors[temp.steps[j].flows[k].actor2]["order"]:
                # First actor has a greater ordering number
                coordX = whiteBorder+20+j*400+l*50
                coordY1 = originAreaY+(totalActors[temp.steps[j].flows[k].actor1]["order"])*150
                coordY2 = originAreaY+barSize+(totalActors[temp.steps[j].flows[k].actor2]["order"])*150
                ctx.move_to(coordX, coordY1)
                ctx.line_to(coordX, coordY2)
                ctx.stroke()
                if temp.steps[j].flows[k].direction == "From the first actor to the second one":
                    # Arrow must be drawn on the second actor
                    ctx.translate(coordX, coordY1)
                    ctx.arc(0, 0, 4, 0, 3*pi)
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.fill()
                    # go back to origin
                    ctx.translate(-coordX, -coordY1)
                    
                    # Draw label box
                    ctx.set_source_rgba(0.95, 0.95, 0.95,0.9)
                    ctx.rectangle(coordX-len(temp.steps[j].flows[k].what)*4, coordY1-33, 
                                  len(temp.steps[j].flows[k].what)*8, 18)
                    ctx.fill()
                    # Draw label
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                    ctx.set_font_size(12)
                    ctx.move_to(coordX-len(temp.steps[j].flows[k].what)*2.5, coordY1-20)
                    ctx.show_text(temp.steps[j].flows[k].what)
                    
                elif temp.steps[j].flows[k].direction == "From the second actor to the first one":
                    # Arrow must be drawn on the first actor
                    ctx.translate(coordX, coordY2)
                    ctx.arc(0, 0, 4, 0, 3*pi)
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.fill()
                    # go back to origin
                    ctx.translate(-coordX, -coordY2)
                    
                    # Draw label box
                    ctx.set_source_rgba(0.95, 0.95, 0.95,0.9)
                    ctx.rectangle(coordX-len(temp.steps[j].flows[k].what)*4, coordY2+8, 
                                  len(temp.steps[j].flows[k].what)*8, 18)
                    ctx.fill()
                    # Draw label
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                    ctx.set_font_size(12)
                    ctx.move_to(coordX-len(temp.steps[j].flows[k].what)*2.5, coordY2+20)
                    ctx.show_text(temp.steps[j].flows[k].what)
                    
                elif temp.steps[j].flows[k].direction == "Both directions":
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
                    ctx.rectangle(coordX-len(temp.steps[j].flows[k].what)*4, coordY1-33, 
                                  len(temp.steps[j].flows[k].what)*8, 18)
                    ctx.fill()
                    # Draw label
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                    ctx.set_font_size(12)
                    ctx.move_to(coordX-len(temp.steps[j].flows[k].what)*2.5, coordY1-20)
                    ctx.show_text(temp.steps[j].flows[k].what)
            
            else:
                # First actor has a smaller ordering number
                coordX = whiteBorder+20+j*400+l*50
                coordY1 = originAreaY+barSize+(totalActors[temp.steps[j].flows[k].actor1]["order"])*150
                coordY2 = originAreaY+(totalActors[temp.steps[j].flows[k].actor2]["order"])*150
                ctx.move_to(coordX, coordY1)
                ctx.line_to(coordX, coordY2)
                ctx.stroke()
                if temp.steps[j].flows[k].direction == "From the first actor to the second one":
                    # Arrow must be drawn on the second actor
                    ctx.translate(coordX, coordY1)
                    ctx.arc(0, 0, 4, 0, 3*pi)
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.fill()
                    # go back to origin
                    ctx.translate(-coordX, -coordY1)
                    
                    # Draw label box
                    ctx.set_source_rgba(0.95, 0.95, 0.95,0.9)
                    ctx.rectangle(coordX-len(temp.steps[j].flows[k].what)*4, coordY1+8, 
                                  len(temp.steps[j].flows[k].what)*8, 18)
                    ctx.fill()
                    # Draw label
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                    ctx.set_font_size(12)
                    ctx.move_to(coordX-len(temp.steps[j].flows[k].what)*2.5, coordY1+20)
                    ctx.show_text(temp.steps[j].flows[k].what)
                    
                elif temp.steps[j].flows[k].direction == "From the second actor to the first one":
                    # Arrow must be drawn on the first actor
                    ctx.translate(coordX, coordY2)
                    ctx.arc(0, 0, 4, 0, 3*pi)
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.fill()
                    # go back to origin
                    ctx.translate(-coordX, -coordY2)
                    
                    # Draw label box
                    ctx.set_source_rgba(0.95, 0.95, 0.95,0.9)
                    ctx.rectangle(coordX-len(temp.steps[j].flows[k].what)*4, coordY2-33, 
                                  len(temp.steps[j].flows[k].what)*8, 18)
                    ctx.fill()
                    # Draw label
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                    ctx.set_font_size(12)
                    ctx.move_to(coordX-len(temp.steps[j].flows[k].what)*2.5, coordY2-20)
                    ctx.show_text(temp.steps[j].flows[k].what)
                    
                elif temp.steps[j].flows[k].direction == "Both directions":
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
                    ctx.rectangle(coordX-len(temp.steps[j].flows[k].what)*4, coordY1+8, 
                                  len(temp.steps[j].flows[k].what)*8, 18)
                    ctx.fill()
                    # Draw label
                    ctx.set_source_rgb(0, 0, 0)
                    ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
                    ctx.set_font_size(12)
                    ctx.move_to(coordX-len(temp.steps[j].flows[k].what)*2.5, coordY1+20)
                    ctx.show_text(temp.steps[j].flows[k].what)
            
    # Write the canvas as a .png file
    surface.write_to_png(filename)
    
    
def process_participation_render(temp,filename):
    originY = 70
    originAreaY = 130
    whiteBorder = 10
    stepSize = 400
    actorSize = 150
    barSize = 70
    canvasX = (whiteBorder*2)+len(temp.steps)*stepSize
    canvasY = 500
    
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
    ctx.show_text("Participation and speed of the Open Design process")
    
    # Draw the borders of the areas for the steps
    for j in range(len(temp.steps)):    
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(2)
        ctx.set_dash([1.0])
        ctx.move_to(10+j*400, originY)
        ctx.line_to(10+j*400, canvasY-whiteBorder*2) 
        ctx.stroke()
    # Draw last border
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(2)
    ctx.set_dash([1.0])
    final = len(temp.steps)
    ctx.move_to(10+final*400, originY)
    ctx.line_to(10+final*400, canvasY-whiteBorder*2) 
    ctx.stroke()
    
    # Draw the titles of the steps
    ctx.set_source_rgb(0, 0, 0)
    ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(24)
    for j in range(len(temp.steps)):
        ctx.move_to(whiteBorder + stepSize/2-len(temp.steps[j].title)*6 + j*stepSize, originY+24)
        ctx.show_text(temp.steps[j].title)
        
    # Draw lines for creating a table layout
    for k in range(6):
        ctx.set_source_rgb(0.7,0.7,0.7)
        ctx.move_to(whiteBorder, originAreaY+k*70)
        ctx.line_to(whiteBorder++len(temp.steps)*stepSize, originAreaY+k*70) 
        ctx.stroke()

    # Check each participation level in each step 
    participationCell = {}
    
    for j in range(len(temp.steps)):
        ctx.set_source_rgb(0.7,0.7,0.7)
        posX = (whiteBorder)+j*stepSize
        if temp.steps[j].participation == "None":
            posY = originAreaY+0*70
        elif temp.steps[j].participation == "Indirect":
            posY = originAreaY+1*70
        elif temp.steps[j].participation == "Consultative":
            posY = originAreaY+2*70
        elif temp.steps[j].participation == "Shared control":
            posY = originAreaY+3*70
        elif temp.steps[j].participation == "Full control":
            posY = originAreaY+4*70
        
        ctx.rectangle(posX, 
                      posY, 
                      stepSize, 
                      barSize)
        ctx.fill()
        
        # Draw labels for the specific participation level
        ctx.set_source_rgb(0, 0, 0)
        ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        ctx.set_font_size(16)
        ctx.move_to(posX+stepSize/2-4*len(temp.steps[j].participation), posY+40)
        ctx.show_text(temp.steps[j].participation)
    
    
    # Write the canvas as a .png file
    surface.write_to_png(filename)
    
    
def business_model_render(temp,filename):
    originY = 70
    originAreaY = 130
    whiteBorder = 10
    stepSize = 400
    actorSize = 150
    barSize = 70
    canvasX = (whiteBorder*2)+len(temp.steps)*stepSize
    canvasY = 500
    
    # Initialize canvas
    surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, 5000, 3055)
    ctx = cairo.Context (surface)
    
    # Load and place the background .png image
    background = cairo.ImageSurface.create_from_png('images/bmc.png')  
    ctx.set_source_surface(background, 0, 0) 
    ctx.paint()
    
    
    # Key Partners text area
    ctx.set_source_rgb(0.9,0.9,0.9)
    ctx.rectangle(50, 440, 920, 1680)
    ctx.fill()
    
    # Draw text in the Key Partners text area
    ctx.set_source_rgb(0,0,0)
    ctx.translate(50,440)
    pangocairo_context = pangocairo.CairoContext(ctx)
    layout = pangocairo_context.create_layout()
    layout.set_width(920)
    layout.set_alignment(pango.ALIGN_LEFT)
    layout.set_wrap(pango.WRAP_WORD)
    layout.set_width(pango.SCALE * 920)
    layout.set_font_description(pango.FontDescription("TitilliumText25L 25"))
    layout.set_text(temp.businessmodel.keypartners)
    pangocairo_context.update_layout(layout)
    pangocairo_context.show_layout(layout)
    ctx.translate(-50,-440)
    
    # Key Activities text area
    ctx.set_source_rgb(0.9,0.9,0.9)
    ctx.rectangle(1040, 440, 920, 600)
    ctx.fill()
    
    # Draw text in the Key Activities text area
    ctx.set_source_rgb(0,0,0)
    ctx.translate(1040,440)
    pangocairo_context = pangocairo.CairoContext(ctx)
    layout = pangocairo_context.create_layout()
    layout.set_width(920)
    layout.set_alignment(pango.ALIGN_LEFT)
    layout.set_wrap(pango.WRAP_WORD)
    layout.set_width(pango.SCALE * 920)
    layout.set_font_description(pango.FontDescription("TitilliumText25L 25"))
    layout.set_text(temp.businessmodel.keyactivities)
    pangocairo_context.update_layout(layout)
    pangocairo_context.show_layout(layout)
    ctx.translate(-1040,-440)
    
    # Key Resources text area
    ctx.set_source_rgb(0.9,0.9,0.9)
    ctx.rectangle(1040, 1440, 920, 680)
    ctx.fill()
    
    # Draw text in the Key Resources text area
    ctx.set_source_rgb(0,0,0)
    ctx.translate(1040,1440)
    pangocairo_context = pangocairo.CairoContext(ctx)
    layout = pangocairo_context.create_layout()
    layout.set_width(920)
    layout.set_alignment(pango.ALIGN_LEFT)
    layout.set_wrap(pango.WRAP_WORD)
    layout.set_width(pango.SCALE * 920)
    layout.set_font_description(pango.FontDescription("TitilliumText25L 25"))
    layout.set_text(temp.businessmodel.keyresources)
    pangocairo_context.update_layout(layout)
    pangocairo_context.show_layout(layout)
    ctx.translate(-1040,-1440)
    
    # Value Propositions text area
    ctx.set_source_rgb(0.9,0.9,0.9)
    ctx.rectangle(2030, 440, 920, 1680)
    ctx.fill()
    
    # Draw text in the Value Proposition text area
    ctx.set_source_rgb(0,0,0)
    ctx.translate(2030,440)
    pangocairo_context = pangocairo.CairoContext(ctx)
    layout = pangocairo_context.create_layout()
    layout.set_width(920)
    layout.set_alignment(pango.ALIGN_LEFT)
    layout.set_wrap(pango.WRAP_WORD)
    layout.set_width(pango.SCALE * 920)
    layout.set_font_description(pango.FontDescription("TitilliumText25L 25"))
    layout.set_text(temp.businessmodel.valueproposition)
    pangocairo_context.update_layout(layout)
    pangocairo_context.show_layout(layout)
    ctx.translate(-2030,-440)
    
    # Customer Relationships text area
    ctx.set_source_rgb(0.9,0.9,0.9)
    ctx.rectangle(3030, 440, 920, 600)
    ctx.fill()
    
    # Draw text in the Customer Relationships text area
    ctx.set_source_rgb(0,0,0)
    ctx.translate(3030,440)
    pangocairo_context = pangocairo.CairoContext(ctx)
    layout = pangocairo_context.create_layout()
    layout.set_width(920)
    layout.set_alignment(pango.ALIGN_LEFT)
    layout.set_wrap(pango.WRAP_WORD)
    layout.set_width(pango.SCALE * 920)
    layout.set_font_description(pango.FontDescription("TitilliumText25L 25"))
    layout.set_text(temp.businessmodel.customerrelationships)
    pangocairo_context.update_layout(layout)
    pangocairo_context.show_layout(layout)
    ctx.translate(-3030,-440)
    
    # Channels text area
    ctx.set_source_rgb(0.9,0.9,0.9)
    ctx.rectangle(3030, 1440, 920, 680)
    ctx.fill()
    
    # Draw text in the Channels text area
    ctx.set_source_rgb(0,0,0)
    ctx.translate(3030,1440)
    pangocairo_context = pangocairo.CairoContext(ctx)
    layout = pangocairo_context.create_layout()
    layout.set_width(920)
    layout.set_alignment(pango.ALIGN_LEFT)
    layout.set_wrap(pango.WRAP_WORD)
    layout.set_width(pango.SCALE * 920)
    layout.set_font_description(pango.FontDescription("TitilliumText25L 25"))
    layout.set_text(temp.businessmodel.channels)
    pangocairo_context.update_layout(layout)
    pangocairo_context.show_layout(layout)
    ctx.translate(-3030,-1440)
    
    # Customer Segments text area
    ctx.set_source_rgb(0.9,0.9,0.9)
    ctx.rectangle(4030, 440, 920, 1680)
    ctx.fill()
    
    # Draw text in the Customer Segments text area
    ctx.set_source_rgb(0,0,0)
    ctx.translate(4030,440)
    pangocairo_context = pangocairo.CairoContext(ctx)
    layout = pangocairo_context.create_layout()
    layout.set_width(920)
    layout.set_alignment(pango.ALIGN_LEFT)
    layout.set_wrap(pango.WRAP_WORD)
    layout.set_width(pango.SCALE * 920)
    layout.set_font_description(pango.FontDescription("TitilliumText25L 25"))
    layout.set_text(temp.businessmodel.customersegments)
    pangocairo_context.update_layout(layout)
    pangocairo_context.show_layout(layout)
    ctx.translate(-4030,-440)
    
    # Cost Structure text area
    ctx.set_source_rgb(0.9,0.9,0.9)
    ctx.rectangle(50, 2450, 920, 450)
    ctx.fill()
    
    # Draw text in the Cost Structure first text area
    if len(temp.businessmodel.coststructure) > 1250:
        firstareatext = temp.businessmodel.coststructure[0:1250]
        secondareatext = temp.businessmodel.coststructure[1251:2500]
    else:
        firstareatext = temp.businessmodel.coststructure
        secondareatext = ""
    
    ctx.set_source_rgb(0,0,0)
    ctx.translate(50,2450)
    pangocairo_context = pangocairo.CairoContext(ctx)
    layout = pangocairo_context.create_layout()
    layout.set_width(920)
    layout.set_alignment(pango.ALIGN_LEFT)
    layout.set_wrap(pango.WRAP_WORD)
    layout.set_width(pango.SCALE * 920)
    layout.set_font_description(pango.FontDescription("TitilliumText25L 25"))
    layout.set_text(firstareatext)
    pangocairo_context.update_layout(layout)
    pangocairo_context.show_layout(layout)
    ctx.translate(-50,-2450)
    
    # Second Area
    ctx.set_source_rgb(0.9,0.9,0.9)
    ctx.rectangle(1100, 2450, 920, 450)
    ctx.fill()
    
    ctx.set_source_rgb(0,0,0)
    ctx.translate(1100,2450)
    pangocairo_context = pangocairo.CairoContext(ctx)
    layout = pangocairo_context.create_layout()
    layout.set_width(920)
    layout.set_alignment(pango.ALIGN_LEFT)
    layout.set_wrap(pango.WRAP_WORD)
    layout.set_width(pango.SCALE * 920)
    layout.set_font_description(pango.FontDescription("TitilliumText25L 25"))
    layout.set_text(secondareatext)
    pangocairo_context.update_layout(layout)
    pangocairo_context.show_layout(layout)
    ctx.translate(-1100,-2450)
    
    
    # Revenue Stream text area
    ctx.set_source_rgb(0.9,0.9,0.9)
    ctx.rectangle(2530, 2530, 920, 370)
    ctx.fill()
    
    # Draw text in the Revenue Stream first text area
    if len(temp.businessmodel.revenuestreams) > 989:
        firstareatext = temp.businessmodel.revenuestreams[0:989]
        secondareatext = temp.businessmodel.revenuestreams[990:1978]
    else:
        firstareatext = temp.businessmodel.revenuestreams
        secondareatext = ""
        
    ctx.set_source_rgb(0,0,0)
    ctx.translate(2530,2530)
    pangocairo_context = pangocairo.CairoContext(ctx)
    layout = pangocairo_context.create_layout()
    layout.set_width(920)
    layout.set_alignment(pango.ALIGN_LEFT)
    layout.set_wrap(pango.WRAP_WORD)
    layout.set_width(pango.SCALE * 920)
    layout.set_font_description(pango.FontDescription("TitilliumText25L 25"))
    layout.set_text(firstareatext)
    pangocairo_context.update_layout(layout)
    pangocairo_context.show_layout(layout)
    ctx.translate(-2530,-2530)
    
    # Second Area
    ctx.set_source_rgb(0.9,0.9,0.9)
    ctx.rectangle(3600, 2530, 920, 370)
    ctx.fill()
    
    ctx.set_source_rgb(0,0,0)
    ctx.translate(3600,2530)
    pangocairo_context = pangocairo.CairoContext(ctx)
    layout = pangocairo_context.create_layout()
    layout.set_width(920)
    layout.set_alignment(pango.ALIGN_LEFT)
    layout.set_wrap(pango.WRAP_WORD)
    layout.set_width(pango.SCALE * 920)
    layout.set_font_description(pango.FontDescription("TitilliumText25L 25"))
    layout.set_text(secondareatext)
    pangocairo_context.update_layout(layout)
    pangocairo_context.show_layout(layout)
    ctx.translate(-3600,-2530)
    
    # Write the canvas as a .png file
    surface.write_to_png(filename)
    
if __name__ == "__main__":
    pass
