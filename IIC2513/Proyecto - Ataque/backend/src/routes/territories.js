const Router = require('koa-router');

const router = new Router();

router.post('territories.move', '/move', async (ctx) => {
  try {
    // finds territories
    const playerTerritory1 = await ctx.orm.PlayerTerritory.findAll({
      where: {
        gameId: ctx.request.body.gameId,
        territoryId: ctx.request.body.from,
      },
    });
    const playerTerritory2 = await ctx.orm.PlayerTerritory.findAll({
      where: {
        gameId: ctx.request.body.gameId,
        territoryId: ctx.request.body.to,
      },
    });
    const from = playerTerritory1[0];
    const to = playerTerritory2[0];
    const territoryFrom = await ctx.orm.Territory.findByPk(from.territoryId);
    const territoryTo = await ctx.orm.Territory.findByPk(to.territoryId);
    // Create response
    let response = `Moved ${ctx.request.body.armies} armies from ${territoryFrom.name} to ${territoryTo.name}`;
    let moved = true;
    // check if the amount of armies is valid (TODO)

    // check if the receiving territory is adjacent to the sending territory
    if (!territoryFrom.neighbours.includes(territoryTo.id)) {
      response = 'Territories are not adjacent';
      moved = false;
    }

    // check if move leaves less than one army in the territory
    if (from.armies - ctx.request.body.armies < 1) {
      response = 'You cannot leave less than one army in a territory';
      moved = false;
    }

    // Move is valid, update the territories
    if (moved) {
      from.set({ armies: from.armies - ctx.request.body.armies });
      await from.save();
      to.set({ armies: to.armies + ctx.request.body.armies });
      await to.save();
    }

    // Send response
    ctx.body = response;
  } catch (error) {
    console.log(error);
    // Manejo de errores en caso de que el juego no sea encontrado
    ctx.status = 404;
    ctx.body = {
      error: 'Could not complete move',
    };
  }
});

router.post('territories.add', '/add', async (ctx) => {
  try {
    // finds territories
    const playerTerritory = await ctx.orm.PlayerTerritory.findAll({
      where: {
        gameId: ctx.request.body.gameId,
        territoryId: ctx.request.body.value,
      },
    });
    const addTo = playerTerritory[0];
    const territoryTo = await ctx.orm.Territory.findByPk(addTo.territoryId);
    // Create response
    const response = `Added ${ctx.request.body.armies} armies to ${territoryTo.name}`;

    // Save the new amount of armies
    addTo.set({ armies: addTo.armies + ctx.request.body.armies });
    await addTo.save();
    // Send response
    ctx.body = response;
  } catch (error) {
    console.log(error);
    // Manejo de errores en caso de que el juego no sea encontrado
    ctx.status = 404;
    ctx.body = {
      error: 'Could not complete move',
    };
  }
});

module.exports = router;
