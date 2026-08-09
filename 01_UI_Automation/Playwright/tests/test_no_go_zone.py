import requests

import pytest

from playwright.sync_api import Page


# ==================================================
# Test Data
# ==================================================

test_data = [
    ("Living Room", "F01"),
    ("Kitchen", "F01"),
    ("Bedroom", "F01"),
    ("Bathroom", "F01"),
    ("Study Room", "F02"),
    ("Living Room", "F02"),
    ("Kitchen", "F02"),
    ("Bedroom", "F03"),
    ("Kids Room", "F03"),
    ("Dining Room", "F03"),
]


# ==================================================
# No-Go Zone Creation Test
# ==================================================
#pytest.mark.parametrize    //  동일테스트 > 입력 데이터별 반복


@pytest.mark.parametrize(
    "room_name, floor_id",
    test_data
)
def test_create_no_go_zone(
    page: Page,
    room_name,
    floor_id
):

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
    # 5. UI에서 생성된 Zone 확인
    # ==========================================

    zone = page.locator(
        "#zone-list li"
    ).last


    zone.wait_for(
        state="visible"
    )


    # ==========================================
    # 6. UI 데이터 가져오기
    # ==========================================

    ui_zone_id = zone.get_attribute(
        "data-zone-id"
    )

    ui_floor_id = zone.get_attribute(
        "data-floor-id"
    )

    ui_zone_name = zone.get_attribute(
        "data-zone-name"
    )


    # ==========================================
    # 7. UI 데이터 검증
    # ==========================================

    assert ui_zone_id is not None

    assert ui_floor_id == floor_id

    assert ui_zone_name == room_name


    # ==========================================
    # 8. API를 통해 Zone 조회
    # ==========================================

    response = requests.get(
        "http://127.0.0.1:5000/api/zones"
    )


    # ==========================================
    # 9. API Response 검증
    # ==========================================

    assert response.status_code == 200


    zones = response.json()


    assert len(zones) > 0


    # ==========================================
    # 10. 현재 테스트에서 생성한
    #     Zone ID 검색
    # ==========================================

    api_zone = next(

        (
            zone
            for zone in zones

            if zone["zone_id"]
            == ui_zone_id
        ),

        None
    )


    # ==========================================
    # 11. 서버에 동일한 Zone 존재 확인
    # ==========================================

    assert api_zone is not None


    # ==========================================
    # 12. UI와 API 데이터 비교
    # ==========================================

    assert (
        api_zone["zone_id"]
        == ui_zone_id
    )

    assert (
        api_zone["floor_id"]
        == floor_id
    )

    assert (
        api_zone["name"]
        == room_name
    )

    assert (
        api_zone["status"]
        == "active"
    )


    # ==========================================
    # 13. 테스트 결과 출력
    # ==========================================

    print()

    print(
        "=========================================="
    )

    print(
        "No-Go Zone 생성 결과"
    )

    print(
        "=========================================="
    )

    print(
        f"Floor ID  : {ui_floor_id}"
    )

    print(
        f"Room Name : {ui_zone_name}"
    )

    print(
        f"Zone ID   : {ui_zone_id}"
    )

    print(
        f"Status    : {api_zone['status']}"
    )

    print(
        "=========================================="
    )
    
    
    