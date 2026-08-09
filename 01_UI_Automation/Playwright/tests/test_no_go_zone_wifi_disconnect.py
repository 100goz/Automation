import requests

from playwright.sync_api import Page, expect


def test_no_go_zone_wifi_disconnect(page: Page):

    # ==========================================
    # Test Data
    # ==========================================

    room_name = "My Bedroom"
    floor_id = "F02"


    # ==========================================
    # 1. Robot Vacuum UI 접속
    # ==========================================

    page.goto(
        "http://127.0.0.1:5000/"
    )


    # ==========================================
    # 2. Room Name 입력
    # ==========================================

    page.locator(
        "#zone-name"
    ).fill(room_name)


    # ==========================================
    # 3. Floor 선택
    # ==========================================

    page.locator(
        "#floor-id"
    ).select_option(floor_id)


    # ==========================================
    # 4. Wi-Fi 연결 끊기
    # ==========================================

    page.context.set_offline(True)

    print()
    print("Wi-Fi Status : OFFLINE")


    # ==========================================
    # 5. No-Go Zone 저장 시도
    # ==========================================

    page.locator(
        "#create-zone"
    ).click()


    # ==========================================
    # 6. 연결 끊김 상태에서 Zone 생성 실패 확인
    # ==========================================

    zone_list = page.locator(
        "#zone-list li"
    )

    expect(zone_list).to_have_count(0)

    print(
        "Save Result  : Failed while offline"
    )


    # ==========================================
    # 7. Wi-Fi 연결 복구
    # ==========================================

    page.context.set_offline(False)

    print(
        "Wi-Fi Status : ONLINE"
    )


    # ==========================================
    # 8. No-Go Zone 다시 저장
    # ==========================================

    page.locator(
        "#create-zone"
    ).click()


    # ==========================================
    # 9. 저장된 Zone 확인
    # ==========================================

    zone = page.locator(
        "#zone-list li"
    ).last

    zone.wait_for(
        state="visible"
    )


    # ==========================================
    # 10. UI 데이터 검증
    # ==========================================

    expect(zone).to_have_attribute(
        "data-floor-id",
        floor_id
    )

    expect(zone).to_have_attribute(
        "data-zone-name",
        room_name
    )


    zone_id = zone.get_attribute(
        "data-zone-id"
    )

    assert zone_id is not None


    # ==========================================
    # 11. Server API 데이터 확인
    # ==========================================

    response = requests.get(
        "http://127.0.0.1:5000/api/zones"
    )

    assert response.status_code == 200


    zones = response.json()


    # ==========================================
    # 12. Server에 Zone 정상 저장 확인
    # ==========================================

    saved_zone = next(
        (
            zone
            for zone in zones
            if zone["zone_id"] == zone_id
        ),
        None
    )


    assert saved_zone is not None

    assert saved_zone["floor_id"] == floor_id

    assert saved_zone["name"] == room_name


    # ==========================================
    # 13. 결과 출력
    # ==========================================

    print()

    print(
        "=========================================="
    )

    print(
        "No-Go Zone Wi-Fi Disconnect Test"
    )

    print(
        "=========================================="
    )

    print(
        f"Zone        : "
        f"{floor_id} | "
        f"{room_name} | "
        f"{zone_id}"
    )

    print(
        "Offline Save : Failed"
    )

    print(
        "Reconnect    : Success"
    )

    print(
        "UI Save      : Success"
    )

    print(
        "Server Save  : Success"
    )

    print(
        "=========================================="
    )
    
    
    