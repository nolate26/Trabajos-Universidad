CREATE OR REPLACE FUNCTION

-- declaramos la función y sus argumentos
convertir_pasajeros (pasaporte varchar(20), nombre varchar(30))

-- declaramos lo que retorna, en este caso un booleano
RETURNS BOOLEAN AS $$ -- el buleano es solo para ver si se cumple

DECLARE
idmax int; -- maximo id existente ver por defecto q tenga valor

-- definimos nuestra función
BEGIN
     
    SELECT INTO idmax
    MAX(id_usuario)
    FROM usuarios; 
    
    -- verificar si existe la columna generation, si no existe la agregamos y seteamos todos los valores de esa columna en 1
    IF pasaporte NOT IN (SELECT username FROM usuarios) THEN
        INSERT INTO usuarios values(idmax + 1, pasaporte, 'contraseña', 'Pasajero');
        
        RETURN TRUE; 

    ELSE
        -- y false si no se agregó
        RETURN FALSE;    
    END IF;

-- finalizamos la definición de la función y declaramos el lenguaje
END
$$ language plpgsql