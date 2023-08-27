import json

# JSONファイルのパスを指定
file_path = "./data/media_sazae_data.json"

# JSONファイルを開いてデータを読み込む
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# 結果を保存するための空のリスト
result = []

# 各レコードを処理する
for record in data["record"]:
    metadata = record["metadata"]
    access_info = metadata.get("ma:accessInfo", [{}])

    # 必要な情報を抽出する
    for info in access_info:
        alternative_headline = info.get("schema:alternativeHeadline", [None])[0]
        episode_number = info.get("schema:episodeNumber", [None])[0]

        if alternative_headline and episode_number:
            result.append(
                {
                    "schema:alternativeHeadline": alternative_headline,
                    "schema:episodeNumber": episode_number,
                }
            )

# 結果をJSONファイルに保存
with open("result.json", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=2)

print("抽出が完了しました。結果はresult.jsonファイルに保存されています。")
