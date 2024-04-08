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

def select_file(title="Choose File", wildcard="All files (*.*)|*.*", multi=False):
	app = wx.App(False)  # Create wx.App object
	style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
	if multi:
		style |= wx.FD_MULTIPLE
	dialog = wx.FileDialog(None, title, wildcard=wildcard, style=style)
	paths = []

	if dialog.ShowModal() == wx.ID_OK:
		if multi:
			paths = dialog.GetPaths()
		else:
			paths = [dialog.GetPath()]
	dialog.Destroy()
	app.ExitMainLoop()  # Destroy wx.App object
	return paths

def select_folder(title="Choose Folder"):
	app = wx.App(False)  # Create wx.App object
	dialog = wx.DirDialog(None, title)
	path = ""

	if dialog.ShowModal() == wx.ID_OK:
		path = dialog.GetPath()
	dialog.Destroy()
	app.ExitMainLoop()  # Destroy wx.App object
	return path
