import setuptools
from pathlib import Path


CURRENT_FOLDER = Path(__file__).parent
README_PATH = CURRENT_FOLDER / 'README.md'


def main():
    setuptools.setup(
        name = "signapp",
        version = "1.0.1",
        author = "Ariel Tubul",
        description = "Apk signer script",
        packages = setuptools.find_packages(),
        long_description = README_PATH.read_text(),
        url = "https://github.com/mon231/signapp/",
        long_description_content_type='text/markdown',
        entry_points = {'console_scripts': ['signapp=signapp.signapp:main', 'signapp_fetch_tools=signapp.download_tools:main']},
        install_requires = ['requests']
    )


if __name__ == '__main__':
    main()
