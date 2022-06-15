

# import os

# path = '.'

# directory_contents = os.listdir(path)
# for item in directory_contents:
#     if os.path.isdir(item):
# print(item)


# ------------------ fixed error in a.txt return result in b.txt -------------------------------------

# import ast
# from googletrans import Translator

# translator = Translator()


# f = open('a.txt', 'r', encoding='utf-8')
# for line in f:
#     result = []
#     for i in ast.literal_eval(line):
#         translated = translator.translate(i, src='en', dest='ko')
#         result.append(translated.text)

#     with open('b.txt', 'a', encoding="utf-8") as f:
#         f.write(str(result) + '\n')
# f.close()


# ------------------ fixed error in a.txt return result in b.txt -------------------------------------


#  --------------- get bieuthue2022.json --------------------------


# import ast
# import json
# import pandas as pd

# years = ['2022']

# for year in years:

#     df = pd.read_excel('./' + year + '/result.xlsx', converters={
#         'dashes': str, '_nest_parent_': str}).fillna("")

#     def toRealList(strList):
#         try:
#             if pd.isna(strList) or strList == '':
#                 return
#             lst = ast.literal_eval(strList)
#             return json.loads(json.dumps(lst))
#         except:
#             with open('a.txt', 'a', encoding="utf-8") as f:
#                 f.write(str(strList) + '\n')
#             return False

# df['notes'] = df['notes'].apply(lambda x: toRealList(x))
# df['en_notes'] = df['en_notes'].apply(lambda x: toRealList(x))
# df['ko_notes'] = df['ko_notes'].apply(lambda x: toRealList(x))
# df['general'] = df['general'].apply(lambda x: toRealList(x))
# df['en_general'] = df['en_general'].apply(lambda x: toRealList(x))
# df['ko_general'] = df['ko_general'].apply(lambda x: toRealList(x))
# df['regulation_id'] = df['regulation_id'].apply(lambda x: toRealList(x))

# with open('bieuthue' + year + '.json', 'w') as f:
#     json.dump(json.loads(df.to_json(orient="records")), f)
# df.to_excel('bieuthue' + year + '.xlsx', index=False)

#  --------------- get bieuthue2022.json --------------------------
