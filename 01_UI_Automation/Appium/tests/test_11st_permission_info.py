from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait


def test_11st_permission_info():

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
        # 2. 11번가 권한 안내 팝업의 확인 버튼 대기
        # ==========================================

        wait = WebDriverWait(
            driver,
            20
        )

        confirm_button = wait.until(
            lambda d: d.find_element(
                AppiumBy.ID,
                "com.elevenst:id/popup_close"
            )
        )


        # ==========================================
        # 3. 확인 버튼 표시 확인
        # ==========================================

        assert confirm_button.is_displayed()


        # ==========================================
        # 4. 확인 버튼 클릭
        # ==========================================

        confirm_button.click()


        # ==========================================
        # 5. 결과 출력
        # ==========================================

        print()
        print("==========================================")
        print("11st Permission Info Test")
        print("==========================================")
        print("Permission Info Popup : PASS")
        print("Confirm Button        : PASS")
        print("==========================================")


    finally:

        # ==========================================
        # 6. Appium Session 종료
        # ==========================================

        driver.quit()
        
        