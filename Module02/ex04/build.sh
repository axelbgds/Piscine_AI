python3 -m pip install --upgrade build twine wheel setuptools
python3 -m build my_minipack
python3 -m twine upload --repository testpypi my_minipack/dist/*