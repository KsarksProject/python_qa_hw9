import os
from tests.pages.registration_page import RegistrationPage


def test_registration_form(browser_management):
    test_data = {
        'first_name': 'Linus',
        'last_name': 'Torvalds',
        'email': 'torvalds@osdl.org',
        'gender': 'Male',
        'mobile': '9876543210',
        'birth_day': '28',
        'birth_month': 'December',
        'birth_year': '1969',
        'subjects': ['Accounting', 'Maths'],
        'hobby': 'Reading',
        'picture': 'contact.jpg',
        'address': '123, Open Source Development Labs',
        'state': 'NCR',
        'city': 'Delhi'
    }

    picture_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', test_data["picture"]))
    assert os.path.exists(picture_path), f"Файл {picture_path} не найден!"

    registration_page = RegistrationPage()
    registration_page.open() \
        .fill_first_name(test_data['first_name']) \
        .fill_last_name(test_data['last_name']) \
        .fill_email(test_data['email']) \
        .select_gender(test_data['gender']) \
        .fill_mobile(test_data['mobile']) \
        .set_date_of_birth(
            test_data['birth_day'],
            test_data['birth_month'],
            test_data['birth_year']
        ) \
        .fill_subjects(test_data['subjects']) \
        .select_hobby(test_data['hobby']) \
        .upload_picture(picture_path) \
        .fill_address(test_data['address']) \
        .select_state_and_city(
            test_data['state'],
            test_data['city']
        ) \
        .submit()
