import requests
import os
from dotenv import load_dotenv

load_dotenv()

def sign_in():
    my_cookie = os.environ.get("HOYOLAB_COOKIE")

    if not my_cookie:
        print("找不到cookie!")
        return

    act_id = "e202102251931481"
    url = f"https://sg-hk4e-api.hoyolab.com/event/sol/sign?lang=zh-cn&act_id={act_id}"

    headers = {
        "Cookie":my_cookie,
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0..0 Safari/537.36",
        "Origin": "https://act.hoyolab.com",
        "Referer":"https://act.hoyolab.com/",
    }

    print("正在发送签到请求~")

    try:
        response = requests.post(url, headers=headers, json={"act_id": act_id})
        result = response.json()

        retcode = result.get("retcode")
        message = result.get("message")

        if retcode == 0:
            print(f"签到了 \(@v@)/ ({message})")
        elif retcode == -5003:
            print(f"{message} (今天已经签过了)")
        else:
            print(f"签到失败: 状态码 {retcode}, 信息: {message}")
    except Exception as e:
        print(f"代码运行出错: {e}")   

if __name__ == "__main__":
    sign_in()