#!/usr/bin/env python
# -*- coding: utf8 -*-

# *************************************************************************** #
#                                                                             #
#      Version 0.1 - 2013-08-01                                               #
#      Copyright (C) 2013 Marco Crippa                                        #
#                                                                             #
#      This program is free software; you can redistribute it and/or          #
#      modify it under the terms of the GNU General Public License            #
#      as published by the Free Software Foundation; either version 2         #
#      of the License, or (at your option) any later version.                 #
#                                                                             #
#      This program is distributed in the hope that it will be useful,        #
#      but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#      GNU General Public License for more details.                           #
#                                                                             #
#      You should have received a copy of the GNU General Public License      #
#      along with this program; if not, write to the                          #
#      Free Software Foundation, Inc.,                                        #
#      51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA           #
#                                                                             #
# *************************************************************************** #

#http://www.youtube.com/watch?v=2GwOi1lJYPo

from gimpfu import *

def earlybird( img, draw ):
	
	current_f=pdb.gimp_context_get_foreground()

	img.disable_undo()

	lg=pdb.gimp_layer_group_new(img)
	pdb.gimp_image_insert_layer(img, lg, None, 0)
	pdb.gimp_item_set_name(lg,"Earlybird Effect")

	#copy image
	drawCopy=pdb.gimp_layer_new_from_drawable(draw,img)
	pdb.gimp_image_insert_layer(img, drawCopy, lg, 0)
	pdb.gimp_item_set_name(drawCopy,"earlybirdBG")

	#adjust hue, saturation and lightness
	pdb.gimp_hue_saturation(drawCopy,0,0,1,-30)

	#adjust levels colors
	pdb.gimp_levels(drawCopy, 0, 0, 255, 1.2, 0, 255)
	pdb.gimp_levels(drawCopy, 1, 0, 255, 1.0, 25, 255)

	#adjust brightness contrast
	pdb.gimp_brightness_contrast(drawCopy, 8, 20)

	#adjust hue, saturation and lightness
	pdb.gimp_hue_saturation(drawCopy,0,0,0,-15)

	#adjust levels colors
	pdb.gimp_levels(drawCopy, 0, 0, 235, 0.9, 0, 255)


	pdb.gimp_selection_all
	sel_size=pdb.gimp_selection_bounds(img)
	w=sel_size[3]-sel_size[1]
	h=sel_size[4]-sel_size[2]

	#set new color layer
	l = pdb.gimp_layer_new(img,w,h,0,"earlybirdCol",100.0,3)
	pdb.gimp_image_insert_layer(img, l, lg, 0)
	pdb.gimp_image_set_active_layer(img,l)
	pdb.gimp_context_set_foreground((252,243,214))
	pdb.gimp_edit_fill(l,0)
	pdb.gimp_selection_clear(img)

	#create vignette
	v = pdb.gimp_layer_new(img,w,h,1,"vignette",100.0,17)
	pdb.gimp_image_insert_layer(img, v, lg, 0)
	pdb.gimp_image_set_active_layer(img,v)
	pdb.gimp_image_select_ellipse(img,0,0,0,w,h)
	if w>=h:
		lat=w
	else:
		lat=h
	pdb.gimp_selection_feather(img,lat/10)
	pdb.gimp_selection_invert(img)
	pdb.gimp_context_set_foreground((184,184,184))
	pdb.gimp_edit_fill(v,0)
	pdb.gimp_selection_clear(img)
	pdb.gimp_layer_set_opacity(v,60)

	#add white border
	Wborder = pdb.gimp_layer_new(img,w,h,1,"whiteBorder",100.0,0)
	pdb.gimp_image_insert_layer(img, Wborder, lg, 0)
	pdb.gimp_image_set_active_layer(img,Wborder)
	pdb.gimp_context_set_foreground((255,255,255))
	pdb.gimp_image_select_rectangle(img, 0, 0,0, w,h )
	dimBorder=int( (w/100)*2 )
	if dimBorder<5:
		dimBorder=5
	pdb.gimp_selection_shrink(img, dimBorder)
	pdb.gimp_selection_invert(img)
	pdb.gimp_edit_fill(Wborder,0)
	pdb.gimp_selection_clear(img)
	
	#add black border
	Bborder = pdb.gimp_layer_new(img,w,h,1,"blackBorder",100.0,0)
	pdb.gimp_image_insert_layer(img, Bborder, lg, 0)
	pdb.gimp_image_set_active_layer(img,Bborder)
	pdb.gimp_context_set_foreground((0,0,0))
	pdb.gimp_image_select_rectangle(img, 0, 0,0, w,h )
	dimBorder=int( (w/100)*2 )
	if dimBorder<5:
		dimBorder=5
	pdb.gimp_selection_shrink(img, dimBorder)
	pdb.gimp_selection_invert(img)
	pdb.gimp_edit_fill(Bborder,0)
	pdb.gimp_selection_clear(img)

	img.enable_undo()

	pdb.gimp_context_set_foreground(current_f)


register( "gimp_instagram_earlybird",
  "Add Instagram Earlybird effect",
  "Add Instagram Earlybird effect",
  "Marco Crippa",
  "(©) 2013 Marco Crippa",
  "2013-01-08",
  "<Image>/Filters/Instagram/Earlybird",
  'RGB*',
  [],
  '',
  earlybird)

main()

