use ifoverflow;

-- RF 01 ------------------------------
DELIMITER $$
CREATE PROCEDURE cadastrarUsuario (nome VARCHAR(80), avatar VARCHAR(200), email VARCHAR(200), senha VARCHAR(200), Campus_id_campus INT)
BEGIN

  -- CRIO USUÁRIO
  INSERT INTO usuarios (nome,avatar,email,senha,Campus_id_campus) 
  VALUES (nome,avatar,email,senha,Campus_id_campus);

END $$
DELIMITER ;

-- RF 02 ------------------------------
DELIMITER $$
CREATE PROCEDURE perguntar (assunto VARCHAR(100), descricao TEXT(1000), Categorias_id_categoria INT, Usuarios_id_usuario INT)
BEGIN

INSERT INTO perguntas (assunto,descricao,Categorias_id_categoria,Usuarios_id_usuario)
VALUES (assunto,descricao,Categorias_id_categoria,Usuarios_id_usuario);

END $$
DELIMITER ;

-- RF 03 ------------------------------
DELIMITER $$
CREATE PROCEDURE responder (descricao TEXT(1000), Usuarios_id_usuario INT, Perguntas_id_pergunta INT)
BEGIN

  -- CRIO RESPOSTA
  INSERT INTO respostas (descricao, Usuarios_id_usuario, Perguntas_id_pergunta)
  VALUES (descricao, Usuarios_id_usuario, Perguntas_id_pergunta);

END $$
DELIMITER ;

-- RF 04 ------------------------------

-- RF 04 - Resposta
DELIMITER $$
CREATE PROCEDURE comentarResposta (descricao TEXT(1000), Usuarios_id_usuario INT, Respostas_id_resposta INT)
BEGIN

  -- CRIO COMENTÁRIO
  INSERT INTO comentarios_resposta (descricao, Usuarios_id_usuario, Respostas_id_resposta)
  VALUES (descricao, Usuarios_id_usuario, Respostas_id_resposta);

END $$
DELIMITER ;

-- RF 04 - Pergunta
DELIMITER $$
CREATE PROCEDURE comentarPergunta (descricao TEXT(1000), Usuarios_id_usuario INT, Perguntas_id_pergunta INT)
BEGIN

  -- CRIO COMENTÁRIO
  INSERT INTO comentarios_pergunta (descricao, Usuarios_id_usuario, Perguntas_id_pergunta)
  VALUES (descricao, Usuarios_id_usuario, Perguntas_id_pergunta);

END $$
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
DELIMITER $$
CREATE PROCEDURE votarNaResposta (id_usuario INT, id_resposta INT, voto INT)
BEGIN

DECLARE `_rollback` BOOL DEFAULT 0;
DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET `_rollback` = 1;

START TRANSACTION;
  -- LOCALIZO O DO DONO DA RESPOSTA
  SELECT donoDaResposta(id_resposta)
  INTO @id_usuario_dono;
  -- ATUALIZO O VOTO DO DONO DA RESPOSTA
  UPDATE usuarios SET usuarios.votos = usuarios.votos + voto WHERE usuarios.id_usuario = @id_usuario_dono;
  -- ATUALIZO O VOTO DA RESPOSTA
  UPDATE respostas SET respostas.votos = respostas.votos + voto WHERE respostas.id_resposta = id_resposta;
  -- REGISTRAR VOTO
  INSERT INTO votos_resposta (voto, Usuarios_id_usuario, Respostas_id_resposta)
  VALUES (voto, id_usuario, id_resposta);

IF `_rollback` THEN
    ROLLBACK;
ELSE
    COMMIT;
END IF;

END $$
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
DELIMITER $$
CREATE PROCEDURE votarNaPergunta (id_usuario INT, id_pergunta INT, voto INT)
BEGIN

DECLARE `_rollback` BOOL DEFAULT 0;
DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET `_rollback` = 1;

START TRANSACTION;
  -- LOCALIZO O DO DONO DA PERGUNTA
  SELECT donoDaPergunta(id_pergunta)
  INTO @id_usuario_dono;
  -- ATUALIZO O VOTO DO DONO DA PERGUNTA
  UPDATE usuarios SET usuarios.votos = usuarios.votos + voto WHERE usuarios.id_usuario = @id_usuario_dono;
  -- ATUALIZO O VOTO DA PERGUNTA
  UPDATE perguntas SET perguntas.votos = perguntas.votos + voto WHERE perguntas.id_pergunta = id_pergunta;
  -- REGISTRAR VOTO
  INSERT INTO votos_pergunta (voto, Usuarios_id_usuario, Perguntas_id_pergunta)
  VALUES (voto, id_usuario, id_pergunta);

IF `_rollback` THEN
    ROLLBACK;
ELSE
    COMMIT;
END IF;

END $$
DELIMITER ;

-- RF 07 ------------------------------
SET GLOBAL log_bin_trust_function_creators = 1;
-- RF 07
CREATE FUNCTION usuarioFoiClassificado(id_usuario INT)  
RETURNS INT

RETURN IFNULL((SELECT classes.id_classe 
  FROM usuarios, classes 
  WHERE usuarios.id_usuario = id_usuario
  AND classes.limite = usuarios.votos), 0);

-- RF 07 - Trigger Resposta

DELIMITER $$
CREATE TRIGGER tr_votosResposta AFTER UPDATE  
ON respostas  
FOR EACH ROW
BEGIN
  SET @id_classe = usuarioFoiClassificado(NEW.Usuarios_id_usuario);

  IF @id_classe > 0 THEN 
    UPDATE usuarios SET usuarios.Classe_id_classe = @id_classe 
    WHERE usuarios.id_usuario = NEW.Usuarios_id_usuario;
  END IF;
END$$
DELIMITER ;

-- RF 07 - Trigger Pergunta

DELIMITER $$
CREATE TRIGGER tr_votosPergunta AFTER UPDATE  
ON perguntas  
FOR EACH ROW
BEGIN
  SET @id_classe = usuarioFoiClassificado(NEW.Usuarios_id_usuario);

  IF @id_classe > 0 THEN 
    UPDATE usuarios SET usuarios.Classe_id_classe = @id_classe 
    WHERE usuarios.id_usuario = NEW.Usuarios_id_usuario;
  END IF;
END$$
DELIMITER ;

-- RF 08 ------------------------------
DELIMITER $$
CREATE PROCEDURE atualizarParaMelhorResposta (id_resposta INT)
BEGIN
  UPDATE respostas SET respostas.aceita = 1 
  WHERE respostas.id_resposta = id_resposta;
END $$
DELIMITER ;
