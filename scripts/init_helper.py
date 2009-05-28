import os, zipfile

z = zipfile.ZipFile("../libs/tiny_mce.zip", 'r')

for f in z.namelist():
    path = os.path.join("../static/", f)
    if not os.path.exists(os.path.dirname(path)):
        os.mkdir(os.path.dirname(path))
    print path
    print f

