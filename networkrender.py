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


import networkx as nx
#import matplotlib.pyplot as plt
import cairo
import math


originY = 70
whiteBorder = 10
max_width = 1280
max_height = 1024
font_size = 14
originAreaY = 130
originAreaX = whiteBorder + 200

# Load graph and calculate layout
G = nx.read_graphml("miserables.graphml")
pos = nx.spring_layout(G,scale=1)
nx.set_node_attributes(G,'pos',pos)

# Max x coordinate:
# max(data[0] for data in pos.values())
# Max y coordinate:
# max(data[1] for data in pos.values())



# Initialize canvas
surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, originAreaX+max_width+whiteBorder, max_height+originAreaY+whiteBorder)
ctx = cairo.Context (surface)

# Paint background
ctx.set_source_rgb(1, 1, 1) # blue
ctx.rectangle(0, 0, originAreaX+max_width+whiteBorder, max_height+originAreaY+whiteBorder)
ctx.fill()

# Write the canvas title
ctx.set_source_rgb(0, 0, 0)
ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
ctx.set_font_size(32)
ctx.move_to(10, 32)
ctx.show_text("Networks of interactions in the Open Design process")

print G.node

# Draw the legend
for i in G.nodes_iter():
    print G[i]["label"]

# Draw edges
for j in G.edges_iter():
    # Draw edges
    ctx.set_source_rgba(0, 0, 0,0.2)
    ctx.set_line_width(1)
    ctx.move_to(originAreaX+pos[j[0]][0]*max_width, originAreaY+pos[j[0]][1]*max_height)
    ctx.line_to(originAreaX+pos[j[1]][0]*max_width, originAreaY+pos[j[1]][1]*max_height) 
    ctx.stroke()

    # Draw arrows

    

# Assign degree to the nodes
deg = nx.degree_centrality(G)
for i in G.nodes_iter():
    G[i]["weight"] = deg[i]

# Assign betweenness to the nodes
#bet = nx.betweenness_centrality(G)
#for i in G.nodes_iter():
#    G[i]["betweenness"] = bet[i]

# Draw nodes
for i in G.nodes_iter():
    ctx.set_line_width(4)
    ctx.set_source_rgb(0.7, 0.2, 0.0)
    ctx.arc(int(originAreaX+max_width*pos[i][0]), int(originAreaY + max_height*pos[i][1]), G[i]["weight"]*50, 0, 2*math.pi)
    ctx.stroke_preserve()
    ctx.set_source_rgb(0.3, 0.4, 0.6)
    ctx.fill()


# Draw labels
for i in G.nodes_iter():
    ctx.set_source_rgb(0, 0, 0)
    ctx.select_font_face("TitilliumText25L", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(font_size)
    ctx.move_to(int(originAreaX+max_width*pos[i][0])+5+G[i]["weight"]*50, int(originAreaY+max_height*pos[i][1]))
    ctx.show_text(i)



surface.write_to_png ("example.png") # Output to PNG
