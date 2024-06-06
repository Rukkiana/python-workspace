print(())
print(type(()))
years = (2020,2021,2016,2016,2016,2018,2022)
print(years)
print(years[::-1])
second_year = years[::-1]
print(2024 in years)
for year in years:
    print(year)
    print(2023 in years)
start_year = 2010
for year in second_year:
    print(year - start_year)
    print(years.count(2016))
    print(f"how many times do {year}",years.count(year),years.index(year))
tp1=(1,2,3,4)
tp2=(5,6,7)
print(tp1 + tp2)