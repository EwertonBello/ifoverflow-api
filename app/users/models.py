from sqlalchemy import Column, ForeignKey, VARCHAR, INT, TEXT
from app.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'Usuarios'

    id = Column('id_usuario', INT, primary_key=True)
    name = Column('nome', VARCHAR(80))
    votes = Column('votos', INT)
    avatar = Column('avatar', VARCHAR(200))
    email = Column('email', VARCHAR(200))
    password = Column('senha', VARCHAR(200))
    # --- belongsTo ---
    rating_id = Column('Classe_id_classe', INT, ForeignKey('Classes.id_classe'))
    rating = relationship("Rating", back_populates="users")

    campus_id = Column('Campus_id_campus', INT, ForeignKey('Campus.id_campus'))
    campus = relationship("Campus", back_populates="users")
    # --- belongsTo ---
    # --- hasMany ---
    questions = relationship("Question", back_populates="user")
    answers = relationship("Answer", back_populates="user")
    comments_answer = relationship("Comments_Answer", back_populates="user")
    comments_question = relationship("Comments_Question", back_populates="user")
    # --- hasMany ---


class Rating(Base):
    __tablename__ = 'Classes'

    id = Column('id_classe', INT, primary_key=True)
    name = Column('nome', VARCHAR(80))
    description = Column('descricao', TEXT)
    limit = Column('limite', INT)
    # --- hasMany ---
    users = relationship("User", back_populates="rating")
    # --- hasMany ---


class Campus(Base):
    __tablename__ = 'Campus'

    id = Column('id_campus', INT, primary_key=True)
    name = Column('nome', VARCHAR(80))
    # --- belongsTo ---
    state_id = Column('UF_id_uf', INT, ForeignKey('UF.id_uf'))
    state = relationship("State", back_populates="campus")
    # --- belongsTo ---

    # --- hasMany ---
    users = relationship("User", back_populates="campus")
    # --- hasMany ---


class State(Base):
    __tablename__ = 'UF'

    id = Column('id_uf', INT, primary_key=True)
    name = Column('nome', VARCHAR(80))
    # --- hasMany ---
    campus = relationship("Campus", back_populates="state")
    # --- hasMany ---
