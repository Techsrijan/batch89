'''the format is;
\033[  Escape code, this is always the same
1 = Style, 1 for normal.
32 = Text colour, 32 for bright green.
40m = Background colour, 40 is for black.'''

'''


This table shows some of the available formats;
TEXT COLOR	CODE	   TEXT STYLE	CODE	BACKGROUND COLOR	CODE
Black	    30	        No effect	0	      Black	            40
Red	        31	        Bold	    1	      Red	            41
Green	    32	        Underline	2	      Green	            42
Yellow	    33	        Negative1	3	      Yellow        	43
Blue	    34	        Negative2	5	       Blue	            44
Purple	    35			                       Purple	        45
Cyan	    36			                        Cyan	        46
White	    37		                         	White	        47'''''

print('Techsrijan Consultancy services Pvt Limited')

print("\033[1;33;44m Techsrijan Consultancy services Pvt Limited  ")