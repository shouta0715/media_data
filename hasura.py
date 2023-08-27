import json

# JSONファイルのパスを指定
file_path = "./result.json"

# JSONファイルを開いてデータを読み込む
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# 各レコードを処理する
for record in data:
    title = record["schema:alternativeHeadline"]
    number = record["schema:episodeNumber"]

    # 指定された形式で表示（ダブルクォーテーションで囲む）
    print(
        '{title: "'
        + title
        + '", number: '
        + str(number)
        + ', start_time: "2021-01-01T00:00:00", end_time: "2021-01-01T00:00:00", work_id: 828, has_next_episode: false, has_prev_episode: false},'
    )
