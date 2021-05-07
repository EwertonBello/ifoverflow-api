-- RF 02 ------------------------------
DELIMITER //
CREATE PROCEDURE perguntar (assunto VARCHAR(100), descricao TEXT(1000), Categorias_id_categoria INT, Usuarios_id_usuario INT)
BEGIN

INSERT INTO perguntas (assunto,descricao,Categorias_id_categoria,Usuarios_id_usuario)
VALUES (assunto,descricao,Categorias_id_categoria,Usuarios_id_usuario);

END //
DELIMITER ;


-- RF 05 ------------------------------
SET GLOBAL log_bin_trust_function_creators = 1;
-- FUNÇÕES PARA LOCALIZAR O USUÁRIO
-- LOCALIZAR DONO DA PERGUNTA
CREATE FUNCTION donoDaPergunta(id_pergunta INT)  
RETURNS INT
RETURN (SELECT perguntas.Usuarios_id_usuario 
FROM perguntas 
WHERE perguntas.id_pergunta = id_pergunta);

-- RF 05 - 
DELIMITER //
CREATE PROCEDURE votarNaPergunta (id_pergunta INT, voto INT)
BEGIN

DECLARE `_rollback` BOOL DEFAULT 0;
DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET `_rollback` = 1;

START TRANSACTION;
  -- LOCALIZO O DO DONO DA PERGUNTA
  SELECT donoDaPergunta(id_pergunta)
  INTO @id_usuario;
  -- ATUALIZO O VOTO DO DONO DA PERGUNTA
  UPDATE usuarios SET usuarios.votos = usuarios.votos + voto WHERE usuarios.id_usuario = @id_usuario;
  -- ATUALIZO O VOTO DA PERGUNTA
  UPDATE perguntas SET perguntas.votos = perguntas.votos + voto WHERE perguntas.id_pergunta = id_pergunta;

IF `_rollback` THEN
    ROLLBACK;
ELSE
    COMMIT;
END IF;

END //
DELIMITER ;