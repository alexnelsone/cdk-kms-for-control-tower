#!/usr/bin/env python3
import aws_cdk as cdk
from cdk_nag import AwsSolutionsChecks, NIST80053R5Checks

from cdk_kms_for_control_tower.cdk_kms_for_control_tower_stack import (
    CdkKmsForControlTowerStack,
)

app = cdk.App()
CdkKmsForControlTowerStack(
    app,
    "CdkKmsForControlTowerStack",
    synthesizer=cdk.DefaultStackSynthesizer(generate_bootstrap_version_rule=False),
)

app.synth()


cdk.Tags.of(app).add("CreatedBy", "cdk")

cdk.Aspects.of(app).add(AwsSolutionsChecks())
cdk.Aspects.of(app).add(NIST80053R5Checks())
app.synth()
