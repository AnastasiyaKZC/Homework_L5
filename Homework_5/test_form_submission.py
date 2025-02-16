from selene import browser, have, be


def test_fill_form():
    # Заполняем поля формы
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element("#firstName").type("Анастасия")
    browser.element("#lastName").type("Кузнецова")
    browser.element("#userEmail").type("kuznetsova@mail.com")

    # Выбираем пол
    browser.element('[for="gender-radio-2"]').click()

    # Вводим номер телефона
    browser.element("#userNumber").type("1234567890")

    # Убираем дату рождения
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__year-select").type("1984")
    browser.element(".react-datepicker__month-select").type("May")
    browser.element(".react-datepicker__day--009").click()

    # Вводим предметы
    #browser.element("#subjectsInput").type("Selene").press_enter()

    # Вводим изображение
    browser.element("#uploadPicture").send_keys("/Users/kuznetsova/Desktop/download.jpg")

    # Вводим текущий адрес
    browser.element("#currentAddress").type("Ростов-на-Дону, ул.Города Волос")

    # Выбираем штат
    browser.element("#state").click()
    browser.all("div.css-11unzgr").element_by(have.text("Haryana")).click()

    # Дожидаемся загрузки списка городов
    browser.element("#city").should(be.clickable).click()
    browser.all("div.css-11unzgr").element_by(have.text("Karnal")).click()

    # Отправляем форму
    browser.element("#submit").press_enter()

    # Проверяем, что форма отправлена (например, через проверку заголовка или успешного сообщения)
    browser.element(".modal-title").should(have.text("Thanks for submitting the form"))