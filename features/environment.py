from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application

# Change the browser value to "chrome" or "firefox" or "headless" to execute in that environment
#browser = "Chrome"

browser_names = ('chrome', 'firefox', 'headless')


def browser_init(context):  #scenario_name): - required for browserstack
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

   ###FIREFOX  BROWSER Support###
   # service = Service(executable_path="/Users/raman/Documents/Careerist/QA/python_pop_automation/geckodriver")
   #  driver_path = GeckoDriverManager().install()
   #  service = Service(driver_path)
   #  context.driver = webdriver.Firefox(service=service)

    ### SAFARI  BROWSER Support ###
   #  context.driver = webdriver.Safari()

    ###HEADLESS BROWSER SUPPORT###
    # options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ###BrOWSERSTACK -runing testcases on cloud###
    # https://www.browserstack.com/automate/capabilities
    # bs_user = "reaper_9yL8gs"
    # bs_key = "4prCBjhpVgCu9rJdiJMt"
    # url = f"https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub"

    #options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '10',
    #     'browserName': 'Firefox',
    #     'sessionName': scenario_name
    # }
    # bstack_options = {
    #     "os": "OS X",
    #     "osVersion": "Ventura",
    #     "browserName": "Chrome",
    #     'sessionName': scenario_name
    # }
    #
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)
    #
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
