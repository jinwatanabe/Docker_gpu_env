import glob
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib 

def data_pre(df):
    all_null_list = []

    for col in df.columns:
        if df[col].count() == 0:
            all_null_list.append(col)

    df = df.drop(all_null_list, axis=1)

    df = df.drop("種類", axis=1)
    df = df.drop("市区町村コード", axis=1)

    dis = {
        "30分?60分": 45,
        "1H?1H30": 75,
        "1H30?2H": 105,
        "2H?": 120
    }

    df["最寄駅：距離（分）"] = df["最寄駅：距離（分）"].replace(dis).astype(float)

    df["面積（㎡）"] = df["面積（㎡）"].replace("2000㎡以上", 2000).astype(float)

    year_dist = {}
    for i in df["建築年"].value_counts().keys():
        if "平成" in i:
            num = i.split("平成")[1].split("年")[0]
            year = 33 - int(num)
        if "昭和" in i:
            num = i.split("昭和")[1].split("年")[0]
            year = 96 - int(num)
        if "令和" in i:
            num = i.split("令和")[1].split("年")[0]
            year = 3 - int(num)
        if "戦前" in i:
            year = 76
        year_dist[i] = year

    df["建築年"] = df["建築年"].replace(year_dist).astype(float)

    year = {
        "年第１四半期":".25",
        "年第２四半期":".50",
        "年第３四半期":".75",
        "年第４四半期":".99"
    }

    year_list = {}
    for i in df["取引時点"].value_counts().keys():
        for k, j in year.items():
            if k in i:
                year_rep = i.replace(k, j)

        year_list[i] = year_rep

    df["取引時点"] = df["取引時点"].replace(year_list).astype(float)

    df["場所"] = df["都道府県名"].str.cat(df['市区町村名'])
    area = pd.read_csv('area_axis.csv')
    df = pd.merge(df.reset_index(), area, on="場所").set_index("ID")
    
    df = df.drop(["場所"], axis=1)

    for col in ["都道府県名", "市区町村名", "地区名", "最寄駅：名称", "間取り", "建物の構造", "用途", "今後の利用目的", "都市計画", "改装", "取引の事情等"]:
        df[col] = df[col].astype("category")
 
    return df