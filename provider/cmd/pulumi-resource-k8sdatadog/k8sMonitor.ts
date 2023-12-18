import { ComponentResource, ComponentResourceOptions, interpolate, Output } from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";

// Interface for Network
export interface K8sMonitorArgs{
  apiKey: Output<string>,
}

// Creates Network elements (e.g. VPC, etc)
export class K8sMonitor extends ComponentResource {
  public readonly namespace: Output<string>;

  constructor(name: string, args: K8sMonitorArgs, opts?: ComponentResourceOptions) {
    super("k8sdatadog:index:K8sMonitor", name, args, opts);

    const datadogNameSpace =  new k8s.core.v1.Namespace(`${name}-datadogns`, {}, {parent: this})

    const datadogK8sAgent = new k8s.helm.v3.Release(`${name}-datadogk8sagent`, {
      namespace: datadogNameSpace.id,
      name: "ddk8s",
      chart: "datadog",
      repositoryOpts: {
          repo: "https://helm.datadoghq.com",
      },
      version: "3.49.5",
      values: {
          datadog: {
            apiKey: args.apiKey,
            logs: {
              enabled: true,
            },
            kubelet: {
              tlsVerify: false,
            },
          },
      },
    }, {parent: this, ignoreChanges: ["checksum"]});

    this.namespace = datadogNameSpace.id
    this.registerOutputs({});
  }
}
