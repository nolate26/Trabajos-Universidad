const Router = require('koa-router');

const router = new Router();

router.get('game.show', '/show/:id', async (ctx) => {
  const gameId = ctx.params.id;
  try {
    console.log(gameId);
    const gameExists = await ctx.orm.Game.findOne({
      where: { id: gameId },
    });

    if (!gameExists) {
      // Si el juego no existe, retorna un error 404
      ctx.status = 404;
      console.log(gameId);
      ctx.body = {
        error: 'Juego no encontrado',
      };
      return;
    }
    const players = await ctx.orm.Player.findAll({
      where: { gameId },
      attributes: ['id', 'color'], // Puedes incluir otros atributos que necesites
    });

    // Busca todos los territorios en el juego específico
    const territories = await ctx.orm.Territory.findAll({
      attributes: ['id', 'name', 'value'], // Puedes incluir otros atributos que necesites
    });
    const playerTerritories = await ctx.orm.PlayerTerritory.findAll({
      where: { gameId },
      attributes: ['owner', 'armies', 'territoryId'],
    });

    // Construye el JSON de respuesta
    const response = {
      gameId,
      turn: gameExists.turn,
      players: players.map((player) => ({
        id: player.id,
        color: player.color,
        territories: playerTerritories
          .filter((playerTerritory) => playerTerritory.owner === player.id)
          .map((playerTerritory) => ({
            id: playerTerritory.territoryId,
            armies: playerTerritory.armies,
          })),
      })),
    };

    // Envía el JSON como respuesta
    ctx.body = response;
  } catch (error) {
    // Manejo de errores en caso de que el juego no sea encontrado
    ctx.status = 404;
    console.log(error);
    ctx.body = {
      error: 'Juego no encontrado',
    };
  }
});

// Ruta POST para crear un nuevo juego y sus territorios
router.post('game.create', '/create', async (ctx) => {
  try {
    // Crea un nuevo juego con los atributos especificados
    const game = await ctx.orm.Game.create({
      state: 'en juego',
      turn: 1,
    });
    // Create players from users
    const colors = ['red', 'blue', 'green', 'yellow', 'pink', 'orange'];
    const users = ctx.request.body.mails;
    const players = [];
    for (email of users) {
      const user = await ctx.orm.User.findOne({
        where: { mail: email },
      });
      const player = await ctx.orm.Player.create({
        userId: user.id,
        gameId: game.id,
        color: colors.pop(),
      });
      players.push(player);
    }
    game.set({
      turn: players[1].id,
    });
    await game.save();
    // Crea los territorios y los asocia al juego recién creado
    const playerTerritories = [
      {
        armies: 2, owner: 1, gameId: game.id, territoryId: 1, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 1, gameId: game.id, territoryId: 2, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 1, gameId: game.id, territoryId: 3, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 1, gameId: game.id, territoryId: 4, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 1, gameId: game.id, territoryId: 5, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 2, gameId: game.id, territoryId: 6, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 2, gameId: game.id, territoryId: 7, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 2, gameId: game.id, territoryId: 8, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 2, gameId: game.id, territoryId: 9, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 2, gameId: game.id, territoryId: 10, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 2, gameId: game.id, territoryId: 11, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 2, gameId: game.id, territoryId: 12, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 3, gameId: game.id, territoryId: 13, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 3, gameId: game.id, territoryId: 14, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 3, gameId: game.id, territoryId: 15, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 3, gameId: game.id, territoryId: 16, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 3, gameId: game.id, territoryId: 17, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 3, gameId: game.id, territoryId: 18, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 3, gameId: game.id, territoryId: 19, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 4, gameId: game.id, territoryId: 20, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 4, gameId: game.id, territoryId: 21, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 4, gameId: game.id, territoryId: 22, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 4, gameId: game.id, territoryId: 23, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 4, gameId: game.id, territoryId: 24, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 4, gameId: game.id, territoryId: 25, createdAt: new Date(), updatedAt: new Date(),
      },
      {
        armies: 2, owner: 4, gameId: game.id, territoryId: 26, createdAt: new Date(), updatedAt: new Date(),
      },
    ];
    let chosenPlayers = players.map((x) => x);
    console.log(players.map((x) => x.id));
    for (territory of playerTerritories) {
      if (chosenPlayers.length === 0) {
        chosenPlayers = players.map((x) => x);
      }
      const randomNumber = Math.floor(Math.random() * chosenPlayers.length);
      const randomPlayer = chosenPlayers.splice(randomNumber, 1)[0];
      territory.owner = randomPlayer.id;
      await ctx.orm.PlayerTerritory.create(territory);
    }

    ctx.body = 'Partida creada con exito';
    ctx.status = 200;
  } catch (error) {
    // Manejo de errores en caso de que ocurra una excepción
    ctx.status = 500;
    console.log(error);
    ctx.body = {
      error: 'Error interno del servidor',
    };
  }
});




// Ruta POST para crear un nuevo juego y sus territorios
router.post('game.updateTurn', '/update_turn', async (ctx) => {
  try {
    // Crea un nuevo juego con los atributos especificados
    const gameId = ctx.request.body.gameId;
    const game = await ctx.orm.Game.findByPk(gameId);

    // Obtener todos los jugadores con el gameId especificado
    const players = await ctx.orm.Player.findAll({
      where: {
        gameId: gameId,
      },
      attributes: ['id'],
    });
    const playerIds = players.map((player) => player.id);
    console.log(playerIds);
    // Obtener la posición del turno actual en el array de playerIds
    const currentTurnIndex = playerIds.findIndex((id) => id === game.turn);
    let nextTurn;
    if (currentTurnIndex === -1) {
      // Si el turno actual no se encuentra en el array, seleccionar el primer jugador
      nextTurn = playerIds[0];
    } else if (currentTurnIndex === playerIds.length - 1) {
      // Si el turno actual es el último del array, pasar al primer jugador
      nextTurn = playerIds[0];
    } else {
      // Pasar al siguiente jugador en el array
      nextTurn = playerIds[currentTurnIndex + 1];
    }
    // Actualizar el turno en el juego
    await game.update({ turn: nextTurn });
    console.log(game.turn);

    ctx.body = 'Turno actualizado correctamente';
    ctx.status = 200;
  } catch (error) {
    // Manejo de errores en caso de que ocurra una excepción
    ctx.status = 500;
    console.log(error);
    ctx.body = {
      error: 'Error interno del servidor',
    };
  }
});



module.exports = router;
