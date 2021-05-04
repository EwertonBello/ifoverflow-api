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

DELIMITER //
CREATE TRIGGER tr_votosResposta AFTER UPDATE  
ON respostas  
FOR EACH ROW
BEGIN
  SET @id_classe = usuarioFoiClassificado(NEW.Usuarios_id_usuario);

  IF @id_classe > 0 THEN 
    UPDATE usuarios SET usuarios.Classe_id_classe = @id_classe 
    WHERE usuarios.id_usuario = NEW.Usuarios_id_usuario;
  END IF;
END//
DELIMITER ;

-- RF 07 - Trigger Pergunta

DELIMITER //
CREATE TRIGGER tr_votosPergunta AFTER UPDATE  
ON perguntas  
FOR EACH ROW
BEGIN
  SET @id_classe = usuarioFoiClassificado(NEW.Usuarios_id_usuario);

  IF @id_classe > 0 THEN 
    UPDATE usuarios SET usuarios.Classe_id_classe = @id_classe 
    WHERE usuarios.id_usuario = NEW.Usuarios_id_usuario;
  END IF;
END//
DELIMITER ;