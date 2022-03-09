from selenium import webdriver
import time

E_MAIL = 'YOUR EMAIL'
PASSWORD = 'YOUR PASSWORD'

chrome_driver_path = 'chromedriver--path'
driver = webdriver.Chrome(executable_path=chrome_driver_path)


linkedin_url = 'https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=' \
               'London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0'
driver.get(linkedin_url)

''' Log - in '''

time.sleep(5)
sign_in = driver.find_element_by_class_name('cta-modal__primary-btn')
sign_in.click()

user = driver.find_element_by_id('username')
user.send_keys(E_MAIL)

password = driver.find_element_by_id('password')
password.send_keys(PASSWORD)

submit = driver.find_element_by_css_selector('.login__form_action_container button')
submit.click()

''' Applying for all jobs '''

time.sleep(5)
jobs = driver.find_elements_by_css_selector('.disabled.ember-view.job-card-container__link.job-card-list__title '
                                            '#ember749')
print(len(jobs))

for job in jobs:
    job.click()

''' Easy Apply '''
#
# time.sleep(3)
# company = driver.find_element_by_id('ember286')
# company.click()
#
# time.sleep(2)
# easy_apply = driver.find_element_by_id('ember397')
# easy_apply.click()
#
# time.sleep(2)
# phone_number = driver.find_element_by_id('urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2432102199,'
#                                          '20868410,phoneNumber~nationalNumber)')
# phone_number.send_keys('22222222')
#
# time.sleep(1)
# step1 = driver.find_element_by_id('ember404')
# step1.click()
#
# time.sleep(1)
# step2 = driver.find_element_by_id('ember404')
# step2.click()
#
# work_exp1 = driver.find_element_by_id('urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:'
#                                       '2432102199,20868402,numeric)')
# work_exp1.send_keys('0')
#
# work_exp2 = driver.find_element_by_id('urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2432102199'
#                                       ',20868386,numeric)')
# work_exp2.send_keys('0')
#
# review = driver.find_element_by_id('ember431')
# review.click()
#
# cancel = driver.find_element_by_id('ember400')
# cancel.click()
#
# confirm_cancel = driver.find_element_by_id('ember449')
# confirm_cancel.click()
