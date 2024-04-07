import os

def get_contents(fn, mode="r"):
	try:
		with open(fn, mode) as d:
			return d.read()
	except:
		return ""

def put_contents(fn, content, mode="w", overwrite=True):
	if not overwrite and exists(fn): return False
	try:
		with open(fn, mode) as f:
			f.write(content)
			return True
	except:
		return False

def exists(p):
	return os.path.exists(p)

def delete(p):
	if exists(p):
		os.remove(p)
		return True
	else:
		return False

def get_size(fn):
	return os.path.getsize(fn)