from sqlalchemy import Column, ForeignKey, INT, TEXT, BOOLEAN
from app.database import Base
from sqlalchemy.orm import relationship


class Answer(Base):
    __tablename__ = 'Respostas'

    id = Column('id_resposta', INT, primary_key=True)
    description = Column('descricao', TEXT(1000))
    votes = Column('votos', INT)
    accepted = Column('aceita', BOOLEAN)
    my_vote: int = 0
    # --- belongsTo ---
    user_id = Column('Usuarios_id_usuario', INT, ForeignKey('Usuarios.id_usuario'))
    user = relationship("User", back_populates="answers")

    question_id = Column('Perguntas_id_pergunta', INT, ForeignKey('Perguntas.id_pergunta'))
    question = relationship("Question", back_populates="answers")
    # --- belongsTo ---
    # --- hasMany ---
    comments = relationship("Comments_Answer", back_populates="answer")
    my_votes = relationship("Votes_Answer", back_populates="answer")
    # --- hasMany ---


class Votes_Answer(Base):
    __tablename__ = 'Votos_Resposta'

    id = Column('id_votos_resposta', INT, primary_key=True)
    vote = Column('voto', INT)
    # --- belongsTo ---
    user_id = Column('Usuarios_id_usuario', INT, ForeignKey('Usuarios.id_usuario'))
    answer_id = Column('Respostas_id_resposta', INT, ForeignKey('Respostas.id_resposta'))
    answer = relationship("Answer", back_populates="my_votes")
    # --- belongsTo ---
