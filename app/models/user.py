import hashlib
from sqlalchemy import Integer, String, Column
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def hash_password(self):
        if self.password:
            password_encoded = self.password.encode('utf8')
            hash_object = hashlib.sha256(password_encoded)
            self.password = hash_object.hexdigest()

    def check_password(self, password):
        password_encoded = password.encode('utf8')
        hash_object = hashlib.sha256(password_encoded)
        hashed_password = hash_object.hexdigest()
        return hashed_password == self.password
