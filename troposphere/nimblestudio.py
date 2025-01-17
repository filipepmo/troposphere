# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 51.0.0


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import double


class StreamConfiguration(AWSProperty):
    """
    `StreamConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html>`__
    """

    props: PropsDictType = {
        "ClipboardMode": (str, True),
        "Ec2InstanceTypes": ([str], True),
        "MaxSessionLengthInMinutes": (double, False),
        "StreamingImageIds": ([str], True),
    }


class LaunchProfile(AWSObject):
    """
    `LaunchProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html>`__
    """

    resource_type = "AWS::NimbleStudio::LaunchProfile"

    props: PropsDictType = {
        "Description": (str, False),
        "Ec2SubnetIds": ([str], True),
        "LaunchProfileProtocolVersions": ([str], True),
        "Name": (str, True),
        "StreamConfiguration": (StreamConfiguration, True),
        "StudioComponentIds": ([str], True),
        "StudioId": (str, True),
        "Tags": (Tags, False),
    }


class StreamingImage(AWSObject):
    """
    `StreamingImage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html>`__
    """

    resource_type = "AWS::NimbleStudio::StreamingImage"

    props: PropsDictType = {
        "Description": (str, False),
        "Ec2ImageId": (str, True),
        "Name": (str, True),
        "StudioId": (str, True),
        "Tags": (Tags, False),
    }


class StudioEncryptionConfiguration(AWSProperty):
    """
    `StudioEncryptionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studio-studioencryptionconfiguration.html>`__
    """

    props: PropsDictType = {
        "KeyArn": (str, False),
        "KeyType": (str, True),
    }


class Studio(AWSObject):
    """
    `Studio <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html>`__
    """

    resource_type = "AWS::NimbleStudio::Studio"

    props: PropsDictType = {
        "AdminRoleArn": (str, True),
        "DisplayName": (str, True),
        "StudioEncryptionConfiguration": (StudioEncryptionConfiguration, False),
        "StudioName": (str, True),
        "Tags": (Tags, False),
        "UserRoleArn": (str, True),
    }


class ScriptParameterKeyValue(AWSProperty):
    """
    `ScriptParameterKeyValue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-scriptparameterkeyvalue.html>`__
    """

    props: PropsDictType = {
        "Key": (str, False),
        "Value": (str, False),
    }


class ActiveDirectoryComputerAttribute(AWSProperty):
    """
    `ActiveDirectoryComputerAttribute <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectorycomputerattribute.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Value": (str, False),
    }


class ActiveDirectoryConfiguration(AWSProperty):
    """
    `ActiveDirectoryConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectoryconfiguration.html>`__
    """

    props: PropsDictType = {
        "ComputerAttributes": ([ActiveDirectoryComputerAttribute], False),
        "DirectoryId": (str, False),
        "OrganizationalUnitDistinguishedName": (str, False),
    }


class ComputeFarmConfiguration(AWSProperty):
    """
    `ComputeFarmConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-computefarmconfiguration.html>`__
    """

    props: PropsDictType = {
        "ActiveDirectoryUser": (str, False),
        "Endpoint": (str, False),
    }


class LicenseServiceConfiguration(AWSProperty):
    """
    `LicenseServiceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-licenseserviceconfiguration.html>`__
    """

    props: PropsDictType = {
        "Endpoint": (str, False),
    }


class SharedFileSystemConfiguration(AWSProperty):
    """
    `SharedFileSystemConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html>`__
    """

    props: PropsDictType = {
        "Endpoint": (str, False),
        "FileSystemId": (str, False),
        "LinuxMountPoint": (str, False),
        "ShareName": (str, False),
        "WindowsMountDrive": (str, False),
    }


class StudioComponentConfiguration(AWSProperty):
    """
    `StudioComponentConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentconfiguration.html>`__
    """

    props: PropsDictType = {
        "ActiveDirectoryConfiguration": (ActiveDirectoryConfiguration, False),
        "ComputeFarmConfiguration": (ComputeFarmConfiguration, False),
        "LicenseServiceConfiguration": (LicenseServiceConfiguration, False),
        "SharedFileSystemConfiguration": (SharedFileSystemConfiguration, False),
    }


class StudioComponentInitializationScript(AWSProperty):
    """
    `StudioComponentInitializationScript <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentinitializationscript.html>`__
    """

    props: PropsDictType = {
        "LaunchProfileProtocolVersion": (str, False),
        "Platform": (str, False),
        "RunContext": (str, False),
        "Script": (str, False),
    }


class StudioComponent(AWSObject):
    """
    `StudioComponent <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html>`__
    """

    resource_type = "AWS::NimbleStudio::StudioComponent"

    props: PropsDictType = {
        "Configuration": (StudioComponentConfiguration, False),
        "Description": (str, False),
        "Ec2SecurityGroupIds": ([str], False),
        "InitializationScripts": ([StudioComponentInitializationScript], False),
        "Name": (str, True),
        "ScriptParameters": ([ScriptParameterKeyValue], False),
        "StudioId": (str, True),
        "Subtype": (str, False),
        "Tags": (Tags, False),
        "Type": (str, True),
    }
