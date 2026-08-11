from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait


def test_11st_notification_permission():

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
        # 2. Android 알림 권한 팝업 확인
        # ==========================================

        wait = WebDriverWait(
            driver,
            20
        )

        permission_message = wait.until(
            lambda d: d.find_element(
                AppiumBy.ID,
                "com.android.permissioncontroller:id/permission_message"
            )
        )

        assert permission_message.is_displayed()


        # ==========================================
        # 3. "허용 안함" 버튼 확인
        # ==========================================

        deny_button = wait.until(
            lambda d: d.find_element(
                AppiumBy.ID,
                "com.android.permissioncontroller:id/permission_deny_button"
            )
        )

        assert deny_button.is_displayed()


        # ==========================================
        # 4. 알림 권한 거부
        # ==========================================

        deny_button.click()


        # ==========================================
        # 5. 권한 팝업 종료 확인
        # ==========================================

        wait.until(
            lambda d: not d.find_elements(
                AppiumBy.ID,
                "com.android.permissioncontroller:id/permission_deny_button"
            )
        )


        # ==========================================
        # 6. 결과 출력
        # ==========================================

        print()
        print("==========================================")
        print("11st Notification Permission Test")
        print("==========================================")
        print("Permission Popup : PASS")
        print("Deny Button      : PASS")
        print("Permission Deny  : PASS")
        print("==========================================")


    finally:

        # ==========================================
        # 7. Appium Session 종료
        # ==========================================

        driver.quit()
        
        