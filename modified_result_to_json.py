import ast
import json
import pandas as pd

years = ['2017', '2018', '2019', '2020', '2021', '2022']

for year in years:

    df = pd.read_excel('./' + year + '/result.xlsx', converters={
        'dashes': str, '_nest_parent_': str}).fillna("")

    def toRealList(strList):
        if pd.isna(strList) or strList == '':
            return
        lst = ast.literal_eval(strList)
        return json.loads(json.dumps(lst))

    df['notes'] = df['notes'].apply(lambda x: toRealList(x))
    df['en_notes'] = df['en_notes'].apply(lambda x: toRealList(x))
    df['ko_notes'] = df['ko_notes'].apply(lambda x: toRealList(x))
    df['general'] = df['general'].apply(lambda x: toRealList(x))
    df['en_general'] = df['en_general'].apply(lambda x: toRealList(x))
    df['ko_general'] = df['ko_general'].apply(lambda x: toRealList(x))
    df['regulation_id'] = df['regulation_id'].apply(lambda x: toRealList(x))

    with open('bieuthue' + year + '.json', 'w') as f:
        json.dump(json.loads(df.to_json(orient="records")), f)
    # df.to_excel('bieuthue' + year + '.xlsx', index=False)
