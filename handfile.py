import argparse
import os
import tempfile
import shutil
import zipfile
import logging

logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG, filename=u'mylog.log')


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    return parser


parser = createParser()
filename = parser.parse_args()

with tempfile.TemporaryDirectory() as tmpdir:
    logging.info(u'Created temporary directory "%s"' % tmpdir)
with zipfile.ZipFile(filename.filename, 'r') as zf:
    zf.extractall(path=tmpdir)

for i in os.walk(tmpdir):
    if "__init__.py" not in i[2] and i[1] == []:
        shutil.rmtree(i[0])
newname = (filename.filename).split(".")[0] + "_zip.zip"
logging.info(u'File name "%s" changed to "%s"' % (filename.filename, newname))

with zipfile.ZipFile(newname, "w") as zf:
    for dirpath, dirnames, files in os.walk(tmpdir):
        zf.write(tmpdir)
        for filename in files:
            zf.write(os.path.join(dirpath, filename))
logging.info(u'Archive file was created : "%s" ' % newname)
