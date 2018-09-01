#! /usr/bin/python2.7 -tt

import sys
import argparse
import os.path
import operator
import subprocess
import datetime

def main():
	wdir = os.path.abspath(sys.argv[1])
	print "The working directory is " + wdir
	
	# get a list of subdirectories and save the wdir and filenames as a tuple
	imdir = list()
	for filenames in os.listdir(wdir):
		if os.path.isdir(os.path.join(wdir, filenames)):
			imdir.append((wdir, filenames))	

	for id_imdir in imdir:
		dir = id_imdir[0]
		id = id_imdir[1]
		print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
		print "Current directory: %s | AnonCode is: %s" % (os.path.join(dir,id),id)
		for root,_,filenames in os.walk(os.path.join(dir,id)):
			print "Found %i files in %s" % (len(filenames),root)
			for filename in filenames:
				try:
					anonDcm(os.path.join(root,filename), id)
				except:
					continue


def anonDcm(file, id):
	os.system('dcmodify -m "(0008,0020)=%s" "%s" -nb -imt -q' % ('20010101',file))
	os.system('dcmodify -m "(0008,0021)=%s" "%s" -nb -imt -q' % ('20010101',file))
	os.system('dcmodify -m "(0008,0022)=%s" "%s" -nb -imt -q' % ('20010101',file))
	os.system('dcmodify -m "(0008,0023)=%s" "%s" -nb -imt -q' % ('20010101',file))
	os.system('dcmodify -m "(0008,0030)=%s" "%s" -nb -imt -q' % ('120101',file))
	os.system('dcmodify -m "(0008,0031)=%s" "%s" -nb -imt -q' % ('120101',file))
	os.system('dcmodify -m "(0008,0032)=%s" "%s" -nb -imt -q' % ('120101',file))
	os.system('dcmodify -m "(0008,0033)=%s" "%s" -nb -imt -q' % ('120101',file))
	os.system('dcmodify -m "(0008,0090)=%s" "%s" -nb -imt -q' % (id,file))
	os.system('dcmodify -m "(0008,1070)=%s" "%s" -nb -imt -q' % (id,file))
	os.system('dcmodify -m "(0010,0010)=%s" "%s" -nb -imt -q' % (id,file))
	os.system('dcmodify -m "(0010,0020)=%s" "%s" -nb -imt -q' % (id,file))
	os.system('dcmodify -m "(0010,0030)=%s" "%s" -nb -imt -q' % ('20010101',file))
	os.system('dcmodify -m "(0010,0040)=%s" "%s" -nb -imt -q' % ('',file))
	os.system('dcmodify -m "(0010,1010)=%s" "%s" -nb -imt -q' % ('01Y',file))
	os.system('dcmodify -m "(0010,1030)=%s" "%s" -nb -imt -q' % ('100',file))
	os.system('dcmodify -m "(0010,21b0)=%s" "%s" -nb -imt -q' % (id,file))
	os.system('dcmodify -m "(0038,0010)=%s" "%s" -nb -imt -q' % (id,file))
	os.system('dcmodify -m "(0038,0011)=%s" "%s" -nb -imt -q' % (id,file))
	os.system('dcmodify -m "(0040,0244)=%s" "%s" -nb -imt -q' % ('20010101',file))



if __name__ == '__main__':
        main()


