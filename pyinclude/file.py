import os

def get_contents(fn, mode="r"):
	try:
		d=open(fn, mode)
		return d.read()
	except:
		return ""

def put_contents(fn, content, mode="r"):
	try:
		f=open(fn, mode)
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