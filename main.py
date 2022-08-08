import pandas as pd
import numpy as np

df = pd.read_csv('C:/users/07108/OneDrive - VEKA/Документы/GitHub/pandas_numpy_tasks/data/adult.data.csv')
# print(df.head())
df = df.rename(columns={
    'education-num' : 'education_num',
    'marital-status' : 'marital_status',
    'capital-gain' : 'capital_gain',
    'capital-loss' : 'capital_loss',
    'hours-per-week' : 'hours_per_week',
    'native-country' : 'native_country'
})
print(df.head())


# 1. Посчитайте, сколько мужчин и женщин (признак sex) представлено в этом датасете

print('1. Посчитайте, сколько мужчин и женщин (признак sex) представлено в этом датасете')
df_sex_num = df.groupby('sex').agg({'age' : 'count'})
print('1 task', df_sex_num)
print()

# 2. Каков средний возраст мужчин (признак *age*) по всему датасету?

print('2. Каков средний возраст мужчин (признак *age*) по всему датасету?')
df_m_1 = df.query("sex == 'Male'").agg({'age' : 'mean'})
print('2 task, var.1', df_m_1)
print()

df_m = df.loc[df.sex == 'Male'].agg({'age' : 'mean'})
print('2 task, var.2', df_m)
print()

# 3. Какова доля граждан Соединенных Штатов (признак native-country)?

print('3. Какова доля граждан Соединенных Штатов (признак native-country)?')
total_num = df.agg({'age' : 'count'})
# print('total persons', total_num)
# print()
amer_native = df.query("native_country == 'United-States'").agg({'age' : 'count'})
# print('amer persons', amer_native)
amer_share = amer_native.values / total_num.values * 100
print('Amer share = ', amer_share, '%')
print()

# 4-5. Рассчитайте среднее значение и среднеквадратичное отклонение возраста тех,
# кто получает более 50K в год (признак salary) и тех, кто получает менее 50K в го

print('4-5. Рассчитайте среднее значение и среднеквадратичное отклонение возраста тех, '
      'кто получает более 50K в год (признак salary) и тех, кто получает менее 50K в год')
gr_less = df.query("salary == '<=50K'")
gr_more = df.query("salary == '>50K'")
# print(gr_less.head)
# print(gr_more.head)

avg_age_gr_less = gr_less.age.mean()
print('Среднее значение возраста в группе меньше 50К', avg_age_gr_less)
std_age_gr_less = gr_less.age.std()
print('Среднеквадратичное отклонение в группе меньше 50К', std_age_gr_less)
print()

avg_age_gr_more = gr_more.age.mean()
print('Среднее значение возраста в группе больше 50К', avg_age_gr_more)
std_age_gr_more = gr_more.age.std()
print('Среднеквадратичное отклонение в группе меньше 50К', std_age_gr_more)
print()

# 6. Правда ли, что люди, которые получают больше 50k, имеют минимум высшее образование?
# (признак education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters или Doctorate)

print('6. Правда ли, что люди, которые получают больше 50k, имеют минимум высшее образование? '
      '(признак education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters или Doctorate)')
ed_more = gr_more.education.unique()
ed_base = ['Bachelors', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', 'Masters', 'Doctorate']
ed_more_list = ed_more.tolist()
ed_res = ed_base == ed_more_list
if ed_res:
    print('Правда')
else:
    print('Не правда')
print()

# 7. Выведите статистику возраста для каждой расы (признак race) и каждого пола.
# Используйте groupby и describe. Найдите таким образом максимальный возраст мужчин расы Asian-Pac-Islander.

print('7. Выведите статистику возраста для каждой расы (признак race) и каждого пола. '
      'Используйте groupby и describe. Найдите таким образом максимальный возраст мужчин расы Asian-Pac-Islander.')

# stat_nation = df.groupby(['race', 'sex', 'age']).agg()
# print(stat_nation.describe)
print(df.age.describe())
