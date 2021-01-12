# Single letter codes color Matplotlib :
# character color
# 'b'		blue
# 'g'		green
# 'r'		red
# 'c'		cyan
# 'm'		magenta
# 'y'		yellow
# 'k'		black
# 'w'		white

# 	Markers
# character	description
# =============================
# '.'		point marker
# ','		pixel marker
# 'o'		circle marker
# 'v'		triangle_down marker
# '^'		triangle_up marker
# '<'		triangle_left marker
# '>'		triangle_right marker
# '1'		tri_down marker
# '2'		tri_up marker
# '3'		tri_left marker
# '4'		tri_right marker
# 's'		square marker
# 'p'		pentagon marker
# '*'		star marker
# 'h'		hexagon1 marker
# 'H'		hexagon2 marker
# '+'		plus marker
# 'x'		x marker
# 'D'		diamond marker
# 'd'		thin_diamond marker
# '|'		vline marker
# '_'		hline marker

# Line Styles
# character	description
# '-'		solid line style
# '--'		dashed line style
# '-.'		dash-dot line style
# ':'		dotted line style

import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0,10,0.5)
plt.plot(a, "go:", a**3, "r^--", a**2, "c+-.")

plt.xlabel("x is label")
plt.ylabel("y is label")
plt.title("Fist Plot Format String")
plt.show()