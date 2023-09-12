# pip install captcha-crack


from captcha_crack import vtop

# initialise the load object
load = vtop.Load()
# you can use the relative path too
captchaPath = '/Users/svetlanachigai/Python /web_scraping/kaptcha2.jpeg'
# the fucntion get_captcha_text(captchaPath) will return the text of the captcha
captchaText = load.get_captcha_text(captchaPath)

print(captchaText)