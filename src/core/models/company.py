# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

# from db.database import Base


# class Company(Base):
#     __tablename__ = "companies"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     password = Column(String)
#     company_id = Column(Integer, ForeignKey("company.id"))

#     users = relationship("users", back_populates="user")
#     units = relationship("units", back_populates="unit")