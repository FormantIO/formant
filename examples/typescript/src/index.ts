import GrpcAgentClient from "./GrpcAgentClient";
import HttpAgentClient from "./HttpAgentClient";

const args = process.argv.slice(2);
const host = args.length > 0 ? args[0] : "localhost";

if (require.main === module) {
  (async () => {
    const grpcAgentClient = new GrpcAgentClient(`${host}:5501`);
    const httpAgentClient = new HttpAgentClient(`http://${host}:5502`);

    await grpcAgentClient.runTests();
    await httpAgentClient.runTests();
  })();
}
