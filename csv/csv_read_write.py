import csv


# ファイルのリードライトを行うクラス
class CsvFileReadWrite:
    # ファイルを書き込むメソッド
    def csv_write(self, path, text, mode="w"):
        try:

            # ファイルを開く
            target_file = open(path, mode, encoding="utf_8")
            # ファイルオブジェクトのデータをCSVファイル形式で読み込む
            dataWriter = csv.writer(target_file, lineterminator='\n')
            # CSVファイルに書き込む
            dataWriter.writerows(text)
            result = "ok"
            # ファイルを閉じる
            target_file.close()
        except:
            result = "ng"

        return result

    def csv_read(self, path):
        try:
            # ファイルを開く
            target_file = open(path, encoding="utf_8")
            # ファイルオブジェクトのデータを行数分リストで取得する
            text_lines = csv.reader(target_file)
            # 取得したファイルオブジェクトから配列形式でデータを取り出す
            texts = list(text_lines)
            # ファイルを閉じる
            target_file.close()
        except:
            texts = "ng"

        return texts


# クラスのテストコード(CSVファイル書き込み)
def main():
    c = CsvFileReadWrite()
    # 入力データを作成
    texts = [[1, "かきくけこ"], [2, "さしすせそ"]]

    # 追記モードでコールする
    answer = c.csv_write("./test2.csv", texts, "a")
    print(answer)

# クラスのテストコード(CSVファイル読み込み)
    c = CsvFileReadWrite()
    texts = c.csv_read("./test2.csv")
    print(texts)


if __name__ == "__main__":
    main()
