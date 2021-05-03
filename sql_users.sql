-- RF 01 ------------------------------
DELIMITER //
CREATE PROCEDURE cadastrarUsuario (nome VARCHAR(80), avatar VARCHAR(200), email VARCHAR(200), senha VARCHAR(200), Campus_id_campus INT)
BEGIN

  -- CRIO USUÁRIO
  INSERT INTO usuarios (nome,avatar,email,senha,Campus_id_campus) 
  VALUES (nome,avatar,email,senha,Campus_id_campus);

END //
DELIMITER ;