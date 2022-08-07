--Función 5
CREATE OR REPLACE FUNCTION

-- declaramos la función y sus argumentos
aceptar_rechazar_vuelo(codigo varchar(30), respuesta varchar(20))

-- declaramos lo que retorna, en este caso un booleano
RETURNS BOOLEAN AS $$ -- el buleano es solo para ver si se cumple



-- definimos nuestra función
BEGIN


    -- verificar si existe la columna generation, si no existe la agregamos y seteamos todos los valores de esa columna en 1
    IF respuesta = 'aceptar' THEN
        UPDATE codigovuelo
        SET estado = 'aceptado'
        WHERE codigo_vuelo LIKE codigo;
        RETURN TRUE;
    END IF;


    IF respuesta = 'rechazar' THEN
        UPDATE codigovuelo
        SET estado = 'rechazado'
        WHERE codigo_vuelo LIKE codigo;
        RETURN TRUE;

    ELSE
        -- y false si no se agregó
        RETURN FALSE;
    END IF;

-- finalizamos la definición de la función y declaramos el lenguaje
END
$$ language plpgsql
