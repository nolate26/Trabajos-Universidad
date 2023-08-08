const Router = require('koa-router');

const router = new Router();

const { playerObjective } = require('../models');

router.post('players.create', '/create', async (ctx) => {
  try {
    const player = await ctx.orm.Player.create({
      color: ctx.request.body.color,
      userId: ctx.request.body.userId,
      gameId: ctx.request.body.gameId,
    });
    ctx.body = player;
    ctx.status = 201;
  } catch (error) {
    ctx.body = error;
    ctx.status = 400;
  }
});

router.get('players.cards', '/cards_territories/:id', async (ctx) => {
  try {
    const players = await ctx.orm.Player.findAll({
      where: {
        gameId: ctx.params.id,
      },
    });
    for (const player of players) {
      console.log(player.id);
      const randomNumber = Math.floor(Math.random() * 2) + 1;
      console.log(randomNumber);
      if (randomNumber === 1) {
        const objectiveId = Math.floor(Math.random() * 4) + 1;
        console.log(objectiveId);

        // Crea el objeto en la tabla playerObjectives
        await playerObjective.create({
          objectiveId,
          playerId: player.id,
          type: 1,
        });
      } else if (randomNumber === 2) {
        const otherPlayers = players.filter((p) => p.id !== player.id);
        const randomIndex = Math.floor(Math.random() * otherPlayers.length);
        const selectedPlayer = otherPlayers[randomIndex];
        player.objectiveId = selectedPlayer.id;
        await player.save();
        // Crea el objeto en la tabla playerObjectives
        await playerObjective.create({
          objectiveId: selectedPlayer.id,
          playerId: player.id,
          type: 2,
        });
      }
    }
    ctx.body = {
      message: 'Cartas objetivo asignadas correctamente',
    };
  } catch (error) {
    ctx.status = 500;
    ctx.body = {
      error: 'Ocurrió un error al asignar las cartas objetivo',
    };
  }
});


router.get('players.userGames', '/user_games/:id', async (ctx) => {
  try {
    const players = await ctx.orm.Player.findAll({
      where: {
        userId: ctx.params.id, // El userId proporcionado
      },
    });
    const gameIds = players.map((player) => player.gameId);

    ctx.body = gameIds;
    ctx.status = 200;
  } catch (error) {
    ctx.body = error;
    ctx.status = 400;
  }
});

router.get('players.numberArmies', '/number_armies/:id', async (ctx) => {
  try {
    const Id = ctx.params.id;
    console.log(Id);
    const territoryCount = await ctx.orm.PlayerTerritory.count({
      where: {
        owner: Id,
      },
    });
    ctx.body = territoryCount;
    ctx.status = 200;
  } catch (error) {
    ctx.body = error;
    ctx.status = 400;
  }
});

// Hay que arreglarlo
router.get('players.show', '/show_territories/:id', async (ctx) => {
  try {
    const territories = await ctx.orm.Territory.findAll({
      where: {
        playerId: ctx.params.id,
      },
    });
    const aux = [];
    territories.forEach((element) => {
      aux.push({
        id: element.id,
        name: element.name,
        armies: element.armies,
      });
    });
    ctx.body = aux;
  } catch (error) {
    console.log(error);
    ctx.status = 500;
    ctx.body = {
      error: 'Error interno del servidor',
    };
  }
});

router.get('players.find', '/player_id/:userId/:gameId', async (ctx) => {
  try {
    const players = await ctx.orm.Player.findOne({
      where: {
        userId: ctx.params.userId, // El userId proporcionado
        gameId: ctx.params.gameId, // El gameId proporcionado
      },
    });
    ctx.body = players.id;
  } catch (error) {
    console.log(error);
    ctx.status = 500;
    ctx.body = {
      error: 'Error interno del servidor',
    };
  }
});

module.exports = router;
