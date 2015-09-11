from distutils.core import setup

setup(name='smart_upload',
      version='1.0',
      description='smart uploader - uses smart_open to bulk upload files to S3 (or others)',
      author='Joel Ward',
      author_email='jmward@gmail.com',
      url='https://github.com/val314159/smart_upload',
      #packages=['distutils', 'distutils.command'],
      py_modules=['smart_upload'],
      scripts=['scripts/smart_upload'],
      install_requires='smart_open',
     )
