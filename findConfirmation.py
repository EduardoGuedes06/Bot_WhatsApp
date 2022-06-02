import sendMessage
import time
import re
def findConfirmation(driver):
    link = "https://web.whatsapp.com/send?phone=%s&text=%s" %(5511947844341,'')
    driver.get(link)
    x = 1
    messages = []
    while(x == 1):
        time.sleep(10)
        try:
            chatbox = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/div[3]/div/div')
            msgs = chatbox.find_elements_by_xpath(".//div[@class = 'copyable-text']")
            time.sleep(10)    
            for msg in msgs:
                messages.append([msg.get_attribute('data-pre-plain-text'),msg.text])
            x = 0
        except:
            pass
    for msg in messages:
        print(msg)   
driver = sendMessage.initialize()
findConfirmation(driver)

