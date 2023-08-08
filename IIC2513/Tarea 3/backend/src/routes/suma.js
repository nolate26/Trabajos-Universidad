import Router from "koa-router"

const router = new Router();

router.get("/:operand1/:operand2", (ctx, next) => {
    const { operand1, operand2 } = ctx.params;

    const result = Number(operand1) + Number(operand2);

    // Enviar la respuesta con el resultado
    ctx.body = `${result}`;
});



export default router;

