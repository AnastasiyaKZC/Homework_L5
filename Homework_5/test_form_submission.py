from selene import browser, have, be, command


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

    # Выбираем дату рождения
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__year-select").type("1984")
    browser.element(".react-datepicker__month-select").type("May")
    browser.element(".react-datepicker__day--009").click()

    # Вводим предметы
    browser.element("#subjectsInput").type("Math").press_enter() #тут повозилась - не знала, что это выпадашка, пыталась ввести свой текст

    # Вводим хобби
    browser.element('[for="hobbies-checkbox-2"]').click()

    # Вводим изображение
    browser.element("#uploadPicture").send_keys("/Users/kuznetsova/Desktop/download.jpg")

    # Вводим текущий адрес
    browser.element("#currentAddress").type("Ростов-на-Дону, ул.Города Волос")

    # Выбираем штат
    browser.element("#state").perform(command.js.scroll_into_view).click() # скрол к элементу
    browser.element("#state").should(be.clickable).click() # задержка до появления списка
    browser.element("#state").click()
    browser.all("div.css-11unzgr").element_by(have.text("Haryana")).click()

    # Дожидаемся загрузки списка городов
    browser.element("#city").should(be.clickable).click() # задержка до появления списка
    browser.all("div.css-11unzgr").element_by(have.text("Karnal")).click()

    # Отправляем форму
    browser.element("#submit").press_enter()

    # Проверяем, что форма отправлена (например, через проверку заголовка или успешного сообщения)
    browser.element(".modal-title").should(have.text("Thanks for submitting the form"))