from playwright.sync_api import Page, expect


def test_edit_no_go_zone(page: Page):

    # ==========================================
    # Test Data
    # ==========================================

    original_room_name = "My Bedroom"
    updated_room_name = "Master Bedroom"
    floor_id = "F02"


    # ==========================================
    # 1. Robot Vacuum UI 접속
    # ==========================================

    page.goto("http://127.0.0.1:5000/")


    # ==========================================
    # 2 ~ 4. Room Name 입력 & Floor 선택 & Zone 생성
    # ==========================================

    page.locator("#zone-name").fill(original_room_name)
    page.locator("#floor-id").select_option(floor_id)
    page.locator("#create-zone").click()


    # ==========================================
    # 5. 생성된 Zone 확인
    # ==========================================

    zone = page.locator("#zone-list li").last
    zone.wait_for(state="visible")


    # ==========================================
    # 6. 수정 전 Zone 정보 검증 및 저장
    # ==========================================

    # expect를 활용해 속성이 제대로 적용되었는지 확인 후 값 읽기
    expect(zone).to_have_attribute("data-floor-id", floor_id)
    expect(zone).to_have_attribute("data-zone-name", original_room_name)

    original_zone_id = zone.get_attribute("data-zone-id")
    original_floor_id = zone.get_attribute("data-floor-id")
    original_zone_name = zone.get_attribute("data-zone-name")

    assert original_zone_id is not None


    # ==========================================
    # 7 ~ 8. Edit 버튼 클릭 + Prompt 값 입력
    # ==========================================

    edit_button = zone.locator("button", has_text="Edit")

    # Dialog(prompt) 발생 시 updated_room_name을 입력하도록 미리 수신기 등록
    def handle_dialog(dialog):
        assert dialog.type == "prompt"
        dialog.accept(updated_room_name)

    page.once("dialog", handle_dialog)
    edit_button.click()


    # ==========================================
    # 9 ~ 10. 수정 결과 자동 대기 및 검증 (핵심 수정 부분!)
    # ==========================================

    # [수정] wait_for_function 대신 expect 사용
    # data-zone-name 속성이 updated_room_name으로 바뀔 때까지 자동으로 기다림
    expect(zone).to_have_attribute("data-zone-name", updated_room_name)

    # 속성 값 가져오기
    updated_zone_name = zone.get_attribute("data-zone-name")
    updated_floor_id = zone.get_attribute("data-floor-id")
    updated_zone_id = zone.get_attribute("data-zone-id")

    # 핵심 검증: ID 유지 및 floor 정보 확인
    assert updated_floor_id == floor_id
    assert updated_zone_id == original_zone_id


    # ==========================================
    # 11. 화면 표시 내용 검증
    # ==========================================

    # inner_text에도 변경된 이름이 바뀔 때까지 자동 대기 검증
    expect(zone).to_contain_text(f"{floor_id} | {updated_room_name} | {original_zone_id}")


    # ==========================================
    # 12. 결과 출력
    # ==========================================

    print("\n==========================================")
    print("No-Go Zone 수정 결과")
    print("==========================================")
    print(f"Before : {original_floor_id} | {original_zone_name} | {original_zone_id}")
    print(f"After  : {updated_floor_id} | {updated_zone_name} | {updated_zone_id}")
    print("==========================================")