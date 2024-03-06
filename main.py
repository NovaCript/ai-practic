import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Набор данных для обучения
training_data = {
    "Какая погода?": "Сегодня солнечно, температура +20 градусов.",
    "Какое время?": "Сейчас 12:00.",
    "Какая дата?": "Сегодня 10 июня.",
    "Как тебя зовут?": "Меня зовут AI Bot.",
    "Что ты умеешь?": "Я умею отвечать на несколько простых вопросов о погоде, времени и дате.",
    "Как дела?": "У меня все хорошо, спасибо!",
    "Пока": "До встречи!"
}

# Преобразование текста в векторы при помощи TF-IDF
vectorizer = TfidfVectorizer()
training_vectors = vectorizer.fit_transform(training_data.keys())


def get_user_input():
    return input("Ваш вопрос: ")


def find_most_similar(user_input):
    # Преобразование входного текста в вектор
    input_vector = vectorizer.transform([user_input])
    print(f'vector{input_vector}')
    # Вычисление косинусного сходства между векторами
    similarities = cosine_similarity(input_vector, training_vectors)
    print(f'sim{similarities}')
    # Нахождение индекса самого похожего вопроса
    closest = similarities.argmax()
    print(f'clo{closest}')
    # Получение ответа на самом похожем вопросе
    keys = list(training_data.keys())
    print(f'key{keys}')
    return training_data[keys[closest]]


def main():
    print("Привет! Я - AI Bot. Задайте мне вопрос.")
    while True:
        user_input = get_user_input()
        if user_input.lower() == "стоп":
            print("До встречи!")
            break
        response = find_most_similar(user_input)
        print(response)


if __name__ == "__main__":
    main()