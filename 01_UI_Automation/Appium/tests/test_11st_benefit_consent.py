from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait


def test_11st_benefit_consent():

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
        # 2. 혜택 알림 동의 팝업 확인
        # ==========================================

        wait = WebDriverWait(
            driver,
            20
        )

        consent_button = wait.until(
            lambda d: d.find_element(
                AppiumBy.ID,
                "com.elevenst:id/ok"
            )
        )


        # ==========================================
        # 3. 동의 버튼 표시 확인
        # ==========================================

        assert consent_button.is_displayed()


        # ==========================================
        # 4. 동의 버튼 클릭
        # ==========================================

        consent_button.click()


        # ==========================================
        # 5. 동의 버튼 사라짐 확인
        # ==========================================

        wait.until(
            lambda d: not d.find_elements(
                AppiumBy.ID,
                "com.elevenst:id/ok"
            )
        )


        # ==========================================
        # 6. 결과 출력
        # ==========================================

        print()
        print("==========================================")
        print("11st Benefit Consent Test")
        print("==========================================")
        print("Benefit Consent Popup : PASS")
        print("Consent Button        : PASS")
        print("Consent Completed     : PASS")
        print("==========================================")


    finally:

        # ==========================================
        # 7. Appium Session 종료
        # ==========================================

        driver.quit()
        
        