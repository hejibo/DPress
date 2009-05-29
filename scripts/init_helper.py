import os, zipfile

z = zipfile.ZipFile("../libs/tiny_mce.zip", 'r')

for f in z.namelist():
    new_filename = os.path.join("../static/", f)
    if not os.path.exists(os.path.dirname(new_filename)):
        os.mkdir(os.path.dirname(new_filename))
    if new_filename[-1:][0] not in ('\\', '/'):
        file(new_filename, 'wb').write(z.read(f))
