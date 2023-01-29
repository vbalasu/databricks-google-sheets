from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='databricks-google-sheets',
    version='0.8.0',
    author='Vijay Balasubramaniam',
    author_email='vbalasu@gmail.com',
    description='Interact with Google Sheets from Databricks',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vbalasu/databricks-google-sheets',
    packages=find_packages(),
    py_modules=['databricks_google_sheets'],
    install_requires=['gspread-pandas'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
