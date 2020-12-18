# @Time    : 2020/12/17 21:07
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm
import yaml
from selenium import webdriver


class TestFuYong:

    def setup(self):
        pass

    def teardwon(self):
        pass

    # 复用浏览器
    def test_fuyong(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=chrome_arg)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        print("########")
        print(driver.get_cookies())

    # cookie 登录
    def test_cookie(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        # 添加cookie前，先打开页面，这样才能添加成功（因为域）
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = [
            {'domain': 'work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a1939055'},
            {'domain': 'work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851354173003'},
            {'domain': 'work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851354173003'},
            {'domain': 'work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': 'qq.com', 'httpOnly': False, 'name': 'skey', 'path': '/', 'secure': False,
                             'value': '@yFhKquIb3'},
            {'domain': 'qq.com', 'httpOnly': False, 'name': 'uin', 'path': '/', 'secure': False,
             'value': 'o0794422438'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1610803706.755928, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': 'qq.com', 'expiry': 1671283623, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.423811137.1608024763'},
            {'domain': 'work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '23267529712725738'},
            {'domain': 'work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': '4uXBwK6QfEYPk6K51Ohc1Yc56K373MzM8MrhP2JxrzJItvKKIzswtspZtR0RjCuW'},
            {'domain': 'qq.com', 'expiry': 1608298023, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.533288880.1608198327'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1608229858.937185, 'httpOnly': True, 'name': 'ww_rtkey',
             'path': '/', 'secure': False, 'value': '6jrf2k1'},
            {'domain': 'qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
             'secure': False, 'value': '794422438'},
            {'domain': 'work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_f2ba645ba13636ba52b0234381f51cbc',
             'path': '/', 'secure': False, 'value': '1608026108'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1639562108, 'httpOnly': False,
             'name': 'Hm_lvt_f2ba645ba13636ba52b0234381f51cbc', 'path': '/', 'secure': False,
             'value': '1608024763,1608026101'},
            {'domain': 'qq.com', 'httpOnly': False, 'name': 'qm_verifyimagesession', 'path': '/', 'secure': False,
             'value': 'h0110c41ae8df9c7b543812483898ce3f86d741fb9bc16a398a99076b7f3795670be31536ba16448db0'},
            {'domain': 'work.weixin.qq.com', 'httpOnly': False, 'name': '__utmc', 'path': '/', 'secure': False,
             'value': '135912439'},
            {'domain': 'qq.com', 'httpOnly': False, 'name': 'qm_authimgs_id', 'path': '/', 'secure': False,
             'value': '2'},
            {'domain': 'qq.com', 'expiry': 2147483645.578309, 'httpOnly': False, 'name': 'ptcz', 'path': '/',
             'secure': False, 'value': '27c808f0a5926b70af934732620081fdfde656d6ee86a4ff4e9a6bb0fd37da56'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1623794108, 'httpOnly': False, 'name': '__utmz', 'path': '/',
             'secure': False, 'value': '135912439.1608024763.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic'},
            {'domain': 'work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325035203432'},
            {'domain': 'qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '2608676632'},
            {'domain': 'qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '3432633344'},
            {'domain': 'qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False,
             'value': 'ssid=s5980526445'},
            {'domain': 'qq.com', 'httpOnly': False, 'name': 'pgv_si', 'path': '/', 'secure': False,
             'value': 's8045082624'},
            {'domain': 'work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': 'work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'T-I2RZh1FoXn5DZxLV2QzAZ7a-yKz2wJErufck3jEtJa0sZXzwRZUhiPg9sq6Z-7pJYZUqX1tpF0W7-IGlxD10AspyfjecjrxjyfSCr1ggzh90fMFJLCrhAnfw23GaZUVW1dQHcVg3Sv_7TvWz3gZ176zqZpFdyLq-8XEyN_CRRvo-pClVFzpMA_ofCL-_Brcc6gv5ivZ-QPiv770faXl5qSkJHrQhi2gfSfYXSHwzlp0_oe4wnFP0P_uhJR06LYqCYNoNIDHM4Vega1ZDroag'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1639747128, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
             'value': '1608198324,1608198396,1608210925'},
            {'domain': 'qq.com', 'expiry': 1917828745.085437, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '1_794422438'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1639734322.937259, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': 'work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1608211128'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1671098108, 'httpOnly': False, 'name': '__utma', 'path': '/',
             'secure': False, 'value': '135912439.423811137.1608024763.1608024763.1608024763.1'},
            {'domain': 'qq.com', 'expiry': 2147483638.2702, 'httpOnly': False, 'name': 'RK', 'path': '/',
             'secure': False, 'value': 'uQwVu6cXMI'}]

        # expiry 有时会报错，未能识别，所以使用前删掉
        for i in cookies:
            if "expiry" in i:
                del i["expiry"]
            driver.add_cookie(i)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")

    # 获取cookie，序列化后存入yaml文件内
    def test_cookies(self):
        chrome_opt = webdriver.ChromeOptions()
        chrome_opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=chrome_opt)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = driver.get_cookies()
        with open("cookies.yaml", mode="w") as f:
            yaml.dump(cookies, f)
