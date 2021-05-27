from pre import data_pre
import pandas as pd
import glob
import matplotlib.pyplot as plt

def input_df():
    
    # データセットの用意

    files = glob.glob("/tmp/working/dataset/nishika/old_apartment_2020/train/*")

    # trainデータ読み込み
    data_list = []
    for i, file in enumerate(files):
        data_list.append(pd.read_csv(file, index_col=0))

    df = pd.concat(data_list)

    return df