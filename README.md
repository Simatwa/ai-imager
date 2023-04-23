<h1 align="center">AI-Imager</h1>
<p align="center">
<img align="center" width='80px' height='auto' src="https://github.com/Simatwa/ai-imager/raw/main/contents/static/image/favicon.svg" alt="Logo"/><br><br>
<a href="https://github.com/Simatwa/ai-imager"><img src="https://img.shields.io/static/v1?label=Github&message=passing&logo=github&color=green" alt="Github"/></a>
<a href="https://github.com/Simatwa/ai-imager/raw/main/LICENSE"><img src="https://img.shields.io/static/v1?label=License&message=GNU v3.0&logo=license&color=yellow" alt="License"/></a>
<a href="#"><img src="https://visitor-badge.glitch.me/badge?page_id=Simatwa.ai_imager&left_color=lime&right_color=red&left_text=Visitors" alt="visitors"></a>
<a href="#"><img src="https://img.shields.io/static/v1?label=Development&message=Beta&color=Orange&logo=progress" alt="Progress"/></a>
<a href="#"><img src="https://img.shields.io/static/v1?label=Code Style&message=Black&color=black&logo=Black" alt="Code-style"/></a>
<a href="#"><img src="https://img.shields.io/static/v1?label=Coverage&message=80%&color=green" alt="Coverage"/></a>
<a href="https://wakatime.com/badge/github/Simatwa/ai-imager"><img src="https://wakatime.com/badge/github/Simatwa/ai-imager.svg" alt="wakatime"></a>
</p>

## Features 

- Generate image from prompt
  - BingImageCreator
  - DALL-E (2)
- Edit image with a mask
- Generate variant of an image
- User-friendly web interface

## Prerequisites

1. [OPENAI-API-KEY](https://platform.openai.com/account/api-keys)
2. [Bing cookies](bing.com) - (*optional*)
3. [Python >=3.7](Python.org)

## Installation and usage

### Installation

If you have enough permissions you can clone from official repo:

```sh
git clone https://github.com/Simatwa/ai-imager.git
cd ai-imager
bash install.sh
```

If you're viewing this locally, you can install by executing the `install.sh` script.
 
 ```sh
bash install.sh
```

### Usage

Once installed, the site can be fired up as follows:

```sh
ai-imager -k $OPENAI_API_KEY
```

<details>

<summary>

Fire up efficiently - *recommended*

</summary>

- Make **KEY** an environment variable

```sh
export OPENAI_API_KEY=<Your-OPENAI-API-KEY>
```

- Fire up the server - `$ ai-imager`

- If yout want to use Bing's model, you have to parse the path to the cookie file during start up introduced by `-cf <path-to-cookie-file.json`.

- Review [how to get the cookie file.](https://github.com/acheong08/EdgeGPT#getting-authentication-require)

</details>

By default,  the server has the following configurations.

<table align="center">
    <tr>
        <th>Argument</th>
        <th>Default</th>
    </tr>
    <tr>
        <td>Port</td>
        <td>8000</td>
    </tr>
    <tr>
        <td>Logging-level</td>
        <td>20</td>
    </tr>
    <tr>
        <td>Host</td>
        <td>False</td>
    </tr>
    <tr>
        <td>Debug</td>
        <td>False</td>
    </tr>
</table>

<details>

<summary>

Run `$ ai-imager help` for more info.

</summary>

```

usage: ai-imager [-h] [-v] [-k KEY] [-kp PATH] [-l 10-50] [-o PATH]
                 [-cf COOKIE_FILE] [--host] [--thread] [--debug]
                 [port ...]

Manipulate images with OpenAI's model

positional arguments:
  port                  Port to start the server

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -k KEY, --key KEY     OpenAI's API key
  -kp PATH, --key-path PATH
                        Path to OpenAI-API-KEY path
  -l 10-50, --logging-level 10-50
                        Log level of the app
  -o PATH, --output PATH
                        Filepath to log to
  -cf COOKIE_FILE, --cookie-file COOKIE_FILE
                        Path to Bing's cookie file
  --host                Host the site on LAN
  --thread              Run server in multiple threads
  --debug               Start as debugging server

This script has no official relation with OpenAI.

```

</details>

> **Note** To *developers*, execute the [test.py](test.py) script to run server as you modify the contents.

## ToDo

- [x] Generate with BingImageCreator
- [ ] Download button 
- [ ] Chat feature
- [ ] Aunthenticate users

## Acknowledgements

- [x] [LawrenceKimutai](https://github.com/LawrenceKimutai)
<!--
### Contributors

This project exists thanks to all the people who contribute.

<a href="https://github.com/Simatwa/ai-imager/graphs/contributors">
<img src="https://contrib.rocks/image?repo=Simatwa/ai-imager" />
</a>
-->

## Disclaimer

This is not an official OpenAI product. This is a personal project and is not affiliated with OpenAI in any way. Don't sue me.