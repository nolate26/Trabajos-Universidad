import Router from "koa-router"
import suma from "./routes/suma.js"
import mult from "./routes/mult.js"
import resta from "./routes/resta.js"
import div from "./routes/div.js"

const router = new Router();

// agregamos rutas a usar
router.use("/mult", mult.routes());
router.use("/resta", resta.routes());
router.use("/div", div.routes());
router.use("/suma", suma.routes());


export default router;
