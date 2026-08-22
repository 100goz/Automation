import requests


BASE_URL = "http://127.0.0.1:5000"
ROBOT_ID = "RB001"


# ==========================================
# TC-API-01
#
# Wi-Fi 연결 끊김 후 재연결 시
# Robot 정상 동작 여부 확인
# ==========================================

def test_robot_wifi_reconnect():

    print()
    print("==========================================")
    print("Robot Wi-Fi Reconnect API Test")
    print("==========================================")


    # ==========================================
    # 1. 정상 상태 확인
    # ==========================================

    response = requests.get(
        f"{BASE_URL}/api/robots/{ROBOT_ID}/status"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["robot_id"] == ROBOT_ID
    assert data["connection"] == "online"
    assert data["status"] == "cleaning"

    print("Initial Robot Status : PASS")
    print(f"Connection           : {data['connection']}")
    print(f"Robot Status         : {data['status']}")


    # ==========================================
    # 2. Wi-Fi 연결 끊김
    # ==========================================

    response = requests.post(
        f"{BASE_URL}/api/robots/{ROBOT_ID}/network",
        json={
            "connection": "offline"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["connection"] == "offline"

    print("Wi-Fi Disconnect      : PASS")


    # ==========================================
    # 3. Robot Offline 상태 확인
    # ==========================================

    response = requests.get(
        f"{BASE_URL}/api/robots/{ROBOT_ID}/status"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["connection"] == "offline"

    print("Offline Status Check  : PASS")


    # ==========================================
    # 4. Wi-Fi 재연결
    # ==========================================

    response = requests.post(
        f"{BASE_URL}/api/robots/{ROBOT_ID}/network",
        json={
            "connection": "online"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["connection"] == "online"

    print("Wi-Fi Reconnect       : PASS")


    # ==========================================
    # 5. 재연결 후 Robot 상태 확인
    # ==========================================

    response = requests.get(
        f"{BASE_URL}/api/robots/{ROBOT_ID}/status"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["connection"] == "online"

    # 핵심 검증
    # Wi-Fi가 재연결된 후
    # 기존 Cleaning 상태가 유지되는지 확인
    assert data["status"] == "cleaning"

    # 배터리 상태도 유지되는지 확인
    assert data["battery"] == 85

    print("Robot Reconnected    : PASS")
    print(f"Connection           : {data['connection']}")
    print(f"Robot Status         : {data['status']}")
    print(f"Battery              : {data['battery']}%")


    # ==========================================
    # Final Result
    # ==========================================

    print()
    print("==========================================")
    print("TEST RESULT : PASS")
    print("==========================================")
    
    
    
    
    
    
    # ==========================================
# TC-API-02
# 존재하지 않는 Robot ID 조회
# ==========================================

def test_get_invalid_robot():

    response = requests.get(
        f"{BASE_URL}/api/robots/INVALID/status"
    )

    assert response.status_code == 404

    data = response.json()

    assert data["message"] == "Robot not found"

    print()
    print("==========================================")
    print("Invalid Robot ID Test")
    print("==========================================")
    print(f"Status Code : {response.status_code}")
    print("Result      : PASS")
    print("==========================================")


# ==========================================
# TC-API-03
# 잘못된 Wi-Fi 상태값 전송
# ==========================================

def test_invalid_connection_status():

    response = requests.post(
        f"{BASE_URL}/api/robots/{ROBOT_ID}/network",
        json={
            "connection": "unknown"
        }
    )

    assert response.status_code == 400

    data = response.json()

    assert data["message"] == "Invalid connection status"

    print()
    print("==========================================")
    print("Invalid Connection Status Test")
    print("==========================================")
    print(f"Status Code : {response.status_code}")
    print("Result      : PASS")
    print("==========================================")


# ==========================================
# TC-API-04
# connection 값 누락
# ==========================================

def test_missing_connection():

    response = requests.post(
        f"{BASE_URL}/api/robots/{ROBOT_ID}/network",
        json={}
    )

    assert response.status_code == 400

    data = response.json()

    assert data["message"] == "connection is required"

    print()
    print("==========================================")
    print("Missing Connection Test")
    print("==========================================")
    print(f"Status Code : {response.status_code}")
    print("Result      : PASS")
    print("==========================================")
    
    
    
    