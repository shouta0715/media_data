import json
import re

# JSONファイルのパスを指定
file_path = "./final_result_filtered.json"

# JSONファイルを開いてデータを読み込む
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# 最終結果を保存するためのリスト
final_result = []

# 各レコードを処理する
for record in data:
    alternative_headline = record["schema:alternativeHeadline"]
    episode_number = record["schema:episodeNumber"]

    if episode_number < 1742:
        # 数字だけの部分を削除
        titles = re.sub(r"/\d+/", "/", alternative_headline)
        # 余分な空白や全角スペースを削除
        titles = re.sub(r"[\s　]+", "", titles)

        # 結果を追加する
        final_result.append(
            {
                "schema:alternativeHeadline": titles,
                "schema:episodeNumber": episode_number,
            }
        )

# 結果をJSONファイルに保存
with open("final_result_cleaned_v2.json", "w", encoding="utf-8") as file:
    json.dump(final_result, file, ensure_ascii=False, indent=2)

print("処理が完了しました。結果はfinal_result_cleaned_v2.jsonファイルに保存されています。")
