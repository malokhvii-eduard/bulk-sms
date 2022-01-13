<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD041 -->

<div align="center">
  <h2 align="center">📮 Bulk SMS</h2>
  <p align="center">
    A simple tool to send
    <a href="https://en.wikipedia.org/wiki/SMS" arial-label="SMS">SMS</a>
    messages over the carrier's network from an Android phone using the
    <a href="https://developer.android.com/studio/command-line/adb"
      aria-label="Android Debug Bridge">Android Debug Bridge</a>.
  </p>

  <p id="shields" align="center" markdown="1">

[![License](https://img.shields.io/badge/license-MIT-3178C6?style=flat)](LICENSE)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][github-pre-commit]
![Style Guide](https://img.shields.io/badge/code%20style-black-000?style=flat)
[![markdownlint](https://img.shields.io/badge/linter-markdownlint-000?style=flat)][github-markdownlint]
[![commitlint](https://img.shields.io/badge/linter-commitlint-F7B93E?style=flat)][github-commitlint]
[![flake8](https://img.shields.io/badge/linter-flake8-3776AB?style=flat)][github-flake8]
[![bandit](https://img.shields.io/badge/linter-bandit-FFC107?style=flat)][github-bandit]

  </p>
</div>

## 🎉 Features

- 🗜️ Small (~126 lines)
- 🐍 Pure Python tool
- 🔌 Working with multiple devices

## 🌻 Motivation

Probably just for fun at first 🙃. Secondly, for low-cost SMS marketing
campaigns without any equipment or external services.

### 📚 Prerequisites

Firstly you will need to install [Android Debug Bridge][android-adb] and
[Messages][google-play-messages] application from Google Play. Next, you
will need to turn on [Developer Options][android-developer-options] on your
Android phone. After the Developer Options are enabled, turn on Stay Awake and
[USB Debugging][android-debugging]. Finally, plug your phone into your computer
using a USB cable, copy a message to the clipboard on your phone and check that
you have enough credit to send SMS 😅, so here we go! 🚀.

### 📦 Installation

1. Clone the *Repository*
2. Install this *Package* (`./setup.py install`) or install dependencies from
[Pipfile](Pipfile) (`pipenv install`)

### 👀 Usage

```console
bulk-sms --help # Show help and exit
bulk-sms -p "+380500412697" -p "+380500447879" # Send multiple
bulk-sms -d -p "+380500412697" # Save SMS as Draft
bulk-sms -x -p "+380500412697" # Delete SMS after sending
cat phones.txt | bulk-sms # Send multiple from file
```

## 🛠️ Tech Stack

<!-- markdownlint-disable MD013 -->
[![EditorConfig](https://img.shields.io/badge/EditorConfig-FEFEFE?logo=editorconfig&logoColor=000&style=flat)][editorconfig]
![Markdown](https://img.shields.io/badge/Markdown-000?logo=markdown&logoColor=fff&style=flat)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=flat)
[![androidviewclient](https://img.shields.io/badge/androidviewclient-3DDC84?logo=android&logoColor=fff&style=flat)][github-androidviewclient]
[![click](https://img.shields.io/badge/click-4EAA25?logo=gnubash&logoColor=fff&style=flat)][github-click]
[![tqdm](https://img.shields.io/badge/tqdm-FFC107?logo=tqdm&logoColor=000&style=flat)][github-tqdm]
[![pre-commit](https://img.shields.io/badge/pre--commit-FAB040?logo=precommit&logoColor=fff&style=flat)][github-pre-commit]
[![markdownlint](https://img.shields.io/badge/markdownlint-000?logo=markdown&logoColor=fff&style=flat)][github-markdownlint]
[![commitlint](https://img.shields.io/badge/commitlint-F7B93E?logo=c&logoColor=000&style=flat)][github-commitlint]
[![Shields.io](https://img.shields.io/badge/Shields.io-000?logo=shieldsdotio&logoColor=fff&style=flat)][shields]
[![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff&style=flat)][git-scm]
[![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=flat)][github]
<!-- markdownlint-enable MD013 -->

## ✍️ Contributing

👍🎉 *First off, thanks for taking the time to contribute!* 🎉👍

Contributions are what make the open source community such an amazing place to
be learn, inspire, and create. Any contributions you make are **greatly
appreciated**.

1. Fork the *Project*
2. Create your *Feature Branch* (`git checkout -b feature/awesome-feature`)
3. Commit your *Changes* (`git commit -m 'Add awesome feature'`)
4. Push to the *Branch* (`git push origin feature/awesome-feature`)
5. Open a *Pull Request*

## 💖 Like this project?

Leave a ⭐ if you think this project is cool or useful for you.

## ⚠️ License

`bulk-sms` is licenced under the MIT License. See the [LICENSE](LICENSE)
for more information.

<!-- markdownlint-disable MD013 -->
<!-- Github links -->
[github-androidviewclient]: https://github.com/dtmilano/AndroidViewClient
[github-bandit]: https://github.com/PyCQA/bandit
[github-black]: https://github.com/psf/black
[github-click]: https://github.com/pallets/click
[github-commitlint]: https://github.com/conventional-changelog/
[github-flake8]: https://github.com/PyCQA/flake8
[github-markdownlint]: https://github.com/DavidAnson/markdownlint
[github-pre-commit]: https://github.com/pre-commit/pre-commit
[github-tqdm]: https://github.com/tqdm/tqdm
[github]: https://github.com

<!-- Other links -->
[android-adb]: https://developer.android.com/studio/command-line/adb
[android-debugging]: https://developer.android.com/studio/debug/dev-options#debugging
[android-developer-options]: https://developer.android.com/studio/debug/dev-options#enable
[editorconfig]: https://editorconfig.org
[git-scm]: https://git-scm.com
[google-play-messages]: https://play.google.com/store/apps/details?id=com.google.android.apps.messaging&hl=en_US&gl=US
[shields]: https://shields.io
