import requests
import os
import random
import time


try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Origin": "https://act.hoyolab.com",
        "Referer":"https://act.hoyolab.com/",
    }

    # testing的时候不用等,自动晚上触发就需要等

    # 如果触发不到github,比如本地电脑没有github, 找不到eventname的话,会用"manual"来代替
    event_name = os.getenv("EVENT_NAME", "手动")

    if event_name == "schedule":
        print("等待随机时间,防止被当人机")
        wait_time = random.randint(0, 3600)  # 0 到 1小时之间随机数
        print(f"决定等个{wait_time//60}分钟后再签到.")
        time.sleep(wait_time)
    elif event_name == "workflow_dispatch" or event_name == "手动":
        print("手动触发签到,不等待.")
    else:
        print("收到了其他event_name,有点问题!")


    try:
        response = requests.post(url, headers=headers, json={"act_id": act_id})
        result = response.json()

        retcode = result.get("retcode")
        message = result.get("message")

        if retcode == 0:
            print(f"签到了 \(@^0^@)/ ({message})")
        elif retcode == -5003:
            print(f"{message}")
        else:
            print(f"签到失败: 状态码 {retcode}, 信息: {message}")
    except Exception as e:
        print(f"代码运行出错: {e}")   

if __name__ == "__main__":
    sign_in()