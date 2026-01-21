
import csv, time, sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("Önce: python -m pip install requests")
    sys.exit(1)

USERNAMES = [
    "jeg6322","hoidya_","tengyanAI","ClaraChengGo","jinglingcookies","cryptobraveHQ","ZaggyGoKrazy",
    "eeelistar","pgreyy","dylangbane","bigray0x","beingRich2000","Hope_web3_","anymose96","SkylineETH",
    "MOODOO_Diary","TimHaldorsson","EJseong95","jungsama1101","CyberRektruck","MaraCakeHotSale",
    "erequendiweb3","sikiri0","jonnabutija","Day1Global Podcast","0xEvieYang","iinging747","Edward__Park",
    "bongbongcrypto","wyckoffweb","EnHeng456","y_cryptoanalyst","Crypto1Marine","sohota122","gomtu_xyz",
    "grebbycrypto","KierianV","Ch0k07","colu_farmer","0xconglomerate","periagoge1","ToBornSun_","hyeon__dev",
    "kimyg002","dnwlsfus1","N0BOYMAN","I_am_patrimonio","NyxHarrow","hriaznovden","wnektk333","dorong_x",
    "holly_web3","xingpt","momoy917","xabzxbt","r2Jamong","CHUNWON1155","Elizabethofyou","yuyue_chris",
    "CalligramReboot","ramztd","CandyDAO_leaf","semiko8585","heungmangoo","jayplayco","jundeu00","Scaevola_XI",
    "ProofOfTravis","hedacool","Jackhaldorsson","ScarlettWeb3","ouyoung11","xiaoyubtc","yueya_eth","73lV_",
    "0xSleepinRain","MichaelGneiting","xbbory482","babaixin","edoweb3","sezorock","letsgoddc746386","1959_77",
    "COmang___","Node_Park","Monothiez","ChloeTalk1","whenmoonsoon","ZF_lab","paigeinsf","wlgns5388","Tyleryapler",
    "0xMorrison","erbagoragourav","0x_xifeng","JH_929292","Monkeyhater_123","crypto_upalupa","moonyu_myu"
]

H = {
    "Accept": "application/json, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) VSCodeFetcher/1.0",
    "Origin": " ", # e.g. https://gomtu.xyz
    "Referer": " " # e.g. https://gomtu.xyz/
}

def get_json(url: str):
    try:
        r = requests.get(url, headers=H, timeout=25)
        status = r.status_code
        if status != 200:
            return status, {}
        try:
            return status, r.json()
        except Exception:
            return status, {}
    except Exception:
        return None, {}

def main():
    rows = []
    for i, u in enumerate(USERNAMES, 1):
        # smart_follower_count -> user_status
        st_status, st_js = get_json(f" ") # e.g. https://gomtu.xyz/api/kaito/user_status?username={u}
        # yaps_all -> yap/open
        op_status, op_js = get_json(f"") # e.g. https://gomtu.xyz/api/yap/open?username={u}

        # Expected structures: {"data": {...}, "status": 200} ve {"data": {...}}
        st_data = st_js.get("data") if isinstance(st_js, dict) else {}
        op_data = op_js.get("data") if isinstance(op_js, dict) else {}

        smart_follower_count = None
        if isinstance(st_data, dict):
            smart_follower_count = st_data.get("smart_follower_count")

        yaps_all = None
        if isinstance(op_data, dict):
            yaps_all = op_data.get("yaps_all")

        rows.append({
            "username": u,
            "yaps_all": yaps_all,
            "smart_follower_count": smart_follower_count
        })

        print(f"[{i}/{len(USERNAMES)}] {u} -> st={st_status}, op={op_status} | yaps_all={yaps_all} | smart_follower_count={smart_follower_count}")
        time.sleep(0.25)  # nazik gecikme

    out = Path("kaito_yaps_smart_followers.csv")
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["username", "yaps_all", "smart_follower_count"])
        w.writeheader()
        w.writerows(rows)

    print(f"\n Saved: {out.resolve()}")

if __name__ == "__main__":
    main()
