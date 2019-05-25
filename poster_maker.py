import numpy as np
import string
import os
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import scrape_logo
from input_poster import poster_input

def make_poster(size=(8.5, 11), margin=0.5, dpi=100, channel='green'):
		inps = poster_input({})
		reqs = inps.get_resp()

		path1 = scrape_logo.main(reqs['talk1'])
		path2 = scrape_logo.main(reqs['talk2'])
		
		plt.ion()
		fig = plt.figure('poster', figsize=size, dpi=dpi)

		xsize = float(size[0])
		ysize = float(size[1])
		aspect = ysize/xsize

		ax = plt.subplot()
		ax.cla()
		plt.setp(ax.get_xticklabels(), visible=False)
		plt.setp(ax.get_xticklines(), visible=False)
		plt.setp(ax.get_yticklabels(), visible=False)
		plt.setp(ax.get_yticklines(), visible=False)

		plt.xlim(0 , 8.5) 
		plt.ylim(0 , 11)
		plt.subplots_adjust(left=margin/xsize, right=1.0 - margin/xsize, top=1.0 - margin/ysize, bottom=margin/ysize)

		ax.set_facecolor('xkcd:' + reqs['bgcolor'])
		ax.set_facecolor((1.0, 0.47, 0.42))

		ax.text(4.25, 0.75, reqs['time'] , fontsize=30, ha='center', weight='normal', color=reqs['fontcolor'])
		ax.text(4.25, 2, reqs['venue'], fontsize=30, ha='center', weight='bold', color=reqs['fontcolor'])
		ax.text(4.25, 10, reqs['title'] , fontsize=80, color=reqs['fontcolor'], ha='center' , weight='bold', va='top')
		ax.text(2, 7, reqs['talk1'] + '-- ' + reqs['spk1'] , fontsize=30, color=reqs['fontcolor'],  weight='bold')
		ax.text(2, 6, reqs['talk2']  + '-- ' + reqs['spk2'], fontsize=30, color=reqs['fontcolor'],  weight='bold')

		
		im1 = plt.imread(path1)
		im2 = plt.imread(path2)

		ax.imshow(im1, aspect='auto', extent=(3, 4.25, 7, 9), zorder=-1)
		ax.imshow(im2, aspect='auto', extent=(3, 4.25, 4, 6), zorder=-1)
		plt.savefig('outut.jpg')
		plt.draw()
		
		
make_poster()