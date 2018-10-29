import * as fetch from "isomorphic-fetch";

export default class GrpcAgentClient {
  constructor(private host: string) {}

  async createSelectionInterventionRequest(intervention: {
    imageUrl: string;
    imageContentType: string;
    instruction: string;
    optionsList: string[];
  }) {
    await fetch(`${this.host}/v1/intervention-requests`, {
      method: "POST",
      body: JSON.stringify({
        severity: "INFO",
        timestamp: Date.now(),
        selection_request: {
          image: {
            "content-type": intervention.imageContentType,
            url: intervention.imageUrl,
          },
          options: intervention.optionsList,
          instruction: intervention.instruction,
        },
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
  }

  async createBoundingBox2dInterventionRequest(intervention: {
    imageUrl: string;
    imageContentType: string;
    instruction: string;
  }) {
    await fetch(`${this.host}/v1/intervention-requests`, {
      method: "POST",
      body: JSON.stringify({
        severity: "INFO",
        timestamp: Date.now(),
        bounding_box_2d_request: {
          image: {
            "content-type": intervention.imageContentType,
            url: intervention.imageUrl,
          },
          instruction: intervention.instruction,
        },
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
  }

  async postData(stream: { name: string; type: string; value: any }) {
    await fetch(`${this.host}/v1/data`, {
      method: "POST",
      body: JSON.stringify({
        stream: stream.name,
        timestamp: Date.now(),
        [stream.type]: { value: stream.value },
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
  }

  async runTests() {
    console.log(`Connecting to HTTP host ${this.host}`);

    await this.postData({
      name: "text.2",
      type: "text",
      value: "test",
    });

    await this.postData({
      name: "numeric.2",
      type: "numeric",
      value: Math.random() * 100,
    });

    await this.postData({
      name: "pointcloud.2",
      type: "point cloud",
      value: {
        url: "https://example.com/file.pcd",
      },
    });

    await this.postData({
      name: "video.2",
      type: "video",
      value: {
        url: "https://example.com/file.jpg",
      },
    });

    await this.postData({
      name: "image.2",
      type: "image",
      value: {
        url: "https://example.com/file.jpg",
      },
    });

    await this.postData({
      name: "location.2",
      type: "location",
      value: {
        latitude: 37.434417,
        longitude: -122.142925,
      },
    });

    await this.postData({
      name: "file.2",
      type: "file",
      value: {
        url:
          "https://d27jdbl6qcr1lm.cloudfront.net/public-assets/general/error-log.csv",
        filename: "error-log.csv",
        size: 253,
      },
    });

    await this.createSelectionInterventionRequest({
      imageUrl:
        "https://d27jdbl6qcr1lm.cloudfront.net/public-assets/general/fruit-single.png",
      imageContentType: "image/png",
      instruction: "What is in the image?",
      optionsList: ["Cherimoya", "Rollinia", "Soursop", "None of the above"],
    });

    await this.createBoundingBox2dInterventionRequest({
      imageUrl:
        "https://d27jdbl6qcr1lm.cloudfront.net/public-assets/general/fruit-many.png",
      imageContentType: "image/png",
      instruction: "Redraw box around all fruit to help me locate.",
    });
  }
}
