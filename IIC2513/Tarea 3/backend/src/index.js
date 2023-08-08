import koa from "koa";
import KoaLogger from "koa-logger";
import { koaBody } from "koa-body";
import cors from "@koa/cors"; // Importa el módulo cors debido al error
import router from "./routes.js";
import bodyParser from "koa-bodyparser";

// Crear instacioa Koa
const app = new koa();

app.use(KoaLogger());
app.use(koaBody());
app.use(cors());
app.use(bodyParser());

// koa-router
app.use(router.routes())


app.use((ctx, next) => {
    ctx.body = "Hola mundo"
});

app.listen(3000, () => {
    console.log("Iniciando app. Escuchando en el puerto 3000")
});