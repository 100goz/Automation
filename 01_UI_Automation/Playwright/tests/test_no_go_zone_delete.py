import requests

from playwright.sync_api import Page, expect


def test_delete_no_go_zone(page: Page):

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
    # 4. No-Go Zone 생성
    # ==========================================

    page.locator(
        "#create-zone"
    ).click()


    # ==========================================
    # 5. 생성된 Zone 확인
    # ==========================================

    zone = page.locator(
        "#zone-list li"
    ).last

    zone.wait_for(
        state="visible"
    )


    # ==========================================
    # 6. 삭제 전 Zone 정보 확인
    # ==========================================

    zone_id = zone.get_attribute(
        "data-zone-id"
    )

    assert zone_id is not None

    expect(zone).to_have_attribute(
        "data-floor-id",
        floor_id
    )

    expect(zone).to_have_attribute(
        "data-zone-name",
        room_name
    )


    print()

    print(
        f"Created Zone : "
        f"{floor_id} | "
        f"{room_name} | "
        f"{zone_id}"
    )


    # ==========================================
    # 7. Delete 버튼 클릭
    # ==========================================

    delete_button = zone.locator(
        "button",
        has_text="Delete"
    )

    delete_button.click()


    # ==========================================
    # 8. UI에서 Zone 삭제 확인
    # ==========================================

    expect(zone).to_be_hidden()


    # ==========================================
    # 9. GET /api/zones
    # ==========================================

    response = requests.get(
        "http://127.0.0.1:5000/api/zones"
    )


    # ==========================================
    # 10. API 응답 확인
    # ==========================================

    assert response.status_code == 200


    zones = response.json()


    # ==========================================
    # 11. 서버에서 Zone 삭제 확인
    # ==========================================

    remaining_zone_ids = [
        zone["zone_id"]
        for zone in zones
    ]


    assert zone_id not in remaining_zone_ids


    # ==========================================
    # 12. 결과 출력
    # ==========================================

    print()

    print(
        "=========================================="
    )

    print(
        "No-Go Zone 삭제 결과"
    )

    print(
        "=========================================="
    )

    print(
        f"Deleted Zone : "
        f"{floor_id} | "
        f"{room_name} | "
        f"{zone_id}"
    )

    print(
        f"UI Status    : Deleted"
    )

    print(
        f"API Status   : {response.status_code}"
    )

    print(
        f"Server Check : {zone_id} not found"
    )

    print(
        "=========================================="
    )
    
    
    