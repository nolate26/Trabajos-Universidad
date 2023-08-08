const Router = require('koa-router');

const router = new Router();

router.post('attack', '/', async (ctx) => {
  try {
    // Find howe many dice each player is rolling
    const attackerLength = ctx.request.body.attacker_dice.length;
    const defenderLength = ctx.request.body.defender_dice.length;

    // Find who rolls less dices
    const minLength = Math.min(attackerLength, defenderLength);

    // Sort the dices
    const attackerDice = ctx.request.body.attacker_dice.sort((a, b) => b - a);
    const defenderDice = ctx.request.body.defender_dice.sort((a, b) => b - a);

    // Compare the dices
    let attackerWins = 0;
    let defenderWins = 0;
    for (let i = 0; i < minLength; i += 1) {
      if (attackerDice[i] > defenderDice[i]) {
        attackerWins += 1;
      } else {
        defenderWins += 1;
      }
    }
    // Find territories
    const playerTerritory1 = await ctx.orm.PlayerTerritory.findAll({
      where: {
        gameId: ctx.request.body.gameId,
        territoryId: ctx.request.body.attacker,
      },
    });
    const playerTerritory2 = await ctx.orm.PlayerTerritory.findAll({
      where: {
        gameId: ctx.request.body.gameId,
        territoryId: ctx.request.body.defender,
      },
    });
    const attackerPlayerTerritory = playerTerritory1[0];
    const attackerTerritory = await ctx.orm.Territory.findByPk(attackerPlayerTerritory.territoryId);
    const defenderPlayerTerritory = playerTerritory2[0];
    const defenderTerritory = await ctx.orm.Territory.findByPk(defenderPlayerTerritory.territoryId);
    // check if the attacking territory is adjacent to the defending territory
    if (!attackerTerritory.neighbours.includes(defenderTerritory.id)) {
      ctx.body = 'Territories are not adjacent';
      return;
    }
    // Check consecuences
    let consecuence = '';
    if (defenderPlayerTerritory.armies - attackerWins < 1) {
      // Defender lost the territory
      defenderPlayerTerritory.set({
        armies: attackerLength - 1, // Atacking armies move to the new territory
        owner: attackerPlayerTerritory.owner, // Territory is now owned by the attacker
      });
      await defenderPlayerTerritory.save();
      attackerPlayerTerritory.set({
        armies: attackerPlayerTerritory.armies - attackerLength + 1, // Attacking armies move to the new territory
      });
      await attackerPlayerTerritory.save();
      consecuence = `Defender lost the territory ${defenderTerritory.name} and ${attackerLength - 1} armies moved to it`;
    } else if (attackerPlayerTerritory.armies - defenderWins < 1) {
      // Attacker is out of troops
      attackerPlayerTerritory.set({
        armies: 1, // Attacker leaves one army in the territory
      });
      await attackerPlayerTerritory.save();
      consecuence = `Attacker is out of troops to attack in ${attackerTerritory.name}`;
      defenderPlayerTerritory.set({
        armies: defenderPlayerTerritory.armies - attackerWins, // Set amount of troops left in the territory
      });
      await defenderPlayerTerritory.save();
    } else {
      // Normal attack
      attackerPlayerTerritory.set({
        armies: attackerPlayerTerritory.armies - defenderWins, // Attacking armies move to the new territory
      });
      await attackerPlayerTerritory.save();
      defenderPlayerTerritory.set({
        armies: defenderPlayerTerritory.armies - attackerWins, // Set amount of troops left in the territory
      });
      await defenderPlayerTerritory.save();
      consecuence = 'None';
    }
    // Write response
    const response = {
      attackResult: `Attacker lost ${defenderWins} troops, defender lost ${attackerWins} troops`,
      consecuences: consecuence,
    };
    ctx.body = response;
    ctx.status = 201;
  } catch (error) {
    ctx.body = error;
    ctx.status = 400;
  }
});

module.exports = router;
