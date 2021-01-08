# @Time    : 2021/1/8 12:02
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm

def black_wrapper(func):
    def run(*args):
        print("args:",args)
        base_page = args[0]  # 获取self
        try:
            return func(*args)
        except Exception as e:
            for black in base_page.black_list:
                eles = base_page.driver.find_elements(*black)
                # 黑名单被找到
                if len(eles) > 0:
                    # 对黑名单元素进行点击，可以自由扩展
                    eles[0].click()
                    return func(*args)
            raise e

    return run