import json
import re
from collections import defaultdict

# JSONファイルのパスを指定
file_path = "./data/abc_title_number.json"

# JSONファイルを開いてデータを読み込む
with open(file_path, "r", encoding="utf-8") as file:
    extracted_data = json.load(file)

# episodeNumberでグループ化
groups = defaultdict(list)

for record in extracted_data:
    alternative_headline = record["schema:alternativeHeadline"]
    episode_number = record["schema:episodeNumber"]
    episode_number_int = int(re.sub(r"[A-H]", "", episode_number))
    groups[episode_number_int].append(
        {
            "schema:alternativeHeadline": alternative_headline,
            "schema:episodeNumber": episode_number,
        }
    )

# 各グループ内でアルファベット（A-H）に基づいてソート
final_result = []
for key in sorted(groups.keys()):
    group = groups[key]
    group.sort(key=lambda x: re.sub(r"\d+", "", x["schema:episodeNumber"]))
    for item in group:
        item["schema:episodeNumber"] = int(
            re.sub(r"[A-H]", "", item["schema:episodeNumber"])
        )
        final_result.append(item)

# 結果をJSONファイルに保存
with open("type_number.json", "w", encoding="utf-8") as file:
    json.dump(final_result, file, ensure_ascii=False, indent=2)

print("処理が完了しました。結果はtype_number.jsonファイルに保存されています。")
