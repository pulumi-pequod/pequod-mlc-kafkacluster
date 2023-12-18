// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class ConfluentCluster extends pulumi.ComponentResource {
    /** @internal */
    public static readonly __pulumiType = 'kafkacluster:index:ConfluentCluster';

    /**
     * Returns true if the given object is an instance of ConfluentCluster.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ConfluentCluster {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ConfluentCluster.__pulumiType;
    }

    /**
     * Name of the Confluent environment that was created
     */
    public /*out*/ readonly envId!: pulumi.Output<string>;
    /**
     * URL for the Kafka environment.
     */
    public /*out*/ readonly kafkaUrl!: pulumi.Output<string>;

    /**
     * Create a ConfluentCluster resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ConfluentClusterArgs, opts?: pulumi.ComponentResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.kafkaClusterName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'kafkaClusterName'");
            }
            if ((!args || args.kafkaTopics === undefined) && !opts.urn) {
                throw new Error("Missing required property 'kafkaTopics'");
            }
            resourceInputs["kafkaClusterName"] = args ? args.kafkaClusterName : undefined;
            resourceInputs["kafkaTopics"] = args ? args.kafkaTopics : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["envId"] = undefined /*out*/;
            resourceInputs["kafkaUrl"] = undefined /*out*/;
        } else {
            resourceInputs["envId"] = undefined /*out*/;
            resourceInputs["kafkaUrl"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ConfluentCluster.__pulumiType, name, resourceInputs, opts, true /*remote*/);
    }
}

/**
 * The set of arguments for constructing a ConfluentCluster resource.
 */
export interface ConfluentClusterArgs {
    /**
     * Name to use for kafka cluster display name.
     */
    kafkaClusterName: pulumi.Input<string>;
    /**
     * Array of topics for the kafka cluster.
     */
    kafkaTopics: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Region for cluster. Default is region used by rest of stack.
     */
    region?: pulumi.Input<string>;
}
