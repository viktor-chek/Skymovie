from project.dao.models.user import User
from sqlalchemy.exc import NoResultFound


class UserDAO:
    """Класс осуществляющий работу с User"""
    def __init__(self, session):
        self.session = session

    def get_user_by_email(self, email):
        """Запрос к БД по email"""
        try:
            return self.session.query(User).filter(User.email == email).one()
        except NoResultFound:
            print(f"Пользователь не найден")

    def create_user(self, data):
        """Создание пользователя в БД"""
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def user_update(self, user, data):
        """Обновление информации в профиле пользователя"""
        user = self.get_user_by_email(user)
        user.name = data['name']
        user.surname = data['surname']
        user.favorite_genre = data['favorite_genre']
        self.session.add(user)
        self.session.commit()

        return user

    def update_pass(self, user_mail, new_pass):
        """Обновление пароля пользователя"""
        user = self.get_user_by_email(user_mail)
        user.password = new_pass

        self.session.add(user)
        self.session.commit()

        return user
