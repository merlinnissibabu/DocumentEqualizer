import os
from setuptools import setup, find_packages
import codecs

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(name="Doc_Equalizer",
      version="0.0.4",
      author="Merlin",
      author_email="merlinnissibabu@gmail.com",
      description="A small example package",
      long_description_content_type="text/markdown",
      long_description=long_description,
      packages=find_packages(),
      license="MIT",
      python_requires=">=3.6",
      install_requires=[
          'pdf2image == 1.16.0',
          'PyPDF2',
          'numpy == 1.19.5']
)
