from passlib.context import CryptContext

# Создаем CryptContext с аргоном (argon2)
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# Хэшируем пароль "123"
hashed_password = pwd_context.hash("123")

# Выводим хэш
print("Hashed Password:", hashed_password)