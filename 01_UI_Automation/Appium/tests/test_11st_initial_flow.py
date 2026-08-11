import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait


def test_11st_initial_flow():

    # ==========================================
    # Test Data
    # ==========================================

    package_name = "com.elevenst"
    activity_name = ".intro.Intro"

    # 테스트용 계정
    # 실제 계정으로 변경하세요.
    test_id = "YOUR_TEST_ID"
    test_password = "YOUR_TEST_PASSWORD"


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
    # Appium Server 연결
    # ==========================================

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    wait = WebDriverWait(driver, 20)


    try:

        print()
        print("==========================================")
        print("11st Initial Flow Test")
        print("==========================================")


        # ==========================================
        # 1. App 실행
        # ==========================================

        time.sleep(10)

        print("App Launch : PASS")


        # ==========================================
        # 2. Intro 화면 확인 및 닫기
        # ==========================================

        intro_close_buttons = driver.find_elements(
            AppiumBy.ACCESSIBILITY_ID,
            "닫기"
        )

        if intro_close_buttons:

            intro_close_button = intro_close_buttons[0]

            if intro_close_button.is_displayed():

                intro_close_button.click()

                print("Intro Close : PASS")

        else:

            print("Intro Screen : SKIP")


        # ==========================================
        # 3. Android Notification Permission
        # ==========================================

        try:

            deny_button = WebDriverWait(
                driver,
                10
            ).until(
                lambda d: d.find_element(
                    AppiumBy.ID,
                    "com.android.permissioncontroller:id/permission_deny_button"
                )
            )

            if deny_button.is_displayed():

                deny_button.click()

                print("Notification Permission : DENY")

        except Exception:

            print("Notification Permission : SKIP")


        # ==========================================
        # 4. 11st Permission Info Popup
        # ==========================================

        try:

            permission_info_confirm = WebDriverWait(
                driver,
                10
            ).until(
                lambda d: d.find_element(
                    AppiumBy.ID,
                    "com.elevenst:id/popup_close"
                )
            )

            if permission_info_confirm.is_displayed():

                permission_info_confirm.click()

                print("Permission Info : CONFIRMED")

        except Exception:

            print("Permission Info : SKIP")


        # ==========================================
        # 5. Benefit Notification Consent
        # ==========================================

        try:

            benefit_deny_button = WebDriverWait(
                driver,
                10
            ).until(
                lambda d: d.find_element(
                    AppiumBy.ID,
                    "com.elevenst:id/cancel"
                )
            )

            if benefit_deny_button.is_displayed():

                benefit_deny_button.click()

                print("Benefit Notification : DENY")

        except Exception:

            print("Benefit Notification : SKIP")


        # ==========================================
        # 6. Notification Service Info
        # ==========================================

        try:

            notification_service_title = WebDriverWait(
                driver,
                10
            ).until(
                lambda d: d.find_element(
                    AppiumBy.ID,
                    "com.elevenst:id/title"
                )
            )

            if notification_service_title.is_displayed():

                print("Notification Service Info : DISPLAYED")


            notification_service_confirm = WebDriverWait(
                driver,
                10
            ).until(
                lambda d: d.find_element(
                    AppiumBy.ID,
                    "com.elevenst:id/ok"
                )
            )

            if notification_service_confirm.is_displayed():

                notification_service_confirm.click()

                print("Notification Service Info : CONFIRMED")

        except Exception:

            print("Notification Service Info : SKIP")


        # ==========================================
        # 7. 혜택 안내 팝업
        #
        # 팝업 제목:
        # "11번가 앱 전용 혜택 안내"
        #
        # 여기서는 팝업이 나오면
        # "혜택 받으러가기" 버튼을 선택
        # ==========================================

        print()
        print("Benefit Guide Popup : CHECK")

        try:

            benefit_go_button = WebDriverWait(
                driver,
                5
            ).until(
                lambda d: d.find_element(
                    AppiumBy.XPATH,
                    "//*[contains(@text,'혜택 받으러가기') "
                    "or contains(@content-desc,'혜택 받으러가기')]"
                )
            )

            if benefit_go_button.is_displayed():

                print("Benefit Guide Popup : DISPLAYED")

                benefit_go_button.click()

                print("Benefit Guide : CLICKED")

                # 혜택 페이지 이동 대기
                time.sleep(3)

        except Exception:

            print("Benefit Guide Popup : NOT DISPLAYED / SKIP")


        # ==========================================
        # 8. Main 화면 대기
        # ==========================================

        print()
        print("Main Screen : CHECK")

        try:

            WebDriverWait(
                driver,
                10
            ).until(
                lambda d: d.find_element(
                    AppiumBy.ACCESSIBILITY_ID,
                    "나의11번가"
                )
            )

            print("Main Screen : DETECTED")

        except Exception:

            print("Main Screen : NOT DETECTED")

            raise


        # ==========================================
        # 9. 하단 '나의11번가' 선택
        #
        # 실제 XML 확인:
        #
        # content-desc="나의11번가"
        # clickable="true"
        #
        # 따라서 ACCESSIBILITY_ID 사용
        # ==========================================

        my_11st = WebDriverWait(
            driver,
            10
        ).until(
            lambda d: d.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                "나의11번가"
            )
        )

        assert my_11st.is_displayed()

        my_11st.click()

        print("나의11번가 : CLICKED")


        # ==========================================
        # 10. 로그인 UI 찾기
        # ==========================================

        login_button = WebDriverWait(
            driver,
            10
        ).until(
            lambda d: d.find_element(
                AppiumBy.XPATH,
                "//*[@content-desc='로그인' or @text='로그인']"
            )
        )

        assert login_button.is_displayed()

        login_button.click()

        print("Login UI : CLICKED")


        # ==========================================
        # 11. 로그인 화면 확인
        # ==========================================

        login_screen = WebDriverWait(
            driver,
            10
        ).until(
            lambda d: d.find_element(
                AppiumBy.XPATH,
                "//*[contains(@text,'로그인') "
                "or contains(@content-desc,'로그인')]"
            )
        )

        assert login_screen.is_displayed()

        print("Login Screen : DISPLAYED")


        # ==========================================
        # 12. ID / Password 입력창 찾기
        # ==========================================

        edit_texts = WebDriverWait(
            driver,
            10
        ).until(
            lambda d: d.find_elements(
                AppiumBy.CLASS_NAME,
                "android.widget.EditText"
            )
        )

        assert len(edit_texts) >= 2

        id_field = edit_texts[0]
        password_field = edit_texts[1]


        # ==========================================
        # 13. ID 입력
        # ==========================================

        id_field.click()

        id_field.send_keys(test_id)

        print("ID Input : PASS")


        # ==========================================
        # 14. Password 입력
        # ==========================================

        password_field.click()

        password_field.send_keys(test_password)

        print("Password Input : PASS")


        # ==========================================
        # 15. 입력 화면 확인
        #
        # 실제로 입력된 화면을 사용자가 볼 수 있도록
        # 5초 동안 대기
        # ==========================================

        print()
        print("==========================================")
        print("Login Input Completed")
        print("ID / Password 입력 화면을 5초간 유지합니다.")
        print("==========================================")

        time.sleep(5)


        # ==========================================
        # 16. 최종 결과
        # ==========================================

        print()
        print("==========================================")
        print("11st Initial Flow Result")
        print("==========================================")

        print("App Launch              : PASS")
        print("Intro                   : PASS / SKIP")
        print("Notification Permission : PASS / SKIP")
        print("Permission Info         : PASS / SKIP")
        print("Benefit Notification    : PASS / SKIP")
        print("Notification Service    : PASS / SKIP")
        print("Benefit Guide Popup     : PASS / SKIP")
        print("Main Screen             : PASS")
        print("나의11번가              : PASS")
        print("Login UI                : PASS")
        print("Login Screen            : PASS")
        print("ID Input                : PASS")
        print("Password Input          : PASS")
        print("==========================================")


    finally:

        # ==========================================
        # Appium Session 종료
        # ==========================================

        driver.quit()
        