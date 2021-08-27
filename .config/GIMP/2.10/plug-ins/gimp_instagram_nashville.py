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

#http://www.youtube.com/watch?v=Cb4S7hQu3Hg

from gimpfu import *

def nashville( img, draw ):
	
	current_f=pdb.gimp_context_get_foreground()

	img.disable_undo()

	lg=pdb.gimp_layer_group_new(img)
	pdb.gimp_image_insert_layer(img, lg, None, 0)
	pdb.gimp_item_set_name(lg,"Nashville Effect")

	#copy image
	drawCopy=pdb.gimp_layer_new_from_drawable(draw,img)
	pdb.gimp_image_insert_layer(img, drawCopy, lg, 0)
	pdb.gimp_item_set_name(drawCopy,"NashvilleBG")

	#adjust curves colors
	pdb.gimp_curves_spline(drawCopy, 2, 4, (0,37, 255,255) )
	pdb.gimp_curves_spline(drawCopy, 3, 4, (0,131, 255,255) )

	#adjust levels colors
	pdb.gimp_levels(drawCopy, 0, 0, 236, 1.36, 0, 255)

	#adjust brightness contrast
	pdb.gimp_brightness_contrast(drawCopy, 6, 12)

	#adjust curves colors
	pdb.gimp_curves_spline(drawCopy, 2, 4, (13,0, 255,255) )
	pdb.gimp_curves_spline(drawCopy, 3, 4, (88,0, 255,255) )

	#adjust brightness contrast
	pdb.gimp_brightness_contrast(drawCopy, -6, 5)

	#adjust curves colors
	pdb.gimp_curves_spline(drawCopy, 1, 4, (0,4, 255,255) )
	pdb.gimp_curves_spline(drawCopy, 3, 4, (0,14, 255,255) )

	pdb.gimp_selection_all
	sel_size=pdb.gimp_selection_bounds(img)
	w=sel_size[3]-sel_size[1]
	h=sel_size[4]-sel_size[2]

	l = pdb.gimp_layer_new(img,w,h,0,"NashvilleCol",100.0,3)
	pdb.gimp_image_insert_layer(img, l, lg, 0)

	pdb.gimp_image_set_active_layer(img,l)

	pdb.gimp_context_set_foreground((255,218,173))

	pdb.gimp_edit_fill(l,0)

	pdb.gimp_selection_clear(img)

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


register( "gimp_instagram_nashville",
  "Add Instagram Nashville effect",
  "Add Instagram Nashville effect",
  "Marco Crippa",
  "(©) 2013 Marco Crippa",
  "2013-01-08",
  "<Image>/Filters/Instagram/Nashville",
  'RGB*',
  [],
  '',
  nashville)

main()

