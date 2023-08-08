import Router from "koa-router";

const router = new Router();

router.post("/", (ctx, next) => {
    const { operand1, operand2 } = ctx.request.body;
    const result = Number(operand1) - Number(operand2);
    ctx.body = `${result}`;
});

export default router;