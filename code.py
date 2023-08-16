import requests

def get_weather_data(city):
    url = f'https://wttr.in/{city}?format=%C+%t+%w'  # Форматирование запроса для получения температуры, погодных условий и ветра
    res = requests.get(url)
    return res.text

def get_training_advice(weather_condition):
    if 'rain' in weather_condition:
        return 'Игра на мокром поле может быть опасной. Обязательно обратите внимание на технику удержания мяча.'
    elif 'snow' in weather_condition:
        return 'Тренировка на снежной площадке может потребовать больше усилий. Уделите внимание разминке и устойчивости.'
    elif 'sun' in weather_condition:
        return 'Солнечная погода - идеальное время для тренировок. Работайте над физической подготовкой и тактикой.'
    elif 'windy' in weather_condition:
        return 'Ветреная погода может затруднить пасы и удары на дальние дистанции. Тренируйтесь на точность.'
    else:
        return 'Погодные условия нейтральны. Фокусируйтесь на разносторонних тренировках.'

try:
    city = input('Введите название города: ')
    print('Отображение погодного отчета для:', city)

    weather_data = get_weather_data(city)
    print('Погода:', weather_data)

    training_advice = get_training_advice(weather_data.lower())
    print('Советы для тренировки:', training_advice)
except Exception as e:
    print('Произошла ошибка:', e)
