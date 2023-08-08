const Router = require('koa-router');
const dotenv = require('dotenv');
const jwtMiddleware = require('koa-jwt');
const territories = require('./routes/territories');
const games = require('./routes/games');
const users = require('./routes/users');
const players = require('./routes/players');
const attack = require('./routes/attack');
const authRoutes = require('./routes/authentication');
const scopeProtectedRoutes = require('./routes/scopeExample.js');

dotenv.config();

const router = new Router();

router.use(authRoutes.routes());
router.use('/territories', territories.routes());
router.use('/games', games.routes());

router.use('/players', players.routes());
router.use('/attack', attack.routes());

// Desde esta línea, todas las rutas requieriran un JWT. Esto no aplica para
// las líneas anteriores
router.use(jwtMiddleware({ secret: process.env.JWT_SECRET }));
router.use('/users', users.routes());
router.use('/scope-example', scopeProtectedRoutes.routes());

module.exports = router;
