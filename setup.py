from setuptools import setup, find_packages

setup(
    name="auth_module",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A reusable authentication module for Python applications",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/auth_module",
    packages=find_packages(),
    install_requires=[
        "pyjwt==2.8.0",
        "python-dotenv==1.0.0",
        "argon2-cffi==23.1.0"
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)