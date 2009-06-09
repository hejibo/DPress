import os, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
DPRESS_ROOT = STATIC_FOLDER = os.path.join(HERE, "../../")
STATIC_FOLDER = os.path.join(HERE, "../../static/")

def unzip(zip_file, obj_folder):
    z = zipfile.ZipFile(zip_file, 'r')
    for f in z.namelist():
        new_filename = os.path.join(STATIC_FOLDER, f)
        if not os.path.exists(os.path.dirname(new_filename)):
            os.mkdir(os.path.dirname(new_filename))
        if new_filename[-1:][0] not in ('\\', '/'):
            file(new_filename, 'wb').write(z.read(f))

if __name__ == '__main__':
    unzip(os.path.join(DPRESS_ROOT, "libs/tiny_mce.zip"),
            STATIC_FOLDER)
    unzip(os.path.join(DPRESS_ROOT, "libs/syntaxhighlighter.zip"),
            STATIC_FOLDER)
