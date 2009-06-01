import os, zipfile

STATIC_FOLDER = "../static/"

def unzip(zip_file, obj_folder):
    z = zipfile.ZipFile(zip_file, 'r')
    for f in z.namelist():
        new_filename = os.path.join(STATIC_FOLDER, f)
        if not os.path.exists(os.path.dirname(new_filename)):
            os.mkdir(os.path.dirname(new_filename))
        if new_filename[-1:][0] not in ('\\', '/'):
            file(new_filename, 'wb').write(z.read(f))

unzip("../libs/tiny_mce.zip", STATIC_FOLDER)
unzip("../libs/syntaxhighlighter.zip", STATIC_FOLDER)
