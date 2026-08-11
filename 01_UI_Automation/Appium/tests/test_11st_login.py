import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait


def test_11st_login():

    # ==========================================
    # Test Data
    # ==========================================

    package_name = "com.elevenst"
    activity_name = ".intro.Intro"

    # 테스트용 계정
    # 실제 테스트할 계정으로 변경하세요.
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
        print("11st Login Test")
        print("==========================================")


        # ==========================================
        # 1. Main 화면 진입 대기
        # ==========================================

        time.sleep(10)

        print("App Launch : PASS")


        # ==========================================
        # 2. 하단 '나의11번가' 선택
        # ==========================================

        my_11st = wait.until(
            lambda d: d.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                "나의11번가"
            )
        )

        assert my_11st.is_displayed()

        my_11st.click()

        print("나의11번가 : CLICKED")


        # ==========================================
        # 3. 로그인 UI 선택
        # ==========================================

        login_button = wait.until(
            lambda d: d.find_element(
                AppiumBy.XPATH,
                "//*[@content-desc='로그인' or @text='로그인']"
            )
        )

        assert login_button.is_displayed()

        login_button.click()

        print("Login UI : CLICKED")


        # ==========================================
        # 4. 로그인 화면 확인
        # ==========================================

        login_screen = wait.until(
            lambda d: d.find_element(
                AppiumBy.XPATH,
                "//*[contains(@text, '로그인') or contains(@content-desc, '로그인')]"
            )
        )

        assert login_screen.is_displayed()

        print("Login Screen : DISPLAYED")


        # ==========================================
        # 5. ID 입력창 찾기
        # ==========================================

        edit_texts = wait.until(
            lambda d: d.find_elements(
                AppiumBy.CLASS_NAME,
                "android.widget.EditText"
            )
        )

        assert len(edit_texts) >= 2

        id_field = edit_texts[0]
        password_field = edit_texts[1]


        # ==========================================
        # 6. ID 입력
        # ==========================================

        id_field.click()
        id_field.send_keys(test_id)

        print("ID Input : PASS")


        # ==========================================
        # 7. Password 입력
        # ==========================================

        password_field.click()
        password_field.send_keys(test_password)

        print("Password Input : PASS")


        # ==========================================
        # 8. 입력값 확인
        # ==========================================

        assert id_field.text == test_id

        print("Login Input Validation : PASS")


        # ==========================================
        # 최종 결과
        # ==========================================

        print()
        print("==========================================")
        print("11st Login Test Result")
        print("==========================================")
        print("App Launch             : PASS")
        print("나의11번가             : PASS")
        print("Login UI               : PASS")
        print("Login Screen           : PASS")
        print("ID Input               : PASS")
        print("Password Input         : PASS")
        print("==========================================")


    finally:

        driver.quit()
        
        