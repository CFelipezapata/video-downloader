from distutils.core import setup

setup(name='VideoDownloader',
      version='1.0',
      description='Download videos from youtube',
      author='Felipe Zapata',
      packages=['downloader'],
      install_requires=['pytube', 'python-dotenv'],
      entry_points={
          'console_scripts': ['vdownload = downloader.downloader:main']
      }
      )
