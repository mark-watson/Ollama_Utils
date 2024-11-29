from setuptools import setup, find_packages

setup(
    name="ollama_tools",
    version="0.1.0",
    author="Mark Watson",
    author_email="markw@markwatson.com",
    description="A Python package for tools related to Ollama",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mark-watson/Ollama_Tools",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        # Add your package dependencies here
    ],
)
