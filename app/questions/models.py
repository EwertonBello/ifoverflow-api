from sqlalchemy import Column, ForeignKey, VARCHAR, INT, TEXT
from app.database import Base
from sqlalchemy.orm import relationship


class Question(Base):
    __tablename__ = 'Perguntas'

    id = Column('id_pergunta', INT, primary_key=True)
    title = Column('assunto', VARCHAR(100))
    description = Column('descricao', TEXT(1000))
    votes = Column('votos', INT)

    is_owner:bool = False
    my_vote: int = 0
    # --- belongsTo ---
    category_id = Column('Categorias_id_categoria', INT, ForeignKey('Categorias.id_categoria'))
    category = relationship("Category", back_populates="questions")

    user_id = Column('Usuarios_id_usuario', INT, ForeignKey('Usuarios.id_usuario'))
    user = relationship("User", back_populates="questions")
    # --- belongsTo ---
    # --- hasMany ---
    answers = relationship("Answer", back_populates="question")
    tags = relationship("Tags_Questions", back_populates="question")
    comments = relationship("Comments_Question", back_populates="question")
    my_votes = relationship("Votes_Question", back_populates="question")
    # --- hasMany ---


class Category(Base):
    __tablename__ = 'Categorias'

    id = Column('id_categoria', INT, primary_key=True)
    name = Column('nome', VARCHAR(80))
    # --- hasMany ---
    questions = relationship("Question", back_populates="category")
    # --- hasMany ---


class Tag(Base):
    __tablename__ = 'Tags'

    id = Column('id_tag', INT, primary_key=True)
    name = Column('nome', VARCHAR(80))
    # --- hasMany ---
    questions = relationship("Tags_Questions", back_populates="tag")
    # --- hasMany ---


class Tags_Questions(Base):
    __tablename__ = 'Tags_Perguntas'

    # --- belongsTo ---
    tag_id = Column('Tags_id_tag', INT, ForeignKey('Tags.id_tag'), primary_key=True)
    tag = relationship("Tag", back_populates="questions")

    question_id = Column('Perguntas_id_pergunta', INT, ForeignKey('Perguntas.id_pergunta'), primary_key=True)
    question = relationship("Question", back_populates="tags")
    # --- belongsTo ---


class Votes_Question(Base):
    __tablename__ = 'Votos_Pergunta'

    id = Column('id_votos_pergunta', INT, primary_key=True)
    vote = Column('voto', INT)
    # --- belongsTo ---
    user_id = Column('Usuarios_id_usuario', INT, ForeignKey('Usuarios.id_usuario'))
    question_id = Column('Perguntas_id_pergunta', INT, ForeignKey('Perguntas.id_pergunta'))
    question = relationship("Question", back_populates="my_votes")
    # --- belongsTo ---
