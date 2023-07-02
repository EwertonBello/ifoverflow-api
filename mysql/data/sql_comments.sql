-- RF 04 ------------------------------

-- RF 04 - Resposta
DELIMITER //
CREATE PROCEDURE comentarResposta (descricao TEXT(1000), Usuarios_id_usuario INT, Respostas_id_resposta INT)
BEGIN

	-- CRIO COMENTÁRIO
	INSERT INTO comentarios_resposta (descricao, Usuarios_id_usuario, Respostas_id_resposta)
	VALUES (descricao, Usuarios_id_usuario, Respostas_id_resposta);

END //
DELIMITER ;

-- RF 04 - Pergunta
DELIMITER //
CREATE PROCEDURE comentarPergunta (descricao TEXT(1000), Usuarios_id_usuario INT, Perguntas_id_pergunta INT)
BEGIN

	-- CRIO COMENTÁRIO
	INSERT INTO comentarios_pergunta (descricao, Usuarios_id_usuario, Perguntas_id_pergunta)
	VALUES (descricao, Usuarios_id_usuario, Perguntas_id_pergunta);

END //
DELIMITER ;
