#!/usr/bin/env python3

import sys

from setuptools import setup

assert sys.version_info >= (3, 7), "bulk-sms requires Python 3.7+"
from pathlib import Path  # noqa E402


CURRENT_DIR = Path(__file__).parent
sys.path.insert(0, str(CURRENT_DIR))  # for setuptools.build_meta


def get_long_description() -> str:
    return (CURRENT_DIR / "README.md").read_text(encoding="utf8")


if __name__ == "__main__":
    setup(
        version="1.0.0",
        name="bulk-sms",
        description=(
            "A simple tool to send SMS messages over the carrier's network "
            "from an Android phone using the Android Debug Bridge."
        ),
        long_description=get_long_description(),
        long_description_content_type="text/markdown",
        author="Eduard Malokhvii",
        author_email="malokhvii.ee@gmail.com",
        url="https://github.com/malokhvii-eduard/bulk-sms",
        license="MIT",
        py_modules=["bulk_sms"],
        python_requires=">= 3.7",
        install_requires=[
            "androidviewclient>=20.4.4",
            "click>=8.0.3",
            "phonenumbers>=8.12.41",
            "tqdm>=4.62.3",
        ],
        entry_points={
            "console_scripts": [
                "bulk-sms=bulk_sms:main",
            ]
        },
    )
