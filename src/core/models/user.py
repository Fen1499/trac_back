# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

# from db.database import Base


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String)
#     name = Column(String)
#     email = Column(String, unique=True, index=True)
#     password = Column(String)
#     company_id = Column(Integer, ForeignKey("company.id"))

#     companies = relationship("companies", back_populates="company")