from setuptools import setup, find_packages

setup(
    name="clipboard_manager",
    version="0.1",
    packages=find_packages(),
    install_requires=["pyperclip", "colorama"],
    entry_points={
        "console_scripts": [
            "clipboard_manager=clipboard_manager:main",
        ],
    },
)
