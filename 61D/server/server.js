import Fastify from "fastify";
const fastify = Fastify({
  logger: true,
});

fastify.get("/", async function handler(request, reply) {
  return { message: "Jesus is LORD" };
});

try {
  await fastify.listen({ port: 8080 });
} catch (error) {
  fastify.log.error(error);
  process.exit(1);
}
