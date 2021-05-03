from sqlalchemy import Column, ForeignKey, VARCHAR, INT, TEXT
from app.database import Base
from sqlalchemy.orm import relationship


class Question(Base):
    __tablename__ = 'Perguntas'

    id = Column('id_pergunta', INT, primary_key=True)
    title = Column('assunto', VARCHAR(100))
    description = Column('descricao', TEXT(1000))
    votes = Column('votos', INT)
    # --- belongsTo ---
    category_id = Column('Categorias_id_categoria', INT, ForeignKey('Categorias.id_categoria'))
    category = relationship("Category", back_populates="questions")

    user_id = Column('Usuarios_id_usuario', INT, ForeignKey('Usuarios.id_usuario'))
    user = relationship("User", back_populates="questions")
    # --- belongsTo ---


class Category(Base):
    __tablename__ = 'Categorias'

    id = Column('id_categoria', INT, primary_key=True)
    name = Column('nome', VARCHAR(80))
    # --- hasMany ---
    questions = relationship("Question", back_populates="category")
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
