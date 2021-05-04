from sqlalchemy import Column, ForeignKey, INT, TEXT
from app.database import Base
from sqlalchemy.orm import relationship


class Comments_Question(Base):
    __tablename__ = 'Comentarios_Pergunta'

    id = Column('id_comentarios_pergunta', INT, primary_key=True)
    description = Column('descricao', TEXT(1000))
    # --- belongsTo ---
    user_id = Column('Usuarios_id_usuario', INT, ForeignKey('Usuarios.id_usuario'))
    user = relationship("User", back_populates="comments_question")

    question_id = Column('Perguntas_id_pergunta', INT, ForeignKey('Perguntas.id_pergunta'))
    question = relationship("Question", back_populates="comments")
    # --- belongsTo ---

class Comments_Answer(Base):
    __tablename__ = 'Comentarios_Resposta'

    id = Column('id_comentarios_resposta', INT, primary_key=True)
    description = Column('descricao', TEXT(1000))
    # --- belongsTo ---
    user_id = Column('Usuarios_id_usuario', INT, ForeignKey('Usuarios.id_usuario'))
    user = relationship("User", back_populates="comments_answer")

    answer_id = Column('Respostas_id_resposta', INT, ForeignKey('Respostas.id_resposta'))
    answer = relationship("Answer", back_populates="comments")
    # --- belongsTo ---
