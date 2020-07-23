
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
   from setupext_janitor import janitor
   CleanCommand = janitor.CleanCommand
except ImportError:
   CleanCommand = None

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

cmd_classes = {}
if CleanCommand is not None:
   cmd_classes['clean'] = CleanCommand

INSTALL_REQUIRES = [
    'kubernetes-py>=1.10.7.4',
    'powerline-status>=2.7',
    ]

def version():
    with open(os.path.abspath(__file__).replace('setup.py', 'version.meta'), 'r') as v:
        return v.read().replace('\n', '')

# Heavily inspired by the powerline-kubernetes library written by Vincent De Smet
# (vincent.drl@gmail.com) and located at https://github.com/so0k/powerline-kubernetes
setup(
    setup_requires=['setupext_janitor'],
    cmdclass=cmd_classes,
    entry_points={
      # normal parameters, ie. console_scripts[]
      'distutils.commands': [
         ' clean = setupext_janitor.janitor:CleanCommand']
     },
    name='powerkube-fork',
    version=version(),
    description='A powerline segment to show kubernetes context items, with toggling and alert color functionality',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Scott MacGregor',
    author_email='smacgregor@d2iq.com',
    url='https://github.com/d2iq-shadowbq/powerkube-fork',
    download_url='https://github.com/d2iq-shadowbq/powerkube-fork/tarball/'+ version(),
    
    packages=['powerkube_fork'],
    python_requires='>=3.6',
    install_requires=INSTALL_REQUIRES,
    license='Apache 2.0',
    keywords=['kubernetes_py','k8s','powerline','powerkube'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Terminals'
    ]
)
