# 対象の文字列
data = input()

# 文字列を分割して要素をListにする
splitStr = data.split(',')
print(splitStr)

# Listの各要素をintにする
spritInt = [int(i) for i in splitStr]
print(spritInt)

# sortプログラムをかく
sortInt = sorted(spritInt,reverse=True)
print(sortInt)

# 文字列に変換
sortStr = [str(s) for s in sortInt]
print(sortStr)

# Listを結合
joinStr = ''.join(sortStr)
print(joinStr)

# fileに出力する
file = "sort.txt"
fileObject = open(file,"w",encoding="utf-8")
fileObject.write(joinStr + "\n")
fileObject.close()