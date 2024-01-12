import setuptools
# readme.md = github readme.md, 這裡可接受markdown寫法
# 如果沒有的話，需要自己打出介紹此專案的檔案，再讓程式知道
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AILocator",
    version="0.0.1",
    author="Lin Yeh",
    author_email="lin_yeh@outlook.com",
    description="ui automator based on Appium, YOLO, OCR",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GPL-3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
