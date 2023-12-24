from aws_cdk import Stack
from aws_cdk import aws_iam as iam
from aws_cdk import aws_kms as kms
from constructs import Construct


class CdkKmsForControlTowerStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-kms-key-policy-for-cloudtrail.html
        kms_key_policy = iam.PolicyDocument(
            statements=[
                iam.PolicyStatement(
                    sid="Enable IAM User Permissions",
                    actions=["kms:*"],
                    resources=["*"],
                    principals=[
                        iam.AccountRootPrincipal(),
                    ],
                ),
                iam.PolicyStatement(
                    sid="Allow access for Key Administrators",
                    actions=[
                        "kms:Create*",
                        "kms:Describe*",
                        "kms:Enable*",
                        "kms:List*",
                        "kms:Put*",
                        "kms:Update*",
                        "kms:Revoke*",
                        "kms:Disable*",
                        "kms:Get*",
                        "kms:Delete*",
                        "kms:TagResource",
                        "kms:UntagResource",
                        "kms:ScheduleKeyDeletion",
                        "kms:CancelKeyDeletion",
                    ],
                    resources=["*"],
                    principals=[iam.AccountRootPrincipal()],
                ),
                iam.PolicyStatement(
                    sid="Allow use of the key",
                    actions=[
                        "kms:Encrypt",
                        "kms:Decrypt",
                        "kms:ReEncrypt*",
                        "kms:GenerateDataKey*",
                        "kms:DescribeKey",
                    ],
                    resources=["*"],
                    principals=[iam.AccountRootPrincipal()],
                ),
                iam.PolicyStatement(
                    sid="Allow Cloudtrail and Config to encrypt/decrypt logs",
                    actions=[
                        "kms:Decrypt",
                        "kms:GenerateDataKey*",
                    ],
                    resources=["*"],
                    principals=[
                        iam.ServicePrincipal("config.amazonaws.com"),
                        iam.ServicePrincipal("cloudtrail.amazonaws.com"),
                    ],
                ),
                iam.PolicyStatement(
                    sid="Allow attachment of persistent resources",
                    actions=["kms:CreateGrant", "kms:ListGrants", "kms:RevokeGrant"],
                    resources=["*"],
                    principals=[iam.AccountRootPrincipal()],
                    conditions={"Bool": {"kms:GrantIsForAWSResource": "true"}},
                ),
            ]
        )

        kms.Key(
            self,
            "KmsKeyForControlTower",
            alias="kms-key-for-control-tower",
            description="KMS key for Control Tower Encryption",
            enabled=True,
            enable_key_rotation=True,
            policy=kms_key_policy,
        )
