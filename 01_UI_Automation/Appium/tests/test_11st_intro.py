from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait


def test_11st_intro_close():

    # ==========================================
    # Test Data
    # ==========================================

    package_name = "com.elevenst"
    activity_name = ".intro.Intro"


    # ==========================================
    # Android Device Capabilities
    # ==========================================

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "R3CX40L2SV"
    options.app_package = package_name
    options.app_activity = activity_name


    # ==========================================
    # 1. Appium Server 연결
    # ==========================================

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )


    try:

        # ==========================================
        # 2. Intro 화면의 닫기 버튼 대기
        # ==========================================

        wait = WebDriverWait(
            driver,
            20
        )

        close_button = wait.until(
            lambda d: d.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                "닫기"
            )
        )


        # ==========================================
        # 3. 닫기 버튼 확인
        # ==========================================

        assert close_button.is_displayed()


        # ==========================================
        # 4. Intro 팝업 닫기
        # ==========================================

        close_button.click()


        # ==========================================
        # 5. 결과 출력
        # ==========================================

        print()
        print("==========================================")
        print("11st Intro Close Test")
        print("==========================================")
        print("Intro Close Button : PASS")
        print("Intro Close        : PASS")
        print("==========================================")


    finally:

        # ==========================================
        # 6. Appium Session 종료
        # ==========================================

        driver.quit()
        
        