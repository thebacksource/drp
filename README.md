import requests
import time

# List of all major Roblox endpoints (publicly accessible)
roblox_services = {
    # Website & APIs
    "Website": "https://www.roblox.com",
    "API": "https://api.roblox.com",
    "Auth": "https://auth.roblox.com",
    "Catalog": "https://catalog.roblox.com",
    "Inventory": "https://inventory.roblox.com",
    "Friends": "https://friends.roblox.com",
    "Avatar": "https://avatar.roblox.com",
    "Economy": "https://economy.roblox.com",
    "Groups": "https://groups.roblox.com",
    "Notifications": "https://notifications.roblox.com",
    "Develop": "https://develop.roblox.com",
    "Forum": "https://forum.roblox.com",
    "Trading": "https://trades.roblox.com",
    "Presence": "https://presence.roblox.com",
    "GameModeration": "https://gamemoderation.roblox.com",
    "Thumbnails": "https://thumbnails.roblox.com",
    "AssetDelivery": "https://assetdelivery.roblox.com",
    "Badges": "https://badges.roblox.com",
    "Points": "https://points.roblox.com",
    "TextFilter": "https://textfilter.roblox.com",
    "EconomyGames": "https://economygames.roblox.com",
    "GroupsModeration": "https://groupsmoderation.roblox.com",
    "Messaging": "https://messaging.roblox.com",
    "FriendsModeration": "https://friendsmoderation.roblox.com",
    "TradeAndCommerce": "https://trade.roblox.com",
}

def check_roblox_services():
    print("\n=== Checking all Roblox services ===")
    for name, url in roblox_services.items():
        try:
            response = requests.get(url, timeout=5)
            status_code = response.status_code
            if status_code == 200:
                print(f"[✅] {name} is UP | {response.elapsed.total_seconds()*1000:.0f} ms")
            else:
                print(f"[⚠️] {name} returned status code {status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[❌] {name} is DOWN | Error: {e}")

if __name__ == "__main__":
    while True:
        check_roblox_services()
        time.sleep(10)  # refresh every 10 seconds
