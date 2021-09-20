# discord-account-generator
An hcaptcha-solving discord account generator; capable of randomizing **names**, **profile pictures**, and **verifying phone numbers**.

## Usage
In order to use dware, you need both rotating http proxies [iproyal reccomended](https://dashboard.iproyal.com/products/royal-residential-proxies) for evading discord's automated bot detection and an [onlinesim](https://onlinesim.io/) account, loaded with at least $2 in credits for verifying phone numbers. You can add these to your bot config by editing the config.json file with the following
```json
{
    "rotating_proxy": "your proxy",
    "threads": 100,
    "invite": "your discord invite",
    "onlinesim_key": "your onlinesim token"
}
```
