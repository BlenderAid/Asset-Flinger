#!/usr/bin/env python

import sys
import os
import subprocess

def callBlender(filename):
	blenderFilename = "/usr/bin/blender"
	blendFilename = os.path.join(os.path.dirname(os.path.realpath(__file__)), ".thumbnailer_MTL/Thumbnailer.blend")
	command = [blenderFilename, "-b", blendFilename , "--python-text", "ThumbScript", "--objFiles", filename]
	proc = subprocess.Popen(command)


if __name__=="__main__":
	if len(sys.argv)>1:
		for n in sys.argv[1:]:
			callBlender(n)

	raw_input()
