#!/usr/bin/env python3
"""
Test the employees API endpoint
"""
import requests
import json

def test_api():
    """Test the /api/employees endpoint"""
    print("Testing /api/employees endpoint...")
    
    url = "http://127.0.0.1:5000/api/employees"
    
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Response type: {type(data)}")
            
            if isinstance(data, dict):
                if 'success' in data:
                    print(f"Success: {data['success']}")
                    if 'employees' in data:
                        employees = data['employees']
                        print(f"Number of employees: {len(employees)}")
                        if employees:
                            print("First employee:")
                            print(json.dumps(employees[0], indent=2))
                    else:
                        print("No 'employees' key in response")
                        print("Response keys:", list(data.keys()))
                else:
                    print("Response data:")
                    print(json.dumps(data, indent=2))
            else:
                print(f"Unexpected response format: {data}")
        else:
            print(f"Error response: {response.text}")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_api()