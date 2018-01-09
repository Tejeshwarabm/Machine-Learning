#! /usr/bin/env python

import os, sys
import Image

size = 128, 128

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            
            # Add Image.ANTIALIAS to the thumbnail() call. 
            # It's highly recommended in the docs and with this being the top answer, 
            # best practice should be followed. In other words: Replace im.thumbnail(size) 
            # by im.thumbnail(size, Image.ANTIALIAS)
            
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "JPEG")
        except IOError:
            print "cannot create thumbnail for '%s'" % infile
            
            
# Please refer documentation http://effbot.org/imagingbook/introduction.htm
