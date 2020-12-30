def personal_data(**kwargs):
    return kwargs

print(personal_data(name=input('Имя: '),
    surname=input('Фамилия: '),
    birth_year=input('Год рождения: '),
    city_of_residence=input('Город проживания: '),
    email=input('Эл. почта: '),
    phone_number=input('Номер телефона: '),
    ))