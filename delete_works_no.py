import json
import re

# JSONファイルのパスを指定
file_path = "./data/merge_title.json"

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
        # 作品No.（ピリオドの有無を考慮）とそれに続く括弧内のテキストを削除
        titles = re.split(r"作品No\.?(\d+)(?:\（\d+/+\d+\）)?", alternative_headline)
        titles = [re.sub(r"[\s　]+", "", title) for title in titles if title.strip()]

        # タイトルを"/"で結合
        joined_headlines = "/".join(titles)

        # 結果を追加する
        final_result.append(
            {
                "schema:alternativeHeadline": joined_headlines,
                "schema:episodeNumber": episode_number,
            }
        )

# 結果をJSONファイルに保存
with open("final_result_filtered.json", "w", encoding="utf-8") as file:
    json.dump(final_result, file, ensure_ascii=False, indent=2)

print("処理が完了しました。結果はfinal_result_filtered.jsonファイルに保存されています。")
