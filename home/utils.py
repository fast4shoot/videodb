# -*- coding: utf-8 -*-

import tempfile, shutil, os
def create_temporary_copy(path):
	temp_dir = tempfile.gettempdir()
	temp_path = os.path.join(temp_dir, os.path.basename(path) + "copy")
	shutil.copy2(path, temp_path)
	return temp_path
