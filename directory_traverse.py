# -*- coding:utf-8 -*-
import os
fout=open('tree_test.txt','w')
def directory_traverse(path,depth=0,isFinal=False):
	if os.path.isfile(path):
		try:
			pass
		except:
			pass
	elif os.path.isdir(path):
		for i in range(depth):
			print >>fout,'©¦',
			for j in range(1):
				print >>fout,' ',
		if not isFinal:
			print >>fout,'©À©¤'+os.path.basename(path)
		else:
			print >>fout,'©¸©¤'+os.path.basename(path)

		dirs=os.listdir(path)
		num_dirs=len(dirs)
		for i,item in enumerate(dirs):
			itemsrc=os.path.join(path,item)
			if i==num_dirs-1:
				directory_traverse(itemsrc,depth+1,True)
			else:
				directory_traverse(itemsrc,depth+1,False)


directory_traverse('../../20130809')
