[![discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com)
[![github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AcierP)
[![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)

# Discord Account Generator
An hcaptcha-solving discord account generator; capable of randomizing **names**, **profile pictures**, and ~~**verifying phone numbers**~~.

## Usage

```bash
$ pip install -r requirements.txt
```
In order to use dware, you need both rotating http proxies [iproyal reccomended](https://dashboard.iproyal.com/products/royal-residential-proxies) for evading discord's automated bot detection and an [onlinesim](https://onlinesim.io/) account, loaded with at least $2 in credits for verifying phone numbers. You can add these to your bot config by editing the config.json file with the following

```json

{
    "rotating_proxy": "Your proxy.",
    "threads": 100,
    "invite": "Your Discord invite"
}
```
