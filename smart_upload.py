import os, sys, stat
from smart_open import smart_open

def smart_upload(remotefs,localfs='.',tab='',policy='public-read'):
    for dirname in os.listdir(localfs):
        if dirname.startswith('.'):
            continue
        fulllocalname  = os.path.join(localfs, dirname)
        fullremotename = os.path.join(remotefs,dirname)
        if os.path.isdir(fulllocalname):
            recursive_upload( fullremotename, fulllocalname, '- '+tab )
        else:
            fr = smart_open(fulllocalname, 'rb')
            fw = smart_open(fullremotename,'wb',policy=policy)
            try:
                for line in fr:
                    fw.write( line )
            finally:
                fr.close()
                fw.close()
                pass
            pass
        pass
    pass

def cli(args=sys.argv[1:]): smart_upload( *args )

if __name__=='__main__': cli()
