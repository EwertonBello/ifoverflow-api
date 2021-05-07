-- RF 03 ------------------------------
DELIMITER //
CREATE PROCEDURE responder (descricao TEXT(1000), Usuarios_id_usuario INT, Perguntas_id_pergunta INT)
BEGIN

  -- CRIO RESPOSTA
  INSERT INTO respostas (descricao, Usuarios_id_usuario, Perguntas_id_pergunta)
  VALUES (descricao, Usuarios_id_usuario, Perguntas_id_pergunta);

END //
DELIMITER ;

-- RF 05 ------------------------------
SET GLOBAL log_bin_trust_function_creators = 1;
-- FUNÇÕES PARA LOCALIZAR O USUÁRIO
-- LOCALIZAR DONO DA RESPOSTA
CREATE FUNCTION donoDaResposta(id_resposta INT)  
RETURNS INT
RETURN (SELECT respostas.Usuarios_id_usuario 
FROM respostas 
WHERE respostas.id_resposta = id_resposta);


-- RF 05 - Resposta
DELIMITER //
CREATE PROCEDURE votarNaResposta (id_resposta INT, voto INT)
BEGIN

DECLARE `_rollback` BOOL DEFAULT 0;
DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET `_rollback` = 1;

START TRANSACTION;
  -- LOCALIZO O DO DONO DA RESPOSTA
  SELECT donoDaResposta(id_resposta)
  INTO @id_usuario;
  -- ATUALIZO O VOTO DO DONO DA RESPOSTA
  UPDATE usuarios SET usuarios.votos = usuarios.votos + voto WHERE usuarios.id_usuario = @id_usuario;
  -- ATUALIZO O VOTO DA RESPOSTA
  UPDATE respostas SET respostas.votos = respostas.votos + voto WHERE respostas.id_resposta = id_resposta;

IF `_rollback` THEN
    ROLLBACK;
ELSE
    COMMIT;
END IF;

END //
DELIMITER ;


-- RF 08 ------------------------------
DELIMITER //
CREATE PROCEDURE atualizarParaMelhorResposta (id_resposta INT)
BEGIN
  UPDATE respostas SET respostas.aceita = 1 
  WHERE respostas.id_resposta = id_resposta;
END //
DELIMITER ;
