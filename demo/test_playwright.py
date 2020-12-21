from time import sleep

from playwright import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    # Go to https://ipayfront.cloudwalk.cn/agent/#/
    page.goto("https://ipayfront.cloudwalk.cn/agent/#/")

    # Click input[placeholder="请输入帐户名"]
    page.click("input[placeholder=\"请输入帐户名\"]")

    # Fill input[placeholder="请输入帐户名"]
    page.fill("input[placeholder=\"请输入帐户名\"]", "S2943256")

    # Click input[placeholder="请输入密码"]
    page.click("input[placeholder=\"请输入密码\"]")

    # Fill input[placeholder="请输入密码"]
    page.fill("input[placeholder=\"请输入密码\"]", "yckj3256")

    # Click //button[normalize-space(.)='确 定']
    page.click("//button[normalize-space(.)='确 定']")

    # Go to https://ipayfront.cloudwalk.cn/agent/#/dashboard/analysis
    page.goto("https://ipayfront.cloudwalk.cn/agent/#/dashboard/analysis")

    # Click //div[normalize-space(.)='下级代理商管理']
    page.click("//div[normalize-space(.)='下级代理商管理']")

    # Click //a[normalize-space(.)='代理商管理']
    page.click("//a[normalize-space(.)='代理商管理']")
    # assert page.url == "https://ipayfront.cloudwalk.cn/agent/#/agent/sub/list"

    # Click //button[normalize-space(.)='新代理商']
    page.click("//button[normalize-space(.)='新代理商']")
    # assert page.url == "https://ipayfront.cloudwalk.cn/agent/#/agent/info/add"

    # Click text="请选择代理商类型"
    page.click("text=\"请选择代理商类型\"")

    # Click //li[normalize-space(.)='个人代理商' and normalize-space(@role)='option']
    page.click("//li[normalize-space(.)='个人代理商' and normalize-space(@role)='option']")

    # Click input[placeholder="请输入代理商名称"]
    page.click("input[placeholder=\"请输入代理商名称\"]")

    # Fill input[placeholder="请输入代理商名称"]
    page.fill("input[placeholder=\"请输入代理商名称\"]", "playwright")

    # Fill input[placeholder="请输入负责人姓名"]
    page.fill("input[placeholder=\"请输入负责人姓名\"]", "playwright")

    # Fill input[placeholder="请输入负责人手机号"]
    page.fill("input[placeholder=\"请输入负责人手机号\"]", "13300011111")

    # Fill input[placeholder="请输入开户账号"]
    page.fill("input[placeholder=\"请输入开户账号\"]", "6226090218441299")

    # Fill input[placeholder="请输入开户名称"]
    page.fill("input[placeholder=\"请输入开户名称\"]", "playwright")

    # Fill input[placeholder="请输入开户人手机号码"]
    page.fill("input[placeholder=\"请输入开户人手机号码\"]", "13300011111")

    # Fill input[placeholder="请输入证件号码"]
    page.fill("input[placeholder=\"请输入证件号码\"]", "131102199004132019")

    # Fill input[placeholder="须高于您的成本价"]
    page.fill("input[placeholder=\"须高于您的成本价\"]", "4")

    # Fill //div[2]/div/div[2]/div/span/div[normalize-space(.)='‰']/input[normalize-space(@placeholder)='须高于您的成本价' and normalize-space(@type)='number']
    page.fill("//div[2]/div/div[2]/div/span/div[normalize-space(.)='‰']/input[normalize-space(@placeholder)='须高于您的成本价' and normalize-space(@type)='number']", "6")

    # Fill input[placeholder="须高于您的成本价"]
    page.fill("input[placeholder=\"须高于您的成本价\"]", "6")

    # Fill (//div[1]/div[1]/div/div[2]/div/span/div[normalize-space(.)='‰']/input[normalize-space(@placeholder)='须高于您的成本价' and normalize-space(@type)='number'])[3]
    page.fill("(//div[1]/div[1]/div/div[2]/div/span/div[normalize-space(.)='‰']/input[normalize-space(@placeholder)='须高于您的成本价' and normalize-space(@type)='number'])[3]", "5")

    # Fill (//div[1]/div[2]/div/div[2]/div/span/div[normalize-space(.)='‰']/input[normalize-space(@placeholder)='须高于您的成本价' and normalize-space(@type)='number'])[3]
    page.fill("(//div[1]/div[2]/div/div[2]/div/span/div[normalize-space(.)='‰']/input[normalize-space(@placeholder)='须高于您的成本价' and normalize-space(@type)='number'])[3]", "6")

    # Fill (//div[1]/div[1]/div/div[2]/div/span/div[normalize-space(.)='‰']/input[normalize-space(@placeholder)='须高于您的成本价' and normalize-space(@type)='number'])[4]
    page.fill("(//div[1]/div[1]/div/div[2]/div/span/div[normalize-space(.)='‰']/input[normalize-space(@placeholder)='须高于您的成本价' and normalize-space(@type)='number'])[4]", "5")

    # Fill (//div[1]/div[2]/div/div[2]/div/span/div[normalize-space(.)='‰']/input[normalize-space(@placeholder)='须高于您的成本价' and normalize-space(@type)='number'])[4]
    page.fill("(//div[1]/div[2]/div/div[2]/div/span/div[normalize-space(.)='‰']/input[normalize-space(@placeholder)='须高于您的成本价' and normalize-space(@type)='number'])[4]", "6")

    sleep(100)
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)