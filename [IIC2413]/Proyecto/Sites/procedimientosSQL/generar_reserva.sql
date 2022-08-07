CREATE OR REPLACE FUNCTION

-- declaramos la función y sus argumentos
generar_reserva(pasajero1 varchar(30), pasajero2 varchar(30), pasajero3 varchar(30), codigo varchar(20), rutcomprador varchar(30))

-- declaramos lo que retorna, en este caso un booleano
RETURNS VOID AS $$ -- el buleano es solo para ver si se cumple

DECLARE
idmax int;
idticketmax int;
--vuelo_id varchar(20);
-- definimos nuestra función
BEGIN
    -- verificar si existe la columna generation, si no existe la agregamos y seteamos todos los valores de esa columna en 1
    SELECT INTO idmax
    MAX(reserva_id)
    FROM pasajerocomprador; 

    SELECT INTO idticketmax
    MAX(numero_ticket)
    FROM pasajerocomprador; 

    --SELECT vuelo_id
    --FROM idvuelo
    --WHERE codigo_vuelo = codigo;



    IF pasajero1 <> '' THEN
        INSERT INTO pasajerocomprador values(idmax + 1, idticketmax + 1, rutcomprador);
        INSERT INTO pasajeros values(idticketmax + 1, pasajero1);
        INSERT INTO ticketreserva values('codigo reserva', idticketmax + 1, 10000, 69, 222000);            
    END IF;

    IF pasajero2 <> '' THEN
        INSERT INTO pasajerocomprador values(idmax + 2, idticketmax + 2, rutcomprador);
        INSERT INTO pasajeros values(idticketmax + 2, pasajero2);
        INSERT INTO ticketreserva values('codigo reserva', idticketmax + 2, 10000, 69, 222000);            
    END IF;
    

    IF pasajero3 <> '' THEN
        INSERT INTO pasajerocomprador values(idmax + 3, idticketmax + 3, rutcomprador);
        INSERT INTO pasajeros values(idticketmax + 3, pasajero3);
        INSERT INTO ticketreserva values('codigo reserva', idticketmax + 3, 10000, 69, 222000);            
    END IF;


-- finalizamos la definición de la función y declaramos el lenguaje
END
$$ language plpgsql