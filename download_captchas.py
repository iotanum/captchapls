import requests
import io

from PIL import Image


# we're starting from this random number :)
start = 1696080000

# we're downloading this many captchas
to_download = 1100

# link to the captcha
link = "https://game.granbluefantasy.jp/c/i?t="

# directory to save the captchas
directory = "dataset/"

if __name__ == '__main__':
    for i in range(to_download):
        save_path = f"{directory}/{i}.png"
        c_captcha = start + 1
        captcha_link = f"{link}{c_captcha}"
        req = requests.get(captcha_link)
        img = Image.open(io.BytesIO(req.content))
        img.save(save_path)
        print(f"Saved '{save_path}'")
