from violent_webdriver import Chrome

# the value of executable_path should be your own path
dr = Chrome.violent_chromedriver(executable_path='C://MyDownloads/Download/chrome-win32/chromedriver.exe')
dr.get('https://www.baidu.com')
dr.v_send_keys(locate_rule=[['name', 'wd']], message='test')
dr.v_click(locate_rule=[['id', 'su']])
