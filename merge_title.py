import json

# JSONファイルのパスを指定（上で保存した結果）
file_path = "./data/type_number.json"
# JSONファイルを開いてデータを読み込む
with open(file_path, "r", encoding="utf-8") as file:
    extracted_data = json.load(file)

# 同じepisodeNumberのレコードをグループ化する辞書
grouped_data = {}
for record in extracted_data:
    alternative_headline = record["schema:alternativeHeadline"]
    # 作品No.を取り除く
    alternative_headline = alternative_headline.split(" 作品No.")[0]
    # すべての空白を取り除く
    alternative_headline = alternative_headline.replace(" ", "")
    episode_number = record["schema:episodeNumber"]

    if episode_number not in grouped_data:
        grouped_data[episode_number] = {
            "schema:alternativeHeadline": alternative_headline,
            "schema:episodeNumber": episode_number,
        }
    else:
        grouped_data[episode_number]["schema:alternativeHeadline"] += (
            "/" + alternative_headline
        )

# 結果をリストに変換
final_result = list(grouped_data.values())

# 結果をJSONファイルに保存
with open("merge_title.json", "w", encoding="utf-8") as file:
    json.dump(final_result, file, ensure_ascii=False, indent=2)

print("処理が完了しました。結果はmerge_title.jsonファイルに保存されています。")
