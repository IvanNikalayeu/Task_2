import pandas as pd


df = pd.read_csv('data/adult.data.csv')

df = df.rename(columns={
    'education-num' : 'education_num',
    'marital-status' : 'marital_status',
    'capital-gain' : 'capital_gain',
    'capital-loss' : 'capital_loss',
    'hours-per-week' : 'hours_per_week',
    'native-country' : 'native_country'
})

# print(df)
#
# # 1. Посчитайте, сколько мужчин и женщин (признак sex) представлено в этом датасете
#
# print('1. Посчитайте, сколько мужчин и женщин (признак sex) представлено в этом датасете')
# df_sex_num = df.groupby('sex').agg({'age' : 'count'})
# print('1 task', df_sex_num)
# print()
#
# # 2. Каков средний возраст мужчин (признак *age*) по всему датасету?
#
# print('2. Каков средний возраст мужчин (признак *age*) по всему датасету?')
# df_m_1 = df.query("sex == 'Male'").agg({'age' : 'mean'})
# print('2 task, var.1', df_m_1)
# print()
#
# df_m = df.loc[df.sex == 'Male'].agg({'age' : 'mean'})
# print('2 task, var.2', df_m)
# print()
#
# # 3. Какова доля граждан Соединенных Штатов (признак native-country)?
#
# print('3. Какова доля граждан Соединенных Штатов (признак native-country)?')
# total_num = df.agg({'age' : 'count'})
# # print('total persons', total_num)
# # print()
# amer_native = df.query("native_country == 'United-States'").agg({'age' : 'count'})
# # print('amer persons', amer_native)
# amer_share = amer_native.values / total_num.values * 100
# print('Amer share = ', amer_share, '%')
# print()
#
# # 4-5. Рассчитайте среднее значение и среднеквадратичное отклонение возраста тех,
# # кто получает более 50K в год (признак salary) и тех, кто получает менее 50K в го
#
# print('4-5. Рассчитайте среднее значение и среднеквадратичное отклонение возраста тех, '
#       'кто получает более 50K в год (признак salary) и тех, кто получает менее 50K в год')
# gr_less = df.query("salary == '<=50K'")
# gr_more = df.query("salary == '>50K'")
# # print(gr_less.head)
# # print(gr_more.head)
#
# avg_age_gr_less = gr_less.age.mean()
# print('Среднее значение возраста в группе меньше 50К', avg_age_gr_less)
# std_age_gr_less = gr_less.age.std()
# print('Среднеквадратичное отклонение в группе меньше 50К', std_age_gr_less)
# print()
#
# avg_age_gr_more = gr_more.age.mean()
# print('Среднее значение возраста в группе больше 50К', avg_age_gr_more)
# std_age_gr_more = gr_more.age.std()
# print('Среднеквадратичное отклонение в группе меньше 50К', std_age_gr_more)
# print()
#
# # 6. Правда ли, что люди, которые получают больше 50k, имеют минимум высшее образование?
# # (признак education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters или Doctorate)
#
# print('6. Правда ли, что люди, которые получают больше 50k, имеют минимум высшее образование? '
#       '(признак education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters или Doctorate)')
# ed_more = gr_more.education.unique()
# ed_base = ['Bachelors', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', 'Masters', 'Doctorate']
# ed_more_list = ed_more.tolist()
# ed_res = ed_base == ed_more_list
# if ed_res:
#     print('Правда')
# else:
#     print('Не правда')
# print()

# 7. Выведите статистику возраста для каждой расы (признак race) и каждого пола.
# Используйте groupby и describe. Найдите таким образом максимальный возраст мужчин расы Asian-Pac-Islander.

# print('7. Выведите статистику возраста для каждой расы (признак race) и каждого пола. '
#       'Используйте groupby и describe. Найдите таким образом максимальный возраст мужчин расы Asian-Pac-Islander.')


# stat_nation = df.groupby(['race', 'sex', 'age']).agg({'fnlwgt' : 'count'})
# print(stat_nation.head())
# print(stat_nation.describe())
# stat_nation.discribe())
#print(df.age.describe())
# print(stat_nation)
# stat_nation= df.groupby(['race', 'sex']).agg({'age':['describe']}).round(2)
# print(stat_nation)

# 8. Среди кого больше доля зарабатывающих много (>50K): среди женатых или холостых мужчин (признак marital-status)?
# Женатыми считаем тех, у кого marital-status начинается с Married
# (Married-civ-spouse, Married-spouse-absent или Married-AF-spouse), остальных считаем холостыми.

# married = df[df['marital_status'].str.match('Married')]
# total_married = df[df['marital_status'].str.match('Married')].shape[0]
# print('Total_married', total_married)
# married_more = married.query("salary == '>50K'").shape[0]
# print('Married with >50K', married_more)
# married_share = round((married_more / total_married * 100),2)
# print(f'Married >50K share = {married_share}%')
#
# non_married = df[df['marital_status'].str.match('^(?![Married])')]
# total_non_married = df[df['marital_status'].str.match('^(?![Married])')].shape[0]
# print(f'Total unmarried {total_non_married}')
# unmarried_more = non_married.query('salary == ">50K"').shape[0]
# print('Unmarried with >50K', unmarried_more)
# unmarried_share = round((unmarried_more/total_non_married*100),2)
# print('Unmarried >50K share = ', unmarried_share, '%')
# if married_share > unmarried_share:
#     print('Married won')
# else:
#     print('Unmarried - cool')

# 9. Какое максимальное число часов человек работает в неделю
# (признак hours-per-week)? Сколько людей работают такое количество часов и каков среди них процент зарабатывающих много?
#
# max_hours = df.hours_per_week.max()
# print('Max hours per week = ', max_hours)
# num_max_hours = df.query(f'hours_per_week == {max_hours}')
# num_max_hours_shape = num_max_hours.shape[0]
# print('Number of max hours persons = ', num_max_hours_shape)
# num_max_hours_more = num_max_hours.query('salary == ">50K"').shape[0]
# print('Number >50K persons from them  = ', num_max_hours_more)
# perc_more = round(num_max_hours_more/num_max_hours_shape*100)
# print('% of >50K persons = ', perc_more, '%')

# 10. Посчитайте среднее время работы (hours-per-week) зарабатывающих мало и много (salary)
# для каждой страны (native-country).
#
# avg_time = df.groupby(['native_country', 'salary']).agg({'hours_per_week' : 'mean'})
# print(avg_time)

# 11. группируйте людей по возрастным группам young, adult, retiree, где:
#       young соответствует 16-35 лет
#       adult - 35-70 лет
#       retiree - 70-100 лет
#   Проставьте название соответсвтуещей группы для каждого человека в новой колонке AgeGroup
#
# gr_young = df.query('age >= 16 and age < 35')
# gr_young.insert(15, 'AgeGroup', 'young')
# gr_adult = df.query('age >= 35 and age < 70')
# gr_adult.insert(15, 'AgeGroup', 'adult')
# gr_retiree = df.query('age >= 70 and age < 100')
# gr_retiree.insert(15, 'AgeGroup', 'retiree')
#
# df_sort = pd.concat([gr_young,gr_adult, gr_retiree], sort=False, axis=0)
# print(df_sort)
#
# # 12. Определите количество зарабатывающих >50K в каждой из возрастных групп (колонка AgeGroup),
# # а также выведите название возрастной группы, в которой чаще зарабатывают больше 50К (>50K)
#
# num_gr_more = df_sort.query('salary == ">50K"').groupby('AgeGroup').agg({'age' : 'count'})
# num_gr_total = df_sort.groupby('AgeGroup').agg({'age' : 'count'})
# a_test = (num_gr_more['age'] / num_gr_total['age'])
# print(a_test[a_test == a_test.max()])


# 13. Сгруппируйте людей по типу занятости (колонка occupation) и определите количество людей в каждой группе.
# После чего напишите функцию фильтрации filter_func, которая будет возвращать только те группы,
# в которых средний возраст (колонка age) не больше 40 и в которых все работники отрабатывают
# более 5 часов в неделю (колонка hours-per-week)

gr_occupation = df.groupby('occupation').agg({'age' : 'count'})
print(type(gr_occupation))


