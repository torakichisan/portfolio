import pandas as pd
import datetime

pd.set_option('display.unicode.east_asian_width', True)

def convertjisseki(ImpExcelPath,ImpSheetName):

    #定数宣言
    CONST_ANKEN = "txtSgy"
    CONST_SYANAI = "txtSgy_9999999"
    CONST_UNDER_BAR = '_'
    CONST_ANKEN_SUB = "00"
    CONST_SYANAI_SUB = "07"

    #シート内の取込範囲設定
    CONST_USE_COL = [5,7,9,12]

    #庶務のIDその他社内定例　：txtPln_9999999_00000018_07_35_20190501"
    #開発、運用案件のID ：txtSgy_XXXXXXXXXX_XXXXXXXXXX_02_00_20190501

    df = pd.read_excel(ImpExcelPath
                       ,header=2
                       ,usecols=CONST_USE_COL
                       ,sheet_name=ImpSheetName
                       ,na_values = 'na'
                       )

    print(df)

    df['日付'] = df['日付'].astype(str)
    df['日付'] = df['日付'].str.replace('-','')
    df['日付'] = df['日付'].str.replace('00:00:00','')
    df['日付'] = df['日付'].str.replace(' ', '')

    df = df.dropna(how='any')

    pkey_anken = CONST_ANKEN \
                 + CONST_UNDER_BAR \
                 + df['案件番号'] \
                 + CONST_UNDER_BAR \
                 + df['案件番号'] \
                 + df['コード'] \
                 + CONST_UNDER_BAR \
                 + df['日付']

    pkey_shanai = CONST_SYANAI + CONST_UNDER_BAR \
                 + df['案件番号'] \
                 + CONST_UNDER_BAR \
                 + CONST_SYANAI_SUB \
                 + df['コード']\
                 + CONST_UNDER_BAR \
                 + df['日付']

    #ABC部署主管案件
    df.loc[df['案件番号'].str.contains('ABC'),'Pkey'] = pkey_anken

    #DEF部署主管案件
    df.loc[df['案件番号'].str.contains('DEF'), 'Pkey'] = pkey_anken

    #GHI部署主管案件
    df.loc[df['案件番号'].str.contains('GHI'), 'Pkey'] = pkey_anken

    #社内庶務
    df.loc[df['案件番号'].str.contains('00000018'), 'Pkey'] = pkey_shanai

    grouped = df.groupby(['Pkey'], as_index=False).agg(sum)

    print(grouped)

    grouped['time'] = str
    grouped['date'] = int

    for i in range(len(grouped.index)):

        # 作業時間(数値)
        time = 0
        # 作業時間(文字列)
        StrTime = ""

        Str_date = ""
        Int_date = ""

        # td = time
        # td = (datetime.timedelta(hours=time))
        # print(td)
        time = grouped.時間[i]

        StrTime = str((datetime.timedelta(hours=time)))
        StrTime = StrTime[:len(StrTime)-3]
        grouped.time[i] = StrTime

        Str_date = grouped.Pkey[i]
        Int_date = int(Str_date[-8:])
        grouped.date[i] = Int_date

    print(grouped)

    grouped = grouped.sort_values('date')

    print(grouped)

    grouped = grouped.reset_index(drop=True)

    print(grouped)

    return grouped