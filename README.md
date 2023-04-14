<h1 align="center">AI-Imager</h1>
<p align="center">
<a href="https://github.com/Simatwa/ai-imager"><img src="https://img.shields.io/static/v1?label=Github&message=passing&logo=github&color=green" alt="Github"/></a>
<a href="#"><img src="https://visitor-badge.glitch.me/badge?page_id=Simatwa.ai_imager&left_color=lime&right_color=red&left_text=Visitors" alt="visitors"></a>
<a href="#"><img src="https://img.shields.io/static/v1?label=Development&message=Beta&color=Orange&logo=progress" alt="Progress"/></a>
<a href="#"><img src="https://img.shields.io/static/v1?label=Code Style&message=Black&color=black&logo=Black" alt="Code-style"/></a>
<a href="#"><img src="https://img.shields.io/static/v1?label=Coverage&message=80%&color=green" alt="Coverage"/></a>
<a href="https://wakatime.com/badge/github/Simatwa/ai-imager"><img src="https://wakatime.com/badge/github/Simatwa/ai-imager.svg" alt="wakatime"></a><br>
<img align="center" src="https://github.com/Simatwa/ai-imager/raw/main/contents/static/image/favicon.svg" alt="Logo"/>
</p>

## Features 

- Generate image from prompt
  - EdgeGPT - *(Soon)*
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
bash install.sh
```

If you're viewing this locally, you can install by executing the `install.sh` script.
 
 ```sh
bash install.sh
```

### Usage

Once installed, the site can be fired up as follows:

```sh
ai-image -k {OPENAI_API_KEY}
```

<details>

<summary>

Fire up efficiently - *recommended*

</summary>

- Make **KEY** an environment variable
- Fire up the server - `ai-imager`

</details>

By default,  the server has the following configurations.

<table>
    <thead>Default configurations</thead>
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

## ToDo

- [x] Render urls in JS
- [x] Prettify display
- [ ] Aunthenticate users