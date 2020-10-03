# -*- coding: utf-8-*-

"""
Formula 1 1996'daki puan sistemi yerine 2018'deki
puan sistemi olsaydı 1996 şampiyonu değişir miydi?

"""
# %%
import pandas as pd
import numpy as np

# Verilen sıralamaya göre puan değerini döndüren fonksiyon


def get_points(nth):
    nth = int(nth)
    if 0 < nth <= 10:
        url_new = "https://en.wikipedia.org/wiki/2018_Formula_One_World_Championship#Scoring_system"

        # 2018 sayfasından tüm tabloları alalım
        tables_new = pd.read_html(url_new)

        # puan sisteminin bulunduğu tabloyu seçelim
        df_point_system = tables_new[4]

        # points kolonunu silelim çünkü index numaralarından gideceğiz
        df_point_system.drop(0, axis=1, inplace=True)

        # puanların olduğu satırı iloc integer indexing ile seçelim ve bir Series elde edelim
        sr_point_system = df_point_system.iloc[1]

        return int(sr_point_system[nth])
    else:
        return 0

# Yarış sıralamalarını döndüren fonksiyon


def get_races():
    url_old = "https://en.wikipedia.org/wiki/1996_Formula_One_World_Championship#Points_scoring_system"
    columns = []

    # 1996 sayfasından tüm tabloları alalım
    tables_old = pd.read_html(url_old)

    # yarış skorlarının yazdığı tabloyu seçelim
    # ve içerisinden yalnızca sürücü isimleri ile yarış sıraları bulunan kısmı seçelim
    df_races = tables_old[6].iloc[2:26, 1:-1]

    # indexleri sürücü ismi yapıp eski indexleri drop edelim
    df_races = df_races.set_index(1, drop=True)

    # index kolonuna "driver" yazalım
    df_races.index.names = ["driver"]

    # kolon isimlerini düzenleyelim,
    for number in range(len(df_races.columns)):
        columns.append(number)
    df_races.columns = columns

    return df_races


def export_result():
    drivers = {}
    races = get_races()

    for row in races.itertuples():
        drivers[row[0]] = 0
        for item in row:
            if isinstance(item, str) and item.isnumeric():
                drivers[row[0]] += get_points(item)

    df_drivers = pd.DataFrame.from_dict(drivers, orient="index")
    stop_value = len(df_drivers) + 1
    df_drivers.insert(0, "place", np.arange(1, stop_value))
    df_drivers.rename(columns={0: "points"})
    df_drivers.to_csv(path_or_buf="result.csv")

    return drivers


def main():
    test = export_result()
    print(test)


if __name__ == "__main__":
    main()

# %%
