<h1 align="center">AI-Imager</h1>
<p align="center">
<a href="https://github.com/Simatwa/ai-imager"><img src="https://img.shields.io/static/v1?label=Github&message=passing&logo=github&color=green" alt="Github"/></a>
<a href="https://github.com/Simatwa/ai-imager/raw/main/LICENSE"><img src="https://img.shields.io/static/v1?label=License&message=GNU v3.0&logo=license&color=yellow" alt="License"/></a>
<a href="#"><img src="https://visitor-badge.glitch.me/badge?page_id=Simatwa.ai_imager&left_color=lime&right_color=red&left_text=Visitors" alt="visitors"></a>
<a href="#"><img src="https://img.shields.io/static/v1?label=Development&message=Beta&color=Orange&logo=progress" alt="Progress"/></a>
<a href="#"><img src="https://img.shields.io/static/v1?label=Code Style&message=Black&color=black&logo=Black" alt="Code-style"/></a>
<a href="#"><img src="https://img.shields.io/static/v1?label=Coverage&message=80%&color=green" alt="Coverage"/></a>
<a href="https://wakatime.com/badge/github/Simatwa/ai-imager"><img src="https://wakatime.com/badge/github/Simatwa/ai-imager.svg" alt="wakatime"></a><br>
<img align="center" width='80px' height='auto' src="https://github.com/Simatwa/ai-imager/raw/main/contents/static/image/favicon.svg" alt="Logo"/>
</p>

## Features 

- Generate image from prompt
  - EdgeGPT
  - ChatGPT
- Edit image with a mask
- Generate variant of an image

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

usage: ai-imager [-h] [-v] [-k KEY] [-kp KEY_PATH] [-l 10-50] [-o OUTPUT]
                 [--host] [--debug]
                 [port ...]

Manipulate images with OpenAI's model

positional arguments:
  port                  Port to start the server

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -k KEY, --key KEY     OpenAI's API key
  -kp KEY_PATH, --key-path KEY_PATH
                        Path to OpenAI-API-KEY path
  -l 10-50, --logging-level 10-50
                        Log level of the app
  -o OUTPUT, --output OUTPUT
                        Filepath to log to
  --host                Host the site on LAN
  --debug               Start as debugging server

```

</details>

> **Note** To *developers*, execute the [test.py](test.py) script to run server as you modify the contents.

## ToDo

- [x] Render urls in JS
- [x] Prettify display
- [ ] Aunthenticate users
- [x] Generate with EdgeGPT
- [ ] Chat feature

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

> **Tips** - Incase you're stack while using the script, don't hesitate to hit the developer's inbox 📥.

## Developer Contacts

<p align='center'>
<a href="https://facebook.com/beny.carl.3"><img alt="Facebook" src="https://img.shields.io/static/v1?logo=facebook&message=Inbox&color=blue&label=Facebook"/></a>
<a href="https://twitter.com/Smartwa_Caleb"><img alt="Twitter" src="https://img.shields.io/static/v1?logo=twitter&message=DM&color=cyan&label=Twitter"/></a>
<a href="http://instagram.com/smartwa_caleb"><img alt="instagram" src="https://img.shields.io/static/v1?logo=instagram&message=DM&color=pink&label=Instagram"/>
<a href="https://wa.me/254774304553?text=Hi *Smartwa*, I need help with *ai-imager* script ..."><img alt='Whatsapp' src="https://img.shields.io/static/v1?logo=whatsapp&message=Inbox&color=green&label=WhatsApp"/></a>