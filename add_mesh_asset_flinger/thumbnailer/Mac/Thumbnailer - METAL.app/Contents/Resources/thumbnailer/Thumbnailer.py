#!/usr/bin/env python

import sys
import os
import subprocess
import logging


def callBlender(filepath):
	import json
	path_config = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'thumbnailer/config')
	logging.debug(path_config)
	with open(path_config, "r") as config:
		print("Loading custom config")
		logging.debug('Loading custom config')
		config = json.load(config)
		blender_path = config["blender_path"]
		logging.info(blender_path)

	blendfile_render = os.path.join(os.path.dirname(os.path.realpath(__file__)), "thumbnailer/Thumbnailer.blend")
	command = [blender_path, "-b", blendfile_render , "--python-text", "ThumbScript", "--objFiles", filepath]

	proc = subprocess.Popen(command)

if __name__=="__main__":
	logging.basicConfig(filename='/tmp/flinger_debug.log', level=logging.DEBUG)
	if len(sys.argv)>1:
		logging.info('Running smoothly')
		for filepath in sys.argv[1:]:
			logging.info(filepath)
			callBlender(filepath)
	else:
		logging.info('Running failing')


	raw_input()
