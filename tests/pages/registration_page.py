from selene import browser, have, command


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, first_name: str):
        browser.element('#firstName').type(first_name)
        return self

    def fill_last_name(self, last_name: str):
        browser.element('#lastName').type(last_name)
        return self

    def fill_email(self, email: str):
        browser.element('#userEmail').type(email)
        return self

    def select_gender(self, gender: str):
        browser.element(f'input[value="{gender}"]').perform(command.js.click)
        return self

    def fill_mobile(self, mobile: str):
        browser.element('#userNumber').type(mobile)
        return self

    def set_date_of_birth(self, day: str, month: str, year: str):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.all('.react-datepicker__year-select option').element_by(have.text(year)).click()
        browser.element('.react-datepicker__month-select').click()
        browser.all('.react-datepicker__month-select option').element_by(have.text(month)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subjects(self, subjects: list[str]):
        for subject in subjects:
            browser.element('#subjectsInput').type(subject).press_enter()
        return self

    def select_hobby(self, hobby: str):
        browser.all('.custom-checkbox label').element_by(have.text(hobby)).click()
        return self

    def upload_picture(self, picture_path: str):
        browser.element('#uploadPicture').send_keys(picture_path)
        return self

    def fill_address(self, address: str):
        browser.element('#currentAddress').type(address)
        return self

    def select_state_and_city(self, state: str, city: str):
        browser.element('#state').click()
        browser.all('[id^="react-select-3-option"]').element_by(have.text(state)).click()
        browser.element('#city').click()
        browser.all('[id^="react-select-4-option"]').element_by(have.text(city)).click()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self
