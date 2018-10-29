import { AgentClient } from "./generated/agent_pb_service";
import {
  Datapoint,
  Numeric,
  Text,
  PointCloud,
  Video,
  Image,
  File,
  Location,
  InterventionRequest,
  SelectionRequest,
  Severity,
  BoundingBox2dRequest,
} from "./generated/agent_pb";

export default class GrpcAgentClient {
  client: AgentClient;

  constructor(private host: string) {
    this.client = new AgentClient(host);
  }

  generateText(stream: string, value: string) {
    const payload = new Text();
    payload.setValue(value);

    const datapoint = new Datapoint();
    datapoint.setStream(stream);
    datapoint.setText(payload);

    return datapoint;
  }

  generateNumeric(stream: string, value: number) {
    const payload = new Numeric();
    payload.setValue(value);

    const datapoint = new Datapoint();
    datapoint.setStream(stream);
    datapoint.setNumeric(payload);

    return datapoint;
  }

  generatePointCloud(stream: string, value: { url: string }) {
    const payload = new PointCloud();
    payload.setUrl(value.url);

    const datapoint = new Datapoint();
    datapoint.setStream(stream);
    datapoint.setPointCloud(payload);

    return datapoint;
  }

  generateVideo(stream: string, value: { url: string }) {
    const payload = new Video();
    payload.setUrl(value.url);

    const datapoint = new Datapoint();
    datapoint.setStream(stream);
    datapoint.setVideo(payload);

    return datapoint;
  }

  generateImage(stream: string, value: { url: string }) {
    const payload = new Image();
    payload.setUrl(value.url);

    const datapoint = new Datapoint();
    datapoint.setStream(stream);
    datapoint.setImage(payload);

    return datapoint;
  }

  generateLocation(
    stream: string,
    value: { longitude: number; latitude: number },
  ) {
    const payload = new Location();
    payload.setLongitude(value.longitude);
    payload.setLatitude(value.latitude);

    const datapoint = new Datapoint();
    datapoint.setStream(stream);
    datapoint.setLocation(payload);

    return datapoint;
  }

  generateFile(
    stream: string,
    value: { url: string; filename: string; size: number },
  ) {
    const payload = new File();
    payload.setUrl(value.url);
    payload.setFilename(value.filename);
    payload.setSize(value.size);

    const datapoint = new Datapoint();
    datapoint.setStream(stream);
    datapoint.setFile(payload);

    return datapoint;
  }

  generateSelectionInterventionRequest(value: {
    url: string;
    instruction: string;
    optionsList: string[];
  }) {
    const image = new Image();
    image.setUrl(value.url);

    const selection = new SelectionRequest();
    selection.setImage(image);
    selection.setInstruction(value.instruction);
    selection.setOptionsList(value.optionsList);

    const intervention = new InterventionRequest();
    intervention.setSelectionRequest(selection);
    intervention.setSeverity(Severity.INFO);

    return intervention;
  }

  generateBoundingBox2dInterventionRequest(value: {
    url: string;
    instruction: string;
  }) {
    const image = new Image();
    image.setUrl(value.url);

    const box = new BoundingBox2dRequest();
    box.setImage(image);
    box.setInstruction(value.instruction);

    const intervention = new InterventionRequest();
    intervention.setBoundingBox2dRequest(box);
    intervention.setSeverity(Severity.INFO);

    return intervention;
  }

  async postDataAsync(datapoint: Datapoint) {
    await new Promise((resolve, reject) =>
      this.client.postData(datapoint, err => (err ? reject(err) : resolve())),
    );
  }

  async runTests() {
    console.log(`Connecting to GRPC host ${this.host}`);

    await this.postDataAsync(this.generateText("text.1", "test"));
    await this.postDataAsync(
      this.generateNumeric("numeric.1", Math.random() * 100),
    );

    await this.postDataAsync(
      this.generatePointCloud("pointcloud.1", {
        url: "https://example.com/file.pcd",
      }),
    );

    await this.postDataAsync(
      this.generateVideo("video.1", {
        url: "https://example.com/file.jpg",
      }),
    );

    await this.postDataAsync(
      this.generateImage("image.1", {
        url: "https://example.com/file.jpg",
      }),
    );

    await this.postDataAsync(
      this.generateLocation("location.1", {
        latitude: 37.434417,
        longitude: -122.142925,
      }),
    );

    await this.postDataAsync(
      this.generateFile("file.1", {
        url:
          "https://d27jdbl6qcr1lm.cloudfront.net/public-assets/general/error-log.csv",
        filename: "error-log.csv",
        size: 253,
      }),
    );

    await new Promise((resolve, reject) =>
      this.client.createInterventionRequest(
        this.generateSelectionInterventionRequest({
          url:
            "https://d27jdbl6qcr1lm.cloudfront.net/public-assets/general/fruit-single.png",
          instruction: "What is in the image?",
          optionsList: [
            "Cherimoya",
            "Rollinia",
            "Soursop",
            "None of the above",
          ],
        }),
        err => (err ? reject(err) : resolve()),
      ),
    );

    await new Promise((resolve, reject) =>
      this.client.createInterventionRequest(
        this.generateBoundingBox2dInterventionRequest({
          url:
            "https://d27jdbl6qcr1lm.cloudfront.net/public-assets/general/fruit-many.png",
          instruction: "Redraw box around all fruit to help me locate.",
        }),
        err => (err ? reject(err) : resolve()),
      ),
    );
  }
}
