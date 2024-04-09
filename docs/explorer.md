# Functions

```
import pyinclude.explorer as fileobj
f=fileobj.file()
d=fileobj.dir()
```

## `get_contents(fn, mode="r")`

Return the file contents. You can use this on file.

## `put_contents(fn, content, mode="r", overwrite=True)`

Puts the contents into the file, return True or False. You can use on file class.

## `exists(p)`

Checks whether the file is exists. You can use this on file and dir.

## `delete(p)`

Deletes the file. You can use on file and dir.

## `get_size(fn)`

Return the file's size in bytes. Only file class.

## `search(desk)`

Searches a list of files / dirs.