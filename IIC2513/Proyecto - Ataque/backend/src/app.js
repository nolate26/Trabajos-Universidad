const Koa = require('koa');
const KoaLogger = require('koa-logger');
const bodyParser = require('koa-bodyparser');
const { koaBody } = require('koa-body');
const cors = require('@koa/cors');
const router = require('./routes');
const orm = require('./models');

// Crear instancia de Koa
const app = new Koa();

app.context.orm = orm;

// Middleweares por Koa
app.use(cors());
app.use(KoaLogger());
app.use(koaBody());
app.use(bodyParser());

// koa-router
app.use(router.routes());

app.use((ctx, next) => {
  ctx.body = 'Hola mundo! SALUDOS OLMA';
});

// app.listen(3000, () => {
//     console.log("Iniciando app. Escuchando el puerto 3000");
// });
module.exports = app;
