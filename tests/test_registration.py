from tests.pages.registration_page import RegistrationPage
from tests.models.user import User


def test_registration_form(browser_management):
    user = User(
        first_name='Linus',
        last_name='Torvalds',
        email='torvalds@osdl.org',
        gender='Male',
        mobile='9876543210',
        birth_day='28',
        birth_month='December',
        birth_year='1969',
        subjects=['Accounting', 'Maths'],
        hobby='Reading',
        picture='contact.jpg',
        address='123, Open Source Development Labs',
        state='NCR',
        city='Delhi'
    )

    expected_results = {
        'Student Name': f"{user.first_name} {user.last_name}",
        'Student Email': user.email,
        'Gender': user.gender,
        'Mobile': user.mobile,
        'Date of Birth': f"{user.birth_day} {user.birth_month},{user.birth_year}",
        'Subjects': ', '.join(user.subjects),
        'Hobbies': user.hobby,
        'Picture': user.picture,
        'Address': user.address,
        'State and City': f"{user.state} {user.city}"
    }

    registration_page = RegistrationPage()
    registration_page.open() \
        .register(user)

    # Проверка
    registration_page.should_have_registered(expected_results)
